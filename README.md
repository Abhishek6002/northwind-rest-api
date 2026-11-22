
# Northwind REST API

A RESTful API built using Python Flask to manage the Northwind MySQL database. This project demonstrates CRUD operations, database integration, data validation, layered architecture, unit testing, and automated CI using GitHub Actions.

## Tech Stack

- **Language:** Python
- **Framework:** Flask
- **Database:** MySQL
- **ORM:** Flask-SQLAlchemy
- **Validation:** Marshmallow
- **Testing:** Pytest
- **Version Control:** Git and GitHub
- **CI/CD:** GitHub Actions (Continuous Integration)

## Features

- Customer CRUD operations
- Product CRUD operations
- Order CRUD operations
- Retrieve complete customer order history
- View order details and associated product information
- Input validation using Marshmallow
- Database operations using SQLAlchemy ORM
- Layered MVC-style architecture
- Application logging
- Unit testing using Pytest and mocking
- Automated test execution using GitHub Actions

## Project Structure

```text
northwind_rest_api/
├── .github/
│   └── workflows/
│       └── tests.yml
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
├── .gitignore
├── requirements.txt
├── run.py
└── test_customer_schema.py
```

## API Endpoints

### Customer Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/customers/` | Retrieve all customers |
| GET | `/api/customers/<customer_id>` | Retrieve customer by ID |
| POST | `/api/customers/` | Create a customer |
| PUT | `/api/customers/<customer_id>` | Update customer details |
| GET | `/api/customers/<customer_id>/order-history` | Retrieve customer order history |

### Product Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/products/` | Retrieve all products |
| GET | `/api/products/<product_id>` | Retrieve product by ID |
| POST | `/api/products/` | Create a product |
| PUT | `/api/products/<product_id>` | Update product details |

### Order Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/orders/` | Retrieve all orders |
| GET | `/api/orders/<order_id>` | Retrieve order by ID |
| POST | `/api/orders/` | Create an order |
| PUT | `/api/orders/<order_id>` | Update order details |

## Application Architecture

The project follows a layered MVC-style architecture.

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

### Layer Responsibilities

- **Controllers:** Handle HTTP requests and responses.
- **Models:** Represent database tables and relationships.
- **Schemas:** Validate incoming data and serialize responses.
- **Services:** Handle business logic and database operations.
- **Tests:** Verify controller behavior using mocked service methods.

## Installation and Setup

### Prerequisites

Install the following before running the application:

- Python 3.12 or compatible version
- MySQL Server
- MySQL Workbench (recommended)
- Git

You also need the Northwind sample database imported into MySQL.

### Step 1: Clone the Repository

```powershell
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project:

```powershell
cd northwind_rest_api
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the actual GitHub repository URL.

### Step 2: Create a Virtual Environment

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### Step 4: Set Up the Northwind Database

The Northwind database dump is not included in this repository.

Obtain a compatible MySQL version of the Northwind sample database separately.

Using MySQL Workbench:

1. Open MySQL Workbench.
2. Connect to your local MySQL server.
3. Obtain a compatible Northwind `.sql` database dump.
4. If necessary, create a schema named `northwind`.
5. Navigate to **Server → Data Import**.
6. Select **Import from Self-Contained File**.
7. Browse and select the Northwind SQL dump.
8. Select `northwind` as the target schema if prompted.
9. Click **Start Import**.
10. Refresh the Schemas panel and verify that the tables have been imported.

The application expects the database name to be `northwind`.

### Step 5: Configure Environment Variables

Create a `.env` file in the project root directory, alongside `run.py`.

Add your MySQL connection details:

```env
DATABASE_URL=mysql+pymysql://YOUR_USERNAME:YOUR_PASSWORD@localhost/northwind
```

Replace the placeholders with your own MySQL username and password.

If your password contains URL-reserved characters, URL-encode those characters in the connection string.

**Important:** Do not upload your `.env` file or expose your database credentials on GitHub.

### Step 6: Start the Flask Application

```powershell
python run.py
```

The application will run locally at:

`http://127.0.0.1:5000`

## Verify the API

Keep the Flask application running.

Open another PowerShell window and execute the following requests.

### Retrieve All Customers

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/customers/"
```

### Retrieve Customer by ID

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/customers/1"
```

### Retrieve All Products

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/products/"
```

### Retrieve All Orders

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/orders/"
```

### Retrieve Customer Order History

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/customers/1/order-history" | ConvertTo-Json -Depth 10
```

Successful requests should return JSON responses containing the requested database records.

POST and PUT endpoints can be tested by sending JSON request bodies containing the required fields.

## Unit Testing

The project uses Pytest and mocking to test controller behavior independently of actual database operations.

Run the test suite:

```powershell
pytest -v
```

The current test suite contains 8 unit tests covering customer, product, and order controller behavior.

## GitHub Actions - Continuous Integration

GitHub Actions is configured to automatically execute unit tests whenever code is pushed to the `main` branch or a pull request targets `main`.

### CI Workflow

```text
       Developer Pushes Code
                |
                v
       GitHub Actions Starts
                |
                v
       Checkout Repository
                |
                v
         Set Up Python
                |
                v
       Install Dependencies
                |
                v
          Run Pytest
                |
          +-----+-----+
          |           |
          v           v
       SUCCESS      FAILURE
       Green Tick   Red Cross
```

The workflow uses a temporary SQLite database configuration for automated testing and does not require a running MySQL server.

## Logging

Application logs are maintained in:

```text
logs/app.log
```

## Version Control

Git is used for version control, and GitHub hosts the source code.

The repository includes a GitHub Actions workflow for automated unit testing.

---

**Developed using Python, Flask, MySQL, and SQLAlchemy.**
