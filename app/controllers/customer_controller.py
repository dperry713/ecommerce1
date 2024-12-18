from flask import Blueprint, request, jsonify
from app.services.customer_service import (
    get_all_customers, get_customer_by_id,
    create_customer, update_customer, delete_customer
)

customer_bp = Blueprint("customers", __name__)

@customer_bp.route("/", methods=["GET"])
def list_customers():
    customers = get_all_customers()
    return jsonify([customer.to_dict() for customer in customers]), 200

@customer_bp.route("/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = get_customer_by_id(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    return jsonify(customer.to_dict()), 200

@customer_bp.route("/", methods=["POST"])
def add_customer():
    data = request.json
    customer = create_customer(data)
    return jsonify(customer.to_dict()), 201

@customer_bp.route("/<int:customer_id>", methods=["PUT"])
def edit_customer(customer_id):
    data = request.json
    customer = update_customer(customer_id, data)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    return jsonify(customer.to_dict()), 200

@customer_bp.route("/<int:customer_id>", methods=["DELETE"])
def remove_customer(customer_id):
    customer = delete_customer(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    return jsonify({"message": "Customer deleted"}), 200
