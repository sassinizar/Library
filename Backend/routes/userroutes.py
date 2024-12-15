from flask import Flask, jsonify, request
from pymongo import MongoClient
from config import Config
from models.user import User
from models.media import Media
from models.borrowing import Borrowing

app.route('/api/users/register', methods=['POST'])
def register_user():
    data = request.json
    try:
        user = user_model.create_user(
            data['username'], 
            data['email'], 
            data['password']
        )
        return jsonify({'message': 'User registered successfully', 'user_id': str(user.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/users/login', methods=['POST'])
def login_user():
    data = request.json
    user = user_model.authenticate_user(data['email'], data['password'])
    if user:
        return jsonify({'message': 'Login successful', 'user_id': str(user['_id'])}), 200
    return jsonify({'error': 'Invalid credentials'}), 401