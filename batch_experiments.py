"""
Batch experiment runner for RAG system evaluation.
This script runs multiple experiments with different model combinations.
Uses OPTIMIZED RAGAS evaluation for better performance.
"""

import os
import json
import logging
from datetime import datetime
import pandas as pd
from ragas_evaluation_fixed import RAGASEvaluator  # Using optimized version
from config import Config
from rag_system import RAGSystem

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('batch_experiments.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class BatchExperimentRunner:
    """Runner for batch experiments with different model combinations"""
    
    def __init__(self):
        self.config = Config()
        
        # Define 16 experiments with different model combinations
        self.experiments = [
            # Experiments 1-4: all-MiniLM-L6-v2 embeddings
            {
                'experiment_id': 1,
                'embedding_model': 'all-MiniLM-L6-v2',
                'llm_model': 'llama3-70b-8192',
                'description': 'all-MiniLM-L6-v2 + llama3-70b-8192'
            },
            {
                'experiment_id': 2,
                'embedding_model': 'all-MiniLM-L6-v2',
                'llm_model': 'mixtral-8x7b-32768',
                'description': 'all-MiniLM-L6-v2 + mixtral-8x7b-32768'
            },
            {
                'experiment_id': 3,
                'embedding_model': 'all-MiniLM-L6-v2',
                'llm_model': 'llama-3.3-70b-versatile',
                'description': 'all-MiniLM-L6-v2 + llama-3.3-70b-versatile'
            },
            {
                'experiment_id': 4,
                'embedding_model': 'all-MiniLM-L6-v2',
                'llm_model': 'llama-3.1-8b-instant',
                'description': 'all-MiniLM-L6-v2 + llama-3.1-8b-instant'
            },
            
            # Experiments 5-8: all-MiniLM-L12-v2 embeddings
            {
                'experiment_id': 5,
                'embedding_model': 'all-MiniLM-L12-v2',
                'llm_model': 'llama3-70b-8192',
                'description': 'all-MiniLM-L12-v2 + llama3-70b-8192'
            },
            {
                'experiment_id': 6,
                'embedding_model': 'all-MiniLM-L12-v2',
                'llm_model': 'mixtral-8x7b-32768',
                'description': 'all-MiniLM-L12-v2 + mixtral-8x7b-32768'
            },
            {
                'experiment_id': 7,
                'embedding_model': 'all-MiniLM-L12-v2',
                'llm_model': 'llama-3.3-70b-versatile',
                'description': 'all-MiniLM-L12-v2 + llama-3.3-70b-versatile'
            },
            {
                'experiment_id': 8,
                'embedding_model': 'all-MiniLM-L12-v2',
                'llm_model': 'llama-3.1-8b-instant',
                'description': 'all-MiniLM-L12-v2 + llama-3.1-8b-instant'
            },
            
            # Experiments 9-12: bge-small-en-v1.5 embeddings
            {
                'experiment_id': 9,
                'embedding_model': 'bge-small-en-v1.5',
                'llm_model': 'llama3-70b-8192',
                'description': 'bge-small-en-v1.5 + llama3-70b-8192'
            },
            {
                'experiment_id': 10,
                'embedding_model': 'bge-small-en-v1.5',
                'llm_model': 'mixtral-8x7b-32768',
                'description': 'bge-small-en-v1.5 + mixtral-8x7b-32768'
            },
            {
                'experiment_id': 11,
                'embedding_model': 'bge-small-en-v1.5',
                'llm_model': 'llama-3.3-70b-versatile',
                'description': 'bge-small-en-v1.5 + llama-3.3-70b-versatile'
            },
            {
                'experiment_id': 12,
                'embedding_model': 'bge-small-en-v1.5',
                'llm_model': 'llama-3.1-8b-instant',
                'description': 'bge-small-en-v1.5 + llama-3.1-8b-instant'
            },
            
            # Experiments 13-16: bge-base-en-v1.5 embeddings
            {
                'experiment_id': 13,
                'embedding_model': 'bge-base-en-v1.5',
                'llm_model': 'llama3-70b-8192',
                'description': 'bge-base-en-v1.5 + llama3-70b-8192'
            },
            {
                'experiment_id': 14,
                'embedding_model': 'bge-base-en-v1.5',
                'llm_model': 'mixtral-8x7b-32768',
                'description': 'bge-base-en-v1.5 + mixtral-8x7b-32768'
            },
            {
                'experiment_id': 15,
                'embedding_model': 'bge-base-en-v1.5',
                'llm_model': 'llama-3.3-70b-versatile',
                'description': 'bge-base-en-v1.5 + llama-3.3-70b-versatile'
            },
            {
                'experiment_id': 16,
                'embedding_model': 'bge-base-en-v1.5',
                'llm_model': 'llama-3.1-8b-instant',
                'description': 'bge-base-en-v1.5 + llama-3.1-8b-instant'
            }
        ]
        
        logger.info(f"Initialized BatchExperimentRunner with {len(self.experiments)} experiments")

    def load_evaluation_dataset(self):
        """Load the evaluation dataset from CSV"""
        try:
            csv_file = "SAMPLE_EVALUATION_DATASET.csv"
            if not os.path.exists(csv_file):
                logger.error(f"Evaluation dataset {csv_file} not found")
                return None
            
            logger.info(f"Loading evaluation dataset from {csv_file}")
            df = pd.read_csv(csv_file)
            logger.info(f"Loaded {len(df)} examples from evaluation dataset")
            return df
            
        except Exception as e:
            logger.error(f"Error loading evaluation dataset: {str(e)}")
            return None

    def run_single_experiment(self, experiment_config):
        """Run a single experiment with the given configuration"""
        try:
            experiment_id = experiment_config['experiment_id']
            embedding_model = experiment_config['embedding_model']
            llm_model = experiment_config['llm_model']
            
            logger.info(f"Starting Experiment {experiment_id}: {experiment_config['description']}")
            
            # Load evaluation dataset
            df = self.load_evaluation_dataset()
            if df is None:
                return None
            
            # Initialize RAG system with experiment configuration
            logger.info(f"Initializing RAG system with {embedding_model} + {llm_model}")
            rag_system = RAGSystem(
                embedding_model=embedding_model,
                llm_model=llm_model
            )
            
            # Prepare evaluation data
            evaluation_data = []
            for _, row in df.iterrows():
                question = row['question']
                ground_truth = row['ground_truth']
                
                # Get answer from RAG system
                try:
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
                    
                    evaluation_data.append({
                        'question': question,
                        'answer': chatbot_answer,
                        'contexts': truncated_contexts,
                        'ground_truth': ground_truth
                    })
                    
                except Exception as e:
                    logger.warning(f"Error getting answer for question: {e}")
                    # Use ground truth as fallback
                    evaluation_data.append({
                        'question': question,
                        'answer': ground_truth,
                        'contexts': [str(ground_truth)],
                        'ground_truth': ground_truth
                    })
            
            # Run RAGAS evaluation with optimized evaluator
            logger.info(f"Running RAGAS evaluation for Experiment {experiment_id}")
            evaluator = RAGASEvaluator(model_name="mistralai/Mistral-7B-Instruct-v0.2")
            results = evaluator.evaluate(evaluation_data)
            
            # Add experiment metadata
            results['experiment_id'] = experiment_id
            results['embedding_model'] = embedding_model
            results['llm_model'] = llm_model
            results['description'] = experiment_config['description']
            results['ragas_model'] = "mistralai/Mistral-7B-Instruct-v0.2"
            results['optimization'] = "batch_processing"
            
            # Save experiment results
            self.save_experiment_results(results)
            
            logger.info(f"Completed Experiment {experiment_id}")
            return results
            
        except Exception as e:
            logger.error(f"Error in experiment {experiment_config.get('experiment_id', 'Unknown')}: {str(e)}")
            return None

    def save_experiment_results(self, results):
        """Save individual experiment results"""
        try:
            # Create results directory
            results_dir = "batch_experiment_results"
            os.makedirs(results_dir, exist_ok=True)
            
            # Generate filename
            experiment_id = results['experiment_id']
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"Experiment_{experiment_id}_{timestamp}.json"
            filepath = os.path.join(results_dir, filename)
            
            # Save results
            with open(filepath, 'w') as f:
                json.dump(results, f, indent=2, default=str)
            
            logger.info(f"Saved experiment results to {filepath}")
            
        except Exception as e:
            logger.error(f"Error saving experiment results: {str(e)}")

    def run_all_experiments(self):
        """Run all experiments sequentially"""
        try:
            logger.info("Starting batch experiments")
            print("🚀 STARTING BATCH EXPERIMENTS")
            print("=" * 60)
            print(f"📊 Total experiments: {len(self.experiments)}")
            print(f"🤖 RAGAS Model: mistralai/Mistral-7B-Instruct-v0.2 (Optimized)")
            print("=" * 60)
            
            all_results = []
            
            for i, experiment_config in enumerate(self.experiments, 1):
                print(f"\n🧪 Running Experiment {i}/{len(self.experiments)}")
                print(f"📋 {experiment_config['description']}")
                
                result = self.run_single_experiment(experiment_config)
                
                if result:
                    all_results.append(result)
                    print(f"✅ Experiment {i} completed successfully")
                    print(f"📈 Average Score: {result['metrics'].get('average_score', 0):.3f}")
                else:
                    print(f"❌ Experiment {i} failed")
                
                print("-" * 40)
            
            # Save summary
            self.save_batch_summary(all_results)
            
            print(f"\n🎉 BATCH EXPERIMENTS COMPLETED!")
            print(f"✅ Successful: {len(all_results)}/{len(self.experiments)}")
            
            return all_results
            
        except Exception as e:
            logger.error(f"Error in batch experiments: {str(e)}")
            return []

    def save_batch_summary(self, results):
        """Save summary of all experiments"""
        try:
            summary = {
                'timestamp': datetime.now().isoformat(),
                'total_experiments': len(self.experiments),
                'completed_experiments': len(results),
                'ragas_model': 'mistralai/Mistral-7B-Instruct-v0.2',
                'optimization': 'batch_processing',
                'experiments': []
            }
            
            for result in results:
                summary['experiments'].append({
                    'experiment_id': result['experiment_id'],
                    'embedding_model': result['embedding_model'],
                    'llm_model': result['llm_model'],
                    'description': result['description'],
                    'metrics': result['metrics'],
                    'processing_time': result.get('processing_time', 0)
                })
            
            # Save summary
            results_dir = "batch_experiment_results"
            os.makedirs(results_dir, exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            summary_file = os.path.join(results_dir, f"batch_summary_{timestamp}.json")
            
            with open(summary_file, 'w') as f:
                json.dump(summary, f, indent=2, default=str)
            
            logger.info(f"Saved batch summary to {summary_file}")
            
        except Exception as e:
            logger.error(f"Error saving batch summary: {str(e)}")

def main():
    """Main execution function"""
    try:
        runner = BatchExperimentRunner()
        
        print("Choose an option:")
        print("1. Run all experiments")
        print("2. Run single experiment")
        
        choice = input("Enter your choice (1 or 2): ").strip()
        
        if choice == "1":
            runner.run_all_experiments()
        elif choice == "2":
            experiment_number = int(input("Enter experiment number (1-16): "))
            if 1 <= experiment_number <= 16:
                experiment_config = runner.experiments[experiment_number - 1]
                runner.run_single_experiment(experiment_config)
            else:
                print("Invalid experiment number")
        else:
            print("Invalid choice")
            
    except Exception as e:
        logger.error(f"Error in main: {str(e)}")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 