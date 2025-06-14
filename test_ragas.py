import logging
from ragas_evaluation import RAGASEvaluator

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('test_ragas_debug.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Test dataset
test_data = [
    {
        'question': 'What are the main causes of floods?',
        'answer': 'Floods are caused by rainfall, poor drainage, or broken dams.',
        'contexts': [
            'Floods are caused by heavy rainfall, poor drainage, or dam failure.',
            'Climate change increases flood frequency and intensity.',
            'Urban development and deforestation can worsen flood impacts.'
        ],
        'ground_truth': 'Floods occur due to excessive rain, poor water management, and dam failures.'
    },
    {
        'question': 'How do earthquakes affect infrastructure?',
        'answer': 'Earthquakes damage buildings and roads, especially if they\'re not built to withstand shaking.',
        'contexts': [
            'Earthquakes can cause severe damage to buildings, bridges, and roads.',
            'The intensity of damage depends on the magnitude and depth of the earthquake.',
            'Poorly constructed buildings are most vulnerable to earthquake damage.'
        ],
        'ground_truth': 'Earthquakes can severely damage infrastructure, with the extent of damage depending on construction quality and earthquake magnitude.'
    }
]

def main():
    try:
        logger.info("Initializing RAGAS evaluator...")
        evaluator = RAGASEvaluator()
        
        logger.info("Running evaluation with test data...")
        logger.debug(f"Test data: {test_data}")
        
        results = evaluator.evaluate(test_data)
        
        logger.info("Evaluation completed!")
        logger.info("\nResults summary:")
        logger.info("=" * 50)
        for metric, score in results['metrics'].items():
            logger.info(f"{metric}: {score:.3f}")
            
    except Exception as e:
        logger.error(f"Error in main: {str(e)}")
        logger.error(f"Error traceback: {traceback.format_exc()}")
        raise

if __name__ == "__main__":
    main() 