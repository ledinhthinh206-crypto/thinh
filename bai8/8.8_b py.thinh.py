import tkinter as tk
from tkinter import messagebox

def run_bai_8b():
    # 1. Khởi tạo cửa sổ chính
    root_b = tk.Tk()
    root_b.title("Bài 8b: Radio Button và Button")
    
    row_num = 0

    # Biến chứa giá trị của Radio Button (sẽ là 1, 2, hoặc 3)
    radio_value = tk.IntVar(root_b, 1) # Mặc định chọn giá trị 1

    def click_me_action():
        """Hàm xử lý khi nhấn nút Click Me, hiển thị giá trị Radio Button đã chọn."""
        selected = radio_value.get()
        messagebox.showinfo("Thông báo", f"Bạn đã chọn: {selected}")

    # 1. Tạo Label "Welcome"
    tk.Label(root_b, text="Welcome").grid(row=row_num, column=0, sticky='w', padx=10, pady=5)

    # 2. Tạo các Radio Button 
    # Đặt tất cả trên cùng một hàng (row_num)
    tk.Radiobutton(root_b, text="First", variable=radio_value, value=1).grid(row=row_num, column=1, sticky='w')
    tk.Radiobutton(root_b, text="Second", variable=radio_value, value=2).grid(row=row_num, column=2, sticky='w')
    tk.Radiobutton(root_b, text="Third", variable=radio_value, value=3).grid(row=row_num, column=3, sticky='w')

    # 3. Tạo Nút "Click Me"
    # Đặt nút ở hàng tiếp theo
    tk.Button(root_b, text="Click Me", command=click_me_action).grid(row=row_num + 1, column=3, sticky='e', padx=10, pady=5)

    # 4. VÒNG LẶP CHÍNH
    root_b.mainloop()

if __name__ == '__main__':
    run_bai_8b()
