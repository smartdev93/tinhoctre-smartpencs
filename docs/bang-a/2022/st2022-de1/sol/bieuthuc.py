import sys


def solve_bieuthuc(data):
    a, b, c, d = map(int, data.split()[:4])
    # x - y nhỏ nhất khi x nhỏ nhất (x = a) và y lớn nhất (y = d)
    return str(a - d)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_bieuthuc(data) + "\n")
    except FileNotFoundError:
        print(solve_bieuthuc(sys.stdin.read()))
