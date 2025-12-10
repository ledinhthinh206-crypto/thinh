import tkinter as tk
from tkinter import IntVar

def ShowChoice():
    # Lấy giá trị hiện tại (1, 2, 3...)
    choice_value = v.get()
    
    # Tìm tên ngôn ngữ tương ứng
    choice_name = [name for name, val in languages if val == choice_value][0]
    
    print(f"Bạn đã chọn: {choice_name}")

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Indicator Buttons")

# Biến điều khiển và thiết lập mặc định (Python, value=1)
v = IntVar()
v.set(1)

# Danh sách ngôn ngữ (Tên, Giá trị)
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C#", 5)
]

# Label hướng dẫn
tk.Label(
    root,
    text="Choose your favourite\nprogramming language:",
    justify=tk.LEFT,
    padx=20
).pack(anchor=tk.W)

# Tạo các Radiobutton với indicatoron=0
for language, val in languages:
    tk.Radiobutton(
        root,
        text=language,
        indicatoron=0, # Tắt vòng tròn radio button, biến thành indicator
        width=20,      # Chiều rộng cố định
        variable=v,
        command=ShowChoice,
        value=val
    ).pack(anchor=tk.W, pady=2) # anchor=tk.W căn lề trái, pady=2 thêm chút khoảng trống

root.mainloop()
