## 🤖 AI HR Helpdesk Chatbot (Demo) [https://aichatbot-beige-seven.vercel.app/]

An AI-powered HR Helpdesk Chatbot built using **Python, Flask, Machine Learning, and Natural Language Processing (NLP)**. The chatbot understands employee queries, predicts their intent using a trained Machine Learning model, and provides appropriate HR-related responses.

This project demonstrates how NLP can be used to automate Frequently Asked Questions (FAQs) in an organization's HR department.

---

## 🚀 Features

- Intent-based HR chatbot
- Natural Language Processing using TF-IDF
- Logistic Regression classifier
- Interactive web interface using Flask
- HR FAQ dataset
- Real-time chat responses
- Easy to customize by modifying the dataset
- Beginner-friendly project structure

---

## 🛠️ Tech Stack

- Python
- Flask
- Scikit-learn
- NLTK
- HTML
- CSS
- JavaScript
- JSON

---

## 📂 Project Structure

```
AI-HR-Helpdesk-Chatbot/

│
├── dataset/
│   └── intents.json
│
├── model/
│   └── chatbot_pipeline.pkl
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── chatbot.py
├── train.py
├── requirements.txt
└── README.md
```

---

## 🧠 Machine Learning Workflow

```
User Query
      │
      ▼
TF-IDF Vectorizer
      │
      ▼
Logistic Regression
      │
      ▼
Intent Prediction
      │
      ▼
Retrieve Response
      │
      ▼
Display Answer
```

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/AI-HR-Helpdesk-Chatbot.git

cd AI-HR-Helpdesk-Chatbot

python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Train the Model

```bash
python train.py
```

Run the Application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## 💬 Example Questions

- Hi
- How do I apply for leave?
- What are office timings?
- When is salary credited?
- I forgot my attendance
- What are employee benefits?
- How do I resign?

---

## 🎯 Future Improvements

- Confidence-based prediction
- Admin dashboard
- Database integration
- User authentication
- Chat history
- Ticket generation
- Voice support
- Generative AI integration

---

## 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository, improve the project, and submit a pull request.

---

## 📄 License

This project is developed for educational and learning purposes.

---

## 👨‍💻 Author

**Pramith Maredukonda**

AI/ML Learning & Python Developer

LinkedIn:[linkedin.com/in/pramith-maredukonda]
