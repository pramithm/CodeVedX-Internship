import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

# Create Polynomial Regression Model
model = Pipeline([
    ("poly", PolynomialFeatures(degree=3)),
    ("linear", LinearRegression())
])


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


def is_model_trained():
    return hasattr(model.named_steps["linear"], "coef_")