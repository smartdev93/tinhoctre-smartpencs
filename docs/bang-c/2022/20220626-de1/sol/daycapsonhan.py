import sys

MOD = 10**9 + 7
K = 32  # q >= 2, a_i <= 10^9 nên dãy cấp số nhân dài tối đa 30 phần tử


def solve_daycapsonhan(data):
    tokens = data.split()
    n, q = int(tokens[0]), int(tokens[1])
    a = tokens[2:2 + n]
    # cnt[v][L] = số dãy cấp số nhân độ dài L kết thúc bằng giá trị v (đã duyệt)
    cnt = {}
    total = [0] * (K + 1)
    for t in a:
        v = int(t)
        cur = [0] * (K + 1)
        cur[1] = 1
        if v % q == 0:
            prev = cnt.get(v // q)
            if prev is not None:
                # nối v vào sau các dãy kết thúc bằng v / q
                for L in range(2, K + 1):
                    cur[L] = prev[L - 1]
        own = cnt.get(v)
        if own is None:
            own = [0] * (K + 1)
            cnt[v] = own
        for L in range(1, K + 1):
            if cur[L]:
                own[L] = (own[L] + cur[L]) % MOD
                total[L] = (total[L] + cur[L]) % MOD
    res = []
    for k in range(2, n + 1):
        res.append(total[k] if k <= K else 0)
    return " ".join(map(str, res))


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_daycapsonhan(data) + "\n")
    except FileNotFoundError:
        print(solve_daycapsonhan(sys.stdin.read()))
