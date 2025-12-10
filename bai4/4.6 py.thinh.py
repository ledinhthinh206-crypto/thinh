# Yêu cầu: Nhập một tên người (Họ + Tên riêng, chỉ gồm 2 từ cách nhau bởi dấu cách) 
# và in riêng Họ và Tên riêng ra màn hình.

def tach_ho_ten():
    # 1. Nhập tên từ bàn phím
    # Sử dụng input() để nhận chuỗi nhập vào từ người dùng
    ten_day_du = input("Nhập tên đầy đủ (Ví dụ: 'Nguyen Dung'): ")

    # 2. Tách chuỗi thành các từ
    # Hàm split() mặc định sẽ tách chuỗi dựa trên ký tự dấu cách (' ').
    # Kết quả trả về là một danh sách (list) các từ.
    cac_phan_ten = ten_day_du.split()

    # 3. Xử lý và in kết quả dựa trên giả thiết
    
    # Giả thiết là tên chỉ có 2 phần (Họ và Tên riêng)
    if len(cac_phan_ten) == 2:
        # Lấy phần tử đầu tiên (index 0) làm Họ
        ho = cac_phan_ten[0]
        
        # Lấy phần tử thứ hai (index 1) làm Tên riêng
        ten_rieng = cac_phan_ten[1]
        
        # 4. In kết quả ra màn hình
        print("\n--- KẾT QUẢ TÁCH TÊN ---")
        print(f"Tên đầy đủ đã nhập: **{ten_day_du}**")
        print(f"Phần Họ: **{ho}**")
        print(f"Phần Tên riêng: **{ten_rieng}**")
        
    else:
        # Xử lý trường hợp không tuân thủ giả thiết (tên có 1 từ, 3 từ trở lên)
        print("\nLỖI: Tên bạn nhập không tuân thủ giả thiết (Họ và Tên riêng chỉ gồm 2 từ cách nhau bởi dấu cách).")
        print(f"Số lượng từ tìm thấy: {len(cac_phan_ten)}.")

# Gọi hàm để thực thi chương trình
tach_ho_ten()
