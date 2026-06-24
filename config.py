import os
from dotenv import load_dotenv

# Memuat variabel dari file .env
load_dotenv()

class Config:
    TIDB_HOST = os.getenv("TIDB_HOST")
    TIDB_PORT = int(os.getenv("TIDB_PORT", 4000))
    TIDB_USER = os.getenv("TIDB_USER")
    TIDB_PASSWORD = os.getenv("TIDB_PASSWORD")
    TIDB_DB_NAME = os.getenv("TIDB_DB_NAME")
    
    CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
    CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
    
    RESEND_API_KEY = os.getenv("RESEND_API_KEY")
    FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")