from utils import check_columns_ventas

import numpy as np
import pandas as pd
import sqlite3



expected_columns = np.array(["fecha", "producto", "categoria", "cantidad", "precio_unitario", "cliente_id"])

def extract_data(db_path:str) -> pd.DataFrame:
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM ventas")
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    df = pd.DataFrame(rows, columns=columns)

    check_columns_ventas(df)

    return df