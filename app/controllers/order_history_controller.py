from flask import Blueprint, jsonify
from sqlalchemy.orm import joinedload

from app.extensions import db
from app.models.customer import Customer
from app.models.order import Order
from app.models.order_detail import OrderDetail
from app.schemas.order_schema import OrderSchema
from app.schemas.product_schema import ProductSchema

history_bp = Blueprint("history", __name__, url_prefix="/api/customers")


@history_bp.route("/<int:customer_id>/order-history", methods=["GET"])
def get_order_history(customer_id):

    customer = db.session.query(Customer).options(
        joinedload(Customer.orders)
        .joinedload(Order.order_details)
        .joinedload(OrderDetail.product)
    ).filter_by(id=customer_id).first()

    if customer is None:
        return jsonify({"message": "Customer not found"}), 404

    orders = []

    for order in customer.orders:
        order_data = OrderSchema().dump(order)
        order_data["order_details"] = []

        for detail in order.order_details:
            order_data["order_details"].append({
                "id": detail.id,
                "product_id": detail.product_id,
                "quantity": str(detail.quantity),
                "unit_price": str(detail.unit_price) if detail.unit_price is not None else None,
                "discount": detail.discount,
                "product": ProductSchema().dump(detail.product) if detail.product else None
            })

        orders.append(order_data)

    return jsonify({
        "customer_id": customer.id,
        "customer_name": customer.first_name,
        "orders": orders
    }), 200
