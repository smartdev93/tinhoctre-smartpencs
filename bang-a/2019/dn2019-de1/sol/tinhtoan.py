def solve_tinh_toan():
    n = int(input().strip())  # số hình vuông
    a = int(input().strip())  # cạnh hình vuông nhỏ nhất

    tong = 0
    canh = a
    for i in range(n):
        tong = tong + canh * canh  # cộng diện tích hình vuông thứ i+1
        canh = canh + 20           # hình sau lớn hơn hình trước 20 đơn vị

    print(tong)


if __name__ == "__main__":
    solve_tinh_toan()
