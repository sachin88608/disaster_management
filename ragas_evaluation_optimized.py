#!/usr/bin/env python3
"""
OPTIMIZED RAGAS evaluation script for assessing RAG system performance.
This script uses batch processing and parallel execution to maximize GPU efficiency.

Key optimizations:
- Batch processing instead of sequential
- Parallel metric calculation
- Optimized GPU memory usage
- Reduced redundant model calls
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
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ragas_optimized.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class OptimizedHuggingFaceLLM(LLM):
    """Optimized LLM wrapper for HuggingFace models with batch processing"""
    
    model_name: str = Field(default="mistralai/Mistral-7B-Instruct-v0.2")
    tokenizer: Optional[Any] = Field(default=None)
    model: Optional[Any] = Field(default=None)
    pipe: Optional[Any] = Field(default=None)
    max_length: int = Field(default=4096)  # Increased token limit
    batch_size: int = Field(default=4)  # Batch size for processing
    
    class Config:
        arbitrary_types_allowed = True
    
    def __init__(self, **data):
        super().__init__(**data)
        try:
            logger.info(f"Loading optimized model {self.model_name}...")
            self.tokenizer = AutoTokenizer.from_pretrained(
                self.model_name, 
                trust_remote_code=True,
                padding_side='left'
            )
            
            # Add pad token if it doesn't exist
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            
            # Optimized model loading with better memory management
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                device_map="auto",
                torch_dtype=torch.float16,  # Use half precision for speed
                trust_remote_code=True,
                low_cpu_mem_usage=True
            )
            
            # Create optimized pipeline with batch processing
            self.pipe = pipeline(
                "text-generation",
                model=self.model,
                tokenizer=self.tokenizer,
                device=0,  # Use GPU
                max_new_tokens=50,  # Reduced for faster generation
                do_sample=True,
                temperature=0.1,  # Lower temperature for more consistent results
                pad_token_id=self.tokenizer.eos_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
                batch_size=self.batch_size,  # Enable batch processing
                return_full_text=False  # Only return generated text
            )
            logger.info(f"Successfully initialized optimized model {self.model_name}")
            
        except Exception as e:
            logger.error(f"Error initializing optimized model: {str(e)}")
            raise

    def batch_generate(self, prompts: List[str]) -> List[str]:
        """Generate responses for multiple prompts in batch"""
        try:
            if not prompts:
                return []
            
            # Prepare prompts for batch processing
            formatted_prompts = []
            for prompt in prompts:
                # Create focused evaluation prompts
                if "faithfulness" in prompt.lower() or "supported" in prompt.lower():
                    eval_prompt = f"Evaluate if the answer is supported by the context. Answer with 'Yes' or 'No' and brief explanation.\n\n{prompt}\n\nEvaluation:"
                elif "relevancy" in prompt.lower():
                    eval_prompt = f"Evaluate if this is relevant. Answer with 'Yes' or 'No' and brief explanation.\n\n{prompt}\n\nEvaluation:"
                else:
                    eval_prompt = f"Evaluate this content. Provide a brief assessment.\n\n{prompt}\n\nEvaluation:"
                
                # Truncate if too long
                eval_prompt = self.truncate_text(eval_prompt)
                formatted_prompts.append(eval_prompt)
            
            # Process in batches
            all_responses = []
            for i in range(0, len(formatted_prompts), self.batch_size):
                batch_prompts = formatted_prompts[i:i + self.batch_size]
                
                # Generate responses for the batch
                responses = self.pipe(
                    batch_prompts,
                    max_new_tokens=50,
                    num_return_sequences=1,
                    pad_token_id=self.tokenizer.eos_token_id,
                    do_sample=True,
                    temperature=0.1
                )
                
                # Extract and clean responses
                batch_responses = []
                for j, response in enumerate(responses):
                    generated_text = response[0]['generated_text']
                    cleaned_text = self._clean_response(generated_text, batch_prompts[j])
                    batch_responses.append(cleaned_text)
                
                all_responses.extend(batch_responses)
            
            return all_responses
            
        except Exception as e:
            logger.error(f"Error in batch generation: {str(e)}")
            return ["Unable to determine."] * len(prompts)

    def truncate_text(self, text: str, max_tokens: int = None) -> str:
        """Truncate text to fit within token limit"""
        if max_tokens is None:
            max_tokens = self.max_length - 100
            
        tokens = self.tokenizer.encode(text)
        if len(tokens) <= max_tokens:
            return text
        
        truncated_tokens = tokens[:max_tokens]
        truncated_text = self.tokenizer.decode(truncated_tokens, skip_special_tokens=True)
        
        logger.warning(f"Text truncated from {len(tokens)} to {len(truncated_tokens)} tokens")
        return truncated_text

    def _clean_response(self, text: str, prompt: str = "") -> str:
        """Clean and format the model's response"""
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
            
            if len(text.strip()) < 3:
                return "Unable to determine."
            
            text = text.strip()
            if not any(word in text.lower() for word in ['yes', 'no', 'true', 'false', 'relevant', 'accurate', 'supported', 'unable', 'cannot']):
                return "Unable to determine."
                
            return text
            
        except Exception as e:
            logger.error(f"Error cleaning response: {str(e)}")
            return "Unable to determine."

    def _call(self, prompt: Any, stop: Optional[List[str]] = None, run_manager: Optional[CallbackManagerForLLMRun] = None, **kwargs: Any) -> str:
        """Single prompt generation (for compatibility)"""
        responses = self.batch_generate([str(prompt)])
        return responses[0] if responses else "Unable to determine."

    async def agenerate(self, prompts: Union[List[str], List[Any]], stop: Optional[List[str]] = None, run_manager: Optional[CallbackManagerForLLMRun] = None, **kwargs: Any) -> LLMResult:
        """Async generate method that RAGAS expects"""
        try:
            if not isinstance(prompts, list):
                prompts = [prompts]
            
            # Extract prompt texts
            prompt_texts = [str(prompt) for prompt in prompts]
            
            # Use batch generation
            responses = self.batch_generate(prompt_texts)
            
            # Create LLMResult
            generations = [[Generation(text=response)] for response in responses]
            return LLMResult(generations=generations)
            
        except Exception as e:
            logger.error(f"Error in async generate: {str(e)}")
            return LLMResult(generations=[[Generation(text="Unable to determine.")] for _ in prompts])

    def generate(self, prompts: Union[List[str], List[Any]], stop: Optional[List[str]] = None, run_manager: Optional[CallbackManagerForLLMRun] = None, **kwargs: Any) -> LLMResult:
        """Synchronous generate method"""
        return asyncio.run(self.agenerate(prompts, stop, run_manager, **kwargs))

    @property
    def _llm_type(self) -> str:
        return "optimized_huggingface"

