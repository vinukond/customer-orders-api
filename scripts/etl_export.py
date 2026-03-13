import sqlite3
import pandas as pd
import boto3
import os

# connect to database
conn = sqlite3.connect("database.db")

query = """
SELECT 
    c.id,
    c.first_name,
    c.surname,
    o.product_name,
    o.quantity,
    o.unit_price
FROM customers c
JOIN orders o
ON c.id = o.customer_id
WHERE c.status = 'active'
"""

df = pd.read_sql_query(query, conn)

# transformations
df["full_name"] = df["first_name"] + " " + df["surname"]
df["order_total"] = df["quantity"] * df["unit_price"]

result = df[["id", "full_name", "product_name", "quantity", "order_total"]]

# export to CSV
output_file = "output/customer_orders_summary.csv"
result.to_csv(output_file, index=False)

print("CSV exported successfully.")

# optional S3 upload
bucket = os.getenv("S3_BUCKET")

if bucket:
    s3 = boto3.client("s3")
    s3.upload_file(output_file, bucket, "customer_orders_summary.csv")
    print(f"File uploaded to S3 bucket: {bucket}")
else:
    print("S3_BUCKET not set. Skipping S3 upload.")

conn.close()