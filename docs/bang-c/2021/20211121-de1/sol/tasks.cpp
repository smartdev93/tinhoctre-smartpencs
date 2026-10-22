#include <algorithm>
#include <cstdio>
#include <deque>
#include <iostream>
#include <vector>
using namespace std;

long long solve_tasks(int n, int m, vector<long long> c) {
    sort(c.begin(), c.end());
    vector<long long> g(n - 1);  // chênh lệch hai bài liền kề
    for (int i = 0; i + 1 < n; i++) g[i] = c[i + 1] - c[i];

    if (m < n) {
        // Giữ m bài liên tiếp (sau sắp xếp) là tối ưu -> cửa sổ m-1 khoảng liền kề.
        // Lấy min của max trên mọi cửa sổ bằng deque (max trượt).
        int w = m - 1;
        deque<int> dq;
        long long best = -1;
        for (int i = 0; i < n - 1; i++) {
            while (!dq.empty() && g[dq.back()] <= g[i]) dq.pop_back();
            dq.push_back(i);
            if (dq.front() <= i - w) dq.pop_front();
            if (i >= w - 1 && (best < 0 || g[dq.front()] < best)) best = g[dq.front()];
        }
        return best;
    }

    // m > n: thêm k bài. Khoảng g cần ceil(g/d) - 1 bài chen vào để mọi khoảng <= d.
    // Bài thừa đặt trùng độ khó đã có (chênh lệch 0) nên không ảnh hưởng.
    long long k = m - n;
    long long mx = *max_element(g.begin(), g.end());
    if (mx == 0) return 0;
    long long lo = 1, hi = mx;
    while (lo < hi) {
        long long d = (lo + hi) / 2;
        long long need = 0;
        for (long long x : g)
            if (x > d) need += (x - 1) / d;
        if (need <= k) hi = d;
        else lo = d + 1;
    }
    return lo;
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
    int n, m;
    cin >> n >> m;
    vector<long long> c(n);
    for (auto &x : c) cin >> x;
    cout << solve_tasks(n, m, c) << "\n";
    return 0;
}
