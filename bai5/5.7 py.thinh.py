import numpy as np

# 1. Định nghĩa kiểu dữ liệu (dtype) cho mảng có cấu trúc
# 'name': chuỗi 15 ký tự (S15), 'class': số nguyên (int), 'height': số thực (float)
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# 2. Định nghĩa dữ liệu sinh viên
# Dữ liệu mẫu (Tên, Lớp, Chiều cao)
students_details = [('James', 5, 48.3), ('Nail', 6, 52.5), ('Paul', 5, 42.10), ('Pit', 5, 40.11)]

# 3. Tạo mảng có cấu trúc (Structured Array)
students = np.array(students_details, dtype=data_type)

print("Mảng gốc (Original array):")
print(students)

# 4. Sắp xếp mảng theo trường 'height' (chiều cao)
# np.sort(a, order='field')
sorted_students = np.sort(students, order='height')

print("\nMảng đã sắp xếp theo chiều cao (Sort by height):")
print(sorted_students)
