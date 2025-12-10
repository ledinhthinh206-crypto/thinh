

# --- PHẦN HÀM XỬ LÝ (TƯƠNG ĐƯƠNG VỚI my_module.py) ---

def tim_lon_nhat_nho_nhat(danh_sach):
    """
    Sắp xếp danh sách (in-place) và trả về phần tử nhỏ nhất và lớn nhất.
    """
    if not danh_sach:
        return None, None 

    # Sắp xếp danh sách tăng dần
    danh_sach.sort() 

    # Tìm phần tử nhỏ nhất và lớn nhất sau khi sắp xếp
    nho_nhat = danh_sach[0]
    lon_nhat = danh_sach[-1]

    return nho_nhat, lon_nhat

def hien_thi_ket_qua(nho_nhat, lon_nhat):
    """
    Hàm hiển thị kết quả ra màn hình.
    """
    if nho_nhat is not None:
        print("\n--- KẾT QUẢ TÌM KIẾM ---")
        print(f"Phần tử nhỏ nhất: {nho_nhat}")
        print(f"Phần tử lớn nhất: {lon_nhat}")
        print("------------------------")
    else:
        print("\nDanh sách rỗng, không thể tìm phần tử lớn nhất/nhỏ nhất.")


# --- PHẦN CHƯƠNG TRÌNH CHÍNH (TƯƠNG ĐƯƠNG VỚI main_5.py) ---

def nhap_danh_sach():
    """
    Hàm nhập số lượng và giá trị các phần tử của danh sách từ bàn phím.
    """
    try:
        n = int(input("Nhập số lượng phần tử của danh sách: "))
        if n <= 0:
            print("Số lượng phải là số nguyên dương.")
            return []

        danh_sach = []
        print(f"Bắt đầu nhập {n} phần tử:")

        for i in range(n):
            gia_tri = int(input(f"  > Nhập phần tử thứ {i+1}: "))
            danh_sach.append(gia_tri)

        return danh_sach

    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số nguyên cho số lượng và giá trị.")
        return []

if __name__ == "__main__":
    # 1. Nhập liệu từ bàn phím
    danh_sach_goc = nhap_danh_sach()
    
    print("\nDanh sách gốc vừa nhập:", danh_sach_goc)

    # 2. Gọi hàm xử lý (không cần import)
    nho_nhat, lon_nhat = tim_lon_nhat_nho_nhat(danh_sach_goc)

    # 3. Hiển thị kết quả
    hien_thi_ket_qua(nho_nhat, lon_nhat)
