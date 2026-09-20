def solve_tang_banh():
    n = int(input().strip())
    ans = 0

    for box_large in range(n // 210 + 1):
        remaining = n - box_large * 210
        for box_small in range(remaining // 38 + 1):
            left = remaining - box_small * 38
            cakes = box_large * 30 + box_small * 5 + left // 9
            if cakes > ans:
                ans = cakes

    print(ans)


if __name__ == "__main__":
    solve_tang_banh()
