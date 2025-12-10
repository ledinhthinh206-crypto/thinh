def count_letters_and_digits():
    """
    Chấp nhận một chuỗi đầu vào và đếm số lượng chữ cái và chữ số.
    """
    # Khởi tạo biến đếm
    count_letters = 0
    count_digits = 0
    
    # 1. Chấp nhận đầu vào là một câu/chuỗi
    input_sentence = input("23. Nhập một câu hoặc chuỗi ký tự: ")
    
    # 2. Lặp qua từng ký tự trong chuỗi
    for char in input_sentence:
        # Kiểm tra xem ký tự đó có phải là chữ cái không
        if char.isalpha():
            count_letters += 1
        
        # Kiểm tra xem ký tự đó có phải là chữ số không
        elif char.isdigit():
            count_digits += 1
            
    # 3. In kết quả theo định dạng yêu cầu
    print(f"\nĐầu vào: {input_sentence}")
    print(f"Số chữ cái là: {count_letters}")
    print(f"Số chữ số là: {count_digits}")

# --- Chạy chương trình ---
if __name__ == "__main__":
    count_letters_and_digits()
