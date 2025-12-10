# Chương trình đảo ngược chuỗi (Không dùng file)

# Lấy chuỗi từ người dùng
input_string = input("Please enter the string you want to reverse: ")

# Lấy độ dài của chuỗi
l = len(input_string)

# Khởi tạo chuỗi kết quả đảo ngược
s = ''

# Vòng lặp để duyệt ngược chuỗi
while(l >= 1):
    # Cộng dồn ký tự từ cuối chuỗi 'input_string' vào 's'
    s = s + input_string[l-1]
    
    # Giảm chỉ mục
    l = l - 1

# In ra chuỗi đã được đảo ngược
print("Chuỗi đảo ngược là:", s)
