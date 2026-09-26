"""Custom exceptions for sales data operations."""


class WrongDBColumnsException(Exception):
    """Raised when the sales table is missing required columns."""

    def __init__(self, actual_columns, expected_columns):
        """Describe the actual and expected sales table columns."""
        super().__init__(
            f"Columns in the 'ventas' table are not the expected ones. Received: {actual_columns}. Expected at least: {expected_columns}"
        )
