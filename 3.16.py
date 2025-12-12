print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
s = input("Nhập các số nhị phân, cách nhau bởi dấu phẩy: ")
ds = s.split(',')
for b in ds:
    print(int(b, 2))  # chuyển từ nhị phân sang thập phân
