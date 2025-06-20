"""
Script to run a single RAGAS experiment by experiment number.
This allows running experiments one by one instead of all at once.
Uses OPTIMIZED RAGAS evaluation for better performance.
"""

import os
import json
import logging
from datetime import datetime
import pandas as pd
from ragas_evaluation_fixed import RAGASEvaluator  # Using optimized version
from config import Config
from batch_experiments import BatchExperimentRunner

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('single_experiment.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def run_experiment(experiment_number: int):
    """Run a single experiment by its number (1-16)"""
    try:
        if not 1 <= experiment_number <= 16:
            raise ValueError("Experiment number must be between 1 and 16")
        
        print(f"🚀 Starting Experiment {experiment_number} (OPTIMIZED)")
        print("="*50)
        
        # Initialize batch runner
        runner = BatchExperimentRunner()
        
        # Get experiment config
        experiment_config = runner.experiments[experiment_number - 1]
        
        print(f"📋 Experiment Configuration:")
        print(f"   Embedding Model: {experiment_config['embedding_model']}")
        print(f"   LLM Model: {experiment_config['llm_model']}")
        print(f"   RAGAS Model: mistralai/Mistral-7B-Instruct-v0.2 (Optimized)")
        print()
        
        # Run the experiment
        result = runner.run_single_experiment(experiment_config)
        
        if result:
            print(f"\n✅ Successfully completed Experiment {experiment_number}!")
            print("\nResults Summary:")
            print("-" * 40)
            print(f"Embedding Model: {result.get('embedding_model', 'Unknown')}")
            print(f"LLM Model: {result.get('llm_model', 'Unknown')}")
            print(f"Processing Time: {result.get('processing_time', 0):.2f} seconds")
            print("\nMetric Scores:")
            for metric_name, score in result['metrics'].items():
                if metric_name != 'average_score':
                    print(f"  {metric_name.replace('_', ' ').title()}: {score:.3f}")
            print(f"  Average Score: {result['metrics']['average_score']:.3f}")
        else:
            print(f"\n❌ Experiment {experiment_number} failed")
        
    except Exception as e:
        logger.error(f"Error running experiment {experiment_number}: {str(e)}")
        print(f"Error: {str(e)}")

def main():
    """Main execution function"""
    try:
        # Get experiment number from user
        while True:
            try:
                experiment_number = int(input("\nEnter experiment number (1-16): "))
                if 1 <= experiment_number <= 16:
                    break
                print("Please enter a number between 1 and 16")
            except ValueError:
                print("Please enter a valid number")
        
        # Run the experiment
        run_experiment(experiment_number)
        
    except Exception as e:
        logger.error(f"Error in main: {str(e)}")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 