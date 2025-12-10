class py_solution:
    """Class Chuyển đổi Số La Mã thành Số Nguyên."""
    
    def roman_to_int(self, s):
        # Khởi tạo dictionary giá trị
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        
        # Duyệt chuỗi từ trái sang phải
        for i in range(len(s)):
            current_val = rom_val[s[i]]
            
            # Kiểm tra xem có ký tự kế tiếp và giá trị kế tiếp có lớn hơn không
            if i + 1 < len(s) and current_val < rom_val[s[i+1]]:
                # Trường hợp trừ (ví dụ: IV, IX): Trừ đi giá trị hiện tại
                int_val -= current_val
            else:
                # Trường hợp cộng (Bình thường): Cộng giá trị hiện tại
                int_val += current_val
                
        return int_val

# --- Ví dụ kiểm tra ---
py_sol = py_solution()

# MCMXCIV = 1994
print(f"'MCMXCIV' -> {py_sol.roman_to_int('MCMXCIV')}")

# MMMCMXLVIII = 3948
print(f"'MMMCMXLVIII' -> {py_sol.roman_to_int('MMMCMXLVIII')}")

# CC = 200
print(f"'CC' -> {py_sol.roman_to_int('CC')}")
