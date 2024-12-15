class Config:
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/media_library')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')