# Customer Orders API – Technical Assessment

## Overview

This project was created for the **Junior Python / AWS Developer technical assessment**.
It demonstrates building a simple backend system that manages **customers and their orders**, exposes the data through a **REST API**, and processes the data through an **ETL pipeline**.

The solution includes:

* A script to create and populate a database
* A REST API to retrieve customer and order data
* An ETL script to export processed data into a CSV file
* Cloud-ready API support for potential AWS deployment

---

# Technologies Used

| Technology | Purpose                          |
| ---------- | -------------------------------- |
| Python     | Main programming language        |
| FastAPI    | REST API framework               |
| SQLite     | Lightweight relational database  |
| Pandas     | Data transformation for ETL      |
| Uvicorn    | Server for running the API       |
| Mangum     | Enables AWS Lambda compatibility |

---

# Project Structure

```
project
│
├── app
│   └── app.py
│
├── scripts
│   ├── generate_data.py
│   ├── setup_database.py
│   └── etl_export.py
│
├── data
│   ├── customers.csv
│   └── orders.csv
│
├── output
│   └── customer_orders_export.csv
│
├── database.db
├── requirements.txt
└── README.md
```

---

# How to Run the Application (Using VS Code)

### 1. Open the Project

1. Open **Visual Studio Code**
2. Click **File → Open Folder**
3. Select the project folder.

---

### 2. Open the Terminal

In VS Code open the integrated terminal:

```
Terminal → New Terminal
```

---

### 3. Install Dependencies

Run the following command in the terminal:

```
pip install -r requirements.txt
```

This installs all required Python libraries.

---

### 4. Generate Sample Data

Run the data generation script:

```
python scripts/generate_data.py
```

This creates:

* `data/customers.csv`
* `data/orders.csv`

Each dataset contains **sample records for customers and orders**.

---

### 5. Create and Populate the Database

Run:

```
python scripts/setup_database.py
```

This script:

* Creates the SQLite database
* Creates the Customers and Orders tables
* Loads the sample data into the database

The script is **repeatable** and can be run multiple times without creating duplicates.

---

### 6. Start the REST API

Run the following command:

```
uvicorn app.app:app --reload
```

Once the server starts, open your browser and go to:

```
http://127.0.0.1:8000/docs
```

This opens the **FastAPI interactive documentation** where you can test the API.

Example request:

```
GET /customer/3
```

This returns customer details along with their orders.

---

# API Endpoints

### Root Endpoint

```
GET /
```

Returns the API status.

---

### Health Check

```
GET /health
```

Returns a simple health status response.

Example:

```
{
 "status": "ok"
}
```

---

### Get Customer Orders

```
GET /customer/{customer_id}
```

Returns customer information and their associated orders.

Example response:

```
{
 "customer": {
  "id": 3,
  "name": "Customer3 Test3",
  "email": "customer3@example.com",
  "status": "active"
 },
 "orders": [
  {
   "product_name": "Keyboard",
   "quantity": 2,
   "unit_price": 50
  }
 ]
}
```

---

# ETL Data Export

The ETL script extracts customer order data, transforms it, and exports the results.

Run the script:

```
python scripts/etl_export.py
```

This performs three steps:

### Extract

Query the database for **active customers and their orders**.

### Transform

* Combine first name and surname into a `name` field
* Calculate `total_value = quantity × unit_price`

### Export

Write the processed data to a CSV file:

```
output/customer_orders_export.csv
```

Example output:

```
name,product_name,quantity,unit_price,total_value
Customer1 Test1,Laptop,1,1000,1000
Customer3 Test3,Keyboard,2,50,100
Customer7 Test7,Mouse,1,20,20
```

---

# Application Flow

The flow of data through the application is:

```
Sample Data (CSV)
      ↓
Database Setup Script
      ↓
SQLite Database
      ↓
FastAPI REST API
      ↓
ETL Script
      ↓
Exported CSV Dataset
```

---

# Design Choices and Reasoning

**SQLite**

SQLite was chosen because it is lightweight, simple to configure, and suitable for small applications or demonstrations.

**FastAPI**

FastAPI provides:

* High performance
* Automatic API documentation
* Simple integration with Python type hints

**Pandas**

Pandas simplifies data transformation and exporting structured datasets.

**Mangum**

Mangum was included to make the API compatible with **AWS Lambda**, allowing potential serverless deployment.

---

# Possible Improvements

If more time were available, the following improvements could be made:

* Add automated unit tests for the API
* Replace SQLite with PostgreSQL
* Containerize the application using Docker
* Deploy the API on AWS (Lambda or ECS)
* Add authentication and authorization
* Implement logging and monitoring

---

# Summary

This project demonstrates:

* Python backend development
* Database creation and data loading
* REST API implementation
* ETL data processing
* Cloud-ready architecture

The solution provides a complete example of a **simple Python data application combining API and data processing components**.

