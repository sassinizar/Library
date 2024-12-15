from pymongo import MongoClient
from bson import ObjectId
import bcrypt

class Media:
    def __init__(self, db):
        self.collection = db['media']
    
    def add_media(self, title, media_type, author, isbn=None, publisher=None):
        media = {
            'title': title,
            'type': media_type,
            'author': author,
            'isbn': isbn,
            'publisher': publisher,
            'available': True,
            'total_copies': 1,
            'current_copies': 1
        }
        return self.collection.insert_one(media)
    
    def search_media(self, query=None, media_type=None):
        search_filter = {}
        if query:
            search_filter['$or'] = [
                {'title': {'$regex': query, '$options': 'i'}},
                {'author': {'$regex': query, '$options': 'i'}}
            ]
        if media_type:
            search_filter['type'] = media_type
        
        return list(self.collection.find(search_filter))
    
    def update_media_availability(self, media_id, available):
        return self.collection.update_one(
            {'_id': ObjectId(media_id)},
            {'$set': {'available': available}}
        )