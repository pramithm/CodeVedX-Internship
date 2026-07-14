from utils.menu import display_menu
from utils.file_handler import load_data, add_record, update_record
from models.predictor import train_model, predict_usage, is_model_trained
from utils.validator import validate_month, validate_usage

def get_validated_month(prompt="Enter Month (1-12): "):
    while True:
        val = input(prompt)
        if validate_month(val):
            return int(val)
        print("Error: Month must be an integer between 1 and 12.")

def get_validated_usage(prompt="Enter Usage: "):
    while True:
        val = input(prompt)
        if validate_usage(val):
            return float(val)
        print("Error: Usage must be a non-negative number.")

while True:
    display_menu()

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            data = load_data()
            print("\nUtility Usage Data")
            print(data)

        case "2":
            month = get_validated_month()
            usage = get_validated_usage()

            add_record(month, usage)
            print("Record added successfully.")

        case "3":
            month = get_validated_month("Enter Month to Update (1-12): ")
            usage = get_validated_usage("Enter New Usage: ")

            if update_record(month, usage):
                print("Record updated successfully.")
            else:
                print("Month not found in existing records.")

        case "4":
            data = load_data()

            if len(data) < 2:
               print("Not enough data to train the model. Minimum 2 records required.")
            else:
               train_model(data)
               print("Model trained successfully.")

        case "5":
            if not is_model_trained():
                data = load_data()
                if len(data) >= 2:
                    print("Model is not trained. Training the model now with historical data...")
                    train_model(data)
                else:
                    print("Error: Model is not trained and there is insufficient data to train (minimum 2 records required).")
                    continue

            month = get_validated_month()
            prediction = predict_usage(month)
            print(f"\nPredicted Usage for Month {month}: {prediction:.2f} units")

        case "6":
            print("Thank you for using the application.")
            break

        case _:
            print("Invalid choice. Please try again.")