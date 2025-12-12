print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
n = int(input("Nhập số n: "))
print("Các số nguyên dương nhỏ hơn n và không nguyên tố:")
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            print(i)
            break
