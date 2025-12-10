import tkinter
import random

# Danh sách màu có thể dùng
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = 0
# Vị trí 1: Thay đổi thời gian khởi tạo từ 30 -> 120
timeleft = 120  
game_in_progress = False

# Hàm bắt đầu game
def startGame(event):
    global game_in_progress
    global timeleft
    
    if not game_in_progress:
        game_in_progress = True
        # Vị trí 2: Thay đổi thời gian đặt lại khi bắt đầu từ 30 -> 120
        timeleft = 120  
        scorelabel.config(text="Score: 0")
        countdown()
        nextColour()

# Hàm chọn và hiển thị màu tiếp theo (Logic tính điểm CŨ, chưa thực hiện Bước 3)
def nextColour():
    global score
    global timeleft
    global game_in_progress

    if timeleft > 0:
        e.focus_set()

        input_colour = e.get().lower()
        correct_colour = colours[1].lower()
        
        # Logic tính điểm GỐC của Bước 1 (+1 điểm cho đúng)
        if input_colour == correct_colour:
            score += 1 
        
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scorelabel.config(text="Score: " + str(score))
    
    else: # Hết giờ
        game_in_progress = False
        label.config(text="HẾT GIỜ!", fg="red")
        e.config(state='disabled')
        scorelabel.config(text="Press Enter to start", font=('Helvetica', 12))


# Hàm đếm ngược thời gian
def countdown():
    global timeleft
    global game_in_progress

    if game_in_progress and timeleft > 0:
        timeleft -= 1
        timelabel.config(text="Time left: " + str(timeleft))
        timelabel.after(1000, countdown)
    elif timeleft == 0:
        nextColour()

# Driver Code: Thiết lập GUI
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x200")

# Nhãn hướng dẫn
instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!",
                             font=('Helvetica', 12))
instructions.pack()

# Nhãn điểm số (Ban đầu là hướng dẫn)
scorelabel = tkinter.Label(root, text="Press enter to start",
                           font=('Helvetica', 12))
scorelabel.pack()

# Nhãn thời gian còn lại (Sẽ hiển thị 120s ngay khi chạy)
timelabel = tkinter.Label(root, text="Time left: " + str(timeleft),
                          font=('Helvetica', 12))
timelabel.pack()

# Nhãn hiển thị màu
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# Ô nhập liệu
e = tkinter.Entry(root)
# Liên kết phím Enter với hàm startGame
root.bind('<Return>', startGame) 
e.pack()

e.focus_set()

root.mainloop()
