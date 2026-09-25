from datetime import date
from pathlib import Path

import pandas as pd
import pytest

from dataops_taller_jonatan_palomares.extract import extract_data
from dataops_taller_jonatan_palomares.utils import expected_columns


@pytest.fixture(scope="module")
def sales_df():
	db_path = Path(__file__).resolve().parents[1] / "data" / "database.db"
	df = extract_data(db_path)

	assert not df.empty, "La tabla ventas no debe estar vacía"
	return df


def test_cantidad_has_no_negative_values(sales_df):
	assert (sales_df["cantidad"].dropna() >= 0).all()


def test_precio_unitario_is_greater_than_zero(sales_df):
	assert (sales_df["precio_unitario"].dropna() > 0).all()


def test_ventas_has_expected_columns(sales_df):
	assert set(expected_columns).issubset(sales_df.columns)


def test_fecha_has_no_future_dates(sales_df):
	dates = pd.to_datetime(sales_df["fecha"])

	assert (dates.dt.date <= date.today()).all()
