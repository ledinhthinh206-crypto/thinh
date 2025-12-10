# 1. Nhập chuỗi và chuyển thành danh sách (list)
# .split() sẽ tự động tách chuỗi dựa trên khoảng trắng, tab, và xuống dòng.
ds = input('Danh sách: ').split()

# 2. In cả dãy vừa nhập (in danh sách ds)
print(ds)

# 3. In từng phần tử trên một dòng
for so in ds:
    print(so)
