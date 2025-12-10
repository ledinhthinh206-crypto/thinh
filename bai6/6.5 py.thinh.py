class py_solution:
    """Class chứa phương thức đảo ngược thứ tự các từ trong chuỗi."""
    
    def reverse_words(self, s):
        """
        Thực hiện đảo ngược thứ tự các từ trong chuỗi s.
        Logic: Tách chuỗi thành từ -> Đảo ngược thứ tự -> Ghép lại.
        """
        # ['hello', 'py'] -> reversed -> 'py hello'
        return ' '.join(reversed(s.split()))

# ----------------------------------------------------
# --- Ví dụ kiểm tra ---
# ----------------------------------------------------
py_sol = py_solution()

# Dữ liệu vào theo đề bài: 'hello py'
input_string = 'hello py' 
result = py_sol.reverse_words(input_string)

print(f"Chuỗi ban đầu: '{input_string}'")
# Lưu ý: Kết quả chuẩn của việc đảo ngược là 'py hello'. 
# Nếu bạn cần đầu ra là ':py hello' như trong đề, bạn chỉ cần thêm ':' vào trước kết quả.
print(f"Chuỗi sau khi đảo ngược từ: '{result}'")

# Ví dụ kiểm tra khác
print(f"Mẫu: 'Day la mot bai tap' -> '{py_sol.reverse_words('Day la mot bai tap')}'")
