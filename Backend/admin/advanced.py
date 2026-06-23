from flask import Blueprint, request, jsonify
from model import get_db_connection

advanced_bp = Blueprint('advanced', __name__)

# --- API PENGALAMAN ---
@advanced_bp.route('/api/admin/pengalaman', methods=['GET', 'POST'])
def kelola_pengalaman():
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        data = request.json
        if data.get('id'): # Update
            cursor.execute("UPDATE pengalaman SET periode=%s, jabatan=%s, perusahaan=%s, deskripsi=%s WHERE id=%s", 
                           (data['periode'], data['jabatan'], data['perusahaan'], data['deskripsi'], data['id']))
        else: # Insert
            cursor.execute("INSERT INTO pengalaman (periode, jabatan, perusahaan, deskripsi) VALUES (%s, %s, %s, %s)",
                           (data['periode'], data['jabatan'], data['perusahaan'], data['deskripsi']))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"})
    
    cursor.execute("SELECT * FROM pengalaman ORDER BY id DESC")
    data = cursor.fetchall()
    conn.close()
    return jsonify({"status": "success", "data": data})

@advanced_bp.route('/api/admin/pengalaman/<id>', methods=['DELETE'])
def hapus_pengalaman(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pengalaman WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})

# --- API SKILLS ---
@advanced_bp.route('/api/admin/skills', methods=['GET', 'POST'])
def kelola_skills():
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        data = request.json
        if data.get('id'): # Update
            cursor.execute("UPDATE skill SET nama_skill=%s, icon=%s WHERE id=%s", (data['nama'], data['icon'], data['id']))
        else: # Insert
            cursor.execute("INSERT INTO skill (nama_skill, icon) VALUES (%s, %s)", (data['nama'], data['icon']))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"})
    
    cursor.execute("SELECT * FROM skill ORDER BY id DESC")
    data = cursor.fetchall()
    conn.close()
    return jsonify({"status": "success", "data": data})

@advanced_bp.route('/api/admin/skills/<id>', methods=['DELETE'])
def hapus_skills(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM skill WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})

# --- API PESAN INBOX ---
@advanced_bp.route('/api/admin/inbox', methods=['GET'])
def get_inbox():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kontak ORDER BY id DESC")
    data = cursor.fetchall()
    conn.close()
    return jsonify({"status": "success", "data": data})

@advanced_bp.route('/api/admin/inbox/read/<id>', methods=['POST'])
def read_inbox(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE kontak SET is_read = TRUE WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})

# --- API PENGATURAN & SEO ---
@advanced_bp.route('/api/settings', methods=['GET', 'POST'])
def kelola_pengaturan():
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        data = request.json
        cursor.execute("UPDATE pengaturan SET title=%s, deskripsi=%s, analytics_id=%s, maintenance_mode=%s WHERE id=1",
                       (data['title'], data['deskripsi'], data['analytics_id'], data['maintenance']))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"})
    
    cursor.execute("SELECT * FROM pengaturan WHERE id=1")
    data = cursor.fetchone()
    conn.close()
    return jsonify({"status": "success", "data": data})