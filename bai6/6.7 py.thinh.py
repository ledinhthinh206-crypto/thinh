import math

class Circle:
    """
    Class mô tả hình tròn với thuộc tính bán kính (radius) và các 
    phương thức để tính diện tích và chu vi.
    """
    
    # Hàm khởi tạo: Lưu bán kính
    def __init__(self, r):
        self.radius = r
        
    # Phương thức tính diện tích (Area)
    def area(self):
        # Công thức: Diện tích = π * r²
        return math.pi * (self.radius ** 2)
        
    # Phương thức tính chu vi (Circumference)
    def perimeter(self):
        # Công thức: Chu vi = 2 * π * r
        return 2 * math.pi * self.radius

# ----------------------------------------------------
# --- Ví dụ kiểm tra ---
# ----------------------------------------------------

# Bán kính mẫu
r_value = 5

# Tạo đối tượng Circle
my_circle = Circle(r_value)

# In kết quả
print("--- THÔNG TIN HÌNH TRÒN ---")
print(f"Bán kính (r): {my_circle.radius}")
print(f"Diện tích: {my_circle.area():.2f}")     # Làm tròn 2 chữ số thập phân
print(f"Chu vi: {my_circle.perimeter():.2f}") # Làm tròn 2 chữ số thập phân
