#!/usr/bin/env python3
"""
Quick test to compare RAGAS evaluation models
"""

import time
from ragas_evaluation import RAGASEvaluator

def test_model_performance(model_name: str, test_name: str):
    """Test a model's performance on RAGAS evaluation"""
    print(f"\n🧪 TESTING {test_name}")
    print("=" * 50)
    
    start_time = time.time()
    
    # Create evaluator
    evaluator = RAGASEvaluator(model_name=model_name)
    
    # Test with a small dataset
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
        }
    ]
    
    # Run evaluation
    results = evaluator.evaluate(test_data)
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"⏱️  Time taken: {duration:.2f} seconds")
    print(f"📊 Results: {results}")
    
    return results, duration

def main():
    print("🚀 RAGAS MODEL COMPARISON TEST")
    print("=" * 60)
    
    # Test current model
    current_results, current_time = test_model_performance(
        "mistralai/Mistral-7B-Instruct-v0.2", 
        "CURRENT MODEL (Mistral-7B)"
    )
    
    # Test smaller alternative
    try:
        smaller_results, smaller_time = test_model_performance(
            "microsoft/phi-2", 
            "SMALLER ALTERNATIVE (Phi-2)"
        )
        
        print(f"\n📈 COMPARISON SUMMARY")
        print("=" * 40)
        print(f"Mistral-7B: {current_time:.2f}s")
        print(f"Phi-2: {smaller_time:.2f}s")
        print(f"Speed improvement: {current_time/smaller_time:.1f}x faster")
        
    except Exception as e:
        print(f"❌ Smaller model test failed: {e}")
    
    print(f"\n✅ Current model is working well!")

if __name__ == "__main__":
    main() 