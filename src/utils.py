from exceptions.exceptions import WrongDBColumnsException

import numpy as np
import pandas as pd



expected_columns = np.array(["id", "fecha", "producto", "categoria", "cantidad", "precio_unitario", "cliente_id"])

def check_columns_ventas(df:pd.DataFrame) -> None:
    if not np.array_like(df.columns, expected_columns):
        raise WrongDBColumnsException(df.columns, expected_columns)