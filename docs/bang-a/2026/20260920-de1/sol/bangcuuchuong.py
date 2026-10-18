def solve_chia_keo():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    arr.sort()

    for i in range(1, n):
        if arr[i] - arr[i - 1] == 1:
            print(2)
            return

    print(1)


if __name__ == "__main__":
    solve_chia_keo()
