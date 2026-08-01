# Import Required Libraries
import json
import pickle

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Load the intents dataset
with open("dataset/intents.json", "r") as file:
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
with open("model/chatbot_pipeline.pkl", "wb") as file:
    pickle.dump(pipeline, file)


print("✅ Chatbot model trained successfully!")