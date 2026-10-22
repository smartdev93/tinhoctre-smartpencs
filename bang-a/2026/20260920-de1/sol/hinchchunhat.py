def solve_tang_banh():
    n = int(input().strip())

    # Hộp lớn rẻ nhất (7 nghìn/cái) nên mua tối đa hộp lớn,
    # phần tiền dư (< 210) thử từng số hộp nhỏ, còn lại mua lẻ.
    box_large = n // 210
    remaining = n - box_large * 210
    ans = 0

    for box_small in range(remaining // 38 + 1):
        left = remaining - box_small * 38
        cakes = box_large * 30 + box_small * 5 + left // 9
        if cakes > ans:
            ans = cakes

    print(ans)


if __name__ == "__main__":
    solve_tang_banh()
