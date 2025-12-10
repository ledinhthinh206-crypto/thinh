# bai_8_search.py - Giải thuật tìm kiếm tuần tự (Sequential Search)

# --- PHẦN HÀM TÌM KIẾM (MODULE) ---
def Sequential_Search(dlist, item):
    """
    Thực hiện giải thuật tìm kiếm tuần tự.
    Trả về (True, Vị trí index) nếu tìm thấy, hoặc (False, None) nếu không tìm thấy.
    """
    vi_tri = 0
    tim_thay = False
    
    # Duyệt qua từng phần tử
    while vi_tri < len(dlist) and not tim_thay:
        # Kiểm tra xem phần tử hiện tại có bằng item cần tìm không
        if dlist[vi_tri] == item:
            tim_thay = True
        else:
            # Chuyển sang vị trí tiếp theo
            vi_tri = vi_tri + 1

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
        item = int(input("\nNhập phần tử CẦN TÌM: "))
        
        return dlist, item

    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số nguyên.")
        return [], None

# --- THỰC THI CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    # A. Nhập liệu
    danh_sach, item_can_tim = nhap_danh_sach_va_item()
    
    if danh_sach and item_can_tim is not None:
        print(f"\nDanh sách vừa nhập: {danh_sach}")
        print(f"Phần tử cần tìm: {item_can_tim}")

        # B. Gọi hàm tìm kiếm tuần tự
        ket_qua_tim_thay, vi_tri = Sequential_Search(danh_sach, item_can_tim)

        # C. Hiển thị kết quả
        if ket_qua_tim_thay:
            print(f"\nKẾT QUẢ: (True, {vi_tri})")
            print(f"Tìm thấy phần tử {item_can_tim} tại Vị trí (index): {vi_tri}")
        else:
            print(f"\nKẾT QUẢ: (False, None)")
            print(f"Không tìm thấy phần tử {item_can_tim} trong danh sách.")
