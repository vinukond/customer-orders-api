import pandas as pd
import random

# Generate customers
customers = []
for i in range(1, 51):
    customers.append({
        "id": i,
        "first_name": f"Customer{i}",
        "surname": f"Test{i}",
        "email": f"customer{i}@example.com",
        "status": "active" if i % 5 != 0 else "inactive"
    })

customers_df = pd.DataFrame(customers)
customers_df.to_csv("data/customers.csv", index=False)


# Generate orders
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Tablet", "Headphones"]

orders = []
order_id = 1

for customer_id in range(1, 51):
    for _ in range(random.randint(1, 3)):
        orders.append({
            "order_id": order_id,
            "customer_id": customer_id,
            "product_name": random.choice(products),
            "quantity": random.randint(1, 3),
            "unit_price": random.choice([20, 50, 100, 200, 500, 1000])
        })
        order_id += 1

orders_df = pd.DataFrame(orders)
orders_df.to_csv("data/orders.csv", index=False)

print("Datasets generated successfully.")
