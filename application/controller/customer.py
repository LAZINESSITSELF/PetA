from flask import Blueprint, request, jsonify, current_app
from bson.objectid import ObjectId

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/', methods=['GET'])
def get_customers():
    db = current_app.db
    customers = list(db.customers.find())
    for c in customers:
        c['_id'] = str(c['_id'])
    return jsonify(customers)

@customer_bp.route('/', methods=['POST'])
def create_customer():
    data = request.json
    db = current_app.db
    result = db.customers.insert_one(data)
    return jsonify({ 'inserted_id': str(result.inserted_id) }), 201

@customer_bp.route('/<id>', methods=['PUT'])
def update_customer(id):
    data = request.json
    db = current_app.db
    db.customers.update_one({ '_id': ObjectId(id) }, { '$set': data })
    return jsonify({ 'message': 'Customer updated' })

@customer_bp.route('/<id>', methods=['DELETE'])
def delete_customer(id):
    db = current_app.db
    db.customers.delete_one({ '_id': ObjectId(id) })
    return jsonify({ 'message': 'Customer deleted' })