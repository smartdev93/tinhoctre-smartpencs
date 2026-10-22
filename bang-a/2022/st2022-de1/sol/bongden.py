import sys


def solve_bongden(data):
    a = int(data.split()[0])
    # Chu vi bảng: 4 * a dm = 40 * a cm, cứ 5 cm một bóng
    so_bong = 40 * a // 5
    return str(so_bong)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_bongden(data) + "\n")
    except FileNotFoundError:
        print(solve_bongden(sys.stdin.read()))
