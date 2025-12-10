def pascal_triangle(n):
    """In n dòng đầu tiên của tam giác Pascal."""
    if n <= 0:
        return
        
    prev_row = []
    
    for _ in range(n):
        current_row = [1] 
        
        # Tính toán các giá trị giữa bằng cách lấy tổng các cặp kề nhau của dòng trước
        if prev_row:
            for j in range(len(prev_row) - 1):
                current_row.append(prev_row[j] + prev_row[j+1])
            current_row.append(1)
        
        # In dòng hiện tại (căn giữa để đẹp hơn, có thể bỏ .center() nếu không cần)
        print(" ".join(map(str, current_row)).center(n * 3))
        
        # Cập nhật dòng trước
        prev_row = current_row

# --- Chạy chương trình ---
try:
    N = int(input("Nhập số dòng n (Pascal): "))
    print("\nTam giác Pascal:")
    pascal_triangle(N)
except ValueError:
    print("Lỗi: Đầu vào không phải là số nguyên.")
