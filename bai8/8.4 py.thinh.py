from tkinter import *

# 1. Xây dựng cửa sổ đồ họa (Window Form)
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200') # Đặt kích thước cửa sổ (ngang x dọc)

# Tạo Nhãn (Label)
# Label là widget hiển thị văn bản tĩnh
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0) # Đặt nhãn vào ô (cột 0, hàng 0)

# 3. Xây dựng phương thức xử lý sự kiện (Hàm clicked)
def clicked():
    # Thao tác này sẽ được thực hiện khi nút bấm
    lbl.configure(text="Button was clicked !!")

# 2. Thêm một widget (Button)
# Tạo nút bấm (Button)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0) # Đặt nút bấm vào ô (cột 1, hàng 0)

# Khởi chạy vòng lặp sự kiện chính của Tkinter
window.mainloop()
