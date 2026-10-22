import sys

DONG_CHU = "HOITHITINHOCTRECAPTHANHPHO"


def solve_bai2(data):
    tokens = data.split()
    n = int(tokens[0])
    ch = tokens[1]
    L = len(DONG_CHU)  # 26 ký tự
    # Đếm ch trong một lần lặp của dòng chữ
    dem_mot_lan = 0
    for c in DONG_CHU:
        if c == ch:
            dem_mot_lan += 1
    # n ký tự = (n // L) lần lặp đầy đủ + (n % L) ký tự đầu của lần tiếp theo
    ans = (n // L) * dem_mot_lan
    for i in range(n % L):
        if DONG_CHU[i] == ch:
            ans += 1
    return str(ans)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_bai2(data) + "\n")
    except FileNotFoundError:
        print(solve_bai2(sys.stdin.read()))
