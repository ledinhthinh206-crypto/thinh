import math

# Khởi tạo vị trí ban đầu của Robot tại (0, 0)
# pos[0] là tọa độ x (ngang), pos[1] là tọa độ y (dọc)
pos = [0, 0]

print("⚠️ CHÚ Ý: Nhập các lệnh di chuyển (ví dụ: UP 5, RIGHT 2).")
print("          Nhấn Enter (hoặc gửi một dòng trống) để kết thúc nhập liệu và xem kết quả.")

# Bắt đầu vòng lặp để nhận đầu vào liên tục
while True:
    # Nhận đầu vào từ người dùng
    s = input("> ")
    
    # Điều kiện dừng: nếu đầu vào là chuỗi trống
    if not s:
        break
    
    try:
        # Tách chuỗi thành hướng và số bước (ví dụ: "UP 5" -> ["UP", "5"])
        movement = s.split(" ")
        direction = movement[0].upper() # Lấy hướng và chuyển sang chữ hoa
        steps = int(movement[1])        # Lấy số bước và chuyển sang số nguyên
        
        # Cập nhật tọa độ dựa trên hướng di chuyển
        if direction == "UP":
            pos[1] += steps
        elif direction == "DOWN":
            pos[1] -= steps
        elif direction == "LEFT":
            pos[0] -= steps
        elif direction == "RIGHT":
            pos[0] += steps
        # else: Bỏ qua các lệnh không hợp lệ
            
    except Exception as e:
        # Xử lý các lỗi như thiếu số bước hoặc số bước không phải là số
        print("❌ Lỗi cú pháp. Vui lòng nhập đúng định dạng 'DIRECTION STEPS' (ví dụ: UP 5).")
        # print(f"Chi tiết lỗi: {e}") # Có thể bỏ dòng này để gọn hơn

# --- Tính toán kết quả cuối cùng ---

# Khoảng cách Euclid D = sqrt(x^2 + y^2)
x_sq = pos[0]**2
y_sq = pos[1]**2
distance = math.sqrt(x_sq + y_sq)

# In kết quả, làm tròn đến số nguyên gần nhất và chuyển sang kiểu int
final_distance = int(round(distance))

print("\n==================================")
print("✅ KẾT QUẢ CUỐI CÙNG:")
print(f"* Vị trí cuối cùng của Robot: ({pos[0]}, {pos[1]})")
print(f"* Khoảng cách thô: {distance:.4f}")
print(f"* Khoảng cách (làm tròn): **{final_distance}**")
print("==================================")
