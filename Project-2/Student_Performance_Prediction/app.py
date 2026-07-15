import io
import csv
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template

from src.train_model import load_data, train_model

# Initialize Flask Application with customized template and static folders
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static"
)

# Constants
DATASET_PATH = "data/student_performance_cleaned.csv"

# ---------------------------------------------------------------------------
# In-memory model — trained once at startup, retrained via /api/train
# ---------------------------------------------------------------------------
_model = None
_train_metrics = None

def init_model():
    """Train the model from the cleaned dataset and cache it in memory."""
    global _model, _train_metrics
    data = load_data(DATASET_PATH)
    _model, _train_metrics = train_model(data)
    print("Model ready (in-memory).")

def get_model():
    """Return the cached in-memory model."""
    return _model

# Train on startup
init_model()


# Helper to generate recommendations
def generate_recommendations(prediction, attendance, study_hours, midterm_marks):
    # Grade status
    if prediction >= 90:
        category = "Excellent"
    elif prediction >= 75:
        category = "Good"
    elif prediction >= 50:
        category = "Average"
    else:
        category = "At Risk"

    # Attendance recommendations
    if attendance < 75:
        attendance_rec = "Critical Attendance: Your attendance is below the 75% requirement. Try to attend every class to understand concepts better and avoid institutional penalties."
    elif attendance < 85:
        attendance_rec = "Satisfactory Attendance: You are above the threshold, but attending more classes will directly reinforce your learning and final performance."
    else:
        attendance_rec = "Excellent Attendance: Keep up the consistent presence. This is a vital driver of your academic success."

    # Study hours recommendations
    if study_hours < 4.0:
        study_rec = "Low Study Intensity: Dedicating less than 4 hours weekly to self-study is limiting your growth. Aim for at least 5-6 structured hours per week."
    elif study_hours < 7.0:
        study_rec = "Moderate Study Intensity: Good work, but expanding your study hours slightly (e.g. by 1-2 hours) could push your grade into the next performance tier."
    else:
        study_rec = "Outstanding Study Focus: Excellent commitment. Ensure your study hours focus on active recall and practice problems."

    # Midterm marks recommendations
    if midterm_marks < 60:
        midterm_rec = f"Low Midterm Performance ({midterm_marks}/100): Your midterms show gaps in foundational knowledge. Re-evaluate your midterm papers, target weak points, and attend office hours."
    elif midterm_marks < 80:
        midterm_rec = f"Solid Midterm Performance ({midterm_marks}/100): Good baseline. Review the questions you got wrong to refine your conceptual understanding before finals."
    else:
        midterm_rec = f"Top Tier Midterm Performance ({midterm_marks}/100): Exceptional. Maintain this focus and don't get complacent. Focus on solving mock final exams."

    # Overall recommendation summary
    if category == "Excellent":
        overall_rec = "🏆 Academic Excellence Path: On track for a top-tier grade. Continue with your current habits and act as a study group lead to solidify concepts."
    elif category == "Good":
        overall_rec = "📈 Strong Performance Path: You are doing well. Small improvements in study hours or exam preparation can push you into the Excellent bracket."
    elif category == "Average":
        overall_rec = "⚠️ Performance Alert: You are in the pass range but close to the border. Increase study hours, seek tutoring, and do weekly revisions."
    else:
        overall_rec = "🚨 Critical Performance Alert: Projected to fall behind. Immediate action required. Schedule a counseling session, establish a rigid study timetable, and revise basic topics."

    return {
        "category": category,
        "recommendations": {
            "attendance": attendance_rec,
            "study_hours": study_rec,
            "midterm_marks": midterm_rec,
            "overall": overall_rec
        }
    }


# ---------------- API ROUTES ---------------- #

@app.route("/")
def index():
    """Serve the single page application HTML."""
    return render_template("index.html")


