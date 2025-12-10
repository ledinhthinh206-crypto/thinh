
import turtle

# --- Khởi tạo và Thiết lập ---
painter = turtle.Turtle()
painter.speed(0) # Tốc độ vẽ tối đa
painter.pensize(2)

colors = ["red", "green", "blue", "purple", "darkred", "gold", "teal"] # Danh sách màu

radius = 100
num_circles = 18 # Số hình tròn cần vẽ để tạo ra hoa văn đối xứng

# --- Vòng lặp Vẽ và Xoay ---
for i in range(num_circles):
    
    # Đặt màu theo chu kỳ (để màu sắc lặp lại)
    painter.pencolor(colors[i % len(colors)])
    
    # Vẽ hình tròn
    painter.circle(radius)
    
    # Xoay góc cố định: 360 độ chia cho số hình tròn (360/18 = 20 độ)
    painter.right(360 / num_circles)

# Hoàn tất và ẩn rùa
painter.hideturtle()
turtle.done()
