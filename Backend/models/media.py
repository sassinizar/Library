from bson import ObjectId

class Media:
    def __init__(self, db):
        self.collection = db['media']
    
    def add_media(self, title, media_type, author, isbn, publisher):
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
    
    def update_media_availability(self, media_id, is_available):
        result = self.collection.update_one(
            {'_id': ObjectId(media_id)},  # Find the media by its ObjectId
            {'$set': {'is_available': is_available}}  # Update the 'is_available' field
        )
        if result.modified_count == 0:
            raise Exception(f"Media with ID {media_id} not found or already set to {is_available}")
        return result
    
    def get_all_medias(self):
        return list(self.collection.find())
    
    def delete_media(self, media_id):
        """
        Deletes a media document by its ID.
        """
        result = self.collection.delete_one({'_id': ObjectId(media_id)});
        return result.deleted_count > 0
    
    def update_media(self, media_id, update_data):
        result = self.collection.update_one(
            {"_id": ObjectId(media_id)}, 
            {"$set": update_data}
        )
        return result.modified_count > 0