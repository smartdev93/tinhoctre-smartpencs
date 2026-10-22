#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

const long long MOD = 1000000007LL;

long long power(long long a, long long e) {
    long long r = 1;
    a %= MOD;
    while (e > 0) {
        if (e & 1) r = r * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return r;
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
    int m, t;
    cin >> m >> t;
    // Đánh dấu các số áo bị cấm đứng yên bằng mảng hiệu
    vector<int> diff(m + 2, 0);
    for (int s = 0; s < t; s++) {
        int l, r;
        cin >> l >> r;
        diff[l]++;
        diff[r + 1]--;
    }
    int u = 0, cur = 0;
    for (int i = 1; i <= m; i++) {
        cur += diff[i];
        if (cur > 0) u++;
    }
    // Bao hàm - loại trừ: sum (-1)^j * C(u, j) * (m - j)!
    vector<long long> fact(m + 1, 1), inv(m + 1, 1);
    for (int i = 1; i <= m; i++) fact[i] = fact[i - 1] * i % MOD;
    inv[m] = power(fact[m], MOD - 2);
    for (int i = m; i > 0; i--) inv[i - 1] = inv[i] * i % MOD;
    long long ans = 0;
    for (int j = 0; j <= u; j++) {
        long long term = fact[u] * inv[j] % MOD * inv[u - j] % MOD * fact[m - j] % MOD;
        if (j % 2) ans = (ans - term + MOD) % MOD;
        else ans = (ans + term) % MOD;
    }
    cout << ans << "\n";
    return 0;
}
