import numpy as np

def sort_students():
    """
    Tạo mảng cấu trúc NumPy từ dữ liệu sinh viên và sắp xếp theo 
    Lớp, sau đó là Chiều cao.
    """
    
    # 1. Dữ liệu đầu vào theo đề bài
    # Cấu trúc dữ liệu: (Tên, Lớp, Chiều cao)
    student_data = [
        ('James', 5, 48.5), 
        ('Nail', 6, 52.5), 
        ('Paul', 5, 42.1), 
        ('Pit', 5, 40.11)
    ]

    # 2. Định nghĩa kiểu dữ liệu có cấu trúc (dtype)
    # Tên (Name): U10 (Chuỗi Unicode, tối đa 10 ký tự)
    # Lớp (Class): i4 (Số nguyên 4 byte)
    # Chiều cao (Height): f4 (Số thực 4 byte)
    data_type = [
        ('Name', 'U10'), 
        ('Class', 'i4'), 
        ('Height', 'f4')
    ]

    # 3. Tạo mảng cấu trúc NumPy từ dữ liệu và dtype
    students = np.array(student_data, dtype=data_type)

    print("--- Dữ liệu sinh viên BAN ĐẦU (NumPy Structured Array) ---")
    print(students)
    print("-" * 50)
    
    # 4. Sắp xếp mảng cấu trúc
    # Sử dụng np.sort() hoặc ndarray.sort()
    # Để sắp xếp theo nhiều tiêu chí, ta truyền một list tên trường.
    # Thư viện NumPy tự động sắp xếp theo thứ tự ưu tiên trong list: 
    # [Tiêu chí chính, Tiêu chí phụ, ...]
    
    # Tiêu chí sắp xếp: 
    # Ưu tiên 1: 'Class' (Lớp)
    # Ưu tiên 2: 'Height' (Chiều cao)
    
    sorted_students = np.sort(students, order=['Class', 'Height'])

    # 5. In kết quả
    print("--- KẾT QUẢ SẮP XẾP (Theo Lớp, sau đó Chiều cao) ---")
    print(sorted_students)
    print("-" * 50)
    
    # In ra kết quả theo định dạng tuple list để khớp với kết quả mong đợi 
    # (Optional: chỉ để kiểm tra định dạng output)
    print("Kết quả ở định dạng List of Tuples:")
    print([tuple(x) for x in sorted_students])


# Chạy hàm chính
if __name__ == "__main__":
    sort_students()
