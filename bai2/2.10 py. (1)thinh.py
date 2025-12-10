# Khai báo chuỗi đầu vào
a = "hi i am python programmer"

# Bước 1: Tách chuỗi (Split)
# Phương thức .split() sẽ tự động tách chuỗi a tại các khoảng trắng, 
# kết quả là một danh sách (list) các từ.
b = a.split()

# In ra danh sách b để kiểm tra
print("Danh sách b sau khi SPLIT:")
print(b)

# Bước 2: Ghép chuỗi (Join)
# Phương thức .join(b) được gọi bởi chuỗi phân cách " ". 
# Nó dùng khoảng trắng này để nối các phần tử trong danh sách b lại thành một chuỗi mới.
c = " ".join(b)

# In ra chuỗi c để kiểm tra
print("\nChuỗi c sau khi JOIN:")
print(c)
