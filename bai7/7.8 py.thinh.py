# 8. Viết chương trình Python để viết nội dung danh sách vào tệp.

# 1. Khởi tạo danh sách nội dung
my_list = [
    "Dòng 1: Viết từ danh sách vào tệp.",
    "Dòng 2: Danh sách là cấu trúc dữ liệu cơ bản trong Python.",
    "Dòng 3: Mỗi phần tử sẽ là một dòng riêng biệt trong tệp."
]

FILE_NAME = 'list_content.txt' 

def write_list_to_file(filename, data_list):
    """Ghi nội dung của danh sách vào tệp."""
    try:
        # Mở file ở chế độ 'w' (write) để ghi đè nội dung mới.
        # Nếu file chưa tồn tại, nó sẽ được tạo ra.
        with open(filename, 'w') as f:
            # Ghi từng phần tử của danh sách vào file.
            # Dùng '\n'.join(data_list) để nối tất cả các phần tử
            # bằng ký tự xuống dòng ('\n') rồi ghi một lần duy nhất.
            f.write('\n'.join(data_list))
            
        print(f"✅ Đã ghi thành công {len(data_list)} mục từ danh sách vào tệp '{filename}'.")
        
        # (Tùy chọn) In nội dung file ra để kiểm tra
        print("\n--- NỘI DUNG TỆP ---")
        with open(filename, 'r') as f_read:
            print(f_read.read())
        print("--------------------")

    except Exception as e:
        print(f"❌ Lỗi: Không thể ghi nội dung vào tệp: {e}")

# --- THỰC THI CHƯƠNG TRÌNH ---
write_list_to_file(FILE_NAME, my_list)
