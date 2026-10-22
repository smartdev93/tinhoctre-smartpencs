import sys


def solve_tong3k(data):
    k = int(data.split()[0])
    # Số hạng thứ i của dãy 11, 14, 17, ... là 11 + 3*(i - 1) = 3*i + 8
    a = 3 * k + 8
    # Tổng ba số hạng liên tiếp a, a + 3, a + 6
    tong = a + (a + 3) + (a + 6)
    return str(tong)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_tong3k(data) + "\n")
    except FileNotFoundError:
        print(solve_tong3k(sys.stdin.read()))
