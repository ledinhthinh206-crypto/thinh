# Tên file: demnguoc.py (Bạn có thể đặt tên bất kỳ)

# Yêu cầu người dùng nhập số và chuyển nó thành số nguyên
n = int(input("Enter A Number--->"))

# Bắt đầu vòng lặp while, lặp lại miễn là n còn lớn hơn hoặc bằng 0
while n >= 0:
    # In giá trị hiện tại của n
    print(n)
    
    # Giảm n đi 1 để tiến đến 0 và kết thúc vòng lặp
    n = n - 1
