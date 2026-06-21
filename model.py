import pymysql
from config import Config

def get_db_connection():
    # Membuat koneksi ke TiDB menggunakan PyMySQL
    connection = pymysql.connect(
        host=Config.TIDB_HOST,
        port=Config.TIDB_PORT,
        user=Config.TIDB_USER,
        password=Config.TIDB_PASSWORD,
        database=Config.TIDB_DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection