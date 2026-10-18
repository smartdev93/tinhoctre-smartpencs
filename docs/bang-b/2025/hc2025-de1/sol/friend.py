import sys


def tong_uoc_thuc_su(n):
    # Tổng các ước của n, không kể chính n. Duyệt i đến căn n -> O(√n).
    if n <= 1:
        return 0
    s = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            if i * i != n:
                s += n // i  # ước đối xứng n / i
        i += 1
    return s


def solve_friend(data):
    a, b = map(int, data.split()[:2])
    # Cặp thân thiện phải gồm hai số khác nhau (6 6 là số hoàn hảo -> NO).
    # Kiểm tra A trước, chỉ tính tổng ước của B khi cần -> đỡ một lần O(√N)
    if a != b and tong_uoc_thuc_su(a) == b and tong_uoc_thuc_su(b) == a:
        return "YES"
    return "NO"


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_friend(data) + "\n")
    except FileNotFoundError:
        print(solve_friend(sys.stdin.read()))
