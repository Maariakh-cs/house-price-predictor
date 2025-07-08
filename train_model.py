yp1import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle

# Load dataset
df = pd.read_csv(r'C:\Users\maari\house_price_predictor\house_data.csv')

# Features and target
X = df.drop("price", axis=1)
y = df["price"]

# Pipeline: encode 'location' + train linear regression
pipeline = Pipeline([
    ("encoder", ColumnTransformer(
        transformers=[
            ("loc", OneHotEncoder(), ["location"])
        ],
        remainder='passthrough'  # keep numeric columns
    )),
    ("model", LinearRegression())
])

pipeline.fit(X, y)

# Save model
with open("house_model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("Model trained and saved as 'house_model.pkl'")
