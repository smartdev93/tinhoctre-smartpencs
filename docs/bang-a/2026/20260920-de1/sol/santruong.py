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


if __name__ == "__main__":
    solve_chuoi_lap_deu()
