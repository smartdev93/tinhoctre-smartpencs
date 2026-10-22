import sys
from collections import deque


class ConTro:
    """Con trỏ e chạy tới vị trí đầu tiên r >= l thỏa max(a[l..r]) - min(b[l..r]) >= nguong.

    Cửa sổ [l, e) được giữ bằng hai hàng đợi đơn điệu: max của a và min của b.
    """

    def __init__(self, a, b, nguong):
        self.a, self.b, self.nguong = a, b, nguong
        self.e = 0
        self.qa = deque()  # chỉ số, a giảm dần
        self.qb = deque()  # chỉ số, b tăng dần

    def tim(self, l):
        a, b, qa, qb = self.a, self.b, self.qa, self.qb
        n = len(a)
        while qa and qa[0] < l:
            qa.popleft()
        while qb and qb[0] < l:
            qb.popleft()
        if self.e < l:
            self.e = l
        e = self.e
        while e < n:
            ma = a[e] if not qa or a[qa[0]] < a[e] else a[qa[0]]
            mb = b[e] if not qb or b[qb[0]] > b[e] else b[qb[0]]
            if ma - mb >= self.nguong:
                break
            # Chưa thỏa: đưa e vào cửa sổ rồi xét e + 1
            while qa and a[qa[-1]] <= a[e]:
                qa.pop()
            qa.append(e)
            while qb and b[qb[-1]] >= b[e]:
                qb.pop()
            qb.append(e)
            e += 1
        self.e = e
        return e


def solve_pai(data):
    t = list(map(int, data.split()))
    n = t[0]
    a = t[1:1 + n]
    b = t[1 + n:1 + 2 * n]
    # Cố định l: f(r) = max a - min b không giảm theo r.
    # p = r đầu tiên có f >= 0, q = r đầu tiên có f > 0 -> có q - p đoạn với f = 0.
    # Khi l tăng, f giảm hoặc giữ nguyên nên p, q chỉ tăng (hai con trỏ).
    cp = ConTro(a, b, 0)
    cq = ConTro(a, b, 1)
    dem = 0
    for l in range(n):
        dem += cq.tim(l) - cp.tim(l)
    return str(dem)


if __name__ == "__main__":
    try:
        with open("pai.inp") as f:
            data = f.read()
        with open("pai.out", "w") as f:
            f.write(solve_pai(data) + "\n")
    except FileNotFoundError:
        print(solve_pai(sys.stdin.read()))
