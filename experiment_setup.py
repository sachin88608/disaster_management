"""
Experiment setup script for managing different embedding models efficiently.
This script helps set up separate vector stores for different embedding models.
"""

import os
import shutil
import logging
from config import Config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ExperimentSetup:
    """Class to manage experiment setup for different embedding models"""
    
    def __init__(self):
        self.config = Config()
        self.base_chroma_dir = "./chroma_db"
        
    def setup_embedding_experiment(self, embedding_model: str):
        """Setup vector store for a specific embedding model"""
        try:
            # Create experiment-specific directory
            experiment_dir = f"./chroma_db_{embedding_model.replace('-', '_')}"
            
            logger.info(f"Setting up experiment for embedding model: {embedding_model}")
            logger.info(f"Vector store directory: {experiment_dir}")
            
            # Update environment variables
            os.environ['EMBEDDING_MODEL'] = embedding_model
            os.environ['CHROMA_PERSIST_DIR'] = experiment_dir
            
            # Update config
            self.config.EMBEDDING_MODEL = embedding_model
            self.config.CHROMA_PERSIST_DIR = experiment_dir
            
            logger.info(f"Configuration updated for {embedding_model}")
            
            return experiment_dir
            
        except Exception as e:
            logger.error(f"Error setting up embedding experiment: {str(e)}")
            raise
    
    def run_setup_data(self, embedding_model: str, force_recreate=False):
        """Run setup_data.py with specific embedding model"""
        try:
            logger.info(f"Running setup_data.py for {embedding_model}...")
            
            # Setup the embedding model
            experiment_dir = self.setup_embedding_experiment(embedding_model)
            
            # Import and run setup_data
            from setup_data import main as setup_main
            
            # Run setup
            setup_main()
            
            logger.info(f"Setup completed for {embedding_model}")
            return experiment_dir
            
        except Exception as e:
            logger.error(f"Error running setup_data: {str(e)}")
            raise
    
    def list_experiments(self):
        """List all available experiments"""
        experiments = []
        
        # Check for existing experiment directories
        for item in os.listdir('.'):
            if item.startswith('chroma_db_'):
                embedding_model = item.replace('chroma_db_', '').replace('_', '-')
                experiments.append({
                    'embedding_model': embedding_model,
                    'directory': item,
                    'exists': True
                })
        
        # Add current default
        experiments.append({
            'embedding_model': 'all-MiniLM-L6-v2',
            'directory': 'chroma_db',
            'exists': os.path.exists('chroma_db')
        })
        
        return experiments

def main():
    """Main function to setup experiments"""
    try:
        setup = ExperimentSetup()
        
        print("🔧 Experiment Setup Tool")
        print("="*40)
        
        # List current experiments
        experiments = setup.list_experiments()
        print("\nCurrent experiments:")
        for exp in experiments:
            status = "✅ Ready" if exp['exists'] else "❌ Not setup"
            print(f"  {exp['embedding_model']}: {exp['directory']} ({status})")
        
        # Setup new experiments if needed
        embedding_models = [
            'all-MiniLM-L6-v2',      # Experiment 1 & 3
            'all-MiniLM-L12-v2',     # Experiment 2 & 4
            'bge-small-en-v1.5',     # Experiment 5
            'bge-base-en-v1.5'       # Experiment 6, 7, 8
        ]
        
        print(f"\nSetting up experiments for: {embedding_models}")
        
        for embedding_model in embedding_models:
            try:
                setup.run_setup_data(embedding_model, force_recreate=False)
                print(f"✅ Setup completed for {embedding_model}")
            except Exception as e:
                print(f"❌ Setup failed for {embedding_model}: {str(e)}")
        
        print("\n🎉 Experiment setup completed!")
        print("\nNext steps:")
        print("1. Run: python batch_experiments.py")
        print("2. Check results in: batch_experiment_results/")
        
    except Exception as e:
        logger.error(f"Error in main: {str(e)}")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 