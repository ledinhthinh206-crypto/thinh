# ----------------------------------------------------
# 1. Định nghĩa Class Circle
# ----------------------------------------------------

class Circle:
    """
    Class mô tả một hình tròn với thuộc tính bán kính (radius) 
    và phương thức để tính diện tích.
    """
    
    # Hàm khởi tạo (Constructor)
    # self: tham chiếu đến đối tượng hiện tại
    # r: bán kính hình tròn (radius)
    def __init__(self, r):
        # Lưu bán kính vào thuộc tính self.radius
        self.radius = r
        
    # Phương thức tính diện tích (Method area)
    def area(self):
        # Công thức tính diện tích hình tròn: Pi * r^2
        # Sử dụng 3.14 như gợi ý (hoặc np.pi, math.pi nếu import thư viện)
        # return self.radius**2 * 3.14
        
        # Để chính xác hơn, ta nên dùng hằng số PI chuẩn:
        import math
        return math.pi * (self.radius ** 2)
        # Nếu muốn theo sát gợi ý:
        # return self.radius**2 * 3.14 

# ----------------------------------------------------
# 2. Tạo đối tượng và Kiểm tra
# ----------------------------------------------------

# 1. Tạo một đối tượng Circle có tên là aCircle với bán kính r = 2
r_value = 2
aCircle = Circle(r_value)

# 2. In ra diện tích của aCircle
# Gọi phương thức area() trên đối tượng aCircle
calculated_area = aCircle.area()

print(f"Bán kính hình tròn (r): {r_value}")
print(f"Diện tích hình tròn (Area): {calculated_area:.2f}")

# --- Kiểm tra với công thức gợi ý ---
def area_using_hint(r):
    return r**2 * 3.14

area_hint = area_using_hint(r_value)
print(f"Diện tích theo công thức gợi ý (3.14): {area_hint:.2f}")
