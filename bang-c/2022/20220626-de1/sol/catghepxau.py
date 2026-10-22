import sys

M = (1 << 61) - 1   # mô-đun băm
BASE = 131


def prefix_hash(s):
    h = [0] * (len(s) + 1)
    for i, ch in enumerate(s):
        h[i + 1] = (h[i] * BASE + ord(ch)) % M
    return h


def greedy(s1, s2, rev, last):
    # Tham lam: lặp lại việc ghép đoạn chung DÀI NHẤT còn lại của S1 và S2.
    # rev: duyệt S2 từ phải sang; last: ưu tiên vị trí xuất hiện sau cùng ở S1.
    n = len(s1)
    h1, h2 = prefix_hash(s1), prefix_hash(s2)
    pw = [1] * (n + 1)
    for i in range(n):
        pw[i + 1] = pw[i] * BASE % M
    used1, used2 = bytearray(n), bytearray(n)
    pieces = []          # (vị trí trong S1, vị trí trong S2, độ dài)
    remain = n

    def windows(h, pu, L):
        # (băm, vị trí) của các cửa sổ độ dài L chưa dùng ký tự nào
        p = pw[L]
        return [((h[i + L] - h[i] * p) % M, i)
                for i in range(n - L + 1) if pu[i + L] == pu[i]]

    hi = n
    while remain > 0:
        pu1, pu2 = [0] * (n + 1), [0] * (n + 1)
        for i in range(n):
            pu1[i + 1] = pu1[i] + used1[i]
            pu2[i + 1] = pu2[i] + used2[i]

        def exists(L):
            st = {x for x, _ in windows(h1, pu1, L)}
            return any(x in st for x, _ in windows(h2, pu2, L))

        # tìm độ dài L lớn nhất còn đoạn chung: L chỉ giảm dần nên dò lùi
        # từ hi với bước nhân đôi, rồi chặt nhị phân trong khoảng tìm được
        L = hi
        if not exists(hi):
            bad, step = hi, 1
            while True:
                c = max(1, hi - step)
                if c == 1 or exists(c):  # độ dài 1 luôn có đoạn chung
                    break
                bad, step = c, step * 2
            lo, up = c, bad - 1
            while lo < up:
                mid = (lo + up + 1) // 2
                if exists(mid):
                    lo = mid
                else:
                    up = mid - 1
            L = lo
        # lấy mọi cặp đoạn chung độ dài L không chồng nhau
        cand = {}
        for x, i in windows(h1, pu1, L):
            cand.setdefault(x, []).append(i)
        if last:
            for lst in cand.values():
                lst.reverse()
        w2 = windows(h2, pu2, L)
        if rev:
            w2.reverse()
        for x, p in w2:
            if used2[p] or used2[p + L - 1]:
                continue  # chồng lên đoạn vừa lấy trong lượt này
            lst = cand.get(x)
            if not lst:
                continue
            k = 0
            while k < len(lst):
                a = lst[k]
                if used1[a] or used1[a + L - 1]:
                    del lst[k]  # đoạn đã bị dùng: bỏ khỏi danh sách
                    continue
                if s1[a:a + L] == s2[p:p + L]:  # kiểm tra thật, tránh trùng băm
                    used1[a:a + L] = b"\1" * L
                    used2[p:p + L] = b"\1" * L
                    pieces.append((a, p, L))
                    remain -= L
                    del lst[k]
                    break
                k += 1
        hi = max(1, L - 1)
    # gộp hai đoạn kề nhau ở S1 mà cũng kề nhau, đúng thứ tự ở S2
    pieces.sort()
    merged = [list(pieces[0])]
    for a, p, L in pieces[1:]:
        last_piece = merged[-1]
        if last_piece[1] + last_piece[2] == p:
            last_piece[2] += L
        else:
            merged.append([a, p, L])
    return merged


def solve_catghepxau(data):
    tokens = data.split()
    s1, s2 = tokens[0], tokens[1]
    if len(s1) != len(s2) or sorted(s1) != sorted(s2):
        return "-1"  # khác tập ký tự thì không thể cắt ghép
    best = None
    for rev in (0, 1):          # chạy 4 biến thể, giữ phương án ít đoạn nhất
        for last in (0, 1):
            cur = greedy(s1, s2, rev, last)
            if best is None or len(cur) < len(best):
                best = cur
    cuts = [a for a, _, _ in best[1:]]   # cắt sau ký tự thứ a (đánh số từ 1)
    order = sorted(range(len(best)), key=lambda k: best[k][1])
    return "\n".join([str(len(cuts)),
                      " ".join(map(str, cuts)),
                      " ".join(str(k + 1) for k in order)])


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_catghepxau(data) + "\n")
    except FileNotFoundError:
        print(solve_catghepxau(sys.stdin.read()))
