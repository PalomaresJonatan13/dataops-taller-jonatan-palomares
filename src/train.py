from transform import calculate_metrics

import joblib
from pathlib import Path

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score



def train_model(df:pd.DataFrame) -> dict:
    # create copy with 'mes' and 'venta_total'
    df_copy = calculate_metrics(df)

    # get X and y, and split into train (0.8) and test (0.2)
    X = df_copy[["mes"]]
    y = df_copy["venta_total"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # get predictions and r2
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)

    # save model in models/model.pkl
    BASE_DIR = Path(__file__).resolve().parent.parent
    MODEL_PATH = BASE_DIR / "models" / "model.pkl"
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    return {
        "model": model,
        "r2": r2
    }