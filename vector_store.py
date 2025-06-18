import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Dict, Any, Optional
import logging
import uuid
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import Config
import os
import multiprocessing
from functools import partial
from tqdm import tqdm

logger = logging.getLogger(__name__)

def process_chunk_batch(chunk_batch: List[str], model_name: str) -> List[List[float]]:
    """Process a batch of chunks in parallel"""
    try:
        # Initialize model for this process
        model = SentenceTransformer(model_name)
        # Create embeddings
        embeddings = model.encode(chunk_batch, show_progress_bar=False)
        return embeddings.tolist()
    except Exception as e:
        logger.error(f"Error in parallel processing: {str(e)}")
        return []

class VectorStore:
    """Manages the ChromaDB vector store with embeddings"""
    
    def __init__(self):
        self.config = Config()
        self.embedding_model = SentenceTransformer(self.config.EMBEDDING_MODEL)
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.config.CHUNK_SIZE,
            chunk_overlap=self.config.CHUNK_OVERLAP,
            length_function=len,
        )
        
        # Create directory if it doesn't exist
        os.makedirs(self.config.CHROMA_PERSIST_DIR, exist_ok=True)
        
        # Initialize ChromaDB
        self.client = chromadb.PersistentClient(
            path=self.config.CHROMA_PERSIST_DIR
        )
        
        # Get or create collection
        try:
            self.collection = self.client.get_collection(
                name=self.config.COLLECTION_NAME
            )
            logger.info(f"Loaded existing collection: {self.config.COLLECTION_NAME}")
        except Exception as e:
            logger.warning(f"Collection not found, creating new one: {str(e)}")
            try:
                self.collection = self.client.create_collection(
                    name=self.config.COLLECTION_NAME,
                    metadata={"hnsw:space": "cosine"}  # Use cosine similarity
                )
                logger.info(f"Created new collection: {self.config.COLLECTION_NAME}")
            except Exception as e:
                logger.error(f"Failed to create collection: {str(e)}")
                raise
    
    def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Create embeddings for a list of texts"""
        try:
            embeddings = self.embedding_model.encode(texts, show_progress_bar=True)
            return embeddings.tolist()
        except Exception as e:
            logger.error(f"Error creating embeddings: {str(e)}")
            return []
    
    def chunk_documents(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Split documents into chunks"""
        chunked_docs = []
        
        for doc in documents:
            chunks = self.text_splitter.split_text(doc['content'])
            
            for i, chunk in enumerate(chunks):
                chunked_doc = doc.copy()
                chunked_doc['content'] = chunk
                chunked_doc['chunk_id'] = i
                chunked_doc['total_chunks'] = len(chunks)
                chunked_docs.append(chunked_doc)
        
        logger.info(f"Created {len(chunked_docs)} chunks from {len(documents)} documents")
        return chunked_docs
    
    def process_chunk_batch(self, chunk_batch: List[Dict[str, Any]]) -> bool:
        """Process a single batch of chunks"""
        try:
            # Prepare data for ChromaDB
            texts = [doc['content'] for doc in chunk_batch]
            embeddings = self.create_embeddings(texts)
            
            if not embeddings:
                logger.error("Failed to create embeddings for chunk batch")
                return False
            
            # Create unique IDs
            ids = [str(uuid.uuid4()) for _ in range(len(chunk_batch))]
            
            # Prepare metadata
            metadatas = []
            for doc in chunk_batch:
                metadata = {
                    'source': doc['source'],
                    'type': doc['type'],
                    'chunk_id': doc.get('chunk_id', 0),
                    'total_chunks': doc.get('total_chunks', 1)
                }
                
                # Add specific metadata based on document type
                if doc['type'] == 'pdf':
                    metadata['page'] = doc.get('page', 1)
                elif doc['type'] in ['csv', 'excel']:
                    metadata['row'] = doc.get('row', 1)
                    if 'sheet' in doc:
                        metadata['sheet'] = doc['sheet']
                
                metadatas.append(metadata)
            
            # Add to ChromaDB
            self.collection.add(
                documents=texts,
                embeddings=embeddings,
                metadatas=metadatas,
                ids=ids
            )
            return True
            
        except Exception as e:
            logger.error(f"Error processing chunk batch: {str(e)}")
            return False

    def create_embeddings_parallel(self, texts: List[str], batch_size: int = 100) -> List[List[float]]:
        """Create embeddings in parallel using multiple CPU cores"""
        try:
            # Determine number of CPU cores to use (leave one core free for system)
            num_cores = max(1, multiprocessing.cpu_count() - 1)
            logger.info(f"Using {num_cores} CPU cores for parallel processing")
            
            # Split texts into batches
            text_batches = [texts[i:i + batch_size] for i in range(0, len(texts), batch_size)]
            total_batches = len(text_batches)
            
            # Create a pool of workers
            with multiprocessing.Pool(processes=num_cores) as pool:
                # Create partial function with model name
                process_func = partial(process_chunk_batch, model_name=self.config.EMBEDDING_MODEL)
                
                # Process batches in parallel with progress bar
                results = []
                with tqdm(total=total_batches, desc="Creating embeddings") as pbar:
                    for result in pool.imap_unordered(process_func, text_batches):
                        results.append(result)
                        pbar.update(1)
                        # Log progress percentage
                        progress = (len(results) / total_batches) * 100
                        logger.info(f"Embedding progress: {progress:.1f}%")
            
            # Flatten results
            all_embeddings = [emb for batch_embeddings in results for emb in batch_embeddings]
            
            return all_embeddings
            
        except Exception as e:
            logger.error(f"Error in parallel embedding creation: {str(e)}")
            return []

    def add_documents(self, documents: List[Dict[str, Any]]) -> bool:
        """Add documents to the vector store"""
        try:
            if not documents:
                logger.warning("No documents to add")
                return False
            
            # Process documents in batches
            BATCH_SIZE = 5000  # Slightly smaller than ChromaDB's limit for safety
            CHUNK_BATCH_SIZE = 1000  # Process chunks in smaller batches
            total_docs = len(documents)
            total_chunks_processed = 0
            success = True
            
            logger.info(f"Starting to process {total_docs} documents")
            
            for i in range(0, total_docs, BATCH_SIZE):
                batch_docs = documents[i:i + BATCH_SIZE]
                logger.info(f"Processing document batch {i//BATCH_SIZE + 1} of {(total_docs + BATCH_SIZE - 1)//BATCH_SIZE}")
                
                # Process documents and their chunks in smaller batches
                current_chunk_batch = []
                all_chunks = []
                
                for doc in batch_docs:
                    chunks = self.text_splitter.split_text(doc['content'])
                    for j, chunk in enumerate(chunks):
                        chunked_doc = doc.copy()
                        chunked_doc['content'] = chunk
                        chunked_doc['chunk_id'] = j
                        chunked_doc['total_chunks'] = len(chunks)
                        current_chunk_batch.append(chunked_doc)
                        all_chunks.append(chunk)
                
                # Create embeddings in parallel
                embeddings = self.create_embeddings_parallel(all_chunks)
                
                if not embeddings:
                    logger.error("Failed to create embeddings")
                    success = False
                    continue
                
                # Process chunks in batches
                for j in range(0, len(current_chunk_batch), CHUNK_BATCH_SIZE):
                    chunk_batch = current_chunk_batch[j:j + CHUNK_BATCH_SIZE]
                    batch_embeddings = embeddings[j:j + CHUNK_BATCH_SIZE]
                    
                    try:
                        # Create unique IDs
                        ids = [str(uuid.uuid4()) for _ in range(len(chunk_batch))]
                        
                        # Prepare metadata
                        metadatas = []
                        for doc in chunk_batch:
                            metadata = {
                                'source': doc['source'],
                                'type': doc['type'],
                                'chunk_id': doc.get('chunk_id', 0),
                                'total_chunks': doc.get('total_chunks', 1)
                            }
                            
                            # Add specific metadata based on document type
                            if doc['type'] == 'pdf':
                                metadata['page'] = doc.get('page', 1)
                            elif doc['type'] in ['csv', 'excel']:
                                metadata['row'] = doc.get('row', 1)
                                if 'sheet' in doc:
                                    metadata['sheet'] = doc['sheet']
                            
                            metadatas.append(metadata)
                        
                        # Add to ChromaDB
                        self.collection.add(
                            documents=[doc['content'] for doc in chunk_batch],
                            embeddings=batch_embeddings,
                            metadatas=metadatas,
                            ids=ids
                        )
                        
                        total_chunks_processed += len(chunk_batch)
                        logger.info(f"Processed {total_chunks_processed} chunks so far")
                        
                    except Exception as e:
                        logger.error(f"Error adding chunk batch to vector store: {str(e)}")
                        success = False
            
            logger.info(f"Completed processing {total_docs} documents into {total_chunks_processed} chunks")
            return success
            
        except Exception as e:
            logger.error(f"Error in add_documents: {str(e)}")
            return False
    
    def similarity_search(self, query: str, k: int = None) -> List[Dict[str, Any]]:
        """Search for similar documents using cosine similarity"""
        try:
            if k is None:
                k = self.config.TOP_K_RESULTS
            
            # Create query embedding
            query_embedding = self.embedding_model.encode([query])[0].tolist()
            
            # Search in ChromaDB
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=k,
                include=['documents', 'metadatas', 'distances']
            )
            
            # Format results
            formatted_results = []
            for i in range(len(results['documents'][0])):
                result = {
                    'content': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i],
                    'similarity_score': 1 - results['distances'][0][i],  # Convert distance to similarity
                }
                
                # Only include results above similarity threshold
                if result['similarity_score'] >= self.config.SIMILARITY_THRESHOLD:
                    formatted_results.append(result)
            
            logger.info(f"Found {len(formatted_results)} relevant documents for query")
            return formatted_results
            
        except Exception as e:
            logger.error(f"Error in similarity search: {str(e)}")
            return []
    
    def get_collection_stats(self) -> Dict[str, Any]:
        """Get statistics about the collection"""
        try:
            count = self.collection.count()
            return {
                'total_documents': count,
                'collection_name': self.config.COLLECTION_NAME,
                'embedding_model': self.config.EMBEDDING_MODEL
            }
        except Exception as e:
            logger.error(f"Error getting collection stats: {str(e)}")
            return {}
    
    def reset_collection(self) -> bool:
        """Reset the collection (delete all documents)"""
        try:
            self.client.delete_collection(self.config.COLLECTION_NAME)
            self.collection = self.client.create_collection(
                name=self.config.COLLECTION_NAME,
                metadata={"hnsw:space": "cosine"}
            )
            logger.info("Collection reset successfully")
            return True
        except Exception as e:
            logger.error(f"Error resetting collection: {str(e)}")
            return False

    def get_existing_sources(self) -> List[str]:
        """Get list of existing sources in the vector store"""
        try:
            # Get all documents from the collection
            results = self.collection.get()
            
            # Extract unique sources from metadata
            existing_sources = set()
            if results and results['metadatas']:
                for metadata in results['metadatas']:
                    if 'source' in metadata:
                        existing_sources.add(metadata['source'])
            
            return list(existing_sources)
            
        except Exception as e:
            logger.error(f"Error getting existing sources: {str(e)}")
            return []