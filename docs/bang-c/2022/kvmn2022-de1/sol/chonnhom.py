import sys
from operator import add, sub

MASK64 = (1 << 64) - 1


def exact(n, W):
    # Vét cạn mọi tập con: val[mask] = val[mask bỏ bit cao nhất v] + tổng W[v][u] với u trong phần còn lại.
    # Tổng W[v][u] tra bảng theo 10 bit thấp (lo) và 10 bit cao (hi) của phần còn lại.
    val = [0]
    for v in range(n):
        lo = [0] * 1024
        hi = [0] * 1024
        for r in range(1, 1024):
            b = (r & -r).bit_length() - 1
            lo[r] = lo[r & (r - 1)] + (W[v][b] if b < n else 0)
            hi[r] = hi[r & (r - 1)] + (W[v][b + 10] if b + 10 < n else 0)
        val.extend([val[r] + lo[r & 1023] + hi[r >> 10] for r in range(1 << v)])
    best = max(range(len(val)), key=val.__getitem__)  # mask đầu tiên đạt max
    return val[best], [i + 1 for i in range(n) if best >> i & 1]


def heuristic(n, W, iters=20000):
    # Tìm kiếm cục bộ lặp (iterated local search), KHÔNG đảm bảo tối ưu.
    # Bộ sinh số ngẫu nhiên LCG 64 bit, seed cố định -> chạy lại cho cùng kết quả.
    state = [20220101]

    def rnd():
        state[0] = (state[0] * 6364136223846793005 + 1442695040888963407) & MASK64
        return state[0] >> 33

    ins = [0] * n   # ins[v] = 1 nếu v đang được chọn
    gain = [0] * n  # gain[v] = tổng W[v][u] với u đang được chọn
    cur = [0]       # tổng sự phối hợp của nhóm hiện tại

    def flip(v):
        if ins[v]:
            cur[0] -= gain[v]
            ins[v] = 0
            gain[:] = map(sub, gain, W[v])
        else:
            cur[0] += gain[v]
            ins[v] = 1
            gain[:] = map(add, gain, W[v])

    def climb():
        # Lặp: đổi trạng thái (chọn/bỏ) học sinh làm tăng tổng nhiều nhất, tới khi không tăng được
        while True:
            d = [-g if s else g for g, s in zip(gain, ins)]
            m = max(d)
            if m <= 0:
                return
            flip(d.index(m))

    climb()
    best = cur[0]
    best_set = ins[:]
    for it in range(iters):
        saved = (ins[:], gain[:], cur[0])
        restart = it % 500 == 499
        if restart:
            # khởi tạo lại từ một tập ngẫu nhiên
            for v in range(n):
                if rnd() & 1 != ins[v]:
                    flip(v)
        else:
            # nhiễu: đổi trạng thái 1..4 học sinh ngẫu nhiên
            for _ in range(1 + rnd() % 4):
                flip(rnd() % n)
        climb()
        if not restart and cur[0] < saved[2]:
            ins[:], gain[:], cur[0] = saved[0], saved[1], saved[2]  # tệ hơn thì quay lại
        if cur[0] > best:
            best = cur[0]
            best_set = ins[:]
    return best, [i + 1 for i in range(n) if best_set[i]]


def solve_chonnhom(data):
    t = data.split()
    n, m = int(t[0]), int(t[1])
    W = [[0] * n for _ in range(n)]
    for k in range(m):
        i = int(t[2 + 3 * k]) - 1
        j = int(t[3 + 3 * k]) - 1
        c = int(t[4 + 3 * k])
        if i != j:  # (giả định) bỏ qua cặp i = j; cặp lặp lại thì cộng dồn
            W[i][j] += c
            W[j][i] += c
    if n <= 20:
        value, group = exact(n, W)
    else:
        value, group = heuristic(n, W)
    if value <= 0:
        group = [1]  # không có nhóm tổng dương: chọn 1 học sinh (tổng 0)
    return str(len(group)) + "\n" + " ".join(map(str, group))


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_chonnhom(data) + "\n")
    except FileNotFoundError:
        print(solve_chonnhom(sys.stdin.read()))
