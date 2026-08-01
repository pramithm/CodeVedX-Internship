import os
import json
import pickle

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "intents.json")
MODEL_PATH = os.path.join(BASE_DIR, "model", "chatbot_pipeline.pkl")


# Load the intents dataset
with open(DATASET_PATH, "r", encoding="utf-8") as file:
    data = json.load(file)


# Create empty lists
patterns = []
tags = []


# Extract patterns and tags
for intent in data["intents"]:
    tag = intent["tag"]

    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(tag)


# Create ML Pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])


# Train the model
pipeline.fit(patterns, tags)


# Save the trained pipeline
with open(MODEL_PATH, "wb") as file:
    pickle.dump(pipeline, file)


print("Chatbot model trained successfully!")