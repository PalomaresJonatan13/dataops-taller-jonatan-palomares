import random
from collections import OrderedDict
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
            fake.random_element(elements = OrderedDict([(fecha, 0.99), (None, 0.01)])),
            fake.random_element(elements = OrderedDict([(producto, 0.99), (None, 0.01)])),
            fake.random_element(elements = OrderedDict([(categoria, 0.99), (None, 0.01)])),
            fake.random_element(elements = OrderedDict([(cantidad, 0.99), (None, 0.01)])),
            fake.random_element(elements = OrderedDict([(precio_unitario, 0.99), (None, 0.01)])),
            fake.random_element(elements = OrderedDict([(cliente_id, 0.99), (None, 0.01)]))
        ))
        


# Creation and population of the 'ventas' table
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
cursor.executemany("INSERT INTO ventas (fecha, producto, categoria, cantidad, precio_unitario, cliente_id) VALUES (?, ?, ?, ?, ?, ?)", records)

connection.commit()
connection.close()
