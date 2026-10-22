import sys


def solve_mauchu(data):
    k = int(data.split()[0])
    chu = "TINHOCTRETHANHKHE"  # 17 chữ cái, không tính dấu cách
    mau = ["Blue", "Red", "White", "Yellow"]
    # Chữ thứ k lặp lại theo chu kỳ 17, màu lặp lại theo chu kỳ 4
    ki_tu = chu[(k - 1) % len(chu)]
    mau_chu = mau[(k - 1) % len(mau)]
    return ki_tu + "-" + mau_chu


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_mauchu(data) + "\n")
    except FileNotFoundError:
        print(solve_mauchu(sys.stdin.read()))
