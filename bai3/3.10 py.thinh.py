import math

def Tinh(R):
    """
    Tính chu vi và diện tích hình tròn.
    Đầu vào: Bán kính R.
    Đầu ra: Chu vi và Diện tích (dưới dạng tuple), hoặc thông báo lỗi.
    """
    
    # Kiểm tra tính hợp lệ của bán kính R (R phải lớn hơn 0)
    if R <= 0:
        # Trả về None cho các giá trị và thông báo lỗi
        return None, "Lỗi: Bán kính R phải là số dương (> 0)."
    
    # Công thức:
    # Chu vi: C = 2 * pi * R
    chu_vi = 2 * math.pi * R
    
    # Diện tích: A = pi * R^2
    dien_tich = math.pi * (R ** 2)
    
    return chu_vi, dien_tich

# ----------------------------------------------------
# Phần thực thi chính: Nhận đầu vào và hiển thị kết quả
# ----------------------------------------------------

print("⭐ Chương trình tính Chu vi và Diện tích hình tròn.")

try:
    # Nhập bán kính R từ người dùng (sử dụng float để chấp nhận số thập phân)
    R_input = float(input("Nhập bán kính R: "))
    
    # Gọi hàm để tính toán
    chu_vi, dien_tich = Tinh(R_input)
    
    print("\n--------------------")
    
    # In kết quả
    if chu_vi is not None:
        print(f"Bán kính R đã nhập: {R_input}")
        print(f"1. Chu vi (C = 2*π*R): {chu_vi:.4f}")
        print(f"2. Diện tích (A = π*R²): {dien_tich:.4f}")
    else:
        # In thông báo lỗi từ hàm Tinh(R)
        print(dien_tich)
        
except ValueError:
    print("❌ Lỗi: Đầu vào không hợp lệ. Bán kính phải là một giá trị số.")
