print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
# Nhập chuỗi từ bàn phím
s = input("Nhập chuỗi: ")

# Loại bỏ tất cả các chữ số
ket_qua = ''.join(ch for ch in s if not ch.isdigit())

# In chuỗi mới
print("Chuỗi sau khi loại bỏ chữ số là:")
print(ket_qua)
