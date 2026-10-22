import random
import sys

P = (1 << 61) - 1  # số nguyên tố Mersenne, lớn hơn mọi |A^3 - B| có thể xảy ra
ROUNDS = 2         # số lần thử Freivalds cho mỗi bộ dữ liệu


def mat_vec(m, v):
    # Nhân ma trận m (danh sách dòng) với vectơ v, lấy dư P
    return [sum(map(int.__mul__, row, v)) % P for row in m]


def solve_matran(data):
    tokens = data.split()
    t = int(tokens[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(tokens[pos])
        pos += 1
        a = []
        for _ in range(n):
            a.append(list(map(int, tokens[pos:pos + n])))
            pos += n
        b = []
        for _ in range(n):
            b.append([x % P for x in map(int, tokens[pos:pos + n])])
            pos += n
        ok = True
        for _ in range(ROUNDS):
            # Freivalds: so sánh A(A(Av)) với Bv cho vectơ ngẫu nhiên v
            v = [random.randrange(P) for _ in range(n)]
            if mat_vec(a, mat_vec(a, mat_vec(a, v))) != mat_vec(b, v):
                ok = False
                break
        out.append("YES" if ok else "NO")
    return "\n".join(out)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_matran(data) + "\n")
    except FileNotFoundError:
        print(solve_matran(sys.stdin.read()))
