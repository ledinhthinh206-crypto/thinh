# 7. Chương trình Python để đếm số dòng trong tệp văn bản

FILE_PATH = "test_count.txt" 

# --- BƯỚC 1: TỰ ĐỘNG TẠO FILE MẪU ---
# Đảm bảo file tồn tại để tránh lỗi
try:
    with open(FILE_PATH, 'w') as f_setup:
        # Ghi nội dung 3 dòng
        f_setup.write("Dòng thứ nhất\n")
        f_setup.write("Dòng thứ hai\n")
        f_setup.write("Dòng cuối cùng\n")
    print(f"✅ Đã tạo file mẫu: '{FILE_PATH}'")
except Exception as e:
    print(f"❌ Lỗi khi tạo file: {e}")
    exit()

# --- BƯỚC 2: LOGIC CHÍNH ĐẾM DÒNG ---

def count_lines(filename):
    """Đếm số dòng bằng cách lặp qua file (cách hiệu quả nhất)."""
    try:
        count = 0
        # Mở file và lặp qua từng dòng
        with open(filename, 'r') as f:
            for line in f:
                count += 1
        
        print(f"\n--- KẾT QUẢ ĐẾM DÒNG ---")
        print(f"Tổng số dòng trong tệp là: **{count}**")
        print("--------------------------")
        
    except FileNotFoundError:
        print(f"\n❌ Lỗi: Không tìm thấy tệp '{filename}'.")

# --- BƯỚC 3: THỰC THI ---
count_lines(FILE_PATH)
