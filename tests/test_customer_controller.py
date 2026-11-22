from unittest.mock import patch
from app import create_app


def test_get_customers():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        with patch(
            "app.controllers.customer_controller.CustomerService.get_all_customers",
            return_value=[]
        ):
            response = client.get("/api/customers/")

    assert response.status_code == 200
    assert response.get_json() == []


def test_get_customer_not_found():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        with patch(
            "app.controllers.customer_controller.CustomerService.get_customer_by_id",
            return_value=None
        ):
            response = client.get("/api/customers/999999")

    assert response.status_code == 404
    assert response.get_json()["message"] == "Customer not found"


def test_create_customer():
    app = create_app()
    app.config["TESTING"] = True

    customer = {
        "id": 100,
        "first_name": "Test",
        "last_name": "User",
        "email_address": "test@gmail.com"
    }

    with app.test_client() as client:
        with patch(
            "app.controllers.customer_controller.CustomerService.create_customer",
            return_value=customer
        ):
            response = client.post(
                "/api/customers/",
                json={
                    "first_name": "Test",
                    "last_name": "User",
                    "email_address": "test@gmail.com"
                }
            )

    assert response.status_code == 201
    assert response.get_json()["message"] == "Customer created successfully"


def test_create_customer_invalid_email():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.post(
            "/api/customers/",
            json={"email_address": "invalid-email"}
        )

    assert response.status_code == 400
