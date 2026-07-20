# 🔍 TruthLens AI — Fake News Detection System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.3-black?logo=flask&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.9.0-orange?logo=scikit-learn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-3.10.0-green?logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

> An AI-powered web application that classifies news articles as **REAL** or **FAKE** using Natural Language Processing and Machine Learning — complete with a confidence score and risk meter.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [How It Works](#-how-it-works)
- [Installation & Setup](#-installation--setup)
- [Running the App](#-running-the-app)
- [Usage Guide](#-usage-guide)
- [Testing Examples](#-testing-examples)
- [Model Performance](#-model-performance)
- [API Reference](#-api-reference)

---

##  🔗[Demo Link:] Click Here (https://fake-news-predict.vercel.app/)

---

---

## 🧠 Overview

**TruthLens AI** is a machine learning web application built with Flask that detects misinformation in news articles. It uses a trained **Logistic Regression** model with **TF-IDF vectorization** and **NLP preprocessing** (stemming + stopword removal) to classify text as real or fake, along with a **confidence percentage** indicating how certain the model is.

The model was trained on ~6,300 real-world US political news articles, balanced equally between real and fake news sources.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎯 **Real / Fake Classification** | Instantly classifies any news article or headline |
| 📊 **Confidence Score** | Shows model certainty as a percentage (0–100%) |
| ⚠️ **Risk Level** | HIGH / MED / LOW risk label based on confidence |
| 🌈 **Visual Risk Meter** | 20-segment animated bar colored green → red |
| 🧪 **Quick Examples** | Built-in example pills to test the model instantly |
| 📰 **Text Preview** | Displays analyzed text inside the result card |
| ⚡ **Real-time Analysis** | Sub-second predictions using pre-loaded pipeline |
| 🌾 **Warm UI Design** | Clean cream/amber themed web interface |

---

## 📁 Project Structure

```
fake-news-detection/
│
├── app.py                      # Flask application entry point
│
├── src/
│   ├── __init__.py             # Package initializer
│   ├── preprocessing.py        # Text cleaning: stemming + stopword removal
│   ├── train_model.py          # Model training script (run once)
│   ├── predict.py              # Prediction function used by the app
│   └── test.py                 # Quick CLI test script
│
├── model/
│   └── fake_news_pipeline.pkl  # Trained sklearn Pipeline (saved model)
│
├── data/
│   └── news.csv                # Training dataset (~6,335 articles)
│
├── templates/
│   └── index.html              # Jinja2 HTML template (frontend)
│
├── static/
│   └── style.css               # All CSS styles
│
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.10+, Flask 3.1 |
| **ML Model** | Scikit-learn — Logistic Regression |
| **Vectorizer** | TF-IDF (Term Frequency–Inverse Document Frequency) |
| **NLP** | NLTK — Porter Stemmer + Stopword Removal |
| **Frontend** | HTML5, Vanilla CSS, JavaScript (no frameworks) |
| **Templating** | Jinja2 |
| **Model Storage** | Python Pickle (`.pkl`) |

---

## ⚙️ How It Works

```
User Input (news text)
        │
        ▼
┌──────────────────────┐
│  Text Preprocessing  │  ← Remove punctuation, lowercase,
│  (preprocessing.py)  │    remove stopwords, apply stemming
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  TF-IDF Vectorizer   │  ← Convert cleaned text into
│                      │    numerical feature matrix
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Logistic Regression  │  ← Classify as REAL (1) or FAKE (0)
│     Classifier       │    Output: label + probability scores
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Flask Web App      │  ← Return result, confidence %, risk level
│   (app.py)           │    Render result card in browser
└──────────────────────┘
```

### NLP Preprocessing Pipeline (step by step)

```
Input:  "Scientists Discover shocking Truth About Vaccines!"

Step 1 — Remove non-alpha characters:
         "Scientists Discover shocking Truth About Vaccines "

Step 2 — Lowercase:
         "scientists discover shocking truth about vaccines"

Step 3 — Remove stopwords (a, the, is, about...):
         "scientists discover shocking truth vaccines"

Step 4 — Porter Stemming (root words):
         "scientist discov shock truth vaccin"

Output:  "scientist discov shock truth vaccin"
```

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.10 or higher
- pip package manager

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fake-news-detection.git
cd fake-news-detection
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model *(skip if `model/fake_news_pipeline.pkl` already exists)*

```bash
python -m src.train_model
```

Expected output:
```
Dataset Shape: (6335, 4)
Accuracy on training data: 0.9843
Accuracy on testing data:  0.9216
Model saved successfully inside model/fake_news_pipeline.pkl
```

---

## ▶️ Running the App

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

> **Note:** Make sure your virtual environment is activated before running.

---

## 📖 Usage Guide

### Web Interface

1. **Open** `http://127.0.0.1:5000` in your browser
2. **Paste** a news article or headline into the text box
3. **Click** `Analyze Article`
4. **View** the result:
   - ✅ `REAL` — Likely authentic news
   - ❌ `FAKE` — Likely misinformation
   - Confidence score (e.g. `94.72%`)
   - Risk level: `HIGH`, `MED`, or `LOW`
   - Visual confidence bar and risk spectrum meter

### Command Line (Quick Test)

```bash
python -m src.test
```

Or write your own test:

```python
from src.predict import predict_news

news = "Your news article text here..."
prediction, confidence = predict_news(news)

print(f"Prediction : {prediction}")   # REAL or FAKE
print(f"Confidence : {confidence}%")  # e.g. 94.72
```

---

## 🧪 Testing Examples

> ⚠️ **Important:** This model was trained on **US political news from 2015–2017**.
> It works best with political articles in English. The model classifies based on
> **writing style and vocabulary**, not the topic alone.

---

### ✅ REAL News Examples

These are typical of wire-service reporting (Reuters, AP, CNN) — neutral tone, named sources, specific dates and numbers.

---

**Example 1** *(John Kerry / Paris)*
```
Kerry to go to Paris in gesture of sympathy.

U.S. Secretary of State John F. Kerry said Monday that he will stop
in Paris later this week, amid criticism that no top American officials
attended Sunday's unity march against terrorism.
```
> **Expected:** ✅ REAL · ~95% confidence

---

**Example 2** *(Trump & Fox News)*
```
Trump Will Skip GOP Debate As Feud With Fox News Boils Over.

The stage is set for Thursday's Fox News Channel final debate ahead
of the Iowa caucuses, but Donald Trump will not be on stage. Trump
announced he is boycotting the debate, saying Fox News has treated
him unfairly throughout the campaign.
```
> **Expected:** ✅ REAL · ~90% confidence

---

**Example 3** *(Election reporting)*
```
Cruz, Trump and Rubio win in Iowa. It is always interesting to watch
democracy in action and Iowa is ground zero. Many political pundits
and media analysts complain about the attention Iowa receives from
candidates and the media, but the caucus results show a clear
three-way race emerging among Republican primary voters.
```
> **Expected:** ✅ REAL · ~88% confidence

---

**Example 4** *(Poll reporting)*
```
Dem insiders: Sanders failed to dent Clinton. According to a new
CNN/ORC poll, Hillary Clinton holds a commanding lead among
Democratic insiders despite Bernie Sanders' strong grassroots
fundraising and crowd sizes across the country.
```
> **Expected:** ✅ REAL · ~91% confidence

---

### ❌ FAKE News Examples

These are typical of political blogs and partisan clickbait sites — emotional language, ALL CAPS, vague sourcing, sensational claims.

---

**Example 1** *(Emotional attack language)*
```
You Can Smell Hillary's Fear.

The establishment is absolutely TERRIFIED because the American people
are waking up to the TRUTH and the mainstream media is doing
everything it can to stop this information from spreading!
Share this before it gets deleted!
```
> **Expected:** ❌ FAKE · ~92% confidence

---

**Example 2** *(Clickbait headline style)*
```
Watch The EXACT Moment Paul Ryan Committed Political Suicide At A
Trump Rally (VIDEO). The Republican speaker has betrayed his own
party and the American people will NOT forget this. The establishment
elites think they can fool us but they are DEAD WRONG. This video
is going viral and they want it taken down!
```
> **Expected:** ❌ FAKE · ~94% confidence

---

**Example 3** *(Conspiracy tone)*
```
CNN Reaches New Low, Calls Sheriff Clarke A 'Terrorist' After Trump
Gave Him The Most Important Job! President Trump has given very hard
thought into who will be in his Cabinet. The mainstream media doesn't
want you to know this and they will do ANYTHING to stop it.
Too bad — America is taking its country back! Share if you agree!
```
> **Expected:** ❌ FAKE · ~96% confidence

---

**Example 4** *(Vague sourcing + hyperbole)*
```
Bernie supporters on Twitter erupt in anger against the DNC:
'We tried to warn you!' Thousands of grassroots activists flooded
social media with outrage after leaked documents revealed what many
had long suspected — the Democratic establishment rigged the entire
primary process against Sanders from day one!
```
> **Expected:** ❌ FAKE · ~89% confidence

---

### 🚦 Classification Signals — What the Model Looks For

| Signal | Points to REAL | Points to FAKE |
|---|---|---|
| **Tone** | Neutral, factual | Emotional, outraged |
| **Verbs** | "said", "reported", "announced" | "exposes", "reveals TRUTH", "caught" |
| **Language** | Balanced, measured | "SHOCKING", "MUST SHARE", "They won't tell you" |
| **Sources** | Named people, institutions | Vague — "sources say", "many believe" |
| **Numbers** | Specific stats, dates, percentages | Round numbers, exaggerated claims |
| **Punctuation** | Normal sentence structure | Excessive `!!!`, ALL CAPS words |
| **Structure** | Full paragraphs, inverted pyramid | Short rant + emotional call to action |

---

### ⚠️ Inputs That May Give Unexpected Results

| Input Type | Reason |
|---|---|
| Science / health news | Out of training domain |
| Sports / entertainment | Not in training data |
| Very short text (< 15 words) | Insufficient TF-IDF signal |
| News from 2020+ | Different political vocabulary |
| Non-English text | Model trained on English only |
| Indian / regional news | Training data is US-centric |

> 💡 **Pro Tip:** Always include **both a headline and a body paragraph** for best
> results. The model was trained on `title + text` combined, so short
> one-liners may give lower confidence scores.

---

## 📈 Model Performance

| Metric | Score |
|---|---|
| **Training Accuracy** | ~98.4% |
| **Testing Accuracy** | ~92.2% |
| **Algorithm** | Logistic Regression |
| **Vectorizer** | TF-IDF |
| **Dataset Size** | 6,335 articles |
| **Class Balance** | 3,171 REAL · 3,164 FAKE |
| **Train / Test Split** | 80% / 20% (stratified) |
| **Random State** | 2 |
| **Max Iterations** | 1,000 |

---

## 🔌 API Reference

### `GET /`

Returns the home page with the input form.

**Response:** HTML page (`200 OK`)

---

### `POST /predict`

Accepts form data and returns a prediction rendered in the HTML template.

**Request Body (form-data):**

| Field | Type | Required | Description |
|---|---|---|---|
| `news` | `string` | ✅ Yes | The news article or headline to classify |

**Template Variables Returned:**

| Variable | Type | Description |
|---|---|---|
| `prediction` | `string` | `"REAL"` or `"FAKE"` |
| `confidence` | `float` | Confidence score, e.g. `94.72` |
| `news` | `string` | The original input text |
| `error` | `string` | Error message if input is empty |

**Example (Python `requests`):**

```python
import requests

url = "http://127.0.0.1:5000/predict"
payload = {"news": "Kerry to go to Paris in gesture of sympathy..."}

response = requests.post(url, data=payload)
print(response.status_code)  # 200
```

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 🙌 Acknowledgements

- Dataset sourced from [Kaggle Fake News datasets](https://www.kaggle.com/datasets)
- Built as part of the **CodeVedX Internship — Project 3**
- NLP preprocessing powered by [NLTK](https://www.nltk.org/)
- ML pipeline built with [Scikit-learn](https://scikit-learn.org/)
- Web framework by [Flask](https://flask.palletsprojects.com/)

---

<div align="center">
  Made with ❤️ &nbsp;·&nbsp; TruthLens AI &nbsp;·&nbsp; Fake News Detection System
</div>
