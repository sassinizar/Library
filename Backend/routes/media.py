from flask import Blueprint, request, jsonify, current_app
from models.media import Media
from models.borrowing import Borrowing

media_bp = Blueprint('media', __name__)

@media_bp.route('/borrow', methods=['POST'])
def borrow_media():
    data = request.json
    borrowing_model = Borrowing(current_app.db)  # Instantiate the Borrowing model
    media_model = Media(current_app.db)  # Instantiate the Media model
    try:
        borrowing =  borrowing_model.borrow_media(
            data['user_id'], 
            data['media_id']
        )
        media_model.update_media_availability(data['media_id'], False)
        return jsonify({'message': 'Media borrowed successfully', 'borrowing_id': str(borrowing.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@media_bp.route('/return', methods=['POST'])
def return_media():
    data = request.json
    try:
        Borrowing.return_media(data['borrowing_id'])
        Media.update_media_availability(data['media_id'], True)
        return jsonify({'message': 'Media returned successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@media_bp.route('/add', methods=['POST'])
def add_media():
    data = request.json
    try:
        media = Media(current_app.db).add_media(
            data['title'],
            data['type'],
            data['author'],
            data['isbn'],
            data['publisher']
        )
        return jsonify({
            'message': 'media added successfully', 
            'media_id': str(media.inserted_id)
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

@media_bp.route('/all', methods=['GET'])
def get_all_medias():
    try:
        medias = Media(current_app.db).get_all_medias()
        media_list = [{
            '_id': str(Media['_id']),
            'title': Media['title'],
            'type': Media['type'],
            'author': Media['author'],
            'isbn': Media['isbn'],
            'publisher': Media['publisher'],
        } for Media in medias]
        return jsonify(media_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@media_bp.route('/delete/<media_id>', methods=['DELETE'])
def delete_media(media_id):
    try:
        media = Media(current_app.db)  # Instantiate the Media model
        success = media.delete_media(media_id)  # Call the delete method from the model

        if success > 0:
            return jsonify({'message': 'Media deleted successfully'}), 200
        else:
            return jsonify({'error': 'Media not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@media_bp.route('/update/<media_id>', methods=['PUT'])
def update_media(media_id):
    data = request.json  # The data to update
    try:
        media_model = Media(current_app.db)
        success = media_model.update_media(media_id, data)
        if success:
            return jsonify({'message': 'Media updated successfully'}), 200
        else:
            return jsonify({'error': 'Media not found or no changes made'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400
