import sys
from math import gcd


def phan_tich(x, mu, dau):
    # Cộng (dau = +1) hoặc trừ (dau = -1) số mũ các thừa số nguyên tố của x vào mu
    d = 2
    while d * d <= x:
        while x % d == 0:
            mu[d] = mu.get(d, 0) + dau
            x //= d
        d += 1
    if x > 1:
        mu[x] = mu.get(x, 0) + dau


def solve_dtask(data):
    n, t = map(int, data.split()[:2])
    if n == 1:
        return "-1"  # mỗi thừa số (a+t)/a > 1 nên tích luôn > 1
    tmu = {}
    phan_tich(t, tmu, 1)
    mu = {}  # số mũ nguyên tố của p/q (dương: thuộc p, âm: thuộc q)

    def hai_so(p, q, amin):
        # Còn đúng 2 thừa số, a <= b: (a*u - q*t) * (b*u - q*t) = p*q*t^2 với u = p - q.
        # Duyệt ước X <= căn(N) của N = p*q*t^2, thử X ≡ -q*t (mod u).
        u = p - q
        qt = q * t
        N = p * q * t * t
        f = {}
        for pr, e in mu.items():
            if e:
                f[pr] = f.get(pr, 0) + abs(e)
        for pr, e in tmu.items():
            f[pr] = f.get(pr, 0) + 2 * e
        ds = list(f.items())

        def gen(i, X):
            if X * X > N:
                return False
            if i == len(ds):
                if (X + qt) % u == 0 and (X + qt) // u >= amin and (N // X + qt) % u == 0:
                    return True
                return False
            pr, e = ds[i]
            for _ in range(e + 1):
                if X * X > N:
                    break
                if gen(i + 1, X):
                    return True
                X *= pr
            return False

        return gen(0, 1)

    def dfs(p, q, k, amin):
        # Viết được p/q thành tích k thừa số (a+t)/a với amin <= a1 <= a2 <= ... ?
        u = p - q
        if k == 1:
            return (t * q) % u == 0 and t * q // u >= amin
        if k == 2:
            return hai_so(p, q, amin)
        # Thừa số đầu là lớn nhất: (a+t)/a < p/q và ((a+t)/a)^k >= p/q
        lo = max(amin, t * q // u + 1)
        hi = int(t / ((p / q) ** (1.0 / k) - 1)) + 2  # cộng 2 phòng sai số số thực
        for a in range(lo, hi + 1):
            np_, nq = p * a, q * (a + t)
            g = gcd(np_, nq)
            np_ //= g
            nq //= g
            if np_ <= nq:
                continue
            phan_tich(a, mu, 1)
            phan_tich(a + t, mu, -1)
            ok = dfs(np_, nq, k - 1, a)
            phan_tich(a, mu, -1)
            phan_tich(a + t, mu, 1)
            if ok:
                return True
        return False

    # Tăng dần k (iterative deepening), k đầu tiên tìm được là nhỏ nhất
    k = 1
    while True:
        mu.clear()
        phan_tich(n, mu, 1)
        if dfs(n, 1, k, 1):
            return str(k)
        k += 1


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_dtask(data) + "\n")
    except FileNotFoundError:
        print(solve_dtask(sys.stdin.read()))
