print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
import tkinter as tk
from tkinter import messagebox

def show_selection():
    # Lấy giá trị được chọn
    choice = var.get()
    messagebox.showinfo("Thông tin chọn", f"Bạn đã chọn số: {choice}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Radio Button Example")
root.geometry("300x200")

tk.Label(root, text="Chọn một số:", font=("Helvetica", 14)).pack(pady=10)

# Biến lưu trữ giá trị radio button
var = tk.IntVar()
var.set(1)  # Giá trị mặc định

# Tạo radio button
tk.Radiobutton(root, text="1", variable=var, value=1).pack(anchor="w", padx=50)
tk.Radiobutton(root, text="2", variable=var, value=2).pack(anchor="w", padx=50)
tk.Radiobutton(root, text="3", variable=var, value=3).pack(anchor="w", padx=50)

# Nút Click Me
tk.Button(root, text="Click Me", command=show_selection).pack(pady=20)

root.mainloop()
