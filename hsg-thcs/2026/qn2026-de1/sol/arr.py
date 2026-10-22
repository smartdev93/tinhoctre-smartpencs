import sys


def solve_arr(data):
    t = list(map(int, data.split()))
    n, b, k1, k2 = t[0], t[1], t[2], t[3]
    a = t[4:4 + n]
    k1 = min(k1, n)
    k2 = min(k2, n)
    # dp[j1][j2] = lượng giảm lớn nhất khi dùng tối đa j1 phép loại 1, j2 phép loại 2
    dp = [[0] * (k2 + 1) for _ in range(k1 + 1)]
    for i, x in enumerate(a):
        v1 = x // 2                      # chỉ loại 1
        v2 = max(x - b, 0)               # chỉ loại 2
        v12 = min(max(v1 - b, 0), v2 // 2)  # cả hai, chọn thứ tự tốt hơn
        g1, g2, g12 = x - v1, x - v2, x - v12
        # Chỉ cần các ô còn có thể dẫn tới dp[k1][k2]: j >= k - (số phần tử còn lại)
        con = n - 1 - i
        lo1, hi1 = max(0, k1 - con), min(k1, i + 1)
        lo2, hi2 = max(0, k2 - con), min(k2, i + 1)
        s = max(lo2, 1)
        # Đi j1 giảm dần để hàng dp[j1 - 1] vẫn là giá trị cũ
        for j1 in range(hi1, lo1 - 1, -1):
            cur = dp[j1]
            if j1 > 0:
                pre = dp[j1 - 1]
                # Cả đoạn được tính từ giá trị cũ rồi mới gán lại
                cur[s:hi2 + 1] = [
                    max(c, c2 + g2, p + g1, p2 + g12)
                    for c, c2, p, p2 in zip(cur[s:hi2 + 1], cur[s - 1:hi2],
                                            pre[s:hi2 + 1], pre[s - 1:hi2])
                ]
                if lo2 == 0 and pre[0] + g1 > cur[0]:
                    cur[0] = pre[0] + g1
            else:
                cur[s:hi2 + 1] = [
                    max(c, c2 + g2)
                    for c, c2 in zip(cur[s:hi2 + 1], cur[s - 1:hi2])
                ]
    return str(sum(a) - dp[k1][k2])


if __name__ == "__main__":
    try:
        with open("arr.inp") as f:
            data = f.read()
        with open("arr.out", "w") as f:
            f.write(solve_arr(data) + "\n")
    except FileNotFoundError:
        print(solve_arr(sys.stdin.read()))
