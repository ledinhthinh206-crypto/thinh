# my_module.py - Chứa các hàm xử lý theo yêu cầu bài

def tim_lon_nhat_nho_nhat(danh_sach):
    """
    Sắp xếp danh sách (in-place) và trả về phần tử nhỏ nhất và lớn nhất.
    Yêu cầu: Phương thức sắp xếp và tìm phần tử lớn nhất được viết thành module.
    """
    if not danh_sach:
        return None, None # Xử lý trường hợp danh sách rỗng

    # 1. Phương thức sắp xếp: Sắp xếp danh sách tăng dần
    # Sử dụng hàm sort() của Python list (thay đổi danh sách gốc)
    danh_sach.sort() 

    # 2. Tìm phần tử nhỏ nhất và lớn nhất sau khi sắp xếp
    nho_nhat = danh_sach[0]
    lon_nhat = danh_sach[-1]

    # Trả về cả hai giá trị
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

# Lưu ý: Hàm tim_lon_nhat_nho_nhat thực hiện cả sắp xếp và tìm max/min theo yêu cầu.
