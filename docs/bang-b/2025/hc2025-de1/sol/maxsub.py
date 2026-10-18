import sys


def solve_maxsub(data):
    tokens = data.split()
    n = int(tokens[0])
    a = map(int, tokens[1:n + 1])

    # Kadane: cur = tổng lớn nhất của đoạn con kết thúc tại phần tử đang xét
    best = None
    cur = 0
    for x in a:
        cur = max(x, cur + x)  # nối tiếp đoạn cũ hoặc bắt đầu đoạn mới tại x
        if best is None or cur > best:
            best = cur
    return str(best)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_maxsub(data) + "\n")
    except FileNotFoundError:
        print(solve_maxsub(sys.stdin.read()))
