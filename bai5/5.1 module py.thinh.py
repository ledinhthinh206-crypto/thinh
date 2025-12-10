# Tên File: mymath.py

def square(n):
    """Tính bình phương (n * n) của một số."""
    return n * n

def cube(n):
    """Tính lập phương (n * n * n) của một số."""
    return n * n * n

def average(values):
    """Tính giá trị trung bình cộng của một danh sách các số."""
    nvals = len(values)
    sum_val = 0.0
    for v in values:
        sum_val = sum_val + v
    
    # Tránh chia cho 0 nếu danh sách rỗng
    if nvals == 0:
        return 0.0
        
    return sum_val / nvals
# Tên File: main_script.py

# 1. Cách import tiêu chuẩn: import <tên_module>
import mymath 
# import mymath # Note no .py

values = [2, 4, 6, 8, 10]

print("Giá trị danh sách:", values)

# Sử dụng hàm square()
print('\nBình phương (Squares):')
for v in values:
    # Cú pháp: module_name.function_name(argument)
    print(f'Số {v} bình phương là: {mymath.square(v)}')

# Sử dụng hàm cube()
print('\nLập phương (Cubes):')
for v in values:
    print(f'Số {v} lập phương là: {mymath.cube(v)}')

# Sử dụng hàm average()
avg_result = mymath.average(values)
print(f'\nGiá trị Trung bình (Average): {avg_result}') 
# Kết quả sẽ là 'Average: 6.0' (vì 30/5 = 6)


# 2. Cách import với tên viết tắt: import <tên_module> as <tên_mới>
import mymath as mt

print('\n' + '='*30)
print('Sử dụng tên viết tắt (mt.square):')
print(f'Bình phương của 2 là: {mt.square(2)}')
print(f'Bình phương của 3 là: {mt.square(3)}')
