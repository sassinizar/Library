import pytest
from app import app, db
from pymongo import MongoClient

@pytest.fixture
def client():
    # Set up a test client
    app.config['TESTING'] = True
    test_client = app.test_client()

    # Use a test database
    app.config['MONGODB_URI'] = 'mongodb://localhost:27017/mediadb'
    client = MongoClient(app.config['MONGODB_URI'])
    test_db = client.get_database()
    db.drop_collection('user')  # Clear data for isolated tests
    db.drop_collection('media')
    db.drop_collection('borrowing')
    yield test_client  # Provide the test client
    client.drop_database('testdb')  # Clean up after tests

def test_home(client):
    """Test the home endpoint"""
    response = client.get('/')
    assert response.status_code == 404  # Example: Update based on your routes

def test_user_creation(client):
    """Test user creation endpoint"""
    payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "securepassword"
    }
    response = client.post('/users', json=payload)
    assert response.status_code == 201
    assert response.json['username'] == "testuser"
