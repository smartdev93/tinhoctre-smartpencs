#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

long long solve_arr(long long b, int k1, int k2, const vector<long long> &a) {
    int n = a.size();
    k1 = min(k1, n);
    k2 = min(k2, n);
    // dp[j1][j2] = lượng giảm lớn nhất khi dùng tối đa j1 phép loại 1, j2 phép loại 2
    vector<vector<long long>> dp(k1 + 1, vector<long long>(k2 + 1, 0));
    long long tong = 0;
    for (int i = 0; i < n; i++) {
        long long x = a[i];
        tong += x;
        long long v1 = x / 2;                                  // chỉ loại 1
        long long v2 = max(x - b, 0LL);                        // chỉ loại 2
        long long v12 = min(max(v1 - b, 0LL), v2 / 2);         // cả hai, chọn thứ tự tốt hơn
        long long g1 = x - v1, g2 = x - v2, g12 = x - v12;
        // Đi ngược cả hai chiều để dp[j1-1][*] và dp[j1][j2-1] vẫn là giá trị cũ
        for (int j1 = min(k1, i + 1); j1 >= 0; j1--) {
            for (int j2 = min(k2, i + 1); j2 >= 0; j2--) {
                long long v = dp[j1][j2];
                if (j2 > 0) v = max(v, dp[j1][j2 - 1] + g2);
                if (j1 > 0) v = max(v, dp[j1 - 1][j2] + g1);
                if (j1 > 0 && j2 > 0) v = max(v, dp[j1 - 1][j2 - 1] + g12);
                dp[j1][j2] = v;
            }
        }
    }
    return tong - dp[k1][k2];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // Có arr.inp thì đọc/ghi file, không thì dùng bàn phím/màn hình
    if (FILE *f = fopen("arr.inp", "r")) {
        fclose(f);
        freopen("arr.inp", "r", stdin);
        freopen("arr.out", "w", stdout);
    }
    int n, k1, k2;
    long long b;
    cin >> n >> b >> k1 >> k2;
    vector<long long> a(n);
    for (long long &x : a) cin >> x;
    cout << solve_arr(b, k1, k2, a) << "\n";
    return 0;
}
