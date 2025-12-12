print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
import tkinter
import random

# Danh sách màu
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = +2
timeleft = 120

# Bắt đầu trò chơi
def startGame(event):
    global timeleft
    if timeleft == 30:
        countdown()
    nextColour()

# Chọn màu tiếp theo
def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()

        # Nếu màu gõ đúng
        if e.get().lower() == label.cget("fg").lower():
            score += 1

        # Xóa ô nhập
        e.delete(0, tkinter.END)

        # Xáo trộn danh sách màu
        random.shuffle(colours)

        # Hiển thị màu mới
        label.config(fg=str(colours[1]), text=str(colours[0]))

        # Cập nhật điểm
        scoreLabel.config(text="Score: " + str(score))

# Đồng hồ đếm ngược
def countdown():
    global timeleft
    if timeleft > 120:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)

# Tạo cửa sổ GUI
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x200")

# Hướng dẫn
instructions = tkinter.Label(root, text="Type in the colour of the words, not the word text!",
                             font=('Helvetica', 12))
instructions.pack()

# Label điểm
scoreLabel = tkinter.Label(root, text="Press Enter to start", font=('Helvetica', 12))
scoreLabel.pack()

# Label thời gian
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

# Label hiển thị màu
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# Entry để gõ màu
e = tkinter.Entry(root)
e.pack()
e.focus_set()

# Bắt sự kiện Enter
root.bind('<Return>', startGame)

# Chạy GUI
root.mainloop()
