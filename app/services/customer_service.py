from app.extensions import db
from app.models.customer import Customer


class CustomerService:

    @staticmethod
    def get_all_customers():
        return Customer.query.all()

    @staticmethod
    def get_customer_by_id(customer_id):
        return db.session.get(Customer, customer_id)

    @staticmethod
    def create_customer(customer_data):
        customer = Customer(**customer_data)

        db.session.add(customer)
        db.session.commit()

        return customer

    @staticmethod
    def update_customer(customer, customer_data):
        for key, value in customer_data.items():
            setattr(customer, key, value)

        db.session.commit()

        return customer