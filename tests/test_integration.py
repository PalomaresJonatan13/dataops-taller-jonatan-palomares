"""Integration tests for the sales data pipeline."""

from pathlib import Path

from dataops_taller_jonatan_palomares.extract import extract_data
from dataops_taller_jonatan_palomares.transform import aggregate_sales


def test_extract_transform_aggregate_pipeline():
	"""Run extraction through aggregation and validate the final frame."""
	db_path = Path(__file__).resolve().parents[1] / "data" / "database.db"
	extracted_df = extract_data(db_path)

	aggregated_sales_df = aggregate_sales(extracted_df)

	assert not aggregated_sales_df.empty
	assert list(aggregated_sales_df.columns) == ["categoria", "mes", "venta_total"]
