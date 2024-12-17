import os  # Add this line to import the os module
from dotenv import load_dotenv  # Optional: If using a .env file for environment variables

# Load environment variables from a .env file if it exists
load_dotenv()

class Config:
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/mediadb')
    SECRET_KEY = os.getenv('SECRET_KEY', 'nizar')