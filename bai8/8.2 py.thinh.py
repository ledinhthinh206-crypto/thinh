import turtle
import random

# Danh sách các màu sẽ được chọn ngẫu nhiên
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Khởi tạo đối tượng rùa và cài đặt bút
painter = turtle.Turtle()
painter.pensize(3)

# Vòng lặp chính: Vẽ 10 hình tròn
for i in range(10):
    # 1. Chọn màu ngẫu nhiên và đặt cho nét bút
    color = random.choice(colors)
    painter.pencolor(color)
    
    # 2. Vẽ hình tròn bán kính 100
    painter.circle(100)
    
    # 3. Thay đổi hướng và đưa rùa về vị trí gốc (0, 0)
    # Lưu ý: Các lệnh quay chỉ thay đổi hướng, setposition là lệnh quyết định vị trí tiếp theo
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0) # Đảm bảo rùa luôn trở về trung tâm màn hình
    
# Giữ cửa sổ đồ họa mở cho đến khi người dùng đóng
turtle.done()
