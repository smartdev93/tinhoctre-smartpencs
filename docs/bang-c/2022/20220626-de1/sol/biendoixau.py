import sys

B = 64                    # kích thước một khối ký tự (lá của cây phân đoạn)
ID = bytes(range(256))    # bảng dịch đồng nhất: không đổi ký tự nào


def solve_biendoixau(data):
    tokens = data.split()
    s = bytearray(tokens[0].encode())
    n = len(s)
    m = int(tokens[1])
    nb = (n + B - 1) // B
    size, log = 1, 0
    while size < nb:
        size *= 2
        log += 1
    # tag[k] = bảng dịch 256 byte "ký tự gốc -> ký tự hiện tại" chưa đẩy xuống của nút k
    tag = [ID] * (2 * size)

    def push(k):
        t = tag[k]
        if t is not ID:
            # thao tác ở nút cha mới hơn thao tác đang chờ ở nút con -> áp sau
            tag[2 * k] = tag[2 * k].translate(t)
            tag[2 * k + 1] = tag[2 * k + 1].translate(t)
            tag[k] = ID

    def materialize(blk):
        # đẩy hết thao tác đang chờ xuống khối blk rồi áp thẳng vào xâu
        k = blk + size
        for h in range(log, 0, -1):
            push(k >> h)
        t = tag[k]
        if t is not ID:
            a = blk * B
            b = min(a + B, n)
            s[a:b] = s[a:b].translate(t)
            tag[k] = ID

    tables = {}
    pos = 2
    for _ in range(m):
        i, j = int(tokens[pos]), int(tokens[pos + 1])
        c1, c2 = tokens[pos + 2], tokens[pos + 3]
        pos += 4
        g = tables.get((c1, c2))
        if g is None:
            tb = bytearray(ID)
            tb[ord(c1)] = ord(c2)
            g = tables[(c1, c2)] = bytes(tb)
        bi, bj = i // B, j // B
        if bi == bj:
            materialize(bi)
            s[i:j + 1] = s[i:j + 1].translate(g)
            continue
        lo, hi = bi, bj
        if i != bi * B:                      # khối trái chỉ phủ một phần
            materialize(bi)
            s[i:(bi + 1) * B] = s[i:(bi + 1) * B].translate(g)
            lo = bi + 1
        if j + 1 != min((bj + 1) * B, n):    # khối phải chỉ phủ một phần
            materialize(bj)
            s[bj * B:j + 1] = s[bj * B:j + 1].translate(g)
            hi = bj - 1
        if lo > hi:
            continue
        # gán thao tác cho các khối nguyên [lo, hi] (cây phân đoạn lười, kiểu từ dưới lên)
        l, r = lo + size, hi + 1 + size
        for h in range(log, 0, -1):
            if ((l >> h) << h) != l:
                push(l >> h)
            if ((r >> h) << h) != r:
                push((r - 1) >> h)
        while l < r:
            if l & 1:
                tag[l] = tag[l].translate(g)
                l += 1
            if r & 1:
                r -= 1
                tag[r] = tag[r].translate(g)
            l >>= 1
            r >>= 1
    # đẩy mọi thao tác xuống lá rồi áp vào từng khối
    for k in range(1, size):
        push(k)
    for blk in range(nb):
        t = tag[blk + size]
        if t is not ID:
            a = blk * B
            b = min(a + B, n)
            s[a:b] = s[a:b].translate(t)
    return s.decode()


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_biendoixau(data) + "\n")
    except FileNotFoundError:
        print(solve_biendoixau(sys.stdin.read()))
