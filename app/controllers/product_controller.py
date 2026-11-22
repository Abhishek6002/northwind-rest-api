from flask import Blueprint, request, jsonify, current_app
from marshmallow import ValidationError

from app.services.product_service import ProductService
from app.schemas.product_schema import ProductSchema


product_bp = Blueprint(
    "products",
    __name__,
    url_prefix="/api/products"
)

product_schema = ProductSchema()


@product_bp.route("/", methods=["GET"])
def get_products():
    products = ProductService.get_all_products()
    return jsonify(product_schema.dump(products, many=True)), 200


@product_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = ProductService.get_product_by_id(product_id)

    if product is None:
        return jsonify({"message": "Product not found"}), 404

    return jsonify(product_schema.dump(product)), 200


@product_bp.route("/", methods=["POST"])
def create_product():
    data = request.get_json()

    if not data:
        return jsonify({"message": "Request body is required"}), 400

    try:
        validated_data = product_schema.load(data)
        product = ProductService.create_product(validated_data)

        return jsonify({
            "message": "Product created successfully",
            "product": product_schema.dump(product)
        }), 201

    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    except Exception:
        current_app.logger.exception("Error creating product")
        return jsonify({"message": "Internal server error"}), 500


@product_bp.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = ProductService.get_product_by_id(product_id)

    if product is None:
        return jsonify({"message": "Product not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"message": "Request body is required"}), 400

    try:
        validated_data = product_schema.load(data, partial=True)
        updated_product = ProductService.update_product(
            product, validated_data
        )

        return jsonify({
            "message": "Product updated successfully",
            "product": product_schema.dump(updated_product)
        }), 200

    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    except Exception:
        current_app.logger.exception("Error updating product")
        return jsonify({"message": "Internal server error"}), 500
