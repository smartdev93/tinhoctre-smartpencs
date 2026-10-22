import sys


def solve_bai1(data):
    tokens = data.split()
    n = int(tokens[0])
    k = int(tokens[1])
    # Các số chia hết cho k trong [1, n]: k, 2k, ..., m*k với m = n // k
    m = n // k
    # Tổng = k * (1 + 2 + ... + m)
    s = k * m * (m + 1) // 2
    return str(s)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_bai1(data) + "\n")
    except FileNotFoundError:
        print(solve_bai1(sys.stdin.read()))
