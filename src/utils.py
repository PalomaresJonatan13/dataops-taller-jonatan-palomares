from exceptions.exceptions import WrongDBColumnsException

import numpy as np
import pandas as pd



expected_columns = ["id", "fecha", "producto", "categoria", "cantidad", "precio_unitario", "cliente_id"]

def check_subset_columns_ventas(df:pd.DataFrame) -> None:
    if not set(expected_columns).issubset(df.columns):
        raise WrongDBColumnsException(df.columns, expected_columns)