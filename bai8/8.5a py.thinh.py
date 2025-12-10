import tkinter as tk
from tkinter import IntVar

# 1. Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Chọn Ngôn Ngữ")

# 2. Định nghĩa biến điều khiển (Intvar) và giá trị mặc định
v = IntVar()
# Thiết lập giá trị mặc định là 1 (tương ứng với Python)
v.set(1)

# 3. Định nghĩa danh sách các ngôn ngữ (text, value)
# Giá trị value phải là số nguyên (integer) vì ta dùng IntVar()
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C#", 5)
]

# 4. Hàm xử lý khi radio button được chọn
def ShowChoice():
    # Lấy giá trị hiện tại của biến v (giá trị của ngôn ngữ được chọn)
    choice_value = v.get()
    # Tìm tên ngôn ngữ tương ứng để in ra
    choice_name = [name for name, val in languages if val == choice_value][0]
    print(f"Ngôn ngữ yêu thích của bạn là: {choice_name} (Value: {choice_value})")

# 5. Thêm Label hướng dẫn
tk.Label(
    root,
    text="Choose your favourite\nprogramming language:",
    justify=tk.LEFT,
    padx=20
).pack()

# 6. Tạo và đóng gói (pack) các Radiobutton
for language, val in languages:
    tk.Radiobutton(
        root,
        text=language,
        padx=20,
        variable=v, # Liên kết với biến điều khiển v
        command=ShowChoice, # Gọi hàm ShowChoice khi nút được nhấn
        value=val # Giá trị gán cho biến v khi nút này được chọn
    ).pack(anchor=tk.W) # anchor=tk.W căn lề trái

# 7. Khởi chạy vòng lặp sự kiện chính của tkinter
root.mainloop()
