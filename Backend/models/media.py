# models/media.py
from bson import ObjectId

class Media:
    def __init__(self, db):
        self.collection = db['media']
    
    def add_media(self, title, media_type, author, isbn=None, publisher=None):
        media = {
            'title': title,
            'type': media_type,
            'author': author,
            'isbn': isbn,
            'publisher': publisher
        }
        return self.collection.insert_one(media)
    
    def search_media(self, query, media_type=None):
        search_query = {'$text': {'$search': query}}
        if media_type:
            search_query['type'] = media_type
        return list(self.collection.find(search_query))
