print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
n = 1_000_000
prime = [True] * n
prime[0] = prime[1] = False

for i in range(2, int(n**0.5) + 1):
    if prime[i]:
        for j in range(i*i, n, 1):
            prime[j] = False

P = tuple(i for i in range(n) if prime[i])
print("Tuple P đã tạo xong!")
print("Số lượng số nguyên tố:",
len(P))
