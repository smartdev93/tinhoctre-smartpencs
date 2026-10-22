import sys


def solve_boba(data):
    a1, b1, a2, b2, a3, b3 = map(int, data.split()[:6])
    ans = 0

    # x = 0 thì z = 0: cần a3 = 0, khi đó mọi y trong [a2, b2] đều được
    if a1 == 0:
        if a3 == 0 and a2 <= b2:
            ans += b2 - a2 + 1
        a1 = 1

    # x >= 1: y thuộc [max(a2, ceil(a3/x)), min(b2, b3 // x)]
    # Chia x thành các khối mà b3 // x và ceil(a3/x) không đổi (mỗi cái O(sqrt) giá trị)
    x = a1
    while x <= b1:
        f = b3 // x
        end = b1
        if f > 0:
            end = min(end, b3 // f)
        if a3 == 0:
            c = 0
        else:
            g = (a3 - 1) // x  # ceil(a3/x) = g + 1
            c = g + 1
            if g > 0:
                end = min(end, (a3 - 1) // g)
        lo = max(a2, c)
        hi = min(b2, f)
        if hi >= lo:
            ans += (hi - lo + 1) * (end - x + 1)
        x = end + 1
    return str(ans)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_boba(data) + "\n")
    except FileNotFoundError:
        print(solve_boba(sys.stdin.read()))
