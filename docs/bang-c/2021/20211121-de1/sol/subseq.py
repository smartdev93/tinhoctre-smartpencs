import sys

MOD = 10**9 + 7


def solve_subseq(data):
    s = data.split()[0] if data.split() else ""
    n = len(s)
    # Σ r(s)^2 * |s| = tổng độ dài trên mọi CẶP cách chọn (I, J) cho ra cùng một xâu con.
    # cnt[i][j]: số cặp kết thúc đúng tại (i, j) với s[i] == s[j]; ln[i][j]: tổng độ dài của chúng.
    # P, Q: tổng tiền tố 2 chiều của cnt, ln (chỉ số lệch 1).
    P = [[0] * (n + 1) for _ in range(n + 1)]
    Q = [[0] * (n + 1) for _ in range(n + 1)]
    ans = 0
    for i in range(1, n + 1):
        Pi, Pp, Qi, Qp = P[i], P[i - 1], Q[i], Q[i - 1]
        ci = s[i - 1]
        for j in range(1, n + 1):
            cnt = ln = 0
            if s[j - 1] == ci:
                prev_c = Pp[j - 1]  # tổng cnt của các cặp (i', j') với i' < i, j' < j
                cnt = (1 + prev_c) % MOD  # bắt đầu mới, hoặc nối dài một cặp trước đó
                ln = (cnt + Qp[j - 1]) % MOD  # mỗi cặp nối dài thêm 1 ký tự
                ans += ln
            Pi[j] = (cnt + Pp[j] + Pi[j - 1] - Pp[j - 1]) % MOD
            Qi[j] = (ln + Qp[j] + Qi[j - 1] - Qp[j - 1]) % MOD
    return str(ans % MOD)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_subseq(data) + "\n")
    except FileNotFoundError:
        print(solve_subseq(sys.stdin.read()))
