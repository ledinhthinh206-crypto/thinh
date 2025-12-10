import numpy as np

# 1. Tạo mảng từ 12 đến 37
x = np.arange(12, 38)

# In mảng gốc để kiểm tra
print("Mảng được tạo:")
print(x)

# 2. Đảo ngược mảng
mang_dao_nguoc = x[::-1]

# In mảng đã đảo ngược
print("\nMảng đảo ngược:")
print(mang_dao_nguoc)
