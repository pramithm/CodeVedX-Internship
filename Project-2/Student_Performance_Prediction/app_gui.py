import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np


# Load trained model
model = joblib.load("models/model.pkl")


def predict():
    try:
        attendance = float(attendance_entry.get())
        study_hours = float(study_hours_entry.get())
        midterm_marks = float(midterm_marks_entry.get())

        features = np.array([[attendance, study_hours, midterm_marks]])

        prediction = model.predict(features)[0]

        result_label.config(
            text=f"Predicted Final Marks: {prediction:.2f}",
            fg="green"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numeric values."
        )


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Student Performance Prediction")
root.geometry("450x420")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Student Performance Prediction System",
    font=("Arial", 16, "bold")
)
title.pack(pady=20)

# Attendance
tk.Label(root, text="Attendance (%)", font=("Arial", 11)).pack()

attendance_entry = tk.Entry(root, width=30)
attendance_entry.pack(pady=5)

# Study Hours
tk.Label(root, text="Study Hours", font=("Arial", 11)).pack()

study_hours_entry = tk.Entry(root, width=30)
study_hours_entry.pack(pady=5)

# Midterm Marks
tk.Label(root, text="Midterm Marks", font=("Arial", 11)).pack()

midterm_marks_entry = tk.Entry(root, width=30)
midterm_marks_entry.pack(pady=5)

# Predict Button
predict_btn = tk.Button(
    root,
    text="Predict",
    width=20,
    bg="blue",
    fg="white",
    command=predict
)
predict_btn.pack(pady=20)

# Result Label
result_label = tk.Label(
    root,
    text="Predicted Final Marks: --",
    font=("Arial", 13, "bold")
)
result_label.pack(pady=20)

root.mainloop()