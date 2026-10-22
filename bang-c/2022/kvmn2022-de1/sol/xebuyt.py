import sys


def solve_xebuyt(data):
    t = data.split()
    n, m, q, a, b = (int(v) for v in t[:5])
    p = [int(v) for v in t[5:5 + m]]
    pos = 5 + m

    # pre[i] = trạm đặc biệt gần nhất <= i, nxt[i] = trạm đặc biệt gần nhất >= i (0 nếu không có)
    special = [False] * (n + 2)
    for v in p:
        special[v] = True
    pre = [0] * (n + 2)
    for i in range(1, n + 1):
        pre[i] = i if special[i] else pre[i - 1]
    nxt = [0] * (n + 2)
    for i in range(n, 0, -1):
        nxt[i] = i if special[i] else nxt[i + 1]

    out = []
    for _ in range(q):
        x = int(t[pos])
        y = int(t[pos + 1])
        pos += 2
        best = a * abs(x - y)  # chỉ đi xe thường
        if b < a:
            # xe thường từ x tới trạm đặc biệt s, xe nhanh s -> u, xe thường u -> y;
            # s chỉ cần thử 2 trạm đặc biệt kề x, u chỉ cần thử 2 trạm kề y
            for s in (pre[x], nxt[x]):
                if s == 0:
                    continue
                cs = a * abs(x - s)
                for u in (pre[y], nxt[y]):
                    if u == 0:
                        continue
                    c = cs + b * abs(s - u) + a * abs(u - y)
                    if c < best:
                        best = c
        out.append(best)
    return "\n".join(map(str, out))


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_xebuyt(data) + "\n")
    except FileNotFoundError:
        print(solve_xebuyt(sys.stdin.read()))
