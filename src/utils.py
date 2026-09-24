from exceptions.exceptions import WrongDBColumnsException
from transform import aggregate_sales

from pathlib import Path

import pandas as pd



expected_columns = ["id", "fecha", "producto", "categoria", "cantidad", "precio_unitario", "cliente_id"]

def check_subset_columns_ventas(df:pd.DataFrame) -> None:
    if not set(expected_columns).issubset(df.columns):
        raise WrongDBColumnsException(df.columns, expected_columns)


def save_to_csv(df:pd.DataFrame, path:str|Path) -> None:
    # get aggregated sales
    aggregated_sales_df = aggregate_sales(df)

    # save to csv
    path = Path(path)
    aggregated_sales_df.to_csv(path, index=False)
