# Yêu cầu người dùng nhập chuỗi
S = input('Nhập chuỗi: ')

print('\n--- Kết quả in ra (Đã bỏ qua khoảng trắng/tab) ---')

# Bắt đầu vòng lặp qua từng ký tự trong chuỗi S
for ch in S:
    # Phương thức .isspace() kiểm tra xem 'ch' có phải là ký tự khoảng trắng, tab, hoặc xuống dòng không.
    # Sử dụng 'not' để chỉ thực hiện in khi ký tự đó KHÔNG phải là khoảng trắng.
    if not ch.isspace():
        print(ch)
