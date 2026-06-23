from flask import Flask, send_from_directory
from model import get_db_connection 

# Import Seluruh Blueprint Backend
from Backend.utama.utama import utama_bp
from Backend.admin.login import login_bp
from Backend.admin.upload import upload_bp 
from Backend.admin.profiles import profiles_bp 
from Backend.admin.projects import projects_bp 
from Backend.admin.advanced import advanced_bp # <--- INI MESIN BARUNYA

app = Flask(__name__, template_folder="Frontend", static_folder="Frontend")
app.secret_key = "portofolio_rahasia_yosua"

# Daftarkan Seluruh Blueprint ke Aplikasi
app.register_blueprint(utama_bp)
app.register_blueprint(login_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(profiles_bp) 
app.register_blueprint(projects_bp)
app.register_blueprint(advanced_bp) # <--- DAFTARKAN MESIN BARUNYA

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/admin')
def admin_login():
    return send_from_directory('Frontend/admin', 'login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    return send_from_directory('Frontend/admin', 'dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)