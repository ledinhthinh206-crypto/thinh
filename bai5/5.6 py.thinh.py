

def tim_va_in_vi_tri():
    """Nhập danh sách, tìm Max/Min và Index của chúng, sau đó in ra."""
    try:
        # 1. Nhập danh sách từ bàn phím (Bắt buộc cho Bài 5)
        n = int(input("Nhập số lượng phần tử: "))
        if n <= 0:
            print("Số lượng không hợp lệ.")
            return

        danh_sach = []
        for i in range(n):
            gia_tri = int(input(f"  > Nhập phần tử thứ {i+1}: "))
            danh_sach.append(gia_tri)

        if not danh_sach:
            print("Danh sách rỗng.")
            return

        print("\nDanh sách gốc:", danh_sach)

        # 2. Tìm giá trị lớn nhất và nhỏ nhất
        nho_nhat = min(danh_sach)
        lon_nhat = max(danh_sach)
        
        # 3. Tìm VỊ TRÍ (INDEX) - Yêu cầu chính của Câu 6
        vi_tri_nho_nhat = danh_sach.index(nho_nhat)
        vi_tri_lon_nhat = danh_sach.index(lon_nhat)
        
        # 4. In ra kết quả
        print("\n--- KẾT QUẢ VỊ TRÍ (INDEX - CÂU 6) ---")
        print(f"Giá trị nhỏ nhất: {nho_nhat}, Vị trí (index): {vi_tri_nho_nhat}")
        print(f"Giá trị lớn nhất: {lon_nhat}, Vị trí (index): {vi_tri_lon_nhat}")
        print("---------------------------------------")

    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số nguyên.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# --- CHẠY CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    tim_va_in_vi_tri()
