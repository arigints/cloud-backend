from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Fungsi untuk terhubung ke database MySQL
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host='52.139.171.12',
            port=3306,
            user='root',  # Ganti dengan username database Anda
            password='mysql',  # Ganti dengan password database Anda
            database='faskes'
        )
        return conn
    except mysql.connector.Error as err:
        print("Koneksi ke database gagal: ", err)
        return None

# Mengambil semua query dari database
def get_all_data():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM data")
            rows = cursor.fetchall()
            return rows
        except mysql.connector.Error as err:
            print("Gagal mengambil data: ", err)
    return None

# Mengatur route API untuk menampilkan semua data
@app.route('/api/data', methods=['GET'])
def api_data():
    data = get_all_data()
    if data:
        result = []
        for row in data:
            result.append({
                'Provinsi': row[1],
                'Lokasi': row[5],
                'Jenis Faskes': row[6]
                # Tambahkan kolom lain sesuai dengan struktur tabel Anda
            })
        return jsonify(result)
    else:
        return jsonify({'message': 'Gagal mengambil data.'}), 500

# Mengatur route API untuk menampilkan kategori jenis Faskes dan jumlahnya
@app.route('/api/jenisfaskes', methods=['GET'])
def api_jenis_faskes():
    data = get_all_data()
    if data:
        faskes_count = {}
        for row in data:
            jenis_faskes = row[6]
            if jenis_faskes in faskes_count:
                faskes_count[jenis_faskes] += 1
            else:
                faskes_count[jenis_faskes] = 1
        return jsonify(faskes_count)
    else:
        return jsonify({'message': 'Gagal mengambil data.'}), 500

@app.route('/api/provinsifaskes', methods=['GET'])
def api_provinsi_faskes():
    data = get_all_data()
    if data:
        faskes_count = {}
        for row in data:
            provinsi = row[1]
            jenis_faskes = row[6]
            if provinsi in faskes_count:
                if jenis_faskes in faskes_count[provinsi]:
                    faskes_count[provinsi][jenis_faskes] += 1
                else:
                    faskes_count[provinsi][jenis_faskes] = 1
            else:
                faskes_count[provinsi] = {jenis_faskes: 1}
        return jsonify(faskes_count)
    else:
        return jsonify({'message': 'Gagal mengambil data.'}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')