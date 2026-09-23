import sqlite3

connection = sqlite3.connect("data/database.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT,
    producto TEXT,
    categoria TEXT,
    cantidad INTEGER,
    precio_unitario REAL,
    cliente_id INTEGER
)
''')
connection.commit()
connection.close()
