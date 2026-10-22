import sys
from bisect import bisect_right


def solve_choncap(data):
    t = data.split()
    n, k, X = int(t[0]), int(t[1]), int(t[2])
    a = [int(v) for v in t[3:3 + n]]

    # P[i] = a1 + ... + ai; trọng số cặp (l, r) = P[r] - P[l-1], cần r - (l-1) >= X
    P = [0] * (n + 1)
    for i in range(n):
        P[i + 1] = P[i] + a[i]
    vals = sorted(set(P))
    rank = [bisect_right(vals, v) for v in P]  # vị trí 1..len(vals) trên cây Fenwick
    sz = len(vals)

    total = (n - X + 1) * (n - X + 2) // 2  # số cặp hợp lệ
    k = min(k, total)  # (giả định) k không vượt quá số cặp

    def count(T, need_sum):
        # Đếm số cặp có trọng số >= T (và tổng trọng số của chúng nếu need_sum)
        bc = [0] * (sz + 1)
        bs = [0] * (sz + 1)
        cnt = 0
        sm = 0
        for j in range(X, n + 1):
            # đưa P[j - X] vào cây: các i = 0..j-X là đầu trái hợp lệ cho j
            i = rank[j - X]
            v = P[j - X]
            while i <= sz:
                bc[i] += 1
                if need_sum:
                    bs[i] += v
                i += i & -i
            # các P[i] <= P[j] - T
            i = bisect_right(vals, P[j] - T)
            c = 0
            s = 0
            while i > 0:
                c += bc[i]
                if need_sum:
                    s += bs[i]
                i -= i & -i
            cnt += c
            if need_sum:
                sm += c * P[j] - s
        return cnt, sm

    # Tìm ngưỡng T lớn nhất mà số cặp có trọng số >= T vẫn >= k
    abs_sum = sum(abs(v) for v in a)  # mọi trọng số nằm trong [-abs_sum, abs_sum]
    lo = -2 * abs_sum - 1  # count(lo) = total >= k
    hi = abs_sum + 1       # count(hi) = 0 < k
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if count(mid, False)[0] >= k:
            lo = mid
        else:
            hi = mid
    T = lo
    # Lấy hết các cặp > T, phần còn thiếu đều có trọng số đúng bằng T
    c, s = count(T + 1, True)
    return str(s + (k - c) * T)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_choncap(data) + "\n")
    except FileNotFoundError:
        print(solve_choncap(sys.stdin.read()))
