from flask import Flask
from pymongo import MongoClient
from config import Config
from routes.user import user_bp
from routes.borrowing import borrowing_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # MongoDB Connection Setup
    client = MongoClient(app.config['MONGODB_URI'])
    db = client.get_default_database()

    # Register Blueprints (routes)
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(borrowing_bp, url_prefix='/return')
    #app.register_blueprint(borrowing_bp, url_prefix='/borrow')

    return app, db
    
app, db = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)