import sys

FULL = (1 << 11) - 1  # chỉ cần biết các tổng con từ 0 đến 10


def solve_pnum(data):
    t = list(map(int, data.split()))
    n, k, m, d = t[0], t[1], t[2], t[3]
    starts = set(t[4:4 + m])
    # Trạng thái: tuple (tổng, mask tổng con) của từng đoạn đang mở,
    # theo thứ tự vị trí bắt đầu. Bit j của mask = có nhóm con tổng j.
    dp = {(): 1}
    for i in range(1, n + 1):
        if i in starts:
            dp = {st + ((0, 1),): c for st, c in dp.items()}
        if () in dp and len(dp) == 1:
            # Không có đoạn nào phủ vị trí i: chữ số tự do
            dp[()] = dp[()] * k % d
            continue
        ndp = {}
        for st, c in dp.items():
            for x in range(1, k + 1):
                ns = []
                ok = True
                for s, msk in st:
                    s += x
                    if s > 20:
                        ok = False
                        break
                    ns.append((s, (msk | (msk << x)) & FULL))
                if not ok:
                    continue
                key = tuple(ns)
                ndp[key] = (ndp.get(key, 0) + c) % d
        # Đoạn mở sớm nhất kết thúc tại i (bắt đầu tại i - 9)?
        if (i - 9) in starts:
            dp = {}
            for st, c in ndp.items():
                s, msk = st[0]
                if s == 20 and msk >> 10 & 1:
                    key = st[1:]
                    dp[key] = (dp.get(key, 0) + c) % d
        else:
            dp = ndp
    return str(sum(dp.values()) % d)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_pnum(data) + "\n")
    except FileNotFoundError:
        print(solve_pnum(sys.stdin.read()))
