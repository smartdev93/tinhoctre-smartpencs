#include <algorithm>
#include <cstdio>
#include <iostream>
#include <set>
#include <utility>
#include <vector>
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
    int n, m, q;
    cin >> n >> m >> q;
    vector<pair<long long, long long>> earth(n);
    for (auto &e : earth) cin >> e.first;
    for (auto &e : earth) cin >> e.second;
    vector<long long> x(m), y(m);
    for (auto &v : x) cin >> v;
    for (auto &v : y) cin >> v;
    sort(earth.begin(), earth.end());  // tăng dần theo thể lực a
    vector<pair<long long, long long>> z(n);
    while (q--) {
        int k;
        cin >> k;
        for (int j = 0; j < n; j++) z[j] = {x[k - 1 + j], y[k - 1 + j]};
        sort(z.begin(), z.end());  // tăng dần theo x
        multiset<long long> open;  // y của các VĐV Z có x < a hiện tại, chưa bị ghép
        int ptr = 0, win = 0;
        for (auto &e : earth) {
            while (ptr < n && z[ptr].first < e.first) open.insert(z[ptr++].second);
            // Ghép với VĐV Z có y lớn nhất mà vẫn < b
            auto it = open.lower_bound(e.second);
            if (it == open.begin()) continue;
            --it;
            open.erase(it);
            win++;
        }
        cout << win << "\n";
    }
    return 0;
}
