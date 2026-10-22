#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

const int FULL = (1 << 11) - 1;  // chỉ cần biết các tổng con từ 0 đến 10

// Mỗi đoạn đang mở mã hóa thành một số: tổng * 2048 + mask tổng con
typedef vector<int> State;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // Có input.inp thì đọc/ghi file, không thì dùng bàn phím/màn hình
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    int n, k, m;
    long long d;
    cin >> n >> k >> m >> d;
    set<int> starts;
    for (int i = 0; i < m; i++) {
        int p;
        cin >> p;
        starts.insert(p);
    }
    map<State, long long> dp;
    dp[State()] = 1 % d;
    for (int i = 1; i <= n; i++) {
        if (starts.count(i)) {
            // Mở đoạn mới: tổng 0, mask chỉ có bit 0
            map<State, long long> t;
            for (auto &e : dp) {
                State st = e.first;
                st.push_back(1);
                t[st] = e.second;
            }
            dp.swap(t);
        }
        if (dp.size() == 1 && dp.begin()->first.empty()) {
            // Không có đoạn nào phủ vị trí i: chữ số tự do
            dp.begin()->second = dp.begin()->second * k % d;
            continue;
        }
        map<State, long long> ndp;
        for (auto &e : dp) {
            for (int x = 1; x <= k; x++) {
                State ns;
                bool ok = true;
                for (int code : e.first) {
                    int s = code >> 11, msk = code & FULL;
                    s += x;
                    if (s > 20) {
                        ok = false;
                        break;
                    }
                    msk = (msk | (msk << x)) & FULL;
                    ns.push_back(s << 11 | msk);
                }
                if (!ok) continue;
                long long &v = ndp[ns];
                v = (v + e.second) % d;
            }
        }
        if (starts.count(i - 9)) {
            // Đoạn mở sớm nhất kết thúc tại i: phải có tổng 20 và chia được thành 10 + 10
            dp.clear();
            for (auto &e : ndp) {
                int code = e.first[0];
                int s = code >> 11, msk = code & FULL;
                if (s == 20 && (msk >> 10 & 1)) {
                    State rest(e.first.begin() + 1, e.first.end());
                    long long &v = dp[rest];
                    v = (v + e.second) % d;
                }
            }
        } else {
            dp.swap(ndp);
        }
    }
    long long ans = 0;
    for (auto &e : dp) ans = (ans + e.second) % d;
    cout << ans << "\n";
    return 0;
}
