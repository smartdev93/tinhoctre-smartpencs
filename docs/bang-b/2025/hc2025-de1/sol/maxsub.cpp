#include <algorithm>
#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;

    // Kadane: cur = tổng lớn nhất của đoạn con kết thúc tại phần tử đang xét
    // Tổng tới 10^5 * 10^9 = 10^14 -> long long
    long long best = 0, cur = 0;
    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        cur = max(x, cur + x);  // nối tiếp đoạn cũ hoặc bắt đầu đoạn mới tại x
        if (i == 0 || cur > best) best = cur;
    }
    cout << best << "\n";
    return 0;
}
