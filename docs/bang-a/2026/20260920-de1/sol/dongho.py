def solve_tinh_tich():
    n = int(input().strip())
    arr = list(map(int, input().split()))

    total = sum(arr)
    prefix = 0
    ans = 0

    for i in range(n - 1):
        prefix += arr[i]
        ans = max(ans, prefix * (total - prefix))

    print(ans)


if __name__ == "__main__":
    solve_tinh_tich()
