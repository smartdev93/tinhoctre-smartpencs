#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int solve_arrange(vector<long long> w, long long k) {
    sort(w.begin(), w.end());
    // Hai con trỏ: kiện nặng nhất (right) luôn chiếm một thùng.
    // Nếu ghép được với kiện nhẹ nhất (left) thì cho vào chung thùng.
    int left = 0, right = (int)w.size() - 1;
    int ans = 0;
    while (left <= right) {
        if (left < right && w[left] + w[right] <= k) left++;  // tổng tới 2*10^9 -> long long
        right--;
        ans++;
    }
    return ans;
}

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long k;
    cin >> n >> k;
    vector<long long> w(n);
    for (auto &x : w) cin >> x;
    cout << solve_arrange(w, k) << "\n";
    return 0;
}
