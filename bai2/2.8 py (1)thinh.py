# 1. Khởi tạo các biến
a, b = 1, 2
total = 0
fib_series = "" # Biến mới để lưu trữ dãy số

# 2. Bắt đầu vòng lặp while
while (a < 4000000):
    
    # 3. Kiểm tra số chẵn và tính tổng
    if a % 2 == 0:
        total = total + a
        
    # 4. Lưu số hạng và cập nhật dãy số
    fib_series += str(a) + ", "
    
    # Tính số Fibonacci tiếp theo
    a, b = b, a + b

# 5. In kết quả cuối cùng
# Cắt bỏ hai ký tự cuối cùng (", ") trong chuỗi dãy số
print("Dãy số Fibonacci nhỏ hơn 4,000,000:")
print(fib_series[:-2])

print("\nTổng các số chẵn trong dãy là:", total)
