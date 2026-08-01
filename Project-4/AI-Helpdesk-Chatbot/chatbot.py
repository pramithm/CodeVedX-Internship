import os
import json
import pickle
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "chatbot_pipeline.pkl")
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "intents.json")

# Load the trained pipeline
with open(MODEL_PATH, "rb") as file:
    pipeline = pickle.load(file)


# Load intents dataset
with open(DATASET_PATH, "r", encoding="utf-8") as file:
    data = json.load(file)


# Create Prediction Function
def get_response(user_message):

    # Predict the intent
    predicted_tag = pipeline.predict([user_message])[0]

    # Find matching intent and return a random response
    for intent in data["intents"]:
        if intent["tag"] == predicted_tag:
            return random.choice(intent["responses"])

    # Default response (should rarely happen)
    return "Sorry, I couldn't understand your question."


# Test the chatbot
if __name__ == "__main__":

    print("=== AI Helpdesk Chatbot ===")
    print("Type 'quit' to exit.\n")

    while True:

        message = input("You: ")

        if message.lower() == "quit":
            print("Bot: Goodbye!")
            break

        reply = get_response(message)

        print("Bot:", reply)    