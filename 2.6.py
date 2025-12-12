print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
def get_sum(*num): # *num cho phép truyền nhiều đối số vào
    tmp = 0
    # duyệt các tham số
    for i in num:
        tmp +=i
    return tmp

result = get_sum(1, 2, 3, 4, 5)
print(result)

# Giải thích:
# Dấu * trước tham số (*num) cho phép bạn tryền bao nhiêu tham số cũng được vào hàm.
# Biến tmp dùng để cộng dồn
# Vòng lặp for i in num duyệt qua từng số cộng vào tmp
# Trả về tổng của tất cả số
