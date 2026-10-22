def solve_dong_phuc():
    n = int(input().strip())
    s = input().strip()

    # Áo S cần 2 mét, M cần 3 mét, L cần 4 mét vải
    tong = 0
    for i in range(n):
        if s[i] == "S":
            tong += 2
        elif s[i] == "M":
            tong += 3
        elif s[i] == "L":
            tong += 4

    print(tong)


if __name__ == "__main__":
    solve_dong_phuc()
