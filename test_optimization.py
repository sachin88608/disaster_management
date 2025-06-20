#!/usr/bin/env python3
"""
Performance comparison test between original and optimized RAGAS evaluation
"""

import time
import sys
import os

# Add current directory to path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ragas_evaluation import RAGASEvaluator
from ragas_evaluation_optimized import OptimizedRAGASEvaluator

def test_original_evaluation():
    """Test original evaluation performance"""
    print("\n🧪 TESTING ORIGINAL EVALUATION")
    print("=" * 50)
    
    start_time = time.time()
    
    # Create evaluator
    evaluator = RAGASEvaluator(model_name="mistralai/Mistral-7B-Instruct-v0.2")
    
    # Test data
    test_data = [
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
        },
        {
            'question': 'What are the main causes of floods?',
            'answer': 'Floods are caused by heavy rainfall and snowmelt.',
            'contexts': ['The weather in Paris is usually mild with occasional rain. The city has many beautiful parks and gardens.'],
            'ground_truth': 'Floods are primarily caused by heavy rainfall, snowmelt, and dam failures.'
        },
        {
            'question': 'What was the magnitude of the 2011 Japan earthquake?',
            'answer': 'The 2011 Japan earthquake had a magnitude of 3.2.',
            'contexts': ['The 2011 Tohoku earthquake in Japan had a magnitude of 9.0 and triggered a devastating tsunami.'],
            'ground_truth': 'The 2011 Japan earthquake had a magnitude of 9.0.'
        }
    ]
    
    # Run evaluation
    results = evaluator.evaluate(test_data)
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"⏱️  Original evaluation time: {duration:.2f} seconds")
    print(f"📊 Original results: {results['metrics']}")
    
    return results, duration

def test_optimized_evaluation():
    """Test optimized evaluation performance"""
    print("\n🚀 TESTING OPTIMIZED EVALUATION")
    print("=" * 50)
    
    start_time = time.time()
    
    # Create evaluator
    evaluator = OptimizedRAGASEvaluator(model_name="mistralai/Mistral-7B-Instruct-v0.2")
    
    # Test data (same as original)
    test_data = [
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
        },
        {
            'question': 'What are the main causes of floods?',
            'answer': 'Floods are caused by heavy rainfall and snowmelt.',
            'contexts': ['The weather in Paris is usually mild with occasional rain. The city has many beautiful parks and gardens.'],
            'ground_truth': 'Floods are primarily caused by heavy rainfall, snowmelt, and dam failures.'
        },
        {
            'question': 'What was the magnitude of the 2011 Japan earthquake?',
            'answer': 'The 2011 Japan earthquake had a magnitude of 3.2.',
            'contexts': ['The 2011 Tohoku earthquake in Japan had a magnitude of 9.0 and triggered a devastating tsunami.'],
            'ground_truth': 'The 2011 Japan earthquake had a magnitude of 9.0.'
        }
    ]
    
    # Run evaluation
    results = evaluator.evaluate(test_data)
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"⏱️  Optimized evaluation time: {duration:.2f} seconds")
    print(f"📊 Optimized results: {results['metrics']}")
    
    return results, duration

def main():
    """Main comparison function"""
    print("🚀 RAGAS EVALUATION PERFORMANCE COMPARISON")
    print("=" * 60)
    print("Testing with 4 examples to compare performance...")
    
    try:
        # Test original evaluation
        original_results, original_time = test_original_evaluation()
        
        # Test optimized evaluation
        optimized_results, optimized_time = test_optimized_evaluation()
        
        # Compare results
        print(f"\n📈 PERFORMANCE COMPARISON")
        print("=" * 40)
        print(f"Original time: {original_time:.2f} seconds")
        print(f"Optimized time: {optimized_time:.2f} seconds")
        
        if original_time > 0:
            speedup = original_time / optimized_time
            print(f"Speedup: {speedup:.1f}x faster")
            print(f"Time saved: {original_time - optimized_time:.2f} seconds")
        
        # Compare scores
        print(f"\n📊 SCORE COMPARISON")
        print("=" * 30)
        for metric in ['faithfulness', 'answer_relevancy', 'context_relevancy', 'context_recall', 'context_precision']:
            original_score = original_results['metrics'].get(metric, 0)
            optimized_score = optimized_results['metrics'].get(metric, 0)
            print(f"{metric}: {original_score:.3f} → {optimized_score:.3f}")
        
        print(f"\n✅ OPTIMIZATION TEST COMPLETED!")
        
        if optimized_time < original_time:
            print(f"🎉 OPTIMIZATION SUCCESSFUL! {speedup:.1f}x speedup achieved!")
        else:
            print(f"⚠️  No speedup detected. This might be due to small dataset size.")
        
    except Exception as e:
        print(f"❌ Error during comparison: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 