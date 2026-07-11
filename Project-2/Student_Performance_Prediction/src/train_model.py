import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def load_data(file_path):
    """
    Load cleaned dataset.
    """
    return pd.read_csv(file_path)


def train_model(data):
    """
    Train Linear Regression model.
    """

    # Features
    X = data[["Attendance", "StudyHours", "MidtermMarks"]]

    # Target
    y = data["FinalMarks"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Create model
    model = LinearRegression()

    # Train model
    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)

    # Evaluation
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("\nModel Evaluation")
    print("-" * 40)
    print(f"Mean Absolute Error : {mae:.2f}")
    print(f"Mean Squared Error  : {mse:.2f}")
    print(f"R² Score            : {r2:.2f}")

    # Save model
    joblib.dump(model, "models/model.pkl")

    print("\nModel saved successfully!")
    print("Location: models/model.pkl")


def main():
    data = load_data("data/student_performance_cleaned.csv")
    train_model(data)


if __name__ == "__main__":
    main()