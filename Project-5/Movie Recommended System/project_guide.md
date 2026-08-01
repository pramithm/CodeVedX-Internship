# 🎬 Movie Recommendation System — Comprehensive Project Guide

This guide provides a complete, beginner-friendly technical explanation of the **Movie Recommendation System** project. It covers the dataset origins, external API integrations, machine learning pipeline, file structure, and step-by-step setup procedure.

---

## 📌 1. Project Overview

The **Movie Recommendation System** is a **Content-Based Recommender** web application built with Python. When a user selects a movie, the system analyzes textual attributes (plot summary, genres, keywords, top cast, and director) to find and display the **top 6 most similar movies** along with their official poster artwork.

---

## 📊 2. Dataset Information

### **Source**
- **Dataset Name:** TMDB 5000 Movie Dataset
- **Origin:** [Kaggle - TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

### **Raw Files Used During Training:**
1. `tmdb_5000_movies.csv`: Contains metadata for 4,803 movies (budget, genres, homepage, keywords, overview, popularity, production companies, release date, revenue, runtime, vote average, vote count).
2. `tmdb_5000_credits.csv`: Contains metadata for cast and crew across movies.

### **Features Selected for Model:**
- **`movie_id`**: Unique TMDB identifier (essential for API queries).
- **`title`**: Movie name.
- **`overview`**: Brief plot summary.
- **`genres`**: Categories (Action, Sci-Fi, Comedy, etc.).
- **`keywords`**: Subject matter tags associated with the plot.
- **`cast`**: Top 3 lead actors/actresses.
- **`crew`**: Director of the film.

---

## 🌐 3. Poster Fetching API

### **API Provider**
- **Service:** The Movie Database (TMDB) API v3
- **Base URL:** `https://api.themoviedb.org/3/movie/{movie_id}`
- **Authentication:** API Key (`89214b375dd9a15327af92e478c5bff3`)

### **Poster Retrieval Workflow:**
1. The app takes the `movie_id` of a recommended movie.
2. Sends an HTTP `GET` request to TMDB API:
   ```
   https://api.themoviedb.org/3/movie/{movie_id}?api_key=89214b375dd9a15327af92e478c5bff3&language=en-US
   ```
3. Parses JSON response for `poster_path` (e.g., `/5iTwPDNtvK6ZZF607BHBbU3HO0B.jpg`).
4. Appends `poster_path` to TMDB's CDN image URL:
   ```
   https://image.tmdb.org/t/p/w500/5iTwPDNtvK6ZZF607BHBbU3HO0B.jpg
   ```
5. **Fail-Safe Fallback:** If the network request fails or TMDB resets the connection, the application catches the exception and returns a fallback poster (`https://placehold.co/500x750/28282B/FFF?text=No+Poster`) to prevent the web app from crashing.

---

## 🤖 4. Machine Learning Architecture

The system uses **Content-Based Filtering** powered by **Natural Language Processing (NLP)**.

```
[Raw Data] ➔ [Data Merging & Cleaning] ➔ [Feature Extraction] ➔ [Stemming] ➔ [Vectorization] ➔ [Cosine Similarity] ➔ [Pickle Export]
```

### **Step 1: Data Merging & Preprocessing**
- Datasets are merged on the `title` column.
- Missing values in `overview` are filled with empty strings.
- JSON strings (`genres`, `keywords`, `cast`, `crew`) are evaluated using `ast.literal_eval`.
- Multi-word tokens are collapsed (e.g., "Sam Worthington" ➔ "SamWorthington", "Science Fiction" ➔ "ScienceFiction") to avoid splitting full names into separate tokens.

### **Step 2: Tag Creation**
All 5 attributes are concatenated into a single string column called `tags`:
$$\text{tags} = \text{overview} + \text{genres} + \text{keywords} + \text{cast} + \text{crew}$$

### **Step 3: Text Stemming**
Uses `nltk.stem.porter.PorterStemmer` to convert words to base root forms (e.g., `"loved"`, `"loving"`, `"loves"` ➔ `"love"`).

### **Step 4: Vectorization (Bag-of-Words)**
`CountVectorizer` from `scikit-learn` converts text tags into 5,000-dimensional numerical vectors:
- `max_features=5000`: Selects the 5,000 most frequent unique words across the entire corpus.
- `stop_words='english'`: Excludes common English stop words (`in`, `the`, `and`).

### **Step 5: Cosine Similarity Metric**
Computes the cosine of the angle between vectors to evaluate similarity:
$$\text{similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}$$
This produces a $4809 \times 4809$ matrix where each element $(i, j)$ represents the similarity score between movie $i$ and movie $j$.

---

## 📂 5. Directory & File Explanation

```
Movie Recommended System/
├── app.py                         # Web Application Script (Streamlit)
├── movie_recommendation_system.py # ML Model Training & Preprocessing Script
├── movies.pkl                     # Processed Movies DataFrame (Pickled)
├── similarity.pkl                 # Cosine Similarity Matrix (Pickled)
├── requirements.txt               # Required Python Libraries
├── README.md                      # GitHub Repository Summary
├── project_guide.md               # Detailed Technical & Developer Guide
├── venv/                          # Isolated Virtual Environment Folder
└── Screenshots/                   # Project Screenshots / Visual Assets
```

### **File Details:**

- **`app.py`**:
  - The main user interface script.
  - Loads `movies.pkl` and `similarity.pkl`.
  - Implements UI using Streamlit widgets (`st.selectbox`, `st.button`, `st.columns`).
  - Calls `fetch_poster(movie_id)` to retrieve artwork dynamically.
  - Features custom CSS glassmorphism & background animated elements.

- **`movie_recommendation_system.py`**:
  - The end-to-end Machine Learning pipeline script.
  - Loads raw CSV datasets (`tmdb_5000_movies.csv`, `tmdb_5000_credits.csv`).
  - Cleans data, creates tags, performs vectorization, computes similarity, and dumps `.pkl` files.

- **`movies.pkl`**:
  - Pickled Pandas DataFrame containing `movie_id`, `title`, and `tags`.

- **`similarity.pkl`**:
  - Pickled $4809 \times 4809$ NumPy array storing pairwise similarity values.

- **`requirements.txt`**:
  - Lists essential Python packages (`streamlit`, `pandas`, `scikit-learn`, `requests`, `nltk`).

---

## 🛠️ 6. How to Run & Execute the Project

### **Step 1: Open Terminal in Project Directory**
Navigate to the project root directory:
```bash
cd "c:\Users\HOME\Desktop\CodeVedX Internship\Project-5\Movie Recommended System"
```

### **Step 2: Activate Virtual Environment**
- **Windows (CMD / PowerShell):**
  ```cmd
  venv\Scripts\activate
  ```

### **Step 3: Install Required Dependencies (If not installed)**
```bash
pip install -r requirements.txt
```

### **Step 4: Launch Streamlit Web Application**
⚠️ **Crucial Note:** Streamlit applications must be executed using `streamlit run`, NOT `python app.py`.

```bash
streamlit run app.py
```
Or directly via virtual environment Python:
```bash
.\venv\Scripts\python.exe -m streamlit run app.py
```

### **Step 5: Access Web Interface**
The browser will automatically load:
```
http://localhost:8501
```

---

## ❓ 7. Frequently Asked Questions & Troubleshooting

### **Q1: Why does `python app.py` fail with warnings?**
**Answer:** `app.py` relies on Streamlit's runtime engine. Running standard `python app.py` executes without creating a web context. Always use `streamlit run app.py`.

### **Q2: Why does `venv\Scripts\activate` say "path specified not found"?**
**Answer:** You must be inside the `Movie Recommended System` directory before running `venv\Scripts\activate`.

### **Q3: What happens if movie posters fail to load?**
**Answer:** The app uses error handling around TMDB API calls. If your network or TMDB API rate-limits requests, fallback placeholder images will display automatically without crashing the app.
