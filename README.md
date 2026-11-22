# Northwind REST API

A RESTful API built with Python Flask to manage the Northwind MySQL database.

## Tech Stack

- **Language:** Python
- **Framework:** Flask
- **Database:** MySQL
- **ORM:** Flask-SQLAlchemy
- **Validation and serialization:** Marshmallow
- **Testing:** Pytest
- **Version control:** Git and GitHub

## Features

- Create, retrieve, and update customers
- Create, retrieve, and update products
- Create, retrieve, and update orders
- Retrieve a customer's order history, including order details and product information
- Validate incoming request data with Marshmallow schemas
- Use SQLAlchemy ORM for database operations
- Organize the application into controller, model, schema, and service layers
- Write application logs to `logs/app.log`
- Test controller behavior with Pytest and mocked service calls

## Project Structure

```text
northwind_rest_api/
├── app/
│   ├── controllers/
│   │   ├── customer_controller.py
│   │   ├── product_controller.py
│   │   ├── order_controller.py
│   │   └── order_history_controller.py
│   ├── models/
│   │   ├── customer.py
│   │   ├── product.py
│   │   ├── order.py
│   │   └── order_detail.py
│   ├── schemas/
│   │   ├── customer_schema.py
│   │   ├── product_schema.py
│   │   └── order_schema.py
│   ├── services/
│   │   ├── customer_service.py
│   │   ├── product_service.py
│   │   └── order_service.py
│   ├── __init__.py
│   ├── config.py
│   └── extensions.py
├── tests/
│   ├── test_customer_controller.py
│   ├── test_product_controller.py
│   └── test_order_controller.py
├── logs/
├── .gitignore
├── requirements.txt
├── run.py
└── test_customer_schema.py
```

## API Endpoints

### Customers

| HTTP method | Endpoint | Description |
|---|---|---|
| GET | `/api/customers/` | Retrieve all customers |
| GET | `/api/customers/<customer_id>` | Retrieve a customer by ID |
| POST | `/api/customers/` | Create a customer |
| PUT | `/api/customers/<customer_id>` | Update a customer |
| GET | `/api/customers/<customer_id>/order-history` | Retrieve a customer's orders and order details |

### Products

| HTTP method | Endpoint | Description |
|---|---|---|
| GET | `/api/products/` | Retrieve all products |
| GET | `/api/products/<product_id>` | Retrieve a product by ID |
| POST | `/api/products/` | Create a product |
| PUT | `/api/products/<product_id>` | Update a product |

### Orders

| HTTP method | Endpoint | Description |
|---|---|---|
| GET | `/api/orders/` | Retrieve all orders |
| GET | `/api/orders/<order_id>` | Retrieve an order by ID |
| POST | `/api/orders/` | Create an order |
| PUT | `/api/orders/<order_id>` | Update an order |

## Application Architecture

The application uses a layered MVC-style structure:

```text
             HTTP Request
                  |
                  v
              Controller
                  |
                  v
          Schema Validation
                  |
                  v
               Service
                  |
                  v
            SQLAlchemy ORM
                  |
                  v
                MySQL
```

- **Controllers:** Handle incoming HTTP requests and return HTTP responses.
- **Models:** Represent database tables and relationships.
- **Schemas:** Validate incoming data and serialize response data.
- **Services:** Contain database operations and application logic.
- **Tests:** Verify controller behavior using mocked service methods.

## Prerequisites

- Python installed
- MySQL Server installed and running
- The Northwind database imported into MySQL

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

Replace `YOUR_REPOSITORY_URL` with the HTTPS URL of your GitHub repository.

### 2. Navigate to the project directory

```powershell
cd northwind_rest_api
```

### 3. Create a virtual environment

```powershell
python -m venv venv
```

### 4. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```powershell
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root directory. Add your own MySQL connection details:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost/northwind
```

Replace `username` and `password` with your MySQL credentials. Do not commit the `.env` file or share database passwords.

### 7. Run the application

```powershell
python run.py
```

The API will be available locally at:

`http://127.0.0.1:5000`

## Running Tests

From the project root, run:

```powershell
pytest -v
```

The controller tests use mocks to isolate controller behavior from actual database operations.

## Logging

Application logs are written to:

```text
logs/app.log
```

## Version Control

The project uses Git for version control and GitHub for repository hosting.

---

**Built with Python, Flask, MySQL, and SQLAlchemy.**
