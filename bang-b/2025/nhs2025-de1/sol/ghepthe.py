import sys
from functools import cmp_to_key


def so_sanh(a, b):
    # a đứng trước b nếu a + b tạo số lớn hơn b + a
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0


def solve_ghep_the(data):
    tokens = data.split()
    n = int(tokens[0])
    the = tokens[1 : n + 1]

    the.sort(key=cmp_to_key(so_sanh))
    ket_qua = "".join(the)

    # Mọi thẻ đều là 0 -> in "0" thay vì "000..."
    return "0" if ket_qua[0] == "0" else ket_qua


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_ghep_the(data) + "\n")
    except FileNotFoundError:
        print(solve_ghep_the(sys.stdin.read()))
