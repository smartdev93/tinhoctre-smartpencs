import sys
from bisect import bisect_left


def max_win(earth, xs, ys):
    # earth: danh sách (a, b) đã sắp tăng theo a. xs, ys: các VĐV hành tinh Z được cử.
    n = len(xs)
    sy = sorted(ys)
    # Hạng của từng y (1..n, các y bằng nhau vẫn có hạng riêng)
    order = sorted(range(n), key=ys.__getitem__)
    rank = [0] * n
    for r, j in enumerate(order, 1):
        rank[j] = r
    zx = sorted(range(n), key=xs.__getitem__)
    tree = [0] * (n + 1)  # cây Fenwick đếm VĐV Z "đã mở" theo hạng y
    top = 1
    while top * 2 <= n:
        top *= 2
    ptr = 0
    win = 0
    for a, b in earth:
        # Mở mọi VĐV Z có x < a (VĐV Trái đất sau có a lớn hơn nên cũng thắng được về thể lực)
        while ptr < n and xs[zx[ptr]] < a:
            r = rank[zx[ptr]]
            while r <= n:
                tree[r] += 1
                r += r & -r
            ptr += 1
        # Số VĐV Z đã mở có y < b
        lim = bisect_left(sy, b)
        cnt = 0
        r = lim
        while r > 0:
            cnt += tree[r]
            r -= r & -r
        if cnt == 0:
            continue
        # Tìm VĐV thứ cnt (y lớn nhất mà vẫn < b) rồi xóa
        pos = 0
        step = top
        rem = cnt
        while step:
            if pos + step <= n and tree[pos + step] < rem:
                pos += step
                rem -= tree[pos]
            step //= 2
        r = pos + 1
        while r <= n:
            tree[r] -= 1
            r += r & -r
        win += 1
    return win


def solve_badmi(data):
    t = list(map(int, data.split()))
    n, m, q = t[0], t[1], t[2]
    p = 3
    a = t[p:p + n]; p += n
    b = t[p:p + n]; p += n
    x = t[p:p + m]; p += m
    y = t[p:p + m]; p += m
    ks = t[p:p + q]
    earth = sorted(zip(a, b))
    out = []
    for k in ks:
        out.append(str(max_win(earth, x[k - 1:k - 1 + n], y[k - 1:k - 1 + n])))
    return "\n".join(out)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_badmi(data) + "\n")
    except FileNotFoundError:
        print(solve_badmi(sys.stdin.read()))
