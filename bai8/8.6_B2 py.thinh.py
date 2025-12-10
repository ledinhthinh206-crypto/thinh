from tkinter import *

# --- Khai báo các hàm xử lý (sẽ hoàn thiện ở Bước 3) ---
def NewFile():
    print("New File!")
def OpenFile():
    print("Open File Selected")
def About():
    print("This is a simple example of a menu")
def InsText():
    print("Insert Text Selected")
def InsPic():
    print("Insert Picture Selected")
# --- Hết Khai báo hàm ---

# 1. Khởi tạo cửa sổ chính (root window)
root = Tk()
root.title("Custom Menu")
root.geometry("300x200") # Thiết lập kích thước cửa sổ

# 2. Tạo thanh Menu Bar
menu = Menu(root)
root.config(menu=menu)

# 3. Cập nhật Menu "File"
filemenu = Menu(menu, tearoff=0) # tearoff=0 loại bỏ dấu gạch ngang ở đầu menu
menu.add_cascade(label="File", menu=filemenu) 
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile) # THÊM Open
filemenu.add_separator() 
filemenu.add_command(label="Exit", command=root.quit)

# 4. TẠO MENU "Insert" MỚI
insertmenu = Menu(menu, tearoff=0) # Tạo menu con Insert
menu.add_cascade(label="Insert", menu=insertmenu) # Thêm Insert menu vào thanh Menu Bar
insertmenu.add_command(label="Text", command=InsText) # Mục Text
insertmenu.add_command(label="Picture", command=InsPic) # Mục Picture

# 5. Cập nhật Menu "Help"
helpmenu = Menu(menu, tearoff=0) 
menu.add_cascade(label="Help", menu=helpmenu) 
helpmenu.add_command(label="About...", command=About)

# Vòng lặp chính
mainloop()
