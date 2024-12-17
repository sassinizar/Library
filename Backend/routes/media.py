from flask import Flask, jsonify, request
from pymongo import MongoClient
from config import Config
from models.user import User
from models.media import Media
from models.borrowing import Borrowing

app.route('/api/borrow', methods=['POST'])
def borrow_media():
    data = request.json
    try:
        borrowing = borrowing_model.borrow_media(
            data['user_id'], 
            data['media_id']
        )
        media_model.update_media_availability(data['media_id'], False)
        return jsonify({'message': 'Media borrowed successfully', 'borrowing_id': str(borrowing.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/return', methods=['POST'])
def return_media():
    data = request.json
    try:
        borrowing_model.return_media(data['borrowing_id'])
        media_model.update_media_availability(data['media_id'], True)
        return jsonify({'message': 'Media returned successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
