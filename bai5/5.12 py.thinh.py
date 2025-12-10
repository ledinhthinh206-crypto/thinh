import numpy as np

def sort_students_by_height():
    """
    Sắp xếp ID sinh viên theo chiều cao tăng dần sử dụng np.lexsort().
    """
    
    # 1. Dữ liệu đầu vào
    student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
    student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])

    print("--- Dữ liệu BAN ĐẦU ---")
    print(f"ID Sinh viên:   {student_id}")
    print(f"Chiều cao:      {student_height}")
    print("-" * 50)
    
    # 2. Sử dụng np.lexsort() để tìm chỉ mục sắp xếp
    # Lexsort sắp xếp mảng dựa trên mảng cuối cùng trong tuple/list được truyền vào.
    # Cú pháp: np.lexsort((key_phụ, key_chính, ...))
    # Yêu cầu: Sắp xếp ID theo Chiều cao. Chiều cao là key chính.
    
    # Trường hợp này chỉ có 1 key sắp xếp là student_height.
    # lexsort trả về một mảng chỉ mục (indices) mà khi áp dụng cho các mảng
    # sẽ sắp xếp chúng theo đúng thứ tự.
    
    # Lưu ý: lexsort sắp xếp theo chiều tăng dần (ascending)
    indices = np.lexsort((student_height,)) 
    
    print("--- KẾT QUẢ LEXSORT ---")
    print(f"Chỉ số sắp xếp: {indices}")
    
    # 3. Áp dụng chỉ mục (indices) để sắp xếp cả hai mảng
    # student_id[indices] sẽ sắp xếp mảng student_id
    # student_height[indices] sẽ sắp xếp mảng student_height
    
    sorted_id = student_id[indices]
    sorted_height = student_height[indices]

    # 4. In kết quả đã sắp xếp
    print("\n--- DỮ LIỆU SAU KHI SẮP XẾP (Theo Chiều cao tăng dần) ---")
    
    # Hiển thị theo định dạng ID | Chiều cao như kết quả mẫu
    print("{:<5} | {:<5}".format("ID", "Chiều cao"))
    print("-" * 15)
    for id_val, height_val in zip(sorted_id, sorted_height):
        print(f"{id_val:<5} | {height_val:<5.1f}")
        
    print("-" * 50)
    
    # 5. So sánh với kết quả mẫu (để kiểm tra)
    # Kết quả sắp xếp theo đề bài có vẻ đã xử lý các trường hợp bằng nhau 
    # (như 40.0, 42.0) theo thứ tự ID/Chỉ mục ban đầu hoặc ID tăng dần.
    # Kết quả của lexsort:
    # 1682 (38.0)
    # 1023 (40.0)
    # 5241 (40.0) 
    # 1671 (41.0)
    # 5202 (42.0)
    # 4532 (42.0)
    # 6230 (45.0)

# Chạy hàm chính
if __name__ == "__main__":
    sort_students_by_height()
