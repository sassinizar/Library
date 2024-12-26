# models/user.py
from bson import ObjectId
import bcrypt

class User:
    def __init__(self, db):
        self.collection = db['user']
    
    def create_user(self, username, email, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = {
            'username': username,
            'email': email,
            'password': hashed_password,
            'role': 'subscriber',
            'active': True
        }
        return self.collection.insert_one(user)
    
    def authenticate_user(self, email, password):
        user = self.collection.find_one({'email': email})
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return user
        return None
    
    def get_user_by_id(self, user_id):
        return self.collection.find_one({'_id': ObjectId(user_id)})
    
    # Add this method to get all users
    def get_all_users(self):
        return list(self.collection.find())