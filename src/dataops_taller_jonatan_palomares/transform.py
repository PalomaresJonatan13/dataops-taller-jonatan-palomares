"""Clean sales data, calculate metrics, and aggregate results."""

import pandas as pd

from dataops_taller_jonatan_palomares.utils import check_subset_columns_ventas


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate sales, fill missing values and change fecha to datetime."""
    check_subset_columns_ventas(df)

    # drop duplicates
    df_copy = df.drop_duplicates(subset=df.columns[df.columns != "id"])

    # fill missing 'cantidad' with 0
    df_copy["cantidad"] = df_copy["cantidad"].fillna(0)

    # fill missing 'precio unitario' with its mean
    mean_precio = df_copy["precio_unitario"].mean()
    df_copy["precio_unitario"] = df_copy["precio_unitario"].fillna(mean_precio)

    # convert 'fecha' to datetime
    df_copy["fecha"] = pd.to_datetime(df_copy["fecha"])

    return df_copy


def calculate_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Add total sales and calendar month columns."""
    df_copy = clean_data(df)

    # add 'vental_total'
    df_copy["venta_total"] = df_copy["cantidad"] * df_copy["precio_unitario"]

    # add 'mes'
    df_copy["mes"] = df_copy["fecha"].dt.month

    return df_copy


def aggregate_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Sum total sales by category and month."""
    df_copy = calculate_metrics(df)

    # group by 'categoria' and 'mes' and calculate the sum of 'venta_total'
    aggregate_sales_df = (
        df_copy.groupby(["categoria", "mes"])["venta_total"].sum().reset_index()
    )

    return aggregate_sales_df
