# application/controller/auth.py
from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    verify_jwt_in_request,
    get_jwt
)

auth_bp = Blueprint('auth', __name__)
_blocklist = set()

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json or {}
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'msg': 'username & password required'}), 400

    db = current_app.db

    owner_exists = db.users.count_documents({'role': 'owner'}, limit=1) > 0

    if owner_exists:
        try:
            verify_jwt_in_request()
        except Exception:
            return jsonify({'msg': 'Authentication required to add admin'}), 401

        claims = get_jwt()
        if claims.get('role') != 'owner':
            return jsonify({'msg': 'Only owner can create admin users'}), 403

        role = 'admin'
    else:
        role = 'owner'

    if db.users.find_one({'username': username}):
        return jsonify({'msg': 'User already exists'}), 400

    hashed = generate_password_hash(password)
    new = {
        'username': username,
        'password': hashed,
        'role': role
    }
    result = db.users.insert_one(new)

    return jsonify({
        'msg': f'{role.title()} account created',
        'user_id': str(result.inserted_id),
        'role': role
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json or {}
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'msg': 'username & password required'}), 400

    db = current_app.db
    user = db.users.find_one({'username': username})
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'msg': 'Bad username or password'}), 401

    access_token = create_access_token(
        identity=str(user['_id']),
        additional_claims={'role': user['role']}
    )
    return jsonify({
        'access_token': access_token,
        'role': user['role']
    }), 200

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    _blocklist.add(jti)
    return jsonify({'msg': 'Successfully logged out'}), 200

# @auth_bp.app.jwt.token_in_blocklist_loader
# def check_if_token_revoked(jwt_header, jwt_payload):
#     return jwt_payload['jti'] in _blocklist
