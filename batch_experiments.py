"""
Batch experiment script for RAGAS evaluation with different LLM and embedding combinations.
This script will run all 4 experiments automatically and save results with clear naming.
"""

import os
import json
import logging
from datetime import datetime
import pandas as pd
from ragas_evaluation import RAGASEvaluator
from config import Config
import shutil

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
    """Class to run multiple RAGAS experiments with different configurations"""
    
    def __init__(self):
        self.config = Config()
        
        # All 8 Experiments Configuration:
        # Experiment 1: all-MiniLM-L6-v2 + llama3-70b-8192 (COMPLETED)
        # Experiment 2: all-MiniLM-L12-v2 + llama3-70b-8192
        # Experiment 3: all-MiniLM-L6-v2 + mixtral-8x7b-32768
        # Experiment 4: all-MiniLM-L12-v2 + mixtral-8x7b-32768
        # Experiment 5: bge-small-en-v1.5 + llama-3.3-70b-versatile
        # Experiment 6: bge-base-en-v1.5 + llama-3.3-70b-versatile
        # Experiment 7: bge-base-en-v1.5 + llama-3.1-8b-instant
        # Experiment 8: bge-small-en-v1.5 + llama-3.1-8b-instant
        
        self.experiments = [
            {
                'name': 'Experiment_1',
                'description': 'all-MiniLM-L6-v2 + llama3-70b-8192',
                'embedding_model': 'all-MiniLM-L6-v2',
                'llm_model': 'llama3-70b-8192',
                'ragas_model': 'microsoft/phi-2'
            },
            {
                'name': 'Experiment_2', 
                'description': 'all-MiniLM-L12-v2 + llama3-70b-8192',
                'embedding_model': 'all-MiniLM-L12-v2',
                'llm_model': 'llama3-70b-8192',
                'ragas_model': 'microsoft/phi-2'
            },
            {
                'name': 'Experiment_3',
                'description': 'all-MiniLM-L6-v2 + mixtral-8x7b-32768', 
                'embedding_model': 'all-MiniLM-L6-v2',
                'llm_model': 'mixtral-8x7b-32768',
                'ragas_model': 'microsoft/phi-2'
            },
            {
                'name': 'Experiment_4',
                'description': 'all-MiniLM-L12-v2 + mixtral-8x7b-32768',
                'embedding_model': 'all-MiniLM-L12-v2', 
                'llm_model': 'mixtral-8x7b-32768',
                'ragas_model': 'microsoft/phi-2'
            },
            {
                'name': 'Experiment_5',
                'description': 'bge-small-en-v1.5 + llama-3.3-70b-versatile',
                'embedding_model': 'bge-small-en-v1.5',
                'llm_model': 'llama-3.3-70b-versatile',
                'ragas_model': 'microsoft/phi-2'
            },
            {
                'name': 'Experiment_6',
                'description': 'bge-base-en-v1.5 + llama-3.3-70b-versatile',
                'embedding_model': 'bge-base-en-v1.5',
                'llm_model': 'llama-3.3-70b-versatile',
                'ragas_model': 'microsoft/phi-2'
            },
            {
                'name': 'Experiment_7',
                'description': 'bge-base-en-v1.5 + llama-3.1-8b-instant',
                'embedding_model': 'bge-base-en-v1.5',
                'llm_model': 'llama-3.1-8b-instant',
                'ragas_model': 'microsoft/phi-2'
            },
            {
                'name': 'Experiment_8',
                'description': 'bge-small-en-v1.5 + llama-3.1-8b-instant',
                'embedding_model': 'bge-small-en-v1.5',
                'llm_model': 'llama-3.1-8b-instant',
                'ragas_model': 'microsoft/phi-2'
            }
        ]
        
    def update_config(self, embedding_model: str, llm_model: str):
        """Update configuration for current experiment"""
        try:
            # Update environment variables for this experiment
            os.environ['EMBEDDING_MODEL'] = embedding_model
            os.environ['GROQ_MODEL'] = llm_model
            
            # Reload config
            self.config.EMBEDDING_MODEL = embedding_model
            self.config.GROQ_MODEL = llm_model
            
            logger.info(f"Updated config - Embedding: {embedding_model}, LLM: {llm_model}")
            
        except Exception as e:
            logger.error(f"Error updating config: {str(e)}")
            raise
    
    def setup_rag_system(self, experiment_config: dict):
        """Setup RAG system with experiment configuration"""
        try:
            # Update configuration
            self.update_config(
                experiment_config['embedding_model'], 
                experiment_config['llm_model']
            )
            
            # Import and initialize RAG system with new config
            from rag_system import RAGSystem
            logger.info(f"Initializing RAG system for {experiment_config['name']}...")
            
            # Force reinitialization with new config
            rag_system = RAGSystem()
            
            # Test the system
            test_response = rag_system.query("What is a flood?")
            logger.info(f"RAG system test successful for {experiment_config['name']}")
            
            return rag_system
            
        except Exception as e:
            logger.error(f"Error setting up RAG system for {experiment_config['name']}: {str(e)}")
            raise
    
    def run_single_experiment(self, experiment_config: dict, rag_system=None):
        """Run a single experiment"""
        try:
            experiment_name = experiment_config['name']
            logger.info(f"\n{'='*60}")
            logger.info(f"Starting {experiment_name}: {experiment_config['description']}")
            logger.info(f"{'='*60}")
            
            # Setup RAG system if not provided
            if rag_system is None:
                rag_system = self.setup_rag_system(experiment_config)
            
            # Initialize RAGAS evaluator
            evaluator = RAGASEvaluator(model_name=experiment_config['ragas_model'])
            
            # Load evaluation dataset
            sample_file = 'SAMPLE_EVALUATION_DATASET.csv'
            if not os.path.exists(sample_file):
                logger.error(f"Evaluation dataset {sample_file} not found!")
                return None
            
            logger.info(f"Loading evaluation data from {sample_file}...")
            df = pd.read_csv(sample_file)
            
            # Convert DataFrame to evaluation format
            evaluation_data = []
            for idx, row in df.iterrows():
                question = row['question']
                ground_truth = row['ground_truth_answer']
                source = row['source']
                
                logger.info(f"Processing question {idx+1}: {question}")
                
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
                    
                    logger.info(f"Chatbot answer: {chatbot_answer[:100]}...")
                    logger.info(f"Retrieved contexts: {len(truncated_contexts)} contexts")
                    
                    evaluation_data.append({
                        'question': question,
                        'answer': chatbot_answer,
                        'contexts': truncated_contexts,
                        'ground_truth': ground_truth,
                        'source': source
                    })
                    
                except Exception as e:
                    logger.error(f"Error getting answer for question {idx+1}: {e}")
                    # Fallback to ground truth
                    evaluation_data.append({
                        'question': question,
                        'answer': ground_truth,
                        'contexts': [str(ground_truth)],
                        'ground_truth': ground_truth,
                        'source': source
                    })
            
            # Run evaluation
            logger.info(f"Running RAGAS evaluation for {experiment_name}...")
            results = evaluator.evaluate(evaluation_data)
            
            # Add experiment metadata
            results['experiment_name'] = experiment_name
            results['experiment_description'] = experiment_config['description']
            results['embedding_model'] = experiment_config['embedding_model']
            results['llm_model'] = experiment_config['llm_model']
            results['ragas_model'] = experiment_config['ragas_model']
            
            # Save results with experiment name
            self.save_experiment_results(results, experiment_name)
            
            logger.info(f"Completed {experiment_name} successfully!")
            return results
            
        except Exception as e:
            logger.error(f"Error in experiment {experiment_config['name']}: {str(e)}")
            return None
    
    def save_experiment_results(self, results: dict, experiment_name: str):
        """Save experiment results with clear naming"""
        try:
            # Create results directory
            results_dir = "batch_experiment_results"
            os.makedirs(results_dir, exist_ok=True)
            
            # Generate filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(results_dir, f"{experiment_name}_{timestamp}.json")
            
            # Save results
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2, default=str)
            
            logger.info(f"Results saved to {output_file}")
            
            # Print summary
            print(f"\n{experiment_name} Results Summary:")
            print("-" * 40)
            print(f"Embedding Model: {results.get('embedding_model', 'Unknown')}")
            print(f"LLM Model: {results.get('llm_model', 'Unknown')}")
            print(f"Dataset Size: {results.get('dataset_size', 0)}")
            print("\nMetric Scores:")
            for metric_name, score in results['metrics'].items():
                if metric_name != 'average_score':
                    print(f"  {metric_name.replace('_', ' ').title()}: {score:.3f}")
            print(f"  Average Score: {results['metrics']['average_score']:.3f}")
            print("-" * 40)
            
        except Exception as e:
            logger.error(f"Error saving results: {str(e)}")
    
    def run_all_experiments(self, skip_completed=True):
        """Run all experiments"""
        try:
            logger.info("Starting batch experiments...")
            
            # Check which experiments are already completed
            results_dir = "batch_experiment_results"
            completed_experiments = set()
            
            if skip_completed and os.path.exists(results_dir):
                for filename in os.listdir(results_dir):
                    if filename.endswith('.json'):
                        experiment_name = filename.split('_')[0]
                        completed_experiments.add(experiment_name)
            
            all_results = []
            
            for experiment_config in self.experiments:
                experiment_name = experiment_config['name']
                
                if skip_completed and experiment_name in completed_experiments:
                    logger.info(f"Skipping {experiment_name} (already completed)")
                    continue
                
                # Run experiment
                result = self.run_single_experiment(experiment_config)
                if result:
                    all_results.append(result)
                
                # Small delay between experiments
                import time
                time.sleep(2)
            
            # Generate comparison report
            self.generate_comparison_report(all_results)
            
            logger.info("All experiments completed!")
            return all_results
            
        except Exception as e:
            logger.error(f"Error in batch experiments: {str(e)}")
            return []
    
    def generate_comparison_report(self, results: list):
        """Generate a comparison report of all experiments"""
        try:
            if not results:
                logger.warning("No results to compare")
                return
            
            # Create comparison data
            comparison_data = []
            for result in results:
                comparison_data.append({
                    'Experiment': result['experiment_name'],
                    'Description': result['experiment_description'],
                    'Embedding Model': result['embedding_model'],
                    'LLM Model': result['llm_model'],
                    'Faithfulness': result['metrics']['faithfulness'],
                    'Answer Relevancy': result['metrics']['answer_relevancy'],
                    'Context Relevancy': result['metrics']['context_relevancy'],
                    'Context Recall': result['metrics']['context_recall'],
                    'Context Precision': result['metrics']['context_precision'],
                    'Average Score': result['metrics']['average_score']
                })
            
            # Create DataFrame
            df = pd.DataFrame(comparison_data)
            
            # Save comparison report
            results_dir = "batch_experiment_results"
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            comparison_file = os.path.join(results_dir, f"experiment_comparison_{timestamp}.csv")
            df.to_csv(comparison_file, index=False)
            
            # Print comparison
            print("\n" + "="*80)
            print("EXPERIMENT COMPARISON REPORT")
            print("="*80)
            print(df.to_string(index=False))
            print("="*80)
            
            # Find best performing experiment
            best_experiment = df.loc[df['Average Score'].idxmax()]
            print(f"\n🏆 BEST PERFORMING EXPERIMENT:")
            print(f"   {best_experiment['Experiment']}: {best_experiment['Description']}")
            print(f"   Average Score: {best_experiment['Average Score']:.3f}")
            
            logger.info(f"Comparison report saved to {comparison_file}")
            
        except Exception as e:
            logger.error(f"Error generating comparison report: {str(e)}")

def main():
    """Main execution function"""
    try:
        print("🚀 Starting Batch RAGAS Experiments")
        print("="*50)
        
        runner = BatchExperimentRunner()
        
        # Run all experiments
        results = runner.run_all_experiments(skip_completed=True)
        
        if results:
            print(f"\n✅ Successfully completed {len(results)} experiments!")
        else:
            print("\n❌ No experiments completed successfully")
        
    except Exception as e:
        logger.error(f"Error in main: {str(e)}")
        print(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main() 