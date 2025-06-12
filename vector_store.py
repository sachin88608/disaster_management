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

logger = logging.getLogger(__name__)

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
        except:
            self.collection = self.client.create_collection(
                name=self.config.COLLECTION_NAME,
                metadata={"hnsw:space": "cosine"}  # Use cosine similarity
            )
            logger.info(f"Created new collection: {self.config.COLLECTION_NAME}")
    
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
    
    def add_documents(self, documents: List[Dict[str, Any]]) -> bool:
        """Add documents to the vector store"""
        try:
            if not documents:
                logger.warning("No documents to add")
                return False
            
            # Chunk documents
            chunked_docs = self.chunk_documents(documents)
            
            # Prepare data for ChromaDB
            texts = [doc['content'] for doc in chunked_docs]
            embeddings = self.create_embeddings(texts)
            
            if not embeddings:
                logger.error("Failed to create embeddings")
                return False
            
            # Create unique IDs
            ids = [str(uuid.uuid4()) for _ in range(len(chunked_docs))]
            
            # Prepare metadata
            metadatas = []
            for doc in chunked_docs:
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
            
            logger.info(f"Added {len(chunked_docs)} document chunks to vector store")
            return True
            
        except Exception as e:
            logger.error(f"Error adding documents to vector store: {str(e)}")
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