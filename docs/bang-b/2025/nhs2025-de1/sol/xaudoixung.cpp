#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve_xau_doi_xung(const string &s) {
    int n = s.size();
    if (n == 0) return 0;

    // dp[j] ứng với DP[i][j]: số ký tự ít nhất cần chèn vào S[i..j].
    // Duyệt i từ cuối lên, chỉ giữ một hàng -> bộ nhớ O(N).
    vector<int> dp(n, 0);
    for (int i = n - 2; i >= 0; i--) {
        int prev = 0;  // DP[i+1][j-1] với j = i+1 (đoạn rỗng)
        for (int j = i + 1; j < n; j++) {
            int tmp = dp[j];  // DP[i+1][j]
            if (s[i] == s[j])
                dp[j] = prev;
            else
                dp[j] = 1 + min(dp[j], dp[j - 1]);  // min(DP[i+1][j], DP[i][j-1])
            prev = tmp;
        }
    }
    return dp[n - 1];
}

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    string s;
    cin >> s;
    cout << solve_xau_doi_xung(s) << "\n";
    return 0;
}
