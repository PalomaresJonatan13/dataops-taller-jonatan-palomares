CREATE TABLE ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    producto TEXT NOT NULL,
    categoria TEXT NOT NULL,
    cantidad INTEGER,
    precio_unitario REAL,
    cliente_id INTEGER NOT NULL
)