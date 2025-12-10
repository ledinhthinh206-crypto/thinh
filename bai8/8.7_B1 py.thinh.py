import tkinter
import random

# Khai báo cơ bản
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 30  # Giá trị gốc (sẽ thay đổi ở Bước 2)
game_in_progress = False

# Hàm bắt đầu game
def startGame(event):
    global game_in_progress
    global timeleft
    
    if not game_in_progress:
        game_in_progress = True
        timeleft = 30 # Giá trị gốc
        scorelabel.config(text="Score: 0")
        countdown()
        nextColour()

# Hàm kiểm tra màu (Logic tính điểm GỐC: đúng +1)
def nextColour():
    global score
    global timeleft
    global game_in_progress

    if timeleft > 0:
        e.focus_set()

        input_colour = e.get().lower()
        correct_colour = colours[1].lower()
        
        # LOGIC GỐC: Cộng 1 điểm
        if input_colour == correct_colour:
            score += 1
        
        # Xử lý sai (trước Bước 3 thì không trừ điểm)
        
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scorelabel.config(text="Score: " + str(score))
    
    else: 
        game_in_progress = False
        label.config(text="HẾT GIỜ!", fg="red")
        e.config(state='disabled')
        scorelabel.config(text="Press Enter to start", font=('Helvetica', 12))

# Hàm đếm ngược
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

instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!", font=('Helvetica', 12))
instructions.pack()

scorelabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scorelabel.pack()

timelabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timelabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)
root.bind('<Return>', lambda event: nextColour()) 
e.pack()

e.focus_set()
root.mainloop()
