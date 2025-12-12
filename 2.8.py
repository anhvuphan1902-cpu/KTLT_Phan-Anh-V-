print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
import math

# Vị trí ban đầu tại (0, 0)
pos = [0, 0]

while True:
    s = input()  # Nhập lệnh, ví dụ: UP 5
    if not s:    # Nếu nhập dòng trống → thoát vòng lặp
        break

    movement = s.split()
    direction = movement[0]
    steps = int(movement[1])

    if direction == "UP":
        pos[1] += steps
    elif direction == "DOWN":
        pos[1] -= steps
    elif direction == "LEFT":
        pos[0] -= steps
    elif direction == "RIGHT":
        pos[0] += steps

# Tính khoảng cách từ (0, 0) đến vị trí cuối cùng
distance = int(round(math.sqrt(pos[0]**2 + pos[1]**2)))
print(distance)
