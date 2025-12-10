# 9. Sao chép thủ công (Không dùng shutil)

SOURCE_FILE = 'source.txt'
DESTINATION_FILE = 'destination_manual.txt'

# (Phần tự động tạo file mẫu giống hệt như trên, tôi bỏ qua để code gọn)

def copy_file_manual(src, dest):
    """Sao chép nội dung từ src sang dest dùng read/write."""
    try:
        # 1. Mở file nguồn để đọc ('r')
        with open(src, 'r') as f_source:
            content = f_source.read() # Đọc toàn bộ nội dung
            
        # 2. Mở file đích để ghi ('w')
        with open(dest, 'w') as f_dest:
            f_dest.write(content) # Ghi nội dung vào file đích
            
        print(f"\n✅ Sao chép thủ công thành công từ '{src}' sang '{dest}'.")
        
    except FileNotFoundError:
        print(f"\n❌ Lỗi: Không tìm thấy tệp nguồn '{src}'.")
    except Exception as e:
        print(f"\n❌ Đã xảy ra lỗi trong quá trình sao chép: {e}")

# --- THỰC THI ---
copy_file_manual(SOURCE_FILE, DESTINATION_FILE)
