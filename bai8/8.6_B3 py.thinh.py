import tkinter as tk
from tkinter import Menu, messagebox # Import cả messagebox

# --- Cập nhật các hàm xử lý để sử dụng messagebox ---
def NewFile():
    messagebox.showinfo("Thông báo", "Lệnh New File đã được chọn!")

def OpenFile():
    # Thêm hộp thoại thông báo cho OpenFile
    messagebox.showinfo("Thông báo", "Lệnh Open File đã được chọn!")

def Exit():
    # Lệnh Exit (thoát)
    root.quit()

def About():
    messagebox.showinfo("About", "Đây là ví dụ đơn giản về Menu Bar với tkinter.")

def InsText():
    # Thêm hộp thoại thông báo cho InsText
    messagebox.showinfo("Thông báo", "Lệnh Insert Text đã được chọn!")

def InsPic():
    # Thêm hộp thoại thông báo cho InsPic
    messagebox.showinfo("Thông báo", "Lệnh Insert Picture đã được chọn!")
# --- Hết Khai báo hàm ---


# 1. Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Menu Hoàn Chỉnh")
root.geometry("300x200") 

# 2. Tạo thanh Menu Bar
menu = Menu(root)
root.config(menu=menu)

# 3. Cập nhật Menu "File"
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu) 
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator() 
filemenu.add_command(label="Exit", command=Exit) # Sử dụng hàm Exit()

# 4. Tạo MENU "Insert"
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

# 5. Menu "Help"
helpmenu = Menu(menu, tearoff=0) 
menu.add_cascade(label="Help", menu=helpmenu) 
helpmenu.add_command(label="About...", command=About)

# Vòng lặp chính
root.mainloop()
