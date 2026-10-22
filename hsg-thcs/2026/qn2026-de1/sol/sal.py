import sys


def solve_sal(data):
    k, d, a, b = map(int, data.split()[:4])
    # Mỗi tuần trọn vẹn có 5 ngày thường và 2 ngày cuối tuần
    tong = (d // 7) * (5 * a + 2 * b)
    # Duyệt các ngày lẻ còn lại (tối đa 6 ngày)
    thu = k
    for _ in range(d % 7):
        tong += b if thu >= 7 else a  # 7 = thứ Bảy, 8 = Chủ Nhật
        thu = thu + 1 if thu < 8 else 2
    return str(tong)


if __name__ == "__main__":
    try:
        with open("sal.inp") as f:
            data = f.read()
        with open("sal.out", "w") as f:
            f.write(solve_sal(data) + "\n")
    except FileNotFoundError:
        print(solve_sal(sys.stdin.read()))
