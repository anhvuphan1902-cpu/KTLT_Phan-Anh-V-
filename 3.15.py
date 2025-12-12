print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
s = input("Nhập các từ tiếng Anh (cách nhau bởi khoảng trắng): ")
tu = s.split()
tu.sort()
print("Các từ theo thứ tự từ điển là:")
print(' '.join(tu))
