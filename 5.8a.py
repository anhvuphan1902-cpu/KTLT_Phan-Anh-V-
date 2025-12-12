print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Thông tin cá nhân")
root.geometry("400x250")

# Tiêu đề
tk.Label(root, text="Thông tin cá nhân", font=("Helvetica", 16, "bold")).pack(pady=10)

# Thông tin cá nhân
tk.Label(root, text="Họ tên: Phan Anh Vũ", font=("Helvetica", 12)).pack(anchor="w", padx=20)
tk.Label(root, text="Ngày sinh: 19/02/2004", font=("Helvetica", 12)).pack(anchor="w", padx=20)
tk.Label(root, text="MSSV:245751030310014", font=("Helvetica", 12)).pack(anchor="w", padx=20)
tk.Label(root, text="Ngành học: Công nghệ Kỹ thuật Điều khiển và Tự động hóa", font=("Helvetica", 12)).pack(anchor="w", padx=20)

root.mainloop()
