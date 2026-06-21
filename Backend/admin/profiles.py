from flask import Blueprint, request, jsonify, session
from model import get_db_connection

profiles_bp = Blueprint('profiles', __name__)

# Mengambil data profil saat ini (Read)
@profiles_bp.route('/api/admin/profil', methods=['GET'])
def get_profil():
    # Satpam Keamanan Diaktifkan dengan Kunci yang BENAR!
    if not session.get('logged_in'):
        return jsonify({'status': 'error', 'message': 'Akses ditolak!'}), 401
        
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT nama, deskripsi FROM profil LIMIT 1")
        row = cursor.fetchone()
        conn.close()
        
        if row:
            if isinstance(row, dict):
                profil_data = {'nama': row.get('nama', ''), 'deskripsi': row.get('deskripsi', '')}
            else:
                profil_data = {
                    'nama': row[0] if len(row) > 0 else '', 
                    'deskripsi': row[1] if len(row) > 1 else ''
                }
            return jsonify({'status': 'success', 'data': profil_data})
        else:
            return jsonify({'status': 'error', 'message': 'Data profil kosong di database!'})
            
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Menyimpan data profil baru (Update)
@profiles_bp.route('/api/admin/profil', methods=['PUT'])
def update_profil():
    if not session.get('logged_in'):
        return jsonify({'status': 'error', 'message': 'Akses ditolak!'}), 401
        
    data = request.json
    nama = data.get('nama')
    deskripsi = data.get('deskripsi')
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE profil 
            SET nama = %s, deskripsi = %s 
        """, (nama, deskripsi))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success', 'message': 'Profil berhasil diperbarui!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500