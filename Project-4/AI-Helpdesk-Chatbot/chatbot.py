# Import Required Libraries
import json
import pickle
import random


# Load the trained pipeline
with open("model/chatbot_pipeline.pkl", "rb") as file:
    pipeline = pickle.load(file)


# Load intents dataset
with open("dataset/intents.json", "r") as file:
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