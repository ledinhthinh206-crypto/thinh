import tkinter as tk
from tkinter import ttk

def run_bai_8a():
    # 1. Khởi tạo cửa sổ chính
    root_a = tk.Tk()
    root_a.title("Bài 8a: Form Thông tin Cá nhân")

    # Danh sách các trường thông tin
    fields = ["Họ tên:", "Ngày tháng năm sinh:", "MSSV:", "Ngành học:"]

    row_num = 0

    for field in fields:
        # Tạo Label (Nhãn)
        tk.Label(root_a, text=field).grid(row=row_num, column=0, sticky='w', padx=10, pady=5)
        
        # Tạo Entry (Hộp nhập liệu)
        tk.Entry(root_a, width=40).grid(row=row_num, column=1, padx=10, pady=5)
        
        row_num += 1

    # 4. VÒNG LẶP CHÍNH
    root_a.mainloop()

if __name__ == '__main__':
    run_bai_8a()
