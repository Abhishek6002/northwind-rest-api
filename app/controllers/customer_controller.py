from flask import Blueprint, request, jsonify, current_app
from marshmallow import ValidationError

from app.services.customer_service import CustomerService
from app.schemas.customer_schema import CustomerSchema


customer_bp = Blueprint(
    "customers",
    __name__,
    url_prefix="/api/customers"
)

customer_schema = CustomerSchema()


# GET: Fetch all customers
@customer_bp.route("/", methods=["GET"])
def get_customers():
    customers = CustomerService.get_all_customers()

    return jsonify(customer_schema.dump(customers, many=True)), 200

# GET: Fetch a customer by ID
@customer_bp.route("/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = CustomerService.get_customer_by_id(customer_id)

    if customer is None:
        return jsonify({"message": "Customer not found"}), 404

    return jsonify(customer_schema.dump(customer)), 200

# POST: Create a new customer
@customer_bp.route("/", methods=["POST"])
def create_customer():
    data = request.get_json()

    if not data:
        return jsonify({"message": "Request body is required"}), 400

    try:
        validated_data = customer_schema.load(data)

        customer = CustomerService.create_customer(validated_data)

        return jsonify({
            "message": "Customer created successfully",
            "customer": customer_schema.dump(customer)
        }), 201

    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    except Exception:
        current_app.logger.exception("Error creating customer")
        return jsonify({"message": "Internal server error"}), 500

# PUT: Update an existing customer
@customer_bp.route("/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    customer = CustomerService.get_customer_by_id(customer_id)

    if customer is None:
        return jsonify({"message": "Customer not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"message": "Request body is required"}), 400

    try:
        validated_data = customer_schema.load(data, partial=True)

        updated_customer = CustomerService.update_customer(
            customer,
            validated_data
        )

        return jsonify({
            "message": "Customer updated successfully",
            "customer": customer_schema.dump(updated_customer)
        }), 200

    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    except Exception:
        current_app.logger.exception("Error updating customer")
        return jsonify({"message": "Internal server error"}), 500