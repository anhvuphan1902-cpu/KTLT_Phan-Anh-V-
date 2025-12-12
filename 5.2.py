print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
import turtle
import turtle

# Tạo màn hình
screen = turtle.Screen()
screen.title("Ve mat troi bang Turtle")

# Tạo bút vẽ
pen = turtle.Turtle()
pen.pensize(3)
pen.color("orange")
pen.speed(5)

# Vẽ hình tròn (mặt trời)
pen.begin_fill()
pen.fillcolor("yellow")
pen.circle(60)   # bán kính 60px
pen.end_fill()

# Vẽ các tia mặt trời
pen.penup()
pen.goto(0, 60)
pen.pendown()

pen.color("orange")
for _ in range(12):
    pen.forward(80)
    pen.backward(80)
    pen.right(30)

turtle.done()
