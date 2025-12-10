# 5. Chương trình Python để nối văn bản vào tệp và hiển thị văn bản.

# Tên file cần thao tác
FILE_NAME = 'abc.txt' 

def append_and_read_file(filename):
    """
    Nối nội dung mới vào file và sau đó đọc toàn bộ file.
    """
    
    # 1. NỐI/THÊM VĂN BẢN (Chế độ 'a' - append)
    # Chế độ 'a' sẽ tạo file nếu nó chưa tồn tại, giúp tránh lỗi FileNotFoundError.
    try:
        with open(filename, 'a') as myfile:
            # Thêm nội dung mẫu mới vào cuối file
            myfile.write("\n--- Nội dung mới được thêm vào ---\n")
            myfile.write("Python Exercises (Nội dung mới nối thêm)\n")
            myfile.write("Java Exercises (Nội dung mới nối thêm)\n")
        print(f"✅ Đã thêm nội dung mới vào '{filename}'.")
    except Exception as e:
        print(f"❌ Lỗi khi thêm nội dung: {e}")
        return
        
    # 2. ĐỌC VÀ HIỂN THỊ VĂN BẢN (Chế độ 'r' - read)
    try:
        # Mở file ở chế độ 'r' để đọc toàn bộ nội dung
        with open(filename, 'r') as myfile:
            content = myfile.read()
            
        print("\n--- TOÀN BỘ NỘI DUNG TỆP ---")
        print(content)
        print("-----------------------------")

    except FileNotFoundError:
        # Lỗi này khó xảy ra vì file đã được tạo ở bước 1
        print(f"❌ Lỗi: Không tìm thấy file '{filename}' để đọc.")
        
# --- Thực thi chương trình ---
append_and_read_file(FILE_NAME)
