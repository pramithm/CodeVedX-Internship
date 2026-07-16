"""
# Importing Dependences
"""

import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer  # Coverts Text into features columns also it will convert into numerical value go to google for this.
from sklearn.pipeline import Pipeline

from src.preprocessing import stemming

"""Data Pre-processing"""

# loading the dataset into pandas DataFrame, we will see in good tablular format
new_dataset = pd.read_csv("data/news.csv")

print("Dataset Shape:", new_dataset.shape)

# Checking the Missing values so here text and lable column one field is missing
print(new_dataset.isnull().sum())

# For Lable fixing use central tendency for categoral data use mode
new_dataset['label'].fillna(new_dataset['label'].mode()[0], inplace=True)

# Removing the row in text because 'text'(missing value) is a unique field is replace with mode it leads to incorrect data, and removing Unnamed columns not useful
new_dataset.drop(columns=['Unnamed: 0'], inplace=True)
new_dataset.dropna(subset=['title', 'text'], inplace=True)

# Change the column type to integer for labels
new_dataset['label'] = new_dataset['label'].replace({'FAKE': 0, 'REAL': 1}).astype(int)

# Creating new column that combines (title + text) single column
new_dataset['content'] = new_dataset['title'] + " " + new_dataset['text']

# Removing a text,title column
new_dataset.drop(columns=['title', 'text'], inplace=True)

# Spliting the dataset into X for content, Y for labels
X = new_dataset['content']
Y = new_dataset['label']

"""Spliting into train and test data"""

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    stratify=Y,
    random_state=2
)

"""Training the model using Logistic Regression"""

from src.preprocessing import TextPreprocessor

pipeline = Pipeline([
    ("preprocessor", TextPreprocessor()),
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, Y_train)

"""Evaluation

Accuracy
"""

# Accuracy on training data
X_train_prediction = pipeline.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)

print("Accuracy on training data:", training_data_accuracy)

# Accuracy on testing data
X_test_prediction = pipeline.predict(X_test)
testing_data_accuracy = accuracy_score(Y_test, X_test_prediction)

print("Accuracy on testing data:", testing_data_accuracy)

"""Saving the trained pipeline"""

with open("model/fake_news_pipeline.pkl", "wb") as file:
    pickle.dump(pipeline, file)

print("Model saved successfully inside model/fake_news_pipeline.pkl")