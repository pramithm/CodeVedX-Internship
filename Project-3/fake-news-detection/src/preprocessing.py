"""
# Importing Dependences
"""

import os
import re  # re-Regular Expression, Helps in searching words in a text or paragraph,to search, extract, modify, and validate text data

import nltk
from nltk.corpus import stopwords  # Natural Language Toolkit help to remove unwanted words like (a,an,is,the,and,this,that,those)
from nltk.stem.porter import PorterStemmer  # It gives the root word such as for words like Loving, Lover, Loved, Lovable the root word is Love it will convert into root word

# Point NLTK at the bundled nltk_data/ directory in the project root.
# This allows the app to run on read-only filesystems (e.g. Vercel) without
# calling nltk.download() at runtime.
_BUNDLE = os.path.join(os.path.dirname(__file__), "..", "nltk_data")
if os.path.isdir(_BUNDLE):
    nltk.data.path.insert(0, os.path.abspath(_BUNDLE))

# So this are the stops words which are not useful in our dataset we will try to remove these words.
STOP_WORDS = set(stopwords.words('english'))

# Stemming the words(Converting to its root words)
port_stem = PorterStemmer()

# Creating a function
def stemming(content):
    # It removes {nums, commas, quotes} and replace with space
    stemming_content = re.sub('[^a-zA-Z]', ' ', str(content))

    # converting into lower case for best results
    stemming_content = stemming_content.lower()

    # Splitting the words
    stemming_content = stemming_content.split()

    # converting stemming words excluding the stops word like a,the,is,and,or
    stemming_content = [
        port_stem.stem(word)
        for word in stemming_content
        if word not in STOP_WORDS
    ]

    stemmed_content = ' '.join(stemming_content)

    return stemmed_content

from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class TextPreprocessor(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        if isinstance(X, pd.Series):
            return X.apply(stemming)

        return [stemming(text) for text in X]