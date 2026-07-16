"""
# Importing Dependences
"""

import pickle
from src.preprocessing import TextPreprocessor

# Loading the trained pipeline
with open("model/fake_news_pipeline.pkl", "rb") as file:
    pipeline = pickle.load(file)


# Creating Prediction Function
def predict_news(news):

    prediction = pipeline.predict([news])[0]

    probabilities = pipeline.predict_proba([news])[0]

    confidence = max(probabilities) * 100

    if prediction == 0:
        result = "FAKE"
    else:
        result = "REAL"

    return result, round(confidence, 2)