#!/usr/bin/env python3
"""
Setup script to create sample data and initialize the RAG system
"""

import os
import pandas as pd
from pathlib import Path
import logging
from rag_system import RAGSystem
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_data_directory():
    """Create data directory structure"""
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    subdirs = ["earthquake", "flood", "processed"]
    for subdir in subdirs:
        (data_dir / subdir).mkdir(exist_ok=True)
    
    logger.info("Data directory structure created")

def create_sample_earthquake_data():
    """Create sample earthquake data"""
    
    # Sample earthquake CSV data
    earthquake_data = {
        'Date': ['2023-01-15', '2023-02-20', '2023-03-10', '2023-04-05', '2023-05-12'],
        'Location': ['California, USA', 'Tokyo, Japan', 'Turkey', 'Mexico', 'Indonesia'],
        'Magnitude': [6.2, 7.1, 7.8, 5.9, 6.7],
        'Depth_km': [10, 15, 8, 12, 20],
        'Casualties': [12, 156, 2847, 3, 89],
        'Description': [
            'Moderate earthquake causing minor structural damage in rural areas',
            'Major earthquake with significant building damage in urban Tokyo area',
            'Devastating earthquake causing widespread destruction and casualties',
            'Light earthquake felt widely but causing minimal damage',
            'Strong earthquake triggering landslides in mountainous regions'
        ],
        'Preparedness_Tips': [
            'Secure heavy furniture and practice drop-cover-hold drills',
            'Maintain emergency kits and establish family communication plans',
            'Reinforce building structures and create evacuation routes',
            'Stay informed about seismic activity and emergency procedures',
            'Prepare for aftershocks and potential secondary hazards like landslides'
        ]
    }
    
    df = pd.DataFrame(earthquake_data)
    df.to_csv('data/earthquake_data.csv', index=False)
    
    # Create earthquake information text file
    earthquake_info = """
# Earthquake Safety and Preparedness Guide

## What is an Earthquake?
An earthquake is the shaking of the surface of the Earth resulting from a sudden release of energy in the Earth's lithosphere that creates seismic waves.

## Before an Earthquake:
1. **Prepare an Emergency Kit**: Include water, food, flashlights, batteries, first aid supplies, medications, and important documents.

2. **Secure Your Home**: 
   - Bolt tall furniture to walls
   - Install latches on cabinets
   - Secure water heater and gas appliances
   - Identify safe spots in each room

3. **Create a Family Emergency Plan**:
   - Designate meeting places
   - Establish communication methods
   - Practice earthquake drills

4. **Learn About Your Area's Risk**: Understand local seismic activity and building codes.

## During an Earthquake:
1. **Drop, Cover, and Hold On**:
   - Drop to hands and knees
   - Take cover under a sturdy table or desk
   - Hold on to your shelter and protect your head

2. **If You're Outside**: Move away from buildings, trees, and power lines.

3. **If You're Driving**: Pull over safely, avoid bridges and overpasses.

4. **Stay Calm**: Don't run outside during shaking.

## After an Earthquake:
1. **Check for Injuries**: Provide first aid if needed.

2. **Inspect Your Home**: Look for damage to structure and utilities.

3. **Be Prepared for Aftershocks**: They can be as dangerous as the main quake.

4. **Listen to Emergency Information**: Use battery-powered radio for updates.

5. **Help Others**: Assist neighbors and community members if possible.

## Earthquake Magnitude Scale:
- **2.5 or less**: Usually not felt
- **2.5 to 5.4**: Often felt, minor damage
- **5.5 to 6.0**: Slight damage to buildings
- **6.1 to 6.9**: May cause significant damage
- **7.0 to 7.9**: Major earthquake, serious damage
- **8.0 or greater**: Great earthquake, can destroy communities

## Building Safety:
- Modern buildings are designed to withstand earthquakes
- Older buildings may need retrofitting
- Know your building's earthquake resistance
- Identify structural vs. non-structural hazards
"""
    
    with open('data/earthquake_info.txt', 'w') as f:
        f.write(earthquake_info)
    
    logger.info("Sample earthquake data created")

