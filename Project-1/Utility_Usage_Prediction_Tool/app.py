from flask import Flask, render_template, request, redirect, url_for, flash

from utils.file_handler import (
    load_data,
    add_record,
    update_record
)

from models.predictor import (
    train_model,
    predict_usage,
    is_model_trained
)

from utils.validator import (
    validate_month,
    validate_usage
)

app = Flask(__name__)
app.secret_key = "utility_prediction_secret"


@app.route("/")
def home():

    data = load_data()
    total_records = len(data)
    
    if not is_model_trained() and len(data) >= 2:
        train_model(data)
        
    model_status = "Trained" if is_model_trained() else "Not Trained"
    
    trend_data = []
    if is_model_trained():
        trend_data = [round(max(0.0, float(predict_usage(m))), 2) for m in range(1, 13)]

    return render_template(
        "index.html",
        data=data.to_dict(orient="records"),
        total_records=total_records,
        prediction=None,
        model_status=model_status,
        trend_data=trend_data
    )


@app.route("/add", methods=["POST"])
def add():

    month_raw = request.form.get("month")
    usage_raw = request.form.get("usage")

    if not validate_month(month_raw) or not validate_usage(usage_raw):
        flash("Invalid input values. Month must be between 1 and 12, and Usage must be non-negative.", "danger")
        return redirect(url_for("home"))

    month = int(month_raw)
    usage = float(usage_raw)

    add_record(month, usage)

    flash("Record added successfully!", "success")

    return redirect(url_for("home"))


@app.route("/update", methods=["POST"])
def update():

    month_raw = request.form.get("month")
    usage_raw = request.form.get("usage")

    if not validate_month(month_raw) or not validate_usage(usage_raw):
        flash("Invalid input values. Month must be between 1 and 12, and Usage must be non-negative.", "danger")
        return redirect(url_for("home"))

    month = int(month_raw)
    usage = float(usage_raw)

    updated = update_record(month, usage)

    if updated:
        flash("Record updated successfully!", "success")
    else:
        flash("Month not found!", "danger")

    return redirect(url_for("home"))


@app.route("/train", methods=["POST"])
def train():

    data = load_data()

    if len(data) < 2:

        flash("Not enough data to train the model. Minimum 2 records required.", "warning")

        return redirect(url_for("home"))

    train_model(data)

    flash("Model trained successfully!", "success")

    return redirect(url_for("home"))


@app.route("/predict", methods=["POST"])
def predict():

    month_raw = request.form.get("month")
    if not validate_month(month_raw):
        flash("Invalid month selected for prediction.", "danger")
        return redirect(url_for("home"))

    month = int(month_raw)
    data = load_data()

    if len(data) < 2:
        flash("Not enough data to make predictions. Minimum 2 records required.", "warning")
        return redirect(url_for("home"))

    train_model(data)

    result = predict_usage(month)
    model_status = "Trained" if is_model_trained() else "Not Trained"
    
    trend_data = []
    if is_model_trained():
        trend_data = [round(max(0.0, float(predict_usage(m))), 2) for m in range(1, 13)]

    return render_template(
        "index.html",
        data=data.to_dict(orient="records"),
        total_records=len(data),
        prediction=round(result, 2),
        model_status=model_status,
        trend_data=trend_data
    )


if __name__ == "__main__":
    app.run(debug=True)