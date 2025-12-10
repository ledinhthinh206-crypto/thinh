class Hinhchunhat:
    """Class Hình chữ nhật: Lưu chiều dài, chiều rộng, và tính diện tích."""
    
    # Hàm khởi tạo (Constructor)
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    # Phương thức tính diện tích
    def area(self):
        return self.length * self.width

# --- Ví dụ kiểm tra ---
# 1. Định nghĩa kích thước
chieu_dai = 12
chieu_rong = 6

# 2. Tạo đối tượng
hcn = Hinhchunhat(chieu_dai, chieu_rong)

# 3. In kết quả
print(f"Hình chữ nhật có Chiều dài = {hcn.length} và Chiều rộng = {hcn.width}")
print(f"Diện tích = {hcn.area()}")
