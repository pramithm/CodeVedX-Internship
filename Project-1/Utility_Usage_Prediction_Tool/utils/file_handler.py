import pandas as pd
import os

FILE_PATH = "data/usage_data.csv"

def load_data():
    if not os.path.exists(FILE_PATH):
        df =pd.DataFrame(columns=["Month","Usage"])
        df.to_csv(FILE_PATH, index=False)
    return pd.read_csv(FILE_PATH)

def add_record(month, usage):
    df = load_data()
    new_record = pd.DataFrame({
        "Month": [month],
        "Usage": [usage]
    })

    df = pd.concat([df, new_record], ignore_index=True)

    df.to_csv(FILE_PATH, index=False)
    
def update_record(month, new_usage):
    df = load_data()

    if month in df["Month"].values:
        df.loc[df["Month"] == month, "Usage"] = new_usage
        df.to_csv(FILE_PATH, index=False)
        return True

    return False