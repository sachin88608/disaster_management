"""
Quick test script to verify RAGAS evaluation fixes work correctly.
This uses a small dataset to test the evaluation logic before running full experiments.
"""

import json
import pandas as pd
from datetime import datetime
import os
from ragas_evaluation import RAGASEvaluator

def create_mini_test_dataset():
    """Create a small test dataset with known good/bad examples"""
    test_data = [
        {
            'question': 'What is the magnitude of the 2015 Nepal earthquake?',
            'answer': 'The 2015 Nepal earthquake had a magnitude of 7.8 on the Richter scale.',
            'contexts': ['The 2015 Nepal earthquake occurred on April 25 with a magnitude of 7.8. It caused widespread damage in Kathmandu and surrounding areas.'],
            'ground_truth': 'The 2015 Nepal earthquake had a magnitude of 7.8.',
            'source': 'earthquake_data'
        },
        {
            'question': 'How many people died in the 2004 Indian Ocean tsunami?',
            'answer': 'The 2004 Indian Ocean tsunami caused approximately 230,000 deaths across 14 countries.',
            'contexts': ['The 2004 Indian Ocean tsunami was one of the deadliest natural disasters in recorded history, causing approximately 230,000 deaths across 14 countries.'],
            'ground_truth': 'The 2004 Indian Ocean tsunami caused approximately 230,000 deaths.',
            'source': 'tsunami_data'
        },
        {
            'question': 'What is the capital of France?',  # Bad example - not disaster related
            'answer': 'The capital of France is Paris.',
            'contexts': ['Paris is the capital and largest city of France. It is known for its culture, art, and cuisine.'],
            'ground_truth': 'Paris is the capital of France.',
            'source': 'general_knowledge'
        },
        {
            'question': 'What are the main causes of floods?',
            'answer': 'Floods are caused by heavy rainfall, snowmelt, and dam failures.',
            'contexts': ['Floods can be caused by various factors including heavy rainfall, rapid snowmelt, dam or levee failures, and storm surges.'],
            'ground_truth': 'Floods are primarily caused by heavy rainfall, snowmelt, and dam failures.',
            'source': 'flood_data'
        },
        {
            'question': 'What is the weather like today?',  # Very bad example
            'answer': 'I cannot provide current weather information.',
            'contexts': ['This is a disaster management chatbot focused on historical disaster data.'],
            'ground_truth': 'The chatbot should not provide current weather information.',
            'source': 'system_info'
        }
    ]
    return test_data

def test_evaluation_logic():
    """Test the evaluation logic with the mini dataset"""
    print("🧪 TESTING RAGAS EVALUATION FIXES")
    print("=" * 50)
    
    # Create mini test dataset
    test_data = create_mini_test_dataset()
    print(f"Created test dataset with {len(test_data)} examples")
    
    # Initialize evaluator
    print("\nInitializing RAGAS evaluator...")
    evaluator = RAGASEvaluator(model_name="mistralai/Mistral-7B-Instruct-v0.2")
    
    # Run evaluation
    print("Running evaluation...")
    results = evaluator.evaluate(test_data)
    
    if results and 'metrics' in results:
        print("\n✅ EVALUATION COMPLETED SUCCESSFULLY!")
        print("\n📊 RESULTS SUMMARY:")
        print("-" * 30)
        
        metrics = results['metrics']
        for metric_name, score in metrics.items():
            if metric_name != 'average_score':
                print(f"{metric_name.replace('_', ' ').title()}: {score:.3f}")
        
        print("-" * 30)
        print(f"Average Score: {metrics['average_score']:.3f}")
        
        # Analyze results
        print("\n🔍 ANALYSIS:")
        print("-" * 30)
        
        # Check if scores are realistic
        if metrics['context_recall'] < 0.9:
            print("✅ Context Recall looks realistic (not artificially high)")
        else:
            print("⚠️  Context Recall still seems too high")
            
        if metrics['context_relevancy'] < 0.9:
            print("✅ Context Relevancy looks realistic")
        else:
            print("⚠️  Context Relevancy still seems too high")
            
        if 0.2 <= metrics['faithfulness'] <= 0.8:
            print("✅ Faithfulness score looks realistic")
        else:
            print("⚠️  Faithfulness score seems unusual")
            
        # Check for variation
        score_variation = max(metrics.values()) - min([v for k, v in metrics.items() if k != 'average_score'])
        if score_variation > 0.2:
            print("✅ Good variation in scores (realistic)")
        else:
            print("⚠️  Scores are too similar (suspicious)")
            
        print("\n🎯 RECOMMENDATION:")
        if (metrics['context_recall'] < 0.9 and 
            metrics['context_relevancy'] < 0.9 and 
            score_variation > 0.2):
            print("✅ EVALUATION LOOKS GOOD! You can proceed with full experiments.")
        else:
            print("⚠️  Some issues detected. Check the evaluation logic further.")
            
    else:
        print("❌ EVALUATION FAILED!")
        print("Error:", results.get('error', 'Unknown error'))
    
    return results

def test_with_real_rag():
    """Test with actual RAG system responses"""
    print("\n" + "=" * 50)
    print("🧪 TESTING WITH REAL RAG SYSTEM")
    print("=" * 50)
    
    try:
        from rag_system import RAGSystem
        print("Initializing RAG system...")
        rag_system = RAGSystem()
        
        # Test questions
        test_questions = [
            "What was the magnitude of the 2015 Nepal earthquake?",
            "How many people died in the 2004 tsunami?",
            "What causes floods?"
        ]
        
        evaluation_data = []
        
        for i, question in enumerate(test_questions):
            print(f"\nProcessing question {i+1}: {question}")
            
            try:
                response = rag_system.query(question)
                answer = response['answer']
                contexts = [source['snippet'] for source in response['sources']]
                
                print(f"Answer: {answer[:100]}...")
                print(f"Contexts: {len(contexts)} retrieved")
                
                evaluation_data.append({
                    'question': question,
                    'answer': answer,
                    'contexts': contexts,
                    'ground_truth': 'Test ground truth',
                    'source': 'rag_system'
                })
                
            except Exception as e:
                print(f"Error processing question: {e}")
                continue
        
        if evaluation_data:
            print(f"\nRunning evaluation on {len(evaluation_data)} real examples...")
            evaluator = RAGASEvaluator(model_name="mistralai/Mistral-7B-Instruct-v0.2")
            results = evaluator.evaluate(evaluation_data)
            
            if results and 'metrics' in results:
                print("\n✅ REAL RAG EVALUATION COMPLETED!")
                metrics = results['metrics']
                print("\n📊 REAL RAG RESULTS:")
                print("-" * 30)
                for metric_name, score in metrics.items():
                    if metric_name != 'average_score':
                        print(f"{metric_name.replace('_', ' ').title()}: {score:.3f}")
                print(f"Average Score: {metrics['average_score']:.3f}")
            else:
                print("❌ Real RAG evaluation failed!")
        else:
            print("❌ No valid evaluation data generated from RAG system")
            
    except Exception as e:
        print(f"❌ Error testing with RAG system: {e}")

if __name__ == "__main__":
    # Test 1: Mini dataset
    results = test_evaluation_logic()
    
    # Test 2: Real RAG system (optional)
    try:
        test_with_real_rag()
    except Exception as e:
        print(f"Real RAG test skipped due to error: {e}")
    
    print("\n" + "=" * 50)
    print("🧪 TESTING COMPLETE!")
    print("=" * 50) 