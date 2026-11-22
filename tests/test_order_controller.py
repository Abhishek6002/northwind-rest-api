from unittest.mock import patch
from app import create_app


def test_get_orders():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        with patch(
            "app.controllers.order_controller.OrderService.get_all_orders",
            return_value=[]
        ):
            response = client.get("/api/orders/")

    assert response.status_code == 200
    assert response.get_json() == []


def test_get_order_not_found():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        with patch(
            "app.controllers.order_controller.OrderService.get_order_by_id",
            return_value=None
        ):
            response = client.get("/api/orders/999999")

    assert response.status_code == 404
