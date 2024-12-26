# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Use proper authentication credentials in MongoDB URI
    MONGODB_URI = 'mongodb://admin:secret@mongodb:27017/mediadb?authSource=admin'
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret')
    DEBUG = os.getenv('FLASK_DEBUG', True)