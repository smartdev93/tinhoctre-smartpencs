import sys


def solve_socanbang(data):
    n = int(data.split()[0])
    dem = 0
    # Số cân bằng có 2L chữ số = x * (10^L + 1), với x có đúng L chữ số
    nho = 1          # 10^(L-1): số nhỏ nhất có L chữ số
    while True:
        lon = nho * 10 - 1          # số lớn nhất có L chữ số
        he_so = nho * 10 + 1        # 10^L + 1
        if nho * he_so > n:         # số cân bằng nhỏ nhất đã vượt n
            break
        x_max = min(lon, n // he_so)
        dem += x_max - nho + 1
        nho = nho * 10
    return str(dem)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_socanbang(data) + "\n")
    except FileNotFoundError:
        print(solve_socanbang(sys.stdin.read()))
