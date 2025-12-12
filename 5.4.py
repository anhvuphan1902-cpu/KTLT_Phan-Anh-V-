print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
import tkinter as tk
from tkinter import messagebox

# a) Tạo cửa sổ đồ họa
window = tk.Tk()
window.title("Demo Tkinter")
window.geometry("300x200")

# c) Phương thức xử lý sự kiện khi nhấn nút
def on_button_click():
    messagebox.showinfo("Thông báo", "Bạn vừa nhấn nút!")

# b + d) Thêm button và đổi màu nền, màu chữ
button = tk.Button(
    window,
    text="Nhấn vào đây",
    command=on_button_click,
    bg="yellow",    # màu nền
    fg="red"        # màu chữ
)
button.pack(pady=20)

# Hiển thị cửa sổ
window.mainloop()
