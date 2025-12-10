import math # Không thực sự cần thiết cho phép tính cơ bản, nhưng giữ lại nếu bạn muốn mở rộng sau này

# ----------------------------------------------------
# 1. Định nghĩa các hàm (Functions)
# ----------------------------------------------------

def add(x, y):
    # Hàm cộng hai số
    return x + y

def subtract(x, y):
    # Hàm trừ hai số
    return x - y

def multiply(x, y):
    # Hàm nhân hai số
    return x * y

def divide(x, y):
    # Hàm chia hai số, có kiểm tra chia cho 0
    if y == 0:
        return "Lỗi: Không thể chia cho 0!"
    return x / y

# ----------------------------------------------------
# 2. Phần logic chính của chương trình
# ----------------------------------------------------

print("⭐ CHƯƠNG TRÌNH MÁY TÍNH ĐƠN GIẢN ⭐")
print("1. Cộng (Add)")
print("2. Trừ (Subtract)")
print("3. Nhân (Multiply)")
print("4. Chia (Divide)")

# Nhận lựa chọn phép toán từ người dùng
choice = input("Nhập lựa chọn (1/2/3/4): ")

# Kiểm tra lựa chọn và nhận số đầu vào
if choice in ('1', '2', '3', '4'):
    try:
        # Sử dụng float để hỗ trợ cả số nguyên và số thập phân
        num1 = float(input("Nhập số thứ nhất: "))
        num2 = float(input("Nhập số thứ hai: "))
    except ValueError:
        print("❌ Lỗi: Đầu vào phải là số.")
        exit()

    print("--------------------")
    
    # Thực hiện phép toán và gán ký hiệu
    if choice == '1':
        result = add(num1, num2)
        operation_symbol = "+"
    
    elif choice == '2':
        result = subtract(num1, num2)
        operation_symbol = "-"
        
    elif choice == '3':
        result = multiply(num1, num2)
        operation_symbol = "*"
        
    elif choice == '4':
        result = divide(num1, num2)
        operation_symbol = "/"
        
    # In kết quả
    if isinstance(result, str) and "Lỗi" in result:
        # Trường hợp chia cho 0
        print(f"Kết quả: {num1} {operation_symbol} {num2} = {result}") 
    else:
        # Trường hợp tính toán thành công
        print(f"Kết quả: {num1} {operation_symbol} {num2} = {result}")

else:
    print("❌ Lựa chọn không hợp lệ. Vui lòng chọn số từ 1 đến 4.")
