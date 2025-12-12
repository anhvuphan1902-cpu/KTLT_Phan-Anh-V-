print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
import tkinter as tk

root = tk.Tk()
root.title("Indicator Radio Buttons")
root.geometry("300x250")

# Biến lưu lựa chọn
choice = tk.StringVar()
choice.set("Python")   # mặc định

# Hàm xử lý lựa chọn
def ShowChoice():
    print("Bạn chọn:", choice.get())

# Tiêu đề
label = tk.Label(root, text="Choose your favourite programming language:")
label.pack(pady=5)

languages = ["Python", "Perl", "Java", "C++", "C#"]

# Tạo các radio button dạng indicator
for lang in languages:
    tk.Radiobutton(
        root,
        text=lang,
        indicatoron=0,
        width=20,
        padx=20,
        variable=choice,
        value=lang,
        command=ShowChoice
    ).pack(anchor=tk.W, pady=2)

root.mainloop()
