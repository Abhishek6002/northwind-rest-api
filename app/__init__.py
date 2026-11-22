import logging
import os

from flask import Flask

from app.config import Config
from app.extensions import db
from app.models import Customer, Product, Order, OrderDetail
from app.controllers.customer_controller import customer_bp
from app.controllers.product_controller import product_bp
from app.controllers.order_controller import order_bp 
from app.controllers.order_history_controller import history_bp

def configure_logging(app):
    log_directory = os.path.join(app.root_path, "..", "logs")
    os.makedirs(log_directory, exist_ok=True)

    log_file = os.path.join(log_directory, "app.log")

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    configure_logging(app)

    db.init_app(app)

    app.logger.info("Flask application initialized successfully")

    app.register_blueprint(customer_bp)

    app.register_blueprint(product_bp)

    app.register_blueprint(order_bp)

    app.register_blueprint(history_bp)

    return app
   
