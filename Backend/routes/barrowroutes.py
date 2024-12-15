from flask import Flask, jsonify, request
from pymongo import MongoClient
from config import Config
from models.user import User
from models.media import Media
from models.borrowing import Borrowing

@app.route('/api/media/add', methods=['POST'])
def add_media():
    data = request.json
    try:
        media = media_model.add_media(
            data['title'], 
            data['type'], 
            data['author'],
            data.get('isbn'),
            data.get('publisher')
        )
        return jsonify({'message': 'Media added successfully', 'media_id': str(media.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/media/search', methods=['GET'])
def search_media():
    query = request.args.get('query')
    media_type = request.args.get('type')
    media_list = media_model.search_media(query, media_type)
    return jsonify([{**media, '_id': str(media['_id'])} for media in media_list]), 200