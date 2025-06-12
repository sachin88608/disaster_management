from groq import Groq
from typing import List, Dict, Any, Optional
import logging
from config import Config

logger = logging.getLogger(__name__)

class LLMInterface:
    """Interface for GROQ LLM integration"""
    
    def __init__(self):
        self.config = Config()
        
        if not self.config.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        
        self.client = Groq(api_key=self.config.GROQ_API_KEY)
        self.model = self.config.GROQ_MODEL
        
        logger.info(f"Initialized GROQ client with model: {self.model}")
    
    def create_prompt(self, question: str, context_docs: List[Dict[str, Any]]) -> str:
        """Create a prompt for the LLM with context"""
        
        if not context_docs:
            return f"""
You are a helpful assistant specialized in disaster management and emergency response. 
Answer the following question based on your knowledge:

Question: {question}

Please provide a clear, accurate, and helpful response.
"""
        
        # Build context from retrieved documents
        context_parts = []
        for i, doc in enumerate(context_docs, 1):
            metadata = doc.get('metadata', {})
            source = metadata.get('source', 'Unknown')
            doc_type = metadata.get('type', 'Unknown')
            
            context_part = f"Document {i} (Source: {source}, Type: {doc_type}):\n{doc['content']}\n"
            context_parts.append(context_part)
        
        context = "\n".join(context_parts)
        
        prompt = f"""
You are a helpful assistant specialized in disaster management and emergency response. 
Use the following context documents to answer the question. If the context doesn't contain 
enough information to fully answer the question, you can supplement with your general knowledge 
but clearly indicate what comes from the provided context vs. your general knowledge.

Context Documents:
{context}

Question: {question}

Instructions:
1. Answer based primarily on the provided context
2. Be specific and cite relevant information from the documents
3. If using general knowledge, clearly indicate this
4. Provide actionable advice when appropriate
5. Keep your response clear and well-structured

Answer:
"""
        return prompt
    
    def generate_response(self, question: str, context_docs: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Generate response using GROQ LLM"""
        try:
            if context_docs is None:
                context_docs = []
            
            prompt = self.create_prompt(question, context_docs)
            
            # Call GROQ API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a knowledgeable assistant specializing in disaster management, emergency response, and related topics. Provide accurate, helpful, and actionable information."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=1024,
                top_p=1,
                stop=None
            )
            
            answer = response.choices[0].message.content
            
            # Calculate tokens used
            prompt_tokens = response.usage.prompt_tokens
            completion_tokens = response.usage.completion_tokens
            total_tokens = response.usage.total_tokens
            
            return {
                'answer': answer,
                'model': self.model,
                'context_used': len(context_docs),
                'tokens': {
                    'prompt': prompt_tokens,
                    'completion': completion_tokens,
                    'total': total_tokens
                }
            }
            
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return {
                'answer': f"Sorry, I encountered an error while generating the response: {str(e)}",
                'model': self.model,
                'context_used': 0,
                'tokens': {'prompt': 0, 'completion': 0, 'total': 0}
            }
    
    def get_available_models(self) -> List[str]:
        """Get list of available GROQ models"""
        return [
            "llama3-70b-8192",
            "mixtral-8x7b-32768",
            "llama2-13b-4096"
        ]
    
    def switch_model(self, model_name: str) -> bool:
        """Switch to a different GROQ model"""
        if model_name in self.get_available_models():
            self.model = model_name
            logger.info(f"Switched to model: {model_name}")
            return True
        else:
            logger.error(f"Model {model_name} not available")
            return False