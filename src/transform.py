from utils import check_subset_columns_ventas

import numpy as np
import pandas as pd



def clean_data(df:pd.DataFrame) -> pd.DataFrame:
    check_subset_columns_ventas(df)

    # drop duplicates
    df_copy = df.drop_duplicates(subset=df.columns[df.columns != "id"])

    # fill missing 'cantidad' with 0
    df_copy['cantidad'] = df_copy['cantidad'].fillna(0)

    # fill missing 'precio unitario' with its mean
    mean_precio = df_copy['precio_unitario'].mean()
    df_copy['precio_unitario'] = df_copy['precio_unitario'].fillna(mean_precio)

    # convert 'fecha' to datetime
    df_copy['fecha'] = pd.to_datetime(df_copy['fecha'])

    return df_copy



def calculate_metrics(df:pd.DataFrame) -> pd.DataFrame:
    pass


def aggegate_sales(df:pd.DataFrame) -> pd.DataFrame:
    pass