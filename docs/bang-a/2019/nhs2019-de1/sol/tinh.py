import sys


def solve_tinh(data):
    # Thử mọi số có hai chữ số x = 10..99
    # Viết thêm chữ số 9 vào bên trái x được số 900 + x
    ket_qua = []
    for x in range(10, 100):
        if 900 + x == 16 * x:
            ket_qua.append(str(x))
    return " ".join(ket_qua)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_tinh(data) + "\n")
    except FileNotFoundError:
        print(solve_tinh(""))
