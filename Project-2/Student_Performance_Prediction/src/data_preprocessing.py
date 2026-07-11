import pandas as pd


def load_data(file_path):
    """
    Load dataset from CSV file.
    """
    data = pd.read_csv(file_path)
    return data


def preprocess_data(data):
    """
    Clean and preprocess the dataset.
    """

    # Remove duplicate rows
    data.drop_duplicates(inplace=True)

    # Fill missing values with column mean
    data.fillna(data.mean(numeric_only=True), inplace=True)

    return data


def main():
    file_path = "data/student_performance.csv"

    # Load dataset
    data = load_data(file_path)

    print("\nOriginal Dataset")
    print(data.head())

    # Preprocess dataset
    cleaned_data = preprocess_data(data)

    print("\nCleaned Dataset")
    print(cleaned_data.head())

    # Save cleaned dataset
    cleaned_data.to_csv("data/student_performance_cleaned.csv", index=False)

    print("\nCleaned dataset saved successfully!")


if __name__ == "__main__":
    main()