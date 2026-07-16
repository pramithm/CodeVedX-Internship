"""
# Importing Dependences
"""

from flask import Flask, render_template, request

from src.predict import predict_news

# Creating Flask Application
app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():

    # Getting news from HTML Form
    news = request.form["news"]

    # Checking Empty Input
    if not news.strip():
        return render_template(
            "index.html",
            error="Please enter news text."
        )

    # Predicting News
    prediction, confidence = predict_news(news)

    # Sending Result Back to HTML
    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        news=news
    )


# Running Flask Application
if __name__ == "__main__":
    app.run(debug=True)