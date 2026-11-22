\# Northwind REST API



A RESTful API built using Python Flask to manage the Northwind MySQL database.



\## Tech Stack

\- Python

\- Flask

\- MySQL

\- Flask-SQLAlchemy (ORM)

\- Marshmallow (Data Validation)

\- Pytest

\- Git \& GitHub



\## Project Structure

```text

northwind\_rest\_api/

├── app/

│   ├── controllers/

│   ├── models/

│   ├── schemas/

│   ├── services/

│   ├── config.py

│   └── extensions.py

├── tests/

├── logs/

├── run.py

├── requirements.txt

└── .gitignore

```



\## Features

\- Customer CRUD operations

\- Product CRUD operations

\- Order CRUD operations

\- Customer order history with order details and product information

\- Input validation using Marshmallow

\- Database operations using SQLAlchemy ORM

\- Layered MVC architecture

\- Application logging

\- Unit testing with mocked service calls



\## Setup Instructions



1\. Clone the repository:

&#x20;  `git clone YOUR\_REPOSITORY\_URL`



2\. Navigate into the project:

&#x20;  `cd northwind\_rest\_api`



3\. Create a virtual environment:

&#x20;  `python -m venv venv`



4\. Activate it:

&#x20;  `.\\venv\\Scripts\\Activate.ps1`



5\. Install dependencies:

&#x20;  `pip install -r requirements.txt`



6\. Create a `.env` file and configure your MySQL connection:

&#x20;  `DATABASE\_URL=mysql+pymysql://username:password@localhost/northwind`



7\. Start the application:

&#x20;  `python run.py`



\## API Endpoints



| Method | Endpoint | Description |

|---|---|---|

| GET | `/api/customers/` | Get all customers |

| GET | `/api/customers/<id>` | Get customer |

| POST | `/api/customers/` | Create customer |

| PUT | `/api/customers/<id>` | Update customer |

| GET | `/api/products/` | Get all products |

| POST | `/api/products/` | Create product |

| PUT | `/api/products/<id>` | Update product |

| GET | `/api/orders/` | Get all orders |

| POST | `/api/orders/` | Create order |

| PUT | `/api/orders/<id>` | Update order |

| GET | `/api/customers/<id>/order-history` | Get customer order history |



\## Run Tests



```bash

pytest -v

```



\## Architecture



Request → Controller → Schema Validation → Service → SQLAlchemy ORM → MySQL



