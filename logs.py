INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:chromadb.telemetry.product.posthog:Anonymized telemetry enabled. See                     https://docs.trychroma.com/telemetry for more information.
INFO:vector_store:Loaded existing collection: disaster_knowledge
INFO:llm_interface:Initialized GROQ client with model: llama3-70b-8192
INFO:rag_system:RAG System initialized successfully
INFO:__main__:Force reprocessing all data...
INFO:vector_store:Collection reset successfully
INFO:rag_system:System reset successfully
INFO:rag_system:Processing data for disaster type: earthquake
INFO:data_ingestion:Processed Excel: data/earthquake/afghanistan-natural-disaster-incidents-from-january-to-may-2025.xlsx, Documents: 220
INFO:rag_system:Successfully processed 220 documents from data/earthquake/afghanistan-natural-disaster-incidents-from-january-to-may-2025.xlsx
INFO:data_ingestion:Processed Excel: data/earthquake/idmc_internal_displacement_conflict-violence_disasters-39.xlsx, Documents: 7556
INFO:rag_system:Successfully processed 7556 documents from data/earthquake/idmc_internal_displacement_conflict-violence_disasters-39.xlsx
INFO:data_ingestion:Processed Excel: data/earthquake/ht_climato-hydro-meteo_emdat_data-20220623.xlsx, Documents: 126
INFO:rag_system:Successfully processed 126 documents from data/earthquake/ht_climato-hydro-meteo_emdat_data-20220623.xlsx
INFO:data_ingestion:Processed CSV: data/earthquake/congo-admin1-flood.csv, Rows: 1990
INFO:rag_system:Successfully processed 1990 documents from data/earthquake/congo-admin1-flood.csv
INFO:data_ingestion:Processed Excel: data/earthquake/200204_philippines-2019-events-data.xlsx, Documents: 824
INFO:rag_system:Successfully processed 824 documents from data/earthquake/200204_philippines-2019-events-data.xlsx
INFO:data_ingestion:Processed Excel: data/earthquake/afghanistan-natural-disaster-incidents-from-january-to-september-2022.xlsx, Documents: 724
INFO:rag_system:Successfully processed 724 documents from data/earthquake/afghanistan-natural-disaster-incidents-from-january-to-september-2022.xlsx
INFO:data_ingestion:Processed Excel: data/earthquake/afghanistan-natural-disaster-incidents-from-january-to-december-2020.xlsx, Documents: 606
INFO:rag_system:Successfully processed 606 documents from data/earthquake/afghanistan-natural-disaster-incidents-from-january-to-december-2020.xlsx
INFO:data_ingestion:Processed Excel: data/earthquake/afghanistan-natural-disaster-incidents-from-january-to-july-2021.xlsx, Documents: 197
INFO:rag_system:Successfully processed 197 documents from data/earthquake/afghanistan-natural-disaster-incidents-from-january-to-july-2021.xlsx
INFO:rag_system:Successfully processed 1 documents from https://www.emdat.be
ERROR:data_ingestion:Error processing URL https://www.researchgate.net/publication/387765577_TE23D_A_Dataset_for_Earthquake_Damage_Assessment_and_Evaluation: 403 Client Error: Forbidden for url: https://www.researchgate.net/publication/387765577_TE23D_A_Dataset_for_Earthquake_Damage_Assessment_and_Evaluation
WARNING:rag_system:No documents extracted from https://www.researchgate.net/publication/387765577_TE23D_A_Dataset_for_Earthquake_Damage_Assessment_and_Evaluation
WARNING:rag_system:No documents extracted from https://earthquake.usgs.gov
INFO:rag_system:Successfully processed 1 documents from https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports
INFO:rag_system:Successfully processed 1 documents from https://datascience.codata.org/articles/10.5334/dsj-2025-008
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://www.iitk.ac.in/nicee/wcee/article/14_01-1022.pdf
INFO:rag_system:Successfully processed 1 documents from https://www.eeri.org/projects/earthquake-clearinghouse/
INFO:rag_system:Successfully processed 1 documents from https://www.globalquakemodel.org/gem
INFO:rag_system:Successfully processed 1 documents from https://ngawest2.berkeley.edu
INFO:rag_system:Successfully processed 1 documents from https://ds.iris.edu/ds/nodes/dmc
INFO:rag_system:Successfully processed 1 documents from https://data.humdata.org
INFO:rag_system:Successfully processed 1 documents from https://reliefweb.int/disasters
INFO:rag_system:Successfully processed 1 documents from https://arxiv.org/search/?query=earthquake&searchtype=all&abstracts=show
INFO:rag_system:Successfully processed 1 documents from https://www.worldbank.org/en/topic/disasterriskmanagement
INFO:rag_system:Successfully processed 1 documents from https://www.ngdc.noaa.gov/hazel/view/hazards/earthquake/event-data?maxYear=2025&minYear=1990
INFO:rag_system:Successfully processed 1 documents from https://www.emsc-csem.org
INFO:rag_system:Successfully processed 1 documents from https://earthquake.usgs.gov/data/shakemap/
INFO:rag_system:Successfully processed 1 documents from https://gdacs.org
INFO:rag_system:Successfully processed 1 documents from https://earthquake.usgs.gov/earthquakes/search/
INFO:rag_system:Successfully processed 1 documents from https://reliefweb.int/disasters?_gl=1*juuxfq*_ga*NzI2NjIxNDEzLjE3NDk3NDE0MjA.*_ga_E60ZNX2F68*czE3NDk3NDE0MjAkbzEkZzEkdDE3NDk3NDE0NDgkajMyJGwwJGgw
INFO:rag_system:Successfully processed 1 documents from https://reliefweb.int/disaster/fl-2025-000076-bgd
INFO:rag_system:Successfully processed 1 documents from https://reliefweb.int/disaster/ep-2025-000062-ecu
INFO:rag_system:Successfully processed 1 documents from https://earthquake.usgs.gov/fdsnws/event/1/
INFO:rag_system:Successfully processed 1 documents from https://earthquake.usgs.gov/data/comcat/
INFO:rag_system:Successfully processed 1 documents from https://earthquake.usgs.gov/earthquakes/map/
INFO:rag_system:Successfully processed 1 documents from https://www.emsc-csem.org/
INFO:rag_system:Successfully processed 1 documents from https://www.globalquakemodel.org/
INFO:rag_system:Successfully processed 1 documents from https://platform.openquake.org/
INFO:rag_system:Successfully processed 1 documents from https://www.ready.gov/earthquakes
INFO:rag_system:Successfully processed 1 documents from https://ds.iris.edu/seismon/
INFO:rag_system:Successfully processed 1 documents from https://www.ready.gov/earthquakes
INFO:rag_system:Successfully processed 1 documents from https://www.gfdrr.org/en/publications
ERROR:data_ingestion:Error processing URL https://data.humdata.org/organization/gfdrr: 404 Client Error: Not Found for url: https://data.humdata.org/organization/gfdrr
WARNING:rag_system:No documents extracted from https://data.humdata.org/organization/gfdrr
INFO:rag_system:Successfully processed 1 documents from https://www.kaggle.com/datasets/headsortails/us-natural-disaster-declarations
INFO:rag_system:Successfully processed 1 documents from https://www.kaggle.com/datasets/naiyakhalid/flood-prediction-dataset
INFO:rag_system:Successfully processed 1 documents from http://kaggle.com/datasets/umeradnaan/prediction-of-disaster-management-in-2024
INFO:rag_system:Successfully processed 1 documents from https://www.kaggle.com/datasets/rgbnihal/c2a-dataset
INFO:rag_system:Successfully processed 1 documents from https://www.kaggle.com/datasets/christianlillelund/passenger-list-for-the-estonia-ferry-disaster
INFO:rag_system:Successfully processed 1 documents from https://www.kaggle.com/datasets/rupakroy/cyclone-wildfire-flood-earthquake-database
INFO:rag_system:Successfully processed 1 documents from https://www.kaggle.com/datasets/fema/federal-disasters
INFO:rag_system:Successfully processed 1 documents from http://kaggle.com/datasets/rahultp97/louisiana-flood-2016
INFO:rag_system:Successfully processed 1 documents from https://www.kaggle.com/datasets/usgs/earthquake-database
INFO:rag_system:Successfully processed 1 documents from https://www.iris.edu/hq/inclass
WARNING:rag_system:No documents extracted from https://earthquake.usgs.gov/research/
INFO:rag_system:Successfully processed 1 documents from https://reliefweb.int/updates?search=earthquake
INFO:rag_system:Successfully processed 1 documents from https://sedac.ciesin.columbia.edu/data/collection/ndh
INFO:rag_system:Successfully processed 1 documents from https://earthdata.nasa.gov/
INFO:rag_system:Successfully processed 1 documents from https://www.who.int/health-topics/earthquakes#tab=tab_1
INFO:rag_system:Successfully processed 1 documents from https://huggingface.co/datasets
INFO:rag_system:Successfully processed 1 documents from https://paperswithcode.com/task/disaster-response
INFO:rag_system:Successfully processed 1 documents from https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
INFO:rag_system:Successfully processed 1 documents from https://docs.google.com/spreadsheets/d/e/2PACX-1vQcVkjSTYsPCzoUuar82a_W4VmRClkzTtisFOrRAX3knhDGSlJoyBhp6ruKlgqqOz5cg7qCjL1Op4YH/pubhtml
INFO:rag_system:Successfully processed 1 documents from https://data.humdata.org/dataset/?q=flood+disaster&sort=score+desc%2C+last_modified+desc&ext_page_size=25
INFO:vector_store:Starting to process 12292 documents
INFO:vector_store:Processing document batch 1 of 3
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/58 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▋                                                                                             | 1/58 [02:27<2:19:47, 147.14s/it]INFO:vector_store:Embedding progress: 1.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   3%|███▍                                                                                              | 2/58 [02:27<56:38, 60.69s/it]INFO:vector_store:Embedding progress: 3.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   5%|█████                                                                                             | 3/58 [02:27<30:26, 33.20s/it]INFO:vector_store:Embedding progress: 5.2%
INFO:vector_store:Embedding progress: 6.9%
INFO:vector_store:Embedding progress: 8.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|██████████▏                                                                                       | 6/58 [02:28<09:46, 11.28s/it]INFO:vector_store:Embedding progress: 10.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▊                                                                                      | 7/58 [02:28<07:18,  8.60s/it]INFO:vector_store:Embedding progress: 12.1%
INFO:vector_store:Embedding progress: 13.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▏                                                                                  | 9/58 [02:28<04:12,  5.15s/it]INFO:vector_store:Embedding progress: 15.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  17%|████████████████▋                                                                                | 10/58 [02:29<03:26,  4.31s/it]INFO:vector_store:Embedding progress: 17.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  19%|██████████████████▍                                                                              | 11/58 [02:29<02:34,  3.30s/it]INFO:vector_store:Embedding progress: 19.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  21%|████████████████████                                                                             | 12/58 [02:49<05:45,  7.51s/it]INFO:vector_store:Embedding progress: 20.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████▋                                                                           | 13/58 [02:50<04:12,  5.62s/it]INFO:vector_store:Embedding progress: 22.4%
INFO:vector_store:Embedding progress: 24.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████                                                                        | 15/58 [02:50<02:21,  3.30s/it]INFO:vector_store:Embedding progress: 25.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|██████████████████████████▊                                                                      | 16/58 [02:50<01:48,  2.58s/it]INFO:vector_store:Embedding progress: 27.6%
INFO:vector_store:Embedding progress: 29.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  31%|██████████████████████████████                                                                   | 18/58 [02:51<01:04,  1.60s/it]INFO:vector_store:Embedding progress: 31.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  33%|███████████████████████████████▊                                                                 | 19/58 [02:51<00:49,  1.27s/it]INFO:vector_store:Embedding progress: 32.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|█████████████████████████████████▍                                                               | 20/58 [02:51<00:38,  1.01s/it]INFO:vector_store:Embedding progress: 34.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|███████████████████████████████████                                                              | 21/58 [02:51<00:30,  1.22it/s]INFO:vector_store:Embedding progress: 36.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 37.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▍                                                          | 23/58 [03:11<02:44,  4.70s/it]INFO:vector_store:Embedding progress: 39.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  41%|████████████████████████████████████████▏                                                        | 24/58 [03:11<02:04,  3.66s/it]INFO:vector_store:Embedding progress: 41.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  43%|█████████████████████████████████████████▊                                                       | 25/58 [03:37<04:58,  9.05s/it]INFO:vector_store:Embedding progress: 43.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  45%|███████████████████████████████████████████▍                                                     | 26/58 [03:44<04:33,  8.54s/it]INFO:vector_store:Embedding progress: 44.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  47%|█████████████████████████████████████████████▏                                                   | 27/58 [03:44<03:17,  6.38s/it]INFO:vector_store:Embedding progress: 46.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▊                                                  | 28/58 [03:47<02:39,  5.32s/it]INFO:vector_store:Embedding progress: 48.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 29/58 [03:47<01:51,  3.83s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▏                                              | 30/58 [03:47<01:17,  2.76s/it]INFO:vector_store:Embedding progress: 51.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  53%|███████████████████████████████████████████████████▊                                             | 31/58 [03:48<00:58,  2.17s/it]INFO:vector_store:Embedding progress: 53.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  55%|█████████████████████████████████████████████████████▌                                           | 32/58 [03:48<00:40,  1.57s/it]INFO:vector_store:Embedding progress: 55.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  57%|███████████████████████████████████████████████████████▏                                         | 33/58 [03:49<00:33,  1.33s/it]INFO:vector_store:Embedding progress: 56.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  59%|████████████████████████████████████████████████████████▊                                        | 34/58 [04:07<02:33,  6.38s/it]INFO:vector_store:Embedding progress: 58.6%
INFO:vector_store:Embedding progress: 60.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|████████████████████████████████████████████████████████████▏                                    | 36/58 [04:13<01:46,  4.85s/it]INFO:vector_store:Embedding progress: 62.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|█████████████████████████████████████████████████████████████▉                                   | 37/58 [04:14<01:21,  3.87s/it]INFO:vector_store:Embedding progress: 63.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|███████████████████████████████████████████████████████████████▌                                 | 38/58 [04:25<01:55,  5.76s/it]INFO:vector_store:Embedding progress: 65.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  67%|█████████████████████████████████████████████████████████████████▏                               | 39/58 [04:28<01:30,  4.79s/it]INFO:vector_store:Embedding progress: 67.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  69%|██████████████████████████████████████████████████████████████████▉                              | 40/58 [04:34<01:32,  5.14s/it]INFO:vector_store:Embedding progress: 69.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:  71%|████████████████████████████████████████████████████████████████████▌                            | 41/58 [04:34<01:03,  3.73s/it]INFO:vector_store:Embedding progress: 70.7%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:  72%|██████████████████████████████████████████████████████████████████████▏                          | 42/58 [04:34<00:43,  2.70s/it]INFO:vector_store:Embedding progress: 72.4%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 74.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|█████████████████████████████████████████████████████████████████████████▌                       | 44/58 [04:36<00:27,  1.95s/it]INFO:vector_store:Embedding progress: 75.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|███████████████████████████████████████████████████████████████████████████▎                     | 45/58 [04:37<00:22,  1.75s/it]INFO:vector_store:Embedding progress: 77.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  79%|████████████████████████████████████████████████████████████████████████████▉                    | 46/58 [04:38<00:17,  1.42s/it]INFO:vector_store:Embedding progress: 79.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  81%|██████████████████████████████████████████████████████████████████████████████▌                  | 47/58 [04:38<00:12,  1.11s/it]INFO:vector_store:Embedding progress: 81.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  83%|████████████████████████████████████████████████████████████████████████████████▎                | 48/58 [04:38<00:08,  1.14it/s]INFO:vector_store:Embedding progress: 82.8%
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▉               | 49/58 [04:46<00:25,  2.88s/it]INFO:vector_store:Embedding progress: 84.5%
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▌             | 50/58 [04:48<00:21,  2.70s/it]INFO:vector_store:Embedding progress: 86.2%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▎           | 51/58 [04:49<00:13,  1.97s/it]INFO:vector_store:Embedding progress: 87.9%
Creating embeddings:  90%|██████████████████████████████████████████████████████████████████████████████████████▉          | 52/58 [04:52<00:13,  2.27s/it]INFO:vector_store:Embedding progress: 89.7%
Creating embeddings:  91%|████████████████████████████████████████████████████████████████████████████████████████▋        | 53/58 [04:53<00:09,  1.91s/it]INFO:vector_store:Embedding progress: 91.4%
Creating embeddings:  93%|██████████████████████████████████████████████████████████████████████████████████████████▎      | 54/58 [04:53<00:05,  1.42s/it]INFO:vector_store:Embedding progress: 93.1%
INFO:vector_store:Embedding progress: 94.8%
Creating embeddings:  97%|█████████████████████████████████████████████████████████████████████████████████████████████▋   | 56/58 [04:54<00:01,  1.08it/s]INFO:vector_store:Embedding progress: 96.6%
Creating embeddings:  98%|███████████████████████████████████████████████████████████████████████████████████████████████▎ | 57/58 [04:54<00:00,  1.30it/s]INFO:vector_store:Embedding progress: 98.3%
INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 58/58 [04:54<00:00,  5.08s/it]
INFO:vector_store:Processed 1000 chunks so far
INFO:vector_store:Processed 2000 chunks so far
INFO:vector_store:Processed 3000 chunks so far
INFO:vector_store:Processed 4000 chunks so far
INFO:vector_store:Processed 5000 chunks so far
INFO:vector_store:Processed 5730 chunks so far
INFO:vector_store:Processing document batch 2 of 3
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/50 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▉                                                                                             | 1/50 [01:47<1:27:50, 107.56s/it]INFO:vector_store:Embedding progress: 2.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                              | 2/50 [01:48<35:40, 44.60s/it]INFO:vector_store:Embedding progress: 4.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▉                                                                                            | 3/50 [01:48<19:09, 24.46s/it]INFO:vector_store:Embedding progress: 6.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▊                                                                                          | 4/50 [01:48<11:25, 14.90s/it]INFO:vector_store:Embedding progress: 8.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▊                                                                                        | 5/50 [01:49<07:14,  9.65s/it]INFO:vector_store:Embedding progress: 10.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▊                                                                                      | 6/50 [01:49<04:42,  6.42s/it]INFO:vector_store:Embedding progress: 12.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▋                                                                                    | 7/50 [01:49<03:08,  4.37s/it]INFO:vector_store:Embedding progress: 14.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 16.0%
INFO:vector_store:Embedding progress: 18.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 20.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████▎                                                                           | 11/50 [01:49<01:00,  1.55s/it]INFO:vector_store:Embedding progress: 22.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 24.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▏                                                                       | 13/50 [02:10<02:41,  4.36s/it]INFO:vector_store:Embedding progress: 26.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▏                                                                     | 14/50 [02:11<02:12,  3.69s/it]INFO:vector_store:Embedding progress: 28.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|█████████████████████████████                                                                    | 15/50 [02:12<01:49,  3.12s/it]INFO:vector_store:Embedding progress: 30.0%
INFO:vector_store:Embedding progress: 32.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|████████████████████████████████▉                                                                | 17/50 [02:12<01:07,  2.03s/it]INFO:vector_store:Embedding progress: 34.0%
INFO:vector_store:Embedding progress: 36.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 38.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▊                                                          | 20/50 [02:12<00:34,  1.16s/it]INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▋                                                        | 21/50 [02:12<00:28,  1.01it/s]INFO:vector_store:Embedding progress: 42.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 44.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████▌                                                    | 23/50 [02:14<00:23,  1.16it/s]INFO:vector_store:Embedding progress: 46.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▌                                                  | 24/50 [02:28<01:30,  3.48s/it]INFO:vector_store:Embedding progress: 48.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 25/50 [02:31<01:23,  3.33s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▍                                              | 26/50 [02:32<01:08,  2.84s/it]INFO:vector_store:Embedding progress: 52.0%
INFO:vector_store:Embedding progress: 54.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|██████████████████████████████████████████████████████▎                                          | 28/50 [02:33<00:39,  1.79s/it]INFO:vector_store:Embedding progress: 56.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|████████████████████████████████████████████████████████▎                                        | 29/50 [02:33<00:31,  1.49s/it]INFO:vector_store:Embedding progress: 58.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 30/50 [02:33<00:23,  1.19s/it]INFO:vector_store:Embedding progress: 60.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|████████████████████████████████████████████████████████████▏                                    | 31/50 [02:35<00:23,  1.25s/it]INFO:vector_store:Embedding progress: 62.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|██████████████████████████████████████████████████████████████                                   | 32/50 [02:39<00:35,  1.96s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|████████████████████████████████████████████████████████████████                                 | 33/50 [02:43<00:43,  2.56s/it]INFO:vector_store:Embedding progress: 66.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▉                               | 34/50 [02:45<00:39,  2.49s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|███████████████████████████████████████████████████████████████████▉                             | 35/50 [02:49<00:42,  2.83s/it]INFO:vector_store:Embedding progress: 70.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▊                           | 36/50 [02:50<00:31,  2.28s/it]INFO:vector_store:Embedding progress: 72.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|███████████████████████████████████████████████████████████████████████▊                         | 37/50 [02:51<00:24,  1.89s/it]INFO:vector_store:Embedding progress: 74.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|█████████████████████████████████████████████████████████████████████████▋                       | 38/50 [02:51<00:17,  1.46s/it]INFO:vector_store:Embedding progress: 76.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|███████████████████████████████████████████████████████████████████████████▋                     | 39/50 [02:52<00:12,  1.16s/it]INFO:vector_store:Embedding progress: 78.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|█████████████████████████████████████████████████████████████████████████████▌                   | 40/50 [02:52<00:09,  1.11it/s]INFO:vector_store:Embedding progress: 80.0%
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▌                 | 41/50 [02:52<00:06,  1.31it/s]INFO:vector_store:Embedding progress: 82.0%
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▍               | 42/50 [02:53<00:05,  1.56it/s]INFO:vector_store:Embedding progress: 84.0%
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▍             | 43/50 [02:54<00:05,  1.24it/s]INFO:vector_store:Embedding progress: 86.0%
HTTP Error 429 thrown while requesting HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json
WARNING:huggingface_hub.utils._http:HTTP Error 429 thrown while requesting HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json
Retrying in 1s [Retry 1/5].
WARNING:huggingface_hub.utils._http:Retrying in 1s [Retry 1/5].
HTTP Error 429 thrown while requesting HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json
WARNING:huggingface_hub.utils._http:HTTP Error 429 thrown while requesting HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json
Retrying in 2s [Retry 2/5].
WARNING:huggingface_hub.utils._http:Retrying in 2s [Retry 2/5].
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▎           | 44/50 [02:56<00:06,  1.15s/it]INFO:vector_store:Embedding progress: 88.0%
HTTP Error 429 thrown while requesting HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json
WARNING:huggingface_hub.utils._http:HTTP Error 429 thrown while requesting HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json
Retrying in 4s [Retry 3/5].
WARNING:huggingface_hub.utils._http:Retrying in 4s [Retry 3/5].
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▎         | 45/50 [02:57<00:06,  1.31s/it]INFO:vector_store:Embedding progress: 90.0%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▏       | 46/50 [03:01<00:07,  1.88s/it]INFO:vector_store:Embedding progress: 92.0%
Creating embeddings:  94%|███████████████████████████████████████████████████████████████████████████████████████████▏     | 47/50 [03:01<00:04,  1.39s/it]INFO:vector_store:Embedding progress: 94.0%
Creating embeddings:  96%|█████████████████████████████████████████████████████████████████████████████████████████████    | 48/50 [03:01<00:02,  1.03s/it]INFO:vector_store:Embedding progress: 96.0%
HTTP Error 429 thrown while requesting HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json
WARNING:huggingface_hub.utils._http:HTTP Error 429 thrown while requesting HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json
Retrying in 8s [Retry 4/5].
WARNING:huggingface_hub.utils._http:Retrying in 8s [Retry 4/5].
Creating embeddings:  98%|███████████████████████████████████████████████████████████████████████████████████████████████  | 49/50 [03:05<00:01,  1.94s/it]INFO:vector_store:Embedding progress: 98.0%
HTTP Error 429 thrown while requesting HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json
WARNING:huggingface_hub.utils._http:HTTP Error 429 thrown while requesting HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json
Retrying in 8s [Retry 5/5].
WARNING:huggingface_hub.utils._http:Retrying in 8s [Retry 5/5].
HTTP Error 429 thrown while requesting HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json
WARNING:huggingface_hub.utils._http:HTTP Error 429 thrown while requesting HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [03:24<00:00,  7.07s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [03:24<00:00,  4.09s/it]
INFO:vector_store:Processed 6730 chunks so far
INFO:vector_store:Processed 7730 chunks so far
INFO:vector_store:Processed 8730 chunks so far
INFO:vector_store:Processed 9730 chunks so far
INFO:vector_store:Processed 10703 chunks so far
INFO:vector_store:Processing document batch 3 of 3
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/31 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   3%|███                                                                                            | 1/31 [02:52<1:26:23, 172.78s/it]INFO:vector_store:Embedding progress: 3.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|██████▎                                                                                           | 2/31 [02:54<34:56, 72.30s/it]INFO:vector_store:Embedding progress: 6.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▍                                                                                        | 3/31 [02:55<18:26, 39.52s/it]INFO:vector_store:Embedding progress: 9.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  13%|████████████▋                                                                                     | 4/31 [02:56<11:02, 24.55s/it]INFO:vector_store:Embedding progress: 12.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▊                                                                                  | 5/31 [03:31<12:12, 28.17s/it]INFO:vector_store:Embedding progress: 16.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  19%|██████████████████▉                                                                               | 6/31 [03:32<07:52, 18.90s/it]INFO:vector_store:Embedding progress: 19.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  23%|██████████████████████▏                                                                           | 7/31 [03:32<05:06, 12.78s/it]INFO:vector_store:Embedding progress: 22.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▎                                                                        | 8/31 [03:32<03:22,  8.78s/it]INFO:vector_store:Embedding progress: 25.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  29%|████████████████████████████▍                                                                     | 9/31 [03:33<02:17,  6.24s/it]INFO:vector_store:Embedding progress: 29.0%
INFO:vector_store:Embedding progress: 32.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  35%|██████████████████████████████████▍                                                              | 11/31 [03:33<01:07,  3.38s/it]INFO:vector_store:Embedding progress: 35.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  39%|█████████████████████████████████████▌                                                           | 12/31 [03:34<00:49,  2.62s/it]INFO:vector_store:Embedding progress: 38.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▋                                                        | 13/31 [03:34<00:36,  2.03s/it]INFO:vector_store:Embedding progress: 41.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 45.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▉                                                  | 15/31 [03:34<00:18,  1.18s/it]INFO:vector_store:Embedding progress: 48.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████                                               | 16/31 [04:04<01:58,  7.87s/it]INFO:vector_store:Embedding progress: 51.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  55%|█████████████████████████████████████████████████████▏                                           | 17/31 [04:06<01:29,  6.42s/it]INFO:vector_store:Embedding progress: 54.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|████████████████████████████████████████████████████████▎                                        | 18/31 [04:07<01:05,  5.02s/it]INFO:vector_store:Embedding progress: 58.1%
INFO:vector_store:Embedding progress: 61.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|██████████████████████████████████████████████████████████████▌                                  | 20/31 [04:09<00:36,  3.28s/it]INFO:vector_store:Embedding progress: 64.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▋                               | 21/31 [04:10<00:27,  2.71s/it]INFO:vector_store:Embedding progress: 67.7%
Creating embeddings:  71%|████████████████████████████████████████████████████████████████████▊                            | 22/31 [04:11<00:20,  2.28s/it]INFO:vector_store:Embedding progress: 71.0%
Creating embeddings:  74%|███████████████████████████████████████████████████████████████████████▉                         | 23/31 [04:30<00:54,  6.79s/it]INFO:vector_store:Embedding progress: 74.2%
Creating embeddings:  77%|███████████████████████████████████████████████████████████████████████████                      | 24/31 [04:33<00:40,  5.75s/it]INFO:vector_store:Embedding progress: 77.4%
Creating embeddings:  81%|██████████████████████████████████████████████████████████████████████████████▏                  | 25/31 [04:46<00:45,  7.64s/it]INFO:vector_store:Embedding progress: 80.6%
INFO:vector_store:Embedding progress: 83.9%
Creating embeddings:  87%|████████████████████████████████████████████████████████████████████████████████████▍            | 27/31 [04:46<00:17,  4.32s/it]INFO:vector_store:Embedding progress: 87.1%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▌         | 28/31 [04:57<00:17,  5.82s/it]INFO:vector_store:Embedding progress: 90.3%
Creating embeddings:  94%|██████████████████████████████████████████████████████████████████████████████████████████▋      | 29/31 [04:57<00:09,  4.51s/it]INFO:vector_store:Embedding progress: 93.5%
Creating embeddings:  97%|█████████████████████████████████████████████████████████████████████████████████████████████▊   | 30/31 [04:57<00:03,  3.36s/it]INFO:vector_store:Embedding progress: 96.8%
INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 31/31 [04:57<00:00,  9.61s/it]
INFO:vector_store:Processed 11703 chunks so far
INFO:vector_store:Processed 12703 chunks so far
INFO:vector_store:Processed 13703 chunks so far
INFO:vector_store:Processed 13727 chunks so far
INFO:vector_store:Completed processing 12292 documents into 13727 chunks
INFO:rag_system:Successfully ingested 12292 documents for earthquake
INFO:rag_system:Processing data for disaster type: flood
INFO:data_ingestion:Processed CSV: data/RS_Session_255_AU_887.1.csv, Rows: 21
INFO:rag_system:Successfully processed 21 documents from data/RS_Session_255_AU_887.1.csv
WARNING:rag_system:File not found: data/flood/public_emdat_data.xlsx
WARNING:rag_system:File not found: data/flood/WHO-COVID-19-global-daily-data.csv
WARNING:rag_system:File not found: data/flood/28_e80340_TCP21(2024 edition).pdfdata/flood/61_245057_Cyclone Warning SOP Booklet final.pdf
INFO:data_ingestion:Processed PDF: data/flood/61_d385f4_FINAL SOP 2024_December.pdf, Pages: 265
INFO:rag_system:Successfully processed 265 documents from data/flood/61_d385f4_FINAL SOP 2024_December.pdf
INFO:data_ingestion:Processed PDF: data/flood/71_7d2c29_MARINE SOP.pdf, Pages: 102
INFO:rag_system:Successfully processed 102 documents from data/flood/71_7d2c29_MARINE SOP.pdf
INFO:data_ingestion:Processed PDF: data/flood/72_211daa_bulletin_sop.pdf, Pages: 62
INFO:rag_system:Successfully processed 62 documents from data/flood/72_211daa_bulletin_sop.pdf
INFO:data_ingestion:Processed CSV: data/flood/flood_risk_dataset_india.csv, Rows: 10000
INFO:rag_system:Successfully processed 10000 documents from data/flood/flood_risk_dataset_india.csv
INFO:data_ingestion:Processed Excel: data/flood/s_fld_haz_ar.xls, Documents: 2950
INFO:rag_system:Successfully processed 2950 documents from data/flood/s_fld_haz_ar.xls
INFO:data_ingestion:Processed CSV: data/flood/District_FloodedArea.csv, Rows: 732
INFO:rag_system:Successfully processed 732 documents from data/flood/District_FloodedArea.csv
INFO:data_ingestion:Processed CSV: data/flood/District_FloodImpact.csv, Rows: 732
INFO:rag_system:Successfully processed 732 documents from data/flood/District_FloodImpact.csv
INFO:data_ingestion:Processed CSV: data/flood/India_Flood_Inventory_v3.csv, Rows: 6876
INFO:rag_system:Successfully processed 6876 documents from data/flood/India_Flood_Inventory_v3.csv
ERROR:data_ingestion:Error processing CSV data/flood/allocation-partners-un-19july2011.csv: 'utf-8' codec can't decode byte 0xa3 in position 132: invalid start byte
WARNING:rag_system:No documents extracted from data/flood/allocation-partners-un-19july2011.csv
INFO:data_ingestion:Processed CSV: data/flood/cyberFlood_1104.csv, Rows: 2712
INFO:rag_system:Successfully processed 2712 documents from data/flood/cyberFlood_1104.csv
INFO:data_ingestion:Processed CSV: data/flood/Floodplains_Outline.csv, Rows: 1664
INFO:rag_system:Successfully processed 1664 documents from data/flood/Floodplains_Outline.csv
INFO:data_ingestion:Processed CSV: data/flood/flood.csv, Rows: 50000
INFO:rag_system:Successfully processed 50000 documents from data/flood/flood.csv
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://ndem.nrsc.gov.in/documents/downloads/Flood%20Affected%20Area%20%20Atlas%20of%20India%20-Satellite%20based%20study.pdf
INFO:rag_system:Successfully processed 1 documents from https://data.jrc.ec.europa.eu/dataset/1d128b6c-a4ee-4858-9e34-6210707f3c81
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://saarc-sdmc.org/sites/default/files/programmes_doc_upload/SDMC_Day2_Lect2_Hands_on_OpenDataPortals.pdf
INFO:rag_system:Successfully processed 1 documents from https://environment.data.gov.uk/flood-planning/download/cycle-2/
INFO:rag_system:Successfully processed 1 documents from https://public.emdat.be/
INFO:rag_system:Successfully processed 1 documents from https://ndmindia.mha.gov.in/ndmi/whatNewSituation
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://ndmindia.mha.gov.in/ndmi/viewUploadedDocument?uid=NEW2568
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://ndmindia.mha.gov.in/ndmi/viewUploadedDocument?uid=NEW2567
INFO:rag_system:Successfully processed 1 documents from https://internal.imd.gov.in/pages/press_release_mausam.php
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://internal.imd.gov.in/press_release/20250608_pr_4040.pdf
INFO:rag_system:Successfully processed 1 documents from https://indiawris.gov.in/wiki/doku.php?id=cwc_national_flood_forecasting_network#:~:text=Central%20Water%20Commission%20through%20its,Barrage%20Authorities%2F%20District%20Magistrates%2F%20Sub
INFO:rag_system:Successfully processed 1 documents from https://rsmcnewdelhi.imd.gov.in/report.php?internal_menu=NjE=
INFO:rag_system:Successfully processed 1 documents from https://rsmcnewdelhi.imd.gov.in/report.php?internal_menu=NzE=
INFO:rag_system:Successfully processed 1 documents from https://rsmcnewdelhi.imd.gov.in/report.php?internal_menu=NzI=
INFO:rag_system:Successfully processed 1 documents from https://www.ndma.gov.in/Natural-Hazards/Floods
INFO:rag_system:Successfully processed 1 documents from https://www.ndma.gov.in/Natural-Hazards/Cyclone
INFO:rag_system:Successfully processed 1 documents from https://www.ndma.gov.in/Natural-Hazards/Tsunami
INFO:rag_system:Successfully processed 1 documents from https://www.ndma.gov.in/Natural-Hazards/Urban-Floods
ERROR:data_ingestion:Error processing URL https://tsunami.incois.gov.in/TEWS/National.jsp: HTTPSConnectionPool(host='tsunami.incois.gov.in', port=443): Max retries exceeded with url: /TEWS/National.jsp (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)')))
WARNING:rag_system:No documents extracted from https://tsunami.incois.gov.in/TEWS/National.jsp
INFO:rag_system:Successfully processed 1 documents from https://waterwatch.usgs.gov/index.php?id=ww_flood
INFO:rag_system:Successfully processed 1 documents from https://waterwatch.usgs.gov/index.php?id=ww_drought
INFO:rag_system:Successfully processed 1 documents from https://zenodo.org/records/7545697
INFO:rag_system:Successfully processed 1 documents from https://urs.earthdata.nasa.gov/profile
INFO:rag_system:Successfully processed 1 documents from https://ndma.gov.in/Natural-Hazards/Urban-Floods
INFO:rag_system:Successfully processed 1 documents from https://ndma.gov.in/Natural-Hazards/Floods
INFO:vector_store:Starting to process 76140 documents
INFO:vector_store:Processing document batch 1 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/55 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▋                                                                                             | 1/55 [02:28<2:13:34, 148.41s/it]INFO:vector_store:Embedding progress: 1.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▌                                                                                              | 2/55 [02:34<57:09, 64.71s/it]INFO:vector_store:Embedding progress: 3.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   5%|█████▎                                                                                            | 3/55 [02:41<33:06, 38.19s/it]INFO:vector_store:Embedding progress: 5.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   7%|███████▏                                                                                          | 4/55 [02:45<21:09, 24.90s/it]INFO:vector_store:Embedding progress: 7.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   9%|████████▉                                                                                         | 5/55 [02:46<13:35, 16.30s/it]INFO:vector_store:Embedding progress: 9.1%
Creating embeddings:  11%|██████████▋                                                                                       | 6/55 [02:46<08:48, 10.79s/it]INFO:vector_store:Embedding progress: 10.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  13%|████████████▍                                                                                     | 7/55 [02:47<06:06,  7.63s/it]INFO:vector_store:Embedding progress: 12.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  15%|██████████████▎                                                                                   | 8/55 [02:48<04:11,  5.34s/it]INFO:vector_store:Embedding progress: 14.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|████████████████                                                                                  | 9/55 [02:48<02:52,  3.75s/it]INFO:vector_store:Embedding progress: 16.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▋                                                                               | 10/55 [02:49<02:03,  2.74s/it]INFO:vector_store:Embedding progress: 18.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 20.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████▏                                                                           | 12/55 [03:20<06:16,  8.76s/it]INFO:vector_store:Embedding progress: 21.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|██████████████████████▉                                                                          | 13/55 [03:30<06:26,  9.19s/it]INFO:vector_store:Embedding progress: 23.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  25%|████████████████████████▋                                                                        | 14/55 [03:33<05:04,  7.42s/it]INFO:vector_store:Embedding progress: 25.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  27%|██████████████████████████▍                                                                      | 15/55 [03:43<05:27,  8.18s/it]INFO:vector_store:Embedding progress: 27.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  29%|████████████████████████████▏                                                                    | 16/55 [03:45<04:06,  6.33s/it]INFO:vector_store:Embedding progress: 29.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  31%|█████████████████████████████▉                                                                   | 17/55 [03:47<03:19,  5.25s/it]INFO:vector_store:Embedding progress: 30.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 32.7%
INFO:vector_store:Embedding progress: 34.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|███████████████████████████████████▎                                                             | 20/55 [03:47<01:24,  2.41s/it]INFO:vector_store:Embedding progress: 36.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|█████████████████████████████████████                                                            | 21/55 [03:48<01:05,  1.93s/it]INFO:vector_store:Embedding progress: 38.2%
INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▌                                                        | 23/55 [04:13<03:11,  6.00s/it]INFO:vector_store:Embedding progress: 41.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|██████████████████████████████████████████▎                                                      | 24/55 [04:24<03:39,  7.09s/it]INFO:vector_store:Embedding progress: 43.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  45%|████████████████████████████████████████████                                                     | 25/55 [04:28<03:10,  6.36s/it]INFO:vector_store:Embedding progress: 45.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  47%|█████████████████████████████████████████████▊                                                   | 26/55 [04:38<03:27,  7.15s/it]INFO:vector_store:Embedding progress: 47.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  49%|███████████████████████████████████████████████▌                                                 | 27/55 [04:39<02:38,  5.64s/it]INFO:vector_store:Embedding progress: 49.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  51%|█████████████████████████████████████████████████▍                                               | 28/55 [04:43<02:20,  5.19s/it]INFO:vector_store:Embedding progress: 50.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  53%|███████████████████████████████████████████████████▏                                             | 29/55 [04:45<01:50,  4.25s/it]INFO:vector_store:Embedding progress: 52.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  55%|████████████████████████████████████████████████████▉                                            | 30/55 [04:45<01:17,  3.08s/it]INFO:vector_store:Embedding progress: 54.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|██████████████████████████████████████████████████████▋                                          | 31/55 [04:45<00:54,  2.26s/it]INFO:vector_store:Embedding progress: 56.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 58.2%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 33/55 [04:46<00:30,  1.38s/it]INFO:vector_store:Embedding progress: 60.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|███████████████████████████████████████████████████████████▉                                     | 34/55 [05:06<02:05,  5.99s/it]INFO:vector_store:Embedding progress: 61.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|█████████████████████████████████████████████████████████████▋                                   | 35/55 [05:20<02:40,  8.00s/it]INFO:vector_store:Embedding progress: 63.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|███████████████████████████████████████████████████████████████▍                                 | 36/55 [05:24<02:12,  6.99s/it]INFO:vector_store:Embedding progress: 65.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  67%|█████████████████████████████████████████████████████████████████▎                               | 37/55 [05:36<02:27,  8.19s/it]INFO:vector_store:Embedding progress: 67.3%
Creating embeddings:  69%|███████████████████████████████████████████████████████████████████                              | 38/55 [05:36<01:40,  5.89s/it]INFO:vector_store:Embedding progress: 69.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  71%|████████████████████████████████████████████████████████████████████▊                            | 39/55 [05:41<01:31,  5.73s/it]INFO:vector_store:Embedding progress: 70.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  73%|██████████████████████████████████████████████████████████████████████▌                          | 40/55 [05:42<01:06,  4.43s/it]INFO:vector_store:Embedding progress: 72.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  75%|████████████████████████████████████████████████████████████████████████▎                        | 41/55 [05:43<00:47,  3.38s/it]INFO:vector_store:Embedding progress: 74.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|██████████████████████████████████████████████████████████████████████████                       | 42/55 [05:43<00:31,  2.43s/it]INFO:vector_store:Embedding progress: 76.4%
INFO:vector_store:Embedding progress: 78.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|█████████████████████████████████████████████████████████████████████████████▌                   | 44/55 [05:44<00:15,  1.38s/it]INFO:vector_store:Embedding progress: 80.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▎                 | 45/55 [06:03<00:59,  5.90s/it]INFO:vector_store:Embedding progress: 81.8%
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▏               | 46/55 [06:14<01:04,  7.15s/it]INFO:vector_store:Embedding progress: 83.6%
Creating embeddings:  85%|██████████████████████████████████████████████████████████████████████████████████▉              | 47/55 [06:18<00:50,  6.26s/it]INFO:vector_store:Embedding progress: 85.5%
Creating embeddings:  87%|████████████████████████████████████████████████████████████████████████████████████▋            | 48/55 [06:26<00:46,  6.66s/it]INFO:vector_store:Embedding progress: 87.3%
Creating embeddings:  89%|██████████████████████████████████████████████████████████████████████████████████████▍          | 49/55 [06:27<00:31,  5.24s/it]INFO:vector_store:Embedding progress: 89.1%
Creating embeddings:  91%|████████████████████████████████████████████████████████████████████████████████████████▏        | 50/55 [06:28<00:18,  3.77s/it]INFO:vector_store:Embedding progress: 90.9%
Creating embeddings:  93%|█████████████████████████████████████████████████████████████████████████████████████████▉       | 51/55 [06:31<00:14,  3.55s/it]INFO:vector_store:Embedding progress: 92.7%
Creating embeddings:  95%|███████████████████████████████████████████████████████████████████████████████████████████▋     | 52/55 [06:31<00:08,  2.69s/it]INFO:vector_store:Embedding progress: 94.5%
Creating embeddings:  96%|█████████████████████████████████████████████████████████████████████████████████████████████▍   | 53/55 [06:31<00:03,  1.97s/it]INFO:vector_store:Embedding progress: 96.4%
INFO:vector_store:Embedding progress: 98.2%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 55/55 [06:32<00:00,  1.10s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 55/55 [06:32<00:00,  7.13s/it]
INFO:vector_store:Processed 1000 chunks so far
INFO:vector_store:Processed 2000 chunks so far
INFO:vector_store:Processed 3000 chunks so far
INFO:vector_store:Processed 4000 chunks so far
INFO:vector_store:Processed 5000 chunks so far
INFO:vector_store:Processed 5472 chunks so far
INFO:vector_store:Processing document batch 2 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/50 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▉                                                                                             | 1/50 [02:24<1:58:08, 144.66s/it]INFO:vector_store:Embedding progress: 2.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                              | 2/50 [02:25<48:00, 60.01s/it]INFO:vector_store:Embedding progress: 4.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▉                                                                                            | 3/50 [02:26<26:00, 33.20s/it]INFO:vector_store:Embedding progress: 6.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▊                                                                                          | 4/50 [02:27<15:44, 20.52s/it]INFO:vector_store:Embedding progress: 8.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 10.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▊                                                                                      | 6/50 [02:27<07:06,  9.69s/it]INFO:vector_store:Embedding progress: 12.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▋                                                                                    | 7/50 [02:28<05:05,  7.09s/it]INFO:vector_store:Embedding progress: 14.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 16.0%
INFO:vector_store:Embedding progress: 18.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████▍                                                                             | 10/50 [02:28<02:11,  3.30s/it]INFO:vector_store:Embedding progress: 20.0%
INFO:vector_store:Embedding progress: 22.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▎                                                                         | 12/50 [03:17<06:36, 10.44s/it]INFO:vector_store:Embedding progress: 24.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▏                                                                       | 13/50 [03:20<05:33,  9.01s/it]INFO:vector_store:Embedding progress: 26.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▏                                                                     | 14/50 [03:22<04:35,  7.64s/it]INFO:vector_store:Embedding progress: 28.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|█████████████████████████████                                                                    | 15/50 [03:25<03:47,  6.51s/it]INFO:vector_store:Embedding progress: 30.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|███████████████████████████████                                                                  | 16/50 [03:26<02:53,  5.10s/it]INFO:vector_store:Embedding progress: 32.0%
INFO:vector_store:Embedding progress: 34.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|██████████████████████████████████▉                                                              | 18/50 [03:26<01:35,  3.00s/it]INFO:vector_store:Embedding progress: 36.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▊                                                            | 19/50 [03:27<01:12,  2.33s/it]INFO:vector_store:Embedding progress: 38.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▊                                                          | 20/50 [03:27<00:53,  1.79s/it]INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▋                                                        | 21/50 [03:27<00:39,  1.38s/it]INFO:vector_store:Embedding progress: 42.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 44.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████▌                                                    | 23/50 [04:07<04:14,  9.41s/it]INFO:vector_store:Embedding progress: 46.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▌                                                  | 24/50 [04:11<03:31,  8.14s/it]INFO:vector_store:Embedding progress: 48.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 25/50 [04:16<02:59,  7.19s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▍                                              | 26/50 [04:24<02:57,  7.41s/it]INFO:vector_store:Embedding progress: 52.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|████████████████████████████████████████████████████▍                                            | 27/50 [04:25<02:15,  5.87s/it]INFO:vector_store:Embedding progress: 54.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|██████████████████████████████████████████████████████▎                                          | 28/50 [04:26<01:34,  4.29s/it]INFO:vector_store:Embedding progress: 56.0%
INFO:vector_store:Embedding progress: 58.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 30/50 [04:26<00:49,  2.50s/it]INFO:vector_store:Embedding progress: 60.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 62.0%
Creating embeddings:  64%|██████████████████████████████████████████████████████████████                                   | 32/50 [04:26<00:27,  1.55s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|████████████████████████████████████████████████████████████████                                 | 33/50 [04:26<00:21,  1.24s/it]INFO:vector_store:Embedding progress: 66.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▉                               | 34/50 [05:00<02:23,  8.98s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|███████████████████████████████████████████████████████████████████▉                             | 35/50 [05:04<01:54,  7.60s/it]INFO:vector_store:Embedding progress: 70.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▊                           | 36/50 [05:07<01:31,  6.55s/it]INFO:vector_store:Embedding progress: 72.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|███████████████████████████████████████████████████████████████████████▊                         | 37/50 [05:21<01:49,  8.40s/it]INFO:vector_store:Embedding progress: 74.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|█████████████████████████████████████████████████████████████████████████▋                       | 38/50 [05:23<01:19,  6.63s/it]INFO:vector_store:Embedding progress: 76.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|███████████████████████████████████████████████████████████████████████████▋                     | 39/50 [05:23<00:53,  4.82s/it]INFO:vector_store:Embedding progress: 78.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|█████████████████████████████████████████████████████████████████████████████▌                   | 40/50 [05:24<00:35,  3.52s/it]INFO:vector_store:Embedding progress: 80.0%
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▌                 | 41/50 [05:24<00:22,  2.52s/it]INFO:vector_store:Embedding progress: 82.0%
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▍               | 42/50 [05:24<00:15,  1.94s/it]INFO:vector_store:Embedding progress: 84.0%
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▍             | 43/50 [05:24<00:10,  1.43s/it]INFO:vector_store:Embedding progress: 86.0%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▎           | 44/50 [05:25<00:06,  1.08s/it]INFO:vector_store:Embedding progress: 88.0%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▎         | 45/50 [05:43<00:31,  6.24s/it]INFO:vector_store:Embedding progress: 90.0%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▏       | 46/50 [05:45<00:20,  5.11s/it]INFO:vector_store:Embedding progress: 92.0%
Creating embeddings:  94%|███████████████████████████████████████████████████████████████████████████████████████████▏     | 47/50 [05:47<00:11,  3.96s/it]INFO:vector_store:Embedding progress: 94.0%
Creating embeddings:  96%|█████████████████████████████████████████████████████████████████████████████████████████████    | 48/50 [05:51<00:07,  3.96s/it]INFO:vector_store:Embedding progress: 96.0%
Creating embeddings:  98%|███████████████████████████████████████████████████████████████████████████████████████████████  | 49/50 [05:51<00:02,  3.00s/it]INFO:vector_store:Embedding progress: 98.0%
INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [05:52<00:00,  7.04s/it]
INFO:vector_store:Processed 6472 chunks so far
INFO:vector_store:Processed 7472 chunks so far
INFO:vector_store:Processed 8472 chunks so far
INFO:vector_store:Processed 9472 chunks so far
INFO:vector_store:Processed 10472 chunks so far
INFO:vector_store:Processing document batch 3 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/51 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▊                                                                                             | 1/51 [02:07<1:46:39, 128.00s/it]INFO:vector_store:Embedding progress: 2.0%
Creating embeddings:   4%|███▊                                                                                              | 2/51 [02:08<43:06, 52.78s/it]INFO:vector_store:Embedding progress: 3.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▊                                                                                            | 3/51 [02:10<23:54, 29.88s/it]INFO:vector_store:Embedding progress: 5.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▋                                                                                          | 4/51 [02:11<14:30, 18.51s/it]INFO:vector_store:Embedding progress: 7.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▌                                                                                        | 5/51 [02:12<09:14, 12.05s/it]INFO:vector_store:Embedding progress: 9.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▌                                                                                      | 6/51 [02:14<06:28,  8.64s/it]INFO:vector_store:Embedding progress: 11.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▍                                                                                    | 7/51 [02:17<04:56,  6.73s/it]INFO:vector_store:Embedding progress: 13.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▎                                                                                  | 8/51 [02:19<03:48,  5.32s/it]INFO:vector_store:Embedding progress: 15.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▎                                                                                | 9/51 [02:20<02:40,  3.82s/it]INFO:vector_store:Embedding progress: 17.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████                                                                              | 10/51 [02:22<02:17,  3.35s/it]INFO:vector_store:Embedding progress: 19.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|████████████████████▉                                                                            | 11/51 [02:22<01:35,  2.40s/it]INFO:vector_store:Embedding progress: 21.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|██████████████████████▊                                                                          | 12/51 [02:42<05:06,  7.85s/it]INFO:vector_store:Embedding progress: 23.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  25%|████████████████████████▋                                                                        | 13/51 [02:44<03:42,  5.85s/it]INFO:vector_store:Embedding progress: 25.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  27%|██████████████████████████▋                                                                      | 14/51 [02:48<03:18,  5.35s/it]INFO:vector_store:Embedding progress: 27.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  29%|████████████████████████████▌                                                                    | 15/51 [02:49<02:30,  4.17s/it]INFO:vector_store:Embedding progress: 29.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  31%|██████████████████████████████▍                                                                  | 16/51 [02:52<02:07,  3.65s/it]INFO:vector_store:Embedding progress: 31.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  33%|████████████████████████████████▎                                                                | 17/51 [02:54<01:45,  3.10s/it]INFO:vector_store:Embedding progress: 33.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  35%|██████████████████████████████████▏                                                              | 18/51 [02:57<01:44,  3.18s/it]INFO:vector_store:Embedding progress: 35.3%
INFO:vector_store:Embedding progress: 37.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  39%|██████████████████████████████████████                                                           | 20/51 [02:58<00:59,  1.93s/it]INFO:vector_store:Embedding progress: 39.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  41%|███████████████████████████████████████▉                                                         | 21/51 [02:59<00:53,  1.78s/it]INFO:vector_store:Embedding progress: 41.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  43%|█████████████████████████████████████████▊                                                       | 22/51 [03:03<01:03,  2.20s/it]INFO:vector_store:Embedding progress: 43.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  45%|███████████████████████████████████████████▋                                                     | 23/51 [03:22<03:10,  6.81s/it]INFO:vector_store:Embedding progress: 45.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  47%|█████████████████████████████████████████████▋                                                   | 24/51 [03:23<02:20,  5.20s/it]INFO:vector_store:Embedding progress: 47.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  49%|███████████████████████████████████████████████▌                                                 | 25/51 [03:29<02:21,  5.44s/it]INFO:vector_store:Embedding progress: 49.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  51%|█████████████████████████████████████████████████▍                                               | 26/51 [03:37<02:33,  6.13s/it]INFO:vector_store:Embedding progress: 51.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  53%|███████████████████████████████████████████████████▎                                             | 27/51 [03:40<02:10,  5.45s/it]INFO:vector_store:Embedding progress: 52.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  55%|█████████████████████████████████████████████████████▎                                           | 28/51 [03:42<01:36,  4.18s/it]INFO:vector_store:Embedding progress: 54.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  57%|███████████████████████████████████████████████████████▏                                         | 29/51 [03:45<01:25,  3.88s/it]INFO:vector_store:Embedding progress: 56.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  59%|█████████████████████████████████████████████████████████                                        | 30/51 [03:46<01:04,  3.07s/it]INFO:vector_store:Embedding progress: 58.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:  61%|██████████████████████████████████████████████████████████▉                                      | 31/51 [03:46<00:44,  2.20s/it]INFO:vector_store:Embedding progress: 60.8%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 62.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|██████████████████████████████████████████████████████████████▊                                  | 33/51 [03:47<00:23,  1.31s/it]INFO:vector_store:Embedding progress: 64.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  67%|████████████████████████████████████████████████████████████████▋                                | 34/51 [03:47<00:19,  1.16s/it]INFO:vector_store:Embedding progress: 66.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  69%|██████████████████████████████████████████████████████████████████▌                              | 35/51 [03:49<00:22,  1.42s/it]INFO:vector_store:Embedding progress: 68.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  71%|████████████████████████████████████████████████████████████████████▍                            | 36/51 [03:54<00:33,  2.22s/it]INFO:vector_store:Embedding progress: 70.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  73%|██████████████████████████████████████████████████████████████████████▎                          | 37/51 [03:56<00:32,  2.34s/it]INFO:vector_store:Embedding progress: 72.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  75%|████████████████████████████████████████████████████████████████████████▎                        | 38/51 [03:59<00:32,  2.47s/it]INFO:vector_store:Embedding progress: 74.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:  76%|██████████████████████████████████████████████████████████████████████████▏                      | 39/51 [03:59<00:21,  1.80s/it]INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 76.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|████████████████████████████████████████████████████████████████████████████                     | 40/51 [04:02<00:20,  1.88s/it]INFO:vector_store:Embedding progress: 78.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|█████████████████████████████████████████████████████████████████████████████▉                   | 41/51 [04:03<00:16,  1.67s/it]INFO:vector_store:Embedding progress: 80.4%
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▉                 | 42/51 [04:03<00:11,  1.32s/it]INFO:vector_store:Embedding progress: 82.4%
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▊               | 43/51 [04:04<00:09,  1.13s/it]INFO:vector_store:Embedding progress: 84.3%
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▋             | 44/51 [04:04<00:06,  1.14it/s]INFO:vector_store:Embedding progress: 86.3%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▌           | 45/51 [04:05<00:05,  1.13it/s]INFO:vector_store:Embedding progress: 88.2%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▍         | 46/51 [04:06<00:04,  1.24it/s]INFO:vector_store:Embedding progress: 90.2%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▍       | 47/51 [04:07<00:04,  1.07s/it]INFO:vector_store:Embedding progress: 92.2%
Creating embeddings:  94%|███████████████████████████████████████████████████████████████████████████████████████████▎     | 48/51 [04:09<00:03,  1.16s/it]INFO:vector_store:Embedding progress: 94.1%
Creating embeddings:  96%|█████████████████████████████████████████████████████████████████████████████████████████████▏   | 49/51 [04:17<00:06,  3.41s/it]INFO:vector_store:Embedding progress: 96.1%
Creating embeddings:  98%|███████████████████████████████████████████████████████████████████████████████████████████████  | 50/51 [04:18<00:02,  2.45s/it]INFO:vector_store:Embedding progress: 98.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 51/51 [04:21<00:00,  2.76s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 51/51 [04:21<00:00,  5.13s/it]
INFO:vector_store:Processed 11472 chunks so far
INFO:vector_store:Processed 12472 chunks so far
INFO:vector_store:Processed 13472 chunks so far
INFO:vector_store:Processed 14472 chunks so far
INFO:vector_store:Processed 15472 chunks so far
INFO:vector_store:Processed 15525 chunks so far
INFO:vector_store:Processing document batch 4 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/52 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▊                                                                                             | 1/52 [02:20<1:59:20, 140.40s/it]INFO:vector_store:Embedding progress: 1.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▊                                                                                              | 2/52 [02:20<48:18, 57.96s/it]INFO:vector_store:Embedding progress: 3.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▋                                                                                            | 3/52 [02:21<26:13, 32.11s/it]INFO:vector_store:Embedding progress: 5.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▌                                                                                          | 4/52 [02:23<15:52, 19.84s/it]INFO:vector_store:Embedding progress: 7.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 9.6%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▎                                                                                      | 6/52 [02:23<07:11,  9.38s/it]INFO:vector_store:Embedding progress: 11.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  13%|█████████████▏                                                                                    | 7/52 [02:23<05:11,  6.93s/it]INFO:vector_store:Embedding progress: 13.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 15.4%
INFO:vector_store:Embedding progress: 17.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  19%|██████████████████▋                                                                              | 10/52 [02:23<02:14,  3.21s/it]INFO:vector_store:Embedding progress: 19.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 21.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  23%|██████████████████████▍                                                                          | 12/52 [03:11<06:46, 10.16s/it]INFO:vector_store:Embedding progress: 23.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  25%|████████████████████████▎                                                                        | 13/52 [03:15<05:50,  8.99s/it]INFO:vector_store:Embedding progress: 25.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  27%|██████████████████████████                                                                       | 14/52 [03:22<05:23,  8.52s/it]INFO:vector_store:Embedding progress: 26.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  29%|███████████████████████████▉                                                                     | 15/52 [03:22<04:05,  6.64s/it]INFO:vector_store:Embedding progress: 28.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  31%|█████████████████████████████▊                                                                   | 16/52 [03:24<03:10,  5.29s/it]INFO:vector_store:Embedding progress: 30.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  33%|███████████████████████████████▋                                                                 | 17/52 [03:24<02:22,  4.08s/it]INFO:vector_store:Embedding progress: 32.7%
INFO:vector_store:Embedding progress: 34.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  37%|███████████████████████████████████▍                                                             | 19/52 [03:24<01:17,  2.35s/it]INFO:vector_store:Embedding progress: 36.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|█████████████████████████████████████▎                                                           | 20/52 [03:25<00:58,  1.82s/it]INFO:vector_store:Embedding progress: 38.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|███████████████████████████████████████▏                                                         | 21/52 [03:25<00:43,  1.41s/it]INFO:vector_store:Embedding progress: 40.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|█████████████████████████████████████████                                                        | 22/52 [03:25<00:33,  1.12s/it]INFO:vector_store:Embedding progress: 42.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|██████████████████████████████████████████▉                                                      | 23/52 [04:06<05:48, 12.03s/it]INFO:vector_store:Embedding progress: 44.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████▊                                                    | 24/52 [04:09<04:26,  9.53s/it]INFO:vector_store:Embedding progress: 46.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▋                                                  | 25/52 [04:19<04:20,  9.65s/it]INFO:vector_store:Embedding progress: 48.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 26/52 [04:22<03:23,  7.82s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▎                                              | 27/52 [04:23<02:23,  5.73s/it]INFO:vector_store:Embedding progress: 51.9%
INFO:vector_store:Embedding progress: 53.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|██████████████████████████████████████████████████████                                           | 29/52 [04:23<01:13,  3.20s/it]INFO:vector_store:Embedding progress: 55.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|███████████████████████████████████████████████████████▉                                         | 30/52 [04:24<00:54,  2.47s/it]INFO:vector_store:Embedding progress: 57.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|█████████████████████████████████████████████████████████▊                                       | 31/52 [04:25<00:46,  2.21s/it]INFO:vector_store:Embedding progress: 59.6%
INFO:vector_store:Embedding progress: 61.5%
INFO:vector_store:Embedding progress: 63.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|███████████████████████████████████████████████████████████████▍                                 | 34/52 [04:56<01:55,  6.41s/it]INFO:vector_store:Embedding progress: 65.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  67%|█████████████████████████████████████████████████████████████████▎                               | 35/52 [05:02<01:47,  6.30s/it]INFO:vector_store:Embedding progress: 67.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  69%|███████████████████████████████████████████████████████████████████▏                             | 36/52 [05:12<01:54,  7.17s/it]INFO:vector_store:Embedding progress: 69.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  71%|█████████████████████████████████████████████████████████████████████                            | 37/52 [05:22<01:58,  7.88s/it]INFO:vector_store:Embedding progress: 71.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  73%|██████████████████████████████████████████████████████████████████████▉                          | 38/52 [05:24<01:28,  6.31s/it]INFO:vector_store:Embedding progress: 73.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  75%|████████████████████████████████████████████████████████████████████████▊                        | 39/52 [05:24<01:02,  4.83s/it]INFO:vector_store:Embedding progress: 75.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  77%|██████████████████████████████████████████████████████████████████████████▌                      | 40/52 [05:26<00:46,  3.90s/it]INFO:vector_store:Embedding progress: 76.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  79%|████████████████████████████████████████████████████████████████████████████▍                    | 41/52 [05:27<00:34,  3.18s/it]INFO:vector_store:Embedding progress: 78.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  81%|██████████████████████████████████████████████████████████████████████████████▎                  | 42/52 [05:28<00:23,  2.38s/it]INFO:vector_store:Embedding progress: 80.8%
Creating embeddings:  83%|████████████████████████████████████████████████████████████████████████████████▏                | 43/52 [05:30<00:21,  2.34s/it]INFO:vector_store:Embedding progress: 82.7%
Creating embeddings:  85%|██████████████████████████████████████████████████████████████████████████████████               | 44/52 [05:31<00:15,  1.88s/it]INFO:vector_store:Embedding progress: 84.6%
Creating embeddings:  87%|███████████████████████████████████████████████████████████████████████████████████▉             | 45/52 [05:52<00:52,  7.54s/it]INFO:vector_store:Embedding progress: 86.5%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▊           | 46/52 [05:55<00:38,  6.43s/it]INFO:vector_store:Embedding progress: 88.5%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▋         | 47/52 [06:00<00:29,  5.85s/it]INFO:vector_store:Embedding progress: 90.4%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▌       | 48/52 [06:00<00:16,  4.19s/it]INFO:vector_store:Embedding progress: 92.3%
Creating embeddings:  94%|███████████████████████████████████████████████████████████████████████████████████████████▍     | 49/52 [06:01<00:09,  3.16s/it]INFO:vector_store:Embedding progress: 94.2%
Creating embeddings:  96%|█████████████████████████████████████████████████████████████████████████████████████████████▎   | 50/52 [06:01<00:04,  2.28s/it]INFO:vector_store:Embedding progress: 96.2%
INFO:vector_store:Embedding progress: 98.1%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 52/52 [06:02<00:00,  1.33s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 52/52 [06:02<00:00,  6.96s/it]
INFO:vector_store:Processed 16525 chunks so far
INFO:vector_store:Processed 17525 chunks so far
INFO:vector_store:Processed 18525 chunks so far
INFO:vector_store:Processed 19525 chunks so far
INFO:vector_store:Processed 20525 chunks so far
INFO:vector_store:Processed 20714 chunks so far
INFO:vector_store:Processing document batch 5 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/50 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▉                                                                                             | 1/50 [01:51<1:31:06, 111.56s/it]INFO:vector_store:Embedding progress: 2.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                              | 2/50 [01:53<37:44, 47.19s/it]INFO:vector_store:Embedding progress: 4.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▉                                                                                            | 3/50 [01:54<20:12, 25.80s/it]INFO:vector_store:Embedding progress: 6.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▊                                                                                          | 4/50 [01:54<12:04, 15.76s/it]INFO:vector_store:Embedding progress: 8.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▊                                                                                        | 5/50 [01:54<07:41, 10.26s/it]INFO:vector_store:Embedding progress: 10.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▊                                                                                      | 6/50 [01:55<05:08,  7.02s/it]INFO:vector_store:Embedding progress: 12.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▋                                                                                    | 7/50 [01:56<03:30,  4.90s/it]INFO:vector_store:Embedding progress: 14.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▋                                                                                  | 8/50 [01:57<02:41,  3.85s/it]INFO:vector_store:Embedding progress: 16.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▋                                                                                | 9/50 [02:00<02:20,  3.42s/it]INFO:vector_store:Embedding progress: 18.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████▍                                                                             | 10/50 [02:01<01:51,  2.79s/it]INFO:vector_store:Embedding progress: 20.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████▎                                                                           | 11/50 [02:02<01:21,  2.09s/it]INFO:vector_store:Embedding progress: 22.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▎                                                                         | 12/50 [02:25<05:30,  8.70s/it]INFO:vector_store:Embedding progress: 24.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▏                                                                       | 13/50 [02:27<04:06,  6.65s/it]INFO:vector_store:Embedding progress: 26.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▏                                                                     | 14/50 [02:30<03:13,  5.37s/it]INFO:vector_store:Embedding progress: 28.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|█████████████████████████████                                                                    | 15/50 [02:31<02:20,  4.01s/it]INFO:vector_store:Embedding progress: 30.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|███████████████████████████████                                                                  | 16/50 [02:31<01:36,  2.84s/it]INFO:vector_store:Embedding progress: 32.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|████████████████████████████████▉                                                                | 17/50 [02:33<01:31,  2.78s/it]INFO:vector_store:Embedding progress: 34.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|██████████████████████████████████▉                                                              | 18/50 [02:34<01:09,  2.16s/it]INFO:vector_store:Embedding progress: 36.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▊                                                            | 19/50 [02:36<01:03,  2.06s/it]INFO:vector_store:Embedding progress: 38.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▊                                                          | 20/50 [02:36<00:45,  1.51s/it]INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▋                                                        | 21/50 [02:40<01:01,  2.11s/it]INFO:vector_store:Embedding progress: 42.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|██████████████████████████████████████████▋                                                      | 22/50 [02:40<00:44,  1.59s/it]INFO:vector_store:Embedding progress: 44.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████▌                                                    | 23/50 [03:00<03:14,  7.19s/it]INFO:vector_store:Embedding progress: 46.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▌                                                  | 24/50 [03:01<02:14,  5.17s/it]INFO:vector_store:Embedding progress: 48.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 25/50 [03:04<01:52,  4.49s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▍                                              | 26/50 [03:04<01:17,  3.22s/it]INFO:vector_store:Embedding progress: 52.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|████████████████████████████████████████████████████▍                                            | 27/50 [03:05<01:02,  2.72s/it]INFO:vector_store:Embedding progress: 54.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|██████████████████████████████████████████████████████▎                                          | 28/50 [03:08<00:59,  2.70s/it]INFO:vector_store:Embedding progress: 56.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|████████████████████████████████████████████████████████▎                                        | 29/50 [03:09<00:44,  2.10s/it]INFO:vector_store:Embedding progress: 58.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 30/50 [03:10<00:37,  1.87s/it]INFO:vector_store:Embedding progress: 60.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|████████████████████████████████████████████████████████████▏                                    | 31/50 [03:11<00:29,  1.55s/it]INFO:vector_store:Embedding progress: 62.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|██████████████████████████████████████████████████████████████                                   | 32/50 [03:13<00:32,  1.79s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:  66%|████████████████████████████████████████████████████████████████                                 | 33/50 [03:13<00:21,  1.28s/it]INFO:vector_store:Embedding progress: 66.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▉                               | 34/50 [03:32<01:41,  6.36s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|███████████████████████████████████████████████████████████████████▉                             | 35/50 [03:34<01:19,  5.31s/it]INFO:vector_store:Embedding progress: 70.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▊                           | 36/50 [03:35<00:54,  3.92s/it]INFO:vector_store:Embedding progress: 72.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|███████████████████████████████████████████████████████████████████████▊                         | 37/50 [03:36<00:39,  3.07s/it]INFO:vector_store:Embedding progress: 74.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|█████████████████████████████████████████████████████████████████████████▋                       | 38/50 [03:39<00:35,  2.97s/it]INFO:vector_store:Embedding progress: 76.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|███████████████████████████████████████████████████████████████████████████▋                     | 39/50 [03:40<00:24,  2.24s/it]INFO:vector_store:Embedding progress: 78.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|█████████████████████████████████████████████████████████████████████████████▌                   | 40/50 [03:42<00:24,  2.40s/it]INFO:vector_store:Embedding progress: 80.0%
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▌                 | 41/50 [03:43<00:16,  1.83s/it]INFO:vector_store:Embedding progress: 82.0%
INFO:vector_store:Embedding progress: 84.0%
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▍             | 43/50 [03:45<00:10,  1.54s/it]INFO:vector_store:Embedding progress: 86.0%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▎           | 44/50 [03:46<00:07,  1.26s/it]INFO:vector_store:Embedding progress: 88.0%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▎         | 45/50 [04:06<00:31,  6.24s/it]INFO:vector_store:Embedding progress: 90.0%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▏       | 46/50 [04:13<00:25,  6.35s/it]INFO:vector_store:Embedding progress: 92.0%
Creating embeddings:  94%|███████████████████████████████████████████████████████████████████████████████████████████▏     | 47/50 [04:13<00:14,  4.71s/it]INFO:vector_store:Embedding progress: 94.0%
Creating embeddings:  96%|█████████████████████████████████████████████████████████████████████████████████████████████    | 48/50 [04:14<00:07,  3.52s/it]INFO:vector_store:Embedding progress: 96.0%
Creating embeddings:  98%|███████████████████████████████████████████████████████████████████████████████████████████████  | 49/50 [04:14<00:02,  2.58s/it]INFO:vector_store:Embedding progress: 98.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [04:14<00:00,  1.86s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [04:14<00:00,  5.09s/it]
INFO:vector_store:Processed 21714 chunks so far
INFO:vector_store:Processed 22714 chunks so far
INFO:vector_store:Processed 23714 chunks so far
INFO:vector_store:Processed 24714 chunks so far
INFO:vector_store:Processed 25714 chunks so far
INFO:vector_store:Processing document batch 6 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/50 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▉                                                                                             | 1/50 [02:16<1:51:12, 136.18s/it]INFO:vector_store:Embedding progress: 2.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                              | 2/50 [02:16<45:00, 56.25s/it]INFO:vector_store:Embedding progress: 4.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▉                                                                                            | 3/50 [02:18<24:35, 31.38s/it]INFO:vector_store:Embedding progress: 6.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▊                                                                                          | 4/50 [02:18<14:38, 19.09s/it]INFO:vector_store:Embedding progress: 8.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▊                                                                                        | 5/50 [02:18<09:13, 12.30s/it]INFO:vector_store:Embedding progress: 10.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▊                                                                                      | 6/50 [02:19<06:00,  8.20s/it]INFO:vector_store:Embedding progress: 12.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▋                                                                                    | 7/50 [02:19<04:00,  5.59s/it]INFO:vector_store:Embedding progress: 14.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▋                                                                                  | 8/50 [02:19<02:43,  3.90s/it]INFO:vector_store:Embedding progress: 16.0%
INFO:vector_store:Embedding progress: 18.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████▍                                                                             | 10/50 [02:19<01:23,  2.08s/it]INFO:vector_store:Embedding progress: 20.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 22.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▎                                                                         | 12/50 [03:10<07:19, 11.56s/it]INFO:vector_store:Embedding progress: 24.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▏                                                                       | 13/50 [03:10<05:33,  9.00s/it]INFO:vector_store:Embedding progress: 26.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▏                                                                     | 14/50 [03:15<04:43,  7.87s/it]INFO:vector_store:Embedding progress: 28.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|█████████████████████████████                                                                    | 15/50 [03:16<03:33,  6.10s/it]INFO:vector_store:Embedding progress: 30.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|███████████████████████████████                                                                  | 16/50 [03:17<02:42,  4.78s/it]INFO:vector_store:Embedding progress: 32.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|████████████████████████████████▉                                                                | 17/50 [03:17<01:55,  3.50s/it]INFO:vector_store:Embedding progress: 34.0%
Creating embeddings:  36%|██████████████████████████████████▉                                                              | 18/50 [03:17<01:21,  2.54s/it]INFO:vector_store:Embedding progress: 36.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▊                                                            | 19/50 [03:17<00:57,  1.85s/it]INFO:vector_store:Embedding progress: 38.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▊                                                          | 20/50 [03:17<00:41,  1.37s/it]INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 42.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|██████████████████████████████████████████▋                                                      | 22/50 [03:18<00:21,  1.30it/s]INFO:vector_store:Embedding progress: 44.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████▌                                                    | 23/50 [04:01<05:05, 11.31s/it]INFO:vector_store:Embedding progress: 46.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▌                                                  | 24/50 [04:03<03:52,  8.93s/it]INFO:vector_store:Embedding progress: 48.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 25/50 [04:09<03:17,  7.91s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▍                                              | 26/50 [04:13<02:44,  6.87s/it]INFO:vector_store:Embedding progress: 52.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|████████████████████████████████████████████████████▍                                            | 27/50 [04:15<02:07,  5.54s/it]INFO:vector_store:Embedding progress: 54.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|██████████████████████████████████████████████████████▎                                          | 28/50 [04:16<01:30,  4.11s/it]INFO:vector_store:Embedding progress: 56.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 58.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 30/50 [04:16<00:45,  2.30s/it]INFO:vector_store:Embedding progress: 60.0%
INFO:vector_store:Embedding progress: 62.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|██████████████████████████████████████████████████████████████                                   | 32/50 [04:16<00:25,  1.44s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:vector_store:Embedding progress: 66.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▉                               | 34/50 [04:52<01:56,  7.30s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|███████████████████████████████████████████████████████████████████▉                             | 35/50 [04:57<01:44,  6.98s/it]INFO:vector_store:Embedding progress: 70.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▊                           | 36/50 [05:01<01:26,  6.18s/it]INFO:vector_store:Embedding progress: 72.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|███████████████████████████████████████████████████████████████████████▊                         | 37/50 [05:10<01:30,  6.99s/it]INFO:vector_store:Embedding progress: 74.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|█████████████████████████████████████████████████████████████████████████▋                       | 38/50 [05:13<01:12,  6.01s/it]INFO:vector_store:Embedding progress: 76.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|███████████████████████████████████████████████████████████████████████████▋                     | 39/50 [05:14<00:50,  4.58s/it]INFO:vector_store:Embedding progress: 78.0%
INFO:vector_store:Embedding progress: 80.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▌                 | 41/50 [05:14<00:23,  2.63s/it]INFO:vector_store:Embedding progress: 82.0%
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▍               | 42/50 [05:15<00:16,  2.10s/it]INFO:vector_store:Embedding progress: 84.0%
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▍             | 43/50 [05:15<00:11,  1.64s/it]INFO:vector_store:Embedding progress: 86.0%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▎           | 44/50 [05:16<00:08,  1.47s/it]INFO:vector_store:Embedding progress: 88.0%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▎         | 45/50 [05:31<00:26,  5.29s/it]INFO:vector_store:Embedding progress: 90.0%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▏       | 46/50 [05:34<00:17,  4.43s/it]INFO:vector_store:Embedding progress: 92.0%
Creating embeddings:  94%|███████████████████████████████████████████████████████████████████████████████████████████▏     | 47/50 [05:34<00:10,  3.37s/it]INFO:vector_store:Embedding progress: 94.0%
Creating embeddings:  96%|█████████████████████████████████████████████████████████████████████████████████████████████    | 48/50 [05:37<00:06,  3.14s/it]INFO:vector_store:Embedding progress: 96.0%
Creating embeddings:  98%|███████████████████████████████████████████████████████████████████████████████████████████████  | 49/50 [05:37<00:02,  2.40s/it]INFO:vector_store:Embedding progress: 98.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [05:43<00:00,  3.43s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [05:43<00:00,  6.88s/it]
INFO:vector_store:Processed 26714 chunks so far
INFO:vector_store:Processed 27714 chunks so far
INFO:vector_store:Processed 28714 chunks so far
INFO:vector_store:Processed 29714 chunks so far
INFO:vector_store:Processed 30714 chunks so far
INFO:vector_store:Processing document batch 7 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/50 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▉                                                                                             | 1/50 [02:12<1:48:36, 132.99s/it]INFO:vector_store:Embedding progress: 2.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                              | 2/50 [02:13<43:56, 54.92s/it]INFO:vector_store:Embedding progress: 4.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▉                                                                                            | 3/50 [02:14<23:59, 30.62s/it]INFO:vector_store:Embedding progress: 6.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▊                                                                                          | 4/50 [02:15<14:21, 18.73s/it]INFO:vector_store:Embedding progress: 8.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▊                                                                                        | 5/50 [02:15<09:03, 12.07s/it]INFO:vector_store:Embedding progress: 10.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▊                                                                                      | 6/50 [02:15<05:52,  8.01s/it]INFO:vector_store:Embedding progress: 12.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 14.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 16.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 18.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████▍                                                                             | 10/50 [02:16<01:50,  2.76s/it]INFO:vector_store:Embedding progress: 20.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████▎                                                                           | 11/50 [02:16<01:28,  2.28s/it]INFO:vector_store:Embedding progress: 22.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▎                                                                         | 12/50 [03:07<08:00, 12.65s/it]INFO:vector_store:Embedding progress: 24.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▏                                                                       | 13/50 [03:07<06:03,  9.84s/it]INFO:vector_store:Embedding progress: 26.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▏                                                                     | 14/50 [03:14<05:25,  9.06s/it]INFO:vector_store:Embedding progress: 28.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|█████████████████████████████                                                                    | 15/50 [03:14<03:57,  6.80s/it]INFO:vector_store:Embedding progress: 30.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|███████████████████████████████                                                                  | 16/50 [03:15<02:54,  5.12s/it]INFO:vector_store:Embedding progress: 32.0%
INFO:vector_store:Embedding progress: 34.0%
INFO:vector_store:Embedding progress: 36.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▊                                                            | 19/50 [03:16<01:16,  2.47s/it]INFO:vector_store:Embedding progress: 38.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▊                                                          | 20/50 [03:16<01:00,  2.01s/it]INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 42.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|██████████████████████████████████████████▋                                                      | 22/50 [03:16<00:37,  1.35s/it]INFO:vector_store:Embedding progress: 44.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████▌                                                    | 23/50 [03:58<04:23,  9.75s/it]INFO:vector_store:Embedding progress: 46.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▌                                                  | 24/50 [04:00<03:28,  8.01s/it]INFO:vector_store:Embedding progress: 48.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 25/50 [04:12<03:45,  9.02s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▍                                              | 26/50 [04:14<02:52,  7.17s/it]INFO:vector_store:Embedding progress: 52.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|████████████████████████████████████████████████████▍                                            | 27/50 [04:15<02:02,  5.33s/it]INFO:vector_store:Embedding progress: 54.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|██████████████████████████████████████████████████████▎                                          | 28/50 [04:15<01:28,  4.04s/it]INFO:vector_store:Embedding progress: 56.0%
INFO:vector_store:Embedding progress: 58.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 30/50 [04:16<00:47,  2.36s/it]INFO:vector_store:Embedding progress: 60.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|████████████████████████████████████████████████████████████▏                                    | 31/50 [04:16<00:35,  1.85s/it]INFO:vector_store:Embedding progress: 62.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|██████████████████████████████████████████████████████████████                                   | 32/50 [04:16<00:25,  1.43s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|████████████████████████████████████████████████████████████████                                 | 33/50 [04:16<00:18,  1.11s/it]INFO:vector_store:Embedding progress: 66.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▉                               | 34/50 [04:58<03:16, 12.29s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|███████████████████████████████████████████████████████████████████▉                             | 35/50 [04:58<02:13,  8.89s/it]INFO:vector_store:Embedding progress: 70.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▊                           | 36/50 [05:10<02:16,  9.75s/it]INFO:vector_store:Embedding progress: 72.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|███████████████████████████████████████████████████████████████████████▊                         | 37/50 [05:13<01:42,  7.85s/it]INFO:vector_store:Embedding progress: 74.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|█████████████████████████████████████████████████████████████████████████▋                       | 38/50 [05:14<01:09,  5.79s/it]INFO:vector_store:Embedding progress: 76.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|███████████████████████████████████████████████████████████████████████████▋                     | 39/50 [05:16<00:49,  4.46s/it]INFO:vector_store:Embedding progress: 78.0%
INFO:vector_store:Embedding progress: 80.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▌                 | 41/50 [05:16<00:23,  2.61s/it]INFO:vector_store:Embedding progress: 82.0%
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▍               | 42/50 [05:17<00:16,  2.00s/it]INFO:vector_store:Embedding progress: 84.0%
INFO:vector_store:Embedding progress: 86.0%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▎           | 44/50 [05:17<00:07,  1.23s/it]INFO:vector_store:Embedding progress: 88.0%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▎         | 45/50 [05:39<00:29,  5.92s/it]INFO:vector_store:Embedding progress: 90.0%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▏       | 46/50 [05:39<00:18,  4.62s/it]INFO:vector_store:Embedding progress: 92.0%
Creating embeddings:  94%|███████████████████████████████████████████████████████████████████████████████████████████▏     | 47/50 [05:44<00:14,  4.77s/it]INFO:vector_store:Embedding progress: 94.0%
Creating embeddings:  96%|█████████████████████████████████████████████████████████████████████████████████████████████    | 48/50 [05:46<00:07,  3.85s/it]INFO:vector_store:Embedding progress: 96.0%
INFO:vector_store:Embedding progress: 98.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [05:46<00:00,  2.22s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [05:46<00:00,  6.93s/it]
INFO:vector_store:Processed 31714 chunks so far
INFO:vector_store:Processed 32714 chunks so far
INFO:vector_store:Processed 33714 chunks so far
INFO:vector_store:Processed 34714 chunks so far
INFO:vector_store:Processed 35714 chunks so far
INFO:vector_store:Processing document batch 8 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/50 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▉                                                                                             | 1/50 [01:51<1:30:42, 111.06s/it]INFO:vector_store:Embedding progress: 2.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                              | 2/50 [01:52<37:06, 46.38s/it]INFO:vector_store:Embedding progress: 4.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▉                                                                                            | 3/50 [01:52<19:53, 25.40s/it]INFO:vector_store:Embedding progress: 6.0%
INFO:vector_store:Embedding progress: 8.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▊                                                                                        | 5/50 [01:53<08:21, 11.15s/it]INFO:vector_store:Embedding progress: 10.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▊                                                                                      | 6/50 [01:53<05:54,  8.06s/it]INFO:vector_store:Embedding progress: 12.0%
INFO:vector_store:Embedding progress: 14.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▋                                                                                  | 8/50 [01:53<03:07,  4.45s/it]INFO:vector_store:Embedding progress: 16.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▋                                                                                | 9/50 [01:53<02:19,  3.40s/it]INFO:vector_store:Embedding progress: 18.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████▍                                                                             | 10/50 [01:54<01:45,  2.63s/it]INFO:vector_store:Embedding progress: 20.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████▎                                                                           | 11/50 [01:54<01:21,  2.08s/it]INFO:vector_store:Embedding progress: 22.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▎                                                                         | 12/50 [02:30<07:10, 11.33s/it]INFO:vector_store:Embedding progress: 24.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▏                                                                       | 13/50 [02:41<06:58, 11.32s/it]INFO:vector_store:Embedding progress: 26.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▏                                                                     | 14/50 [02:42<05:03,  8.44s/it]INFO:vector_store:Embedding progress: 28.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|█████████████████████████████                                                                    | 15/50 [02:43<03:35,  6.15s/it]INFO:vector_store:Embedding progress: 30.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|███████████████████████████████                                                                  | 16/50 [02:43<02:31,  4.45s/it]INFO:vector_store:Embedding progress: 32.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|████████████████████████████████▉                                                                | 17/50 [02:45<01:59,  3.62s/it]INFO:vector_store:Embedding progress: 34.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|██████████████████████████████████▉                                                              | 18/50 [02:46<01:28,  2.76s/it]INFO:vector_store:Embedding progress: 36.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▊                                                            | 19/50 [02:46<01:04,  2.09s/it]INFO:vector_store:Embedding progress: 38.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▊                                                          | 20/50 [02:47<00:52,  1.74s/it]INFO:vector_store:Embedding progress: 40.0%
INFO:vector_store:Embedding progress: 42.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|██████████████████████████████████████████▋                                                      | 22/50 [02:47<00:27,  1.02it/s]INFO:vector_store:Embedding progress: 44.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████▌                                                    | 23/50 [03:10<02:55,  6.49s/it]INFO:vector_store:Embedding progress: 46.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▌                                                  | 24/50 [03:18<02:59,  6.89s/it]INFO:vector_store:Embedding progress: 48.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 25/50 [03:21<02:23,  5.73s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▍                                              | 26/50 [03:23<01:50,  4.60s/it]INFO:vector_store:Embedding progress: 52.0%
INFO:vector_store:Embedding progress: 54.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|██████████████████████████████████████████████████████▎                                          | 28/50 [03:25<01:05,  2.98s/it]INFO:vector_store:Embedding progress: 56.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|████████████████████████████████████████████████████████▎                                        | 29/50 [03:26<00:51,  2.47s/it]INFO:vector_store:Embedding progress: 58.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 30/50 [03:26<00:38,  1.91s/it]INFO:vector_store:Embedding progress: 60.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|████████████████████████████████████████████████████████████▏                                    | 31/50 [03:27<00:30,  1.59s/it]INFO:vector_store:Embedding progress: 62.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|██████████████████████████████████████████████████████████████                                   | 32/50 [03:27<00:21,  1.18s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|████████████████████████████████████████████████████████████████                                 | 33/50 [03:27<00:15,  1.13it/s]INFO:vector_store:Embedding progress: 66.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▉                               | 34/50 [03:48<01:46,  6.64s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|███████████████████████████████████████████████████████████████████▉                             | 35/50 [03:56<01:47,  7.19s/it]INFO:vector_store:Embedding progress: 70.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▊                           | 36/50 [04:01<01:28,  6.35s/it]INFO:vector_store:Embedding progress: 72.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|███████████████████████████████████████████████████████████████████████▊                         | 37/50 [04:03<01:07,  5.19s/it]INFO:vector_store:Embedding progress: 74.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|█████████████████████████████████████████████████████████████████████████▋                       | 38/50 [04:04<00:46,  3.83s/it]INFO:vector_store:Embedding progress: 76.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|███████████████████████████████████████████████████████████████████████████▋                     | 39/50 [04:06<00:36,  3.35s/it]INFO:vector_store:Embedding progress: 78.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|█████████████████████████████████████████████████████████████████████████████▌                   | 40/50 [04:07<00:26,  2.61s/it]INFO:vector_store:Embedding progress: 80.0%
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▌                 | 41/50 [04:07<00:17,  1.95s/it]INFO:vector_store:Embedding progress: 82.0%
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▍               | 42/50 [04:07<00:11,  1.45s/it]INFO:vector_store:Embedding progress: 84.0%
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▍             | 43/50 [04:07<00:07,  1.06s/it]INFO:vector_store:Embedding progress: 86.0%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▎           | 44/50 [04:08<00:04,  1.29it/s]INFO:vector_store:Embedding progress: 88.0%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▎         | 45/50 [04:25<00:28,  5.65s/it]INFO:vector_store:Embedding progress: 90.0%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▏       | 46/50 [04:27<00:18,  4.75s/it]INFO:vector_store:Embedding progress: 92.0%
Creating embeddings:  94%|███████████████████████████████████████████████████████████████████████████████████████████▏     | 47/50 [04:28<00:10,  3.51s/it]INFO:vector_store:Embedding progress: 94.0%
INFO:vector_store:Embedding progress: 96.0%
INFO:vector_store:Embedding progress: 98.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [04:28<00:00,  1.57s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [04:28<00:00,  5.37s/it]
INFO:vector_store:Processed 36714 chunks so far
INFO:vector_store:Processed 37714 chunks so far
INFO:vector_store:Processed 38714 chunks so far
INFO:vector_store:Processed 39714 chunks so far
INFO:vector_store:Processed 40714 chunks so far
INFO:vector_store:Processing document batch 9 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/50 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▉                                                                                              | 1/50 [01:27<1:11:46, 87.89s/it]INFO:vector_store:Embedding progress: 2.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                              | 2/50 [01:28<29:06, 36.39s/it]INFO:vector_store:Embedding progress: 4.0%
INFO:vector_store:Embedding progress: 6.0%
INFO:vector_store:Embedding progress: 8.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▊                                                                                        | 5/50 [01:28<07:46, 10.38s/it]INFO:vector_store:Embedding progress: 10.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 12.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▋                                                                                    | 7/50 [01:28<04:26,  6.21s/it]INFO:vector_store:Embedding progress: 14.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 16.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▋                                                                                | 9/50 [01:29<02:47,  4.08s/it]INFO:vector_store:Embedding progress: 18.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████▍                                                                             | 10/50 [01:30<02:14,  3.37s/it]INFO:vector_store:Embedding progress: 20.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 22.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▎                                                                         | 12/50 [01:44<03:01,  4.77s/it]INFO:vector_store:Embedding progress: 24.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▏                                                                       | 13/50 [01:44<02:21,  3.81s/it]INFO:vector_store:Embedding progress: 26.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▏                                                                     | 14/50 [02:21<06:53, 11.48s/it]INFO:vector_store:Embedding progress: 28.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|█████████████████████████████                                                                    | 15/50 [02:23<05:16,  9.05s/it]INFO:vector_store:Embedding progress: 30.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|███████████████████████████████                                                                  | 16/50 [02:23<03:49,  6.76s/it]INFO:vector_store:Embedding progress: 32.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|████████████████████████████████▉                                                                | 17/50 [02:23<02:43,  4.95s/it]INFO:vector_store:Embedding progress: 34.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|██████████████████████████████████▉                                                              | 18/50 [02:24<01:58,  3.69s/it]INFO:vector_store:Embedding progress: 36.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▊                                                            | 19/50 [02:24<01:26,  2.80s/it]INFO:vector_store:Embedding progress: 38.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▋                                                        | 21/50 [02:24<00:45,  1.57s/it]INFO:vector_store:Embedding progress: 42.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 44.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████▌                                                    | 23/50 [02:25<00:28,  1.06s/it]INFO:vector_store:Embedding progress: 46.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 48.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 25/50 [02:32<00:49,  1.99s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▍                                              | 26/50 [02:47<01:51,  4.63s/it]INFO:vector_store:Embedding progress: 52.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
ERROR:vector_store:Error in parallel processing: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=False&expand=False (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x000001A9F27A7010>: Failed to resolve \'huggingface.co\' ([Errno 11001] getaddrinfo failed)"))'), '(Request ID: 529aa171-2225-4735-87bc-f1135efb2457)')
Creating embeddings:  54%|████████████████████████████████████████████████████▍                                            | 27/50 [03:19<04:09, 10.86s/it]INFO:vector_store:Embedding progress: 54.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|██████████████████████████████████████████████████████▎                                          | 28/50 [03:52<05:54, 16.11s/it]INFO:vector_store:Embedding progress: 56.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|████████████████████████████████████████████████████████▎                                        | 29/50 [03:57<04:36, 13.18s/it]INFO:vector_store:Embedding progress: 58.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 30/50 [03:58<03:18,  9.92s/it]INFO:vector_store:Embedding progress: 60.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|████████████████████████████████████████████████████████████▏                                    | 31/50 [03:59<02:22,  7.48s/it]INFO:vector_store:Embedding progress: 62.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|██████████████████████████████████████████████████████████████                                   | 32/50 [04:02<01:52,  6.25s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 66.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▉                               | 34/50 [04:02<00:56,  3.51s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 70.0%
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▊                           | 36/50 [04:02<00:30,  2.16s/it]INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 72.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|███████████████████████████████████████████████████████████████████████▊                         | 37/50 [04:02<00:22,  1.72s/it]INFO:vector_store:Embedding progress: 74.0%
INFO:vector_store:Embedding progress: 76.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|███████████████████████████████████████████████████████████████████████████▋                     | 39/50 [04:22<00:52,  4.77s/it]INFO:vector_store:Embedding progress: 78.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|█████████████████████████████████████████████████████████████████████████████▌                   | 40/50 [04:28<00:50,  5.06s/it]INFO:vector_store:Embedding progress: 80.0%
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▌                 | 41/50 [04:29<00:37,  4.20s/it]INFO:vector_store:Embedding progress: 82.0%
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▍               | 42/50 [04:31<00:27,  3.49s/it]INFO:vector_store:Embedding progress: 84.0%
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▍             | 43/50 [04:35<00:26,  3.75s/it]INFO:vector_store:Embedding progress: 86.0%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▎           | 44/50 [04:35<00:16,  2.75s/it]INFO:vector_store:Embedding progress: 88.0%
INFO:vector_store:Embedding progress: 90.0%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▏       | 46/50 [04:37<00:07,  1.92s/it]INFO:vector_store:Embedding progress: 92.0%
INFO:vector_store:Embedding progress: 94.0%
INFO:vector_store:Embedding progress: 96.0%
INFO:vector_store:Embedding progress: 98.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [04:46<00:00,  2.11s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [04:46<00:00,  5.73s/it]
INFO:vector_store:Processed 41714 chunks so far
INFO:vector_store:Processed 42714 chunks so far
INFO:vector_store:Processed 43714 chunks so far
INFO:vector_store:Processed 44714 chunks so far
ERROR:vector_store:Error adding chunk batch to vector store: Number of embeddings 900 must match number of ids 1000
INFO:vector_store:Processing document batch 10 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/50 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▉                                                                                              | 1/50 [01:17<1:03:09, 77.34s/it]INFO:vector_store:Embedding progress: 2.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                              | 2/50 [01:43<37:53, 47.37s/it]INFO:vector_store:Embedding progress: 4.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▉                                                                                            | 3/50 [01:50<22:29, 28.72s/it]INFO:vector_store:Embedding progress: 6.0%
Creating embeddings:   8%|███████▊                                                                                          | 4/50 [01:50<13:21, 17.42s/it]INFO:vector_store:Embedding progress: 8.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▊                                                                                        | 5/50 [01:50<08:28, 11.31s/it]INFO:vector_store:Embedding progress: 10.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▊                                                                                      | 6/50 [01:51<05:32,  7.55s/it]INFO:vector_store:Embedding progress: 12.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▋                                                                                    | 7/50 [01:51<03:47,  5.28s/it]INFO:vector_store:Embedding progress: 14.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▋                                                                                  | 8/50 [01:52<02:43,  3.89s/it]INFO:vector_store:Embedding progress: 16.0%
INFO:vector_store:Embedding progress: 18.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████▍                                                                             | 10/50 [01:52<01:23,  2.10s/it]INFO:vector_store:Embedding progress: 20.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████▎                                                                           | 11/50 [01:53<01:05,  1.68s/it]INFO:vector_store:Embedding progress: 22.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 24.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▏                                                                       | 13/50 [01:56<01:03,  1.72s/it]INFO:vector_store:Embedding progress: 26.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▏                                                                     | 14/50 [02:35<06:06, 10.19s/it]INFO:vector_store:Embedding progress: 28.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|█████████████████████████████                                                                    | 15/50 [02:35<04:32,  7.78s/it]INFO:vector_store:Embedding progress: 30.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|███████████████████████████████                                                                  | 16/50 [02:35<03:16,  5.78s/it]INFO:vector_store:Embedding progress: 32.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|████████████████████████████████▉                                                                | 17/50 [02:35<02:19,  4.24s/it]INFO:vector_store:Embedding progress: 34.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 36.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▊                                                            | 19/50 [02:36<01:15,  2.44s/it]INFO:vector_store:Embedding progress: 38.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▊                                                          | 20/50 [02:36<00:57,  1.93s/it]INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▋                                                        | 21/50 [02:45<01:49,  3.79s/it]INFO:vector_store:Embedding progress: 42.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|██████████████████████████████████████████▋                                                      | 22/50 [02:46<01:26,  3.09s/it]INFO:vector_store:Embedding progress: 44.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████▌                                                    | 23/50 [02:47<01:03,  2.37s/it]INFO:vector_store:Embedding progress: 46.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▌                                                  | 24/50 [03:11<03:37,  8.37s/it]INFO:vector_store:Embedding progress: 48.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 25/50 [03:11<02:30,  6.01s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▍                                              | 26/50 [03:12<01:53,  4.72s/it]INFO:vector_store:Embedding progress: 52.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|████████████████████████████████████████████████████▍                                            | 27/50 [03:13<01:24,  3.65s/it]INFO:vector_store:Embedding progress: 54.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|██████████████████████████████████████████████████████▎                                          | 28/50 [03:14<00:57,  2.62s/it]INFO:vector_store:Embedding progress: 56.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|████████████████████████████████████████████████████████▎                                        | 29/50 [03:14<00:39,  1.90s/it]INFO:vector_store:Embedding progress: 58.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 30/50 [03:14<00:27,  1.38s/it]INFO:vector_store:Embedding progress: 60.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|████████████████████████████████████████████████████████████▏                                    | 31/50 [03:17<00:35,  1.85s/it]INFO:vector_store:Embedding progress: 62.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|██████████████████████████████████████████████████████████████                                   | 32/50 [03:17<00:24,  1.37s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|████████████████████████████████████████████████████████████████                                 | 33/50 [03:17<00:17,  1.00s/it]INFO:vector_store:Embedding progress: 66.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▉                               | 34/50 [03:19<00:20,  1.26s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
ERROR:vector_store:Error in parallel processing: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=False&expand=False (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x000002BF5C3FF710>: Failed to resolve \'huggingface.co\' ([Errno 11001] getaddrinfo failed)"))'), '(Request ID: 77481cb7-faa4-4417-873e-f40b44d35a08)')
ERROR:vector_store:Error in parallel processing: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=False&expand=False (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x000001FDECC5A9D0>: Failed to resolve \'huggingface.co\' ([Errno 11001] getaddrinfo failed)"))'), '(Request ID: e231e8a3-2a5b-4f49-9c7f-f12aea0f05b2)')
ERROR:vector_store:Error in parallel processing: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=False&expand=False (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x00000236A93AF1D0>: Failed to resolve \'huggingface.co\' ([Errno 11001] getaddrinfo failed)"))'), '(Request ID: 4f4bc2f7-d293-4a7f-8101-2b50e5d71996)')
ERROR:vector_store:Error in parallel processing: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=False&expand=False (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x0000020140B25050>: Failed to resolve \'huggingface.co\' ([Errno 11001] getaddrinfo failed)"))'), '(Request ID: 58213a7c-9b88-46a8-be79-26fa09f745b9)')
Creating embeddings:  70%|███████████████████████████████████████████████████████████████████▉                             | 35/50 [03:33<01:17,  5.14s/it]INFO:vector_store:Embedding progress: 70.0%
INFO:vector_store:Embedding progress: 72.0%
INFO:vector_store:Embedding progress: 74.0%
INFO:vector_store:Embedding progress: 76.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|███████████████████████████████████████████████████████████████████████████▋                     | 39/50 [04:05<01:15,  6.83s/it]INFO:vector_store:Embedding progress: 78.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|█████████████████████████████████████████████████████████████████████████████▌                   | 40/50 [04:10<01:04,  6.50s/it]INFO:vector_store:Embedding progress: 80.0%
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▌                 | 41/50 [04:10<00:47,  5.29s/it]INFO:vector_store:Embedding progress: 82.0%
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▍               | 42/50 [04:10<00:33,  4.13s/it]INFO:vector_store:Embedding progress: 84.0%
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▍             | 43/50 [04:11<00:22,  3.27s/it]INFO:vector_store:Embedding progress: 86.0%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▎           | 44/50 [04:11<00:14,  2.46s/it]INFO:vector_store:Embedding progress: 88.0%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▎         | 45/50 [04:11<00:09,  1.85s/it]INFO:vector_store:Embedding progress: 90.0%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▏       | 46/50 [04:12<00:05,  1.37s/it]INFO:vector_store:Embedding progress: 92.0%
Creating embeddings:  94%|███████████████████████████████████████████████████████████████████████████████████████████▏     | 47/50 [04:12<00:03,  1.05s/it]INFO:vector_store:Embedding progress: 94.0%
Creating embeddings:  96%|█████████████████████████████████████████████████████████████████████████████████████████████    | 48/50 [04:15<00:03,  1.79s/it]INFO:vector_store:Embedding progress: 96.0%
Creating embeddings:  98%|███████████████████████████████████████████████████████████████████████████████████████████████  | 49/50 [04:21<00:02,  2.93s/it]INFO:vector_store:Embedding progress: 98.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [04:24<00:00,  3.04s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [04:24<00:00,  5.30s/it]
INFO:vector_store:Processed 45714 chunks so far
INFO:vector_store:Processed 46714 chunks so far
INFO:vector_store:Processed 47714 chunks so far
INFO:vector_store:Processed 48714 chunks so far
ERROR:vector_store:Error adding chunk batch to vector store: Number of embeddings 600 must match number of ids 1000
INFO:vector_store:Processing document batch 11 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/50 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▉                                                                                              | 1/50 [01:23<1:07:55, 83.17s/it]INFO:vector_store:Embedding progress: 2.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                              | 2/50 [01:23<27:31, 34.41s/it]INFO:vector_store:Embedding progress: 4.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▉                                                                                            | 3/50 [01:23<14:41, 18.76s/it]INFO:vector_store:Embedding progress: 6.0%
INFO:vector_store:Embedding progress: 8.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▊                                                                                        | 5/50 [01:23<06:08,  8.19s/it]INFO:vector_store:Embedding progress: 10.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▊                                                                                      | 6/50 [01:23<04:19,  5.90s/it]INFO:vector_store:Embedding progress: 12.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 14.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▋                                                                                  | 8/50 [01:24<02:17,  3.27s/it]INFO:vector_store:Embedding progress: 16.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▋                                                                                | 9/50 [01:59<07:34, 11.09s/it]INFO:vector_store:Embedding progress: 18.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████▍                                                                             | 10/50 [02:00<05:36,  8.41s/it]INFO:vector_store:Embedding progress: 20.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████▎                                                                           | 11/50 [02:00<04:03,  6.25s/it]INFO:vector_store:Embedding progress: 22.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▎                                                                         | 12/50 [02:03<03:21,  5.31s/it]INFO:vector_store:Embedding progress: 24.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▏                                                                       | 13/50 [02:03<02:25,  3.93s/it]INFO:vector_store:Embedding progress: 26.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▏                                                                     | 14/50 [02:04<01:41,  2.82s/it]INFO:vector_store:Embedding progress: 28.0%
INFO:vector_store:Embedding progress: 30.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|███████████████████████████████                                                                  | 16/50 [02:04<00:53,  1.57s/it]INFO:vector_store:Embedding progress: 32.0%
INFO:vector_store:Embedding progress: 34.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 36.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 38.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▊                                                          | 20/50 [02:35<02:32,  5.10s/it]INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▋                                                        | 21/50 [02:39<02:23,  4.96s/it]INFO:vector_store:Embedding progress: 42.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|██████████████████████████████████████████▋                                                      | 22/50 [02:42<02:04,  4.46s/it]INFO:vector_store:Embedding progress: 44.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████▌                                                    | 23/50 [02:45<01:53,  4.19s/it]INFO:vector_store:Embedding progress: 46.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▌                                                  | 24/50 [02:45<01:24,  3.24s/it]INFO:vector_store:Embedding progress: 48.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 25/50 [02:45<01:03,  2.55s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 52.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|████████████████████████████████████████████████████▍                                            | 27/50 [02:46<00:35,  1.53s/it]INFO:vector_store:Embedding progress: 54.0%
INFO:vector_store:Embedding progress: 56.0%
INFO:vector_store:Embedding progress: 58.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 30/50 [02:46<00:16,  1.21it/s]INFO:vector_store:Embedding progress: 60.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|████████████████████████████████████████████████████████████▏                                    | 31/50 [03:08<01:29,  4.71s/it]INFO:vector_store:Embedding progress: 62.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|██████████████████████████████████████████████████████████████                                   | 32/50 [03:13<01:26,  4.78s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|████████████████████████████████████████████████████████████████                                 | 33/50 [03:16<01:16,  4.51s/it]INFO:vector_store:Embedding progress: 66.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▉                               | 34/50 [03:21<01:13,  4.61s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|███████████████████████████████████████████████████████████████████▉                             | 35/50 [03:22<00:54,  3.64s/it]INFO:vector_store:Embedding progress: 70.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▊                           | 36/50 [03:22<00:37,  2.69s/it]INFO:vector_store:Embedding progress: 72.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 74.0%
Creating embeddings:  76%|█████████████████████████████████████████████████████████████████████████▋                       | 38/50 [03:23<00:18,  1.55s/it]INFO:vector_store:Embedding progress: 76.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 78.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|█████████████████████████████████████████████████████████████████████████████▌                   | 40/50 [03:23<00:09,  1.02it/s]INFO:vector_store:Embedding progress: 80.0%
INFO:vector_store:Embedding progress: 82.0%
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▍               | 42/50 [03:37<00:25,  3.20s/it]INFO:vector_store:Embedding progress: 84.0%
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▍             | 43/50 [03:41<00:23,  3.35s/it]INFO:vector_store:Embedding progress: 86.0%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▎           | 44/50 [03:44<00:19,  3.29s/it]INFO:vector_store:Embedding progress: 88.0%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▎         | 45/50 [03:49<00:18,  3.67s/it]INFO:vector_store:Embedding progress: 90.0%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▏       | 46/50 [03:49<00:11,  2.84s/it]INFO:vector_store:Embedding progress: 92.0%
INFO:vector_store:Embedding progress: 94.0%
INFO:vector_store:Embedding progress: 96.0%
INFO:vector_store:Embedding progress: 98.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [03:50<00:00,  1.17s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [03:50<00:00,  4.60s/it]
INFO:vector_store:Processed 49714 chunks so far
INFO:vector_store:Processed 50714 chunks so far
INFO:vector_store:Processed 51714 chunks so far
INFO:vector_store:Processed 52714 chunks so far
INFO:vector_store:Processed 53714 chunks so far
INFO:vector_store:Processing document batch 12 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/50 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▉                                                                                              | 1/50 [01:33<1:16:06, 93.19s/it]INFO:vector_store:Embedding progress: 2.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                              | 2/50 [01:34<31:22, 39.22s/it]INFO:vector_store:Embedding progress: 4.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▉                                                                                            | 3/50 [01:35<16:50, 21.50s/it]INFO:vector_store:Embedding progress: 6.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 8.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▊                                                                                        | 5/50 [01:35<07:03,  9.42s/it]INFO:vector_store:Embedding progress: 10.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 12.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 14.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 16.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▋                                                                                | 9/50 [01:35<02:29,  3.64s/it]INFO:vector_store:Embedding progress: 18.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 20.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████▎                                                                           | 11/50 [01:35<01:39,  2.54s/it]INFO:vector_store:Embedding progress: 22.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▎                                                                         | 12/50 [02:02<04:23,  6.94s/it]INFO:vector_store:Embedding progress: 24.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▏                                                                       | 13/50 [02:08<04:10,  6.77s/it]INFO:vector_store:Embedding progress: 26.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▏                                                                     | 14/50 [02:10<03:21,  5.59s/it]INFO:vector_store:Embedding progress: 28.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|█████████████████████████████                                                                    | 15/50 [02:10<02:29,  4.28s/it]INFO:vector_store:Embedding progress: 30.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 32.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:  34%|████████████████████████████████▉                                                                | 17/50 [02:10<01:24,  2.56s/it]INFO:vector_store:Embedding progress: 34.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 36.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▊                                                            | 19/50 [02:11<00:51,  1.66s/it]INFO:vector_store:Embedding progress: 38.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▊                                                          | 20/50 [02:12<00:48,  1.63s/it]INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▋                                                        | 21/50 [02:12<00:37,  1.29s/it]INFO:vector_store:Embedding progress: 42.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|██████████████████████████████████████████▋                                                      | 22/50 [02:13<00:29,  1.04s/it]INFO:vector_store:Embedding progress: 44.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████▌                                                    | 23/50 [02:25<01:49,  4.04s/it]INFO:vector_store:Embedding progress: 46.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▌                                                  | 24/50 [02:40<03:03,  7.05s/it]INFO:vector_store:Embedding progress: 48.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 25/50 [02:41<02:15,  5.44s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▍                                              | 26/50 [02:42<01:34,  3.92s/it]INFO:vector_store:Embedding progress: 52.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|████████████████████████████████████████████████████▍                                            | 27/50 [02:42<01:06,  2.88s/it]INFO:vector_store:Embedding progress: 54.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|██████████████████████████████████████████████████████▎                                          | 28/50 [02:48<01:21,  3.70s/it]INFO:vector_store:Embedding progress: 56.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|████████████████████████████████████████████████████████▎                                        | 29/50 [02:50<01:09,  3.31s/it]INFO:vector_store:Embedding progress: 58.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 30/50 [02:52<00:56,  2.80s/it]INFO:vector_store:Embedding progress: 60.0%
INFO:vector_store:Embedding progress: 62.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|██████████████████████████████████████████████████████████████                                   | 32/50 [02:52<00:29,  1.65s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|████████████████████████████████████████████████████████████████                                 | 33/50 [02:53<00:26,  1.57s/it]INFO:vector_store:Embedding progress: 66.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▉                               | 34/50 [03:00<00:43,  2.74s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|███████████████████████████████████████████████████████████████████▉                             | 35/50 [03:20<01:54,  7.66s/it]INFO:vector_store:Embedding progress: 70.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 72.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|███████████████████████████████████████████████████████████████████████▊                         | 37/50 [03:21<00:57,  4.42s/it]INFO:vector_store:Embedding progress: 74.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|█████████████████████████████████████████████████████████████████████████▋                       | 38/50 [03:21<00:42,  3.51s/it]INFO:vector_store:Embedding progress: 76.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|███████████████████████████████████████████████████████████████████████████▋                     | 39/50 [03:24<00:36,  3.28s/it]INFO:vector_store:Embedding progress: 78.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|█████████████████████████████████████████████████████████████████████████████▌                   | 40/50 [03:26<00:27,  2.78s/it]INFO:vector_store:Embedding progress: 80.0%
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▌                 | 41/50 [03:27<00:20,  2.32s/it]INFO:vector_store:Embedding progress: 82.0%
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▍               | 42/50 [03:27<00:14,  1.80s/it]INFO:vector_store:Embedding progress: 84.0%
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▍             | 43/50 [03:27<00:09,  1.33s/it]INFO:vector_store:Embedding progress: 86.0%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▎           | 44/50 [03:29<00:07,  1.31s/it]INFO:vector_store:Embedding progress: 88.0%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▎         | 45/50 [03:32<00:10,  2.02s/it]INFO:vector_store:Embedding progress: 90.0%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▏       | 46/50 [03:43<00:17,  4.49s/it]INFO:vector_store:Embedding progress: 92.0%
INFO:vector_store:Embedding progress: 94.0%
INFO:vector_store:Embedding progress: 96.0%
Creating embeddings:  98%|███████████████████████████████████████████████████████████████████████████████████████████████  | 49/50 [03:43<00:02,  2.03s/it]INFO:vector_store:Embedding progress: 98.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [03:44<00:00,  1.73s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [03:44<00:00,  4.48s/it]
INFO:vector_store:Processed 54714 chunks so far
INFO:vector_store:Processed 55714 chunks so far
INFO:vector_store:Processed 56714 chunks so far
INFO:vector_store:Processed 57714 chunks so far
INFO:vector_store:Processed 58714 chunks so far
INFO:vector_store:Processing document batch 13 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/50 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▉                                                                                              | 1/50 [01:26<1:10:54, 86.82s/it]INFO:vector_store:Embedding progress: 2.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                              | 2/50 [01:27<28:47, 35.98s/it]INFO:vector_store:Embedding progress: 4.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▉                                                                                            | 3/50 [01:27<15:27, 19.72s/it]INFO:vector_store:Embedding progress: 6.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▊                                                                                          | 4/50 [01:27<09:11, 11.99s/it]INFO:vector_store:Embedding progress: 8.0%
INFO:vector_store:Embedding progress: 10.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 12.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▋                                                                                    | 7/50 [01:27<03:13,  4.49s/it]INFO:vector_store:Embedding progress: 14.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 16.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▋                                                                                | 9/50 [01:28<01:57,  2.87s/it]INFO:vector_store:Embedding progress: 18.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 20.0%
INFO:vector_store:Embedding progress: 22.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▎                                                                         | 12/50 [01:57<03:44,  5.91s/it]INFO:vector_store:Embedding progress: 24.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▏                                                                       | 13/50 [02:01<03:28,  5.63s/it]INFO:vector_store:Embedding progress: 26.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▏                                                                     | 14/50 [02:02<02:45,  4.59s/it]INFO:vector_store:Embedding progress: 28.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|█████████████████████████████                                                                    | 15/50 [02:02<02:06,  3.60s/it]INFO:vector_store:Embedding progress: 30.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 32.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|████████████████████████████████▉                                                                | 17/50 [02:02<01:14,  2.27s/it]INFO:vector_store:Embedding progress: 34.0%
INFO:vector_store:Embedding progress: 36.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▊                                                            | 19/50 [02:02<00:45,  1.48s/it]INFO:vector_store:Embedding progress: 38.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▊                                                          | 20/50 [02:05<00:51,  1.71s/it]INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▋                                                        | 21/50 [02:05<00:39,  1.38s/it]INFO:vector_store:Embedding progress: 42.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|██████████████████████████████████████████▋                                                      | 22/50 [02:06<00:33,  1.19s/it]INFO:vector_store:Embedding progress: 44.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████▌                                                    | 23/50 [02:28<03:02,  6.78s/it]INFO:vector_store:Embedding progress: 46.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▌                                                  | 24/50 [02:37<03:09,  7.30s/it]INFO:vector_store:Embedding progress: 48.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 25/50 [02:38<02:16,  5.46s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▍                                              | 26/50 [02:38<01:35,  3.96s/it]INFO:vector_store:Embedding progress: 52.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|████████████████████████████████████████████████████▍                                            | 27/50 [02:38<01:06,  2.90s/it]INFO:vector_store:Embedding progress: 54.0%
INFO:vector_store:Embedding progress: 56.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|████████████████████████████████████████████████████████▎                                        | 29/50 [02:38<00:34,  1.63s/it]INFO:vector_store:Embedding progress: 58.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 30/50 [02:39<00:26,  1.31s/it]INFO:vector_store:Embedding progress: 60.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|████████████████████████████████████████████████████████████▏                                    | 31/50 [02:40<00:26,  1.41s/it]INFO:vector_store:Embedding progress: 62.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|██████████████████████████████████████████████████████████████                                   | 32/50 [02:41<00:19,  1.06s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|████████████████████████████████████████████████████████████████                                 | 33/50 [02:41<00:14,  1.18it/s]INFO:vector_store:Embedding progress: 66.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▉                               | 34/50 [02:59<01:32,  5.77s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|███████████████████████████████████████████████████████████████████▉                             | 35/50 [03:14<02:06,  8.45s/it]INFO:vector_store:Embedding progress: 70.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▊                           | 36/50 [03:15<01:28,  6.32s/it]INFO:vector_store:Embedding progress: 72.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|███████████████████████████████████████████████████████████████████████▊                         | 37/50 [03:15<00:58,  4.52s/it]INFO:vector_store:Embedding progress: 74.0%
INFO:vector_store:Embedding progress: 76.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|███████████████████████████████████████████████████████████████████████████▋                     | 39/50 [03:16<00:27,  2.52s/it]INFO:vector_store:Embedding progress: 78.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 80.0%
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▌                 | 41/50 [03:16<00:14,  1.60s/it]INFO:vector_store:Embedding progress: 82.0%
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▍               | 42/50 [03:17<00:12,  1.53s/it]INFO:vector_store:Embedding progress: 84.0%
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▍             | 43/50 [03:18<00:08,  1.19s/it]INFO:vector_store:Embedding progress: 86.0%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▎           | 44/50 [03:18<00:05,  1.04it/s]INFO:vector_store:Embedding progress: 88.0%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▎         | 45/50 [03:25<00:12,  2.57s/it]INFO:vector_store:Embedding progress: 90.0%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▏       | 46/50 [03:34<00:17,  4.35s/it]INFO:vector_store:Embedding progress: 92.0%
Creating embeddings:  94%|███████████████████████████████████████████████████████████████████████████████████████████▏     | 47/50 [03:35<00:10,  3.46s/it]INFO:vector_store:Embedding progress: 94.0%
Creating embeddings:  96%|█████████████████████████████████████████████████████████████████████████████████████████████    | 48/50 [03:35<00:05,  2.53s/it]INFO:vector_store:Embedding progress: 96.0%
INFO:vector_store:Embedding progress: 98.0%
INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [03:35<00:00,  4.32s/it]
INFO:vector_store:Processed 59714 chunks so far
INFO:vector_store:Processed 60714 chunks so far
INFO:vector_store:Processed 61714 chunks so far
INFO:vector_store:Processed 62714 chunks so far
INFO:vector_store:Processed 63714 chunks so far
INFO:vector_store:Processing document batch 14 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/50 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▉                                                                                              | 1/50 [01:25<1:09:35, 85.22s/it]INFO:vector_store:Embedding progress: 2.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                              | 2/50 [01:25<28:23, 35.49s/it]INFO:vector_store:Embedding progress: 4.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 6.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▊                                                                                          | 4/50 [01:26<10:11, 13.30s/it]INFO:vector_store:Embedding progress: 8.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▊                                                                                        | 5/50 [01:26<06:56,  9.26s/it]INFO:vector_store:Embedding progress: 10.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▊                                                                                      | 6/50 [01:26<04:44,  6.47s/it]INFO:vector_store:Embedding progress: 12.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▋                                                                                    | 7/50 [01:26<03:17,  4.59s/it]INFO:vector_store:Embedding progress: 14.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 16.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▋                                                                                | 9/50 [01:59<06:48,  9.97s/it]INFO:vector_store:Embedding progress: 18.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████▍                                                                             | 10/50 [02:00<05:15,  7.89s/it]INFO:vector_store:Embedding progress: 20.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████▎                                                                           | 11/50 [02:01<03:53,  5.98s/it]INFO:vector_store:Embedding progress: 22.0%
INFO:vector_store:Embedding progress: 24.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▏                                                                       | 13/50 [02:01<02:09,  3.50s/it]INFO:vector_store:Embedding progress: 26.0%
INFO:vector_store:Embedding progress: 28.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 30.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|███████████████████████████████                                                                  | 16/50 [02:02<01:03,  1.88s/it]INFO:vector_store:Embedding progress: 32.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 34.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|██████████████████████████████████▉                                                              | 18/50 [02:02<00:42,  1.32s/it]INFO:vector_store:Embedding progress: 36.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 38.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▊                                                          | 20/50 [02:28<02:27,  4.90s/it]INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▋                                                        | 21/50 [02:34<02:31,  5.22s/it]INFO:vector_store:Embedding progress: 42.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|██████████████████████████████████████████▋                                                      | 22/50 [02:35<02:02,  4.38s/it]INFO:vector_store:Embedding progress: 44.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 46.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▌                                                  | 24/50 [02:37<01:18,  3.02s/it]INFO:vector_store:Embedding progress: 48.0%
INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 52.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 54.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|██████████████████████████████████████████████████████▎                                          | 28/50 [02:37<00:32,  1.49s/it]INFO:vector_store:Embedding progress: 56.0%
INFO:vector_store:Embedding progress: 58.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 60.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|████████████████████████████████████████████████████████████▏                                    | 31/50 [03:12<01:36,  5.07s/it]INFO:vector_store:Embedding progress: 62.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|██████████████████████████████████████████████████████████████                                   | 32/50 [03:13<01:22,  4.56s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|████████████████████████████████████████████████████████████████                                 | 33/50 [03:17<01:15,  4.43s/it]INFO:vector_store:Embedding progress: 66.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▉                               | 34/50 [03:21<01:09,  4.37s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 70.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▊                           | 36/50 [03:21<00:39,  2.82s/it]INFO:vector_store:Embedding progress: 72.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|███████████████████████████████████████████████████████████████████████▊                         | 37/50 [03:21<00:29,  2.28s/it]INFO:vector_store:Embedding progress: 74.0%
INFO:vector_store:Embedding progress: 76.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 78.0%
INFO:vector_store:Embedding progress: 80.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▌                 | 41/50 [03:22<00:09,  1.09s/it]INFO:vector_store:Embedding progress: 82.0%
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▍               | 42/50 [03:39<00:29,  3.72s/it]INFO:vector_store:Embedding progress: 84.0%
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▍             | 43/50 [03:43<00:26,  3.73s/it]INFO:vector_store:Embedding progress: 86.0%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▎           | 44/50 [03:43<00:17,  2.97s/it]INFO:vector_store:Embedding progress: 88.0%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▎         | 45/50 [03:50<00:19,  3.92s/it]INFO:vector_store:Embedding progress: 90.0%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▏       | 46/50 [03:50<00:11,  2.97s/it]INFO:vector_store:Embedding progress: 92.0%
INFO:vector_store:Embedding progress: 94.0%
INFO:vector_store:Embedding progress: 96.0%
INFO:vector_store:Embedding progress: 98.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [03:50<00:00,  1.24s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [03:50<00:00,  4.62s/it]
INFO:vector_store:Processed 64714 chunks so far
INFO:vector_store:Processed 65714 chunks so far
INFO:vector_store:Processed 66714 chunks so far
INFO:vector_store:Processed 67714 chunks so far
INFO:vector_store:Processed 68714 chunks so far
INFO:vector_store:Processing document batch 15 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/50 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▉                                                                                             | 1/50 [01:44<1:25:16, 104.42s/it]INFO:vector_store:Embedding progress: 2.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                              | 2/50 [01:45<35:01, 43.78s/it]INFO:vector_store:Embedding progress: 4.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▉                                                                                            | 3/50 [01:46<18:46, 23.97s/it]INFO:vector_store:Embedding progress: 6.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▊                                                                                          | 4/50 [01:46<11:11, 14.60s/it]INFO:vector_store:Embedding progress: 8.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▊                                                                                        | 5/50 [01:47<07:16,  9.70s/it]INFO:vector_store:Embedding progress: 10.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▊                                                                                      | 6/50 [01:47<04:49,  6.58s/it]INFO:vector_store:Embedding progress: 12.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▋                                                                                    | 7/50 [01:56<05:17,  7.39s/it]INFO:vector_store:Embedding progress: 14.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▋                                                                                  | 8/50 [02:01<04:35,  6.56s/it]INFO:vector_store:Embedding progress: 16.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▋                                                                                | 9/50 [02:08<04:26,  6.49s/it]INFO:vector_store:Embedding progress: 18.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████▍                                                                             | 10/50 [02:08<03:09,  4.73s/it]INFO:vector_store:Embedding progress: 20.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████▎                                                                           | 11/50 [02:09<02:11,  3.38s/it]INFO:vector_store:Embedding progress: 22.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▎                                                                         | 12/50 [02:16<02:58,  4.71s/it]INFO:vector_store:Embedding progress: 24.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▏                                                                       | 13/50 [02:19<02:30,  4.08s/it]INFO:vector_store:Embedding progress: 26.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▏                                                                     | 14/50 [02:19<01:44,  2.91s/it]INFO:vector_store:Embedding progress: 28.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|█████████████████████████████                                                                    | 15/50 [02:20<01:22,  2.35s/it]INFO:vector_store:Embedding progress: 30.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|███████████████████████████████                                                                  | 16/50 [02:32<02:54,  5.12s/it]INFO:vector_store:Embedding progress: 32.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|████████████████████████████████▉                                                                | 17/50 [02:32<02:00,  3.64s/it]INFO:vector_store:Embedding progress: 34.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|██████████████████████████████████▉                                                              | 18/50 [02:34<01:38,  3.07s/it]INFO:vector_store:Embedding progress: 36.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▊                                                            | 19/50 [02:36<01:26,  2.80s/it]INFO:vector_store:Embedding progress: 38.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▊                                                          | 20/50 [02:41<01:40,  3.35s/it]INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▋                                                        | 21/50 [02:41<01:11,  2.46s/it]INFO:vector_store:Embedding progress: 42.0%
INFO:vector_store:Embedding progress: 44.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████▌                                                    | 23/50 [02:45<00:59,  2.21s/it]INFO:vector_store:Embedding progress: 46.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▌                                                  | 24/50 [02:46<00:48,  1.87s/it]INFO:vector_store:Embedding progress: 48.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 25/50 [02:46<00:35,  1.43s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▍                                              | 26/50 [02:46<00:26,  1.10s/it]INFO:vector_store:Embedding progress: 52.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|████████████████████████████████████████████████████▍                                            | 27/50 [03:08<02:36,  6.81s/it]INFO:vector_store:Embedding progress: 54.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|██████████████████████████████████████████████████████▎                                          | 28/50 [03:10<01:59,  5.44s/it]INFO:vector_store:Embedding progress: 56.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|████████████████████████████████████████████████████████▎                                        | 29/50 [03:10<01:24,  4.02s/it]INFO:vector_store:Embedding progress: 58.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 30/50 [03:10<00:58,  2.94s/it]INFO:vector_store:Embedding progress: 60.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|████████████████████████████████████████████████████████████▏                                    | 31/50 [03:22<01:42,  5.38s/it]INFO:vector_store:Embedding progress: 62.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|██████████████████████████████████████████████████████████████                                   | 32/50 [03:22<01:10,  3.93s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:  66%|████████████████████████████████████████████████████████████████                                 | 33/50 [03:22<00:47,  2.80s/it]INFO:vector_store:Embedding progress: 66.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▉                               | 34/50 [03:24<00:38,  2.44s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|███████████████████████████████████████████████████████████████████▉                             | 35/50 [03:24<00:26,  1.75s/it]INFO:vector_store:Embedding progress: 70.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▊                           | 36/50 [03:24<00:18,  1.30s/it]INFO:vector_store:Embedding progress: 72.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 74.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|█████████████████████████████████████████████████████████████████████████▋                       | 38/50 [03:34<00:35,  2.93s/it]INFO:vector_store:Embedding progress: 76.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 78.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 80.0%
INFO:vector_store:Embedding progress: 82.0%
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▍               | 42/50 [03:55<00:34,  4.31s/it]INFO:vector_store:Embedding progress: 84.0%
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▍             | 43/50 [04:12<00:44,  6.30s/it]INFO:vector_store:Embedding progress: 86.0%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▎           | 44/50 [04:12<00:30,  5.15s/it]INFO:vector_store:Embedding progress: 88.0%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▎         | 45/50 [04:13<00:20,  4.17s/it]INFO:vector_store:Embedding progress: 90.0%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▏       | 46/50 [04:13<00:12,  3.25s/it]INFO:vector_store:Embedding progress: 92.0%
Creating embeddings:  94%|███████████████████████████████████████████████████████████████████████████████████████████▏     | 47/50 [04:13<00:07,  2.50s/it]INFO:vector_store:Embedding progress: 94.0%
INFO:vector_store:Embedding progress: 96.0%
Creating embeddings:  98%|███████████████████████████████████████████████████████████████████████████████████████████████  | 49/50 [04:13<00:01,  1.48s/it]INFO:vector_store:Embedding progress: 98.0%
INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [04:13<00:00,  5.08s/it]
INFO:vector_store:Processed 69714 chunks so far
INFO:vector_store:Processed 70714 chunks so far
INFO:vector_store:Processed 71714 chunks so far
INFO:vector_store:Processed 72714 chunks so far
INFO:vector_store:Processed 73714 chunks so far
INFO:vector_store:Processing document batch 16 of 16
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                         | 0/272 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   0%|▎                                                                                              | 1/272 [01:34<7:06:58, 94.53s/it]INFO:vector_store:Embedding progress: 0.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   1%|▋                                                                                              | 2/272 [01:34<2:55:46, 39.06s/it]INFO:vector_store:Embedding progress: 0.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   1%|█                                                                                              | 3/272 [01:35<1:36:11, 21.46s/it]INFO:vector_store:Embedding progress: 1.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   1%|█▍                                                                                               | 4/272 [01:36<59:24, 13.30s/it]INFO:vector_store:Embedding progress: 1.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▊                                                                                               | 5/272 [01:36<38:05,  8.56s/it]INFO:vector_store:Embedding progress: 1.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 2.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   3%|██▍                                                                                              | 7/272 [01:36<18:54,  4.28s/it]INFO:vector_store:Embedding progress: 2.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   3%|██▊                                                                                              | 8/272 [01:36<13:57,  3.17s/it]INFO:vector_store:Embedding progress: 2.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 3.3%
INFO:vector_store:Embedding progress: 3.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                            | 11/272 [01:36<06:34,  1.51s/it]INFO:vector_store:Embedding progress: 4.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|████▏                                                                                           | 12/272 [02:31<53:10, 12.27s/it]INFO:vector_store:Embedding progress: 4.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   5%|████▌                                                                                           | 13/272 [02:33<43:01,  9.97s/it]INFO:vector_store:Embedding progress: 4.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   5%|████▉                                                                                           | 14/272 [02:33<32:46,  7.62s/it]INFO:vector_store:Embedding progress: 5.1%
INFO:vector_store:Embedding progress: 5.5%
INFO:vector_store:Embedding progress: 5.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|██████                                                                                          | 17/272 [02:33<16:03,  3.78s/it]INFO:vector_store:Embedding progress: 6.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   7%|██████▎                                                                                         | 18/272 [02:34<13:09,  3.11s/it]INFO:vector_store:Embedding progress: 6.6%
INFO:vector_store:Embedding progress: 7.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 7.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▍                                                                                        | 21/272 [02:34<07:10,  1.71s/it]INFO:vector_store:Embedding progress: 7.7%
INFO:vector_store:Embedding progress: 8.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|████████                                                                                        | 23/272 [03:19<33:23,  8.05s/it]INFO:vector_store:Embedding progress: 8.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   9%|████████▍                                                                                       | 24/272 [03:31<35:47,  8.66s/it]INFO:vector_store:Embedding progress: 8.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   9%|████████▊                                                                                       | 25/272 [03:31<28:56,  7.03s/it]INFO:vector_store:Embedding progress: 9.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▏                                                                                      | 26/272 [03:32<22:30,  5.49s/it]INFO:vector_store:Embedding progress: 9.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▌                                                                                      | 27/272 [03:32<17:14,  4.22s/it]INFO:vector_store:Embedding progress: 9.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▉                                                                                      | 28/272 [03:32<13:08,  3.23s/it]INFO:vector_store:Embedding progress: 10.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  11%|██████████▏                                                                                     | 29/272 [03:32<09:47,  2.42s/it]INFO:vector_store:Embedding progress: 10.7%
INFO:vector_store:Embedding progress: 11.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 11.4%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 11.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▋                                                                                    | 33/272 [03:33<04:04,  1.02s/it]INFO:vector_store:Embedding progress: 12.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|████████████                                                                                    | 34/272 [04:10<29:46,  7.51s/it]INFO:vector_store:Embedding progress: 12.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  13%|████████████▎                                                                                   | 35/272 [04:29<38:40,  9.79s/it]INFO:vector_store:Embedding progress: 12.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  13%|████████████▋                                                                                   | 36/272 [04:30<30:31,  7.76s/it]INFO:vector_store:Embedding progress: 13.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████                                                                                   | 37/272 [04:30<23:14,  5.93s/it]INFO:vector_store:Embedding progress: 13.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▍                                                                                  | 38/272 [04:31<17:42,  4.54s/it]INFO:vector_store:Embedding progress: 14.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▊                                                                                  | 39/272 [04:31<13:44,  3.54s/it]INFO:vector_store:Embedding progress: 14.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  15%|██████████████                                                                                  | 40/272 [04:32<10:42,  2.77s/it]INFO:vector_store:Embedding progress: 14.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 15.1%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  15%|██████████████▊                                                                                 | 42/272 [04:32<06:05,  1.59s/it]INFO:vector_store:Embedding progress: 15.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▏                                                                                | 43/272 [04:33<05:05,  1.33s/it]INFO:vector_store:Embedding progress: 15.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▌                                                                                | 44/272 [04:33<04:03,  1.07s/it]INFO:vector_store:Embedding progress: 16.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  17%|███████████████▉                                                                                | 45/272 [04:39<08:37,  2.28s/it]INFO:vector_store:Embedding progress: 16.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  17%|████████████████▏                                                                               | 46/272 [05:26<55:12, 14.66s/it]INFO:vector_store:Embedding progress: 16.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  17%|████████████████▌                                                                               | 47/272 [05:29<42:47, 11.41s/it]INFO:vector_store:Embedding progress: 17.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|████████████████▉                                                                               | 48/272 [05:33<34:11,  9.16s/it]INFO:vector_store:Embedding progress: 17.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▎                                                                              | 49/272 [05:34<25:19,  6.81s/it]INFO:vector_store:Embedding progress: 18.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▋                                                                              | 50/272 [05:35<19:05,  5.16s/it]INFO:vector_store:Embedding progress: 18.4%
INFO:vector_store:Embedding progress: 18.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  19%|██████████████████▎                                                                             | 52/272 [05:35<10:29,  2.86s/it]INFO:vector_store:Embedding progress: 19.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  19%|██████████████████▋                                                                             | 53/272 [05:36<08:12,  2.25s/it]INFO:vector_store:Embedding progress: 19.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████                                                                             | 54/272 [05:36<06:32,  1.80s/it]INFO:vector_store:Embedding progress: 19.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████▍                                                                            | 55/272 [05:37<05:48,  1.61s/it]INFO:vector_store:Embedding progress: 20.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 20.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  21%|████████████████████                                                                            | 57/272 [06:20<37:04, 10.35s/it]INFO:vector_store:Embedding progress: 21.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  21%|████████████████████▍                                                                           | 58/272 [06:24<31:23,  8.80s/it]INFO:vector_store:Embedding progress: 21.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|████████████████████▊                                                                           | 59/272 [06:31<29:04,  8.19s/it]INFO:vector_store:Embedding progress: 21.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████▏                                                                          | 60/272 [06:33<23:06,  6.54s/it]INFO:vector_store:Embedding progress: 22.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████▌                                                                          | 61/272 [06:35<18:39,  5.31s/it]INFO:vector_store:Embedding progress: 22.4%
INFO:vector_store:Embedding progress: 22.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  23%|██████████████████████▏                                                                         | 63/272 [06:35<10:43,  3.08s/it]INFO:vector_store:Embedding progress: 23.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|██████████████████████▌                                                                         | 64/272 [06:36<08:26,  2.44s/it]INFO:vector_store:Embedding progress: 23.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|██████████████████████▉                                                                         | 65/272 [06:36<06:29,  1.88s/it]INFO:vector_store:Embedding progress: 23.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▎                                                                        | 66/272 [06:36<05:06,  1.49s/it]INFO:vector_store:Embedding progress: 24.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  25%|███████████████████████▋                                                                        | 67/272 [06:36<03:48,  1.12s/it]INFO:vector_store:Embedding progress: 24.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  25%|████████████████████████                                                                        | 68/272 [07:14<38:31, 11.33s/it]INFO:vector_store:Embedding progress: 25.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  25%|████████████████████████▎                                                                       | 69/272 [07:16<29:45,  8.80s/it]INFO:vector_store:Embedding progress: 25.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|████████████████████████▋                                                                       | 70/272 [07:20<24:49,  7.37s/it]INFO:vector_store:Embedding progress: 25.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████                                                                       | 71/272 [07:23<20:44,  6.19s/it]INFO:vector_store:Embedding progress: 26.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▍                                                                      | 72/272 [07:33<24:24,  7.32s/it]INFO:vector_store:Embedding progress: 26.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  27%|█████████████████████████▊                                                                      | 73/272 [07:38<21:05,  6.36s/it]INFO:vector_store:Embedding progress: 26.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  27%|██████████████████████████                                                                      | 74/272 [07:41<18:03,  5.47s/it]INFO:vector_store:Embedding progress: 27.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|██████████████████████████▍                                                                     | 75/272 [07:41<12:55,  3.94s/it]INFO:vector_store:Embedding progress: 27.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|██████████████████████████▊                                                                     | 76/272 [07:42<09:26,  2.89s/it]INFO:vector_store:Embedding progress: 27.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▏                                                                    | 77/272 [07:43<07:49,  2.41s/it]INFO:vector_store:Embedding progress: 28.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  29%|███████████████████████████▌                                                                    | 78/272 [07:43<05:51,  1.81s/it]INFO:vector_store:Embedding progress: 28.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  29%|███████████████████████████▉                                                                    | 79/272 [08:14<33:17, 10.35s/it]INFO:vector_store:Embedding progress: 29.0%
Creating embeddings:  29%|████████████████████████████▏                                                                   | 80/272 [08:14<23:19,  7.29s/it]INFO:vector_store:Embedding progress: 29.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|████████████████████████████▌                                                                   | 81/272 [08:23<24:42,  7.76s/it]INFO:vector_store:Embedding progress: 29.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|████████████████████████████▉                                                                   | 82/272 [08:26<20:42,  6.54s/it]INFO:vector_store:Embedding progress: 30.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  31%|█████████████████████████████▎                                                                  | 83/272 [08:32<19:59,  6.35s/it]INFO:vector_store:Embedding progress: 30.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  31%|█████████████████████████████▋                                                                  | 84/272 [08:41<22:07,  7.06s/it]INFO:vector_store:Embedding progress: 30.9%
Creating embeddings:  31%|██████████████████████████████                                                                  | 85/272 [08:44<17:46,  5.70s/it]INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 31.2%
INFO:vector_store:Embedding progress: 31.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 32.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|███████████████████████████████                                                                 | 88/272 [08:44<07:47,  2.54s/it]INFO:vector_store:Embedding progress: 32.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  33%|███████████████████████████████▍                                                                | 89/272 [08:45<06:46,  2.22s/it]INFO:vector_store:Embedding progress: 32.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  33%|███████████████████████████████▊                                                                | 90/272 [09:11<23:41,  7.81s/it]INFO:vector_store:Embedding progress: 33.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  33%|████████████████████████████████                                                                | 91/272 [09:11<17:58,  5.96s/it]INFO:vector_store:Embedding progress: 33.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|████████████████████████████████▍                                                               | 92/272 [09:19<19:18,  6.44s/it]INFO:vector_store:Embedding progress: 33.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|████████████████████████████████▊                                                               | 93/272 [09:23<16:50,  5.64s/it]INFO:vector_store:Embedding progress: 34.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  35%|█████████████████████████████████▏                                                              | 94/272 [09:26<14:32,  4.90s/it]INFO:vector_store:Embedding progress: 34.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  35%|█████████████████████████████████▌                                                              | 95/272 [09:41<22:55,  7.77s/it]INFO:vector_store:Embedding progress: 34.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  35%|█████████████████████████████████▉                                                              | 96/272 [09:41<16:21,  5.58s/it]INFO:vector_store:Embedding progress: 35.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|██████████████████████████████████▏                                                             | 97/272 [09:41<11:45,  4.03s/it]INFO:vector_store:Embedding progress: 35.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|██████████████████████████████████▌                                                             | 98/272 [09:42<08:39,  2.98s/it]INFO:vector_store:Embedding progress: 36.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|██████████████████████████████████▉                                                             | 99/272 [09:42<06:29,  2.25s/it]INFO:vector_store:Embedding progress: 36.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  37%|██████████████████████████████████▉                                                            | 100/272 [09:47<08:11,  2.86s/it]INFO:vector_store:Embedding progress: 36.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  37%|███████████████████████████████████▎                                                           | 101/272 [10:15<30:11, 10.59s/it]INFO:vector_store:Embedding progress: 37.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|███████████████████████████████████▋                                                           | 102/272 [10:17<22:27,  7.93s/it]INFO:vector_store:Embedding progress: 37.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|███████████████████████████████████▉                                                           | 103/272 [10:18<16:46,  5.96s/it]INFO:vector_store:Embedding progress: 37.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▎                                                          | 104/272 [10:19<11:58,  4.28s/it]INFO:vector_store:Embedding progress: 38.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  39%|████████████████████████████████████▋                                                          | 105/272 [10:21<10:34,  3.80s/it]INFO:vector_store:Embedding progress: 38.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  39%|█████████████████████████████████████                                                          | 106/272 [10:37<20:26,  7.39s/it]INFO:vector_store:Embedding progress: 39.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  39%|█████████████████████████████████████▎                                                         | 107/272 [10:37<14:22,  5.23s/it]INFO:vector_store:Embedding progress: 39.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|█████████████████████████████████████▋                                                         | 108/272 [10:38<10:15,  3.75s/it]INFO:vector_store:Embedding progress: 39.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████                                                         | 109/272 [10:38<07:45,  2.86s/it]INFO:vector_store:Embedding progress: 40.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▍                                                        | 110/272 [10:39<05:30,  2.04s/it]INFO:vector_store:Embedding progress: 40.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  41%|██████████████████████████████████████▊                                                        | 111/272 [10:42<06:34,  2.45s/it]INFO:vector_store:Embedding progress: 40.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  41%|███████████████████████████████████████                                                        | 112/272 [11:09<26:17,  9.86s/it]INFO:vector_store:Embedding progress: 41.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|███████████████████████████████████████▍                                                       | 113/272 [11:11<19:34,  7.39s/it]INFO:vector_store:Embedding progress: 41.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|███████████████████████████████████████▊                                                       | 114/272 [11:12<14:18,  5.44s/it]INFO:vector_store:Embedding progress: 41.9%
INFO:vector_store:Embedding progress: 42.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  43%|████████████████████████████████████████▌                                                      | 116/272 [11:12<08:08,  3.13s/it]INFO:vector_store:Embedding progress: 42.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  43%|████████████████████████████████████████▊                                                      | 117/272 [11:32<18:26,  7.14s/it]INFO:vector_store:Embedding progress: 43.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  43%|█████████████████████████████████████████▏                                                     | 118/272 [11:34<15:10,  5.91s/it]INFO:vector_store:Embedding progress: 43.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|█████████████████████████████████████████▌                                                     | 119/272 [11:36<12:07,  4.75s/it]INFO:vector_store:Embedding progress: 43.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|█████████████████████████████████████████▉                                                     | 120/272 [11:36<08:52,  3.51s/it]INFO:vector_store:Embedding progress: 44.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|██████████████████████████████████████████▎                                                    | 121/272 [11:36<06:30,  2.59s/it]INFO:vector_store:Embedding progress: 44.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  45%|██████████████████████████████████████████▌                                                    | 122/272 [11:39<06:13,  2.49s/it]INFO:vector_store:Embedding progress: 44.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  45%|██████████████████████████████████████████▉                                                    | 123/272 [12:11<27:55, 11.24s/it]INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 45.2%
INFO:vector_store:Embedding progress: 45.6%
Creating embeddings:  46%|███████████████████████████████████████████▋                                                   | 125/272 [12:11<15:07,  6.17s/it]INFO:vector_store:Embedding progress: 46.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████                                                   | 126/272 [12:12<11:33,  4.75s/it]INFO:vector_store:Embedding progress: 46.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  47%|████████████████████████████████████████████▎                                                  | 127/272 [12:12<08:39,  3.58s/it]INFO:vector_store:Embedding progress: 46.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  47%|████████████████████████████████████████████▋                                                  | 128/272 [12:29<17:07,  7.13s/it]INFO:vector_store:Embedding progress: 47.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  47%|█████████████████████████████████████████████                                                  | 129/272 [12:32<14:45,  6.19s/it]INFO:vector_store:Embedding progress: 47.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|█████████████████████████████████████████████▍                                                 | 130/272 [12:34<11:26,  4.84s/it]INFO:vector_store:Embedding progress: 47.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|█████████████████████████████████████████████▊                                                 | 131/272 [12:34<08:10,  3.48s/it]INFO:vector_store:Embedding progress: 48.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  49%|██████████████████████████████████████████████                                                 | 132/272 [12:34<05:58,  2.56s/it]INFO:vector_store:Embedding progress: 48.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  49%|██████████████████████████████████████████████▍                                                | 133/272 [12:36<05:27,  2.36s/it]INFO:vector_store:Embedding progress: 48.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  49%|██████████████████████████████████████████████▊                                                | 134/272 [13:02<21:30,  9.35s/it]INFO:vector_store:Embedding progress: 49.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|███████████████████████████████████████████████▏                                               | 135/272 [13:02<15:10,  6.65s/it]INFO:vector_store:Embedding progress: 49.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|███████████████████████████████████████████████▌                                               | 136/272 [13:03<10:45,  4.74s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|███████████████████████████████████████████████▊                                               | 137/272 [13:04<08:07,  3.61s/it]INFO:vector_store:Embedding progress: 50.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  51%|████████████████████████████████████████████████▏                                              | 138/272 [13:04<06:11,  2.77s/it]INFO:vector_store:Embedding progress: 50.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  51%|████████████████████████████████████████████████▌                                              | 139/272 [13:20<14:50,  6.70s/it]INFO:vector_store:Embedding progress: 51.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  51%|████████████████████████████████████████████████▉                                              | 140/272 [13:34<19:25,  8.83s/it]INFO:vector_store:Embedding progress: 51.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|█████████████████████████████████████████████████▏                                             | 141/272 [13:35<14:08,  6.48s/it]INFO:vector_store:Embedding progress: 51.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|█████████████████████████████████████████████████▌                                             | 142/272 [13:37<11:10,  5.16s/it]INFO:vector_store:Embedding progress: 52.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  53%|█████████████████████████████████████████████████▉                                             | 143/272 [13:38<08:08,  3.79s/it]INFO:vector_store:Embedding progress: 52.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  53%|██████████████████████████████████████████████████▎                                            | 144/272 [13:41<07:29,  3.51s/it]INFO:vector_store:Embedding progress: 52.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  53%|██████████████████████████████████████████████████▋                                            | 145/272 [13:59<17:08,  8.10s/it]INFO:vector_store:Embedding progress: 53.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|██████████████████████████████████████████████████▉                                            | 146/272 [14:01<13:07,  6.25s/it]INFO:vector_store:Embedding progress: 53.7%
INFO:vector_store:Embedding progress: 54.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|███████████████████████████████████████████████████▋                                           | 148/272 [14:02<07:25,  3.59s/it]INFO:vector_store:Embedding progress: 54.4%
INFO:vector_store:Embedding progress: 54.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  55%|████████████████████████████████████████████████████▍                                          | 150/272 [14:17<10:10,  5.00s/it]INFO:vector_store:Embedding progress: 55.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|████████████████████████████████████████████████████▋                                          | 151/272 [14:31<14:01,  6.96s/it]INFO:vector_store:Embedding progress: 55.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|█████████████████████████████████████████████████████                                          | 152/272 [14:33<11:44,  5.87s/it]INFO:vector_store:Embedding progress: 55.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|█████████████████████████████████████████████████████▍                                         | 153/272 [14:34<09:15,  4.67s/it]INFO:vector_store:Embedding progress: 56.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  57%|█████████████████████████████████████████████████████▊                                         | 154/272 [14:35<07:24,  3.77s/it]INFO:vector_store:Embedding progress: 56.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  57%|██████████████████████████████████████████████████████▏                                        | 155/272 [14:37<05:58,  3.06s/it]INFO:vector_store:Embedding progress: 57.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  57%|██████████████████████████████████████████████████████▍                                        | 156/272 [14:57<15:28,  8.00s/it]INFO:vector_store:Embedding progress: 57.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|██████████████████████████████████████████████████████▊                                        | 157/272 [15:00<12:37,  6.58s/it]INFO:vector_store:Embedding progress: 57.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|███████████████████████████████████████████████████████▏                                       | 158/272 [15:01<09:11,  4.84s/it]INFO:vector_store:Embedding progress: 58.1%
INFO:vector_store:Embedding progress: 58.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  59%|███████████████████████████████████████████████████████▉                                       | 160/272 [15:02<05:15,  2.82s/it]INFO:vector_store:Embedding progress: 58.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  59%|████████████████████████████████████████████████████████▏                                      | 161/272 [15:12<08:39,  4.68s/it]INFO:vector_store:Embedding progress: 59.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|████████████████████████████████████████████████████████▌                                      | 162/272 [15:27<13:34,  7.41s/it]INFO:vector_store:Embedding progress: 59.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|████████████████████████████████████████████████████████▉                                      | 163/272 [15:30<10:57,  6.04s/it]INFO:vector_store:Embedding progress: 59.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|█████████████████████████████████████████████████████████▎                                     | 164/272 [15:31<08:49,  4.90s/it]INFO:vector_store:Embedding progress: 60.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  61%|█████████████████████████████████████████████████████████▋                                     | 165/272 [15:33<07:15,  4.07s/it]INFO:vector_store:Embedding progress: 60.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  61%|█████████████████████████████████████████████████████████▉                                     | 166/272 [15:34<05:27,  3.09s/it]INFO:vector_store:Embedding progress: 61.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  61%|██████████████████████████████████████████████████████████▎                                    | 167/272 [15:55<14:24,  8.23s/it]INFO:vector_store:Embedding progress: 61.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|██████████████████████████████████████████████████████████▋                                    | 168/272 [15:58<11:49,  6.82s/it]INFO:vector_store:Embedding progress: 61.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|███████████████████████████████████████████████████████████                                    | 169/272 [15:59<08:27,  4.93s/it]INFO:vector_store:Embedding progress: 62.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|███████████████████████████████████████████████████████████▍                                   | 170/272 [15:59<06:05,  3.59s/it]INFO:vector_store:Embedding progress: 62.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 62.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  63%|████████████████████████████████████████████████████████████                                   | 172/272 [16:07<06:07,  3.68s/it]INFO:vector_store:Embedding progress: 63.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|████████████████████████████████████████████████████████████▍                                  | 173/272 [16:23<11:19,  6.86s/it]INFO:vector_store:Embedding progress: 63.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|████████████████████████████████████████████████████████████▊                                  | 174/272 [16:26<09:36,  5.88s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|█████████████████████████████████████████████████████████████                                  | 175/272 [16:28<07:39,  4.74s/it]INFO:vector_store:Embedding progress: 64.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|█████████████████████████████████████████████████████████████▍                                 | 176/272 [16:30<06:15,  3.92s/it]INFO:vector_store:Embedding progress: 64.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|█████████████████████████████████████████████████████████████▊                                 | 177/272 [16:31<04:49,  3.05s/it]INFO:vector_store:Embedding progress: 65.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|██████████████████████████████████████████████████████████████▏                                | 178/272 [16:48<11:17,  7.21s/it]INFO:vector_store:Embedding progress: 65.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|██████████████████████████████████████████████████████████████▌                                | 179/272 [16:52<09:39,  6.24s/it]INFO:vector_store:Embedding progress: 65.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|██████████████████████████████████████████████████████████████▊                                | 180/272 [16:52<06:50,  4.46s/it]INFO:vector_store:Embedding progress: 66.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  67%|███████████████████████████████████████████████████████████████▏                               | 181/272 [16:53<05:04,  3.34s/it]INFO:vector_store:Embedding progress: 66.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  67%|███████████████████████████████████████████████████████████████▌                               | 182/272 [16:53<03:45,  2.50s/it]INFO:vector_store:Embedding progress: 66.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  67%|███████████████████████████████████████████████████████████████▉                               | 183/272 [16:59<04:58,  3.36s/it]INFO:vector_store:Embedding progress: 67.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|████████████████████████████████████████████████████████████████▎                              | 184/272 [17:05<06:22,  4.35s/it]INFO:vector_store:Embedding progress: 67.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|████████████████████████████████████████████████████████████████▌                              | 185/272 [17:07<05:07,  3.53s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|████████████████████████████████████████████████████████████████▉                              | 186/272 [17:09<04:12,  2.93s/it]INFO:vector_store:Embedding progress: 68.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  69%|█████████████████████████████████████████████████████████████████▎                             | 187/272 [17:10<03:31,  2.49s/it]INFO:vector_store:Embedding progress: 68.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  69%|█████████████████████████████████████████████████████████████████▋                             | 188/272 [17:12<03:05,  2.21s/it]INFO:vector_store:Embedding progress: 69.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  69%|██████████████████████████████████████████████████████████████████                             | 189/272 [17:50<18:07, 13.10s/it]INFO:vector_store:Embedding progress: 69.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|██████████████████████████████████████████████████████████████████▎                            | 190/272 [17:52<13:06,  9.59s/it]INFO:vector_store:Embedding progress: 69.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|██████████████████████████████████████████████████████████████████▋                            | 191/272 [17:52<09:11,  6.81s/it]INFO:vector_store:Embedding progress: 70.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  71%|███████████████████████████████████████████████████████████████████                            | 192/272 [17:53<06:36,  4.96s/it]INFO:vector_store:Embedding progress: 70.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  71%|███████████████████████████████████████████████████████████████████▍                           | 193/272 [17:54<05:08,  3.91s/it]INFO:vector_store:Embedding progress: 71.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  71%|███████████████████████████████████████████████████████████████████▊                           | 194/272 [17:55<03:51,  2.97s/it]INFO:vector_store:Embedding progress: 71.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|████████████████████████████████████████████████████████████████████                           | 195/272 [17:55<02:49,  2.20s/it]INFO:vector_store:Embedding progress: 71.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|████████████████████████████████████████████████████████████████████▍                          | 196/272 [17:56<02:26,  1.92s/it]INFO:vector_store:Embedding progress: 72.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|████████████████████████████████████████████████████████████████████▊                          | 197/272 [17:59<02:48,  2.25s/it]INFO:vector_store:Embedding progress: 72.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  73%|█████████████████████████████████████████████████████████████████████▏                         | 198/272 [18:02<02:58,  2.41s/it]INFO:vector_store:Embedding progress: 72.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  73%|█████████████████████████████████████████████████████████████████████▌                         | 199/272 [18:04<02:39,  2.18s/it]INFO:vector_store:Embedding progress: 73.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|█████████████████████████████████████████████████████████████████████▊                         | 200/272 [18:44<16:16, 13.57s/it]INFO:vector_store:Embedding progress: 73.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|██████████████████████████████████████████████████████████████████████▏                        | 201/272 [18:44<11:22,  9.61s/it]INFO:vector_store:Embedding progress: 73.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|██████████████████████████████████████████████████████████████████████▌                        | 202/272 [18:45<07:56,  6.80s/it]INFO:vector_store:Embedding progress: 74.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  75%|██████████████████████████████████████████████████████████████████████▉                        | 203/272 [18:45<05:33,  4.83s/it]INFO:vector_store:Embedding progress: 74.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  75%|███████████████████████████████████████████████████████████████████████▎                       | 204/272 [18:46<04:06,  3.62s/it]INFO:vector_store:Embedding progress: 75.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  75%|███████████████████████████████████████████████████████████████████████▌                       | 205/272 [18:46<02:59,  2.68s/it]INFO:vector_store:Embedding progress: 75.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|███████████████████████████████████████████████████████████████████████▉                       | 206/272 [18:46<02:08,  1.94s/it]INFO:vector_store:Embedding progress: 75.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|████████████████████████████████████████████████████████████████████████▎                      | 207/272 [18:48<01:52,  1.73s/it]INFO:vector_store:Embedding progress: 76.1%
Creating embeddings:  76%|████████████████████████████████████████████████████████████████████████▋                      | 208/272 [18:48<01:29,  1.40s/it]INFO:vector_store:Embedding progress: 76.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  77%|████████████████████████████████████████████████████████████████████████▉                      | 209/272 [18:52<02:13,  2.11s/it]INFO:vector_store:Embedding progress: 76.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  77%|█████████████████████████████████████████████████████████████████████████▎                     | 210/272 [18:55<02:33,  2.47s/it]INFO:vector_store:Embedding progress: 77.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|█████████████████████████████████████████████████████████████████████████▋                     | 211/272 [19:36<14:15, 14.02s/it]INFO:vector_store:Embedding progress: 77.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|██████████████████████████████████████████████████████████████████████████                     | 212/272 [19:37<09:56,  9.95s/it]INFO:vector_store:Embedding progress: 77.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|██████████████████████████████████████████████████████████████████████████▍                    | 213/272 [19:37<06:55,  7.04s/it]INFO:vector_store:Embedding progress: 78.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  79%|██████████████████████████████████████████████████████████████████████████▋                    | 214/272 [19:39<05:17,  5.48s/it]INFO:vector_store:Embedding progress: 78.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  79%|███████████████████████████████████████████████████████████████████████████                    | 215/272 [19:39<03:45,  3.95s/it]INFO:vector_store:Embedding progress: 79.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  79%|███████████████████████████████████████████████████████████████████████████▍                   | 216/272 [19:40<02:49,  3.03s/it]INFO:vector_store:Embedding progress: 79.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|███████████████████████████████████████████████████████████████████████████▊                   | 217/272 [19:40<02:00,  2.19s/it]INFO:vector_store:Embedding progress: 79.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|████████████████████████████████████████████████████████████████████████████▏                  | 218/272 [19:42<01:45,  1.96s/it]INFO:vector_store:Embedding progress: 80.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  81%|████████████████████████████████████████████████████████████████████████████▍                  | 219/272 [19:42<01:22,  1.56s/it]INFO:vector_store:Embedding progress: 80.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  81%|████████████████████████████████████████████████████████████████████████████▊                  | 220/272 [20:00<05:24,  6.23s/it]INFO:vector_store:Embedding progress: 80.9%
INFO:vector_store:Embedding progress: 81.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  82%|█████████████████████████████████████████████████████████████████████████████▌                 | 222/272 [20:37<09:56, 11.93s/it]INFO:vector_store:Embedding progress: 81.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  82%|█████████████████████████████████████████████████████████████████████████████▉                 | 223/272 [20:37<07:29,  9.17s/it]INFO:vector_store:Embedding progress: 82.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  82%|██████████████████████████████████████████████████████████████████████████████▏                | 224/272 [20:38<05:29,  6.87s/it]INFO:vector_store:Embedding progress: 82.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  83%|██████████████████████████████████████████████████████████████████████████████▌                | 225/272 [20:38<03:57,  5.06s/it]INFO:vector_store:Embedding progress: 82.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  83%|██████████████████████████████████████████████████████████████████████████████▉                | 226/272 [20:39<03:01,  3.94s/it]INFO:vector_store:Embedding progress: 83.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  83%|███████████████████████████████████████████████████████████████████████████████▎               | 227/272 [20:39<02:10,  2.90s/it]INFO:vector_store:Embedding progress: 83.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  84%|███████████████████████████████████████████████████████████████████████████████▋               | 228/272 [20:40<01:36,  2.20s/it]INFO:vector_store:Embedding progress: 83.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  84%|███████████████████████████████████████████████████████████████████████████████▉               | 229/272 [20:41<01:15,  1.76s/it]INFO:vector_store:Embedding progress: 84.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 84.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  85%|████████████████████████████████████████████████████████████████████████████████▋              | 231/272 [20:52<02:22,  3.48s/it]INFO:vector_store:Embedding progress: 84.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  85%|█████████████████████████████████████████████████████████████████████████████████              | 232/272 [20:52<01:48,  2.71s/it]INFO:vector_store:Embedding progress: 85.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  86%|█████████████████████████████████████████████████████████████████████████████████▍             | 233/272 [21:29<07:30, 11.54s/it]INFO:vector_store:Embedding progress: 85.7%
INFO:vector_store:Embedding progress: 86.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  86%|██████████████████████████████████████████████████████████████████████████████████             | 235/272 [21:31<04:19,  7.01s/it]INFO:vector_store:Embedding progress: 86.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  87%|██████████████████████████████████████████████████████████████████████████████████▍            | 236/272 [21:31<03:16,  5.45s/it]INFO:vector_store:Embedding progress: 86.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  87%|██████████████████████████████████████████████████████████████████████████████████▊            | 237/272 [21:31<02:28,  4.23s/it]INFO:vector_store:Embedding progress: 87.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  88%|███████████████████████████████████████████████████████████████████████████████████▏           | 238/272 [21:32<01:47,  3.18s/it]INFO:vector_store:Embedding progress: 87.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  88%|███████████████████████████████████████████████████████████████████████████████████▍           | 239/272 [21:32<01:20,  2.45s/it]INFO:vector_store:Embedding progress: 87.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  88%|███████████████████████████████████████████████████████████████████████████████████▊           | 240/272 [21:32<00:57,  1.81s/it]INFO:vector_store:Embedding progress: 88.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 88.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  89%|████████████████████████████████████████████████████████████████████████████████████▌          | 242/272 [21:39<01:17,  2.57s/it]INFO:vector_store:Embedding progress: 89.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  89%|████████████████████████████████████████████████████████████████████████████████████▊          | 243/272 [21:40<00:59,  2.06s/it]INFO:vector_store:Embedding progress: 89.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  90%|█████████████████████████████████████████████████████████████████████████████████████▏         | 244/272 [22:17<05:12, 11.14s/it]INFO:vector_store:Embedding progress: 89.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  90%|█████████████████████████████████████████████████████████████████████████████████████▌         | 245/272 [22:18<03:46,  8.37s/it]INFO:vector_store:Embedding progress: 90.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  90%|█████████████████████████████████████████████████████████████████████████████████████▉         | 246/272 [22:20<02:50,  6.56s/it]INFO:vector_store:Embedding progress: 90.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  91%|██████████████████████████████████████████████████████████████████████████████████████▎        | 247/272 [22:20<01:59,  4.77s/it]INFO:vector_store:Embedding progress: 90.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  91%|██████████████████████████████████████████████████████████████████████████████████████▌        | 248/272 [22:21<01:27,  3.66s/it]INFO:vector_store:Embedding progress: 91.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 91.5%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  92%|███████████████████████████████████████████████████████████████████████████████████████▎       | 250/272 [22:22<00:48,  2.18s/it]INFO:vector_store:Embedding progress: 91.9%
INFO:vector_store:Embedding progress: 92.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 92.6%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  93%|████████████████████████████████████████████████████████████████████████████████████████▎      | 253/272 [22:26<00:32,  1.70s/it]INFO:vector_store:Embedding progress: 93.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  93%|████████████████████████████████████████████████████████████████████████████████████████▋      | 254/272 [22:26<00:26,  1.49s/it]INFO:vector_store:Embedding progress: 93.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  94%|█████████████████████████████████████████████████████████████████████████████████████████      | 255/272 [23:07<02:48,  9.90s/it]INFO:vector_store:Embedding progress: 93.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  94%|█████████████████████████████████████████████████████████████████████████████████████████▍     | 256/272 [23:10<02:10,  8.18s/it]INFO:vector_store:Embedding progress: 94.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  94%|█████████████████████████████████████████████████████████████████████████████████████████▊     | 257/272 [23:13<01:43,  6.93s/it]INFO:vector_store:Embedding progress: 94.5%
INFO:vector_store:Embedding progress: 94.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  95%|██████████████████████████████████████████████████████████████████████████████████████████▍    | 259/272 [23:14<00:56,  4.33s/it]INFO:vector_store:Embedding progress: 95.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  96%|██████████████████████████████████████████████████████████████████████████████████████████▊    | 260/272 [23:14<00:40,  3.38s/it]INFO:vector_store:Embedding progress: 95.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  96%|███████████████████████████████████████████████████████████████████████████████████████████▏   | 261/272 [23:15<00:29,  2.67s/it]INFO:vector_store:Embedding progress: 96.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  96%|███████████████████████████████████████████████████████████████████████████████████████████▌   | 262/272 [23:15<00:20,  2.05s/it]INFO:vector_store:Embedding progress: 96.3%
Creating embeddings:  97%|███████████████████████████████████████████████████████████████████████████████████████████▊   | 263/272 [23:16<00:15,  1.68s/it]INFO:vector_store:Embedding progress: 96.7%
Creating embeddings:  97%|████████████████████████████████████████████████████████████████████████████████████████████▏  | 264/272 [23:17<00:12,  1.59s/it]INFO:vector_store:Embedding progress: 97.1%
Creating embeddings:  97%|████████████████████████████████████████████████████████████████████████████████████████████▌  | 265/272 [23:18<00:08,  1.23s/it]INFO:vector_store:Embedding progress: 97.4%
Creating embeddings:  98%|████████████████████████████████████████████████████████████████████████████████████████████▉  | 266/272 [23:28<00:22,  3.78s/it]INFO:vector_store:Embedding progress: 97.8%
Creating embeddings:  98%|█████████████████████████████████████████████████████████████████████████████████████████████▎ | 267/272 [23:40<00:31,  6.32s/it]INFO:vector_store:Embedding progress: 98.2%
Creating embeddings:  99%|█████████████████████████████████████████████████████████████████████████████████████████████▌ | 268/272 [23:42<00:19,  4.91s/it]INFO:vector_store:Embedding progress: 98.5%
Creating embeddings:  99%|█████████████████████████████████████████████████████████████████████████████████████████████▉ | 269/272 [23:43<00:11,  3.96s/it]INFO:vector_store:Embedding progress: 98.9%
Creating embeddings:  99%|██████████████████████████████████████████████████████████████████████████████████████████████▎| 270/272 [23:44<00:05,  2.86s/it]INFO:vector_store:Embedding progress: 99.3%
Creating embeddings: 100%|██████████████████████████████████████████████████████████████████████████████████████████████▋| 271/272 [23:44<00:02,  2.13s/it]INFO:vector_store:Embedding progress: 99.6%
INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 272/272 [23:44<00:00,  5.24s/it]
INFO:vector_store:Processed 74714 chunks so far
INFO:vector_store:Processed 75714 chunks so far
INFO:vector_store:Processed 76714 chunks so far
INFO:vector_store:Processed 77714 chunks so far
INFO:vector_store:Processed 78714 chunks so far
INFO:vector_store:Processed 79714 chunks so far
INFO:vector_store:Processed 80714 chunks so far
INFO:vector_store:Processed 81714 chunks so far
INFO:vector_store:Processed 82714 chunks so far
INFO:vector_store:Processed 83714 chunks so far
INFO:vector_store:Processed 84714 chunks so far
INFO:vector_store:Processed 85714 chunks so far
INFO:vector_store:Processed 86714 chunks so far
INFO:vector_store:Processed 87714 chunks so far
INFO:vector_store:Processed 88714 chunks so far
INFO:vector_store:Processed 89714 chunks so far
INFO:vector_store:Processed 90714 chunks so far
INFO:vector_store:Processed 91714 chunks so far
INFO:vector_store:Processed 92714 chunks so far
INFO:vector_store:Processed 93714 chunks so far
INFO:vector_store:Processed 94714 chunks so far
INFO:vector_store:Processed 95714 chunks so far
INFO:vector_store:Processed 96714 chunks so far
INFO:vector_store:Processed 97714 chunks so far
INFO:vector_store:Processed 98714 chunks so far
INFO:vector_store:Processed 99714 chunks so far
INFO:vector_store:Processed 100714 chunks so far
INFO:vector_store:Processed 100841 chunks so far
INFO:vector_store:Completed processing 76140 documents into 100841 chunks
ERROR:rag_system:Failed to add documents to vector store for flood
INFO:rag_system:Processing data for disaster type: plane_crash
INFO:data_ingestion:Processed CSV: data/plane_crash/Plane Crashes.csv, Rows: 28536
INFO:rag_system:Successfully processed 28536 documents from data/plane_crash/Plane Crashes.csv
INFO:rag_system:Successfully processed 1 documents from https://www.thehindu.com/news/national/gujarat/air-india-ahmedabad-plane-crash-death-toll-rises/article69693991.ece
INFO:rag_system:Successfully processed 1 documents from https://timesofindia.indiatimes.com/city/ahmedabad/plane-crashes-in-ahmedabads-meghani-area/articleshow/121798487.cms
INFO:rag_system:Successfully processed 1 documents from https://www.ndtv.com/india-news/ahmedabad-plane-crash-live-updates-air-india-major-plane-crash-dreamliner-787-in-residential-area-emergency-services-rush-to-spot-flight-crash-vijay-r-8649245
INFO:rag_system:Successfully processed 1 documents from https://www.livemint.com/news/air-india-plane-crash-moments-before-ahmedabad-tragedy-pilot-gave-a-final-message-heres-what-he-said-11749956462696.html
INFO:rag_system:Successfully processed 1 documents from https://www.thehindu.com/news/national/gujarat/ahmedabad-flight-crash-a-surprise-that-ended-in-tragedy/article69694711.ece
INFO:rag_system:Successfully processed 1 documents from https://www.hindustantimes.com/india-news/one-more-body-recovered-from-ahmedabad-air-india-crash-site-101749882142877.html
INFO:rag_system:Successfully processed 1 documents from https://economictimes.indiatimes.com/industry/transportation/airlines-/-aviation/expert-discusses-possibility-of-fuel-contamination-behind-ahmedabad-plane-crash/articleshow/121840945.cms?from=mdr
INFO:rag_system:Successfully processed 1 documents from https://www.india.com/news/india/day-after-ahmedabad-plane-crash-another-air-india-flight-aic129-to-london-makes-mid-air-u-turn-returns-to-mumbai-due-to-emerging-situation-in-iran-7880259/
INFO:rag_system:Successfully processed 1 documents from https://www.cnbctv18.com/india/ahmedabad-air-india-plane-crash-live-updates-bodies-recovered-death-toll-bj-medical-college-liveblog-19621095.htm
INFO:rag_system:Successfully processed 1 documents from https://timesofindia.indiatimes.com/city/ahmedabad/ahmedabad-air-india-plane-crash-news-live-air-india-london-flight-crash-sardar-vallabhbhai-patel-international-airport-deaths-injured-rescue-operation-latest-updates/liveblog/121799226.cms
INFO:rag_system:Successfully processed 1 documents from https://www.thehindu.com/news/national/ahmedabad-plane-crash-another-body-recovered-from-crash-site-medical-college-confirms-four-mbbs-students-among-victims/article69694610.ece
INFO:rag_system:Successfully processed 1 documents from https://economictimes.indiatimes.com/industry/transportation/airlines-/-aviation/ahmedabad-plane-crash-engines-lost-power-at-critical-stage-says-ex-air-force-chief-arup-raha/articleshow/121849584.cms?from=mdr
INFO:rag_system:Successfully processed 1 documents from https://indianexpress.com/article/india/ahmedabad-plane-crash-live-updates-10062373/
INFO:rag_system:Successfully processed 1 documents from https://www.pib.gov.in/PressReleasePage.aspx?PRID=2136378
INFO:rag_system:Successfully processed 1 documents from https://www.aljazeera.com/news/2025/6/14/at-least-270-bodies-recovered-from-air-india-crash-site-in-ahmedabad
INFO:rag_system:Successfully processed 1 documents from https://www.newindianexpress.com/nation/2025/Jun/14/gujarat-teen-who-shot-viral-video-of-air-india-plane-crash-records-statement-as-witness
INFO:rag_system:Successfully processed 1 documents from https://timesofindia.indiatimes.com/india/air-india-ai-171-plane-crash-live-updates-ahmedabad-london-air-india-flight-tragedy-242-passengers-international-airport-pm-modi/liveblog/121857714.cms
INFO:rag_system:Successfully processed 1 documents from https://www.ndtv.com/india-news/pilots-last-message-was-mayday-aviation-ministry-on-ahmedabad-air-crash-8666487
INFO:rag_system:Successfully processed 1 documents from https://www.thehindu.com/news/national/ahmedabad-plane-crash-last-remains-of-crash-victims-begin-to-reach-families/article69695470.ece
INFO:rag_system:Successfully processed 1 documents from https://www.thehindu.com/news/national/gujarat/air-india-ahmedabad-plane-crash-death-toll-rises/article69693991.ece
INFO:rag_system:Successfully processed 1 documents from https://timesofindia.indiatimes.com/india/ahmedabad-plane-crash-air-india-ai-express-drop-flight-number-171-report/articleshow/121845745.cms
INFO:rag_system:Successfully processed 1 documents from https://www.thehindu.com/news/national/crash-narrowly-missed-residential-area-and-three-hospitals-staving-off-a-larger-death-toll/article69695557.ece
INFO:rag_system:Successfully processed 1 documents from https://www.thehindu.com/news/international/news-that-one-man-survived-the-ahmedabad-flight-crash-weighs-on-some-other-sole-survivors/article69692877.ece
INFO:rag_system:Successfully processed 1 documents from https://economictimes.indiatimes.com/industry/transportation/airlines-/-aviation/ahmedabad-plane-crash-air-india-announces-additional-rs-25-lakh-compensation-on-top-of-rs-1-crore-to-fast-track-relief-for-victims-families/articleshow/121849426.cms?from=mdr
INFO:rag_system:Successfully processed 1 documents from https://www.thehindu.com/opinion/editorial/crash-and-burn-on-the-ahmedabad-crash-indian-aviation/article69691403.ece
INFO:rag_system:Successfully processed 1 documents from https://www.thehindu.com/news/national/air-india-ahmedabad-air-plane-crash-black-box/article69690768.ece
INFO:rag_system:Successfully processed 1 documents from https://www.livemint.com/news/air-india-plane-crash-how-much-compensation-the-lone-survivor-from-ahmedabad-tragedy-will-receive-from-airline-11749907208459.html
INFO:rag_system:Successfully processed 1 documents from https://timesofindia.indiatimes.com/india/air-india-plane-crash-thrust-not-achieved-falling-mayday-ai-pilots-last-words/articleshow/121855487.cms
INFO:rag_system:Successfully processed 1 documents from https://www.thehindu.com/news/national/ahmedabad-plane-crash-grim-wait-for-kin-as-dna-samples-hold-hope-of-identifying-loved-ones/article69692340.ece
INFO:rag_system:Successfully processed 1 documents from https://www.ndtv.com/india-news/ahmedabad-plane-crash-deaths-rise-to-274-includes-those-on-board-and-on-ground-8664396
INFO:rag_system:Successfully processed 1 documents from https://www.indiatoday.in/india/story/toll-in-air-india-plane-crash-rises-to-270-as-those-injured-at-medical-college-hostel-succumb-2740737-2025-06-14
INFO:rag_system:Successfully processed 1 documents from https://www.thehindu.com/news/national/everything-happened-in-front-of-my-eyes-lone-survivor-of-ahmedabad-plane-crash/article69690395.ece
INFO:rag_system:Successfully processed 1 documents from https://www.thehindu.com/news/national/ahmedabad-plane-crash-government-must-fix-accountability-for-ai-171-accident-says-kharge/article69695369.ece
INFO:rag_system:Successfully processed 1 documents from https://indianexpress.com/article/cities/ahmedabad/ahmedabad-plane-crash-19-identified-through-dna-tests-minister-10067389/
INFO:rag_system:Successfully processed 1 documents from https://www.hindustantimes.com/india-news/air-india-ahmedabad-plane-crash-live-updates-boeing-787-amit-shah-ndrf-rescue-tata-aviation-pm-modi-india-news-us-uk-101749773221075.html
INFO:rag_system:Successfully processed 1 documents from https://www.livemint.com/news/india/ahmedabad-air-india-plane-crash-live-updates-casualties-deaths-latest-news-12-june-2025-11749718614550.html
INFO:rag_system:Successfully processed 1 documents from https://www.bbc.com/news/articles/cdd28legnzvo
INFO:rag_system:Successfully processed 1 documents from https://indianexpress.com/article/india/ahmedabad-plane-crash-live-updates-10062373/
INFO:rag_system:Successfully processed 1 documents from https://timesofindia.indiatimes.com/city/ahmedabad/plane-crashes-in-ahmedabads-meghani-area/articleshow/121798487.cms
INFO:rag_system:Successfully processed 1 documents from https://www.thehindu.com/opinion/editorial/crash-and-burn-on-the-ahmedabad-crash-indian-aviation/article69691403.ece
ERROR:data_ingestion:Error processing URL https://www.reuters.com/world/india/plane-crashes-indias-ahmedabad-airport-tv-channels-report-2025-06-12/: 401 Client Error: HTTP Forbidden for url: https://www.reuters.com/world/india/plane-crashes-indias-ahmedabad-airport-tv-channels-report-2025-06-12/
WARNING:rag_system:No documents extracted from https://www.reuters.com/world/india/plane-crashes-indias-ahmedabad-airport-tv-channels-report-2025-06-12/
INFO:rag_system:Successfully processed 1 documents from https://apnews.com/article/india-plane-crash-cad8dad5cd0e92795b03d357404af5f8
INFO:rag_system:Successfully processed 1 documents from http://bbc.com/news/articles/c2lk55l9wpgo
INFO:rag_system:Successfully processed 1 documents from https://timesofindia.indiatimes.com/india/air-india-plane-crash-dna-samples-of-11-victims-matched-bodies-to-be-handed-over-to-kin/articleshow/121849917.cms
INFO:rag_system:Successfully processed 1 documents from https://www.bbc.com/news/articles/cjwqjv09q7xo
ERROR:data_ingestion:Error processing URL https://www.reuters.com/business/aerospace-defense/rescuers-search-missing-people-aircraft-parts-after-air-india-crash-kills-over-2025-06-13/: 401 Client Error: HTTP Forbidden for url: https://www.reuters.com/business/aerospace-defense/rescuers-search-missing-people-aircraft-parts-after-air-india-crash-kills-over-2025-06-13/
WARNING:rag_system:No documents extracted from https://www.reuters.com/business/aerospace-defense/rescuers-search-missing-people-aircraft-parts-after-air-india-crash-kills-over-2025-06-13/
ERROR:data_ingestion:Error processing URL https://www.reuters.com/world/india/plane-crashes-indias-ahmedabad-airport-tv-channels-report-2025-06-12/: 401 Client Error: HTTP Forbidden for url: https://www.reuters.com/world/india/plane-crashes-indias-ahmedabad-airport-tv-channels-report-2025-06-12/
WARNING:rag_system:No documents extracted from https://www.reuters.com/world/india/plane-crashes-indias-ahmedabad-airport-tv-channels-report-2025-06-12/
INFO:rag_system:Successfully processed 1 documents from https://timesofindia.indiatimes.com/india/ahmedabad-plane-crash-air-india-announces-rs-25-lakh-interim-payment-to-families-of-deceased-says-stands-in-solidarity/articleshow/121849454.cms
INFO:rag_system:Successfully processed 1 documents from https://www.ndtv.com/video/air-india-plane-crash-ahmedabad-plane-crash-ahmedabad-crash-latest-biggest-stories-of-june-14-952748
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1919/1
ERROR:data_ingestion:Error processing URL https://asn.flig`htsafety.org/database/year/1920/1: HTTPSConnectionPool(host='asn.flig%60htsafety.org', port=443): Max retries exceeded with url: /database/year/1920/1 (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x000001AD84C1FD50>: Failed to resolve 'asn.flig%60htsafety.org' ([Errno 11001] getaddrinfo failed)"))
WARNING:rag_system:No documents extracted from https://asn.flig`htsafety.org/database/year/1920/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1921/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1922/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1923/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1924/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1925/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1926/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1927/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1928/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1929/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1930/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1931/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1932/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1933/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1934/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1935/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1936/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1937/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1938/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1939/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1940/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1941/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1942/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1943/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1944/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1945/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1946/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1947/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1948/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1949/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1950/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1951/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1952/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1953/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1954/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1955/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1956/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1957/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1958/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1959/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1960/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1961/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1962/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1963/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1964/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1965/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1966/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1967/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1968/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1969/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1970/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1971/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1972/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1973/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1974/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1975/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1976/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1977/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1978/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1979/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1980/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1981/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1982/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1983/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1984/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1985/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1986/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1987/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1988/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1989/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1990/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1991/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1992/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1993/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1994/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1995/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1996/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1997/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1998/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/1999/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2000/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2001/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2002/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2003/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2004/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2005/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2006/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2007/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2008/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2009/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2010/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2011/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2012/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2013/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2014/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2015/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2016/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2017/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2018/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2019/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2020/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2021/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2022/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2023/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2024/1
INFO:rag_system:Successfully processed 1 documents from https://asn.flightsafety.org/database/year/2025/1
INFO:rag_system:Successfully processed 1 documents from https://www.1001crash.com/
INFO:rag_system:Successfully processed 1 documents from https://flightsafety.org/foundation/80-years-of-aviation-safety-leadership/
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/acr_fatg.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/chklist.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/ctlr.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/animal.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/cabin_fumes.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/chklist.pdf
ERROR:data_ingestion:Error processing URL https://asrs.arc.nasa.gov/docs/rpsts/com_fatigue.pdf: HTTPSConnectionPool(host='asrs.arc.nasa.gov', port=443): Read timed out.
WARNING:rag_system:No documents extracted from https://asrs.arc.nasa.gov/docs/rpsts/com_fatigue.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/icing.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/cftt.pdf
ERROR:data_ingestion:Error processing URL https://asrs.arc.nasa.gov/docs/rpsts/crm.pdf: HTTPSConnectionPool(host='asrs.arc.nasa.gov', port=443): Read timed out.
WARNING:rag_system:No documents extracted from https://asrs.arc.nasa.gov/docs/rpsts/crm.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/ems.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/flt_attendant.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/fuel.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/ga_train.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/gps.pdf
ERROR:data_ingestion:Error processing URL https://asrs.arc.nasa.gov/docs/rpsts/wx.pdf: HTTPSConnectionPool(host='asrs.arc.nasa.gov', port=443): Read timed out.
WARNING:rag_system:No documents extracted from https://asrs.arc.nasa.gov/docs/rpsts/wx.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/mechanic.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/upsets.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/nmac.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/non_twr.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/parachute.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/ped.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/pax.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/penetrat.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/plt_ctlr.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/rnav_arrival.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/helo.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/rwy_incur.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/uas.pdf
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://asrs.arc.nasa.gov/docs/rpsts/waketurb.pdf
INFO:rag_system:Successfully processed 1 documents from https://www.tsb.gc.ca/eng/incidents-occurrence/aviation/index.html
INFO:rag_system:Successfully processed 1 documents from https://www.dgca.gov.in/digigov-portal/?dynamicPage=AccidentReports/500005/0/viewApplicationDtlsReq
INFO:rag_system:Successfully processed 1 documents from https://www.dgca.gov.in/digigov-portal/?dynamicPage=IncidentReports/500006/0/viewApplicationDtlsReq
INFO:rag_system:Successfully processed 1 documents from https://www.dgca.gov.in/digigov-portal/?page=4273/4208/servicename
INFO:rag_system:Successfully processed 1 documents from https://avherald.com/
INFO:rag_system:Successfully processed 1 documents from https://en.wikipedia.org/wiki/List_of_accidents_and_incidents_involving_commercial_aircraft#2025
INFO:rag_system:Successfully processed 1 documents from https://en.wikipedia.org/wiki/Aviation_accidents_and_incidents
INFO:rag_system:Successfully processed 1 documents from https://www.faa.gov/newsroom/statements/accident_incidents
INFO:rag_system:Successfully processed 1 documents from https://www.panish.law/aviation_accident_statistics.html
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://www.boeing.com/content/dam/boeing/boeingdotcom/company/about_bca/pdf/statsum.pdf
INFO:rag_system:Successfully processed 1 documents from https://www.bbc.com/news/topics/c2n5vpdv320t
INFO:vector_store:Starting to process 28728 documents
INFO:vector_store:Processing document batch 1 of 6
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/60 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▌                                                                                             | 1/60 [01:46<1:44:23, 106.16s/it]INFO:vector_store:Embedding progress: 1.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   3%|███▎                                                                                              | 2/60 [01:46<42:20, 43.80s/it]INFO:vector_store:Embedding progress: 3.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   5%|████▉                                                                                             | 3/60 [01:46<22:46, 23.97s/it]INFO:vector_store:Embedding progress: 5.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   7%|██████▌                                                                                           | 4/60 [01:46<13:35, 14.57s/it]INFO:vector_store:Embedding progress: 6.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|████████▏                                                                                         | 5/60 [01:47<08:40,  9.46s/it]INFO:vector_store:Embedding progress: 8.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▊                                                                                        | 6/60 [01:47<05:45,  6.40s/it]INFO:vector_store:Embedding progress: 10.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▍                                                                                      | 7/60 [01:47<03:53,  4.40s/it]INFO:vector_store:Embedding progress: 11.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  13%|█████████████                                                                                     | 8/60 [01:48<02:41,  3.11s/it]INFO:vector_store:Embedding progress: 13.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 15.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  17%|████████████████▏                                                                                | 10/60 [01:48<01:23,  1.68s/it]INFO:vector_store:Embedding progress: 16.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 18.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████▍                                                                             | 12/60 [02:32<07:58,  9.96s/it]INFO:vector_store:Embedding progress: 20.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████                                                                            | 13/60 [02:34<06:22,  8.14s/it]INFO:vector_store:Embedding progress: 21.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  23%|██████████████████████▋                                                                          | 14/60 [02:35<04:54,  6.40s/it]INFO:vector_store:Embedding progress: 23.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  25%|████████████████████████▎                                                                        | 15/60 [02:36<03:43,  4.97s/it]INFO:vector_store:Embedding progress: 25.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  27%|█████████████████████████▊                                                                       | 16/60 [02:37<02:49,  3.84s/it]INFO:vector_store:Embedding progress: 26.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▍                                                                     | 17/60 [02:37<02:03,  2.86s/it]INFO:vector_store:Embedding progress: 28.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|█████████████████████████████                                                                    | 18/60 [02:37<01:30,  2.15s/it]INFO:vector_store:Embedding progress: 30.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|██████████████████████████████▋                                                                  | 19/60 [02:38<01:04,  1.57s/it]INFO:vector_store:Embedding progress: 31.7%
INFO:vector_store:Embedding progress: 33.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 35.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  37%|███████████████████████████████████▌                                                             | 22/60 [02:38<00:28,  1.35it/s]INFO:vector_store:Embedding progress: 36.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|█████████████████████████████████████▏                                                           | 23/60 [03:24<06:19, 10.27s/it]INFO:vector_store:Embedding progress: 38.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▊                                                          | 24/60 [03:31<05:36,  9.36s/it]INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▍                                                        | 25/60 [03:34<04:34,  7.84s/it]INFO:vector_store:Embedding progress: 41.7%
INFO:vector_store:Embedding progress: 43.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  45%|███████████████████████████████████████████▋                                                     | 27/60 [03:36<02:43,  4.97s/it]INFO:vector_store:Embedding progress: 45.0%
INFO:vector_store:Embedding progress: 46.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▉                                                  | 29/60 [03:36<01:40,  3.24s/it]INFO:vector_store:Embedding progress: 48.3%
INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████                                               | 31/60 [03:36<01:02,  2.16s/it]INFO:vector_store:Embedding progress: 51.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  53%|███████████████████████████████████████████████████▋                                             | 32/60 [03:37<00:49,  1.78s/it]INFO:vector_store:Embedding progress: 53.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 55.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  57%|██████████████████████████████████████████████████████▉                                          | 34/60 [04:33<04:54, 11.33s/it]INFO:vector_store:Embedding progress: 56.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|████████████████████████████████████████████████████████▌                                        | 35/60 [04:38<04:08,  9.95s/it]INFO:vector_store:Embedding progress: 58.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 36/60 [04:43<03:35,  8.98s/it]INFO:vector_store:Embedding progress: 60.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|███████████████████████████████████████████████████████████▊                                     | 37/60 [04:45<02:45,  7.21s/it]INFO:vector_store:Embedding progress: 61.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  63%|█████████████████████████████████████████████████████████████▍                                   | 38/60 [04:47<02:08,  5.82s/it]INFO:vector_store:Embedding progress: 63.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|███████████████████████████████████████████████████████████████                                  | 39/60 [04:48<01:34,  4.52s/it]INFO:vector_store:Embedding progress: 65.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  67%|████████████████████████████████████████████████████████████████▋                                | 40/60 [04:49<01:10,  3.54s/it]INFO:vector_store:Embedding progress: 66.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|██████████████████████████████████████████████████████████████████▎                              | 41/60 [04:49<00:51,  2.71s/it]INFO:vector_store:Embedding progress: 68.3%
INFO:vector_store:Embedding progress: 70.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▌                           | 43/60 [04:50<00:27,  1.63s/it]INFO:vector_store:Embedding progress: 71.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  73%|███████████████████████████████████████████████████████████████████████▏                         | 44/60 [04:52<00:26,  1.66s/it]INFO:vector_store:Embedding progress: 73.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  75%|████████████████████████████████████████████████████████████████████████▊                        | 45/60 [05:39<03:19, 13.31s/it]INFO:vector_store:Embedding progress: 75.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  77%|██████████████████████████████████████████████████████████████████████████▎                      | 46/60 [05:45<02:38, 11.32s/it]INFO:vector_store:Embedding progress: 76.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|███████████████████████████████████████████████████████████████████████████▉                     | 47/60 [05:50<02:06,  9.76s/it]INFO:vector_store:Embedding progress: 78.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|█████████████████████████████████████████████████████████████████████████████▌                   | 48/60 [05:54<01:35,  7.96s/it]INFO:vector_store:Embedding progress: 80.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▏                 | 49/60 [06:05<01:39,  9.00s/it]INFO:vector_store:Embedding progress: 81.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  83%|████████████████████████████████████████████████████████████████████████████████▊                | 50/60 [06:06<01:04,  6.47s/it]INFO:vector_store:Embedding progress: 83.3%
Creating embeddings:  85%|██████████████████████████████████████████████████████████████████████████████████▍              | 51/60 [06:06<00:42,  4.74s/it]INFO:vector_store:Embedding progress: 85.0%
Creating embeddings:  87%|████████████████████████████████████████████████████████████████████████████████████             | 52/60 [06:09<00:33,  4.16s/it]INFO:vector_store:Embedding progress: 86.7%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▋           | 53/60 [06:09<00:21,  3.01s/it]INFO:vector_store:Embedding progress: 88.3%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▎         | 54/60 [06:10<00:14,  2.35s/it]INFO:vector_store:Embedding progress: 90.0%
Creating embeddings:  92%|████████████████████████████████████████████████████████████████████████████████████████▉        | 55/60 [06:11<00:09,  1.83s/it]INFO:vector_store:Embedding progress: 91.7%
Creating embeddings:  93%|██████████████████████████████████████████████████████████████████████████████████████████▌      | 56/60 [06:30<00:28,  7.05s/it]INFO:vector_store:Embedding progress: 93.3%
Creating embeddings:  95%|████████████████████████████████████████████████████████████████████████████████████████████▏    | 57/60 [06:31<00:15,  5.14s/it]INFO:vector_store:Embedding progress: 95.0%
Creating embeddings:  97%|█████████████████████████████████████████████████████████████████████████████████████████████▊   | 58/60 [06:32<00:07,  3.92s/it]INFO:vector_store:Embedding progress: 96.7%
Creating embeddings:  98%|███████████████████████████████████████████████████████████████████████████████████████████████▍ | 59/60 [06:33<00:02,  2.97s/it]INFO:vector_store:Embedding progress: 98.3%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 60/60 [06:33<00:00,  2.20s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 60/60 [06:33<00:00,  6.56s/it]
INFO:vector_store:Processed 1000 chunks so far
INFO:vector_store:Processed 2000 chunks so far
INFO:vector_store:Processed 3000 chunks so far
INFO:vector_store:Processed 4000 chunks so far
INFO:vector_store:Processed 5000 chunks so far
INFO:vector_store:Processed 5960 chunks so far
INFO:vector_store:Processing document batch 2 of 6
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/69 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   1%|█▍                                                                                             | 1/69 [02:29<2:49:25, 149.49s/it]INFO:vector_store:Embedding progress: 1.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   3%|██▊                                                                                             | 2/69 [02:35<1:13:00, 65.38s/it]INFO:vector_store:Embedding progress: 2.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|████▎                                                                                             | 3/69 [02:36<39:18, 35.73s/it]INFO:vector_store:Embedding progress: 4.3%
INFO:vector_store:Embedding progress: 5.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   7%|███████                                                                                           | 5/69 [02:36<16:34, 15.54s/it]INFO:vector_store:Embedding progress: 7.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 8.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:  10%|█████████▉                                                                                        | 7/69 [02:36<08:54,  8.63s/it]INFO:vector_store:Embedding progress: 10.1%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 11.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  13%|████████████▊                                                                                     | 9/69 [02:36<05:18,  5.30s/it]INFO:vector_store:Embedding progress: 13.0%
INFO:vector_store:Embedding progress: 14.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 15.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  17%|████████████████▊                                                                                | 12/69 [03:25<09:41, 10.20s/it]INFO:vector_store:Embedding progress: 17.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  19%|██████████████████▎                                                                              | 13/69 [03:48<11:43, 12.57s/it]INFO:vector_store:Embedding progress: 18.8%
INFO:vector_store:Embedding progress: 20.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████                                                                            | 15/69 [03:50<07:45,  8.62s/it]INFO:vector_store:Embedding progress: 21.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  23%|██████████████████████▍                                                                          | 16/69 [03:50<06:14,  7.07s/it]INFO:vector_store:Embedding progress: 23.2%
INFO:vector_store:Embedding progress: 24.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▎                                                                       | 18/69 [03:51<03:56,  4.63s/it]INFO:vector_store:Embedding progress: 26.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|██████████████████████████▋                                                                      | 19/69 [03:51<03:08,  3.77s/it]INFO:vector_store:Embedding progress: 27.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  29%|████████████████████████████                                                                     | 20/69 [03:51<02:25,  2.96s/it]INFO:vector_store:Embedding progress: 29.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|█████████████████████████████▌                                                                   | 21/69 [03:52<01:50,  2.30s/it]INFO:vector_store:Embedding progress: 30.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 31.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  33%|████████████████████████████████▎                                                                | 23/69 [03:57<01:49,  2.37s/it]INFO:vector_store:Embedding progress: 33.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  35%|█████████████████████████████████▋                                                               | 24/69 [04:48<10:09, 13.54s/it]INFO:vector_store:Embedding progress: 34.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|███████████████████████████████████▏                                                             | 25/69 [04:51<07:54, 10.79s/it]INFO:vector_store:Embedding progress: 36.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▌                                                            | 26/69 [04:55<06:28,  9.03s/it]INFO:vector_store:Embedding progress: 37.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  39%|█████████████████████████████████████▉                                                           | 27/69 [04:55<04:45,  6.79s/it]INFO:vector_store:Embedding progress: 39.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  41%|███████████████████████████████████████▎                                                         | 28/69 [05:18<07:43, 11.29s/it]INFO:vector_store:Embedding progress: 40.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▊                                                        | 29/69 [05:21<05:48,  8.72s/it]INFO:vector_store:Embedding progress: 42.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  43%|██████████████████████████████████████████▏                                                      | 30/69 [05:23<04:24,  6.78s/it]INFO:vector_store:Embedding progress: 43.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  45%|███████████████████████████████████████████▌                                                     | 31/69 [05:23<03:06,  4.90s/it]INFO:vector_store:Embedding progress: 44.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████▉                                                    | 32/69 [05:24<02:15,  3.67s/it]INFO:vector_store:Embedding progress: 46.4%
Creating embeddings:  48%|██████████████████████████████████████████████▍                                                  | 33/69 [05:24<01:34,  2.62s/it]INFO:vector_store:Embedding progress: 47.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  49%|███████████████████████████████████████████████▊                                                 | 34/69 [05:25<01:18,  2.24s/it]INFO:vector_store:Embedding progress: 49.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  51%|█████████████████████████████████████████████████▏                                               | 35/69 [06:02<07:03, 12.44s/it]INFO:vector_store:Embedding progress: 50.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▌                                              | 36/69 [06:02<04:55,  8.95s/it]INFO:vector_store:Embedding progress: 52.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|████████████████████████████████████████████████████                                             | 37/69 [06:03<03:29,  6.54s/it]INFO:vector_store:Embedding progress: 53.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  55%|█████████████████████████████████████████████████████▍                                           | 38/69 [06:27<05:58, 11.55s/it]INFO:vector_store:Embedding progress: 55.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  57%|██████████████████████████████████████████████████████▊                                          | 39/69 [06:34<05:11, 10.39s/it]INFO:vector_store:Embedding progress: 56.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|████████████████████████████████████████████████████████▏                                        | 40/69 [06:37<03:55,  8.13s/it]INFO:vector_store:Embedding progress: 58.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  59%|█████████████████████████████████████████████████████████▋                                       | 41/69 [06:37<02:40,  5.74s/it]INFO:vector_store:Embedding progress: 59.4%
INFO:vector_store:Embedding progress: 60.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|████████████████████████████████████████████████████████████▍                                    | 43/69 [06:37<01:21,  3.13s/it]INFO:vector_store:Embedding progress: 62.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|█████████████████████████████████████████████████████████████▊                                   | 44/69 [06:38<01:01,  2.45s/it]INFO:vector_store:Embedding progress: 63.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|███████████████████████████████████████████████████████████████▎                                 | 45/69 [06:53<02:20,  5.87s/it]INFO:vector_store:Embedding progress: 65.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  67%|████████████████████████████████████████████████████████████████▋                                | 46/69 [07:13<03:42,  9.65s/it]INFO:vector_store:Embedding progress: 66.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|██████████████████████████████████████████████████████████████████                               | 47/69 [07:15<02:43,  7.45s/it]INFO:vector_store:Embedding progress: 68.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|███████████████████████████████████████████████████████████████████▍                             | 48/69 [07:18<02:08,  6.13s/it]INFO:vector_store:Embedding progress: 69.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  71%|████████████████████████████████████████████████████████████████████▉                            | 49/69 [07:40<03:35, 10.75s/it]INFO:vector_store:Embedding progress: 71.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|██████████████████████████████████████████████████████████████████████▎                          | 50/69 [07:53<03:40, 11.62s/it]INFO:vector_store:Embedding progress: 72.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|███████████████████████████████████████████████████████████████████████▋                         | 51/69 [07:55<02:35,  8.63s/it]INFO:vector_store:Embedding progress: 73.9%
INFO:vector_store:Embedding progress: 75.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  77%|██████████████████████████████████████████████████████████████████████████▌                      | 53/69 [07:55<01:15,  4.72s/it]INFO:vector_store:Embedding progress: 76.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|███████████████████████████████████████████████████████████████████████████▉                     | 54/69 [07:55<00:54,  3.61s/it]INFO:vector_store:Embedding progress: 78.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|█████████████████████████████████████████████████████████████████████████████▎                   | 55/69 [07:56<00:41,  2.94s/it]INFO:vector_store:Embedding progress: 79.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  81%|██████████████████████████████████████████████████████████████████████████████▋                  | 56/69 [08:14<01:29,  6.91s/it]INFO:vector_store:Embedding progress: 81.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  83%|████████████████████████████████████████████████████████████████████████████████▏                | 57/69 [08:25<01:35,  7.96s/it]INFO:vector_store:Embedding progress: 82.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▌               | 58/69 [08:26<01:05,  5.97s/it]INFO:vector_store:Embedding progress: 84.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  86%|██████████████████████████████████████████████████████████████████████████████████▉              | 59/69 [08:30<00:54,  5.48s/it]INFO:vector_store:Embedding progress: 85.5%
Creating embeddings:  87%|████████████████████████████████████████████████████████████████████████████████████▎            | 60/69 [08:46<01:18,  8.69s/it]INFO:vector_store:Embedding progress: 87.0%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▊           | 61/69 [09:04<01:29, 11.21s/it]INFO:vector_store:Embedding progress: 88.4%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▏         | 62/69 [09:05<00:57,  8.22s/it]INFO:vector_store:Embedding progress: 89.9%
Creating embeddings:  91%|████████████████████████████████████████████████████████████████████████████████████████▌        | 63/69 [09:06<00:36,  6.03s/it]INFO:vector_store:Embedding progress: 91.3%
INFO:vector_store:Embedding progress: 92.8%
Creating embeddings:  94%|███████████████████████████████████████████████████████████████████████████████████████████▍     | 65/69 [09:06<00:13,  3.46s/it]INFO:vector_store:Embedding progress: 94.2%
Creating embeddings:  96%|████████████████████████████████████████████████████████████████████████████████████████████▊    | 66/69 [09:07<00:08,  2.72s/it]INFO:vector_store:Embedding progress: 95.7%
Creating embeddings:  97%|██████████████████████████████████████████████████████████████████████████████████████████████▏  | 67/69 [09:07<00:04,  2.09s/it]INFO:vector_store:Embedding progress: 97.1%
Creating embeddings:  99%|███████████████████████████████████████████████████████████████████████████████████████████████▌ | 68/69 [09:10<00:02,  2.31s/it]INFO:vector_store:Embedding progress: 98.6%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 69/69 [09:12<00:00,  2.15s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 69/69 [09:12<00:00,  8.00s/it]
INFO:vector_store:Processed 6960 chunks so far
INFO:vector_store:Processed 7960 chunks so far
INFO:vector_store:Processed 8960 chunks so far
INFO:vector_store:Processed 9960 chunks so far
INFO:vector_store:Processed 10960 chunks so far
INFO:vector_store:Processed 11960 chunks so far
INFO:vector_store:Processed 12808 chunks so far
INFO:vector_store:Processing document batch 3 of 6
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/75 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   1%|█▎                                                                                             | 1/75 [02:11<2:42:16, 131.58s/it]INFO:vector_store:Embedding progress: 1.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   3%|██▌                                                                                             | 2/75 [02:15<1:08:47, 56.54s/it]INFO:vector_store:Embedding progress: 2.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                              | 3/75 [02:18<38:17, 31.91s/it]INFO:vector_store:Embedding progress: 4.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   5%|█████▏                                                                                            | 4/75 [02:24<25:51, 21.86s/it]INFO:vector_store:Embedding progress: 5.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   7%|██████▌                                                                                           | 5/75 [02:26<16:58, 14.55s/it]INFO:vector_store:Embedding progress: 6.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▊                                                                                          | 6/75 [02:26<11:14,  9.77s/it]INFO:vector_store:Embedding progress: 8.0%
INFO:vector_store:Embedding progress: 9.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  11%|██████████▍                                                                                       | 8/75 [02:28<06:01,  5.40s/it]INFO:vector_store:Embedding progress: 10.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▊                                                                                      | 9/75 [02:30<05:02,  4.58s/it]INFO:vector_store:Embedding progress: 12.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  13%|████████████▉                                                                                    | 10/75 [02:49<09:08,  8.44s/it]INFO:vector_store:Embedding progress: 13.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 14.7%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▌                                                                                 | 12/75 [03:07<09:02,  8.61s/it]INFO:vector_store:Embedding progress: 16.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  17%|████████████████▊                                                                                | 13/75 [03:07<06:49,  6.60s/it]INFO:vector_store:Embedding progress: 17.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  19%|██████████████████                                                                               | 14/75 [03:07<05:06,  5.03s/it]INFO:vector_store:Embedding progress: 18.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████▍                                                                             | 15/75 [03:10<04:19,  4.32s/it]INFO:vector_store:Embedding progress: 20.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
ERROR:vector_store:Error in parallel processing: (ProtocolError('Connection aborted.', RemoteDisconnected('Remote end closed connection without response')), '(Request ID: bcb16ad1-3ea2-4644-806f-455fadd7e6ea)')
Creating embeddings:  21%|████████████████████▋                                                                            | 16/75 [03:11<03:20,  3.40s/it]INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 21.3%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  23%|█████████████████████▉                                                                           | 17/75 [03:30<07:32,  7.80s/it]INFO:vector_store:Embedding progress: 22.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▎                                                                         | 18/75 [03:30<05:18,  5.59s/it]INFO:vector_store:Embedding progress: 24.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  25%|████████████████████████▌                                                                        | 19/75 [04:06<13:29, 14.46s/it]INFO:vector_store:Embedding progress: 25.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  27%|█████████████████████████▊                                                                       | 20/75 [04:15<11:48, 12.89s/it]INFO:vector_store:Embedding progress: 26.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▏                                                                     | 21/75 [04:22<09:56, 11.06s/it]INFO:vector_store:Embedding progress: 28.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  29%|████████████████████████████▍                                                                    | 22/75 [04:25<07:38,  8.65s/it]INFO:vector_store:Embedding progress: 29.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  31%|█████████████████████████████▋                                                                   | 23/75 [04:25<05:20,  6.17s/it]INFO:vector_store:Embedding progress: 30.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|███████████████████████████████                                                                  | 24/75 [04:25<03:42,  4.37s/it]INFO:vector_store:Embedding progress: 32.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  33%|████████████████████████████████▎                                                                | 25/75 [04:25<02:35,  3.11s/it]INFO:vector_store:Embedding progress: 33.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  35%|█████████████████████████████████▋                                                               | 26/75 [04:33<03:42,  4.55s/it]INFO:vector_store:Embedding progress: 34.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|██████████████████████████████████▉                                                              | 27/75 [04:35<02:53,  3.62s/it]INFO:vector_store:Embedding progress: 36.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  37%|████████████████████████████████████▏                                                            | 28/75 [04:38<02:47,  3.57s/it]INFO:vector_store:Embedding progress: 37.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  39%|█████████████████████████████████████▌                                                           | 29/75 [04:40<02:24,  3.14s/it]INFO:vector_store:Embedding progress: 38.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▊                                                          | 30/75 [05:16<09:37, 12.83s/it]INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  41%|████████████████████████████████████████                                                         | 31/75 [05:23<08:16, 11.29s/it]INFO:vector_store:Embedding progress: 41.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  43%|█████████████████████████████████████████▍                                                       | 32/75 [05:32<07:28, 10.42s/it]INFO:vector_store:Embedding progress: 42.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|██████████████████████████████████████████▋                                                      | 33/75 [05:42<07:18, 10.45s/it]INFO:vector_store:Embedding progress: 44.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  45%|███████████████████████████████████████████▉                                                     | 34/75 [05:43<05:09,  7.54s/it]INFO:vector_store:Embedding progress: 45.3%
Creating embeddings:  47%|█████████████████████████████████████████████▎                                                   | 35/75 [05:43<03:32,  5.32s/it]INFO:vector_store:Embedding progress: 46.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 48.0%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  49%|███████████████████████████████████████████████▊                                                 | 37/75 [05:45<02:06,  3.34s/it]INFO:vector_store:Embedding progress: 49.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  51%|█████████████████████████████████████████████████▏                                               | 38/75 [05:47<01:52,  3.05s/it]INFO:vector_store:Embedding progress: 50.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▍                                              | 39/75 [05:48<01:29,  2.48s/it]INFO:vector_store:Embedding progress: 52.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  53%|███████████████████████████████████████████████████▋                                             | 40/75 [05:49<01:08,  1.97s/it]INFO:vector_store:Embedding progress: 53.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  55%|█████████████████████████████████████████████████████                                            | 41/75 [06:17<05:13,  9.21s/it]INFO:vector_store:Embedding progress: 54.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|██████████████████████████████████████████████████████▎                                          | 42/75 [06:29<05:33, 10.11s/it]INFO:vector_store:Embedding progress: 56.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  57%|███████████████████████████████████████████████████████▌                                         | 43/75 [06:39<05:22, 10.09s/it]INFO:vector_store:Embedding progress: 57.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  59%|████████████████████████████████████████████████████████▉                                        | 44/75 [07:02<07:12, 13.96s/it]INFO:vector_store:Embedding progress: 58.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 45/75 [07:03<04:58,  9.95s/it]INFO:vector_store:Embedding progress: 60.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  61%|███████████████████████████████████████████████████████████▍                                     | 46/75 [07:03<03:25,  7.09s/it]INFO:vector_store:Embedding progress: 61.3%
INFO:vector_store:Embedding progress: 62.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|██████████████████████████████████████████████████████████████                                   | 48/75 [07:04<01:47,  3.97s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|███████████████████████████████████████████████████████████████▎                                 | 49/75 [07:05<01:29,  3.43s/it]INFO:vector_store:Embedding progress: 65.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  67%|████████████████████████████████████████████████████████████████▋                                | 50/75 [07:07<01:12,  2.89s/it]INFO:vector_store:Embedding progress: 66.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▉                               | 51/75 [07:08<01:01,  2.57s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  69%|███████████████████████████████████████████████████████████████████▎                             | 52/75 [07:15<01:27,  3.79s/it]INFO:vector_store:Embedding progress: 69.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  71%|████████████████████████████████████████████████████████████████████▌                            | 53/75 [07:22<01:41,  4.62s/it]INFO:vector_store:Embedding progress: 70.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▊                           | 54/75 [07:33<02:12,  6.32s/it]INFO:vector_store:Embedding progress: 72.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  73%|███████████████████████████████████████████████████████████████████████▏                         | 55/75 [08:27<06:46, 20.30s/it]INFO:vector_store:Embedding progress: 73.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  75%|████████████████████████████████████████████████████████████████████████▍                        | 56/75 [08:27<04:36, 14.55s/it]INFO:vector_store:Embedding progress: 74.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|█████████████████████████████████████████████████████████████████████████▋                       | 57/75 [08:28<03:09, 10.51s/it]INFO:vector_store:Embedding progress: 76.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  77%|███████████████████████████████████████████████████████████████████████████                      | 58/75 [08:29<02:07,  7.53s/it]INFO:vector_store:Embedding progress: 77.3%
INFO:vector_store:Embedding progress: 78.7%
INFO:vector_store:Embedding progress: 80.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  81%|██████████████████████████████████████████████████████████████████████████████▉                  | 61/75 [08:29<00:46,  3.35s/it]INFO:vector_store:Embedding progress: 81.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  83%|████████████████████████████████████████████████████████████████████████████████▏                | 62/75 [08:29<00:34,  2.68s/it]INFO:vector_store:Embedding progress: 82.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▍               | 63/75 [08:31<00:28,  2.37s/it]INFO:vector_store:Embedding progress: 84.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  85%|██████████████████████████████████████████████████████████████████████████████████▊              | 64/75 [08:32<00:24,  2.24s/it]INFO:vector_store:Embedding progress: 85.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  87%|████████████████████████████████████████████████████████████████████████████████████             | 65/75 [08:33<00:18,  1.86s/it]INFO:vector_store:Embedding progress: 86.7%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▎           | 66/75 [08:46<00:44,  4.92s/it]INFO:vector_store:Embedding progress: 88.0%
Creating embeddings:  89%|██████████████████████████████████████████████████████████████████████████████████████▋          | 67/75 [09:06<01:12,  9.09s/it]INFO:vector_store:Embedding progress: 89.3%
Creating embeddings:  91%|███████████████████████████████████████████████████████████████████████████████████████▉         | 68/75 [09:36<01:45, 15.03s/it]INFO:vector_store:Embedding progress: 90.7%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▏       | 69/75 [09:37<01:06, 11.07s/it]INFO:vector_store:Embedding progress: 92.0%
Creating embeddings:  93%|██████████████████████████████████████████████████████████████████████████████████████████▌      | 70/75 [09:38<00:40,  8.06s/it]INFO:vector_store:Embedding progress: 93.3%
Creating embeddings:  95%|███████████████████████████████████████████████████████████████████████████████████████████▊     | 71/75 [09:38<00:22,  5.71s/it]INFO:vector_store:Embedding progress: 94.7%
INFO:vector_store:Embedding progress: 96.0%
INFO:vector_store:Embedding progress: 97.3%
INFO:vector_store:Embedding progress: 98.7%
INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 75/75 [09:38<00:00,  7.72s/it]
INFO:vector_store:Processed 13808 chunks so far
INFO:vector_store:Processed 14808 chunks so far
INFO:vector_store:Processed 15808 chunks so far
INFO:vector_store:Processed 16808 chunks so far
INFO:vector_store:Processed 17808 chunks so far
INFO:vector_store:Processed 18808 chunks so far
INFO:vector_store:Processed 19808 chunks so far
ERROR:vector_store:Error adding chunk batch to vector store: Number of embeddings 329 must match number of ids 429
INFO:vector_store:Processing document batch 4 of 6
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/71 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   1%|█▎                                                                                             | 1/71 [02:32<2:57:45, 152.37s/it]INFO:vector_store:Embedding progress: 1.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   3%|██▋                                                                                             | 2/71 [02:33<1:12:49, 63.32s/it]INFO:vector_store:Embedding progress: 2.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|████▏                                                                                             | 3/71 [02:36<40:51, 36.05s/it]INFO:vector_store:Embedding progress: 4.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▌                                                                                            | 4/71 [02:38<25:05, 22.47s/it]INFO:vector_store:Embedding progress: 5.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   7%|██████▉                                                                                           | 5/71 [02:38<15:50, 14.40s/it]INFO:vector_store:Embedding progress: 7.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|████████▎                                                                                         | 6/71 [02:39<10:33,  9.75s/it]INFO:vector_store:Embedding progress: 8.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▋                                                                                        | 7/71 [02:39<07:08,  6.70s/it]INFO:vector_store:Embedding progress: 9.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  11%|███████████                                                                                       | 8/71 [02:40<04:52,  4.64s/it]INFO:vector_store:Embedding progress: 11.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  13%|████████████▍                                                                                     | 9/71 [02:40<03:26,  3.33s/it]INFO:vector_store:Embedding progress: 12.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▋                                                                                   | 10/71 [02:40<02:22,  2.33s/it]INFO:vector_store:Embedding progress: 14.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  15%|███████████████                                                                                  | 11/71 [02:41<01:57,  1.96s/it]INFO:vector_store:Embedding progress: 15.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  17%|████████████████▍                                                                                | 12/71 [03:41<19:10, 19.50s/it]INFO:vector_store:Embedding progress: 16.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▊                                                                               | 13/71 [03:42<13:22, 13.83s/it]INFO:vector_store:Embedding progress: 18.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████▏                                                                             | 14/71 [03:49<11:22, 11.97s/it]INFO:vector_store:Embedding progress: 19.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  21%|████████████████████▍                                                                            | 15/71 [03:50<07:58,  8.54s/it]INFO:vector_store:Embedding progress: 21.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  23%|█████████████████████▊                                                                           | 16/71 [03:52<06:06,  6.66s/it]INFO:vector_store:Embedding progress: 22.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▏                                                                         | 17/71 [03:53<04:26,  4.94s/it]INFO:vector_store:Embedding progress: 23.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  25%|████████████████████████▌                                                                        | 18/71 [03:54<03:22,  3.82s/it]INFO:vector_store:Embedding progress: 25.4%
Creating embeddings:  27%|█████████████████████████▉                                                                       | 19/71 [03:54<02:20,  2.71s/it]INFO:vector_store:Embedding progress: 26.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▎                                                                     | 20/71 [03:55<01:42,  2.02s/it]INFO:vector_store:Embedding progress: 28.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|████████████████████████████▋                                                                    | 21/71 [03:56<01:21,  1.63s/it]INFO:vector_store:Embedding progress: 29.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  31%|██████████████████████████████                                                                   | 22/71 [03:57<01:11,  1.45s/it]INFO:vector_store:Embedding progress: 31.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|███████████████████████████████▍                                                                 | 23/71 [04:51<13:58, 17.47s/it]INFO:vector_store:Embedding progress: 32.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|████████████████████████████████▊                                                                | 24/71 [04:53<09:50, 12.56s/it]INFO:vector_store:Embedding progress: 33.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  35%|██████████████████████████████████▏                                                              | 25/71 [04:59<08:18, 10.84s/it]INFO:vector_store:Embedding progress: 35.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  37%|███████████████████████████████████▌                                                             | 26/71 [05:02<06:22,  8.49s/it]INFO:vector_store:Embedding progress: 36.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▉                                                            | 27/71 [05:05<04:58,  6.78s/it]INFO:vector_store:Embedding progress: 38.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  39%|██████████████████████████████████████▎                                                          | 28/71 [05:08<03:56,  5.50s/it]INFO:vector_store:Embedding progress: 39.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  41%|███████████████████████████████████████▌                                                         | 29/71 [05:08<02:46,  3.97s/it]INFO:vector_store:Embedding progress: 40.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▉                                                        | 30/71 [05:09<02:01,  2.97s/it]INFO:vector_store:Embedding progress: 42.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|██████████████████████████████████████████▎                                                      | 31/71 [05:09<01:29,  2.25s/it]INFO:vector_store:Embedding progress: 43.7%
INFO:vector_store:Embedding progress: 45.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|█████████████████████████████████████████████                                                    | 33/71 [05:10<00:52,  1.39s/it]INFO:vector_store:Embedding progress: 46.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▍                                                  | 34/71 [06:02<08:30, 13.81s/it]INFO:vector_store:Embedding progress: 47.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  49%|███████████████████████████████████████████████▊                                                 | 35/71 [06:05<06:36, 11.02s/it]INFO:vector_store:Embedding progress: 49.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  51%|█████████████████████████████████████████████████▏                                               | 36/71 [06:18<06:45, 11.57s/it]INFO:vector_store:Embedding progress: 50.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████▌                                              | 37/71 [06:19<04:54,  8.65s/it]INFO:vector_store:Embedding progress: 52.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|███████████████████████████████████████████████████▉                                             | 38/71 [06:19<03:26,  6.27s/it]INFO:vector_store:Embedding progress: 53.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  55%|█████████████████████████████████████████████████████▎                                           | 39/71 [06:23<02:54,  5.46s/it]INFO:vector_store:Embedding progress: 54.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|██████████████████████████████████████████████████████▋                                          | 40/71 [06:23<02:04,  4.00s/it]INFO:vector_store:Embedding progress: 56.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|████████████████████████████████████████████████████████                                         | 41/71 [06:25<01:37,  3.24s/it]INFO:vector_store:Embedding progress: 57.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  59%|█████████████████████████████████████████████████████████▍                                       | 42/71 [06:25<01:09,  2.41s/it]INFO:vector_store:Embedding progress: 59.2%
INFO:vector_store:Embedding progress: 60.6%
INFO:vector_store:Embedding progress: 62.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  63%|█████████████████████████████████████████████████████████████▍                                   | 45/71 [07:16<04:34, 10.55s/it]INFO:vector_store:Embedding progress: 63.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|██████████████████████████████████████████████████████████████▊                                  | 46/71 [07:17<03:33,  8.56s/it]INFO:vector_store:Embedding progress: 64.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|████████████████████████████████████████████████████████████████▏                                | 47/71 [07:30<03:50,  9.60s/it]INFO:vector_store:Embedding progress: 66.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|█████████████████████████████████████████████████████████████████▌                               | 48/71 [07:33<03:02,  7.92s/it]INFO:vector_store:Embedding progress: 67.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  69%|██████████████████████████████████████████████████████████████████▉                              | 49/71 [07:34<02:16,  6.20s/it]INFO:vector_store:Embedding progress: 69.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|████████████████████████████████████████████████████████████████████▎                            | 50/71 [07:38<01:58,  5.63s/it]INFO:vector_store:Embedding progress: 70.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▋                           | 51/71 [07:39<01:26,  4.34s/it]INFO:vector_store:Embedding progress: 71.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  73%|███████████████████████████████████████████████████████████████████████                          | 52/71 [07:40<01:02,  3.29s/it]INFO:vector_store:Embedding progress: 73.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  75%|████████████████████████████████████████████████████████████████████████▍                        | 53/71 [07:42<00:51,  2.87s/it]INFO:vector_store:Embedding progress: 74.6%
INFO:vector_store:Embedding progress: 76.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  77%|███████████████████████████████████████████████████████████████████████████▏                     | 55/71 [07:43<00:29,  1.85s/it]INFO:vector_store:Embedding progress: 77.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  79%|████████████████████████████████████████████████████████████████████████████▌                    | 56/71 [08:25<02:53, 11.57s/it]INFO:vector_store:Embedding progress: 78.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|█████████████████████████████████████████████████████████████████████████████▊                   | 57/71 [08:31<02:22, 10.17s/it]INFO:vector_store:Embedding progress: 80.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▏                 | 58/71 [08:46<02:28, 11.39s/it]INFO:vector_store:Embedding progress: 81.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  83%|████████████████████████████████████████████████████████████████████████████████▌                | 59/71 [08:47<01:43,  8.60s/it]INFO:vector_store:Embedding progress: 83.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:  85%|█████████████████████████████████████████████████████████████████████████████████▉               | 60/71 [08:47<01:08,  6.21s/it]INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 84.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▎             | 61/71 [08:51<00:56,  5.67s/it]INFO:vector_store:Embedding progress: 85.9%
Creating embeddings:  87%|████████████████████████████████████████████████████████████████████████████████████▋            | 62/71 [08:54<00:42,  4.74s/it]INFO:vector_store:Embedding progress: 87.3%
Creating embeddings:  89%|██████████████████████████████████████████████████████████████████████████████████████           | 63/71 [08:54<00:27,  3.43s/it]INFO:vector_store:Embedding progress: 88.7%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▍         | 64/71 [08:55<00:18,  2.58s/it]INFO:vector_store:Embedding progress: 90.1%
Creating embeddings:  92%|████████████████████████████████████████████████████████████████████████████████████████▊        | 65/71 [08:58<00:15,  2.62s/it]INFO:vector_store:Embedding progress: 91.5%
Creating embeddings:  93%|██████████████████████████████████████████████████████████████████████████████████████████▏      | 66/71 [08:59<00:11,  2.20s/it]INFO:vector_store:Embedding progress: 93.0%
Creating embeddings:  94%|███████████████████████████████████████████████████████████████████████████████████████████▌     | 67/71 [09:18<00:29,  7.38s/it]INFO:vector_store:Embedding progress: 94.4%
Creating embeddings:  96%|████████████████████████████████████████████████████████████████████████████████████████████▉    | 68/71 [09:20<00:17,  5.70s/it]INFO:vector_store:Embedding progress: 95.8%
Creating embeddings:  97%|██████████████████████████████████████████████████████████████████████████████████████████████▎  | 69/71 [09:24<00:10,  5.18s/it]INFO:vector_store:Embedding progress: 97.2%
Creating embeddings:  99%|███████████████████████████████████████████████████████████████████████████████████████████████▋ | 70/71 [09:24<00:03,  3.69s/it]INFO:vector_store:Embedding progress: 98.6%
INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 71/71 [09:24<00:00,  7.95s/it]
INFO:vector_store:Processed 20808 chunks so far
INFO:vector_store:Processed 21808 chunks so far
INFO:vector_store:Processed 22808 chunks so far
INFO:vector_store:Processed 23808 chunks so far
INFO:vector_store:Processed 24808 chunks so far
INFO:vector_store:Processed 25808 chunks so far
INFO:vector_store:Processed 26808 chunks so far
INFO:vector_store:Processed 26907 chunks so far
INFO:vector_store:Processing document batch 5 of 6
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/92 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   1%|█                                                                                              | 1/92 [02:28<3:45:09, 148.46s/it]INFO:vector_store:Embedding progress: 1.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|██                                                                                              | 2/92 [02:29<1:32:25, 61.62s/it]INFO:vector_store:Embedding progress: 2.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   3%|███▏                                                                                              | 3/92 [02:30<50:48, 34.25s/it]INFO:vector_store:Embedding progress: 3.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|████▎                                                                                             | 4/92 [02:32<31:01, 21.15s/it]INFO:vector_store:Embedding progress: 4.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   5%|█████▎                                                                                            | 5/92 [02:32<19:55, 13.74s/it]INFO:vector_store:Embedding progress: 5.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   7%|██████▍                                                                                           | 6/92 [02:33<13:12,  9.21s/it]INFO:vector_store:Embedding progress: 6.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▍                                                                                          | 7/92 [02:33<08:57,  6.32s/it]INFO:vector_store:Embedding progress: 7.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 8.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▌                                                                                        | 9/92 [02:33<04:40,  3.38s/it]INFO:vector_store:Embedding progress: 9.8%
INFO:vector_store:Embedding progress: 10.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▌                                                                                     | 11/92 [02:34<02:46,  2.05s/it]INFO:vector_store:Embedding progress: 12.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  13%|████████████▋                                                                                    | 12/92 [03:39<21:40, 16.26s/it]INFO:vector_store:Embedding progress: 13.0%
INFO:vector_store:Embedding progress: 14.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  15%|██████████████▊                                                                                  | 14/92 [03:41<13:24, 10.31s/it]INFO:vector_store:Embedding progress: 15.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▊                                                                                 | 15/92 [03:46<11:50,  9.22s/it]INFO:vector_store:Embedding progress: 16.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  17%|████████████████▊                                                                                | 16/92 [03:49<09:38,  7.61s/it]INFO:vector_store:Embedding progress: 17.4%
Creating embeddings:  18%|█████████████████▉                                                                               | 17/92 [03:49<07:08,  5.71s/it]INFO:vector_store:Embedding progress: 18.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 19.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  21%|████████████████████                                                                             | 19/92 [03:49<04:13,  3.47s/it]INFO:vector_store:Embedding progress: 20.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████                                                                            | 20/92 [03:50<03:19,  2.76s/it]INFO:vector_store:Embedding progress: 21.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  23%|██████████████████████▏                                                                          | 21/92 [03:50<02:30,  2.13s/it]INFO:vector_store:Embedding progress: 22.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▏                                                                         | 22/92 [03:51<02:08,  1.84s/it]INFO:vector_store:Embedding progress: 23.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  25%|████████████████████████▎                                                                        | 23/92 [04:49<19:36, 17.05s/it]INFO:vector_store:Embedding progress: 25.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|█████████████████████████▎                                                                       | 24/92 [04:49<14:05, 12.43s/it]INFO:vector_store:Embedding progress: 26.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  27%|██████████████████████████▎                                                                      | 25/92 [04:54<11:30, 10.30s/it]INFO:vector_store:Embedding progress: 27.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████▍                                                                     | 26/92 [04:59<09:39,  8.78s/it]INFO:vector_store:Embedding progress: 28.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  29%|████████████████████████████▍                                                                    | 27/92 [05:04<08:16,  7.64s/it]INFO:vector_store:Embedding progress: 29.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|█████████████████████████████▌                                                                   | 28/92 [05:05<05:49,  5.47s/it]INFO:vector_store:Embedding progress: 30.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|██████████████████████████████▌                                                                  | 29/92 [05:05<04:05,  3.90s/it]INFO:vector_store:Embedding progress: 31.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  33%|███████████████████████████████▋                                                                 | 30/92 [05:06<03:10,  3.07s/it]INFO:vector_store:Embedding progress: 32.6%
INFO:vector_store:Embedding progress: 33.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  35%|█████████████████████████████████▋                                                               | 32/92 [05:08<02:06,  2.11s/it]INFO:vector_store:Embedding progress: 34.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|██████████████████████████████████▊                                                              | 33/92 [05:08<01:37,  1.65s/it]INFO:vector_store:Embedding progress: 35.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  37%|███████████████████████████████████▊                                                             | 34/92 [05:59<13:56, 14.42s/it]INFO:vector_store:Embedding progress: 37.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▉                                                            | 35/92 [05:59<10:07, 10.66s/it]INFO:vector_store:Embedding progress: 38.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  39%|█████████████████████████████████████▉                                                           | 36/92 [06:09<09:35, 10.27s/it]INFO:vector_store:Embedding progress: 39.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|███████████████████████████████████████                                                          | 37/92 [06:11<07:21,  8.02s/it]INFO:vector_store:Embedding progress: 40.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  41%|████████████████████████████████████████                                                         | 38/92 [06:18<06:54,  7.67s/it]INFO:vector_store:Embedding progress: 41.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|█████████████████████████████████████████                                                        | 39/92 [06:19<05:10,  5.87s/it]INFO:vector_store:Embedding progress: 42.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  43%|██████████████████████████████████████████▏                                                      | 40/92 [06:20<03:47,  4.37s/it]INFO:vector_store:Embedding progress: 43.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  45%|███████████████████████████████████████████▏                                                     | 41/92 [06:21<02:48,  3.31s/it]INFO:vector_store:Embedding progress: 44.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████▎                                                    | 42/92 [06:22<02:14,  2.69s/it]INFO:vector_store:Embedding progress: 45.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  47%|█████████████████████████████████████████████▎                                                   | 43/92 [06:23<01:46,  2.16s/it]INFO:vector_store:Embedding progress: 46.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▍                                                  | 44/92 [06:24<01:26,  1.80s/it]INFO:vector_store:Embedding progress: 47.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  49%|███████████████████████████████████████████████▍                                                 | 45/92 [07:13<12:23, 15.81s/it]INFO:vector_store:Embedding progress: 48.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 46/92 [07:15<09:02, 11.79s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  51%|█████████████████████████████████████████████████▌                                               | 47/92 [07:25<08:22, 11.17s/it]INFO:vector_store:Embedding progress: 51.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:  52%|██████████████████████████████████████████████████▌                                              | 48/92 [07:25<05:45,  7.86s/it]INFO:vector_store:Embedding progress: 52.2%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  53%|███████████████████████████████████████████████████▋                                             | 49/92 [07:33<05:42,  7.96s/it]INFO:vector_store:Embedding progress: 53.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|████████████████████████████████████████████████████▋                                            | 50/92 [07:35<04:25,  6.33s/it]INFO:vector_store:Embedding progress: 54.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  55%|█████████████████████████████████████████████████████▊                                           | 51/92 [07:38<03:29,  5.10s/it]INFO:vector_store:Embedding progress: 55.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  57%|██████████████████████████████████████████████████████▊                                          | 52/92 [07:39<02:34,  3.86s/it]INFO:vector_store:Embedding progress: 56.5%
Creating embeddings:  58%|███████████████████████████████████████████████████████▉                                         | 53/92 [07:39<01:46,  2.74s/it]INFO:vector_store:Embedding progress: 57.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  59%|████████████████████████████████████████████████████████▉                                        | 54/92 [07:40<01:32,  2.43s/it]INFO:vector_store:Embedding progress: 58.7%
INFO:vector_store:Embedding progress: 59.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  61%|███████████████████████████████████████████████████████████                                      | 56/92 [08:25<06:53, 11.50s/it]INFO:vector_store:Embedding progress: 60.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|████████████████████████████████████████████████████████████                                     | 57/92 [08:29<05:44,  9.84s/it]INFO:vector_store:Embedding progress: 62.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  63%|█████████████████████████████████████████████████████████████▏                                   | 58/92 [08:37<05:10,  9.14s/it]INFO:vector_store:Embedding progress: 63.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|██████████████████████████████████████████████████████████████▏                                  | 59/92 [08:40<04:09,  7.56s/it]INFO:vector_store:Embedding progress: 64.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|███████████████████████████████████████████████████████████████▎                                 | 60/92 [08:48<04:02,  7.58s/it]INFO:vector_store:Embedding progress: 65.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|████████████████████████████████████████████████████████████████▎                                | 61/92 [08:54<03:41,  7.14s/it]INFO:vector_store:Embedding progress: 66.3%
INFO:vector_store:Embedding progress: 67.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|██████████████████████████████████████████████████████████████████▍                              | 63/92 [08:54<01:57,  4.05s/it]INFO:vector_store:Embedding progress: 68.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|███████████████████████████████████████████████████████████████████▍                             | 64/92 [08:54<01:27,  3.13s/it]INFO:vector_store:Embedding progress: 69.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  71%|████████████████████████████████████████████████████████████████████▌                            | 65/92 [08:56<01:17,  2.85s/it]INFO:vector_store:Embedding progress: 70.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▌                           | 66/92 [08:57<00:56,  2.19s/it]INFO:vector_store:Embedding progress: 71.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  73%|██████████████████████████████████████████████████████████████████████▋                          | 67/92 [09:41<05:49, 13.96s/it]INFO:vector_store:Embedding progress: 72.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|███████████████████████████████████████████████████████████████████████▋                         | 68/92 [09:48<04:42, 11.78s/it]INFO:vector_store:Embedding progress: 73.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  75%|████████████████████████████████████████████████████████████████████████▊                        | 69/92 [09:51<03:33,  9.28s/it]INFO:vector_store:Embedding progress: 75.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|█████████████████████████████████████████████████████████████████████████▊                       | 70/92 [09:53<02:40,  7.29s/it]INFO:vector_store:Embedding progress: 76.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  77%|██████████████████████████████████████████████████████████████████████████▊                      | 71/92 [10:00<02:31,  7.21s/it]INFO:vector_store:Embedding progress: 77.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|███████████████████████████████████████████████████████████████████████████▉                     | 72/92 [10:09<02:32,  7.61s/it]INFO:vector_store:Embedding progress: 78.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  79%|████████████████████████████████████████████████████████████████████████████▉                    | 73/92 [10:11<01:51,  5.87s/it]INFO:vector_store:Embedding progress: 79.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|██████████████████████████████████████████████████████████████████████████████                   | 74/92 [10:11<01:16,  4.27s/it]INFO:vector_store:Embedding progress: 80.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████                  | 75/92 [10:12<00:55,  3.27s/it]INFO:vector_store:Embedding progress: 81.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  83%|████████████████████████████████████████████████████████████████████████████████▏                | 76/92 [10:12<00:37,  2.36s/it]INFO:vector_store:Embedding progress: 82.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  84%|█████████████████████████████████████████████████████████████████████████████████▏               | 77/92 [10:15<00:37,  2.47s/it]INFO:vector_store:Embedding progress: 83.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  85%|██████████████████████████████████████████████████████████████████████████████████▏              | 78/92 [10:57<03:18, 14.17s/it]INFO:vector_store:Embedding progress: 84.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  86%|███████████████████████████████████████████████████████████████████████████████████▎             | 79/92 [11:07<02:51, 13.19s/it]INFO:vector_store:Embedding progress: 85.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  87%|████████████████████████████████████████████████████████████████████████████████████▎            | 80/92 [11:09<01:55,  9.61s/it]INFO:vector_store:Embedding progress: 87.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▍           | 81/92 [11:12<01:24,  7.71s/it]INFO:vector_store:Embedding progress: 88.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  89%|██████████████████████████████████████████████████████████████████████████████████████▍          | 82/92 [11:17<01:10,  7.05s/it]INFO:vector_store:Embedding progress: 89.1%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▌         | 83/92 [11:28<01:12,  8.05s/it]INFO:vector_store:Embedding progress: 90.2%
Creating embeddings:  91%|████████████████████████████████████████████████████████████████████████████████████████▌        | 84/92 [11:30<00:49,  6.20s/it]INFO:vector_store:Embedding progress: 91.3%
Creating embeddings:  92%|█████████████████████████████████████████████████████████████████████████████████████████▌       | 85/92 [11:31<00:32,  4.69s/it]INFO:vector_store:Embedding progress: 92.4%
Creating embeddings:  93%|██████████████████████████████████████████████████████████████████████████████████████████▋      | 86/92 [11:32<00:21,  3.61s/it]INFO:vector_store:Embedding progress: 93.5%
Creating embeddings:  95%|███████████████████████████████████████████████████████████████████████████████████████████▋     | 87/92 [11:33<00:13,  2.69s/it]INFO:vector_store:Embedding progress: 94.6%
Creating embeddings:  96%|████████████████████████████████████████████████████████████████████████████████████████████▊    | 88/92 [11:35<00:10,  2.60s/it]INFO:vector_store:Embedding progress: 95.7%
Creating embeddings:  97%|█████████████████████████████████████████████████████████████████████████████████████████████▊   | 89/92 [11:45<00:14,  4.92s/it]INFO:vector_store:Embedding progress: 96.7%
Creating embeddings:  98%|██████████████████████████████████████████████████████████████████████████████████████████████▉  | 90/92 [11:48<00:08,  4.30s/it]INFO:vector_store:Embedding progress: 97.8%
Creating embeddings:  99%|███████████████████████████████████████████████████████████████████████████████████████████████▉ | 91/92 [11:50<00:03,  3.47s/it]INFO:vector_store:Embedding progress: 98.9%
INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 92/92 [11:50<00:00,  7.72s/it]
INFO:vector_store:Processed 27907 chunks so far
INFO:vector_store:Processed 28907 chunks so far
INFO:vector_store:Processed 29907 chunks so far
INFO:vector_store:Processed 30907 chunks so far
INFO:vector_store:Processed 31907 chunks so far
INFO:vector_store:Processed 32907 chunks so far
INFO:vector_store:Processed 33907 chunks so far
INFO:vector_store:Processed 34907 chunks so far
INFO:vector_store:Processed 35907 chunks so far
INFO:vector_store:Processed 36073 chunks so far
INFO:vector_store:Processing document batch 6 of 6
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                         | 0/394 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   0%|▏                                                                                            | 1/394 [02:30<16:24:44, 150.34s/it]INFO:vector_store:Embedding progress: 0.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   1%|▍                                                                                              | 2/394 [02:31<6:49:40, 62.71s/it]INFO:vector_store:Embedding progress: 0.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   1%|▋                                                                                              | 3/394 [02:34<3:50:01, 35.30s/it]INFO:vector_store:Embedding progress: 0.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   1%|▉                                                                                              | 4/394 [02:35<2:20:54, 21.68s/it]INFO:vector_store:Embedding progress: 1.0%
INFO:vector_store:Embedding progress: 1.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▍                                                                                             | 6/394 [02:38<1:10:56, 10.97s/it]INFO:vector_store:Embedding progress: 1.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▋                                                                                               | 7/394 [02:39<53:44,  8.33s/it]INFO:vector_store:Embedding progress: 1.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▉                                                                                               | 8/394 [02:41<42:12,  6.56s/it]INFO:vector_store:Embedding progress: 2.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|██▏                                                                                              | 9/394 [02:42<31:15,  4.87s/it]INFO:vector_store:Embedding progress: 2.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   3%|██▍                                                                                             | 10/394 [02:43<24:29,  3.83s/it]INFO:vector_store:Embedding progress: 2.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   3%|██▋                                                                                             | 11/394 [02:44<19:43,  3.09s/it]INFO:vector_store:Embedding progress: 2.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   3%|██▊                                                                                           | 12/394 [03:48<2:12:53, 20.87s/it]INFO:vector_store:Embedding progress: 3.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   3%|███                                                                                           | 13/394 [03:49<1:35:52, 15.10s/it]INFO:vector_store:Embedding progress: 3.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▎                                                                                          | 14/394 [03:52<1:12:56, 11.52s/it]INFO:vector_store:Embedding progress: 3.6%
Creating embeddings:   4%|███▋                                                                                            | 15/394 [03:52<51:23,  8.13s/it]INFO:vector_store:Embedding progress: 3.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|███▉                                                                                            | 16/394 [03:54<38:56,  6.18s/it]INFO:vector_store:Embedding progress: 4.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   4%|████▏                                                                                           | 17/394 [03:55<30:04,  4.79s/it]INFO:vector_store:Embedding progress: 4.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   5%|████▍                                                                                           | 18/394 [03:59<27:57,  4.46s/it]INFO:vector_store:Embedding progress: 4.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   5%|████▋                                                                                           | 19/394 [04:01<23:01,  3.68s/it]INFO:vector_store:Embedding progress: 4.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   5%|████▊                                                                                           | 20/394 [04:02<18:52,  3.03s/it]INFO:vector_store:Embedding progress: 5.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:   5%|█████                                                                                           | 21/394 [04:03<13:27,  2.17s/it]INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:vector_store:Embedding progress: 5.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▎                                                                                          | 22/394 [04:05<12:56,  2.09s/it]INFO:vector_store:Embedding progress: 5.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▍                                                                                        | 23/394 [05:06<2:02:56, 19.88s/it]INFO:vector_store:Embedding progress: 5.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▋                                                                                        | 24/394 [05:10<1:32:53, 15.06s/it]INFO:vector_store:Embedding progress: 6.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   6%|█████▉                                                                                        | 25/394 [05:11<1:07:58, 11.05s/it]INFO:vector_store:Embedding progress: 6.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   7%|██████▎                                                                                         | 26/394 [05:13<49:30,  8.07s/it]INFO:vector_store:Embedding progress: 6.6%
INFO:vector_store:Embedding progress: 6.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   7%|██████▊                                                                                         | 28/394 [05:15<29:23,  4.82s/it]INFO:vector_store:Embedding progress: 7.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   7%|███████                                                                                         | 29/394 [05:19<28:27,  4.68s/it]INFO:vector_store:Embedding progress: 7.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▎                                                                                        | 30/394 [05:19<21:34,  3.56s/it]INFO:vector_store:Embedding progress: 7.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▌                                                                                        | 31/394 [05:20<16:22,  2.71s/it]INFO:vector_store:Embedding progress: 7.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|███████▊                                                                                        | 32/394 [05:21<13:16,  2.20s/it]INFO:vector_store:Embedding progress: 8.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   8%|████████                                                                                        | 33/394 [05:23<12:55,  2.15s/it]INFO:vector_store:Embedding progress: 8.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   9%|████████                                                                                      | 34/394 [06:20<1:48:41, 18.11s/it]INFO:vector_store:Embedding progress: 8.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   9%|████████▎                                                                                     | 35/394 [06:28<1:30:34, 15.14s/it]INFO:vector_store:Embedding progress: 8.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   9%|████████▌                                                                                     | 36/394 [06:29<1:06:36, 11.16s/it]INFO:vector_store:Embedding progress: 9.1%
INFO:vector_store:Embedding progress: 9.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▎                                                                                      | 38/394 [06:31<37:35,  6.34s/it]INFO:vector_store:Embedding progress: 9.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▌                                                                                      | 39/394 [06:33<32:18,  5.46s/it]INFO:vector_store:Embedding progress: 9.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▋                                                                                      | 40/394 [06:36<28:02,  4.75s/it]INFO:vector_store:Embedding progress: 10.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▉                                                                                      | 41/394 [06:37<21:30,  3.66s/it]INFO:vector_store:Embedding progress: 10.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  11%|██████████▏                                                                                     | 42/394 [06:38<16:58,  2.89s/it]INFO:vector_store:Embedding progress: 10.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  11%|██████████▍                                                                                     | 43/394 [06:38<13:03,  2.23s/it]INFO:vector_store:Embedding progress: 10.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  11%|██████████▋                                                                                     | 44/394 [06:39<10:40,  1.83s/it]INFO:vector_store:Embedding progress: 11.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  11%|██████████▋                                                                                   | 45/394 [07:36<1:43:52, 17.86s/it]INFO:vector_store:Embedding progress: 11.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|██████████▉                                                                                   | 46/394 [07:48<1:34:02, 16.21s/it]INFO:vector_store:Embedding progress: 11.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▏                                                                                  | 47/394 [07:49<1:08:06, 11.78s/it]INFO:vector_store:Embedding progress: 11.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▋                                                                                    | 48/394 [07:50<48:30,  8.41s/it]INFO:vector_store:Embedding progress: 12.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▉                                                                                    | 49/394 [07:52<37:26,  6.51s/it]INFO:vector_store:Embedding progress: 12.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  13%|████████████▏                                                                                   | 50/394 [07:56<33:06,  5.78s/it]INFO:vector_store:Embedding progress: 12.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  13%|████████████▍                                                                                   | 51/394 [07:59<27:50,  4.87s/it]INFO:vector_store:Embedding progress: 12.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  13%|████████████▋                                                                                   | 52/394 [07:59<20:26,  3.59s/it]INFO:vector_store:Embedding progress: 13.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  13%|████████████▉                                                                                   | 53/394 [08:00<16:20,  2.88s/it]INFO:vector_store:Embedding progress: 13.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▏                                                                                  | 54/394 [08:01<12:17,  2.17s/it]INFO:vector_store:Embedding progress: 13.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▍                                                                                  | 55/394 [08:02<10:22,  1.84s/it]INFO:vector_store:Embedding progress: 14.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▎                                                                                | 56/394 [08:52<1:32:05, 16.35s/it]INFO:vector_store:Embedding progress: 14.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  14%|█████████████▌                                                                                | 57/394 [09:05<1:25:32, 15.23s/it]INFO:vector_store:Embedding progress: 14.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  15%|█████████████▊                                                                                | 58/394 [09:07<1:03:30, 11.34s/it]INFO:vector_store:Embedding progress: 14.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  15%|██████████████▍                                                                                 | 59/394 [09:10<48:31,  8.69s/it]INFO:vector_store:Embedding progress: 15.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  15%|██████████████▌                                                                                 | 60/394 [09:12<38:19,  6.88s/it]INFO:vector_store:Embedding progress: 15.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  15%|██████████████▊                                                                                 | 61/394 [09:15<31:04,  5.60s/it]INFO:vector_store:Embedding progress: 15.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████                                                                                 | 62/394 [09:19<29:02,  5.25s/it]INFO:vector_store:Embedding progress: 15.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▎                                                                                | 63/394 [09:21<22:54,  4.15s/it]INFO:vector_store:Embedding progress: 16.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▌                                                                                | 64/394 [09:22<17:03,  3.10s/it]INFO:vector_store:Embedding progress: 16.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  16%|███████████████▊                                                                                | 65/394 [09:22<13:18,  2.43s/it]INFO:vector_store:Embedding progress: 16.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  17%|████████████████                                                                                | 66/394 [09:23<10:05,  1.85s/it]INFO:vector_store:Embedding progress: 16.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  17%|███████████████▉                                                                              | 67/394 [10:08<1:20:50, 14.83s/it]INFO:vector_store:Embedding progress: 17.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  17%|████████████████▏                                                                             | 68/394 [10:20<1:16:39, 14.11s/it]INFO:vector_store:Embedding progress: 17.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|████████████████▍                                                                             | 69/394 [10:28<1:05:32, 12.10s/it]INFO:vector_store:Embedding progress: 17.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████                                                                               | 70/394 [10:29<47:22,  8.77s/it]INFO:vector_store:Embedding progress: 17.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▎                                                                              | 71/394 [10:30<34:53,  6.48s/it]INFO:vector_store:Embedding progress: 18.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▌                                                                              | 72/394 [10:33<29:41,  5.53s/it]INFO:vector_store:Embedding progress: 18.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  19%|█████████████████▊                                                                              | 73/394 [10:38<28:48,  5.38s/it]INFO:vector_store:Embedding progress: 18.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  19%|██████████████████                                                                              | 74/394 [10:42<25:53,  4.85s/it]INFO:vector_store:Embedding progress: 18.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  19%|██████████████████▎                                                                             | 75/394 [10:43<19:22,  3.64s/it]INFO:vector_store:Embedding progress: 19.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  19%|██████████████████▌                                                                             | 76/394 [10:44<14:53,  2.81s/it]INFO:vector_store:Embedding progress: 19.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|██████████████████▊                                                                             | 77/394 [10:44<11:28,  2.17s/it]INFO:vector_store:Embedding progress: 19.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|██████████████████▌                                                                           | 78/394 [11:27<1:14:37, 14.17s/it]INFO:vector_store:Embedding progress: 19.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|██████████████████▊                                                                           | 79/394 [11:38<1:09:33, 13.25s/it]INFO:vector_store:Embedding progress: 20.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████                                                                           | 80/394 [11:46<1:02:23, 11.92s/it]INFO:vector_store:Embedding progress: 20.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  21%|███████████████████▋                                                                            | 81/394 [11:48<46:40,  8.95s/it]INFO:vector_store:Embedding progress: 20.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  21%|███████████████████▉                                                                            | 82/394 [11:49<33:03,  6.36s/it]INFO:vector_store:Embedding progress: 20.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  21%|████████████████████▏                                                                           | 83/394 [11:54<30:44,  5.93s/it]INFO:vector_store:Embedding progress: 21.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  21%|████████████████████▍                                                                           | 84/394 [12:00<31:45,  6.15s/it]INFO:vector_store:Embedding progress: 21.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|████████████████████▋                                                                           | 85/394 [12:03<26:07,  5.07s/it]INFO:vector_store:Embedding progress: 21.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|████████████████████▉                                                                           | 86/394 [12:03<18:29,  3.60s/it]INFO:vector_store:Embedding progress: 21.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████▏                                                                          | 87/394 [12:04<13:53,  2.72s/it]INFO:vector_store:Embedding progress: 22.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████▍                                                                          | 88/394 [12:06<13:18,  2.61s/it]INFO:vector_store:Embedding progress: 22.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  23%|█████████████████████▏                                                                        | 89/394 [12:46<1:09:43, 13.72s/it]INFO:vector_store:Embedding progress: 22.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  23%|█████████████████████▍                                                                        | 90/394 [12:57<1:05:01, 12.83s/it]INFO:vector_store:Embedding progress: 22.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  23%|█████████████████████▋                                                                        | 91/394 [13:08<1:02:24, 12.36s/it]INFO:vector_store:Embedding progress: 23.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  23%|██████████████████████▍                                                                         | 92/394 [13:10<47:27,  9.43s/it]INFO:vector_store:Embedding progress: 23.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|██████████████████████▋                                                                         | 93/394 [13:11<34:22,  6.85s/it]INFO:vector_store:Embedding progress: 23.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|██████████████████████▉                                                                         | 94/394 [13:14<28:35,  5.72s/it]INFO:vector_store:Embedding progress: 23.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▏                                                                        | 95/394 [13:21<30:31,  6.13s/it]INFO:vector_store:Embedding progress: 24.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  24%|███████████████████████▍                                                                        | 96/394 [13:23<23:21,  4.70s/it]INFO:vector_store:Embedding progress: 24.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  25%|███████████████████████▋                                                                        | 97/394 [13:24<18:33,  3.75s/it]INFO:vector_store:Embedding progress: 24.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  25%|███████████████████████▉                                                                        | 98/394 [13:25<13:43,  2.78s/it]INFO:vector_store:Embedding progress: 24.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  25%|████████████████████████                                                                        | 99/394 [13:27<12:15,  2.49s/it]INFO:vector_store:Embedding progress: 25.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  25%|███████████████████████▌                                                                     | 100/394 [14:04<1:03:29, 12.96s/it]INFO:vector_store:Embedding progress: 25.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|███████████████████████▊                                                                     | 101/394 [14:15<1:00:38, 12.42s/it]INFO:vector_store:Embedding progress: 25.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|████████████████████████                                                                     | 102/394 [14:28<1:01:27, 12.63s/it]INFO:vector_store:Embedding progress: 25.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  26%|████████████████████████▊                                                                      | 103/394 [14:31<46:44,  9.64s/it]INFO:vector_store:Embedding progress: 26.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:  26%|█████████████████████████                                                                      | 104/394 [14:31<32:48,  6.79s/it]INFO:vector_store:Embedding progress: 26.4%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  27%|█████████████████████████▎                                                                     | 105/394 [14:35<28:18,  5.88s/it]INFO:vector_store:Embedding progress: 26.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  27%|█████████████████████████▌                                                                     | 106/394 [14:42<29:21,  6.12s/it]INFO:vector_store:Embedding progress: 26.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  27%|█████████████████████████▊                                                                     | 107/394 [14:45<25:45,  5.38s/it]INFO:vector_store:Embedding progress: 27.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  27%|██████████████████████████                                                                     | 108/394 [14:47<20:15,  4.25s/it]INFO:vector_store:Embedding progress: 27.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|██████████████████████████▎                                                                    | 109/394 [14:47<15:02,  3.17s/it]INFO:vector_store:Embedding progress: 27.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|██████████████████████████▌                                                                    | 110/394 [14:48<12:00,  2.54s/it]INFO:vector_store:Embedding progress: 27.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|██████████████████████████▊                                                                    | 111/394 [15:24<58:18, 12.36s/it]INFO:vector_store:Embedding progress: 28.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  28%|███████████████████████████                                                                    | 112/394 [15:34<55:08, 11.73s/it]INFO:vector_store:Embedding progress: 28.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  29%|███████████████████████████▏                                                                   | 113/394 [15:47<57:12, 12.21s/it]INFO:vector_store:Embedding progress: 28.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  29%|███████████████████████████▍                                                                   | 114/394 [15:55<50:34, 10.84s/it]INFO:vector_store:Embedding progress: 28.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  29%|███████████████████████████▋                                                                   | 115/394 [15:55<35:33,  7.65s/it]INFO:vector_store:Embedding progress: 29.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  29%|███████████████████████████▉                                                                   | 116/394 [15:57<26:47,  5.78s/it]INFO:vector_store:Embedding progress: 29.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|████████████████████████████▏                                                                  | 117/394 [16:03<27:32,  5.97s/it]INFO:vector_store:Embedding progress: 29.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|████████████████████████████▍                                                                  | 118/394 [16:06<23:05,  5.02s/it]INFO:vector_store:Embedding progress: 29.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|████████████████████████████▋                                                                  | 119/394 [16:10<21:59,  4.80s/it]INFO:vector_store:Embedding progress: 30.2%
INFO:vector_store:Embedding progress: 30.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  31%|█████████████████████████████▏                                                                 | 121/394 [16:11<12:28,  2.74s/it]INFO:vector_store:Embedding progress: 30.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  31%|█████████████████████████████▍                                                                 | 122/394 [16:43<45:35, 10.06s/it]INFO:vector_store:Embedding progress: 31.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  31%|█████████████████████████████▋                                                                 | 123/394 [16:58<51:26, 11.39s/it]INFO:vector_store:Embedding progress: 31.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  31%|█████████████████████████████▉                                                                 | 124/394 [17:07<47:42, 10.60s/it]INFO:vector_store:Embedding progress: 31.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|██████████████████████████████▏                                                                | 125/394 [17:15<44:52, 10.01s/it]INFO:vector_store:Embedding progress: 31.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|██████████████████████████████▍                                                                | 126/394 [17:16<33:16,  7.45s/it]INFO:vector_store:Embedding progress: 32.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|██████████████████████████████▌                                                                | 127/394 [17:18<25:32,  5.74s/it]INFO:vector_store:Embedding progress: 32.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|██████████████████████████████▊                                                                | 128/394 [17:25<26:42,  6.03s/it]INFO:vector_store:Embedding progress: 32.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  33%|███████████████████████████████                                                                | 129/394 [17:26<20:14,  4.58s/it]INFO:vector_store:Embedding progress: 32.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  33%|███████████████████████████████▎                                                               | 130/394 [17:30<20:00,  4.55s/it]INFO:vector_store:Embedding progress: 33.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  33%|███████████████████████████████▌                                                               | 131/394 [17:32<16:28,  3.76s/it]INFO:vector_store:Embedding progress: 33.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|███████████████████████████████▊                                                               | 132/394 [17:33<12:55,  2.96s/it]INFO:vector_store:Embedding progress: 33.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|████████████████████████████████                                                               | 133/394 [18:05<50:00, 11.49s/it]INFO:vector_store:Embedding progress: 33.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|████████████████████████████████▎                                                              | 134/394 [18:21<55:57, 12.91s/it]INFO:vector_store:Embedding progress: 34.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  34%|████████████████████████████████▌                                                              | 135/394 [18:32<53:14, 12.33s/it]INFO:vector_store:Embedding progress: 34.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  35%|████████████████████████████████▊                                                              | 136/394 [18:37<43:20, 10.08s/it]INFO:vector_store:Embedding progress: 34.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  35%|█████████████████████████████████                                                              | 137/394 [18:38<31:36,  7.38s/it]INFO:vector_store:Embedding progress: 34.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  35%|█████████████████████████████████▎                                                             | 138/394 [18:39<23:44,  5.56s/it]INFO:vector_store:Embedding progress: 35.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  35%|█████████████████████████████████▌                                                             | 139/394 [18:45<24:38,  5.80s/it]INFO:vector_store:Embedding progress: 35.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|█████████████████████████████████▊                                                             | 140/394 [18:48<20:28,  4.84s/it]INFO:vector_store:Embedding progress: 35.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|█████████████████████████████████▉                                                             | 141/394 [18:51<17:52,  4.24s/it]INFO:vector_store:Embedding progress: 35.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  36%|██████████████████████████████████▏                                                            | 142/394 [18:53<15:27,  3.68s/it]INFO:vector_store:Embedding progress: 36.0%
INFO:vector_store:Embedding progress: 36.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  37%|██████████████████████████████████▋                                                            | 144/394 [19:25<38:51,  9.33s/it]INFO:vector_store:Embedding progress: 36.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  37%|██████████████████████████████████▉                                                            | 145/394 [19:41<45:08, 10.88s/it]INFO:vector_store:Embedding progress: 36.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  37%|███████████████████████████████████▏                                                           | 146/394 [19:54<47:15, 11.43s/it]INFO:vector_store:Embedding progress: 37.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  37%|███████████████████████████████████▍                                                           | 147/394 [19:58<39:15,  9.54s/it]INFO:vector_store:Embedding progress: 37.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|███████████████████████████████████▋                                                           | 148/394 [19:59<29:32,  7.21s/it]INFO:vector_store:Embedding progress: 37.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|███████████████████████████████████▉                                                           | 149/394 [20:01<22:43,  5.57s/it]INFO:vector_store:Embedding progress: 37.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▏                                                          | 150/394 [20:06<21:52,  5.38s/it]INFO:vector_store:Embedding progress: 38.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|████████████████████████████████████▍                                                          | 151/394 [20:07<17:22,  4.29s/it]INFO:vector_store:Embedding progress: 38.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  39%|████████████████████████████████████▋                                                          | 152/394 [20:12<18:03,  4.48s/it]INFO:vector_store:Embedding progress: 38.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  39%|████████████████████████████████████▉                                                          | 153/394 [20:15<16:09,  4.02s/it]INFO:vector_store:Embedding progress: 38.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  39%|█████████████████████████████████████▏                                                         | 154/394 [20:16<11:55,  2.98s/it]INFO:vector_store:Embedding progress: 39.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  39%|█████████████████████████████████████▎                                                         | 155/394 [20:44<41:46, 10.49s/it]INFO:vector_store:Embedding progress: 39.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|█████████████████████████████████████▌                                                         | 156/394 [21:02<51:06, 12.89s/it]INFO:vector_store:Embedding progress: 39.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|█████████████████████████████████████▊                                                         | 157/394 [21:14<49:04, 12.42s/it]INFO:vector_store:Embedding progress: 39.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████                                                         | 158/394 [21:16<36:31,  9.28s/it]INFO:vector_store:Embedding progress: 40.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▎                                                        | 159/394 [21:19<29:08,  7.44s/it]INFO:vector_store:Embedding progress: 40.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  41%|██████████████████████████████████████▌                                                        | 160/394 [21:20<22:04,  5.66s/it]INFO:vector_store:Embedding progress: 40.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  41%|██████████████████████████████████████▊                                                        | 161/394 [21:26<21:35,  5.56s/it]INFO:vector_store:Embedding progress: 40.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  41%|███████████████████████████████████████                                                        | 162/394 [21:37<28:09,  7.28s/it]INFO:vector_store:Embedding progress: 41.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  41%|███████████████████████████████████████▎                                                       | 163/394 [21:38<21:17,  5.53s/it]INFO:vector_store:Embedding progress: 41.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|███████████████████████████████████████▌                                                       | 164/394 [21:39<15:45,  4.11s/it]INFO:vector_store:Embedding progress: 41.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|███████████████████████████████████████▊                                                       | 165/394 [21:40<12:02,  3.15s/it]INFO:vector_store:Embedding progress: 41.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████                                                       | 166/394 [22:04<35:24,  9.32s/it]INFO:vector_store:Embedding progress: 42.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▎                                                      | 167/394 [22:24<47:11, 12.47s/it]INFO:vector_store:Embedding progress: 42.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  43%|████████████████████████████████████████▌                                                      | 168/394 [22:35<45:53, 12.18s/it]INFO:vector_store:Embedding progress: 42.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  43%|████████████████████████████████████████▋                                                      | 169/394 [22:36<33:25,  8.91s/it]INFO:vector_store:Embedding progress: 42.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  43%|████████████████████████████████████████▉                                                      | 170/394 [22:39<26:41,  7.15s/it]INFO:vector_store:Embedding progress: 43.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  43%|█████████████████████████████████████████▏                                                     | 171/394 [22:40<19:28,  5.24s/it]INFO:vector_store:Embedding progress: 43.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|█████████████████████████████████████████▍                                                     | 172/394 [22:46<20:15,  5.47s/it]INFO:vector_store:Embedding progress: 43.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|█████████████████████████████████████████▋                                                     | 173/394 [22:58<26:48,  7.28s/it]INFO:vector_store:Embedding progress: 43.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|█████████████████████████████████████████▉                                                     | 174/394 [22:59<19:51,  5.42s/it]INFO:vector_store:Embedding progress: 44.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  44%|██████████████████████████████████████████▏                                                    | 175/394 [23:01<16:24,  4.49s/it]INFO:vector_store:Embedding progress: 44.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  45%|██████████████████████████████████████████▍                                                    | 176/394 [23:02<12:18,  3.39s/it]INFO:vector_store:Embedding progress: 44.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  45%|██████████████████████████████████████████▋                                                    | 177/394 [23:24<32:41,  9.04s/it]INFO:vector_store:Embedding progress: 44.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  45%|██████████████████████████████████████████▉                                                    | 178/394 [23:43<42:34, 11.83s/it]INFO:vector_store:Embedding progress: 45.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  45%|███████████████████████████████████████████▏                                                   | 179/394 [23:55<42:49, 11.95s/it]INFO:vector_store:Embedding progress: 45.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|███████████████████████████████████████████▍                                                   | 180/394 [23:56<31:25,  8.81s/it]INFO:vector_store:Embedding progress: 45.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|███████████████████████████████████████████▋                                                   | 181/394 [24:00<25:24,  7.16s/it]INFO:vector_store:Embedding progress: 45.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:  46%|███████████████████████████████████████████▉                                                   | 182/394 [24:00<17:55,  5.07s/it]INFO:vector_store:Embedding progress: 46.2%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  46%|████████████████████████████████████████████                                                   | 183/394 [24:09<22:19,  6.35s/it]INFO:vector_store:Embedding progress: 46.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  47%|████████████████████████████████████████████▎                                                  | 184/394 [24:21<27:55,  7.98s/it]INFO:vector_store:Embedding progress: 46.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  47%|████████████████████████████████████████████▌                                                  | 185/394 [24:21<19:55,  5.72s/it]INFO:vector_store:Embedding progress: 47.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  47%|████████████████████████████████████████████▊                                                  | 186/394 [24:23<15:56,  4.60s/it]INFO:vector_store:Embedding progress: 47.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:  47%|█████████████████████████████████████████████                                                  | 187/394 [24:23<11:20,  3.29s/it]INFO:vector_store:Embedding progress: 47.5%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|█████████████████████████████████████████████▎                                                 | 188/394 [24:44<29:20,  8.55s/it]INFO:vector_store:Embedding progress: 47.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|█████████████████████████████████████████████▌                                                 | 189/394 [25:04<40:25, 11.83s/it]INFO:vector_store:Embedding progress: 48.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|█████████████████████████████████████████████▊                                                 | 190/394 [25:17<41:15, 12.13s/it]INFO:vector_store:Embedding progress: 48.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████                                                 | 191/394 [25:18<30:08,  8.91s/it]INFO:vector_store:Embedding progress: 48.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  49%|██████████████████████████████████████████████▎                                                | 192/394 [25:21<23:33,  7.00s/it]INFO:vector_store:Embedding progress: 48.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  49%|██████████████████████████████████████████████▌                                                | 193/394 [25:21<16:38,  4.97s/it]INFO:vector_store:Embedding progress: 49.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  49%|██████████████████████████████████████████████▊                                                | 194/394 [25:30<21:09,  6.35s/it]INFO:vector_store:Embedding progress: 49.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  49%|███████████████████████████████████████████████                                                | 195/394 [25:44<27:57,  8.43s/it]INFO:vector_store:Embedding progress: 49.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|███████████████████████████████████████████████▎                                               | 196/394 [25:45<20:58,  6.36s/it]INFO:vector_store:Embedding progress: 49.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|███████████████████████████████████████████████▌                                               | 197/394 [25:46<15:05,  4.59s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|███████████████████████████████████████████████▋                                               | 198/394 [25:46<11:12,  3.43s/it]INFO:vector_store:Embedding progress: 50.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  51%|███████████████████████████████████████████████▉                                               | 199/394 [26:03<24:02,  7.40s/it]INFO:vector_store:Embedding progress: 50.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  51%|████████████████████████████████████████████████▏                                              | 200/394 [26:26<39:16, 12.15s/it]INFO:vector_store:Embedding progress: 50.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  51%|████████████████████████████████████████████████▍                                              | 201/394 [26:38<38:42, 12.03s/it]INFO:vector_store:Embedding progress: 51.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  51%|████████████████████████████████████████████████▋                                              | 202/394 [26:39<27:48,  8.69s/it]INFO:vector_store:Embedding progress: 51.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|████████████████████████████████████████████████▉                                              | 203/394 [26:41<21:09,  6.65s/it]INFO:vector_store:Embedding progress: 51.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|█████████████████████████████████████████████████▏                                             | 204/394 [26:42<16:13,  5.12s/it]INFO:vector_store:Embedding progress: 51.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|█████████████████████████████████████████████████▍                                             | 205/394 [26:50<18:49,  5.98s/it]INFO:vector_store:Embedding progress: 52.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|█████████████████████████████████████████████████▋                                             | 206/394 [27:06<27:39,  8.83s/it]INFO:vector_store:Embedding progress: 52.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  53%|█████████████████████████████████████████████████▉                                             | 207/394 [27:09<22:13,  7.13s/it]INFO:vector_store:Embedding progress: 52.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:  53%|██████████████████████████████████████████████████▏                                            | 208/394 [27:09<15:41,  5.06s/it]INFO:vector_store:Embedding progress: 52.8%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  53%|██████████████████████████████████████████████████▍                                            | 209/394 [27:10<11:46,  3.82s/it]INFO:vector_store:Embedding progress: 53.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  53%|██████████████████████████████████████████████████▋                                            | 210/394 [27:23<19:35,  6.39s/it]INFO:vector_store:Embedding progress: 53.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|██████████████████████████████████████████████████▉                                            | 211/394 [27:48<36:43, 12.04s/it]INFO:vector_store:Embedding progress: 53.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|███████████████████████████████████████████████████                                            | 212/394 [27:59<36:01, 11.87s/it]INFO:vector_store:Embedding progress: 53.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|███████████████████████████████████████████████████▎                                           | 213/394 [28:00<25:29,  8.45s/it]INFO:vector_store:Embedding progress: 54.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  54%|███████████████████████████████████████████████████▌                                           | 214/394 [28:02<19:53,  6.63s/it]INFO:vector_store:Embedding progress: 54.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  55%|███████████████████████████████████████████████████▊                                           | 215/394 [28:03<14:29,  4.86s/it]INFO:vector_store:Embedding progress: 54.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  55%|████████████████████████████████████████████████████                                           | 216/394 [28:09<15:28,  5.21s/it]INFO:vector_store:Embedding progress: 54.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  55%|████████████████████████████████████████████████████▎                                          | 217/394 [28:27<26:31,  8.99s/it]INFO:vector_store:Embedding progress: 55.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  55%|████████████████████████████████████████████████████▌                                          | 218/394 [28:30<21:27,  7.32s/it]INFO:vector_store:Embedding progress: 55.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|████████████████████████████████████████████████████▊                                          | 219/394 [28:31<15:32,  5.33s/it]INFO:vector_store:Embedding progress: 55.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|█████████████████████████████████████████████████████                                          | 220/394 [28:32<11:59,  4.14s/it]INFO:vector_store:Embedding progress: 55.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|█████████████████████████████████████████████████████▎                                         | 221/394 [28:42<17:09,  5.95s/it]INFO:vector_store:Embedding progress: 56.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  56%|█████████████████████████████████████████████████████▌                                         | 222/394 [29:08<33:52, 11.82s/it]INFO:vector_store:Embedding progress: 56.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  57%|█████████████████████████████████████████████████████▊                                         | 223/394 [29:20<34:02, 11.95s/it]INFO:vector_store:Embedding progress: 56.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  57%|██████████████████████████████████████████████████████                                         | 224/394 [29:22<25:03,  8.84s/it]INFO:vector_store:Embedding progress: 56.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  57%|██████████████████████████████████████████████████████▎                                        | 225/394 [29:24<19:15,  6.84s/it]INFO:vector_store:Embedding progress: 57.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  57%|██████████████████████████████████████████████████████▍                                        | 226/394 [29:26<15:02,  5.37s/it]INFO:vector_store:Embedding progress: 57.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|██████████████████████████████████████████████████████▋                                        | 227/394 [29:30<13:48,  4.96s/it]INFO:vector_store:Embedding progress: 57.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|██████████████████████████████████████████████████████▉                                        | 228/394 [29:49<25:38,  9.27s/it]INFO:vector_store:Embedding progress: 57.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|███████████████████████████████████████████████████████▏                                       | 229/394 [29:52<20:20,  7.40s/it]INFO:vector_store:Embedding progress: 58.1%
Creating embeddings:  58%|███████████████████████████████████████████████████████▍                                       | 230/394 [29:52<14:19,  5.24s/it]INFO:vector_store:Embedding progress: 58.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  59%|███████████████████████████████████████████████████████▋                                       | 231/394 [29:54<11:19,  4.17s/it]INFO:vector_store:Embedding progress: 58.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  59%|███████████████████████████████████████████████████████▉                                       | 232/394 [30:03<15:23,  5.70s/it]INFO:vector_store:Embedding progress: 58.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  59%|████████████████████████████████████████████████████████▏                                      | 233/394 [30:27<29:43, 11.08s/it]INFO:vector_store:Embedding progress: 59.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  59%|████████████████████████████████████████████████████████▍                                      | 234/394 [30:39<30:12, 11.33s/it]INFO:vector_store:Embedding progress: 59.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|████████████████████████████████████████████████████████▋                                      | 235/394 [30:44<25:15,  9.53s/it]INFO:vector_store:Embedding progress: 59.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|████████████████████████████████████████████████████████▉                                      | 236/394 [30:47<19:37,  7.45s/it]INFO:vector_store:Embedding progress: 59.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|█████████████████████████████████████████████████████████▏                                     | 237/394 [30:48<14:38,  5.59s/it]INFO:vector_store:Embedding progress: 60.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|█████████████████████████████████████████████████████████▍                                     | 238/394 [30:51<12:49,  4.93s/it]INFO:vector_store:Embedding progress: 60.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  61%|█████████████████████████████████████████████████████████▋                                     | 239/394 [31:10<23:22,  9.05s/it]INFO:vector_store:Embedding progress: 60.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  61%|█████████████████████████████████████████████████████████▊                                     | 240/394 [31:15<19:49,  7.72s/it]INFO:vector_store:Embedding progress: 60.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  61%|██████████████████████████████████████████████████████████                                     | 241/394 [31:15<14:21,  5.63s/it]INFO:vector_store:Embedding progress: 61.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  61%|██████████████████████████████████████████████████████████▎                                    | 242/394 [31:16<10:22,  4.09s/it]INFO:vector_store:Embedding progress: 61.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|██████████████████████████████████████████████████████████▌                                    | 243/394 [31:24<13:17,  5.28s/it]INFO:vector_store:Embedding progress: 61.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|██████████████████████████████████████████████████████████▊                                    | 244/394 [31:47<26:08, 10.46s/it]INFO:vector_store:Embedding progress: 61.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|███████████████████████████████████████████████████████████                                    | 245/394 [31:59<27:41, 11.15s/it]INFO:vector_store:Embedding progress: 62.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|███████████████████████████████████████████████████████████▎                                   | 246/394 [32:06<24:14,  9.83s/it]INFO:vector_store:Embedding progress: 62.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  63%|███████████████████████████████████████████████████████████▌                                   | 247/394 [32:07<17:24,  7.10s/it]INFO:vector_store:Embedding progress: 62.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  63%|███████████████████████████████████████████████████████████▊                                   | 248/394 [32:09<14:00,  5.76s/it]INFO:vector_store:Embedding progress: 62.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  63%|████████████████████████████████████████████████████████████                                   | 249/394 [32:13<12:17,  5.08s/it]INFO:vector_store:Embedding progress: 63.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  63%|████████████████████████████████████████████████████████████▎                                  | 250/394 [32:30<20:53,  8.71s/it]INFO:vector_store:Embedding progress: 63.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|████████████████████████████████████████████████████████████▌                                  | 251/394 [32:36<18:48,  7.89s/it]INFO:vector_store:Embedding progress: 63.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|████████████████████████████████████████████████████████████▊                                  | 252/394 [32:38<14:43,  6.22s/it]INFO:vector_store:Embedding progress: 64.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|█████████████████████████████████████████████████████████████                                  | 253/394 [32:39<10:33,  4.49s/it]INFO:vector_store:Embedding progress: 64.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  64%|█████████████████████████████████████████████████████████████▏                                 | 254/394 [32:52<16:35,  7.11s/it]INFO:vector_store:Embedding progress: 64.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|█████████████████████████████████████████████████████████████▍                                 | 255/394 [33:06<21:33,  9.30s/it]INFO:vector_store:Embedding progress: 64.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|█████████████████████████████████████████████████████████████▋                                 | 256/394 [33:22<25:38, 11.15s/it]INFO:vector_store:Embedding progress: 65.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|█████████████████████████████████████████████████████████████▉                                 | 257/394 [33:29<22:46,  9.97s/it]INFO:vector_store:Embedding progress: 65.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|██████████████████████████████████████████████████████████████▏                                | 258/394 [33:30<16:21,  7.22s/it]INFO:vector_store:Embedding progress: 65.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|██████████████████████████████████████████████████████████████▍                                | 259/394 [33:33<13:16,  5.90s/it]INFO:vector_store:Embedding progress: 65.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|██████████████████████████████████████████████████████████████▋                                | 260/394 [33:42<15:23,  6.89s/it]INFO:vector_store:Embedding progress: 66.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|██████████████████████████████████████████████████████████████▉                                | 261/394 [33:58<21:38,  9.76s/it]INFO:vector_store:Embedding progress: 66.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  66%|███████████████████████████████████████████████████████████████▏                               | 262/394 [34:01<16:41,  7.59s/it]INFO:vector_store:Embedding progress: 66.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  67%|███████████████████████████████████████████████████████████████▍                               | 263/394 [34:02<12:35,  5.77s/it]INFO:vector_store:Embedding progress: 66.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  67%|███████████████████████████████████████████████████████████████▋                               | 264/394 [34:04<09:53,  4.57s/it]INFO:vector_store:Embedding progress: 67.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  67%|███████████████████████████████████████████████████████████████▉                               | 265/394 [34:12<12:11,  5.67s/it]INFO:vector_store:Embedding progress: 67.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|████████████████████████████████████████████████████████████████▏                              | 266/394 [34:30<19:23,  9.09s/it]INFO:vector_store:Embedding progress: 67.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|████████████████████████████████████████████████████████████████▍                              | 267/394 [34:43<22:03, 10.42s/it]INFO:vector_store:Embedding progress: 67.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|████████████████████████████████████████████████████████████████▌                              | 268/394 [34:53<21:48, 10.39s/it]INFO:vector_store:Embedding progress: 68.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|████████████████████████████████████████████████████████████████▊                              | 269/394 [34:54<15:20,  7.36s/it]INFO:vector_store:Embedding progress: 68.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  69%|█████████████████████████████████████████████████████████████████                              | 270/394 [34:56<12:02,  5.83s/it]INFO:vector_store:Embedding progress: 68.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  69%|█████████████████████████████████████████████████████████████████▎                             | 271/394 [35:04<13:08,  6.41s/it]INFO:vector_store:Embedding progress: 68.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  69%|█████████████████████████████████████████████████████████████████▌                             | 272/394 [35:20<19:05,  9.39s/it]INFO:vector_store:Embedding progress: 69.0%
Creating embeddings:  69%|█████████████████████████████████████████████████████████████████▊                             | 273/394 [35:23<15:13,  7.55s/it]INFO:vector_store:Embedding progress: 69.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|██████████████████████████████████████████████████████████████████                             | 274/394 [35:26<12:12,  6.11s/it]INFO:vector_store:Embedding progress: 69.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|██████████████████████████████████████████████████████████████████▎                            | 275/394 [35:28<09:49,  4.95s/it]INFO:vector_store:Embedding progress: 69.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|██████████████████████████████████████████████████████████████████▌                            | 276/394 [35:35<10:53,  5.54s/it]INFO:vector_store:Embedding progress: 70.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|██████████████████████████████████████████████████████████████████▊                            | 277/394 [35:50<16:07,  8.27s/it]INFO:vector_store:Embedding progress: 70.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  71%|███████████████████████████████████████████████████████████████████                            | 278/394 [36:03<18:36,  9.62s/it]INFO:vector_store:Embedding progress: 70.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  71%|███████████████████████████████████████████████████████████████████▎                           | 279/394 [36:15<20:11, 10.54s/it]INFO:vector_store:Embedding progress: 70.8%
Creating embeddings:  71%|███████████████████████████████████████████████████████████████████▌                           | 280/394 [36:15<14:06,  7.42s/it]INFO:vector_store:Embedding progress: 71.1%
Creating embeddings:  71%|███████████████████████████████████████████████████████████████████▊                           | 281/394 [36:16<10:14,  5.44s/it]INFO:vector_store:Embedding progress: 71.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|███████████████████████████████████████████████████████████████████▉                           | 282/394 [36:24<11:32,  6.18s/it]INFO:vector_store:Embedding progress: 71.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|████████████████████████████████████████████████████████████████████▏                          | 283/394 [36:46<19:50, 10.72s/it]INFO:vector_store:Embedding progress: 71.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|████████████████████████████████████████████████████████████████████▍                          | 284/394 [36:46<14:11,  7.74s/it]INFO:vector_store:Embedding progress: 72.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|████████████████████████████████████████████████████████████████████▋                          | 285/394 [36:47<10:10,  5.60s/it]INFO:vector_store:Embedding progress: 72.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  73%|████████████████████████████████████████████████████████████████████▉                          | 286/394 [36:51<09:14,  5.14s/it]INFO:vector_store:Embedding progress: 72.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  73%|█████████████████████████████████████████████████████████████████████▏                         | 287/394 [36:55<08:31,  4.78s/it]INFO:vector_store:Embedding progress: 72.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  73%|█████████████████████████████████████████████████████████████████████▍                         | 288/394 [37:10<13:43,  7.77s/it]INFO:vector_store:Embedding progress: 73.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  73%|█████████████████████████████████████████████████████████████████████▋                         | 289/394 [37:25<17:45, 10.15s/it]INFO:vector_store:Embedding progress: 73.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|█████████████████████████████████████████████████████████████████████▉                         | 290/394 [37:39<19:18, 11.14s/it]INFO:vector_store:Embedding progress: 73.6%
INFO:vector_store:Embedding progress: 73.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|██████████████████████████████████████████████████████████████████████▍                        | 292/394 [37:40<10:33,  6.21s/it]INFO:vector_store:Embedding progress: 74.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  74%|██████████████████████████████████████████████████████████████████████▋                        | 293/394 [37:46<10:35,  6.29s/it]INFO:vector_store:Embedding progress: 74.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  75%|██████████████████████████████████████████████████████████████████████▉                        | 294/394 [38:08<17:21, 10.42s/it]INFO:vector_store:Embedding progress: 74.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  75%|███████████████████████████████████████████████████████████████████████▏                       | 295/394 [38:09<12:55,  7.83s/it]INFO:vector_store:Embedding progress: 74.9%
Creating embeddings:  75%|███████████████████████████████████████████████████████████████████████▎                       | 296/394 [38:09<09:17,  5.68s/it]INFO:vector_store:Embedding progress: 75.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  75%|███████████████████████████████████████████████████████████████████████▌                       | 297/394 [38:13<08:20,  5.16s/it]INFO:vector_store:Embedding progress: 75.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|███████████████████████████████████████████████████████████████████████▊                       | 298/394 [38:18<07:54,  4.94s/it]INFO:vector_store:Embedding progress: 75.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|████████████████████████████████████████████████████████████████████████                       | 299/394 [38:32<12:13,  7.72s/it]INFO:vector_store:Embedding progress: 75.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|████████████████████████████████████████████████████████████████████████▎                      | 300/394 [38:47<15:26,  9.86s/it]INFO:vector_store:Embedding progress: 76.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  76%|████████████████████████████████████████████████████████████████████████▌                      | 301/394 [39:00<16:34, 10.69s/it]INFO:vector_store:Embedding progress: 76.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  77%|████████████████████████████████████████████████████████████████████████▊                      | 302/394 [39:01<12:10,  7.94s/it]INFO:vector_store:Embedding progress: 76.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
Creating embeddings:  77%|█████████████████████████████████████████████████████████████████████████                      | 303/394 [39:01<08:30,  5.60s/it]INFO:vector_store:Embedding progress: 76.9%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  77%|█████████████████████████████████████████████████████████████████████████▎                     | 304/394 [39:07<08:38,  5.76s/it]INFO:vector_store:Embedding progress: 77.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  77%|█████████████████████████████████████████████████████████████████████████▌                     | 305/394 [39:32<16:45, 11.30s/it]INFO:vector_store:Embedding progress: 77.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|█████████████████████████████████████████████████████████████████████████▊                     | 306/394 [39:33<12:06,  8.26s/it]INFO:vector_store:Embedding progress: 77.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|██████████████████████████████████████████████████████████████████████████                     | 307/394 [39:33<08:31,  5.88s/it]INFO:vector_store:Embedding progress: 77.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|██████████████████████████████████████████████████████████████████████████▎                    | 308/394 [39:37<07:23,  5.15s/it]INFO:vector_store:Embedding progress: 78.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|██████████████████████████████████████████████████████████████████████████▌                    | 309/394 [39:40<06:26,  4.54s/it]INFO:vector_store:Embedding progress: 78.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  79%|██████████████████████████████████████████████████████████████████████████▋                    | 310/394 [39:56<11:15,  8.05s/it]INFO:vector_store:Embedding progress: 78.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  79%|██████████████████████████████████████████████████████████████████████████▉                    | 311/394 [40:08<12:57,  9.37s/it]INFO:vector_store:Embedding progress: 78.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  79%|███████████████████████████████████████████████████████████████████████████▏                   | 312/394 [40:22<14:30, 10.61s/it]INFO:vector_store:Embedding progress: 79.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  79%|███████████████████████████████████████████████████████████████████████████▍                   | 313/394 [40:22<10:08,  7.51s/it]INFO:vector_store:Embedding progress: 79.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|███████████████████████████████████████████████████████████████████████████▋                   | 314/394 [40:23<07:31,  5.64s/it]INFO:vector_store:Embedding progress: 79.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|███████████████████████████████████████████████████████████████████████████▉                   | 315/394 [40:24<05:27,  4.15s/it]INFO:vector_store:Embedding progress: 79.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|████████████████████████████████████████████████████████████████████████████▏                  | 316/394 [40:46<12:09,  9.35s/it]INFO:vector_store:Embedding progress: 80.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|████████████████████████████████████████████████████████████████████████████▍                  | 317/394 [40:55<11:52,  9.25s/it]INFO:vector_store:Embedding progress: 80.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  81%|████████████████████████████████████████████████████████████████████████████▋                  | 318/394 [40:57<09:10,  7.25s/it]INFO:vector_store:Embedding progress: 80.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  81%|████████████████████████████████████████████████████████████████████████████▉                  | 319/394 [40:59<06:51,  5.49s/it]INFO:vector_store:Embedding progress: 81.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  81%|█████████████████████████████████████████████████████████████████████████████▏                 | 320/394 [41:00<05:13,  4.23s/it]INFO:vector_store:Embedding progress: 81.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  81%|█████████████████████████████████████████████████████████████████████████████▍                 | 321/394 [41:19<10:29,  8.62s/it]INFO:vector_store:Embedding progress: 81.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  82%|█████████████████████████████████████████████████████████████████████████████▋                 | 322/394 [41:31<11:34,  9.65s/it]INFO:vector_store:Embedding progress: 81.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  82%|█████████████████████████████████████████████████████████████████████████████▉                 | 323/394 [41:42<12:00, 10.15s/it]INFO:vector_store:Embedding progress: 82.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  82%|██████████████████████████████████████████████████████████████████████████████                 | 324/394 [41:45<09:10,  7.86s/it]INFO:vector_store:Embedding progress: 82.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  82%|██████████████████████████████████████████████████████████████████████████████▎                | 325/394 [41:46<06:38,  5.77s/it]INFO:vector_store:Embedding progress: 82.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  83%|██████████████████████████████████████████████████████████████████████████████▌                | 326/394 [41:46<04:45,  4.21s/it]INFO:vector_store:Embedding progress: 82.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  83%|██████████████████████████████████████████████████████████████████████████████▊                | 327/394 [42:08<10:45,  9.64s/it]INFO:vector_store:Embedding progress: 83.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  83%|███████████████████████████████████████████████████████████████████████████████                | 328/394 [42:15<09:42,  8.83s/it]INFO:vector_store:Embedding progress: 83.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  84%|███████████████████████████████████████████████████████████████████████████████▎               | 329/394 [42:18<07:30,  6.92s/it]INFO:vector_store:Embedding progress: 83.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  84%|███████████████████████████████████████████████████████████████████████████████▌               | 330/394 [42:21<06:14,  5.85s/it]INFO:vector_store:Embedding progress: 83.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  84%|███████████████████████████████████████████████████████████████████████████████▊               | 331/394 [42:22<04:27,  4.25s/it]INFO:vector_store:Embedding progress: 84.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  84%|████████████████████████████████████████████████████████████████████████████████               | 332/394 [42:42<09:23,  9.09s/it]INFO:vector_store:Embedding progress: 84.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  85%|████████████████████████████████████████████████████████████████████████████████▎              | 333/394 [42:54<09:57,  9.79s/it]INFO:vector_store:Embedding progress: 84.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  85%|████████████████████████████████████████████████████████████████████████████████▌              | 334/394 [43:05<10:21, 10.35s/it]INFO:vector_store:Embedding progress: 84.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  85%|████████████████████████████████████████████████████████████████████████████████▊              | 335/394 [43:07<07:44,  7.87s/it]INFO:vector_store:Embedding progress: 85.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  85%|█████████████████████████████████████████████████████████████████████████████████              | 336/394 [43:09<05:48,  6.01s/it]INFO:vector_store:Embedding progress: 85.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  86%|█████████████████████████████████████████████████████████████████████████████████▎             | 337/394 [43:10<04:19,  4.56s/it]INFO:vector_store:Embedding progress: 85.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  86%|█████████████████████████████████████████████████████████████████████████████████▍             | 338/394 [43:31<08:57,  9.59s/it]INFO:vector_store:Embedding progress: 85.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  86%|█████████████████████████████████████████████████████████████████████████████████▋             | 339/394 [43:38<07:53,  8.61s/it]INFO:vector_store:Embedding progress: 86.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  86%|█████████████████████████████████████████████████████████████████████████████████▉             | 340/394 [43:40<06:04,  6.75s/it]INFO:vector_store:Embedding progress: 86.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  87%|██████████████████████████████████████████████████████████████████████████████████▏            | 341/394 [43:42<04:44,  5.36s/it]INFO:vector_store:Embedding progress: 86.5%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  87%|██████████████████████████████████████████████████████████████████████████████████▍            | 342/394 [43:43<03:32,  4.10s/it]INFO:vector_store:Embedding progress: 86.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  87%|██████████████████████████████████████████████████████████████████████████████████▋            | 343/394 [44:05<07:52,  9.27s/it]INFO:vector_store:Embedding progress: 87.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  87%|██████████████████████████████████████████████████████████████████████████████████▉            | 344/394 [44:13<07:25,  8.90s/it]INFO:vector_store:Embedding progress: 87.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  88%|███████████████████████████████████████████████████████████████████████████████████▏           | 345/394 [44:27<08:35, 10.53s/it]INFO:vector_store:Embedding progress: 87.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  88%|███████████████████████████████████████████████████████████████████████████████████▍           | 346/394 [44:30<06:35,  8.24s/it]INFO:vector_store:Embedding progress: 87.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  88%|███████████████████████████████████████████████████████████████████████████████████▋           | 347/394 [44:31<04:51,  6.20s/it]INFO:vector_store:Embedding progress: 88.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  88%|███████████████████████████████████████████████████████████████████████████████████▉           | 348/394 [44:36<04:18,  5.62s/it]INFO:vector_store:Embedding progress: 88.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  89%|████████████████████████████████████████████████████████████████████████████████████▏          | 349/394 [44:53<06:55,  9.23s/it]INFO:vector_store:Embedding progress: 88.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  89%|████████████████████████████████████████████████████████████████████████████████████▍          | 350/394 [44:57<05:27,  7.45s/it]INFO:vector_store:Embedding progress: 88.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  89%|████████████████████████████████████████████████████████████████████████████████████▋          | 351/394 [45:00<04:28,  6.25s/it]INFO:vector_store:Embedding progress: 89.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  89%|████████████████████████████████████████████████████████████████████████████████████▊          | 352/394 [45:04<03:48,  5.43s/it]INFO:vector_store:Embedding progress: 89.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  90%|█████████████████████████████████████████████████████████████████████████████████████          | 353/394 [45:05<02:46,  4.06s/it]INFO:vector_store:Embedding progress: 89.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  90%|█████████████████████████████████████████████████████████████████████████████████████▎         | 354/394 [45:27<06:22,  9.57s/it]INFO:vector_store:Embedding progress: 89.8%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  90%|█████████████████████████████████████████████████████████████████████████████████████▌         | 355/394 [45:35<05:50,  9.00s/it]INFO:vector_store:Embedding progress: 90.1%
Creating embeddings:  90%|█████████████████████████████████████████████████████████████████████████████████████▊         | 356/394 [45:49<06:44, 10.64s/it]INFO:vector_store:Embedding progress: 90.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  91%|██████████████████████████████████████████████████████████████████████████████████████         | 357/394 [45:51<04:51,  7.88s/it]INFO:vector_store:Embedding progress: 90.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  91%|██████████████████████████████████████████████████████████████████████████████████████▎        | 358/394 [45:53<03:44,  6.24s/it]INFO:vector_store:Embedding progress: 90.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  91%|██████████████████████████████████████████████████████████████████████████████████████▌        | 359/394 [45:57<03:19,  5.69s/it]INFO:vector_store:Embedding progress: 91.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  91%|██████████████████████████████████████████████████████████████████████████████████████▊        | 360/394 [46:14<05:08,  9.07s/it]INFO:vector_store:Embedding progress: 91.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  92%|███████████████████████████████████████████████████████████████████████████████████████        | 361/394 [46:19<04:13,  7.67s/it]INFO:vector_store:Embedding progress: 91.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  92%|███████████████████████████████████████████████████████████████████████████████████████▎       | 362/394 [46:21<03:14,  6.09s/it]INFO:vector_store:Embedding progress: 91.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  92%|███████████████████████████████████████████████████████████████████████████████████████▌       | 363/394 [46:25<02:48,  5.44s/it]INFO:vector_store:Embedding progress: 92.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  92%|███████████████████████████████████████████████████████████████████████████████████████▊       | 364/394 [46:26<02:07,  4.23s/it]INFO:vector_store:Embedding progress: 92.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  93%|████████████████████████████████████████████████████████████████████████████████████████       | 365/394 [46:48<04:32,  9.39s/it]INFO:vector_store:Embedding progress: 92.6%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  93%|████████████████████████████████████████████████████████████████████████████████████████▏      | 366/394 [47:01<04:53, 10.49s/it]INFO:vector_store:Embedding progress: 92.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  93%|████████████████████████████████████████████████████████████████████████████████████████▍      | 367/394 [47:11<04:43, 10.51s/it]INFO:vector_store:Embedding progress: 93.1%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  93%|████████████████████████████████████████████████████████████████████████████████████████▋      | 368/394 [47:12<03:19,  7.65s/it]INFO:vector_store:Embedding progress: 93.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  94%|████████████████████████████████████████████████████████████████████████████████████████▉      | 369/394 [47:16<02:39,  6.38s/it]INFO:vector_store:Embedding progress: 93.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  94%|█████████████████████████████████████████████████████████████████████████████████████████▏     | 370/394 [47:21<02:21,  5.89s/it]INFO:vector_store:Embedding progress: 93.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  94%|█████████████████████████████████████████████████████████████████████████████████████████▍     | 371/394 [47:36<03:17,  8.58s/it]INFO:vector_store:Embedding progress: 94.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  94%|█████████████████████████████████████████████████████████████████████████████████████████▋     | 372/394 [47:42<02:52,  7.85s/it]INFO:vector_store:Embedding progress: 94.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  95%|█████████████████████████████████████████████████████████████████████████████████████████▉     | 373/394 [47:43<02:05,  5.99s/it]INFO:vector_store:Embedding progress: 94.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  95%|██████████████████████████████████████████████████████████████████████████████████████████▏    | 374/394 [47:48<01:52,  5.64s/it]INFO:vector_store:Embedding progress: 94.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  95%|██████████████████████████████████████████████████████████████████████████████████████████▍    | 375/394 [47:49<01:19,  4.20s/it]INFO:vector_store:Embedding progress: 95.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  95%|██████████████████████████████████████████████████████████████████████████████████████████▋    | 376/394 [48:07<02:29,  8.29s/it]INFO:vector_store:Embedding progress: 95.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  96%|██████████████████████████████████████████████████████████████████████████████████████████▉    | 377/394 [48:22<02:56, 10.39s/it]INFO:vector_store:Embedding progress: 95.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  96%|███████████████████████████████████████████████████████████████████████████████████████████▏   | 378/394 [48:33<02:51, 10.69s/it]INFO:vector_store:Embedding progress: 95.9%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  96%|███████████████████████████████████████████████████████████████████████████████████████████▍   | 379/394 [48:34<01:55,  7.68s/it]INFO:vector_store:Embedding progress: 96.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  96%|███████████████████████████████████████████████████████████████████████████████████████████▌   | 380/394 [48:38<01:32,  6.64s/it]INFO:vector_store:Embedding progress: 96.4%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  97%|███████████████████████████████████████████████████████████████████████████████████████████▊   | 381/394 [48:43<01:18,  6.05s/it]INFO:vector_store:Embedding progress: 96.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  97%|████████████████████████████████████████████████████████████████████████████████████████████   | 382/394 [48:57<01:40,  8.42s/it]INFO:vector_store:Embedding progress: 97.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  97%|████████████████████████████████████████████████████████████████████████████████████████████▎  | 383/394 [49:03<01:26,  7.85s/it]INFO:vector_store:Embedding progress: 97.2%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  97%|████████████████████████████████████████████████████████████████████████████████████████████▌  | 384/394 [49:06<01:03,  6.36s/it]INFO:vector_store:Embedding progress: 97.5%
Creating embeddings:  98%|████████████████████████████████████████████████████████████████████████████████████████████▊  | 385/394 [49:11<00:51,  5.75s/it]INFO:vector_store:Embedding progress: 97.7%
Creating embeddings:  98%|█████████████████████████████████████████████████████████████████████████████████████████████  | 386/394 [49:11<00:32,  4.09s/it]INFO:vector_store:Embedding progress: 98.0%
Creating embeddings:  98%|█████████████████████████████████████████████████████████████████████████████████████████████▎ | 387/394 [49:18<00:35,  5.04s/it]INFO:vector_store:Embedding progress: 98.2%
Creating embeddings:  98%|█████████████████████████████████████████████████████████████████████████████████████████████▌ | 388/394 [49:25<00:32,  5.44s/it]INFO:vector_store:Embedding progress: 98.5%
Creating embeddings:  99%|█████████████████████████████████████████████████████████████████████████████████████████████▊ | 389/394 [49:33<00:31,  6.22s/it]INFO:vector_store:Embedding progress: 98.7%
Creating embeddings:  99%|██████████████████████████████████████████████████████████████████████████████████████████████ | 390/394 [49:38<00:23,  5.87s/it]INFO:vector_store:Embedding progress: 99.0%
Creating embeddings:  99%|██████████████████████████████████████████████████████████████████████████████████████████████▎| 391/394 [49:38<00:12,  4.25s/it]INFO:vector_store:Embedding progress: 99.2%
Creating embeddings:  99%|██████████████████████████████████████████████████████████████████████████████████████████████▌| 392/394 [49:39<00:06,  3.31s/it]INFO:vector_store:Embedding progress: 99.5%
Creating embeddings: 100%|██████████████████████████████████████████████████████████████████████████████████████████████▊| 393/394 [49:40<00:02,  2.68s/it]INFO:vector_store:Embedding progress: 99.7%
Creating embeddings: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 394/394 [49:42<00:00,  2.24s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 394/394 [49:42<00:00,  7.57s/it]
INFO:vector_store:Processed 37073 chunks so far
INFO:vector_store:Processed 38073 chunks so far
INFO:vector_store:Processed 39073 chunks so far
INFO:vector_store:Processed 40073 chunks so far
INFO:vector_store:Processed 41073 chunks so far
INFO:vector_store:Processed 42073 chunks so far
INFO:vector_store:Processed 43073 chunks so far
INFO:vector_store:Processed 44073 chunks so far
INFO:vector_store:Processed 45073 chunks so far
INFO:vector_store:Processed 46073 chunks so far
INFO:vector_store:Processed 47073 chunks so far
INFO:vector_store:Processed 48073 chunks so far
INFO:vector_store:Processed 49073 chunks so far
INFO:vector_store:Processed 50073 chunks so far
INFO:vector_store:Processed 51073 chunks so far
INFO:vector_store:Processed 52073 chunks so far
INFO:vector_store:Processed 53073 chunks so far
INFO:vector_store:Processed 54073 chunks so far
INFO:vector_store:Processed 55073 chunks so far
INFO:vector_store:Processed 56073 chunks so far
INFO:vector_store:Processed 57073 chunks so far
INFO:vector_store:Processed 58073 chunks so far
INFO:vector_store:Processed 59073 chunks so far
INFO:vector_store:Processed 60073 chunks so far
INFO:vector_store:Processed 61073 chunks so far
INFO:vector_store:Processed 62073 chunks so far
INFO:vector_store:Processed 63073 chunks so far
INFO:vector_store:Processed 64073 chunks so far
INFO:vector_store:Processed 65073 chunks so far
INFO:vector_store:Processed 66073 chunks so far
INFO:vector_store:Processed 67073 chunks so far
INFO:vector_store:Processed 68073 chunks so far
INFO:vector_store:Processed 69073 chunks so far
INFO:vector_store:Processed 70073 chunks so far
INFO:vector_store:Processed 71073 chunks so far
INFO:vector_store:Processed 72073 chunks so far
INFO:vector_store:Processed 73073 chunks so far
INFO:vector_store:Processed 74073 chunks so far
INFO:vector_store:Processed 75073 chunks so far
INFO:vector_store:Processed 75389 chunks so far
INFO:vector_store:Completed processing 28728 documents into 75389 chunks
ERROR:rag_system:Failed to add documents to vector store for plane_crash
INFO:rag_system:Processing data for disaster type: tsunami
INFO:data_ingestion:Processed CSV: data/tsunami/GLOBAL_SITES_TD.csv, Rows: 515
INFO:rag_system:Successfully processed 515 documents from data/tsunami/GLOBAL_SITES_TD.csv
INFO:data_ingestion:Processed CSV: data/tsunami/tsunami_dataset.csv, Rows: 2259
INFO:rag_system:Successfully processed 2259 documents from data/tsunami/tsunami_dataset.csv
ERROR:data_ingestion:Error processing URL https://www.ngdc.noaa.gov/hazel/view/hazards/tsunami/event-data?maxYear=2025&minYear=1900: HTTPSConnectionPool(host='www.ngdc.noaa.gov', port=443): Read timed out. (read timeout=10)
WARNING:rag_system:No documents extracted from https://www.ngdc.noaa.gov/hazel/view/hazards/tsunami/event-data?maxYear=2025&minYear=1900
WARNING:bs4.dammit:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
INFO:rag_system:Successfully processed 1 documents from https://cbe.miis.edu/cgi/viewcontent.cgi?article=1091&context=booc
INFO:rag_system:Successfully processed 1 documents from https://www.weather.gov/itic-car/tsunami_awareness_materials
INFO:rag_system:Successfully processed 1 documents from https://tsunami.ioc.unesco.org/en/pacific/itic
INFO:rag_system:Successfully processed 1 documents from https://psmsl.org/data/obtaining/
INFO:rag_system:Successfully processed 1 documents from https://www.ncei.noaa.gov/products/natural-hazards
INFO:rag_system:Successfully processed 1 documents from https://www.tsunami.gov/
INFO:rag_system:Successfully processed 1 documents from https://www.dnr.wa.gov/programs-and-services/geology/geologic-hazards/tsunamis#understanding-tsunamis.1
INFO:rag_system:Successfully processed 1 documents from https://www.dnr.wa.gov/programs-and-services/geology/geologic-hazards/tsunamis#tsunamis-in-washington
INFO:rag_system:Successfully processed 1 documents from https://www.dnr.wa.gov/programs-and-services/geology/geologic-hazards/tsunamis#preparation-and-evacuation.4
INFO:rag_system:Successfully processed 1 documents from https://www.dnr.wa.gov/programs-and-services/geology/geologic-hazards/tsunamis#tsunami-evacuation-maps
INFO:rag_system:Successfully processed 1 documents from https://www.dnr.wa.gov/programs-and-services/geology/geologic-hazards/tsunamis#tsunami-hazard-maps
INFO:rag_system:Successfully processed 1 documents from https://www.dnr.wa.gov/programs-and-services/geology/geologic-hazards/tsunamis#tsunami-simulation-videos
INFO:rag_system:Successfully processed 1 documents from https://www.dnr.wa.gov/programs-and-services/geology/geologic-hazards/tsunamis#tsunami-alerts
INFO:rag_system:Successfully processed 1 documents from https://www.dnr.wa.gov/programs-and-services/geology/geologic-hazards/tsunamis#historical-tsunamis-worldwide
INFO:rag_system:Successfully processed 1 documents from https://www.dnr.wa.gov/programs-and-services/geology/geologic-hazards/tsunamis#building-code-design-zone-map
INFO:rag_system:Successfully processed 1 documents from https://reliefweb.int/disaster/ts-2004-000147-idn
INFO:rag_system:Successfully processed 1 documents from https://catalog.data.gov/dataset/ncei-wds-global-historical-tsunami-database-2100-bc-to-present1#:~:text=The%20Global%20Historical%20Tsunami%20Database,database%20includes%20two%20related%20files.
INFO:rag_system:Successfully processed 1 documents from https://appliedsciences.nasa.gov/what-we-do/disasters/tsunamis
INFO:rag_system:Successfully processed 1 documents from https://tsunami.org/article-tsunami-and-science/
INFO:rag_system:Successfully processed 1 documents from https://www.britannica.com/science/tsunami
INFO:rag_system:Successfully processed 1 documents from https://www.bbc.com/news/topics/c70467809wzt
INFO:rag_system:Successfully processed 1 documents from https://www.bbc.com/news/articles/c4g3k3pr9e0o
INFO:rag_system:Successfully processed 1 documents from https://legacy.itic.ioc-unesco.org/legacy.itic.ioc-unesco.org/index464f.html?option=com_content&view=category&layout=blog&id=2767&Itemid=3406
INFO:rag_system:Successfully processed 1 documents from https://www.livescience.com/planet-earth/tsunami/tsunamis-up-to-90-feet-high-smash-into-new-zealand-every-580-years-study-finds
INFO:rag_system:Successfully processed 1 documents from https://www.livescience.com/planet-earth/tsunami/1st-mega-tsunami-on-record-since-antiquity-was-triggered-by-tonga-volcanic-eruption
INFO:rag_system:Successfully processed 1 documents from https://www.ncei.noaa.gov/products/natural-hazards/tsunamis-earthquakes-volcanoes/tsunamis/global-historical-data
INFO:rag_system:Successfully processed 1 documents from https://www.ngdc.noaa.gov/hazel/view/hazards/tsunami/event-data
ERROR:data_ingestion:Error processing URL https://rmets.onlinelibrary.wiley.com/doi/10.1002/gdj3.270: 403 Client Error: Forbidden for url: https://rmets.onlinelibrary.wiley.com/doi/10.1002/gdj3.270
WARNING:rag_system:No documents extracted from https://rmets.onlinelibrary.wiley.com/doi/10.1002/gdj3.270
ERROR:data_ingestion:Error processing URL https://tsunami.incois.gov.in/TEWS/tsunamimodeling.jsp: HTTPSConnectionPool(host='tsunami.incois.gov.in', port=443): Max retries exceeded with url: /TEWS/tsunamimodeling.jsp (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)')))
WARNING:rag_system:No documents extracted from https://tsunami.incois.gov.in/TEWS/tsunamimodeling.jsp
INFO:vector_store:Starting to process 2801 documents
INFO:vector_store:Processing document batch 1 of 1
INFO:vector_store:Using 11 CPU cores for parallel processing
Creating embeddings:   0%|                                                                                                          | 0/60 [00:00<?, ?it/s]INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:datasets:PyTorch version 2.7.1 available.
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   2%|█▌                                                                                             | 1/60 [02:04<2:02:19, 124.40s/it]INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:vector_store:Embedding progress: 1.7%
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   3%|███▎                                                                                              | 2/60 [02:05<50:23, 52.12s/it]INFO:vector_store:Embedding progress: 3.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   5%|████▉                                                                                             | 3/60 [02:13<30:12, 31.79s/it]INFO:vector_store:Embedding progress: 5.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:   7%|██████▌                                                                                           | 4/60 [02:14<18:08, 19.44s/it]INFO:vector_store:Embedding progress: 6.7%
INFO:vector_store:Embedding progress: 8.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  10%|█████████▊                                                                                        | 6/60 [02:14<08:18,  9.23s/it]INFO:vector_store:Embedding progress: 10.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  12%|███████████▍                                                                                      | 7/60 [02:16<06:23,  7.23s/it]INFO:vector_store:Embedding progress: 11.7%
INFO:vector_store:Embedding progress: 13.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  15%|██████████████▋                                                                                   | 9/60 [02:16<03:30,  4.13s/it]INFO:vector_store:Embedding progress: 15.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  17%|████████████████▏                                                                                | 10/60 [02:18<03:01,  3.62s/it]INFO:vector_store:Embedding progress: 16.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  18%|█████████████████▊                                                                               | 11/60 [02:24<03:25,  4.18s/it]INFO:vector_store:Embedding progress: 18.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  20%|███████████████████▍                                                                             | 12/60 [03:12<12:43, 15.90s/it]INFO:vector_store:Embedding progress: 20.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  22%|█████████████████████                                                                            | 13/60 [03:14<09:30, 12.14s/it]INFO:vector_store:Embedding progress: 21.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  23%|██████████████████████▋                                                                          | 14/60 [03:23<08:36, 11.23s/it]INFO:vector_store:Embedding progress: 23.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  25%|████████████████████████▎                                                                        | 15/60 [03:28<06:54,  9.22s/it]INFO:vector_store:Embedding progress: 25.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  27%|█████████████████████████▊                                                                       | 16/60 [03:29<05:08,  7.01s/it]INFO:vector_store:Embedding progress: 26.7%
INFO:vector_store:Embedding progress: 28.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  30%|█████████████████████████████                                                                    | 18/60 [03:31<02:58,  4.26s/it]INFO:vector_store:Embedding progress: 30.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  32%|██████████████████████████████▋                                                                  | 19/60 [03:32<02:21,  3.46s/it]INFO:vector_store:Embedding progress: 31.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  33%|████████████████████████████████▎                                                                | 20/60 [03:33<01:51,  2.79s/it]INFO:vector_store:Embedding progress: 33.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  35%|█████████████████████████████████▉                                                               | 21/60 [03:34<01:32,  2.38s/it]INFO:vector_store:Embedding progress: 35.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  37%|███████████████████████████████████▌                                                             | 22/60 [03:37<01:38,  2.60s/it]INFO:vector_store:Embedding progress: 36.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  38%|█████████████████████████████████████▏                                                           | 23/60 [04:24<09:23, 15.23s/it]INFO:vector_store:Embedding progress: 38.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  40%|██████████████████████████████████████▊                                                          | 24/60 [04:26<06:43, 11.21s/it]INFO:vector_store:Embedding progress: 40.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  42%|████████████████████████████████████████▍                                                        | 25/60 [04:37<06:33, 11.25s/it]INFO:vector_store:Embedding progress: 41.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  43%|██████████████████████████████████████████                                                       | 26/60 [04:41<05:09,  9.09s/it]INFO:vector_store:Embedding progress: 43.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  45%|███████████████████████████████████████████▋                                                     | 27/60 [04:43<03:49,  6.96s/it]INFO:vector_store:Embedding progress: 45.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  47%|█████████████████████████████████████████████▎                                                   | 28/60 [04:44<02:51,  5.36s/it]INFO:vector_store:Embedding progress: 46.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  48%|██████████████████████████████████████████████▉                                                  | 29/60 [04:45<01:58,  3.82s/it]INFO:vector_store:Embedding progress: 48.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  50%|████████████████████████████████████████████████▌                                                | 30/60 [04:45<01:22,  2.75s/it]INFO:vector_store:Embedding progress: 50.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  52%|██████████████████████████████████████████████████                                               | 31/60 [04:45<01:00,  2.08s/it]INFO:vector_store:Embedding progress: 51.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  53%|███████████████████████████████████████████████████▋                                             | 32/60 [04:47<00:50,  1.81s/it]INFO:vector_store:Embedding progress: 53.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  55%|█████████████████████████████████████████████████████▎                                           | 33/60 [04:47<00:38,  1.44s/it]INFO:vector_store:Embedding progress: 55.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  57%|██████████████████████████████████████████████████████▉                                          | 34/60 [05:33<06:20, 14.65s/it]INFO:vector_store:Embedding progress: 56.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  58%|████████████████████████████████████████████████████████▌                                        | 35/60 [05:35<04:33, 10.93s/it]INFO:vector_store:Embedding progress: 58.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  60%|██████████████████████████████████████████████████████████▏                                      | 36/60 [05:46<04:23, 10.98s/it]INFO:vector_store:Embedding progress: 60.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  62%|███████████████████████████████████████████████████████████▊                                     | 37/60 [05:49<03:20,  8.71s/it]INFO:vector_store:Embedding progress: 61.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  63%|█████████████████████████████████████████████████████████████▍                                   | 38/60 [05:52<02:29,  6.79s/it]INFO:vector_store:Embedding progress: 63.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  65%|███████████████████████████████████████████████████████████████                                  | 39/60 [05:56<02:07,  6.09s/it]INFO:vector_store:Embedding progress: 65.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  67%|████████████████████████████████████████████████████████████████▋                                | 40/60 [05:56<01:26,  4.30s/it]INFO:vector_store:Embedding progress: 66.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  68%|██████████████████████████████████████████████████████████████████▎                              | 41/60 [05:57<00:58,  3.07s/it]INFO:vector_store:Embedding progress: 68.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  70%|███████████████████████████████████████████████████████████████████▉                             | 42/60 [05:57<00:40,  2.25s/it]INFO:vector_store:Embedding progress: 70.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  72%|█████████████████████████████████████████████████████████████████████▌                           | 43/60 [05:59<00:35,  2.07s/it]INFO:vector_store:Embedding progress: 71.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  73%|███████████████████████████████████████████████████████████████████████▏                         | 44/60 [05:59<00:26,  1.64s/it]INFO:vector_store:Embedding progress: 73.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  75%|████████████████████████████████████████████████████████████████████████▊                        | 45/60 [06:43<03:33, 14.25s/it]INFO:vector_store:Embedding progress: 75.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  77%|██████████████████████████████████████████████████████████████████████████▎                      | 46/60 [06:44<02:25, 10.39s/it]INFO:vector_store:Embedding progress: 76.7%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  78%|███████████████████████████████████████████████████████████████████████████▉                     | 47/60 [06:54<02:12, 10.23s/it]INFO:vector_store:Embedding progress: 78.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  80%|█████████████████████████████████████████████████████████████████████████████▌                   | 48/60 [07:00<01:48,  9.01s/it]INFO:vector_store:Embedding progress: 80.0%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  82%|███████████████████████████████████████████████████████████████████████████████▏                 | 49/60 [07:07<01:32,  8.38s/it]INFO:vector_store:Embedding progress: 81.7%
Creating embeddings:  83%|████████████████████████████████████████████████████████████████████████████████▊                | 50/60 [07:07<00:59,  5.91s/it]INFO:vector_store:Embedding progress: 83.3%
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cpu
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Creating embeddings:  85%|██████████████████████████████████████████████████████████████████████████████████▍              | 51/60 [07:09<00:41,  4.61s/it]INFO:vector_store:Embedding progress: 85.0%
Creating embeddings:  87%|████████████████████████████████████████████████████████████████████████████████████             | 52/60 [07:10<00:27,  3.44s/it]INFO:vector_store:Embedding progress: 86.7%
Creating embeddings:  88%|█████████████████████████████████████████████████████████████████████████████████████▋           | 53/60 [07:11<00:19,  2.76s/it]INFO:vector_store:Embedding progress: 88.3%
Creating embeddings:  90%|███████████████████████████████████████████████████████████████████████████████████████▎         | 54/60 [07:14<00:17,  2.96s/it]INFO:vector_store:Embedding progress: 90.0%
Creating embeddings:  92%|████████████████████████████████████████████████████████████████████████████████████████▉        | 55/60 [07:14<00:10,  2.15s/it]INFO:vector_store:Embedding progress: 91.7%
Creating embeddings:  93%|██████████████████████████████████████████████████████████████████████████████████████████▌      | 56/60 [07:15<00:06,  1.61s/it]INFO:vector_store:Embedding progress: 93.3%
Creating embeddings:  95%|████████████████████████████████████████████████████████████████████████████████████████████▏    | 57/60 [07:28<00:15,  5.23s/it]INFO:vector_store:Embedding progress: 95.0%
Creating embeddings:  97%|█████████████████████████████████████████████████████████████████████████████████████████████▊   | 58/60 [07:29<00:07,  3.73s/it]INFO:vector_store:Embedding progress: 96.7%
Creating embeddings:  98%|███████████████████████████████████████████████████████████████████████████████████████████████▍ | 59/60 [07:32<00:03,  3.58s/it]INFO:vector_store:Embedding progress: 98.3%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 60/60 [07:33<00:00,  2.85s/it]INFO:vector_store:Embedding progress: 100.0%
Creating embeddings: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 60/60 [07:33<00:00,  7.56s/it]
INFO:vector_store:Processed 1000 chunks so far
INFO:vector_store:Processed 2000 chunks so far
INFO:vector_store:Processed 3000 chunks so far
INFO:vector_store:Processed 4000 chunks so far
INFO:vector_store:Processed 5000 chunks so far
INFO:vector_store:Processed 5907 chunks so far
INFO:vector_store:Completed processing 2801 documents into 5907 chunks
INFO:rag_system:Successfully ingested 2801 documents for tsunami
WARNING:__main__:Some sources failed to process: 2
INFO:__main__:System updated successfully!
INFO:__main__:New documents processed: 15093
INFO:__main__:Successful sources: 2
INFO:__main__:Failed sources: 2
INFO:__main__:Setup completed successfully!
INFO:__main__:You can now run: streamlit run streamlit_app.py
INFO:__main__:Setup completed successfully!
