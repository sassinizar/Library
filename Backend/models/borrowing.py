# models/borrowing.py
from bson import ObjectId
from datetime import datetime, timedelta

class Borrowing:
    def __init__(self, db):
        self.collection = db['borrowing']
    
    def borrow_media(self, user_id, media_id, borrow_period_days=14):
        borrowing = {
            'user_id': ObjectId(user_id),
            'media_id': ObjectId(media_id),
            'borrow_date': datetime.utcnow(),
            'due_date': datetime.utcnow() + timedelta(days=borrow_period_days),
            'returned': False
        }
        return self.collection.insert_one(borrowing)
    
    def return_media(self, borrowing_id):
        return self.collection.update_one(
            {'_id': ObjectId(borrowing_id)},
            {'$set': {
                'returned': True,
                'return_date': datetime.utcnow()
            }}
        )
    
    def get_user_borrowings(self, user_id):
        return list(self.collection.find({
            'user_id': ObjectId(user_id),
            'returned': False
        }))
