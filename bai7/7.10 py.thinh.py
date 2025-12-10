# 10. Viết chương trình python để tìm những từ dài nhất trong văn bản.

FILE_PATH = "text_analyze.txt"

# --- BƯỚC 1: TỰ ĐỘNG TẠO FILE MẪU ---
# Đảm bảo file tồn tại với nội dung đa dạng
try:
    with open(FILE_PATH, 'w') as f_setup:
        f_setup.write("Python là một ngôn ngữ lập trình tuyệt vời và đa năng nhất.\n")
        f_setup.write("Chương trình này sẽ tìm từ 'tuyệt vời' và 'đa năng nhất' (có 8 ký tự).\n")
    print(f"✅ Đã tạo file mẫu: '{FILE_PATH}'")
except Exception as e:
    print(f"❌ Lỗi khi tạo file: {e}")
    exit()

# --- BƯỚC 2: LOGIC CHÍNH TÌM TỪ DÀI NHẤT ---

def find_longest_words(filename):
    """Tìm và in ra tất cả các từ dài nhất trong tệp."""
    
    try:
        # 1. Đọc file
        with open(filename, 'r') as f:
            content = f.read()
            
        # 2. Làm sạch và tách từ
        # Tách chuỗi thành danh sách các từ. content.split() tự động xử lý khoảng trắng,
        # dấu xuống dòng, và nhiều khoảng trắng liên tiếp.
        words = content.split() 
        
        # 3. Tìm độ dài từ dài nhất
        # Sử dụng hàm max() với key=len để tìm độ dài của từ dài nhất.
        if not words:
            print("Tệp rỗng, không có từ nào để phân tích.")
            return

        max_length = len(max(words, key=len))
        
        # 4. Lọc ra tất cả các từ có cùng độ dài đó
        longest_words = [word for word in words if len(word) == max_length]
        
        # 5. In kết quả
        print("\n--- KẾT QUẢ PHÂN TÍCH TỪ ---")
        print(f"Độ dài từ dài nhất là: **{max_length}** ký tự.")
        print("Các từ dài nhất trong văn bản là:")
        
        # Dùng set() để loại bỏ các từ lặp lại trước khi in
        for word in sorted(set(longest_words)):
            print(f"- {word}")
        print("----------------------------")

    except FileNotFoundError:
        print(f"\n❌ Lỗi: Không tìm thấy tệp '{filename}'.")

# --- BƯỚC 3: THỰC THI ---
find_longest_words(FILE_PATH)
