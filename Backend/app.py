# app.py
from flask import Flask
from pymongo import MongoClient
from routes.user import user_bp
from routes.media import media_bp
from routes.borrowing import borrowing_bp
from config import Config
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    # Load configuration
    app.config.from_object(Config)
    
    # Initialize MongoDB connection
    try:
        client = MongoClient(app.config['MONGODB_URI'])
        db = client.get_default_database()
        app.db = db  # Attach db to app context
        print(f"Connected to MongoDB: {db.name}")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise
    
    # Register blueprints
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(media_bp, url_prefix='/api/medias')
    app.register_blueprint(borrowing_bp, url_prefix='/api/borrowings')

    return app

# Create the Flask application instance
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)