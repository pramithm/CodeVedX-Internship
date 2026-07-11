import joblib
import numpy as np


def load_model():
    """
    Load the trained model.
    """
    return joblib.load("models/model.pkl")


def predict_final_marks(model, attendance, study_hours, midterm_marks):
    """
    Predict the final marks.
    """
    features = np.array([[attendance, study_hours, midterm_marks]])
    prediction = model.predict(features)

    return prediction[0]


def main():
    print("=" * 45)
    print(" Student Performance Prediction System ")
    print("=" * 45)

    # Load trained model
    model = load_model()

    # Get user input
    attendance = float(input("Enter Attendance (%): "))
    study_hours = float(input("Enter Study Hours: "))
    midterm_marks = float(input("Enter Midterm Marks: "))

    # Predict
    predicted_marks = predict_final_marks(
        model,
        attendance,
        study_hours,
        midterm_marks
    )

    print("\nPredicted Final Marks: {:.2f}".format(predicted_marks))


if __name__ == "__main__":
    main()