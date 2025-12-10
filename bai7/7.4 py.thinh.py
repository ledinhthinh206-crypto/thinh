from itertools import islice

# --- Cấu hình ---
FILE_NAME = 'test.txt'
LINES_TO_READ = 2 # Số dòng cần đọc (giống như trong code gốc)

# --- BƯỚC 1: TỰ ĐỘNG TẠO FILE MẪU ---
# Phần này đảm bảo file 'test.txt' luôn tồn tại với nội dung mẫu
try:
    with open(FILE_NAME, 'w') as f_setup:
        f_setup.write("Dòng số 1: Dòng này sẽ được in ra.\n")
        f_setup.write("Dòng số 2: Dòng này cũng sẽ được in ra.\n")
        f_setup.write("Dòng số 3: Dòng này sẽ bị bỏ qua.\n")
    print(f"✅ Đã tạo file mẫu: '{FILE_NAME}'")
except Exception as e:
    print(f"❌ Lỗi khi tạo file: {e}")
    exit()

# --- BƯỚC 2: HÀM ĐỌC N DÒNG ĐẦU TIÊN (Logic chính của câu 4) ---

def read_first_n_lines(filename, n_lines):
    """Đọc và in n dòng đầu tiên của tệp."""
    try:
        # Sử dụng 'with' và 'islice' để đọc chính xác n dòng
        with open(filename, 'r') as f:
            print(f"\n--- KẾT QUẢ ĐỌC {n_lines} DÒNG ĐẦU ---")
            # islice(f, n_lines) tạo một iterator chỉ trả về n dòng đầu
            for line in islice(f, n_lines):
                # In từng dòng, dùng end='' để tránh dòng trống thừa
                print(line, end='') 
            print("---------------------------------------")
        
    except FileNotFoundError:
        # Lỗi này khó xảy ra vì đã có Bước 1 tự động tạo file
        print(f"\n❌ Lỗi: Không tìm thấy tệp '{filename}'.")

# --- BƯỚC 3: THỰC THI ---
read_first_n_lines(FILE_NAME, LINES_TO_READ)
