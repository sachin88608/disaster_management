"""
Experiment status checker to see which experiments are completed.
"""

import os
import json
from datetime import datetime

def check_experiment_status():
    """Check status of all 8 experiments"""
    
    # All experiments configuration
    experiments = [
        {
            'name': 'Experiment_1',
            'description': 'all-MiniLM-L6-v2 + llama3-70b-8192',
            'embedding_model': 'all-MiniLM-L6-v2',
            'llm_model': 'llama3-70b-8192'
        },
        {
            'name': 'Experiment_2', 
            'description': 'all-MiniLM-L12-v2 + llama3-70b-8192',
            'embedding_model': 'all-MiniLM-L12-v2',
            'llm_model': 'llama3-70b-8192'
        },
        {
            'name': 'Experiment_3',
            'description': 'all-MiniLM-L6-v2 + mixtral-8x7b-32768', 
            'embedding_model': 'all-MiniLM-L6-v2',
            'llm_model': 'mixtral-8x7b-32768'
        },
        {
            'name': 'Experiment_4',
            'description': 'all-MiniLM-L12-v2 + mixtral-8x7b-32768',
            'embedding_model': 'all-MiniLM-L12-v2', 
            'llm_model': 'mixtral-8x7b-32768'
        },
        {
            'name': 'Experiment_5',
            'description': 'bge-small-en-v1.5 + llama-3.3-70b-versatile',
            'embedding_model': 'bge-small-en-v1.5',
            'llm_model': 'llama-3.3-70b-versatile'
        },
        {
            'name': 'Experiment_6',
            'description': 'bge-base-en-v1.5 + llama-3.3-70b-versatile',
            'embedding_model': 'bge-base-en-v1.5',
            'llm_model': 'llama-3.3-70b-versatile'
        },
        {
            'name': 'Experiment_7',
            'description': 'bge-base-en-v1.5 + llama-3.1-8b-instant',
            'embedding_model': 'bge-base-en-v1.5',
            'llm_model': 'llama-3.1-8b-instant'
        },
        {
            'name': 'Experiment_8',
            'description': 'bge-small-en-v1.5 + llama-3.1-8b-instant',
            'embedding_model': 'bge-small-en-v1.5',
            'llm_model': 'llama-3.1-8b-instant'
        }
    ]
    
    print("🔬 EXPERIMENT STATUS CHECKER")
    print("="*80)
    print(f"Checked at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    
    # Check batch experiment results
    batch_results_dir = "batch_experiment_results"
    completed_experiments = set()
    
    if os.path.exists(batch_results_dir):
        for filename in os.listdir(batch_results_dir):
            if filename.endswith('.json'):
                experiment_name = filename.split('_')[0]
                completed_experiments.add(experiment_name)
    
    # Check old evaluation results
    old_results_dir = "evaluation_results"
    if os.path.exists(old_results_dir):
        for filename in os.listdir(old_results_dir):
            if filename.endswith('.json'):
                # This is likely Experiment_1
                completed_experiments.add('Experiment_1')
    
    # Display status
    total_experiments = len(experiments)
    completed_count = len(completed_experiments)
    remaining_count = total_experiments - completed_count
    
    print(f"\n📊 OVERALL STATUS:")
    print(f"   Total Experiments: {total_experiments}")
    print(f"   Completed: {completed_count}")
    print(f"   Remaining: {remaining_count}")
    print(f"   Progress: {(completed_count/total_experiments)*100:.1f}%")
    
    print(f"\n📋 DETAILED STATUS:")
    print("-" * 80)
    print(f"{'Experiment':<12} {'Status':<10} {'Embedding Model':<20} {'LLM Model':<25}")
    print("-" * 80)
    
    for exp in experiments:
        status = "✅ DONE" if exp['name'] in completed_experiments else "⏳ PENDING"
        print(f"{exp['name']:<12} {status:<10} {exp['embedding_model']:<20} {exp['llm_model']:<25}")
    
    print("-" * 80)
    
    # Show next steps
    if remaining_count > 0:
        print(f"\n🚀 NEXT STEPS:")
        print(f"1. Setup embedding models: python experiment_setup.py")
        print(f"2. Run remaining experiments: python batch_experiments.py")
        print(f"3. Check results in: batch_experiment_results/")
    else:
        print(f"\n🎉 ALL EXPERIMENTS COMPLETED!")
        print(f"Check comparison report in: batch_experiment_results/")
    
    # Show best performing experiment if available
    if completed_experiments:
        print(f"\n🏆 BEST PERFORMING EXPERIMENT:")
        best_score = 0
        best_exp = None
        
        # Check batch results
        if os.path.exists(batch_results_dir):
            for filename in os.listdir(batch_results_dir):
                if filename.endswith('.json'):
                    filepath = os.path.join(batch_results_dir, filename)
                    try:
                        with open(filepath, 'r') as f:
                            data = json.load(f)
                            avg_score = data.get('metrics', {}).get('average_score', 0)
                            if avg_score > best_score:
                                best_score = avg_score
                                best_exp = data.get('experiment_name', 'Unknown')
                    except:
                        continue
        
        if best_exp:
            print(f"   {best_exp} with average score: {best_score:.3f}")
        else:
            print(f"   Check individual result files for scores")

if __name__ == "__main__":
    check_experiment_status() 