import sys
from collections import deque


def solve_tasks(data):
    tokens = data.split()
    n, m = int(tokens[0]), int(tokens[1])
    c = sorted(int(x) for x in tokens[2:2 + n])
    g = [c[i + 1] - c[i] for i in range(n - 1)]  # chênh lệch hai bài liền kề

    if m < n:
        # Giữ m bài liên tiếp (sau sắp xếp) là tối ưu -> cửa sổ m-1 khoảng liền kề.
        # Lấy min của max trên mọi cửa sổ bằng deque (max trượt).
        w = m - 1
        dq = deque()
        best = None
        for i in range(n - 1):
            while dq and g[dq[-1]] <= g[i]:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - w:
                dq.popleft()
            if i >= w - 1:
                if best is None or g[dq[0]] < best:
                    best = g[dq[0]]
        return str(best)

    # m > n: thêm k bài. Khoảng g cần ceil(g/d) - 1 bài chen vào để mọi khoảng <= d.
    # Bài thừa đặt trùng độ khó đã có (chênh lệch 0) nên không ảnh hưởng.
    k = m - n
    mx = max(g)
    if mx == 0:
        return "0"
    lo, hi = 1, mx
    while lo < hi:
        d = (lo + hi) // 2
        need = 0
        for x in g:
            if x > d:
                need += (x - 1) // d
        if need <= k:
            hi = d
        else:
            lo = d + 1
    return str(lo)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_tasks(data) + "\n")
    except FileNotFoundError:
        print(solve_tasks(sys.stdin.read()))
