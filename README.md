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
llama3-70b-8192   all-MiniLM-L6-v2 - done

second exp
llama3-70b-8192   all-MiniLM-L12-v2

third Exp
mixtral-8x7b-32768   all-MiniLM-L6-v2

fourth exp
mixtral-8x7b-32768   all-MiniLM-L12-v2

fifth exp
llama-3.3-70b-versatile      bge-small-en-v1.5

sixth exp
llama-3.3-70b-versatile      bge-base-en-v1.5

seventh exp
llama-3.1-8b-instant      bge-small-en-v1.5

eighth exp
llama-3.1-8b-instant      bge-base-en-v1.5

------------------------------------
which disaster you want to select: include plane crash - lastest disaster ahmnedabad 

---------------------------------
remove respose details from UI




TASK
1. RAGAS IMPLEMENT - for evaluation use test_ragas.py 
2. ADD DATASETS FOR 4 DISASTERS - flood, earthquake, plane crash, tsunami - Need to add from sheed and downloads (Flood and Tsunami dataset)
3. DO EXP. AND GET RAGAS METRICS AND SAVE IN THE EXCEL SHEET.


for cursor ai : https://authenticator.cursor.sh/?client_id=client_01GS6W3C96KW4WRS6Z93JCE2RJ&redirect_uri=https%3A%2F%2Fcursor.com%2Fapi%2Fauth%2Fcallback&response_type=code&state=%257B%2522returnTo%2522%253A%2522https%253A%252F%252Fwww.cursor.com%252Fdashboard%2522%257D&authorization_session_id=01JXSBVYJ2HBPDMVTE5S5GA9ZP


python setup_data.py -- > update embeddings only the data i have added
python setup_data.py --force --> for create embeddings from scratch

For evaluation : python ragas_evaluation.py


How to run 8 exp at once :

1. python experiment_status.py --> This will show you exactly which experiments are completed and which are pending.

2. python experiment_setup.py --> This will create vector stores for all 4 embedding models:
all-MiniLM-L6-v2
all-MiniLM-L12-v2
bge-small-en-v1.5
bge-base-en-v1.5

3. python batch_experiments.py --> This will:
✅ Skip Experiment_1 (already completed)
✅ Run Experiments 2-8 automatically
✅ Save results in batch_experiment_results/
✅ Generate comparison report showing best performing experiment


🏆 BEST PERFORMING EXPERIMENT:
   Experiment_6: bge-base-en-v1.5 + llama-3.3-70b-versatile
   Average Score: 0.892


How to run exo one by one:--
1. python experiment_setup.py-->  This means creating vector stores for each embedding model that will be used in the experiments. Run:

2. python run_single_experiment.py -- > When you run the script, it will:
Ask you to enter an experiment number (1-8)
Run only that specific experiment
Show you the results immediately after completion
Save the results in the batch_experiment_results directory


The experiments are:
1. all-MiniLM-L6-v2 + llama3-70b-8192 - done
2. all-MiniLM-L12-v2 + llama3-70b-8192 - done
3. all-MiniLM-L6-v2 + mixtral-8x7b-32768 - done
4. all-MiniLM-L12-v2 + mixtral-8x7b-32768 - done
5. bge-small-en-v1.5 + llama-3.3-70b-versatile - done
6. bge-base-en-v1.5 + llama-3.3-70b-versatile - running
7. bge-base-en-v1.5 + llama-3.1-8b-instant - done
8. bge-small-en-v1.5 + llama-3.1-8b-instant - running

9. all-MiniLM-L6-v2 + llama-3.3-70b-versatile
10. all-MiniLM-L12-v2 + llama-3.3-70b-versatile
11. all-MiniLM-L6-v2 + llama-3.1-8b-instant
12. all-MiniLM-L12-v2 + llama-3.1-8b-instant
13. bge-small-en-v1.5 + llama3-70b-8192
14. bge-small-en-v1.5 + mixtral-8x7b-32768
15. bge-base-en-v1.5 + llama3-70b-8192
16. bge-base-en-v1.5 + mixtral-8x7b-32768


And the detailed results will be saved in the JSON file in the batch_experiment_results directory. You can check all your experiment results at any time using:
python experiment_status.py




Hugging Face Token for google/gemma-2b-it Evaluation model: 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
Token Generation link :  https://huggingface.co/settings/tokens
https://huggingface.co/google/gemma-2b-it
https://huggingface.co/google/gemma-2b-it



---------------------------------------------------------------------------------------------------
COMPLETE COMMAND SEQUENCE:


1. Test with Your Actual Dataset
Run --> python test_with_actual_dataset.py

2. Run Experiment Setup
Run --> python experiment_setup.py

3. Run Your 16 Experiments --(Then enter the experiment number (1-16) when prompted)
Run --> python run_single_experiment.py



Check Status Anytime
Run --> python experiment_status.py