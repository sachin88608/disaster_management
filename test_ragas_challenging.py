"""
Challenging test script with deliberately bad examples to verify RAGAS evaluation can properly score poor responses.
"""

import json
import pandas as pd
from datetime import datetime
import os
from ragas_evaluation import RAGASEvaluator

def create_challenging_test_dataset():
    """Create a test dataset with deliberately bad examples"""
    test_data = [
        # Example 1: Good example (should score high)
        {
            'question': 'What is the magnitude of the 2015 Nepal earthquake?',
            'answer': 'The 2015 Nepal earthquake had a magnitude of 7.8 on the Richter scale.',
            'contexts': ['The 2015 Nepal earthquake occurred on April 25 with a magnitude of 7.8. It caused widespread damage in Kathmandu and surrounding areas.'],
            'ground_truth': 'The 2015 Nepal earthquake had a magnitude of 7.8.',
            'source': 'earthquake_data'
        },
        # Example 2: Bad answer (should score low on faithfulness)
        {
            'question': 'How many people died in the 2004 Indian Ocean tsunami?',
            'answer': 'The 2004 tsunami killed about 50 people.',  # WRONG - should be ~230,000
            'contexts': ['The 2004 Indian Ocean tsunami was one of the deadliest natural disasters in recorded history, causing approximately 230,000 deaths across 14 countries.'],
            'ground_truth': 'The 2004 Indian Ocean tsunami caused approximately 230,000 deaths.',
            'source': 'tsunami_data'
        },
        # Example 3: Irrelevant context (should score low on context relevancy)
        {
            'question': 'What are the main causes of floods?',
            'answer': 'Floods are caused by heavy rainfall and snowmelt.',
            'contexts': ['The weather in Paris is usually mild with occasional rain. The city has many beautiful parks and gardens.'],  # IRRELEVANT
            'ground_truth': 'Floods are primarily caused by heavy rainfall, snowmelt, and dam failures.',
            'source': 'flood_data'
        },
        # Example 4: Completely wrong answer (should score very low)
        {
            'question': 'What was the magnitude of the 2011 Japan earthquake?',
            'answer': 'The 2011 Japan earthquake had a magnitude of 3.2.',  # WRONG - should be 9.0
            'contexts': ['The 2011 Tohoku earthquake in Japan had a magnitude of 9.0 and triggered a devastating tsunami.'],
            'ground_truth': 'The 2011 Japan earthquake had a magnitude of 9.0.',
            'source': 'earthquake_data'
        },
        # Example 5: Off-topic answer (should score low on answer relevancy)
        {
            'question': 'What are the warning signs of a tsunami?',
            'answer': 'I like pizza and ice cream. The weather is nice today.',  # COMPLETELY OFF-TOPIC
            'contexts': ['Tsunami warning signs include unusual ocean behavior, rapid water level changes, and earthquake activity near coastal areas.'],
            'ground_truth': 'Tsunami warning signs include unusual ocean behavior and rapid water level changes.',
            'source': 'tsunami_data'
        },
        # Example 6: Missing context (should score low on context recall)
        {
            'question': 'What was the death toll of Hurricane Katrina?',
            'answer': 'Hurricane Katrina caused significant damage.',
            'contexts': ['Hurricane Katrina was a powerful storm.'],  # MISSING DEATH TOLL INFO
            'ground_truth': 'Hurricane Katrina caused over 1,800 deaths.',
            'source': 'hurricane_data'
        },
        # Example 7: Vague answer (should score medium)
        {
            'question': 'What causes earthquakes?',
            'answer': 'Earthquakes are caused by various factors.',
            'contexts': ['Earthquakes are caused by the sudden release of energy in the Earth\'s crust, usually due to tectonic plate movements.'],
            'ground_truth': 'Earthquakes are caused by tectonic plate movements and the release of energy in the Earth\'s crust.',
            'source': 'earthquake_data'
        },
        # Example 8: Partially correct (should score medium)
        {
            'question': 'What are the effects of volcanic eruptions?',
            'answer': 'Volcanic eruptions can cause lava flows and ash clouds.',
            'contexts': ['Volcanic eruptions can cause lava flows, ash clouds, pyroclastic flows, and climate changes. They can also trigger tsunamis and earthquakes.'],
            'ground_truth': 'Volcanic eruptions can cause lava flows, ash clouds, pyroclastic flows, and climate changes.',
            'source': 'volcano_data'
        }
    ]
    return test_data

