import sys


def solve_bai3(data):
    n = int(data.split()[0])
    # Hàng n có 2n - 1 số, số cuối là n*n, số đầu là (n-1)*(n-1) + 1
    dau = (n - 1) * (n - 1) + 1
    cuoi = n * n
    so_luong = 2 * n - 1
    # Tổng dãy số liên tiếp = (số đầu + số cuối) * số lượng / 2
    s = (dau + cuoi) * so_luong // 2
    return str(s)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_bai3(data) + "\n")
    except FileNotFoundError:
        print(solve_bai3(sys.stdin.read()))
