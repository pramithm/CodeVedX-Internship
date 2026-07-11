import pandas as pd
from sklearn.linear_model import LinearRegression

model = LinearRegression()


def train_model(data):
    x = data[["Month"]]
    y = data["Usage"]

    model.fit(x, y)


def predict_usage(month):
    input_data = pd.DataFrame({
        "Month": [month]
    })

    prediction = model.predict(input_data)
    return prediction[0]