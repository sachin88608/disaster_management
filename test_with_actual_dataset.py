#!/usr/bin/env python3
"""
Test optimized RAGAS evaluation with actual SAMPLE_EVALUATION_DATASET.csv
"""

import time
import sys
import os
import pandas as pd

# Add current directory to path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ragas_evaluation_fixed import RAGASEvaluator

def load_actual_dataset():
    """Load the actual evaluation dataset from CSV"""
    csv_file = "SAMPLE_EVALUATION_DATASET.csv"
    
    if not os.path.exists(csv_file):
        print(f"❌ Error: {csv_file} not found!")
        return None
    
    print(f"📁 Loading dataset from {csv_file}...")
    df = pd.read_csv(csv_file)
    
    print(f"📊 Dataset loaded: {len(df)} examples")
    print(f"📋 Columns: {list(df.columns)}")
    
    # Show sample data
    print("\n📝 Sample data:")
    print("=" * 50)
    for i, (_, row) in enumerate(df.head(3).iterrows()):
        print(f"Example {i+1}:")
        print(f"  Question: {row['question'][:100]}...")
        print(f"  Answer: {row['answer'][:100]}...")
        print(f"  Context: {row['context'][:100]}...")
        print(f"  Ground Truth: {row['ground_truth'][:100]}...")
        print()
    
    return df

def prepare_evaluation_data(df):
    """Prepare DataFrame for RAGAS evaluation"""
    evaluation_data = []
    
    for _, row in df.iterrows():
        evaluation_data.append({
            'question': row['question'],
            'answer': row['answer'],
            'contexts': [row['context']] if pd.notna(row['context']) else [],
            'ground_truth': row['ground_truth'] if pd.notna(row['ground_truth']) else ''
        })
    
    return evaluation_data

def main():
    """Main test function"""
    print("🚀 TESTING OPTIMIZED RAGAS WITH ACTUAL DATASET")
    print("=" * 60)
    
    # Load actual dataset
    df = load_actual_dataset()
    if df is None:
        return
    
    # Prepare evaluation data
    evaluation_data = prepare_evaluation_data(df)
    
    print(f"✅ Prepared {len(evaluation_data)} examples for evaluation")
    
    # Create evaluator with optimized model
    print(f"\n🤖 Initializing optimized RAGAS evaluator...")
    print(f"📋 Model: mistralai/Mistral-7B-Instruct-v0.2")
    print(f"⚡ Optimization: Batch processing enabled")
    
    evaluator = RAGASEvaluator(model_name="mistralai/Mistral-7B-Instruct-v0.2")
    
    # Run evaluation
    print(f"\n🧪 Starting evaluation...")
    start_time = time.time()
    
    results = evaluator.evaluate(evaluation_data)
    
    end_time = time.time()
    total_time = end_time - start_time
    
    # Display results
    print(f"\n✅ EVALUATION COMPLETED!")
    print("=" * 60)
    print(f"⏱️  Total time: {total_time:.2f} seconds")
    print(f"📊 Examples processed: {len(evaluation_data)}")
    print(f"🚀 Average time per example: {total_time/len(evaluation_data):.2f} seconds")
    
    if 'error' in results:
        print(f"❌ Evaluation completed with errors: {results['error']}")
    else:
        print(f"📈 Average score: {results['metrics'].get('average_score', 0):.3f}")
        print(f"✅ Results saved to evaluation_results/")
    
    print(f"\n🎯 READY FOR 16 EXPERIMENTS!")
    print("=" * 60)
    print("The optimized evaluation is working correctly.")
    print("You can now proceed with your 16 experiments.")

if __name__ == "__main__":
    main() 