def test_challenging_evaluation():
    """Test the evaluation logic with challenging examples"""
    print("🧪 TESTING RAGAS EVALUATION WITH CHALLENGING EXAMPLES")
    print("=" * 60)
    
    # Create challenging test dataset
    test_data = create_challenging_test_dataset()
    print(f"Created challenging test dataset with {len(test_data)} examples")
    print("Examples include: good, bad, irrelevant, wrong, and off-topic responses")
    
    # Initialize evaluator
    print("\nInitializing RAGAS evaluator...")
    evaluator = RAGASEvaluator(model_name="google/gemma-2b-it")
    
    # Run evaluation
    print("Running evaluation...")
    results = evaluator.evaluate(test_data)
    
    if results and 'metrics' in results:
        print("\n✅ EVALUATION COMPLETED SUCCESSFULLY!")
        print("\n📊 RESULTS SUMMARY:")
        print("-" * 40)
        
        metrics = results['metrics']
        for metric_name, score in metrics.items():
            if metric_name != 'average_score':
                print(f"{metric_name.replace('_', ' ').title()}: {score:.3f}")
        
        print("-" * 40)
        print(f"Average Score: {metrics['average_score']:.3f}")
        
        # Detailed analysis
        print("\n🔍 DETAILED ANALYSIS:")
        print("-" * 40)
        
        # Check each metric
        if metrics['faithfulness'] < 0.8:
            print("✅ Faithfulness looks realistic (not artificially high)")
        else:
            print("⚠️  Faithfulness still seems too high for mixed quality data")
            
        if metrics['answer_relevancy'] < 0.9:
            print("✅ Answer Relevancy looks realistic")
        else:
            print("⚠️  Answer Relevancy still seems too high")
            
        if metrics['context_relevancy'] < 0.8:
            print("✅ Context Relevancy looks realistic")
        else:
            print("⚠️  Context Relevancy still seems too high")
            
        if 0.4 <= metrics['context_recall'] <= 0.8:
            print("✅ Context Recall looks realistic")
        else:
            print("⚠️  Context Recall seems unusual")
            
        if metrics['context_precision'] < 0.9:
            print("✅ Context Precision looks realistic")
        else:
            print("⚠️  Context Precision still seems too high")
        
        # Check for variation
        score_variation = max(metrics.values()) - min([v for k, v in metrics.items() if k != 'average_score'])
        if score_variation > 0.3:
            print("✅ Good variation in scores (realistic for mixed data)")
        else:
            print("⚠️  Scores are too similar (suspicious for mixed quality data)")
            
        # Overall assessment
        print("\n🎯 OVERALL ASSESSMENT:")
        print("-" * 40)
        
        realistic_scores = 0
        total_metrics = 5
        
        if metrics['faithfulness'] < 0.8: realistic_scores += 1
        if metrics['answer_relevancy'] < 0.9: realistic_scores += 1
        if metrics['context_relevancy'] < 0.8: realistic_scores += 1
        if 0.4 <= metrics['context_recall'] <= 0.8: realistic_scores += 1
        if metrics['context_precision'] < 0.9: realistic_scores += 1
        
        print(f"Realistic metrics: {realistic_scores}/{total_metrics}")
        
        if realistic_scores >= 4 and score_variation > 0.3:
            print("✅ EVALUATION LOOKS GOOD! You can proceed with full experiments.")
        elif realistic_scores >= 3:
            print("⚠️  EVALUATION IS MOSTLY GOOD. Some metrics still seem optimistic.")
            print("   You can proceed, but be aware scores might be slightly inflated.")
        else:
            print("❌ EVALUATION STILL HAS ISSUES. Check the evaluation logic further.")
            
    else:
        print("❌ EVALUATION FAILED!")
        print("Error:", results.get('error', 'Unknown error'))
    
    return results

def test_individual_examples():
    """Test individual examples to see detailed scoring"""
    print("\n" + "=" * 60)
    print("🧪 TESTING INDIVIDUAL EXAMPLES")
    print("=" * 60)
    
    evaluator = RAGASEvaluator(model_name="google/gemma-2b-it")
    test_data = create_challenging_test_dataset()
    
    print("Testing individual examples to see detailed scoring:")
    print("-" * 60)
    
    for i, example in enumerate(test_data[:3]):  # Test first 3 examples
        print(f"\nExample {i+1}: {example['question']}")
        print(f"Answer: {example['answer']}")
        print(f"Context: {example['contexts'][0][:100]}...")
        
        # Test individual metrics
        dataset = evaluator.prepare_dataset([example])
        
        faithfulness = evaluator._calculate_faithfulness(dataset)
        answer_relevancy = evaluator._calculate_answer_relevancy(dataset)
        context_relevancy = evaluator._calculate_context_relevancy(dataset)
        
        print(f"Scores - Faithfulness: {faithfulness:.3f}, Answer Relevancy: {answer_relevancy:.3f}, Context Relevancy: {context_relevancy:.3f}")

if __name__ == "__main__":
    # Test with challenging examples
    results = test_challenging_evaluation()
    
    # Test individual examples
    try:
        test_individual_examples()
    except Exception as e:
        print(f"Individual example test skipped due to error: {e}")
    
    print("\n" + "=" * 60)
    print("🧪 CHALLENGING TEST COMPLETE!")
    print("=" * 60) 