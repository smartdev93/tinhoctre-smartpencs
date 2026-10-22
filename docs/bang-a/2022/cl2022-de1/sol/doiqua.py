def doi_qua():
    k = int(input().strip())

    # Cộng dần 1 + 2 + 3 + ... cho tới khi tổng đạt ít nhất k điểm
    n = 1
    tong = 1
    while tong < k:
        n = n + 1
        tong = tong + n

    print(n)
    print(tong)


if __name__ == "__main__":
    doi_qua()
