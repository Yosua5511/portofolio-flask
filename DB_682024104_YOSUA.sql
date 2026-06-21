-- Membuat tabel Profil
CREATE TABLE IF NOT EXISTS profil (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    deskripsi TEXT,
    foto_url VARCHAR(255)
);

-- Membuat tabel Skill
CREATE TABLE IF NOT EXISTS skill (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_skill VARCHAR(100) NOT NULL,
    persentase INT
);

-- Membuat tabel Pengalaman
CREATE TABLE IF NOT EXISTS pengalaman (
    id INT AUTO_INCREMENT PRIMARY KEY,
    posisi VARCHAR(100) NOT NULL,
    institusi VARCHAR(100) NOT NULL,
    tahun VARCHAR(50),
    deskripsi TEXT
);

-- Membuat tabel Proyek
CREATE TABLE IF NOT EXISTS proyek (
    id INT AUTO_INCREMENT PRIMARY KEY,
    judul VARCHAR(150) NOT NULL,
    deskripsi TEXT,
    link_proyek VARCHAR(255),
    gambar_url VARCHAR(255)
);

-- Membuat tabel Kontak
CREATE TABLE IF NOT EXISTS kontak (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_pengirim VARCHAR(100) NOT NULL,
    email_pengirim VARCHAR(100) NOT NULL,
    pesan TEXT,
    tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- SEEDING DATA AWAL (Contoh Data Portofolio)
-- ==========================================

INSERT INTO profil (nama, deskripsi, foto_url) 
VALUES ('Yosua Fredrik Pratama', 'Mahasiswa Sistem Informasi di Universitas Kristen Satya Wacana dengan ketertarikan mendalam pada pengembangan website, UI/UX design, dan implementasi database. Selalu antusias dalam merancang antarmuka yang user-friendly dan sistem yang efisien.', '');

INSERT INTO skill (nama_skill, persentase) VALUES 
('Figma (UI/UX Design)', 90),
('WordPress & Elementor', 85),
('Python & Flask', 80),
('SQL Database', 85);

INSERT INTO pengalaman (posisi, institusi, tahun, deskripsi) VALUES 
('Head of People Development', 'ISACA Student Group UKSW', '2025 - Sekarang', 'Bertanggung jawab dalam mengelola sumber daya manusia, menyusun rundown acara, serta mengoordinasi komite untuk berbagai kegiatan komunitas mahasiswa di tingkat regional maupun nasional.'),
('Teaching Assistant', 'Universitas Kristen Satya Wacana', '2025', 'Mendampingi mahasiswa dalam mata kuliah Dasar Pemrograman Sistem Informasi, membantu evaluasi proyek akhir, memandu logika flowchart, serta memberikan arahan perbaikan kode.');

INSERT INTO proyek (judul, deskripsi, link_proyek, gambar_url) VALUES 
('Website Coffee Shop', 'Pengembangan website interaktif menggunakan CMS WordPress dan Elementor. Mencakup perancangan struktur website, footer, dan integrasi link edukasi yang responsif di berbagai perangkat.', 'fore-.', ''),
('Hospital Database Management System', 'Implementasi sistem database operasional rumah sakit dengan penyesuaian khusus pada entitas pasien, memastikan pencatatan rekam medis berjalan lancar menggunakan SQL.', '', '');