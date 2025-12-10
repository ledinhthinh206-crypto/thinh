# 1. Nhập chuỗi từ người dùng
chuoi_dau_vao = input("Nhập chuỗi các từ (cách nhau bởi dấu cách): ")

# 2. Tách chuỗi thành list các từ (dựa trên dấu cách ' ')
# Ví dụ: nếu người dùng nhập "banana apple cherry" -> list_tu = ['banana', 'apple', 'cherry']
list_tu = chuoi_dau_vao.split(' ')

# 3. Sắp xếp list các từ theo thứ tự từ điển (A-Z)
list_tu.sort()

# 4. In ra màn hình các từ đã sắp xếp
print("\nCác từ sau khi sắp xếp theo thứ tự từ điển là:")
for tu in list_tu:
    print(tu)
