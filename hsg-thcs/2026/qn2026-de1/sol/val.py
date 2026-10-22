import sys


def solve_val(data):
    t = list(map(int, data.split()))
    n, k = t[0], t[1]
    a = t[2:2 + n]
    dem = [0] * 4  # dem[v] = số lần giá trị v xuất hiện trong cửa sổ
    khac = 0       # số giá trị khác nhau trong cửa sổ a[l..r]
    l = 0
    best = 0
    for r in range(n):
        if dem[a[r]] == 0:
            khac += 1
        dem[a[r]] += 1
        # Thu hẹp bên trái khi cửa sổ có hơn k giá trị
        while khac > k:
            dem[a[l]] -= 1
            if dem[a[l]] == 0:
                khac -= 1
            l += 1
        if khac == k and r - l + 1 > best:
            best = r - l + 1
    return str(best)


if __name__ == "__main__":
    try:
        with open("val.inp") as f:
            data = f.read()
        with open("val.out", "w") as f:
            f.write(solve_val(data) + "\n")
    except FileNotFoundError:
        print(solve_val(sys.stdin.read()))
