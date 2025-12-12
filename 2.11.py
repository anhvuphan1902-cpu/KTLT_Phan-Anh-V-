print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
def benefit(t, n, k):
    # t: lãi suất % mỗi tháng
    # n: số vốn ban đầu
    # k: số tháng gửi
    # Công thức tính lãi kép: A = n * (1 + t/100)^k
    return n * (1 + t/100)**k

try:
    t = float(input("Nhập lãi suất tiết kiệm (% mỗi tháng): "))
    n = float(input("Nhập số vốn ban đầu: "))
    k = int(input("Nhập số tháng gửi: "))

    tien_nhan_duoc = benefit(t, n, k)
    print(f"Số tiền nhận được sau {k} tháng là: {tien_nhan_duoc:.2f}")
except ValueError:
    print("Dữ liệu nhập không hợp lệ. Vui lòng nhập số hợp lệ.")
