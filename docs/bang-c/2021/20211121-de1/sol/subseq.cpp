#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const long long MOD = 1000000007LL;

long long solve_subseq(const string &s) {
    int n = s.size();
    // Σ r(s)^2 * |s| = tổng độ dài trên mọi CẶP cách chọn (I, J) cho ra cùng một xâu con.
    // cnt: số cặp kết thúc đúng tại (i, j) với s[i] == s[j]; ln: tổng độ dài của chúng.
    // P, Q: tổng tiền tố 2 chiều của cnt, ln (chỉ số lệch 1).
    vector<vector<long long>> P(n + 1, vector<long long>(n + 1, 0)), Q = P;
    long long ans = 0;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++) {
            long long cnt = 0, ln = 0;
            if (s[j - 1] == s[i - 1]) {
                cnt = (1 + P[i - 1][j - 1]) % MOD;  // bắt đầu mới, hoặc nối dài cặp trước
                ln = (cnt + Q[i - 1][j - 1]) % MOD;  // mỗi cặp nối dài thêm 1 ký tự
                ans = (ans + ln) % MOD;
            }
            P[i][j] = ((cnt + P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1]) % MOD + MOD) % MOD;
            Q[i][j] = ((ln + Q[i - 1][j] + Q[i][j - 1] - Q[i - 1][j - 1]) % MOD + MOD) % MOD;
        }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // Có input.inp thì đọc/ghi file, không thì dùng bàn phím/màn hình
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    string s;
    cin >> s;
    cout << solve_subseq(s) << "\n";
    return 0;
}
