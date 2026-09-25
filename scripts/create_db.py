"""Create and populate the SQLite ventas database with sample records."""

from collections import OrderedDict
import random
from pathlib import Path

import sqlite3
from faker import Faker



# Creation of fake data for 'ventas' table in the db
fake = Faker()
fake.seed_instance(42)
random.seed(42)

n_records = 200
p_duplicates = 0.03
records = []

for _ in range(n_records):
    fecha = fake.date_this_year().strftime("%Y-%m-%d")
    producto = fake.word()
    categoria = fake.random_element(elements=("Technology", "Clothing", "Home", "Toys", "Food"))
    cantidad = fake.random_int(min=1, max=10)
    precio_unitario = round(fake.random_number(digits=2) + fake.random.random(), 2)
    cliente_id = fake.random_int(min=1, max=100)

    # with a 0.03 probability, the record is going to be a duplicate
    if (len(records) > 0) and (random.random() <= p_duplicates):
        records.append(random.choice(records))
    else:
        records.append((
            fecha,
            producto,
            categoria,
            fake.random_element(elements = OrderedDict([(cantidad, 0.97), (None, 0.03)])),
            fake.random_element(elements = OrderedDict([(precio_unitario, 0.97), (None, 0.03)])),
            cliente_id
        ))
        


# Creation and population of the 'ventas' table
DB_PATH = Path("data/database.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    producto TEXT NOT NULL,
    categoria TEXT NOT NULL,
    cantidad INTEGER,
    precio_unitario REAL,
    cliente_id INTEGER NOT NULL
)
''')
cursor.executemany("INSERT INTO ventas (fecha, producto, categoria, cantidad, precio_unitario, cliente_id) VALUES (?, ?, ?, ?, ?, ?)", records)

connection.commit()
connection.close()
