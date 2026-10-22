import sys
from math import cos, sin, pi

EPS = 1e-9


def solve_cutcake(data):
    tokens = data.split()
    n, m = int(tokens[0]), int(tokens[1])
    # Gom các đường cắt khác nhau; bỏ cạnh của đa giác (hai đỉnh kề nhau không cắt gì)
    seen = set()
    chords = []
    for k in range(m):
        i, j = int(tokens[2 + 2 * k]) - 1, int(tokens[3 + 2 * k]) - 1
        if i > j:
            i, j = j, i
        if (i, j) in seen or j - i == 1 or j - i == n - 1:
            continue
        seen.add((i, j))
        chords.append((i, j))
    xs = [cos(2 * pi * v / n) for v in range(n)]
    ys = [sin(2 * pi * v / n) for v in range(n)]

    # Thêm lần lượt từng đường cắt: số miếng tăng 1 + (số điểm PHÂN BIỆT
    # bên trong bánh mà nó cắt các đường trước đó).
    pieces = 1
    for idx, (i, j) in enumerate(chords):
        x1, y1 = xs[i], ys[i]
        dx, dy = xs[j] - x1, ys[j] - y1
        ts = []
        for (a, b) in chords[:idx]:
            # Hai dây cung cắt nhau bên trong <=> đầu mút xen kẽ nhau
            if (i < a < j) == (i < b < j) or a in (i, j) or b in (i, j):
                continue
            ex, ey = xs[b] - xs[a], ys[b] - ys[a]
            den = dx * ey - dy * ex
            tt = ((xs[a] - x1) * ey - (ys[a] - y1) * ex) / den  # vị trí giao điểm trên dây (i, j)
            ts.append(tt)
        ts.sort()
        distinct = 0
        last = -1.0
        for tt in ts:
            if tt - last > EPS:
                distinct += 1
                last = tt
        pieces += 1 + distinct
    return str(pieces)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_cutcake(data) + "\n")
    except FileNotFoundError:
        print(solve_cutcake(sys.stdin.read()))
