# 3. Đọc toàn bộ tệp văn bản và in ra màn hình
FILE_PATH = "a.txt" 

try:
    # Mở file, đọc toàn bộ nội dung, và in ra ngay
    with open(FILE_PATH, 'r') as f:
        print(f.read())

except FileNotFoundError:
    print(f"❌ Error: File '{FILE_PATH}' not found.")
