# 1. Định nghĩa biến 'a' ở phạm vi TOÀN CỤC (Global)
a = "Hello Guy!"

# 2. Định nghĩa hàm 'say()'
def say():
    # 3. Định nghĩa biến 'a' ở phạm vi CỤC BỘ (Local). 
    # Biến này KHÁC với biến 'a' toàn cục.
    a = "Vinh University"
    
    # In biến 'a' CỤC BỘ
    print(a)

# 4. In biến 'a' TOÀN CỤC trước khi gọi hàm
print(a)

# 5. Gọi hàm say(). Hàm này sẽ in ra giá trị cục bộ của nó.
say()

# 6. In biến 'a' TOÀN CỤC sau khi hàm kết thúc. 
# Biến toàn cục KHÔNG bị thay đổi bởi hàm.
print(a)
