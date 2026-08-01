from flask import Flask, render_template, request, jsonify

from chatbot import get_response

# Create Flask App
app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Chat API
@app.route("/chat", methods=["POST"])
def chat():

    # Get user message from frontend
    user_message = request.json.get("message")

    # Get chatbot reply
    bot_reply = get_response(user_message)

    # Return response as JSON
    return jsonify({
        "reply": bot_reply
    })


# Run the application
if __name__ == "__main__":
    app.run(debug=True)