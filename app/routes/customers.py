from flask import Blueprint, request

from app.services.customer_service import (
    getAllCustomers,
    getCustomerById,
    createCustomer,
    updateCustomer,
    deleteCustomer
)

customers_bp = Blueprint("customers", __name__)

# GET all customers
@customers_bp.route("/", methods=["GET"])
def get_customers():
    return {
        "data": getAllCustomers()
    }, 200

# GET one customer
@customers_bp.route("/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = getCustomerById(customer_id)

    if customer is None:
        return {
            "message": "Customer not found"
        }, 404

    return {
        "data": customer
    }

# CREATE a customer
@customers_bp.route("/", methods=["POST"])
def create_customer():
    data = request.get_json()

    if not data:
        return {
            "message": "Request body is required"
        }

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    if not name or not email or not phone:
        return {
            "message": "Name, email and phone are required"
        }

    customer = createCustomer(name, email, phone)

    return {
        "message": "Customer created successfully",
        "data": customer
    }, 201


# UPDATE a customer
@customers_bp.route("/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    data = request.get_json()

    if not data:
        return {
            "message": "Request body is required"
        }

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    if not name or not email or not phone:
        return {
            "message": "Name, email and phone are required"
        }, 400

    customer = updateCustomer(
        customer_id,
        name,
        email,
        phone
    )

    if customer is None:
        return {
            "message": "Customer not found"
        }, 404

    return {
        "message": "Customer updated successfully",
        "data": customer
    }, 200

# DELETE a customer
@customers_bp.route("/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    customer = deleteCustomer(customer_id)

    if customer is None:
        return {
            "message": "Customer not found"
        }, 404

    return {
        "message": "Customer deleted successfully",
        "data": customer
    }, 200

