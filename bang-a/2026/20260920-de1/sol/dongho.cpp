#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void solve_tinh_tich() {
    int n;
    cin >> n;
    vector<long long> arr(n);
    for (auto &x : arr) cin >> x;

    long long total = 0;
    for (long long x : arr) total += x;
    long long prefix = 0;
    long long ans = 0;  // tích tới ~2,5e15 nên phải dùng long long

    for (int i = 0; i < n - 1; i++) {
        prefix += arr[i];
        ans = max(ans, prefix * (total - prefix));
    }

    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve_tinh_tich();
    return 0;
}
