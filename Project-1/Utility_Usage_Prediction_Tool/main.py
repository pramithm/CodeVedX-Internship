from utils.menu import display_menu
from utils.file_handler import load_data, add_record, update_record
from models.predictor import train_model, predict_usage

while True:
    display_menu()

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            data = load_data()
            print("\nUtility Usage Data")
            print(data)

        case "2":
            month = int(input("Enter Month (1-12): "))
            usage = float(input("Enter Usage: "))

            add_record(month, usage)
            print("Record added successfully.")

        case "3":
            month = int(input("Enter Month to Update: "))
            usage = float(input("Enter New Usage: "))

            if update_record(month, usage):
                print("Record updated successfully.")
            else:
                print("Month not found.")

        case "4":
            data = load_data()

            if len(data) < 2:
               print("Not enough data to train the model.")
            else:
               train_model(data)
               print("Model trained successfully.")

        case "5":
                month = int(input("Enter Month (1-12): "))

                prediction = predict_usage(month)

                print(f"Predicted Usage: {prediction:.2f}")

        case "6":
            print("Thank you for using the application.")
            break

        case _:
            print("Invalid choice. Please try again.")