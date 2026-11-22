from app.extensions import db
from app.models.product import Product


class ProductService:

    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def get_product_by_id(product_id):
        return db.session.get(Product, product_id)

    @staticmethod
    def create_product(data):
        product = Product(**data)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def update_product(product, data):
        for key, value in data.items():
            setattr(product, key, value)

        db.session.commit()
        return product
