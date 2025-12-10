def check_binary_divisible_by_5():
    """
    Chấp nhận chuỗi nhị phân 4 chữ số, phân tách bằng dấu phẩy, 
    và in ra những số chia hết cho 5.
    """
    # 1. Nhập dữ liệu từ người dùng (ví dụ: 0100,0011,1010,1001)
    input_str = input("21. Nhập chuỗi số nhị phân (vd: 0100,0011,1010,1001): ")
    
    # 2. Tách chuỗi đầu vào thành một danh sách các chuỗi nhị phân
    binary_list = input_str.split(',')
    
    result_list = []
    
    # 3. Lặp qua từng chuỗi nhị phân
    for binary_str in binary_list:
        # Loại bỏ khoảng trắng (nếu có)
        binary_str = binary_str.strip() 
        
        # Kiểm tra độ dài có phải là 4 không (tùy chọn)
        if len(binary_str) != 4:
            continue

        try:
            # 4. Chuyển chuỗi nhị phân sang số thập phân (base 2)
            decimal_value = int(binary_str, 2)
            
            # 5. Kiểm tra xem số thập phân có chia hết cho 5 hay không
            if decimal_value % 5 == 0:
                # Nếu chia hết, giữ lại chuỗi nhị phân gốc
                result_list.append(binary_str)
                
        except ValueError:
            # Bỏ qua nếu chuỗi không phải là số nhị phân hợp lệ
            continue
            
    # 6. In ra kết quả, nối các chuỗi nhị phân thỏa mãn bằng dấu phẩy
    output_str = ",".join(result_list)
    
    print(f"\nĐầu vào: {input_str}")
    print(f"Đầu ra (chia hết cho 5): {output_str}")

# --- Chạy chương trình ---
if __name__ == "__main__":
    check_binary_divisible_by_5()
