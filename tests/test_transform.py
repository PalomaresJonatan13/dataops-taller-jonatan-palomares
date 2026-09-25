import pytest
import pandas as pd


import dataops_taller_jonatan_palomares.transform as tf


@pytest.fixture
def df():
	return pd.DataFrame({
        "id": [1, 2, 3, 4, 5, 6],
        "fecha": ["2024-01-05", "2024-01-10", "2024-02-02", "2024-01-05", "2024-02-15", "2024-02-20"],
        "producto": ["p1", "p2", "p3", "p1", "p4", "p5"],
        "categoria": ["A", "A", "B", "A", "B", "A"],
        "cantidad": [2, None, 1, 2, 4, 2],
        "precio_unitario": [10.0, 20.0, None, 10.0, 5.0, 8.0],
        "cliente_id": [101, 102, 103, 101, 104, 105],
	})


def test_clean_data_remove_duplicates(df):
	cleaned = tf.clean_data(df)

	assert len(cleaned) == 5
	assert cleaned["id"].tolist() == [1, 2, 3, 5, 6]


def test_clean_data_fill_missing_values(df):
	cleaned = tf.clean_data(df).set_index("id")

	assert cleaned.loc[2, "cantidad"] == 0
	assert cleaned.loc[3, "precio_unitario"] == pytest.approx(10.75)
	assert cleaned["cantidad"].isna().sum() == 0
	assert cleaned["precio_unitario"].isna().sum() == 0


def test_calculate_metrics_calculate_total_sales(df):
	metrics = tf.calculate_metrics(df).set_index("id")

	assert metrics["venta_total"].to_dict() == pytest.approx(
		{1: 20.0, 2: 0.0, 3: 10.75, 5: 20.0, 6: 16.0}
	)


def test_aggregate_sales_group_by_category_and_month(df):
	aggregated = tf.aggregate_sales(df)
	actual = {
		(row.categoria, row.mes): row.venta_total
		for row in aggregated.itertuples(index=False)
	}

	assert actual == pytest.approx({("A", 1): 20.0, ("A", 2): 16.0, ("B", 2): 30.75})
	