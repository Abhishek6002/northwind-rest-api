from unittest.mock import patch
from app import create_app


def test_get_products():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        with patch(
            "app.controllers.product_controller.ProductService.get_all_products",
            return_value=[]
        ):
            response = client.get("/api/products/")

    assert response.status_code == 200
    assert response.get_json() == []


def test_get_product_not_found():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        with patch(
            "app.controllers.product_controller.ProductService.get_product_by_id",
            return_value=None
        ):
            response = client.get("/api/products/999999")

    assert response.status_code == 404
