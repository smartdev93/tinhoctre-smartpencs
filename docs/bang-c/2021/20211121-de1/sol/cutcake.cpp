#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <set>
#include <utility>
#include <vector>
using namespace std;

const double EPS = 1e-9;

long long solve_cutcake(int n, const vector<pair<int, int>> &cuts) {
    // Gom các đường cắt khác nhau; bỏ cạnh của đa giác (hai đỉnh kề nhau không cắt gì)
    set<pair<int, int>> seen;
    vector<pair<int, int>> chords;
    for (auto c : cuts) {
        int i = c.first - 1, j = c.second - 1;
        if (i > j) swap(i, j);
        if (seen.count({i, j}) || j - i == 1 || j - i == n - 1) continue;
        seen.insert({i, j});
        chords.push_back({i, j});
    }
    const double PI = acos(-1.0);
    vector<double> xs(n), ys(n);
    for (int v = 0; v < n; v++) {
        xs[v] = cos(2 * PI * v / n);
        ys[v] = sin(2 * PI * v / n);
    }
    // Thêm lần lượt từng đường cắt: số miếng tăng 1 + (số điểm PHÂN BIỆT
    // bên trong bánh mà nó cắt các đường trước đó).
    long long pieces = 1;
    for (size_t idx = 0; idx < chords.size(); idx++) {
        int i = chords[idx].first, j = chords[idx].second;
        double x1 = xs[i], y1 = ys[i], dx = xs[j] - x1, dy = ys[j] - y1;
        vector<double> ts;
        for (size_t o = 0; o < idx; o++) {
            int a = chords[o].first, b = chords[o].second;
            // Hai dây cung cắt nhau bên trong <=> đầu mút xen kẽ nhau
            if ((i < a && a < j) == (i < b && b < j) || a == i || a == j || b == i || b == j) continue;
            double ex = xs[b] - xs[a], ey = ys[b] - ys[a];
            double den = dx * ey - dy * ex;
            ts.push_back(((xs[a] - x1) * ey - (ys[a] - y1) * ex) / den);  // vị trí giao điểm
        }
        sort(ts.begin(), ts.end());
        long long distinct = 0;
        double last = -1.0;
        for (double tt : ts)
            if (tt - last > EPS) {
                distinct++;
                last = tt;
            }
        pieces += 1 + distinct;
    }
    return pieces;
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
    vector<pair<int, int>> cuts(m);
    for (auto &c : cuts) cin >> c.first >> c.second;
    cout << solve_cutcake(n, cuts) << "\n";
    return 0;
}
