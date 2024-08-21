# Sử dụng một image chính thức của Python
FROM python:3.9-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép các file cần thiết vào thư mục làm việc
COPY app.py /app/
COPY bin_list_data.db /app/
COPY requirements.txt /app/

# Cài đặt các thư viện cần thiết
RUN pip install -r requirements.txt

# Mở cổng 5000 để truy cập Flask
EXPOSE 5000

# Lệnh để chạy ứng dụng Flask
CMD ["python", "app.py"]

