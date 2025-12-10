from tkinter import *

# Hàm xử lý cho menu "New"
def NewFile():
    print("New File!")

# Hàm xử lý cho menu "About..."
def About():
    print("This is a simple example of a menu")

# 1. Khởi tạo cửa sổ chính (root window)
root = Tk()
root.title("Menu Example")

# 2. Tạo thanh Menu Bar
menu = Menu(root)
root.config(menu=menu) # Đặt menu bar này vào cửa sổ

# 3. Tạo Menu "File" và thêm vào thanh Menu Bar
filemenu = Menu(menu) # Tạo menu con
menu.add_cascade(label="File", menu=filemenu) # Thêm File menu vào thanh Menu Bar
filemenu.add_command(label="New", command=NewFile)
filemenu.add_separator() # Dòng ngăn cách
filemenu.add_command(label="Exit", command=root.quit) # Lệnh thoát ứng dụng

# 4. Tạo Menu "Help" và thêm vào thanh Menu Bar
helpmenu = Menu(menu) # Tạo menu con
menu.add_cascade(label="Help", menu=helpmenu) # Thêm Help menu vào thanh Menu Bar
helpmenu.add_command(label="About...", command=About)

# Vòng lặp chính
mainloop()
