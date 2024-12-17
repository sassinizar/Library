# routes/user_routes.py
from flask import Blueprint, request, jsonify
from models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    try:
        user = User(db).create_user(
            data['username'], 
            data['email'], 
            data['password']
        )
        return jsonify({'message': 'User registered successfully', 'user_id': str(user.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    user = User(db).authenticate_user(data['email'], data['password'])
    if user:
        return jsonify({'message': 'Login successful', 'user_id': str(user['_id'])}), 200
    return jsonify({'error': 'Invalid credentials'}), 401
