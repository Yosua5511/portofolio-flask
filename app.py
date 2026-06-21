from flask import Flask, send_from_directory
from model import get_db_connection 

# Import Seluruh Blueprint Backend
from Backend.utama.utama import utama_bp
from Backend.admin.login import login_bp
from Backend.admin.upload import upload_bp # Import mesin upload Cloudinary
from Backend.admin.profiles import profiles_bp # Import Mesin Profil
from Backend.admin.projects import projects_bp # TAMBAHAN BARU: Mesin Proyek

app = Flask(__name__, template_folder="Frontend", static_folder="Frontend")
app.secret_key = "portofolio_rahasia_yosua"

# Daftarkan Seluruh Blueprint ke Aplikasi
app.register_blueprint(utama_bp)
app.register_blueprint(login_bp)
app.register_blueprint(upload_bp) # Jalur upload diaktifkan
app.register_blueprint(profiles_bp) # API Profil diaktifkan
app.register_blueprint(projects_bp) # TAMBAHAN BARU: API Proyek diaktifkan

# Rute halaman depan (Langsung nampilin index.html dari root folder)
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# Rute Menuju Halaman Login Admin
@app.route('/admin')
def admin_login():
    return send_from_directory('Frontend/admin', 'login.html')

# Rute Menuju Halaman Dashboard Admin
@app.route('/admin/dashboard')
def admin_dashboard():
    return send_from_directory('Frontend/admin', 'dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)