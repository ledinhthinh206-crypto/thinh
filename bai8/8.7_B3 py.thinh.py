# Hàm chọn và hiển thị màu tiếp theo (ĐÃ CẬP NHẬT BƯỚC 3)
def nextColour():
    global score
    global timeleft
    global game_in_progress

    if timeleft > 0:
        # Làm cho ô nhập liệu hoạt động
        e.focus_set()

        # Lấy đáp án của người chơi
        input_colour = e.get().lower()
        # Lấy màu đúng cần gõ (Màu chữ)
        correct_colour = colours[1].lower()
        
        # --- LOGIC TÍNH ĐIỂM MỚI (BƯỚC 3) ---
        if input_colour == correct_colour:
            score += 2 # Cộng 2 điểm cho đúng
        elif input_colour != "":
            score -= 1 # Trừ 1 điểm cho sai (Chỉ trừ khi có nhập liệu)
        # -------------------------------------

        # Xóa ô nhập liệu
        e.delete(0, tkinter.END)

        # Trộn màu và hiển thị màu mới
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))

        # Cập nhật điểm số
        scorelabel.config(text="Score: " + str(score))
    
    else: # Hết giờ
        game_in_progress = False
        label.config(text="HẾT GIỜ!", fg="red")
        e.config(state='disabled')
        scorelabel.config(text="Press Enter to start", font=('Helvetica', 12))
