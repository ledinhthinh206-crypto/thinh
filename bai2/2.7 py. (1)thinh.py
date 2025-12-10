# 1. Yêu cầu nhập số n
n = int(input("Nhập vào một số: "))

# 2. Khởi tạo Dictionary
d = {}

# 3. & 4. Lặp từ 1 đến n và gán key: value
for i in range(1, n + 1):
    # Key là i, Value là i^2
    d[i] = i * i

# 5. In kết quả
print(d)
