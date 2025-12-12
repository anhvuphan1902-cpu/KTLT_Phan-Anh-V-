print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
import turtle

# Tạo cửa sổ
window = turtle.Screen()
window.bgcolor("white")

# Tạo bút vẽ
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(0)

colors = ["red", "green", "blue"]

# Vẽ 12 vòng tròn xoay 30 độ
for i in range(12):
    pen.pencolor(colors[i % 3])   # đổi màu luân phiên
    pen.circle(100)               # vẽ vòng tròn bán kính 100
    pen.left(30)                  # xoay 30 độ (360/12)

window.exitonclick()
