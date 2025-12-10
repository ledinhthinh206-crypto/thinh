# ----------------------------------------------------
# 1. MODULE HÀM bubbleSort
# ----------------------------------------------------

def bubbleSort(data):
    """
    Sắp xếp danh sách 'data' bằng thuật toán Bubble Sort.
    """
    n = len(data)
    
    # Lặp qua các lần duyệt
    for i in range(n):
        swapped = False
        
        # Lặp so sánh các cặp phần tử chưa được sắp xếp
        for j in range(0, n - i - 1):
            
            # Hoán đổi nếu phần tử hiện tại lớn hơn phần tử kế tiếp
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                
        # Tối ưu hóa: Thoát nếu không có hoán đổi nào xảy ra
        if not swapped:
            break
            
    return data

# ----------------------------------------------------
# 2. CHƯƠNG TRÌNH CHÍNH (GỌN HƠN)
# ----------------------------------------------------

def main():
    print("--- CHƯƠNG TRÌNH SẮP XẾP NỔI BỌT ---")
    
    # 1. Nhập danh sách trong một dòng (dùng List Comprehension và map)
    # Ví dụ nhập: 44 46 43 27 57 41 45 21 70
    try:
        # Nhập các số cách nhau bởi khoảng trắng và chuyển chúng thành float
        input_str = input("Nhập các phần tử (cách nhau bằng dấu cách): ")
        # Sử dụng List Comprehension và map để chuyển chuỗi nhập thành list số
        my_list = list(map(float, input_str.split()))
    except ValueError:
        print("Lỗi: Vui lòng nhập các số hợp lệ, cách nhau bằng dấu cách.")
        return
    
    if not my_list:
        print("Danh sách rỗng, không có gì để sắp xếp.")
        return
        
    # In danh sách ban đầu
    print(f"\nDanh sách BAN ĐẦU: {my_list}")

    # 2. Gọi hàm sắp xếp
    # Ta sử dụng my_list[:] để tạo một bản sao, tránh thay đổi list gốc nếu cần.
    # Tuy nhiên, hàm bubbleSort này đã được viết để thay đổi list gốc (in-place)
    # nên ta chỉ cần gọi trực tiếp.
    sorted_list = bubbleSort(my_list)

    # 3. In kết quả cuối cùng
    print(f"Danh sách SAU KHI SẮP XẾP: {sorted_list}")
    
    print("\n--- Dữ liệu mẫu kiểm tra ---")
    sample_data = [44, 46, 43, 27, 57, 41, 45, 21, 70]
    # Sắp xếp bản sao để kiểm tra
    print(f"Mẫu: {sample_data} -> Kết quả: {bubbleSort(sample_data.copy())}")


# Chạy chương trình chính
if __name__ == "__main__":
    main()
