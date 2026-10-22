import sys

MOD = 10**9 + 7


def solve_permu(data):
    t = list(map(int, data.split()))
    m, tt = t[0], t[1]
    # Đánh dấu các số áo bị cấm đứng yên bằng mảng hiệu
    diff = [0] * (m + 2)
    for s in range(tt):
        l, r = t[2 + 2 * s], t[3 + 2 * s]
        diff[l] += 1
        diff[r + 1] -= 1
    u = 0
    cur = 0
    for i in range(1, m + 1):
        cur += diff[i]
        if cur > 0:
            u += 1
    # Bao hàm - loại trừ: sum (-1)^j * C(u, j) * (m - j)!
    fact = [1] * (m + 1)
    for i in range(1, m + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv = [1] * (m + 1)
    inv[m] = pow(fact[m], MOD - 2, MOD)
    for i in range(m, 0, -1):
        inv[i - 1] = inv[i] * i % MOD
    ans = 0
    for j in range(u + 1):
        term = fact[u] * inv[j] % MOD * inv[u - j] % MOD * fact[m - j] % MOD
        ans = (ans - term) % MOD if j % 2 else (ans + term) % MOD
    return str(ans)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_permu(data) + "\n")
    except FileNotFoundError:
        print(solve_permu(sys.stdin.read()))
