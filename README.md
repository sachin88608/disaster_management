Open CMD
Activate Virtual env

1. Place the data in the respective folder under data folder
2. In the config.py file, add the resolurce with path if the data present in data folder then the path is like : 'data/your_new_flood_data.csv'
3. Then run the setup_data.py
4. Then run the streamlit run streamlit_app.py 


Github link : https://github.com/sachin88608/disaster_management

LLMS :-- 

llama3-70b-8192 (default, as per your config)
mixtral-8x7b-32768
llama2-13b-4096

embeddings :--
all-MiniLM-L6-v2 model from sentence-transformers for embeddings.

vector DB :--
ChromaDB

evaluation metrics for RAG/LLM systems:

- ROUGE / BLEU: For comparing generated text to reference answers.
- F1 Score / Precision / Recall: For fact-based Q&A.
- Faithfulness/Correctness: Human or automated checks if the answer is grounded in retrieved documents.
- Context Recall: Percentage of relevant context retrieved.
- Answer Relevance: Human or model-based scoring of answer relevance.
- RAGAS: A library specifically for RAG evaluation 1

Tip:
You have ragas==0.1.0 in your requirements.txt, so you could use it for RAG evaluation if you want to add metrics!

dataset collection with 4 folders 
implement classic rag with 5 different groq open source model
find out common metrics 
find out groq specific models 
which vector database i have to use for embedding and faster response??



prompt : last 100 yrs historical dataset for worldwide disaster data - floods, earthquakes, hurricanes, tornadoes, volcanic eruptions, droughts, wildfires, covid 
Gemini 
claudi
chatgpt
perplexity.ai
deepseek


data collection
store in vector db
cosine similarity----



TO DO : 
TRY with llama3-70b-8192 == 3.2 as well 
all-MiniLM-L6-v2 == try with L12
use embedding model = bge-small
optimize code like create urls in json file

add -- ahmedabad plan crash 12th june 2025 in the data -upload all possible data
use RAGAS for evaluation metrics.

----------------------------------
RAGAS - TOOL which gives us 4 metrics

First Exp
llama3-70b-8192   all-MiniLM-L6-v2

second exp
llama3-70b-8192   all-MiniLM-L12-v2

third Exp
mixtral-8x7b-32768   all-MiniLM-L6-v2

fourth exp
mixtral-8x7b-32768   all-MiniLM-L12-v2


------------------------------------
which disaster you want to select: include plane crash - lastest disaster ahmnedabad 

---------------------------------
remove respose details from UI




TASK
1. RAGAS IMPLEMENT - for evaluation use test_ragas.py
2. ADD DATASETS FOR 4 DISASTERS - flood, earthquake, plane crash, tsunami
3. DO EXP. AND GET RAGAS METRICS AND SAVE IN THE EXCEL SHEET.
