from flask import Blueprint, request, jsonify
from app.services.order_service import (
    get_all_orders, get_order_by_id,
    create_order, delete_order
)

order_bp = Blueprint("orders", __name__)

@order_bp.route("/", methods=["GET"])
def list_orders():
    orders = get_all_orders()
    return jsonify([order.to_dict() for order in orders]), 200

@order_bp.route("/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = get_order_by_id(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order.to_dict()), 200

@order_bp.route("/", methods=["POST"])
def add_order():
    data = request.json
    order = create_order(data)
    return jsonify(order.to_dict()), 201

@order_bp.route("/<int:order_id>", methods=["DELETE"])
def remove_order(order_id):
    order = delete_order(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify({"message": "Order deleted"}), 200
