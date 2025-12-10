def count_case_letters():
    """
    Chấp nhận một chuỗi đầu vào và đếm số lượng chữ cái hoa và thường.
    """
 
    count_upper = 0
    count_lower = 0
    

    input_sentence = input(". Nhập một câu hoặc chuỗi ký tự : ")
    
  
            
  
    print(f"\nĐầu vào: {input_sentence}")
    print(f"Chữ hoa: {count_upper}")
    print(f"Chữ thường: {count_lower}")

# --- Chạy chương trình ---
if __name__ == "__main__":
    count_case_letters()
