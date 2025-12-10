l = [1, 'python', 4, 7]
k = ['cse', 2, 'guntur', 8]
m = []

# Gán danh sách l và k vào danh sách m
m.append(l)
m.append(k)

# In danh sách m (danh sách lồng nhau)
print(m)

# Tạo từ điển d, sử dụng l, k và m làm giá trị
d = {1: l, 2: k, 'combine_list': m}

# In từ điển d
print(d)
