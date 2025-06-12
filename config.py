import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # GROQ Configuration
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = os.getenv("GROQ_MODEL", "llama3-70b-8192")
    
    # Embedding Configuration
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    
    # Vector Database Configuration
    CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "disaster_knowledge")
    
    # RAG Configuration
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    TOP_K_RESULTS = 5
    SIMILARITY_THRESHOLD = 0.5
    
    # Supported File Types
    SUPPORTED_EXTENSIONS = {'.pdf', '.csv', '.xlsx', '.xls', '.txt', '.md'}
    
    # Data Sources Configuration
    DATA_SOURCES = {
        'earthquake': {
            'urls': ['https://www.emdat.be',
                    'https://www.researchgate.net/publication/387765577_TE23D_A_Dataset_for_Earthquake_Damage_Assessment_and_Evaluation',
                    'https://earthquake.usgs.gov',
                    'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports',
                    'https://datascience.codata.org/articles/10.5334/dsj-2025-008',
                    'https://www.iitk.ac.in/nicee/wcee/article/14_01-1022.pdf',
                    'https://www.eeri.org/projects/earthquake-clearinghouse/',
                    'https://www.globalquakemodel.org/gem',
                    'https://ngawest2.berkeley.edu',
                    'https://ds.iris.edu/ds/nodes/dmc',
                    'https://data.humdata.org',
                    'https://reliefweb.int/disasters',
                    'https://arxiv.org/search/?query=earthquake&searchtype=all&abstracts=show',
                    'https://www.worldbank.org/en/topic/disasterriskmanagement',
                    'https://www.ngdc.noaa.gov/hazel/view/hazards/earthquake/event-data?maxYear=2025&minYear=1990',
                    'https://www.emsc-csem.org',
                    'https://earthquake.usgs.gov/data/shakemap/',
                    'https://gdacs.org',
                    'https://earthquake.usgs.gov/earthquakes/search/',
                    'https://reliefweb.int/disasters?_gl=1*juuxfq*_ga*NzI2NjIxNDEzLjE3NDk3NDE0MjA.*_ga_E60ZNX2F68*czE3NDk3NDE0MjAkbzEkZzEkdDE3NDk3NDE0NDgkajMyJGwwJGgw',
                    'https://reliefweb.int/disaster/fl-2025-000076-bgd',
                    'https://reliefweb.int/disaster/ep-2025-000062-ecu',
                    'https://earthquake.usgs.gov/fdsnws/event/1/',
                    'https://earthquake.usgs.gov/data/comcat/',
                    'https://earthquake.usgs.gov/earthquakes/map/',
                    'https://www.emsc-csem.org/',
                    'https://www.globalquakemodel.org/',
                    'https://platform.openquake.org/',
                    'https://www.ready.gov/earthquakes',
                    'https://ds.iris.edu/seismon/',
                    'https://www.ready.gov/earthquakes',
                    'https://www.gfdrr.org/en/publications',
                    'https://data.humdata.org/organization/gfdrr',
                    'https://www.kaggle.com/datasets/headsortails/us-natural-disaster-declarations',
                    'https://www.kaggle.com/datasets/naiyakhalid/flood-prediction-dataset',
                    'http://kaggle.com/datasets/umeradnaan/prediction-of-disaster-management-in-2024',
                    'https://www.kaggle.com/datasets/rgbnihal/c2a-dataset',
                    'https://www.kaggle.com/datasets/christianlillelund/passenger-list-for-the-estonia-ferry-disaster',
                    'https://www.kaggle.com/datasets/rupakroy/cyclone-wildfire-flood-earthquake-database',
                    'https://www.kaggle.com/datasets/fema/federal-disasters',
                    'http://kaggle.com/datasets/rahultp97/louisiana-flood-2016',
                    'https://www.kaggle.com/datasets/usgs/earthquake-database',
                    'https://www.iris.edu/hq/inclass',
                    'https://earthquake.usgs.gov/research/',
                    'https://reliefweb.int/updates?search=earthquake',
                    'https://sedac.ciesin.columbia.edu/data/collection/ndh',
                    'https://earthdata.nasa.gov/',
                    'https://www.who.int/health-topics/earthquakes#tab=tab_1',
                    'https://huggingface.co/datasets',
                    'https://paperswithcode.com/task/disaster-response',
                    'https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php',
                    'https://docs.google.com/spreadsheets/d/e/2PACX-1vQcVkjSTYsPCzoUuar82a_W4VmRClkzTtisFOrRAX3knhDGSlJoyBhp6ruKlgqqOz5cg7qCjL1Op4YH/pubhtml',
                    'https://data.humdata.org/dataset/?q=flood+disaster&sort=score+desc%2C+last_modified+desc&ext_page_size=25'
                    ],
            'files': ['data/earthquake/afghanistan-natural-disaster-incidents-from-january-to-may-2025.xlsx',
                    'data/earthquake/idmc_internal_displacement_conflict-violence_disasters-39.xlsx',
                    'data/earthquake/ht_climato-hydro-meteo_emdat_data-20220623.xlsx',
                    'data/earthquake/congo-admin1-flood.csv',
                    'data/earthquake/200204_philippines-2019-events-data.xlsx',
                    'data/earthquake/afghanistan-natural-disaster-incidents-from-january-to-september-2022.xlsx',
                    'data/earthquake/afghanistan-natural-disaster-incidents-from-january-to-december-2020.xlsx',
                    'data/earthquake/afghanistan-natural-disaster-incidents-from-january-to-july-2021.xlsx']
        },
        'flood': {
            'urls': [],
            'files': ['data/RS_Session_255_AU_887.1.csv',
                      'data/flood/public_emdat_data.xlsx',
                      'data/flood/WHO-COVID-19-global-daily-data.csv']
        }
    }
    
    # Future disaster types (ready for expansion)
    FUTURE_DISASTERS = ['drought', 'covid', 'wildfire', 'hurricane', 'tsunami']