class WrongDBColumnsException(Exception):
    def __init__(self, actual_columns, expected_columns):
        super().__init__(f"Columns in the 'ventas' table are not the expected ones. Received: {actual_columns}. Expected: {expected_columns}")