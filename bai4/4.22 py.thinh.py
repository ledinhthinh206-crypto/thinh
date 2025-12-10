def find_even_digit_numbers():
    """
    Tìm các số từ 1000 đến 3000 mà tất cả các chữ số của nó đều là số chẵn, 
    và in chúng ra, phân tách bằng dấu phẩy.
    """
    # Phạm vi tìm kiếm: từ 1000 đến 3000 (bao gồm cả 3000)
    start = 1000
    end = 3000
    
    result_list = []
    
    # Duyệt qua các số trong phạm vi
    for number in range(start, end + 1):
        # Chuyển số thành chuỗi để kiểm tra từng chữ số
        s = str(number)
        
        # Kiểm tra điều kiện: TẤT CẢ các chữ số có phải là số chẵn không
        # Lưu ý: 3xxx sẽ không bao giờ thỏa mãn vì 3 là số lẻ.
        # Tuy nhiên, vòng lặp vẫn chạy đến 3000.
        is_all_even = True
        for digit in s:
            if int(digit) % 2 != 0: # Nếu gặp bất kỳ số lẻ nào
                is_all_even = False
                break
        
        if is_all_even:
            result_list.append(s)
            
    # Nối list kết quả thành một chuỗi phân tách bằng dấu phẩy
    output_str = ",".join(result_list)
    
    print(f"\n22. Các số từ {start} đến {end} có tất cả chữ số chẵn là:")
    print(output_str)

# --- Chạy chương trình ---
if __name__ == "__main__":
    find_even_digit_numbers()
