#include <array>
#include <cstdio>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

const long long MOD = 1000000007LL;
const int K = 32;  // q >= 2, a_i <= 10^9 nên dãy cấp số nhân dài tối đa 30 phần tử

vector<long long> solve_daycapsonhan(int n, long long q, const vector<long long> &a) {
    // cnt[v][L] = số dãy cấp số nhân độ dài L kết thúc bằng giá trị v (đã duyệt)
    unordered_map<long long, array<long long, K + 1>> cnt;
    cnt.reserve(2 * n + 1);
    array<long long, K + 1> total{};
    for (long long v : a) {
        array<long long, K + 1> cur{};
        cur[1] = 1;
        if (v % q == 0) {
            auto it = cnt.find(v / q);
            if (it != cnt.end())  // nối v vào sau các dãy kết thúc bằng v / q
                for (int L = 2; L <= K; L++) cur[L] = it->second[L - 1];
        }
        auto &own = cnt[v];  // phần tử mới được khởi tạo bằng 0
        for (int L = 1; L <= K; L++) {
            if (cur[L]) {
                own[L] = (own[L] + cur[L]) % MOD;
                total[L] = (total[L] + cur[L]) % MOD;
            }
        }
    }
    vector<long long> res;
    for (int k = 2; k <= n; k++) res.push_back(k <= K ? total[k] : 0);
    return res;
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
    int n;
    long long q;
    cin >> n >> q;
    vector<long long> a(n);
    for (auto &x : a) cin >> x;
    vector<long long> res = solve_daycapsonhan(n, q, a);
    for (size_t i = 0; i < res.size(); i++) {
        if (i) cout << ' ';
        cout << res[i];
    }
    cout << "\n";
    return 0;
}
