"""Extract sales records from the SQLite database."""

from pathlib import Path
import sqlite3

import pandas as pd

from dataops_taller_jonatan_palomares.utils import check_subset_columns_ventas


def extract_data(db_path: str | Path) -> pd.DataFrame:
    """Read the ventas table and validate its required columns."""
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM ventas")
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    df = pd.DataFrame(rows, columns=columns)

    check_subset_columns_ventas(df)

    return df
