from flask import Blueprint, jsonify, request
from model import get_db_connection
from config import Config
import resend

# Inisialisasi API Key Resend
resend.api_key = Config.RESEND_API_KEY

utama_bp = Blueprint('utama', __name__)

# API untuk mengambil seluruh data portofolio dari TiDB
@utama_bp.route('/api/data', methods=['GET'])
def get_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM profil LIMIT 1")
        profil = cursor.fetchone()
        
        cursor.execute("SELECT * FROM skill")
        skills = cursor.fetchall()
        
        cursor.execute("SELECT * FROM pengalaman ORDER BY id DESC")
        pengalaman = cursor.fetchall()
        
        cursor.execute("SELECT * FROM proyek ORDER BY id DESC")
        proyek = cursor.fetchall()
        
        conn.close()
        
        return jsonify({
            "status": "success",
            "data": {
                "profil": profil,
                "skills": skills,
                "pengalaman": pengalaman,
                "proyek": proyek
            }
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# API untuk menerima pesan dari form kontak & simpan ke DB
@utama_bp.route('/api/kirim-pesan', methods=['POST'])
def kirim_pesan():
    try:
        data = request.json
        nama = data.get('nama')
        email = data.get('email')
        pesan = data.get('pesan')

        # Simpan ke database TiDB
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO kontak (nama_pengirim, email_pengirim, pesan) VALUES (%s, %s, %s)", (nama, email, pesan))
        conn.commit()
        conn.close()

        # Integrasi kirim notifikasi email via Resend
        if Config.RESEND_API_KEY:
            params = {
                "from": "Portfolio Admin <onboarding@resend.dev>",
                "to": ["682024104@student.uksw.edu"], # Target email penerima
                "subject": f"📩 Pesan Baru dari {nama}",
                "html": f"""
                    <h3>Ada pesan baru masuk di Website Portofolio lo!</h3>
                    <p><strong>Nama:</strong> {nama}</p>
                    <p><strong>Email:</strong> {email}</p>
                    <div style="background: #f4f4f4; padding: 15px; border-radius: 8px; color: #333; margin-top: 10px;">
                        <strong>Pesan:</strong><br>{pesan}
                    </div>
                """
            }
            resend.Emails.send(params)

        return jsonify({"status": "success", "message": "Pesan berhasil dikirim dan notifikasi email meluncur!"})
    except Exception as e:
        print("=> ERROR CONTACT FORM:", str(e)) # Radar error
        return jsonify({"status": "error", "message": str(e)})