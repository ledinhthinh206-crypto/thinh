# 1. Nhập chuỗi các giá trị nhị phân, phân tách bằng dấu phẩy
chuoi_dau_vao = input("Nhập chuỗi các số nhị phân (ví dụ: 1010,1111,0010): ")

# 2. Tách chuỗi thành list các giá trị dựa trên dấu phẩy (',')
# Phương thức split(',') sẽ tách chuỗi thành list
list_gia_tri = chuoi_dau_vao.split(',')

# 3. In ra các giá trị đã nhập
print("\nCác giá trị đã nhập:")
for gia_tri in list_gia_tri:
    print(gia_tri)
