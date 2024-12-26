# routes/user.py
from flask import Blueprint, request, jsonify, current_app
from models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    try:
        user = User(current_app.db).create_user(
            data['username'],
            data['email'],
            data['password']
        )
        return jsonify({
            'message': 'User registered successfully', 
            'user_id': str(user.inserted_id)
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    try:
        user = User(current_app.db).authenticate_user(
            data['email'], 
            data['password']
        )
        if user:
            return jsonify({
                'message': 'Login successful',
                'user_id': str(user['_id'])
            }), 200
        return jsonify({'error': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@user_bp.route('/all', methods=['GET'])
def get_all_users():
    try:
        users = User(current_app.db).get_all_users()
        users_list = [{
            '_id': str(user['_id']),
            'username': user['username'],
            'email': user['email'],
            'role': user.get('role', 'subscriber'),
            'active': user.get('active', True),
        } for user in users]
        return jsonify(users_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400