from flask import Flask, jsonify, request
import sqlite3

# Tạo ứng dụng Flask
app = Flask(__name__)

# Hàm để kết nối với cơ sở dữ liệu SQLite
def get_db_connection():
    conn = sqlite3.connect('/app/bin_list_data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/bins', methods=['GET'])
def get_bins():
    conn = get_db_connection()
    bins = conn.execute('SELECT * FROM bin_list').fetchall()
    conn.close()
    
    bins_list = [dict(ix) for ix in bins]
    
    return jsonify(bins_list)

@app.route('/api/bin/<string:bin_number>', methods=['GET'])
def get_bin_by_number(bin_number):
    # Lấy 6 ký tự đầu tiên của bin_number để tìm kiếm
    bin_number_prefix = bin_number[:6]
    
    conn = get_db_connection()
    bin_data = conn.execute('SELECT * FROM bin_list WHERE BIN = ?', (bin_number_prefix,)).fetchone()
    conn.close()
    
    if bin_data:
        return jsonify(dict(bin_data))
    else:
        return jsonify({"error": "BIN number not found"}), 404

if __name__ == '__main__':
    # Chạy ứng dụng Flask với hỗ trợ đa nhiệm
    app.run(host='0.0.0.0', port=5000, threaded=True)
