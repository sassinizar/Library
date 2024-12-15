from flask import Flask, jsonify, request
from pymongo import MongoClient
from config import Config
from models.user import User
from models.media import Media
from models.borrowing import Borrowing

app = Flask(__name__)
app.config.from_object(Config)

# MongoDB Connection
client = MongoClient(app.config['MONGODB_URI'])
db = client.get_default_database()

# Initialize models
user_model = User(db)
media_model = Media(db)
borrowing_model = Borrowing(db)