from app.extensions import db
from app.models.order import Order


class OrderService:

    @staticmethod
    def get_all_orders():
        return Order.query.all()

    @staticmethod
    def get_order_by_id(order_id):
        return db.session.get(Order, order_id)

    @staticmethod
    def create_order(data):
        order = Order(**data)
        db.session.add(order)
        db.session.commit()
        return order

    @staticmethod
    def update_order(order, data):
        for key, value in data.items():
            setattr(order, key, value)

        db.session.commit()
        return order
