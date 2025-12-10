import shutil

# 9. Chương trình Python để sao chép nội dung của tệp này sang tệp khác.

SOURCE_FILE = 'source.txt' # Tệp nguồn (cần phải tồn tại)
DESTINATION_FILE = 'destination.txt' # Tệp đích (sẽ được tạo/ghi đè)

# --- BƯỚC 1: TỰ ĐỘNG TẠO FILE NGUỒN MẪU ---
try:
    with open(SOURCE_FILE, 'w') as f_source:
        f_source.write("Đây là nội dung gốc cần được sao chép.\n")
        f_source.write("Dòng này cũng sẽ được chuyển sang tệp đích.\n")
    print(f"✅ Đã tạo tệp nguồn mẫu: '{SOURCE_FILE}'")
except Exception as e:
    print(f"❌ Lỗi khi tạo file nguồn: {e}")
    exit()

# --- BƯỚC 2: SAO CHÉP DÙNG SHUTIL ---

def copy_file_shutil(src, dest):
    """Sao chép nội dung từ src sang dest dùng shutil."""
    try:
        # shutil.copyfile là hàm tối ưu cho việc sao chép nội dung file
        shutil.copyfile(src, dest)
        
        print(f"\n✅ Sao chép thành công từ '{src}' sang '{dest}'.")
        
        # (Tùy chọn) Kiểm tra nội dung tệp đích
        with open(dest, 'r') as f_dest:
            print("\n--- NỘI DUNG TỆP ĐÍCH ---")
            print(f_dest.read())
            print("--------------------------")
            
    except FileNotFoundError:
        print(f"\n❌ Lỗi: Không tìm thấy tệp nguồn '{src}'.")
    except Exception as e:
        print(f"\n❌ Đã xảy ra lỗi trong quá trình sao chép: {e}")

# --- THỰC THI ---
copy_file_shutil(SOURCE_FILE, DESTINATION_FILE)
