# CodeVedX Internship — AI/ML Engineering

A collection of five machine learning projects built during an AI/ML Engineering internship at CodeVedX. Each project is self-contained, covering a different problem domain — from regression and NLP classification to conversational AI and recommendation systems.

## Projects

| # | Project | Problem Type | Stack |
|---|---------|--------------|-------|
| 1 | [Utility Usage Prediction Tool](./Project-1/Utility_Usage_Prediction_Tool) | Regression (Linear Regression) | Python, Pandas, Scikit-learn |
| 2 | [Student Performance Prediction](./Project-2/Student_Performance_Prediction) | Regression (Linear Regression) | Python, Pandas, NumPy, Scikit-learn, Tkinter |
| 3 | [TruthLens AI — Fake News Detection](./Project-3/fake-news-detection) | NLP Classification | Python, Flask, Scikit-learn, NLTK |
| 4 | [AI HR Helpdesk Chatbot](./Project-4/AI-Helpdesk-Chatbot) | Intent Classification (NLP) | Python, Flask, Scikit-learn, NLTK |
| 5 | [Movie Recommendation System](./Project-5/Movie%20Recommended%20System) | Content-Based Recommendation | Python, Scikit-learn, Streamlit, TMDB API |

## Project Summaries

**1. Utility Usage Prediction Tool**
A console-based application that logs utility usage records and predicts future consumption with a Linear Regression model. Includes a menu-driven CLI, CSV-based storage, and input validation.

**2. Student Performance Prediction**
Predicts a student's final marks from attendance, study hours, and midterm scores. Covers the full ML workflow — cleaning, EDA, feature selection, training, and evaluation — with a Tkinter desktop GUI for live predictions.

**3. TruthLens AI — Fake News Detection**
A Flask web app that classifies news articles as REAL or FAKE using NLP preprocessing and a trained classifier, returning a confidence score and risk meter.

**4. AI HR Helpdesk Chatbot**
An intent-based chatbot for HR FAQs. Uses TF-IDF vectorization with a Logistic Regression classifier to interpret employee queries and respond in real time through a Flask web interface.

**5. Movie Recommendation System**
A content-based recommender that suggests the six most similar movies using cosine similarity over plot, genre, keyword, cast, and director data. Built with Streamlit and enriched with live poster fetching via the TMDB API.

## Repository Structure

```text
CodeVedX-Internship/
│
├── Project-1/Utility_Usage_Prediction_Tool/
├── Project-2/Student_Performance_Prediction/
├── Project-3/fake-news-detection/
├── Project-4/AI-Helpdesk-Chatbot/
├── Project-5/Movie Recommended System/
└── Task For Internship.pdf
```

Each project folder contains its own README with setup instructions, tech stack details, and usage notes.

## Getting Started

```bash
git clone https://github.com/pramithm/CodeVedX-Internship.git
cd CodeVedX-Internship/<project-folder>
pip install -r requirements.txt
```

Refer to the individual project README for the exact run command (Flask, Streamlit, or CLI).

## Author

**Pramith M** — AI/ML Engineering Intern, CodeVedX
