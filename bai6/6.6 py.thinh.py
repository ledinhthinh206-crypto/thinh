class IOString:
    """Class chứa phương thức nhận chuỗi và in chuỗi in hoa."""
    
    # Hàm khởi tạo: Khởi tạo thuộc tính chuỗi (str1) với giá trị rỗng
    def __init__(self):
        self.str1 = ""
        
    # Phương thức get_String: Nhận input từ người dùng
    def get_String(self):
        # Tương đương với bước self.str1 = input() trong lưu đồ
        self.str1 = input("Vui lòng nhập một chuỗi: ")
        
    # Phương thức print_String: In chuỗi đã nhập dưới dạng chữ in hoa
    def print_String(self):
        # Tương đương với bước print(self.str1.upper()) trong lưu đồ
        print("Chuỗi đã nhập (In hoa):", self.str1.upper())

# ----------------------------------------------------
# --- Ví dụ kiểm tra ---
# ----------------------------------------------------

# 1. Khởi tạo đối tượng
str_obj = IOString()

# 2. Gọi phương thức nhận chuỗi
str_obj.get_String()

# 3. Gọi phương thức in chuỗi (in hoa)
str_obj.print_String()
