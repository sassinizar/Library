# app.py
from flask import Flask
from pymongo import MongoClient
from routes.user import user_bp
from config import Config

def create_app():
    app = Flask(__name__)
    
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
    
    return app

# Create the Flask application instance
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)