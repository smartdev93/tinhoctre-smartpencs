import sys


def solve_xau_doi_xung(data):
    s = data.split()[0]
    n = len(s)

    # dp[j] ứng với DP[i][j]: số ký tự ít nhất cần chèn vào S[i..j].
    # Duyệt i từ cuối lên, chỉ giữ một hàng -> bộ nhớ O(N).
    dp = [0] * n
    for i in range(n - 2, -1, -1):
        prev = 0  # DP[i+1][j-1] với j = i+1 (đoạn rỗng)
        for j in range(i + 1, n):
            tmp = dp[j]  # DP[i+1][j]
            if s[i] == s[j]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(dp[j], dp[j - 1])  # min(DP[i+1][j], DP[i][j-1])
            prev = tmp

    return dp[n - 1] if n > 0 else 0


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(str(solve_xau_doi_xung(data)) + "\n")
    except FileNotFoundError:
        print(solve_xau_doi_xung(sys.stdin.read()))
