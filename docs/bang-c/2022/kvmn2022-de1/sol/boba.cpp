#include <algorithm>
#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // Có input.inp thì đọc/ghi file, không thì dùng bàn phím/màn hình
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    long long a1, b1, a2, b2, a3, b3;
    cin >> a1 >> b1 >> a2 >> b2 >> a3 >> b3;
    // Kết quả tới khoảng 10^18 -> long long (vẫn dưới 9.2 * 10^18)
    long long ans = 0;

    // x = 0 thì z = 0: cần a3 = 0, khi đó mọi y trong [a2, b2] đều được
    if (a1 == 0) {
        if (a3 == 0 && a2 <= b2) ans += b2 - a2 + 1;
        a1 = 1;
    }

    // x >= 1: y thuộc [max(a2, ceil(a3/x)), min(b2, b3 / x)]
    // Chia x thành các khối mà b3 / x và ceil(a3/x) không đổi
    long long x = a1;
    while (x <= b1) {
        long long f = b3 / x;
        long long end = b1;
        if (f > 0) end = min(end, b3 / f);
        long long c = 0;
        if (a3 > 0) {
            long long g = (a3 - 1) / x;  // ceil(a3/x) = g + 1
            c = g + 1;
            if (g > 0) end = min(end, (a3 - 1) / g);
        }
        long long lo = max(a2, c), hi = min(b2, f);
        if (hi >= lo) ans += (hi - lo + 1) * (end - x + 1);
        x = end + 1;
    }
    cout << ans << "\n";
    return 0;
}
