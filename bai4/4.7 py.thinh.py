# Yêu cầu: Nhập một chuỗi, loại bỏ tất cả các chữ số (0-9) và in chuỗi mới.

def loai_bo_chu_so():
    # 1. Nhập chuỗi từ bàn phím
    chuoi_goc = input("Nhập một chuỗi bất kỳ (có thể chứa chữ, số, ký tự đặc biệt): ")
    
    # 2. Chuẩn bị chuỗi mới
    # Khởi tạo một chuỗi rỗng để chứa các ký tự đã được lọc
    chuoi_moi = ""
    
    # 3. Duyệt và lọc ký tự
    print("\n--- QUÁ TRÌNH LỌC ---")
    
    # Duyệt qua từng ký tự (ky_tu) trong chuỗi gốc
    for ky_tu in chuoi_goc:
        
        # Kiểm tra xem ký tự đó có phải là chữ số hay không
        # Phương thức .isdigit() trả về True nếu ký tự là số (0-9), và False nếu không phải.
        if ky_tu.isdigit():
            # Nếu là chữ số, BỎ QUA (không thêm vào chuỗi_moi)
            # print(f"-> Bỏ qua ký tự: '{ky_tu}' (Là chữ số)") # Có thể bật dòng này để xem quá trình
            pass 
        else:
            # Nếu KHÔNG phải là chữ số, THÊM vào chuỗi_moi
            chuoi_moi += ky_tu
            # print(f"-> Giữ lại ký tự: '{ky_tu}'") # Có thể bật dòng này để xem quá trình

    # 4. In kết quả ra màn hình
    print("\n--- KẾT QUẢ ---")
    print(f"Chuỗi gốc: **{chuoi_goc}**")
    print(f"Chuỗi sau khi loại bỏ chữ số: **{chuoi_moi}**")

# Gọi hàm để thực thi chương trình
loai_bo_chu_so()
