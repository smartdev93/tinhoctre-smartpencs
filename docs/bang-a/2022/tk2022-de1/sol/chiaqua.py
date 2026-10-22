import sys


def solve_chiaqua(data):
    tokens = data.split()
    n = int(tokens[0])  # số sách đang có
    m = int(tokens[1])  # số bạn
    du = n % m
    # Nếu chia hết thì không cần mua thêm, ngược lại mua thêm m - du cuốn
    if du == 0:
        return "0"
    return str(m - du)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_chiaqua(data) + "\n")
    except FileNotFoundError:
        print(solve_chiaqua(sys.stdin.read()))
