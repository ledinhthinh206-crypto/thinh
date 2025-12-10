# 1. Định nghĩa biến 'a' ở phạm vi TOÀN CỤC (Global)
a = "Hello Guy!"

# 2. Định nghĩa hàm 'say()'
def say():
    # Sử dụng từ khóa 'global' để khai báo rằng biến 'a' được tham chiếu
    # và sẽ được thay đổi là biến toàn cục
    global a
    
    # 3. Thay đổi giá trị biến 'a' TOÀN CỤC
    a = "Vinh University"
    
    # 4. In biến 'a' (hiện tại là giá trị mới)
    print(a)

# 5. Gọi hàm say(). Hàm này thay đổi biến 'a' toàn cục.
say()

# 6. In biến 'a' TOÀN CỤC sau khi hàm kết thúc. 
# Giá trị ĐÃ BỊ THAY ĐỔI.
print(a)
