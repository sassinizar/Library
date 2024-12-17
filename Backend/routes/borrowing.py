# routes/borrowing_routes.py
from flask import Blueprint, request, jsonify
from models.borrowing import Borrowing

borrowing_bp = Blueprint('borrowing', __name__)

@borrowing_bp.route('/borrow', methods=['POST'])
def borrow_media():
    data = request.json
    try:
        borrowing = Borrowing(db).borrow_media(
            data['user_id'], 
            data['media_id'], 
            data.get('borrow_period_days', 14)
        )
        return jsonify({'message': 'Media borrowed successfully', 'borrowing_id': str(borrowing.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@borrowing_bp.route('/return', methods=['POST'])
def return_media():
    data = request.json
    try:
        borrowing = Borrowing(db).return_media(data['borrowing_id'])
        return jsonify({'message': 'Media returned successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
        
@borrowing_bp.route('/', methods=['GET'])
def get_all_borrowings():
    # Implement logic for retrieving borrowings here
    return jsonify(message="Borrowings endpoint works"), 200