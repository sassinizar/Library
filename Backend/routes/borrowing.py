from flask import Blueprint, request, jsonify, current_app
from models.borrowing import Borrowing
from bson.json_util import dumps

borrowing_bp = Blueprint('borrowing', __name__)

@borrowing_bp.route('/borrow', methods=['POST'])
def borrow_media():
    data = request.json
    borrowing_model = Borrowing(current_app.db)  # Instantiate the Borrowing model
    try:
        borrowing = borrowing_model.borrow_media(
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
        borrowing = Borrowing().return_media(data['borrowing_id'])
        return jsonify({'message': 'Media returned successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400



@borrowing_bp.route('/all', methods=['GET'])
def get_borrowings():
    try:
        borrowing_model = Borrowing(current_app.db)
        borrowings = borrowing_model.get_all_borrowings()
        return jsonify({'borrowings': dumps(borrowings)}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
