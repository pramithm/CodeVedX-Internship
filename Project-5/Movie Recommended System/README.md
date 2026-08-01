# 🎬 Movie Recommendation System

A Machine Learning-powered Content-Based Movie Recommendation System built with Python, Scikit-learn, and Streamlit. The application recommends top 6 similar movies based on plot overview, genres, keywords, top cast, and director, featuring dynamic poster fetching from The Movie Database (TMDB) API.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=for-the-badge&logo=pandas&logoColor=white)

---

## 🌟 Features

- **Content-Based Filtering**: Natural Language Processing (NLP) pipeline utilizing Stemming, Bag-of-Words Vectorization, and Cosine Similarity.
- **Dynamic Poster Fetching**: Integrates TMDB API v3 to load high-resolution movie posters automatically.
- **Resilient & Fail-Safe**: Integrated error handling and fallback mechanism for network resilience.
- **Modern UI**: Styled with dark mode theme and floating ambient backdrop animation.

---

## 📁 Repository Structure

```
Movie Recommended System/
│
├── app.py                         # Streamlit Web Application Interface
├── movie_recommendation_system.py # ML Pipeline (Preprocessing, Vectorization, Matrix Generation)
├── movies.pkl                     # Processed Movie Dataset (Pickle Binary)
├── similarity.pkl                 # Precomputed Cosine Similarity Matrix (Pickle Binary)
├── requirements.txt               # Dependencies & Library Versions
├── project_guide.md               # Detailed Architecture & Developer Guide
└── Screenshots/                   # UI Showcase & Application Screenshots
```

---

## ⚡ Quick Start Guide

### 1. Prerequisites
Ensure Python 3.9+ is installed on your system.

### 2. Activate Virtual Environment
```bash
# Windows (CMD / PowerShell)
.\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch Application
```bash
streamlit run app.py
```
The application will open automatically in your browser at `http://localhost:8501`.

---

## 📖 Comprehensive Documentation

For a full breakdown of the ML pipeline, dataset origin, TMDB API details, directory structure, and step-by-step developer guide, refer to [project_guide.md](file:///c:/Users/HOME/Desktop/CodeVedX%20Internship/Project-5/Movie%20Recommended%20System/project_guide.md).