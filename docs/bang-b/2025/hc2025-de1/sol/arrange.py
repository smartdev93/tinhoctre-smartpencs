import sys


def solve_arrange(data):
    tokens = data.split()
    n, k = int(tokens[0]), int(tokens[1])
    w = sorted(map(int, tokens[2:2 + n]))

    # Hai con trỏ: kiện nặng nhất (right) luôn chiếm một thùng.
    # Nếu ghép được với kiện nhẹ nhất (left) thì cho vào chung thùng.
    left, right = 0, n - 1
    ans = 0
    while left <= right:
        if left < right and w[left] + w[right] <= k:
            left += 1
        right -= 1
        ans += 1
    return str(ans)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_arrange(data) + "\n")
    except FileNotFoundError:
        print(solve_arrange(sys.stdin.read()))
