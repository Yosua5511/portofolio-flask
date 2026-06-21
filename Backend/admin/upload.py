from flask import Blueprint, request, jsonify
import cloudinary
import cloudinary.uploader
from config import Config

# Inisialisasi Cloudinary dari config.py
cloudinary.config(
    cloud_name = Config.CLOUDINARY_CLOUD_NAME,
    api_key = Config.CLOUDINARY_API_KEY,
    api_secret = Config.CLOUDINARY_API_SECRET
)

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/api/admin/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "Tidak ada file yang dipilih"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"status": "error", "message": "Nama file kosong"}), 400

    try:
        # Proses lempar gambar ke Cloudinary
        upload_result = cloudinary.uploader.upload(file)
        # Mengembalikan link gambar (URL) yang sudah online
        return jsonify({"status": "success", "url": upload_result['secure_url']})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500