from flask import Blueprint, request, jsonify
from app.services.product_service import (
    get_all_products, get_product_by_id,
    create_product, update_product, delete_product
)

product_bp = Blueprint("products", __name__)

@product_bp.route("/", methods=["GET"])
def list_products():
    products = get_all_products()
    return jsonify([product.to_dict() for product in products]), 200

@product_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product.to_dict()), 200

@product_bp.route("/", methods=["POST"])
def add_product():
    data = request.json
    product = create_product(data)
    return jsonify(product.to_dict()), 201

@product_bp.route("/<int:product_id>", methods=["PUT"])
def edit_product(product_id):
    data = request.json
    product = update_product(product_id, data)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product.to_dict()), 200

@product_bp.route("/<int:product_id>", methods=["DELETE"])
def remove_product(product_id):
    product = delete_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"message": "Product deleted"}), 200
