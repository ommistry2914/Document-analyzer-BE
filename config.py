import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
JWT_SECRET = os.getenv("JWT_SECRET", "your-secret-key")
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
INDEX_DIR = os.getenv("INDEX_DIR", "indexes")
