"""
Fixed RAGAS evaluation script that provides more realistic evaluation scores.
This version doesn't default to "Yes" answers and uses better evaluation logic.
"""

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

import json
from datetime import datetime
import os
import logging
from typing import Dict, List, Any, Optional, Union
from datasets import Dataset, Features, Sequence, Value
import numpy as np
from ragas.metrics import (
    Faithfulness,
    AnswerRelevancy,
    ContextRelevancy,
    ContextRecall,
    ContextPrecision
)
from ragas import evaluate
from dotenv import load_dotenv
import traceback
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_core.language_models.llms import LLM
from langchain_core.outputs import Generation, LLMResult
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from pydantic import Field, BaseModel
import torch
import asyncio
from pathlib import Path
import re
import pandas as pd

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ragas_fixed_debug.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class FixedHuggingFaceLLM(LLM):
    """Fixed LLM wrapper for HuggingFace models with better evaluation logic"""
    
    model_name: str = Field(default="microsoft/phi-2")
    tokenizer: Optional[Any] = Field(default=None)
    model: Optional[Any] = Field(default=None)
    pipe: Optional[Any] = Field(default=None)
    max_length: int = Field(default=2048)
    
    class Config:
        arbitrary_types_allowed = True
    
    def __init__(self, **data):
        super().__init__(**data)
        try:
            logger.info(f"Loading model {self.model_name}...")
            self.tokenizer = AutoTokenizer.from_pretrained(
                self.model_name, 
                trust_remote_code=True,
                padding_side='left'
            )
            
            # Add pad token if it doesn't exist
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                device_map="auto" if torch.cuda.is_available() else None,
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                trust_remote_code=True
            )
            
            # Create pipeline with controlled generation parameters
            self.pipe = pipeline(
                "text-generation",
                model=self.model,
                tokenizer=self.tokenizer,
                max_new_tokens=100,  # Increased for better responses
                do_sample=True,
                temperature=0.3,  # Slightly higher for more varied responses
                pad_token_id=self.tokenizer.eos_token_id,
                eos_token_id=self.tokenizer.eos_token_id
            )
            logger.info(f"Successfully initialized model {self.model_name}")
            
        except Exception as e:
            logger.error(f"Error initializing model: {str(e)}")
            raise

    def truncate_text(self, text: str, max_tokens: int = None) -> str:
        """Truncate text to fit within token limit"""
        if max_tokens is None:
            max_tokens = self.max_length - 200
            
        tokens = self.tokenizer.encode(text)
        if len(tokens) <= max_tokens:
            return text
        
        # Truncate and decode back to text
        truncated_tokens = tokens[:max_tokens]
        truncated_text = self.tokenizer.decode(truncated_tokens, skip_special_tokens=True)
        
        logger.warning(f"Text truncated from {len(tokens)} to {len(truncated_tokens)} tokens")
        return truncated_text

    def _extract_prompt_text(self, prompt: Any) -> str:
        """Extract text from various prompt types"""
        try:
            if isinstance(prompt, str):
                return prompt
            elif isinstance(prompt, tuple) and len(prompt) == 2:
                return prompt[1] if isinstance(prompt[1], str) else str(prompt[1])
            elif isinstance(prompt, list):
                return prompt[0] if prompt and isinstance(prompt[0], str) else str(prompt[0])
            elif hasattr(prompt, 'to_string'):
                return prompt.to_string()
            elif hasattr(prompt, 'text'):
                return prompt.text
            elif hasattr(prompt, 'content'):
                return prompt.content
            elif hasattr(prompt, 'value'):
                return prompt.value
            elif hasattr(prompt, '__str__'):
                return str(prompt)
            elif hasattr(prompt, 'messages'):
                if prompt.messages:
                    return str(prompt.messages[0].content) if hasattr(prompt.messages[0], 'content') else str(prompt.messages[0])
                else:
                    return ""
            else:
                return str(prompt)
        except Exception as e:
            logger.error(f"Error extracting prompt text: {str(e)}")
            return str(prompt)

    def _clean_response(self, text: str, prompt: str = "") -> str:
        """Clean and format the model's response - FIXED VERSION"""
        try:
            # Remove the original prompt if it's included in the response
            if prompt and text.startswith(prompt):
                text = text[len(prompt):].strip()
            
            # Remove common unwanted patterns
            patterns_to_remove = [
                r'```python.*?```',
                r'```.*?```',
                r'# %%.*?\n',
                r'def .*?\n',
                r'class .*?\n',
                r'import .*?\n',
                r'from .*?\n',
                r'<\|.*?\|>',
                r'\n\n+',
            ]
            
            for pattern in patterns_to_remove:
                text = re.sub(pattern, ' ', text, flags=re.DOTALL)
            
            # Clean up whitespace
            text = ' '.join(text.split())
            
            # FIXED: Don't default to "Yes" - let the model decide
            if len(text.strip()) < 3:
                # Return a neutral response instead of defaulting to "Yes"
                return "Unable to determine."
            
            # Check if response contains evaluation keywords
            text = text.strip()
            if not any(word in text.lower() for word in ['yes', 'no', 'true', 'false', 'relevant', 'accurate', 'supported', 'unable', 'cannot']):
                # If no clear evaluation words, return neutral
                return "Unable to determine."
                
            return text
            
        except Exception as e:
            logger.error(f"Error cleaning response: {str(e)}")
            return "Unable to determine."

    def _call(
        self,
        prompt: Any,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """Generate text from the model - FIXED VERSION"""
        try:
            # Extract prompt text
            prompt_text = self._extract_prompt_text(prompt)
            
            # Truncate if too long
            prompt_text = self.truncate_text(prompt_text)
            
            logger.debug(f"Processing prompt: {prompt_text[:100]}...")
            
            # Create better evaluation prompts
            if "faithfulness" in prompt_text.lower() or "supported" in prompt_text.lower():
                eval_prompt = f"""Evaluate if the answer is supported by the context. 
Question: {prompt_text.split('Question:')[1].split('Answer:')[0].strip()}
Answer: {prompt_text.split('Answer:')[1].split('Context:')[0].strip()}
Context: {prompt_text.split('Context:')[1].strip()}

Is the answer supported by the context? Answer with 'Yes', 'No', or 'Partially' and explain why:"""
            elif "relevancy" in prompt_text.lower():
                eval_prompt = f"""Evaluate if this is relevant. 
Question: {prompt_text.split('Question:')[1].split('Answer:')[0].strip()}
Answer: {prompt_text.split('Answer:')[1].strip()}

Is the answer relevant to the question? Answer with 'Yes', 'No', or 'Partially' and explain why:"""
            elif "recall" in prompt_text.lower():
                eval_prompt = f"""Evaluate if the context contains necessary information. 
Question: {prompt_text.split('Question:')[1].split('Context:')[0].strip()}
Context: {prompt_text.split('Context:')[1].split('Ground Truth:')[0].strip()}
Ground Truth: {prompt_text.split('Ground Truth:')[1].strip()}

Does the context contain information to answer the question? Answer with 'Yes', 'No', or 'Partially' and explain why:"""
            else:
                eval_prompt = f"Evaluate this content. Provide a brief assessment.\n\n{prompt_text}\n\nEvaluation:"
            
            # Truncate the evaluation prompt
            eval_prompt = self.truncate_text(eval_prompt)
            
            # Generate response
            response = self.pipe(
                eval_prompt,
                max_new_tokens=100,
                num_return_sequences=1,
                pad_token_id=self.tokenizer.eos_token_id,
                do_sample=True,
                temperature=0.3
            )
            
            # Extract and clean the generated text
            generated_text = response[0]['generated_text']
            cleaned_text = self._clean_response(generated_text, eval_prompt)
            
            logger.debug(f"Generated response: {cleaned_text}")
            return cleaned_text
            
        except Exception as e:
            logger.error(f"Error generating text: {str(e)}")
            return "Unable to determine."

    def _score_response(self, response: str) -> float:
        """Score a response based on its content"""
        response_lower = response.lower()
        
        # Positive indicators
        if any(word in response_lower for word in ['yes', 'true', 'supported', 'relevant', 'accurate']):
            return 1.0
        # Negative indicators
        elif any(word in response_lower for word in ['no', 'false', 'not supported', 'not relevant', 'inaccurate']):
            return 0.0
        # Partial indicators
        elif any(word in response_lower for word in ['partially', 'somewhat', 'limited']):
            return 0.5
        # Unable to determine
        elif any(word in response_lower for word in ['unable', 'cannot', 'determine']):
            return 0.3  # Neutral score instead of 0
        else:
            return 0.5  # Neutral score for unclear responses

    async def agenerate(
        self,
        prompts: Union[List[str], List[Any]],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> LLMResult:
        """Async generate method that RAGAS expects"""
        try:
            logger.debug(f"Async generate called")
            
            if not isinstance(prompts, list):
                prompts = [prompts]
            
            generations = []
            for prompt in prompts:
                try:
                    response = self._call(prompt, stop, run_manager, **kwargs)
                    generations.append([Generation(text=response)])
                except Exception as e:
                    logger.error(f"Error processing individual prompt: {str(e)}")
                    generations.append([Generation(text="Unable to determine.")])
            
            return LLMResult(generations=generations)
            
        except Exception as e:
            logger.error(f"Error in agenerate: {str(e)}")
            try:
                num_prompts = len(prompts) if hasattr(prompts, '__len__') else 1
            except:
                num_prompts = 1
            default_generations = [[Generation(text="Unable to determine.")] for _ in range(num_prompts)]
            return LLMResult(generations=default_generations)

    def generate(
        self,
        prompts: Union[List[str], List[Any]],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> LLMResult:
        """Synchronous generate method"""
        try:
            logger.debug(f"Generate called with prompts of type: {type(prompts)}")
            
            if not isinstance(prompts, list):
                prompts = [prompts]
            
            generations = []
            for prompt in prompts:
                try:
                    response = self._call(prompt, stop, run_manager, **kwargs)
                    generations.append([Generation(text=response)])
                except Exception as e:
                    logger.error(f"Error processing prompt: {str(e)}")
                    generations.append([Generation(text="Unable to determine.")])
            
            return LLMResult(generations=generations)
            
        except Exception as e:
            logger.error(f"Error in generate: {str(e)}")
            try:
                num_prompts = len(prompts) if hasattr(prompts, '__len__') else 1
            except:
                num_prompts = 1
            default_generations = [[Generation(text="Unable to determine.")] for _ in range(num_prompts)]
            return LLMResult(generations=default_generations)
    
    @property
    def _llm_type(self) -> str:
        return "fixed_huggingface"

class FixedRAGASEvaluator:
    """Fixed RAGAS evaluator with better evaluation logic"""
    
    def __init__(self, model_name: str = "microsoft/phi-2"):
        self.model_name = model_name
        self.llm = FixedHuggingFaceLLM(model_name=model_name)
        
    def prepare_dataset(self, evaluation_data: List[Dict[str, Any]]) -> Dataset:
        """Prepare the dataset in the correct format for RAGAS"""
        try:
            data = {
                'question': [],
                'contexts': [],
                'answer': [],
                'ground_truth': []
            }
            
            for item in evaluation_data:
                data['question'].append(str(item['question']))
                contexts = item['contexts']
                if isinstance(contexts, str):
                    contexts = [contexts]
                elif not isinstance(contexts, list):
                    contexts = [str(contexts)]
                data['contexts'].append([str(ctx) for ctx in contexts])
                data['answer'].append(str(item['answer']))
                data['ground_truth'].append(str(item.get('ground_truth', '')))
            
            features = Features({
                'question': Value('string'),
                'contexts': Sequence(Value('string')),
                'answer': Value('string'),
                'ground_truth': Value('string')
            })
            
            dataset = Dataset.from_dict(data, features=features)
            logger.info(f"Created dataset with {len(dataset)} examples")
            return dataset
            
        except Exception as e:
            logger.error(f"Error preparing dataset: {str(e)}")
            raise

    def calculate_metrics_manually(self, dataset: Dataset) -> Dict[str, float]:
        """Calculate metrics manually with better logic"""
        try:
            metrics = {}
            
            # Calculate each metric
            metrics['faithfulness'] = self._calculate_faithfulness(dataset)
            metrics['answer_relevancy'] = self._calculate_answer_relevancy(dataset)
            metrics['context_relevancy'] = self._calculate_context_relevancy(dataset)
            metrics['context_recall'] = self._calculate_context_recall(dataset)
            metrics['context_precision'] = self._calculate_context_precision(dataset)
            
            # Calculate average
            valid_scores = [score for score in metrics.values() if score is not None]
            metrics['average_score'] = np.mean(valid_scores) if valid_scores else 0.0
            
            return metrics
            
        except Exception as e:
            logger.error(f"Error calculating metrics: {str(e)}")
            return {
                'faithfulness': 0.0,
                'answer_relevancy': 0.0,
                'context_relevancy': 0.0,
                'context_recall': 0.0,
                'context_precision': 0.0,
                'average_score': 0.0
            }

    def _calculate_faithfulness(self, dataset: Dataset) -> float:
        """Calculate faithfulness with better logic"""
        scores = []
        for i in range(len(dataset)):
            question = dataset[i]['question']
            answer = dataset[i]['answer']
            contexts = dataset[i]['contexts']
            
            context_text = ' '.join(contexts)
            prompt = f"Question: {question}\nAnswer: {answer}\nContext: {context_text}\n\nIs the answer supported by the context? Answer with 'Yes', 'No', or 'Partially' and explain why:"
            
            response = self.llm._call(prompt)
            score = self.llm._score_response(response)
            scores.append(score)
            
            logger.debug(f"Faithfulness - Q: {question[:50]}... Score: {score:.3f}")
        
        return np.mean(scores)

    def _calculate_answer_relevancy(self, dataset: Dataset) -> float:
        """Calculate answer relevancy with better logic"""
        scores = []
        for i in range(len(dataset)):
            question = dataset[i]['question']
            answer = dataset[i]['answer']
            
            prompt = f"Question: {question}\nAnswer: {answer}\n\nIs the answer relevant to the question? Answer with 'Yes', 'No', or 'Partially' and explain why:"
            
            response = self.llm._call(prompt)
            score = self.llm._score_response(response)
            scores.append(score)
            
            logger.debug(f"Answer Relevancy - Q: {question[:50]}... Score: {score:.3f}")
        
        return np.mean(scores)

    def _calculate_context_relevancy(self, dataset: Dataset) -> float:
        """Calculate context relevancy with better logic"""
        scores = []
        for i in range(len(dataset)):
            question = dataset[i]['question']
            contexts = dataset[i]['contexts']
            
            context_text = ' '.join(contexts)
            prompt = f"Question: {question}\nContext: {context_text}\n\nIs the context relevant to the question? Answer with 'Yes', 'No', or 'Partially' and explain why:"
            
            response = self.llm._call(prompt)
            score = self.llm._score_response(response)
            scores.append(score)
            
            logger.debug(f"Context Relevancy - Q: {question[:50]}... Score: {score:.3f}")
        
        return np.mean(scores)

    def _calculate_context_recall(self, dataset: Dataset) -> float:
        """Calculate context recall with better logic"""
        scores = []
        for i in range(len(dataset)):
            question = dataset[i]['question']
            contexts = dataset[i]['contexts']
            ground_truth = dataset[i].get('ground_truth', '')
            
            context_text = ' '.join(contexts)
            prompt = f"Question: {question}\nContext: {context_text}\nGround Truth: {ground_truth}\n\nDoes the context contain the necessary information to answer the question? Answer with 'Yes', 'No', or 'Partially' and explain why:"
            
            response = self.llm._call(prompt)
            score = self.llm._score_response(response)
            scores.append(score)
            
            logger.debug(f"Context Recall - Q: {question[:50]}... Score: {score:.3f}")
        
        return np.mean(scores)

    def _calculate_context_precision(self, dataset: Dataset) -> float:
        """Calculate context precision with better logic"""
        scores = []
        for i in range(len(dataset)):
            question = dataset[i]['question']
            contexts = dataset[i]['contexts']
            
            context_text = ' '.join(contexts)
            prompt = f"Question: {question}\nContext: {context_text}\n\nIs the context precise and focused on the question? Answer with 'Yes', 'No', or 'Partially' and explain why:"
            
            response = self.llm._call(prompt)
            score = self.llm._score_response(response)
            scores.append(score)
            
            logger.debug(f"Context Precision - Q: {question[:50]}... Score: {score:.3f}")
        
        return np.mean(scores)

    def evaluate(self, evaluation_data: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Run the fixed evaluation process"""
        try:
            if evaluation_data is None:
                logger.error("No evaluation data provided")
                return None
            
            logger.info("Starting FIXED RAGAS evaluation...")
            print("\nDataset Details:")
            print("=" * 50)
            print(f"Number of examples: {len(evaluation_data)}")
            
            # Show sample data
            for i, item in enumerate(evaluation_data[:2]):
                print(f"\nExample {i+1}:")
                print(f"Question: {item['question']}")
                print(f"Answer: {item['answer']}")
                print(f"Contexts: {item['contexts']}")
                print(f"Ground Truth: {item['ground_truth']}")
            print("=" * 50)
            
            # Prepare dataset
            dataset = self.prepare_dataset(evaluation_data)
            
            # Calculate metrics using fixed logic
            logger.info("Calculating RAGAS metrics with FIXED logic...")
            metrics = self.calculate_metrics_manually(dataset)
            
            # Prepare results
            results = {
                'metrics': metrics,
                'evaluation_data': evaluation_data,
                'timestamp': datetime.now().isoformat(),
                'model_name': self.model_name,
                'dataset_size': len(evaluation_data),
                'evaluation_method': 'fixed_manual'
            }
            
            # Save results
            self.save_results(results)
            
            return results
            
        except Exception as e:
            error_msg = f"Error in fixed evaluation: {str(e)}"
            logger.error(error_msg)
            logger.error(traceback.format_exc())
            
            return {
                'metrics': {
                    'faithfulness': 0.0,
                    'answer_relevancy': 0.0,
                    'context_relevancy': 0.0,
                    'context_recall': 0.0,
                    'context_precision': 0.0,
                    'average_score': 0.0
                },
                'evaluation_data': evaluation_data or [],
                'timestamp': datetime.now().isoformat(),
                'error': str(e),
                'evaluation_method': 'fixed_manual'
            }
    
    def save_results(self, results: Dict[str, Any]):
        """Save evaluation results to file"""
        try:
            results_dir = "fixed_evaluation_results"
            os.makedirs(results_dir, exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(results_dir, f"fixed_ragas_evaluation_{timestamp}.json")
            
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2, default=str)
            
            logger.info(f"Fixed results saved to {output_file}")
            
            print("\n" + "="*60)
            print("FIXED RAGAS EVALUATION RESULTS SUMMARY")
            print("="*60)
            print(f"Model: {results.get('model_name', 'Unknown')}")
            print(f"Timestamp: {results['timestamp']}")
            print(f"Number of examples evaluated: {results.get('dataset_size', 0)}")
            print(f"Evaluation Method: {results.get('evaluation_method', 'Unknown')}")
            print("\nMetric Scores:")
            print("-" * 30)
            
            for metric_name, score in results['metrics'].items():
                if metric_name != 'average_score':
                    print(f"{metric_name.replace('_', ' ').title()}: {score:.3f}")
            
            print("-" * 30)
            print(f"Average Score: {results['metrics']['average_score']:.3f}")
            print("="*60)
            
        except Exception as e:
            logger.error(f"Error saving results: {str(e)}")

def main():
    """Main execution function for fixed evaluation"""
    try:
        model_name = "microsoft/phi-2"
        print(f"Initializing FIXED RAGAS evaluator with model: {model_name}")
        evaluator = FixedRAGASEvaluator(model_name=model_name)

        # Load evaluation dataset
        sample_file = 'SAMPLE_EVALUATION_DATASET.csv'
        evaluation_data = None
        if os.path.exists(sample_file):
            print(f"Loading evaluation data from {sample_file}...")
            df = pd.read_csv(sample_file)
            
            # Initialize RAG system to get real answers
            try:
                from rag_system import RAGSystem
                print("Initializing RAG system...")
                rag_system = RAGSystem()
                print("RAG system initialized successfully!")
            except Exception as e:
                print(f"Warning: Could not initialize RAG system: {e}")
                print("Using ground truth as answers")
                rag_system = None
            
            # Convert DataFrame to evaluation format
            evaluation_data = []
            for idx, row in df.iterrows():
                question = row['question']
                ground_truth = row['ground_truth_answer']
                source = row['source']
                
                print(f"Processing question {idx+1}: {question}")
                
                if rag_system:
                    try:
                        # Get real answer and context from RAG system
                        response = rag_system.query(question)
                        chatbot_answer = response['answer']
                        retrieved_contexts = [source['snippet'] for source in response['sources']]
                        
                        # Truncate long contexts
                        max_context_length = 500
                        truncated_contexts = []
                        for ctx in retrieved_contexts:
                            if len(ctx) > max_context_length:
                                truncated_contexts.append(ctx[:max_context_length] + "...")
                            else:
                                truncated_contexts.append(ctx)
                        
                        print(f"Chatbot answer: {chatbot_answer[:100]}...")
                        print(f"Retrieved contexts: {len(truncated_contexts)} contexts")
                        
                        evaluation_data.append({
                            'question': question,
                            'answer': chatbot_answer,
                            'contexts': truncated_contexts,
                            'ground_truth': ground_truth,
                            'source': source
                        })
                    except Exception as e:
                        print(f"Error getting answer for question {idx+1}: {e}")
                        evaluation_data.append({
                            'question': question,
                            'answer': ground_truth,
                            'contexts': [str(ground_truth)],
                            'ground_truth': ground_truth,
                            'source': source
                        })
                else:
                    evaluation_data.append({
                        'question': question,
                        'answer': ground_truth,
                        'contexts': [str(ground_truth)],
                        'ground_truth': ground_truth,
                        'source': source
                    })
        else:
            print("No SAMPLE_EVALUATION_DATASET.csv found.")

        print("Starting FIXED evaluation...")
        results = evaluator.evaluate(evaluation_data)

        if 'error' in results:
            print(f"Fixed evaluation completed with errors. Check logs for details.")
        else:
            print("Fixed evaluation completed successfully!")

    except Exception as e:
        logger.error(f"Error in main: {str(e)}")
        print(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main() 