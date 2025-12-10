# Nhập số nguyên n
try:
    n = int(input("Nhập số nguyên n: "))
    
    # Kiểm tra n (nếu n <= 1, dãy chỉ có [0])
    if n <= 0:
        print("Vui lòng nhập n > 0.")
    elif n == 1:
        fib_list = [0]
    else:
        # Khởi tạo list và các biến
        fib_list = []
        a, b = 0, 1
        
        # Vòng lặp đơn giản hóa: chạy và cập nhật
        while a < n:
            fib_list.append(a)
            a, b = b, a + b # Cập nhật a và b chỉ trong một dòng
            
        # In kết quả
        print(f"List Fibonacci < {n}:")
        print(fib_list)
        
except ValueError:
    print("Lỗi: Đầu vào không phải là số nguyên.")
