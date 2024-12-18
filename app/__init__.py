from flask import Flask
from app.db import db
from app.models import Product, Customer, Order
from app.controllers.product_controller import product_bp
from app.controllers.customer_controller import customer_bp
from app.controllers.order_controller import order_bp
from config import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    # Configure the app using the provided config class
    app.config.from_object(config_class)

    # Initialize the database with the Flask app
    db.init_app(app)

    # Register blueprints for modular routing
    app.register_blueprint(product_bp, url_prefix="/products")
    app.register_blueprint(customer_bp, url_prefix="/customers")
    app.register_blueprint(order_bp, url_prefix="/orders")

    # Create all database tables (if not already created)
    with app.app_context():
        db.create_all()

    return app
