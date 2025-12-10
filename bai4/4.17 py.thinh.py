# Bài 17: Tìm các số phong phú (Số có tổng ước > chính nó)
import math

# Nhập số n và kiểm tra đơn giản (nếu muốn ngắn gọn hơn nữa, bỏ qua try/except)
try:
    n = int(input("Nhập n: "))
except:
    print("Lỗi nhập liệu.")
    exit()

print(f"\nCác số phong phú < {n}:")

# Lặp qua các số k từ 2 đến n-1
for k in range(2, n):
    tong_uoc = 1  # 1 luôn là ước của mọi số > 1
    
    # Tìm và cộng các ước số thực sự (từ 2 đến căn bậc hai của k)
    for i in range(2, int(math.sqrt(k)) + 1):
        if k % i == 0:
            tong_uoc += i
            uoc_doi = k // i
            if uoc_doi != i:
                tong_uoc += uoc_doi
    
    # Kiểm tra điều kiện số phong phú: Tổng các ước (không tính k) > k
    if tong_uoc > k:
        print(k)
