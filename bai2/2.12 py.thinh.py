import re

# 1. Nhập chuỗi mật khẩu và tách thành danh sách
# Ví dụ: "Abd1234@!,F1#w2W3E*,We3345"
password_string = input("Nhập các mật khẩu (cách nhau bằng dấu phẩy): ")
passwords = [p.strip() for p in password_string.split(',')]
# Sử dụng list comprehension để loại bỏ khoảng trắng dư thừa (.strip())

valid_passwords = []

print("\n--- Bắt đầu kiểm tra ---")

# 2. Lặp qua từng mật khẩu trong danh sách
for p in passwords:
    # Biến cờ (flag) để theo dõi tính hợp lệ của mật khẩu hiện tại
    is_valid = True
    
    # 3. Kiểm tra Độ dài (Tiêu chí 5 & 6)
    if len(p) < 6 or len(p) > 12:
        # print(f"'{p}' KHÔNG hợp lệ: Độ dài {len(p)}.")
        is_valid = False
    
    # Nếu độ dài không hợp lệ, chuyển sang mật khẩu tiếp theo
    if not is_valid:
        continue
        
    # 4. Kiểm tra Biểu thức chính quy (RegEx) cho các tiêu chí còn lại
    
    # Tiêu chí 1: Ít nhất 1 chữ thường [a-z]
    if not re.search("[a-z]", p):
        # print(f"'{p}' KHÔNG hợp lệ: Thiếu chữ thường.")
        is_valid = False
        
    # Tiêu chí 3: Ít nhất 1 chữ HOA [A-Z]
    if not re.search("[A-Z]", p):
        # print(f"'{p}' KHÔNG hợp lệ: Thiếu chữ HOA.")
        is_valid = False
        
    # Tiêu chí 2: Ít nhất 1 số [0-9]
    if not re.search("[0-9]", p):
        # print(f"'{p}' KHÔNG hợp lệ: Thiếu số.")
        is_valid = False
        
    # Tiêu chí 4: Ít nhất 1 ký tự đặc biệt [$#@]
    # Lưu ý: $ cần được thoát (escape) trong một số ngữ cảnh RegEx, 
    # nhưng trong [..] thì an toàn.
    if not re.search("[$#@]", p):
        # print(f"'{p}' KHÔNG hợp lệ: Thiếu ký tự đặc biệt ($#@).")
        is_valid = False

    # 5. Lưu trữ kết quả: Nếu tất cả kiểm tra đều thành công
    if is_valid:
        valid_passwords.append(p)

print("--- Kết thúc kiểm tra ---")

# In danh sách các mật khẩu hợp lệ
print(f"\nCác mật khẩu hợp lệ là: {', '.join(valid_passwords)}")
