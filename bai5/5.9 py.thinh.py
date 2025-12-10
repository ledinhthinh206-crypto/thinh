

# --- PHẦN HÀM TÌM KIẾM (MODULE) ---
def binary_Search(dlist, value):
    """
    Thực hiện giải thuật tìm kiếm nhị phân. 
    Lưu ý: Danh sách dlist PHẢI được sắp xếp trước khi gọi hàm này.
    Trả về (True, Vị trí index) nếu tìm thấy, hoặc (False, None) nếu không tìm thấy.
    """
    dau = 0
    cuoi = len(dlist) - 1
    tim_thay = False
    
    vi_tri = None

    while dau <= cuoi and not tim_thay:
        # Tính vị trí giữa
        giua = (dau + cuoi) // 2
        
        if dlist[giua] == value:
            tim_thay = True
            vi_tri = giua
        elif value < dlist[giua]:
            # Nếu giá trị cần tìm nhỏ hơn giá trị ở giữa, tìm ở nửa đầu
            cuoi = giua - 1
        else:
            # Nếu giá trị cần tìm lớn hơn giá trị ở giữa, tìm ở nửa sau
            dau = giua + 1

    if tim_thay:
        return True, vi_tri
    else:
        return False, None

# --- PHẦN CHƯƠNG TRÌNH CHÍNH (NHẬP LIỆU) ---
def nhap_danh_sach_va_item():
    """Hàm nhập danh sách và phần tử cần tìm từ bàn phím."""
    try:
        # Nhập danh sách
        n = int(input("Nhập số lượng phần tử của danh sách: "))
        if n <= 0:
            print("Số lượng phải là số nguyên dương.")
            return [], None
        
        dlist = []
        print(f"Bắt đầu nhập {n} phần tử:")
        for i in range(n):
            # Nhập giá trị, giả sử là số nguyên
            gia_tri = int(input(f"  > Nhập phần tử thứ {i+1}: "))
            dlist.append(gia_tri)

        # Nhập phần tử cần tìm
        value_can_tim = int(input("\nNhập phần tử CẦN TÌM (value): "))
        
        return dlist, value_can_tim

    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số nguyên.")
        return [], None

# --- THỰC THI CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    # A. Nhập liệu
    danh_sach_nhap_vao, value_can_tim = nhap_danh_sach_va_item()
    
    if danh_sach_nhap_vao and value_can_tim is not None:
        
        # B. **SẮP XẾP DANH SÁCH** (Bước bắt buộc cho Binary Search)
        danh_sach_da_sap_xep = sorted(danh_sach_nhap_vao)
        
        print(f"\nDanh sách GỐC vừa nhập: {danh_sach_nhap_vao}")
        print(f"Danh sách ĐÃ SẮP XẾP (dùng để tìm kiếm): {danh_sach_da_sap_xep}")
        print(f"Phần tử cần tìm: {value_can_tim}")

        # C. Gọi hàm tìm kiếm nhị phân
        ket_qua_tim_thay, vi_tri = binary_Search(danh_sach_da_sap_xep, value_can_tim)

        # D. Hiển thị kết quả
        if ket_qua_tim_thay:
            print(f"\nKẾT QUẢ: Tìm thấy phần tử {value_can_tim} tại Vị trí (index) trong danh sách ĐÃ SẮP XẾP: {vi_tri}")
        else:
            print(f"\nKẾT QUẢ: Không tìm thấy phần tử {value_can_tim} trong danh sách.")
            
