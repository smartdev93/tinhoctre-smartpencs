def solve_tang_sua():
    n = int(input().strip())

    # Thùng rẻ nhất (285/48 nghìn mỗi hộp) nên mua gần tối đa số thùng.
    # Để chắc chắn, thử bớt 0..5 thùng; với tiền còn lại thử mọi số lốc,
    # phần dư mua lẻ.
    max_thung = n // 285
    ans = 0
    thung = max_thung
    while thung >= 0 and thung >= max_thung - 5:
        con_lai = n - thung * 285
        loc = 0
        while loc * 25 <= con_lai:
            le = (con_lai - loc * 25) // 7
            hop = thung * 48 + loc * 4 + le
            if hop > ans:
                ans = hop
            loc += 1
        thung -= 1

    print(ans)


if __name__ == "__main__":
    solve_tang_sua()
