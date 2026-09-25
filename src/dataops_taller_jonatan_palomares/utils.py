from dataops_taller_jonatan_palomares.exceptions.exceptions import WrongDBColumnsException

from pathlib import Path

import pandas as pd



expected_columns = ["id", "fecha", "producto", "categoria", "cantidad", "precio_unitario", "cliente_id"]

def check_subset_columns_ventas(df:pd.DataFrame) -> None:
    if not set(expected_columns).issubset(df.columns):
        raise WrongDBColumnsException(df.columns, expected_columns)


def save_to_csv(df:pd.DataFrame, path:str|Path) -> None:
    # save to csv
    path = Path(path)
    df.to_csv(path, index=False)
