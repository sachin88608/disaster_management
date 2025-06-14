"""
Evaluation dataset for RAGAS metrics.
This dataset contains questions, contexts, answers, and ground truths for evaluating RAG system performance.
"""

EVALUATION_DATASET = [
    {
        "question": "What are the main causes of floods?",
        "contexts": [
            "Floods are caused by heavy rainfall, poor drainage, or dam failure.",
            "Climate change increases flood frequency and intensity.",
            "Urban development and deforestation can worsen flood impacts."
        ],
        "answer": "Floods are caused by rainfall, poor drainage, or broken dams.",
        "ground_truth": "Floods occur due to excessive rain, poor water management, and dam failures."
    },
    {
        "question": "How do earthquakes affect infrastructure?",
        "contexts": [
            "Earthquakes can cause severe damage to buildings, bridges, and roads.",
            "The intensity of damage depends on the magnitude and depth of the earthquake.",
            "Poorly constructed buildings are most vulnerable to earthquake damage."
        ],
        "answer": "Earthquakes damage buildings and roads, especially if they're not built to withstand shaking.",
        "ground_truth": "Earthquakes can severely damage infrastructure, with the extent of damage depending on construction quality and earthquake magnitude."
    },
    {
        "question": "What are the warning signs of a tsunami?",
        "contexts": [
            "Tsunamis are often preceded by strong earthquakes near coastal areas.",
            "The ocean may recede significantly before a tsunami wave arrives.",
            "Unusual ocean behavior and loud ocean roars can indicate an approaching tsunami."
        ],
        "answer": "Look for earthquakes, ocean receding, and strange ocean sounds as tsunami warnings.",
        "ground_truth": "Warning signs include coastal earthquakes, unusual ocean recession, and abnormal ocean sounds."
    },
    {
        "question": "How can communities prepare for natural disasters?",
        "contexts": [
            "Develop emergency response plans and conduct regular drills.",
            "Create emergency supply kits with food, water, and medical supplies.",
            "Establish early warning systems and evacuation routes.",
            "Train community members in first aid and emergency response."
        ],
        "answer": "Communities should have emergency plans, supply kits, and trained responders ready.",
        "ground_truth": "Effective disaster preparation includes emergency planning, supply stockpiling, warning systems, and community training."
    },
    {
        "question": "What role does climate change play in natural disasters?",
        "contexts": [
            "Climate change increases the frequency and intensity of extreme weather events.",
            "Rising temperatures contribute to more severe storms and flooding.",
            "Changing precipitation patterns affect drought and flood risks.",
            "Sea level rise increases coastal flooding and storm surge impacts."
        ],
        "answer": "Climate change makes weather events more severe and frequent, affecting floods and storms.",
        "ground_truth": "Climate change intensifies natural disasters by increasing extreme weather frequency, severity, and changing precipitation patterns."
    }
]

# Additional test cases for specific disaster types
EARTHQUAKE_EVALUATION = [
    {
        "question": "What is the Richter scale used for?",
        "contexts": [
            "The Richter scale measures earthquake magnitude on a logarithmic scale.",
            "Each whole number increase represents a tenfold increase in amplitude.",
            "The scale was developed by Charles Richter in 1935."
        ],
        "answer": "The Richter scale measures how strong earthquakes are, with each number being 10 times stronger than the last.",
        "ground_truth": "The Richter scale is a logarithmic scale that measures earthquake magnitude, with each whole number representing a tenfold increase in amplitude."
    },
    {
        "question": "How do aftershocks differ from main earthquakes?",
        "contexts": [
            "Aftershocks are smaller earthquakes that follow the main earthquake.",
            "They occur in the same region as the main shock.",
            "Aftershocks can continue for days, weeks, or even months.",
            "They help relieve stress in the surrounding rock."
        ],
        "answer": "Aftershocks are smaller quakes that happen after the main earthquake in the same area.",
        "ground_truth": "Aftershocks are smaller earthquakes that follow the main earthquake in the same region, helping to relieve remaining stress in the Earth's crust."
    }
]

FLOOD_EVALUATION = [
    {
        "question": "What is flash flooding?",
        "contexts": [
            "Flash floods occur within 6 hours of heavy rainfall.",
            "They can develop in areas with poor drainage or steep terrain.",
            "Flash floods are particularly dangerous due to their rapid onset.",
            "They can carry debris and cause significant damage."
        ],
        "answer": "Flash floods happen quickly after heavy rain, often in areas with poor drainage.",
        "ground_truth": "Flash floods are rapid-onset floods that occur within 6 hours of heavy rainfall, particularly in areas with poor drainage or steep terrain."
    },
    {
        "question": "How do flood warning systems work?",
        "contexts": [
            "Flood warning systems monitor rainfall and river levels.",
            "They use weather forecasts and historical data.",
            "Warnings are issued through various communication channels.",
            "Systems can predict flood timing and severity."
        ],
        "answer": "Flood warning systems watch rain and river levels to predict and warn about floods.",
        "ground_truth": "Flood warning systems monitor rainfall and river levels, using weather forecasts and historical data to predict and communicate flood risks."
    }
]

# Combine all evaluation datasets
FULL_EVALUATION_DATASET = EVALUATION_DATASET + EARTHQUAKE_EVALUATION + FLOOD_EVALUATION 