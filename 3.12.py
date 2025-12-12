print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
ds = input("Nhập list: ").split()
if '123' in ds:
    ds.remove('123')  # xoá phần tử '123' nếu có
for ch in ds:
    print(ch)
