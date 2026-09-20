# Python solution for De1: Bảng A - Khối Tiểu học

# -----------------------------
# 1. Tặng bánh
# -----------------------------
def solve_tang_banh():
    n = int(input().strip())
    ans = 0

    for box_large in range(n // 210 + 1):
        remaining = n - box_large * 210
        for box_small in range(remaining // 38 + 1):
            left = remaining - box_small * 38
            cakes = box_large * 30 + box_small * 5 + left // 9
            if cakes > ans:
                ans = cakes

    print(ans)


# -----------------------------
# 2. Chia kẹo
# -----------------------------
def solve_chia_keo():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    arr.sort()

    for i in range(1, n):
        if arr[i] - arr[i - 1] == 1:
            print(2)
            return
    print(1)


# -----------------------------
# 3. Chuỗi lặp đều
# -----------------------------
def solve_chuoi_lap_deu():
    k = int(input().strip())
    s = input().strip()

    if len(s) % k != 0:
        print(-1)
        return

    cnt = {}
    for ch in s:
        cnt[ch] = cnt.get(ch, 0) + 1

    base = []
    for ch in sorted(cnt):
        if cnt[ch] % k != 0:
            print(-1)
            return
        base.extend([ch] * (cnt[ch] // k))

    result = ''.join(base) * k
    print(result)


# -----------------------------
# 4. Tính tích
# -----------------------------
def solve_tinh_tich():
    n = int(input().strip())
    arr = list(map(int, input().split()))

    total = sum(arr)
    prefix = 0
    ans = 0

    for i in range(n - 1):
        prefix += arr[i]
        ans = max(ans, prefix * (total - prefix))

    print(ans)


if __name__ == "__main__":
    # Chọn bài cần chạy ở đây:
    # 1: solve_tang_banh()
    # 2: solve_chia_keo()
    # 3: solve_chuoi_lap_deu()
    # 4: solve_tinh_tich()

    solve_tang_banh()
