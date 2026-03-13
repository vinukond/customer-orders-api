import sqlite3
import pandas as pd

# create database in project root
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# create customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    surname TEXT,
    email TEXT,
    status TEXT
)
""")

# create orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_name TEXT,
    quantity INTEGER,
    unit_price REAL,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
)
""")

# load CSV files
customers = pd.read_csv("data/customers.csv")
orders = pd.read_csv("data/orders.csv")

# insert data
customers.to_sql("customers", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("Database created and data loaded successfully.")