def create_sample_flood_data():
    """Create sample flood data"""
    
    # Sample flood CSV data
    flood_data = {
        'Date': ['2023-06-15', '2023-07-22', '2023-08-10', '2023-09-05', '2023-10-12'],
        'Location': ['Houston, Texas', 'Bangladesh', 'Germany', 'Pakistan', 'Philippines'],
        'Type': ['Flash Flood', 'River Flood', 'Urban Flood', 'Monsoon Flood', 'Coastal Flood'],
        'Duration_hours': [6, 168, 48, 336, 72],
        'Water_Level_ft': [8, 15, 4, 12, 6],
        'Affected_Population': [50000, 2000000, 150000, 1500000, 800000],
        'Description': [
            'Sudden flash flooding due to heavy rainfall overwhelming drainage systems',
            'Prolonged river flooding affecting vast agricultural and residential areas',
            'Urban flooding caused by inadequate drainage infrastructure during storms',
            'Extensive monsoon flooding affecting multiple provinces and districts',
            'Coastal flooding due to storm surge and high tides affecting island communities'
        ],
        'Prevention_Measures': [
            'Improve drainage systems and flood barriers in urban areas',
            'Implement early warning systems and river management strategies',
            'Upgrade stormwater infrastructure and green drainage solutions',
            'Develop flood-resistant infrastructure and evacuation procedures',
            'Build seawalls and implement coastal protection measures'
        ]
    }
    
    df = pd.DataFrame(flood_data)
    df.to_csv('data/flood_data.csv', index=False)
    
    # Create flood information text file
    flood_info = """
# Flood Safety and Preparedness Guide

## What is a Flood?
A flood is an overflow of water that submerges land that is usually dry. Floods can occur due to heavy rainfall, storm surge, dam failure, or rapid snowmelt.

## Types of Floods:
1. **Flash Floods**: Sudden flooding, usually within 6 hours of heavy rain
2. **River Floods**: Gradual rise in water levels over days or weeks
3. **Urban Floods**: Caused by overwhelmed drainage systems in cities
4. **Coastal Floods**: Result from storm surge, high tides, or tsunamis

## Before a Flood:
1. **Know Your Risk**: 
   - Understand flood zones in your area
   - Learn evacuation routes
   - Sign up for community alert systems

2. **Prepare an Emergency Kit**:
   - Water (1 gallon per person per day for 3 days)
   - Non-perishable food for 3 days
   - Battery-powered radio and flashlights
   - First aid kit and medications
   - Important documents in waterproof container

3. **Protect Your Property**:
   - Install sump pumps and backup power
   - Keep sandbags and plastic sheeting available
   - Elevate utilities above potential flood levels
   - Consider flood insurance

4. **Create a Family Plan**:
   - Designate meeting places
   - Plan evacuation routes
   - Identify higher ground locations

## During a Flood:
1. **Stay Safe**:
   - Never drive through flooded roads
   - Avoid walking in moving water
   - Stay away from downed power lines

2. **Monitor Conditions**:
   - Listen to weather radio or emergency broadcasts
   - Watch for rising water levels
   - Be ready to evacuate quickly

3. **If Evacuating**:
   - Take your emergency kit
   - Follow designated evacuation routes
   - Don't return until authorities say it's safe

## After a Flood:
1. **Safety First**:
   - Avoid flood waters (may be contaminated)
   - Check for structural damage before entering buildings
   - Use generators outside only (carbon monoxide risk)

2. **Document Damage**:
   - Take photos for insurance claims
   - Make temporary repairs to prevent further damage
   - Keep receipts for expenses

3. **Clean Up Safely**:
   - Wear protective gear
   - Discard contaminated materials
   - Disinfect everything that got wet

## Flood Safety Rules:
- **Turn Around, Don't Drown**: Just 6 inches of moving water can knock you down
- **2 feet of water can float a car**: Never drive through flooded roads
- **Stay informed**: Monitor weather and emergency alerts
- **Have multiple ways to receive warnings**: Weather radio, phone alerts, sirens

## Flood Insurance:
- Standard homeowner's insurance doesn't cover floods
- Federal flood insurance has a 30-day waiting period
- Document your belongings with photos/video
- Consider coverage for both building and contents
"""
    
    with open('data/flood_info.txt', 'w') as f:
        f.write(flood_info)
    
    logger.info("Sample flood data created")

def initialize_system(force_reprocess: bool = False):
    """Initialize the RAG system with all data sources"""
    try:
        rag_system = RAGSystem()
        
        # If force reprocess is True, reset the system
        if force_reprocess:
            logger.info("Force reprocessing all data...")
            rag_system.reset_system()
            existing_sources = []
        else:
            # Get existing sources from vector store
            existing_sources = rag_system.vector_store.get_existing_sources()
            logger.info(f"Found {len(existing_sources)} existing sources in vector store")
        
        # Get all data sources from config
        data_sources = rag_system.config.DATA_SOURCES
        
        # Filter out sources that are already processed (unless force_reprocess is True)
        new_data_sources = {}
        for disaster_type, sources in data_sources.items():
            new_sources = {'files': [], 'urls': []}
            
            # Check files
            if 'files' in sources:
                for file_path in sources['files']:
                    if force_reprocess or file_path not in existing_sources:
                        new_sources['files'].append(file_path)
                    else:
                        logger.info(f"Skipping existing file: {file_path}")
            
            # Check URLs
            if 'urls' in sources:
                for url in sources['urls']:
                    if force_reprocess or url not in existing_sources:
                        new_sources['urls'].append(url)
                    else:
                        logger.info(f"Skipping existing URL: {url}")
            
            # Only add disaster type if there are new sources
            if new_sources['files'] or new_sources['urls']:
                new_data_sources[disaster_type] = new_sources
        
        if not new_data_sources:
            logger.info("No new data sources to process. All data is up to date!")
            return True
        
        # Initialize with only new data sources
        results = rag_system.ingest_data_sources(new_data_sources)
        
        if results['failed_sources'] > 0:
            logger.warning(f"Some sources failed to process: {results['failed_sources']}")
        
        logger.info("System updated successfully!")
        logger.info(f"New documents processed: {results['total_documents']}")
        logger.info(f"Successful sources: {results['successful_sources']}")
        logger.info(f"Failed sources: {results['failed_sources']}")
        
        # Verify the system is ready
        stats = rag_system.get_system_stats()
        if stats['vector_store'].get('total_documents', 0) > 0:
            logger.info("Setup completed successfully!")
            logger.info("You can now run: streamlit run streamlit_app.py")
            return True
        else:
            logger.error("Setup failed: No documents were added to the vector store")
            return False
            
    except Exception as e:
        logger.error(f"Error during system initialization: {str(e)}")
        return False

def main():
    """Main function to set up the system"""
    try:
        # Parse command line arguments
        parser = argparse.ArgumentParser(description='Setup the RAG system with data')
        parser.add_argument('--force', action='store_true', 
                          help='Force reprocessing of all data, even if it exists in the vector store')
        args = parser.parse_args()
        
        logger.info("Starting data setup...")
        
        # Create data directory structure
        create_data_directory()
        
        # Initialize system with all data sources
        if initialize_system(force_reprocess=args.force):
            logger.info("Setup completed successfully!")
        else:
            logger.error("Setup failed. Please check the logs for details.")
            
    except Exception as e:
        logger.error(f"Setup failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()