@app.route("/api/predict", methods=["POST"])
def predict():
    """Predict final marks for a single student."""
    model = get_model()
    if not model:
        return jsonify({"error": "Model is not available. Please try again shortly."}), 500

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        attendance = float(data.get("attendance", 0))
        study_hours = float(data.get("study_hours", 0))
        midterm_marks = float(data.get("midterm_marks", 0))

        # Check bounds
        if not (0 <= attendance <= 100):
            return jsonify({"error": "Attendance must be between 0 and 100%"}), 400
        if not (0 <= study_hours <= 168):
            return jsonify({"error": "Study hours must be between 0 and 168 hours/week"}), 400
        if not (0 <= midterm_marks <= 100):
            return jsonify({"error": "Midterm marks must be between 0 and 100"}), 400

        # Predict
        features = np.array([[attendance, study_hours, midterm_marks]])
        pred_score = float(model.predict(features)[0])
        pred_score = float(np.clip(pred_score, 0.0, 100.0))  # Cap predicted final marks

        # Generate recommendation details
        rec_details = generate_recommendations(pred_score, attendance, study_hours, midterm_marks)

        return jsonify({
            "attendance": attendance,
            "study_hours": study_hours,
            "midterm_marks": midterm_marks,
            "prediction": pred_score,
            "category": rec_details["category"],
            "recommendations": rec_details["recommendations"]
        })

    except ValueError:
        return jsonify({"error": "Invalid numeric values in inputs"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/predict-batch", methods=["POST"])
def predict_batch():
    """Perform predictions on an uploaded CSV file."""
    model = get_model()
    if not model:
        return jsonify({"error": "Model is not available. Please try again shortly."}), 500

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        # Read CSV file
        stream = io.StringIO(file.stream.read().decode("utf8"), newline=None)
        reader = csv.DictReader(stream)

        # Validate headers
        required_cols = ["Attendance", "StudyHours", "MidtermMarks"]
        headers = reader.fieldnames
        if not headers or not all(col in headers for col in required_cols):
            return jsonify({"error": f"Invalid CSV headers. Required columns: {', '.join(required_cols)}"}), 400

        results = []
        scores = []
        at_risk_count = 0

        for row_idx, row in enumerate(reader):
            try:
                attendance = float(row["Attendance"])
                study_hours = float(row["StudyHours"])
                midterm_marks = float(row["MidtermMarks"])

                # Make prediction
                features = np.array([[attendance, study_hours, midterm_marks]])
                pred_score = float(model.predict(features)[0])
                pred_score = float(np.clip(pred_score, 0.0, 100.0))

                # Success category mapping
                if pred_score >= 90:
                    status = "Excellent"
                elif pred_score >= 75:
                    status = "Good"
                elif pred_score >= 50:
                    status = "Average"
                else:
                    status = "At Risk"
                    at_risk_count += 1

                scores.append(pred_score)
                results.append({
                    "Attendance": attendance,
                    "StudyHours": study_hours,
                    "MidtermMarks": midterm_marks,
                    "PredictedFinalMarks": pred_score,
                    "Status": status
                })
            except (ValueError, KeyError) as e:
                return jsonify({"error": f"Data formatting error at row {row_idx + 2}: {str(e)}"}), 400

        if not results:
            return jsonify({"error": "The uploaded CSV file is empty"}), 400

        # Calculate statistics
        avg_score = float(np.mean(scores))
        pass_rate = float(sum(1 for s in scores if s >= 50) / len(scores)) * 100

        return jsonify({
            "results": results,
            "stats": {
                "total_students": len(results),
                "avg_score": avg_score,
                "pass_rate": pass_rate,
                "at_risk_count": at_risk_count
            }
        })

    except Exception as e:
        return jsonify({"error": f"Failed to parse CSV file: {str(e)}"}), 500


@app.route("/api/stats", methods=["GET"])
def get_stats():
    """Retrieve training dataset rows, descriptive statistics, correlations, and model metrics."""
    import os
    if not os.path.exists(DATASET_PATH):
        return jsonify({"error": "Cleaned dataset not found."}), 404

    model = get_model()
    if not model:
        return jsonify({"error": "Model is not available. Please try again shortly."}), 500

    try:
        # Load dataset
        df = pd.read_csv(DATASET_PATH)

        # Calculate descriptive stats / averages
        averages = df.mean().to_dict()

        # Calculate correlation matrix
        corr = df.corr().to_dict()

        # Convert dataset to list of records
        dataset_records = df.to_dict(orient="records")

        # Dynamic metrics verification (R2, MAE, MSE on active dataset)
        X = df[["Attendance", "StudyHours", "MidtermMarks"]]
        y = df["FinalMarks"]

        predictions = model.predict(X)
        from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
        mae = float(mean_absolute_error(y, predictions))
        mse = float(mean_squared_error(y, predictions))
        r2 = float(r2_score(y, predictions))

        # Model coefficients structure
        coefficients = {
            "Attendance": float(model.coef_[0]),
            "StudyHours": float(model.coef_[1]),
            "MidtermMarks": float(model.coef_[2])
        }
        intercept = float(model.intercept_)

        return jsonify({
            "averages": averages,
            "correlation": corr,
            "dataset": dataset_records,
            "metrics": {
                "r2": r2,
                "mae": mae,
                "mse": mse
            },
            "model_info": {
                "coefficients": coefficients,
                "intercept": intercept
            }
        })
    except Exception as e:
        return jsonify({"error": f"Failed to gather dataset statistics: {str(e)}"}), 500


@app.route("/api/train", methods=["POST"])
def retrain_model():
    """Retrain the model in-memory from the dataset (no file saved to disk)."""
    import os
    try:
        if not os.path.exists(DATASET_PATH):
            return jsonify({"error": f"Data file {DATASET_PATH} not found to retrain model."}), 404

        init_model()  # Re-runs training and updates global _model and _train_metrics

        return jsonify({
            "success": True,
            "message": "Model retrained successfully in-memory (no file saved).",
            "metrics": _train_metrics
        })
    except Exception as e:
        return jsonify({"error": f"Failed to retrain model: {str(e)}"}), 500


if __name__ == "__main__":
    # Start the Flask development server on localhost
    print("--------------------------------------------------")
    # Using default port 5000
    app.run(host="127.0.0.1", port=5000, debug=True)