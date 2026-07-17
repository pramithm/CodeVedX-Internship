"""
# Prediction Module
"""

import os
import pickle

from src.preprocessing import TextPreprocessor  # noqa: F401 — must be importable for pickle

# ---------------------------------------------------------------------------
# Resolve the model path relative to THIS file so the app works correctly
# regardless of the current working directory (local, Docker, Vercel, etc.)
# ---------------------------------------------------------------------------
_HERE = os.path.dirname(os.path.abspath(__file__))          # src/
_ROOT = os.path.dirname(_HERE)                               # project root
_MODEL_PATH = os.path.join(_ROOT, "model", "fake_news_pipeline.pkl")

# Load the trained pipeline once at import time.
# A clear RuntimeError is raised if the model file is missing so the problem
# is immediately obvious in server logs rather than surfacing as a cryptic
# AttributeError later.
try:
    with open(_MODEL_PATH, "rb") as _f:
        pipeline = pickle.load(_f)
except FileNotFoundError:
    raise RuntimeError(
        f"Model file not found at: {_MODEL_PATH}\n"
        "Run `python -m src.train_model` from the project root to generate it."
    )


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