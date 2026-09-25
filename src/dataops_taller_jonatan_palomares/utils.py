"""Shared validation and file-output utilities."""

from pathlib import Path

import pandas as pd

from dataops_taller_jonatan_palomares.exceptions.exceptions import WrongDBColumnsException


expected_columns = [
    "id", "fecha", "producto", "categoria", "cantidad", "precio_unitario", "cliente_id"
]

def check_subset_columns_ventas(df:pd.DataFrame) -> None:
    """Raise an exception when required ventas columns are missing."""
    if not set(expected_columns).issubset(df.columns):
        raise WrongDBColumnsException(df.columns, expected_columns)


def save_to_csv(df:pd.DataFrame, path:str|Path) -> None:
    """Save a DataFrame to a CSV file without its index."""
    # save to csv
    path = Path(path)
    df.to_csv(path, index=False)
