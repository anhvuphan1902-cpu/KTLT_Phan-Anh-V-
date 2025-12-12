print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

painter = turtle.Turtle()
painter.fillcolor('blue')
painter.pencolor('blue')
painter.pensize(3)

def drawsq(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)

for i in range(180):
    painter.left(18)   # 18 = 360 / 20 (thay đổi góc quay)
    drawsq(painter, 200)

window.exitonclick()
