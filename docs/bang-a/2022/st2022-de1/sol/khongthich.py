import sys


def solve_khongthich(data):
    k = int(data.split()[0])
    # Trong mỗi đoạn 30 số liên tiếp có đúng 18 số Polycarp thích
    mau = []
    for x in range(1, 31):
        if x % 3 != 0 and x % 10 != 3:
            mau.append(x)
    # mau = [1, 2, 4, 5, 7, 8, 10, 11, 14, 16, 17, 19, 20, 22, 25, 26, 28, 29]
    nhom = (k - 1) // 18
    vi_tri = (k - 1) % 18
    return str(30 * nhom + mau[vi_tri])


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_khongthich(data) + "\n")
    except FileNotFoundError:
        print(solve_khongthich(sys.stdin.read()))
