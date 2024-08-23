from flask import Flask, jsonify, request
import sqlite3

# Tạo ứng dụng Flask
app = Flask(__name__)

def luhn_check(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10 == 0

# Hàm để kết nối với cơ sở dữ liệu SQLite
def get_db_connection():
    conn = sqlite3.connect('/app/bin_list_data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/bin/<string:bin_number>', methods=['GET'])
def get_bin_by_number(bin_number):
    # Kiểm tra tính hợp lệ của số thẻ
    if not bin_number.isdigit() or len(bin_number) < 6:
        return jsonify({"error": "Invalid BIN number"}), 400

    # Kiểm tra số thẻ theo thuật toán Luhn
    is_valid_luhn = luhn_check(bin_number)

    # Lấy 6 ký tự đầu tiên của bin_number để tìm kiếm
    bin_number_prefix = bin_number[:6]

    conn = get_db_connection()
    bin_data = conn.execute('SELECT * FROM bin_list WHERE BIN = ?', (bin_number_prefix,)).fetchone()
    conn.close()

    if bin_data:
        # Convert kết quả thành dictionary và thêm trường isValid
        result = dict(bin_data)
        result['isValid'] = is_valid_luhn
        return jsonify(result)
    else:
        return jsonify({"error": "BIN number not found"}), 404

if __name__ == '__main__':
    # Chạy ứng dụng Flask với hỗ trợ đa nhiệm
    app.run(host='0.0.0.0', port=5000, threaded=True)
