def tong_vong_lap(n):
    # Cách làm giống trên Scratch: duyệt từ 1 đến N
    tong = 0
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            tong = tong + i
    return tong


def tong_cong_thuc(n):
    # Chia hết cho cả 3 và 5 <=> chia hết cho 15: 15, 30, ..., 15k
    k = n // 15
    return 15 * k * (k + 1) // 2


if __name__ == "__main__":
    n = int(input().strip())
    print(tong_cong_thuc(n))
