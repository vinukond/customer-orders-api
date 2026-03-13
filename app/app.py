from fastapi import FastAPI, HTTPException
import sqlite3
import os
from mangum import Mangum

app = FastAPI(title="Customer Orders API")

DATABASE = os.getenv("DATABASE_PATH", "database.db")


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.get("/")
def home():
    return {
        "message": "Customer Orders API is running",
        "cloud_ready": "AWS Lambda compatible"
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/customer/{customer_id}")
def get_customer(customer_id: int):

    conn = get_db_connection()
    cursor = conn.cursor()

    customer = cursor.execute(
        "SELECT id, first_name, surname, email, status FROM customers WHERE id=?",
        (customer_id,)
    ).fetchone()

    if not customer:
        conn.close()
        raise HTTPException(status_code=404, detail="Customer not found")

    orders = cursor.execute(
        "SELECT product_name, quantity, unit_price FROM orders WHERE customer_id=?",
        (customer_id,)
    ).fetchall()

    conn.close()

    return {
        "customer": {
            "id": customer["id"],
            "name": f"{customer['first_name']} {customer['surname']}",
            "email": customer["email"],
            "status": customer["status"]
        },
        "orders": [
            {
                "product_name": o["product_name"],
                "quantity": o["quantity"],
                "unit_price": o["unit_price"]
            }
            for o in orders
        ]
    }


# AWS Lambda compatibility
handler = Mangum(app)
