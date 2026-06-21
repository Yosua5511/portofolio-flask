from flask import Blueprint, request, jsonify, session

login_bp = Blueprint('login', __name__)

# API Proses Login (Username: admin, Password: admin123)
@login_bp.route('/api/login', methods=['POST'])
def do_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'admin123':
        session['logged_in'] = True
        return jsonify({"status": "success", "message": "Login berhasil!"})
    else:
        return jsonify({"status": "error", "message": "Username atau Password salah!"}), 401

# API Proses Logout
@login_bp.route('/api/logout', methods=['POST'])
def do_logout():
    session.pop('logged_in', None)
    return jsonify({"status": "success", "message": "Logout berhasil!"})
    
# API Cek Status Session Admin
@login_bp.route('/api/check-session', methods=['GET'])
def check_session():
    if session.get('logged_in'):
        return jsonify({"status": "success", "logged_in": True})
    return jsonify({"status": "error", "logged_in": False}), 401