
from flask import Blueprint, request
from app.services.productService import (
    getAllProducts,
    getProductById,
    createProduct,
    updateProduct,
    deleteProduct,
)

products_bp = Blueprint("products", __name__)


# GET all products
@products_bp.route("/", methods=["GET"])
def get_products():
    return {
        "data": getAllProducts()
    }, 200


# GET one product
@products_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = getProductById(product_id)

    if product is None:
        return {"message": "Product not found"}, 404
    
    return {"data": product}, 200



# CREATE a product
@products_bp.route("/", methods=["POST"])
def create_product():
    data = request.get_json()

    if not data:
        return {
            "message": "Request body is required"
        }, 400

    name = data.get("name")
    price = data.get("price")

    if not name or price is None:
        return {
            "message": "Name and price are required"
        }, 400

    try:
        price = float(price)
    except (ValueError, TypeError):
        return {
            "message": "Price must be a number"
        }, 400

    if price < 0:
        return {
            "message": "Price cannot be negative"
        }, 400

    product = createProduct(name, price)

    return {
        "message": "Product created successfully",
        "data": product
    }, 201


# UPDATE a product
@products_bp.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()

    if not data:
        return {
            "message": "Request body is required"
        }, 400

    name = data.get("name")
    price = data.get("price")

    if not name or price is None:
        return {
            "message": "Name and price are required"
        }, 400

    try:
        price = float(price)
    except (ValueError, TypeError):
        return {
            "message": "Price must be a number"
        }, 400

    if price < 0:
        return {
            "message": "Price cannot be negative"
        }, 400

    product = updateProduct(product_id, name, price)

    if product is None:
        return {
                "message": "Product not found"
            }, 404
        
    return {
        "message": "Product updated successfully",
        "data": product
    }, 200

    

# DELETE a product
@products_bp.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = deleteProduct(product_id)

    if product is None:
        return {
                "message": "Product not found"
            }, 404
    return {
        "message": "Product deleted successfully",
        "data": product
    }, 200