class OptimizedRAGASEvaluator:
    """Optimized RAGAS evaluator with batch processing and parallel execution"""
    
    def __init__(self, model_name: str = "mistralai/Mistral-7B-Instruct-v0.2"):
        self.model_name = model_name
        self.llm = OptimizedHuggingFaceLLM(model_name=model_name)
        logger.info(f"Initialized optimized RAGAS evaluator with {model_name}")

    def prepare_dataset(self, evaluation_data: List[Dict[str, Any]]) -> Dataset:
        """Prepare dataset for evaluation"""
        try:
            # Convert to RAGAS format
            ragas_data = []
            for item in evaluation_data:
                ragas_item = {
                    'question': item['question'],
                    'answer': item['answer'],
                    'contexts': item['contexts'],
                    'ground_truth': item.get('ground_truth', '')
                }
                ragas_data.append(ragas_item)
            
            # Create dataset
            dataset = Dataset.from_list(ragas_data)
            logger.info(f"Created dataset with {len(ragas_data)} examples")
            return dataset
            
        except Exception as e:
            logger.error(f"Error preparing dataset: {str(e)}")
            raise

    def _score_response(self, response: str) -> float:
        """Score a response based on evaluation keywords"""
        try:
            response_lower = response.lower().strip()
            
            if 'yes' in response_lower and 'no' not in response_lower:
                return 1.0
            elif 'no' in response_lower and 'yes' not in response_lower:
                return 0.0
            elif 'partially' in response_lower or 'somewhat' in response_lower:
                return 0.5
            elif 'unable' in response_lower or 'cannot' in response_lower:
                return 0.0
            else:
                # Default to neutral if unclear
                return 0.5
                
        except Exception as e:
            logger.error(f"Error scoring response: {str(e)}")
            return 0.5

    def calculate_metrics_batch(self, dataset: Dataset) -> Dict[str, float]:
        """Calculate all metrics using batch processing"""
        try:
            logger.info("Starting batch metric calculation...")
            start_time = time.time()
            
            results = {}
            
            # Prepare all prompts for batch processing
            faithfulness_prompts = []
            answer_relevancy_prompts = []
            context_relevancy_prompts = []
            context_recall_prompts = []
            context_precision_prompts = []
            
            for i in range(len(dataset)):
                question = dataset[i]['question']
                answer = dataset[i]['answer']
                contexts = dataset[i]['contexts']
                ground_truth = dataset[i].get('ground_truth', '')
                context_text = ' '.join(contexts)
                
                # Faithfulness prompts
                faithfulness_prompts.append(
                    f"Question: {question}\nAnswer: {answer}\nContext: {context_text}\n\n"
                    "Is the answer supported by the context? Answer ONLY with 'Yes', 'No', or 'Partially'."
                )
                
                # Answer relevancy prompts
                answer_relevancy_prompts.append(
                    f"Question: {question}\nAnswer: {answer}\n\n"
                    "Is the answer relevant to the question? Answer ONLY with 'Yes', 'No', or 'Partially'."
                )
                
                # Context relevancy prompts
                context_relevancy_prompts.append(
                    f"Question: {question}\nContext: {context_text}\n\n"
                    "Is the context relevant to the question? Answer ONLY with 'Yes', 'No', or 'Partially'."
                )
                
                # Context recall prompts
                context_recall_prompts.append(
                    f"Question: {question}\nContext: {context_text}\nGround Truth: {ground_truth}\n\n"
                    "Does the context contain information to answer the question? Answer ONLY with 'Yes', 'No', or 'Partially'."
                )
                
                # Context precision prompts
                context_precision_prompts.append(
                    f"Question: {question}\nContext: {context_text}\n\n"
                    "Is the context precise and focused on the question? Answer ONLY with 'Yes', 'No', or 'Partially'."
                )
            
            # Process all metrics in parallel using ThreadPoolExecutor
            with ThreadPoolExecutor(max_workers=5) as executor:
                # Submit all metric calculations
                future_to_metric = {
                    executor.submit(self._calculate_single_metric_batch, faithfulness_prompts, "faithfulness"): "faithfulness",
                    executor.submit(self._calculate_single_metric_batch, answer_relevancy_prompts, "answer_relevancy"): "answer_relevancy",
                    executor.submit(self._calculate_single_metric_batch, context_relevancy_prompts, "context_relevancy"): "context_relevancy",
                    executor.submit(self._calculate_single_metric_batch, context_recall_prompts, "context_recall"): "context_recall",
                    executor.submit(self._calculate_single_metric_batch, context_precision_prompts, "context_precision"): "context_precision"
                }
                
                # Collect results
                for future in as_completed(future_to_metric):
                    metric_name = future_to_metric[future]
                    try:
                        score = future.result()
                        results[metric_name] = score
                        logger.info(f"Completed {metric_name}: {score:.3f}")
                    except Exception as e:
                        logger.error(f"Error calculating {metric_name}: {str(e)}")
                        results[metric_name] = 0.0
            
            # Calculate average score
            valid_scores = [score for score in results.values() if score > 0]
            results['average_score'] = np.mean(valid_scores) if valid_scores else 0.0
            
            end_time = time.time()
            logger.info(f"Batch metric calculation completed in {end_time - start_time:.2f} seconds")
            
            return results
            
        except Exception as e:
            logger.error(f"Error in batch metric calculation: {str(e)}")
            return {
                'faithfulness': 0.0,
                'answer_relevancy': 0.0,
                'context_relevancy': 0.0,
                'context_recall': 0.0,
                'context_precision': 0.0,
                'average_score': 0.0
            }

    def _calculate_single_metric_batch(self, prompts: List[str], metric_name: str) -> float:
        """Calculate a single metric using batch processing"""
        try:
            logger.info(f"Calculating {metric_name}...")
            
            # Generate responses in batch
            responses = self.llm.batch_generate(prompts)
            
            # Score responses
            scores = [self._score_response(response) for response in responses]
            
            # Log some examples for debugging
            for i, (prompt, response, score) in enumerate(zip(prompts[:2], responses[:2], scores[:2])):
                logger.info(f"[{metric_name}] Example {i+1}:")
                logger.info(f"[{metric_name}] Prompt: {prompt[:100]}...")
                logger.info(f"[{metric_name}] Response: {response}")
                logger.info(f"[{metric_name}] Score: {score}")
            
            return np.mean(scores)
            
        except Exception as e:
            logger.error(f"Error calculating {metric_name}: {str(e)}")
            return 0.0

    def evaluate(self, evaluation_data: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Run the optimized evaluation process"""
        try:
            if evaluation_data is None:
                # Use sample data for testing
                evaluation_data = [
                    {
                        'question': 'What is the magnitude of the 2015 Nepal earthquake?',
                        'answer': 'The 2015 Nepal earthquake had a magnitude of 7.8 on the Richter scale.',
                        'contexts': ['The 2015 Nepal earthquake occurred on April 25 with a magnitude of 7.8. It caused widespread damage in Kathmandu and surrounding areas.'],
                        'ground_truth': 'The 2015 Nepal earthquake had a magnitude of 7.8.'
                    },
                    {
                        'question': 'How many people died in the 2004 Indian Ocean tsunami?',
                        'answer': 'The 2004 tsunami killed about 50 people.',
                        'contexts': ['The 2004 Indian Ocean tsunami was one of the deadliest natural disasters in recorded history, causing approximately 230,000 deaths across 14 countries.'],
                        'ground_truth': 'The 2004 Indian Ocean tsunami caused approximately 230,000 deaths.'
                    }
                ]
            
            logger.info("Starting OPTIMIZED RAGAS evaluation...")
            print(f"\n🚀 OPTIMIZED EVALUATION")
            print("=" * 50)
            print(f"Number of examples: {len(evaluation_data)}")
            print(f"Model: {self.model_name}")
            print(f"Batch size: {self.llm.batch_size}")
            print("=" * 50)
            
            # Prepare dataset
            dataset = self.prepare_dataset(evaluation_data)
            
            # Calculate metrics using batch processing
            start_time = time.time()
            metrics = self.calculate_metrics_batch(dataset)
            end_time = time.time()
            
            # Prepare results
            results = {
                'metrics': metrics,
                'evaluation_data': evaluation_data,
                'timestamp': datetime.now().isoformat(),
                'model_name': self.model_name,
                'dataset_size': len(evaluation_data),
                'processing_time': end_time - start_time,
                'optimization': 'batch_processing'
            }
            
            # Save results
            self.save_results(results)
            
            return results
            
        except Exception as e:
            error_msg = f"Error in optimized evaluation: {str(e)}"
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
                'error': str(e)
            }
    
    def save_results(self, results: Dict[str, Any]):
        """Save evaluation results to file"""
        try:
            # Create results directory
            results_dir = "evaluation_results"
            os.makedirs(results_dir, exist_ok=True)
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(results_dir, f"ragas_optimized_{timestamp}.json")
            
            # Save results
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2, default=str)
            
            logger.info(f"Optimized results saved to {output_file}")
            
            # Print summary
            print("\n" + "="*60)
            print("OPTIMIZED RAGAS EVALUATION RESULTS")
            print("="*60)
            print(f"Model: {results.get('model_name', 'Unknown')}")
            print(f"Timestamp: {results['timestamp']}")
            print(f"Dataset size: {results.get('dataset_size', 0)}")
            print(f"Processing time: {results.get('processing_time', 0):.2f} seconds")
            print(f"Optimization: {results.get('optimization', 'Unknown')}")
            print("\nMetric Scores:")
            print("-" * 30)
            
            for metric_name, score in results['metrics'].items():
                if metric_name != 'average_score':
                    print(f"{metric_name.replace('_', ' ').title()}: {score:.3f}")
            
            print(f"\nAverage Score: {results['metrics'].get('average_score', 0):.3f}")
            print("="*60)
            
        except Exception as e:
            logger.error(f"Error saving results: {str(e)}")

def main():
    """Main function for testing optimized evaluation"""
    print("🚀 OPTIMIZED RAGAS EVALUATION TEST")
    print("=" * 60)
    
    # Create evaluator
    evaluator = OptimizedRAGASEvaluator(model_name="mistralai/Mistral-7B-Instruct-v0.2")
    
    # Run evaluation
    results = evaluator.evaluate()
    
    print(f"\n✅ OPTIMIZED EVALUATION COMPLETED!")
    print(f"⏱️  Total time: {results.get('processing_time', 0):.2f} seconds")
    print(f"📊 Average score: {results['metrics'].get('average_score', 0):.3f}")

if __name__ == "__main__":
    main() 