import pandas as pd

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
    Train Linear Regression model and return the trained model object along
    with evaluation metrics. No file is saved to disk.
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

    # Create and train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions on test set
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
    print("\nModel trained successfully (in-memory, no file saved).")

    metrics = {
        "mae": float(mae),
        "mse": float(mse),
        "r2": float(r2)
    }

    return model, metrics


def main():
    data = load_data("data/student_performance_cleaned.csv")
    model, metrics = train_model(data)
    print(f"\nMetrics: {metrics}")


if __name__ == "__main__":
    main()