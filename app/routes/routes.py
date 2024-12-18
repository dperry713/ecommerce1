from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService
from app.services.customer_service import CustomerService
from app.services.order_service import OrderService

# Create a Blueprint for the routes
routes_bp = Blueprint('routes', __name__)

# Product Routes
@routes_bp.route('/products', methods=['GET'])
def get_all_products():
    try:
        products = ProductService.get_all_products()
        return jsonify(products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    try:
        product = ProductService.get_product_by_id(product_id)
        if product:
            return jsonify(product), 200
        return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes_bp.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        product = ProductService.create_product(data)
        return jsonify(product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        data = request.get_json()
        updated_product = ProductService.update_product(product_id, data)
        if updated_product:
            return jsonify(updated_product), 200
        return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        result = ProductService.delete_product(product_id)
        if result:
            return jsonify({"message": "Product deleted"}), 200
        return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Customer Routes
@routes_bp.route('/customers', methods=['GET'])
def get_all_customers():
    try:
        customers = CustomerService.get_all_customers()
        return jsonify(customers), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes_bp.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer_by_id(customer_id):
    try:
        customer = CustomerService.get_customer_by_id(customer_id)
        if customer:
            return jsonify(customer), 200
        return jsonify({"error": "Customer not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes_bp.route('/customers', methods=['POST'])
def create_customer():
    try:
        data = request.get_json()
        customer = CustomerService.create_customer(data)
        return jsonify(customer), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes_bp.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    try:
        data = request.get_json()
        updated_customer = CustomerService.update_customer(customer_id, data)
        if updated_customer:
            return jsonify(updated_customer), 200
        return jsonify({"error": "Customer not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes_bp.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        result = CustomerService.delete_customer(customer_id)
        if result:
            return jsonify({"message": "Customer deleted"}), 200
        return jsonify({"error": "Customer not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Order Routes
@routes_bp.route('/orders', methods=['GET'])
def get_all_orders():
    try:
        orders = OrderService.get_all_orders()
        return jsonify(orders), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    try:
        order = OrderService.get_order_by_id(order_id)
        if order:
            return jsonify(order), 200
        return jsonify({"error": "Order not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes_bp.route('/orders', methods=['POST'])
def create_order():
    try:
        data = request.get_json()
        order = OrderService.create_order(data)
        return jsonify(order), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes_bp.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        data = request.get_json()
        updated_order = OrderService.update_order(order_id, data)
        if updated_order:
            return jsonify(updated_order), 200
        return jsonify({"error": "Order not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes_bp.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        result = OrderService.delete_order(order_id)
        if result:
            return jsonify({"message": "Order deleted"}), 200
        return jsonify({"error": "Order not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
