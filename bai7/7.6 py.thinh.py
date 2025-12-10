def read_last_n_lines_simple(filename, n_lines):
    """Đọc n dòng cuối cùng của tệp (Cách đơn giản)."""
    try:
        with open(filename, 'r') as f:
            # Đọc tất cả các dòng vào một danh sách
            all_lines = f.readlines()
            
            # Lấy N dòng cuối cùng bằng slicing [chỉ mục âm]
            last_lines = all_lines[-n_lines:]
            
            print(f"\n--- {n_lines} DÒNG CUỐI CỦA TỆP ---")
            print(''.join(last_lines))
            print("-----------------------------------")
            
    except FileNotFoundError:
        print(f"\n❌ Lỗi: Không tìm thấy tệp '{filename}'.")

# --- THỰC THI (Ví dụ) ---
FILE_NAME = 'test.txt' 
read_last_n_lines_simple(FILE_NAME, 2)
