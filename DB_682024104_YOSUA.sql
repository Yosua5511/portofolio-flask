USE test;

CREATE TABLE IF NOT EXISTS profil (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(150),
    deskripsi TEXT
);

CREATE TABLE IF NOT EXISTS pengalaman (
    id INT AUTO_INCREMENT PRIMARY KEY,
    periode VARCHAR(100),
    jabatan VARCHAR(150),
    perusahaan VARCHAR(150),
    deskripsi TEXT
);

CREATE TABLE IF NOT EXISTS skill (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_skill VARCHAR(100),
    icon VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS proyek (
    id INT AUTO_INCREMENT PRIMARY KEY,
    judul VARCHAR(150),
    deskripsi TEXT,
    link_proyek VARCHAR(255),
    gambar VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS kontak (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_pengirim VARCHAR(150),
    email_pengirim VARCHAR(150),
    pesan TEXT,
    is_read BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS pengaturan (
    id INT PRIMARY KEY DEFAULT 1,
    title VARCHAR(255),
    deskripsi TEXT,
    analytics_id VARCHAR(50),
    maintenance_mode BOOLEAN DEFAULT FALSE
);