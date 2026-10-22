import sys


def solve_compress(data):
    s = data.strip()
    n = len(s)
    parts = []
    i = 0
    while i < n:
        # Đếm đoạn ký tự giống nhau bắt đầu tại i
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        parts.append(str(j - i) + s[i])
        i = j
    # Nối bằng join (O(N)), rồi đảo ngược cả xâu kết quả
    return "".join(parts)[::-1]


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_compress(data) + "\n")
    except FileNotFoundError:
        print(solve_compress(sys.stdin.read()))
