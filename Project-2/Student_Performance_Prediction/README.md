# 🎓 Student Performance Prediction System

A Machine Learning project that predicts a student's **final marks** based on their **attendance**, **study hours**, and **midterm marks**. The project demonstrates the complete ML workflow, from data preprocessing and exploratory analysis to model training, evaluation, and prediction through a simple GUI.

---

## 📌 Features

* 📊 Data Cleaning & Preprocessing
* 📈 Exploratory Data Analysis (EDA)
* 🎯 Feature Selection
* 🤖 Linear Regression Model
* 📉 Model Performance Evaluation
* 💾 Model Saving & Loading
* 🖥️ Simple Tkinter GUI for Predictions

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Tkinter

---

## 📂 Project Structure

```text
Student_Performance_Prediction/
│
├── data/
│   ├── student_performance.csv
│   └── student_performance_cleaned.csv
│
├── models/
│   └── model.pkl
│
├── src/
│   ├── data_preprocessing.py
│   ├── visualization.py
│   ├── train_model.py
│   └── predict.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project folder:

```bash
cd Student_Performance_Prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### 1. Preprocess the Dataset

```bash
python src/data_preprocessing.py
```

### 2. Perform Data Analysis

```bash
python src/visualization.py
```

### 3. Train the Model

```bash
python src/train_model.py
```

### 4. Predict Using the Console

```bash
python src/predict.py
```

### 5. Launch the GUI

```bash
python app.py
```

---

## 📊 Model Information

**Input Features**

* Attendance
* Study Hours
* Midterm Marks

**Target**

* Final Marks

**Algorithm**

* Linear Regression

**Evaluation Metrics**

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

---

## 📸 Screenshots

Add screenshots of:

* Data Visualization
* Model Evaluation
* Prediction Output
* GUI Application

---

## 👨‍💻 Author

**Pramith M**

CodeVedX Internship Project
