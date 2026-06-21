from flask import Blueprint, request, jsonify, session
from model import get_db_connection

projects_bp = Blueprint('projects_admin', __name__)

# Ambil semua data proyek (Read)
@projects_bp.route('/api/admin/proyek', methods=['GET'])
def get_projects():
    if not session.get('logged_in'):
        return jsonify({'status': 'error', 'message': 'Akses ditolak!'}), 401
        
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM proyek ORDER BY id DESC")
        rows = cursor.fetchall()
        conn.close()
        
        # Format data agar mudah dibaca frontend
        projects = []
        for row in rows:
            if isinstance(row, dict):
                projects.append(row)
            else:
                # Sesuaikan index tuple dengan struktur tabel TiDB lo
                # Misal: 0=id, 1=judul, 2=deskripsi, 3=link_proyek, 4=gambar
                project_data = {
                    'id': row[0],
                    'judul': row[1] if len(row) > 1 else '',
                    'deskripsi': row[2] if len(row) > 2 else '',
                    'link_proyek': row[3] if len(row) > 3 else '',
                    'gambar': row[4] if len(row) > 4 else ''
                }
                projects.append(project_data)
                
        return jsonify({'status': 'success', 'data': projects})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Tambah proyek baru (Create)
@projects_bp.route('/api/admin/proyek', methods=['POST'])
def add_project():
    if not session.get('logged_in'):
        return jsonify({'status': 'error', 'message': 'Akses ditolak!'}), 401
        
    data = request.json
    judul = data.get('judul')
    deskripsi = data.get('deskripsi')
    link_proyek = data.get('link_proyek', '')
    gambar = data.get('gambar', '') # Ini URL dari Cloudinary
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Masukkan ke database (abaikan id karena auto-increment)
        cursor.execute("""
            INSERT INTO proyek (judul, deskripsi, link_proyek, gambar) 
            VALUES (%s, %s, %s, %s)
        """, (judul, deskripsi, link_proyek, gambar))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success', 'message': 'Proyek baru berhasil ditambahkan!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Hapus proyek (Delete)
@projects_bp.route('/api/admin/proyek/<int:id>', methods=['DELETE'])
def delete_project(id):
    if not session.get('logged_in'):
        return jsonify({'status': 'error', 'message': 'Akses ditolak!'}), 401
        
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM proyek WHERE id = %s", (id,))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success', 'message': 'Proyek berhasil dihapus!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500