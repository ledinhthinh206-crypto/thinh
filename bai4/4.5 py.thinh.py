# 1. Nhập chuỗi và chuyển thành danh sách (giống như Câu 4)
ds = input('Nhập danh sách: ').split()

# 2. Đảo ngược danh sách
# Sử dụng slicing [::-1] để tạo ra một danh sách mới đảo ngược
ds_dao_nguoc = ds[::-1]

print('\n--- Kết quả in theo thứ tự ngược lại ---')

# 3. In từng phần tử của danh sách đã đảo ngược trên một dòng
for tu in ds_dao_nguoc:
    print(tu)
