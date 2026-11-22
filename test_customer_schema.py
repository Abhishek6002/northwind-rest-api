from app.schemas.customer_schema import CustomerSchema
from marshmallow import ValidationError

customer_schema = CustomerSchema()

# Test 1: Valid customer
customer_data = {
    "first_name": "John",
    "last_name": "Smith",
    "email_address": "john@gmail.com",
    "city": "Bangalore"
}

try:
    result = customer_schema.load(customer_data)
    print("Valid customer:", result)
except ValidationError as error:
    print("Validation failed:", error.messages)


# Test 2: Invalid email
customer_data = {
    "first_name": "John",
    "email_address": "invalid-email"
}

try:
    result = customer_schema.load(customer_data)
    print("Valid customer:", result)
except ValidationError as error:
    print("Validation failed:", error.messages)


# Test 3: First name exceeding 50 characters
customer_data = {
    "first_name": "A" * 51
}

try:
    result = customer_schema.load(customer_data)
    print("Valid customer:", result)
except ValidationError as error:
    print("Validation failed:", error.messages)