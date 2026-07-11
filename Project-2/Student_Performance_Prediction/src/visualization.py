import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """
    Load the cleaned dataset.
    """
    return pd.read_csv(file_path)


def display_dataset_info(data):
    """
    Display basic information about the dataset.
    """
    print("\nDataset Information")
    print("-" * 40)
    print(data.info())

    print("\nStatistical Summary")
    print("-" * 40)
    print(data.describe())

    print("\nMissing Values")
    print("-" * 40)
    print(data.isnull().sum())


def plot_attendance_vs_marks(data):
    plt.figure(figsize=(8, 5))
    plt.scatter(data["Attendance"], data["FinalMarks"])
    plt.title("Attendance vs Final Marks")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Final Marks")
    plt.grid(True)
    plt.show()


def plot_studyhours_vs_marks(data):
    plt.figure(figsize=(8, 5))
    plt.scatter(data["StudyHours"], data["FinalMarks"])
    plt.title("Study Hours vs Final Marks")
    plt.xlabel("Study Hours")
    plt.ylabel("Final Marks")
    plt.grid(True)
    plt.show()


def plot_marks_distribution(data):
    plt.figure(figsize=(8, 5))
    plt.hist(data["FinalMarks"], bins=8)
    plt.title("Distribution of Final Marks")
    plt.xlabel("Final Marks")
    plt.ylabel("Number of Students")
    plt.grid(True)
    plt.show()


def plot_correlation(data):
    plt.figure(figsize=(6, 5))

    correlation = data.corr()

    plt.imshow(correlation, cmap="coolwarm")

    plt.colorbar()

    plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
    plt.yticks(range(len(correlation.columns)), correlation.columns)

    plt.title("Correlation Matrix")

    plt.tight_layout()
    plt.show()


def main():
    data = load_data("data/student_performance_cleaned.csv")

    display_dataset_info(data)

    plot_attendance_vs_marks(data)

    plot_studyhours_vs_marks(data)

    plot_marks_distribution(data)

    plot_correlation(data)


if __name__ == "__main__":
    main()