# AI HR Helpdesk Chatbot

# Complete Project Documentation

---

# 1. Introduction

The AI HR Helpdesk Chatbot is an NLP-based chatbot that answers employee HR-related queries using Machine Learning.

Instead of searching through documents or contacting HR for common questions, employees can ask the chatbot directly.

Examples include:

- Leave Policy
- Salary Date
- Attendance
- Holidays
- Employee Benefits
- Work From Home
- HR Contact

The chatbot predicts the user's intent using a trained Machine Learning model and returns the corresponding response from the dataset.

---

# 2. Project Objectives

- Learn Natural Language Processing
- Understand Intent Classification
- Build a Machine Learning Pipeline
- Integrate ML with Flask
- Create a Web-based Chatbot
- Understand Client-Server Architecture

---

# 3. Technologies Used

Python

Flask

Scikit-learn

NLTK

TF-IDF Vectorizer

Logistic Regression

HTML

CSS

JavaScript

JSON

Pickle

---

# 4. Folder Structure

```
AI-HR-Helpdesk-Chatbot/

dataset/

model/

static/

templates/

app.py

chatbot.py

train.py

requirements.txt
```

---

# 5. Installation

Clone Repository

```bash
git clone https://github.com/yourusername/AI-HR-Helpdesk-Chatbot.git
```

Go into Project

```bash
cd AI-HR-Helpdesk-Chatbot
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 6. Dataset

The chatbot is trained using

```
dataset/intents.json
```

Each intent contains

- Tag
- Patterns
- Responses

Example

```json
{
    "tag":"leave_policy",

    "patterns":[
        "Leave application",
        "How do I apply leave?"
    ],

    "responses":[
        "Apply through HR Portal."
    ]
}
```

---

# 7. Training

Run

```bash
python train.py
```

The script

- Reads intents.json
- Extracts patterns
- Converts text using TF-IDF
- Trains Logistic Regression
- Saves chatbot_pipeline.pkl

---

# 8. Prediction

chatbot.py

Loads

```
chatbot_pipeline.pkl
```

Receives

```
User Question
```

Predicts

```
Intent
```

Returns

```
Response
```

---

# 9. Running the Project

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 10. Application Flow

```
Browser

↓

JavaScript

↓

Flask

↓

Chatbot

↓

Machine Learning Model

↓

Intent Prediction

↓

Dataset Response

↓

Browser
```

---

# 11. How to Add New FAQs

Open

```
dataset/intents.json
```

Add a new intent

Example

```json
{
    "tag":"canteen",

    "patterns":[
        "Where is canteen?",
        "Lunch area"
    ],

    "responses":[
        "The canteen is located on the second floor."
    ]
}
```

Train Again

```bash
python train.py
```

Restart Flask

```bash
python app.py
```

The chatbot now understands the new topic.

---

# 12. Common Errors

### ModuleNotFoundError

Install requirements

```bash
pip install -r requirements.txt
```

---

### Model File Missing

Run

```bash
python train.py
```

---

### Flask Not Starting

Check whether Flask is installed.

```bash
pip install flask
```

---

### script.js 404 Error

Ensure

```
static/script.js
```

exists.

---

# 13. Future Scope

- Confidence Score
- Admin Panel
- SQLite Database
- Authentication
- REST API
- OpenAI Integration
- Voice Assistant
- Docker Deployment
- Cloud Deployment

---

# 14. Learning Outcomes

By completing this project, you will understand

- NLP Fundamentals
- Intent Classification
- TF-IDF
- Logistic Regression
- Flask
- REST APIs
- Frontend & Backend Integration
- Machine Learning Deployment

---