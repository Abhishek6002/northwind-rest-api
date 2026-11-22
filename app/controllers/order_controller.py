from flask import Blueprint, request, jsonify, current_app
from marshmallow import ValidationError

from app.services.order_service import OrderService
from app.schemas.order_schema import OrderSchema


order_bp = Blueprint(
    "orders",
    __name__,
    url_prefix="/api/orders"
)

order_schema = OrderSchema()


@order_bp.route("/", methods=["GET"])
def get_orders():
    orders = OrderService.get_all_orders()
    return jsonify(order_schema.dump(orders, many=True)), 200


@order_bp.route("/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = OrderService.get_order_by_id(order_id)

    if order is None:
        return jsonify({"message": "Order not found"}), 404

    return jsonify(order_schema.dump(order)), 200


@order_bp.route("/", methods=["POST"])
def create_order():
    data = request.get_json()

    if not data:
        return jsonify({"message": "Request body is required"}), 400

    try:
        validated_data = order_schema.load(data)
        order = OrderService.create_order(validated_data)

        return jsonify({
            "message": "Order created successfully",
            "order": order_schema.dump(order)
        }), 201

    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    except Exception:
        current_app.logger.exception("Error creating order")
        return jsonify({"message": "Internal server error"}), 500


@order_bp.route("/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    order = OrderService.get_order_by_id(order_id)

    if order is None:
        return jsonify({"message": "Order not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"message": "Request body is required"}), 400

    try:
        validated_data = order_schema.load(data, partial=True)
        updated_order = OrderService.update_order(order, validated_data)

        return jsonify({
            "message": "Order updated successfully",
            "order": order_schema.dump(updated_order)
        }), 200

    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    except Exception:
        current_app.logger.exception("Error updating order")
        return jsonify({"message": "Internal server error"}), 500
