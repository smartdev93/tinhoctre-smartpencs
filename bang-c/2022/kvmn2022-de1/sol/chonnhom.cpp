#include <cstdint>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;
int n;
vector<vector<ll>> W;

// Vét cạn mọi tập con (n <= 20): val[mask] = val[mask bỏ bit cao nhất v] + tổng W[v][u], u thuộc phần còn lại
ll exact(vector<int> &group) {
    vector<ll> val(1u << n);
    val[0] = 0;
    vector<ll> lo(1024), hi(1024);
    for (int v = 0; v < n; v++) {
        lo[0] = hi[0] = 0;
        for (int r = 1; r < 1024; r++) {
            int b = __builtin_ctz(r);
            lo[r] = lo[r & (r - 1)] + (b < n ? W[v][b] : 0);
            hi[r] = hi[r & (r - 1)] + (b + 10 < n ? W[v][b + 10] : 0);
        }
        for (int r = 0; r < (1 << v); r++) val[(1 << v) | r] = val[r] + lo[r & 1023] + hi[r >> 10];
    }
    int best = 0;
    for (int mask = 1; mask < (1 << n); mask++)
        if (val[mask] > val[best]) best = mask;  // mask đầu tiên đạt max
    for (int i = 0; i < n; i++)
        if (best >> i & 1) group.push_back(i + 1);
    return val[best];
}

// Tìm kiếm cục bộ lặp (iterated local search), KHÔNG đảm bảo tối ưu.
// LCG 64 bit, seed cố định -> chạy lại cho cùng kết quả (và trùng bản Python)
uint64_t state = 20220101;
uint64_t rnd() {
    state = state * 6364136223846793005ULL + 1442695040888963407ULL;
    return state >> 33;
}
vector<int> ins;   // ins[v] = 1 nếu v đang được chọn
vector<ll> gain;   // gain[v] = tổng W[v][u] với u đang được chọn
ll cur = 0;        // tổng sự phối hợp của nhóm hiện tại

void flip(int v) {
    if (ins[v]) {
        cur -= gain[v];
        ins[v] = 0;
        for (int u = 0; u < n; u++) gain[u] -= W[v][u];
    } else {
        cur += gain[v];
        ins[v] = 1;
        for (int u = 0; u < n; u++) gain[u] += W[v][u];
    }
}

// Lặp: đổi trạng thái học sinh làm tăng tổng nhiều nhất, tới khi không tăng được
void climb() {
    while (true) {
        ll m = 0;
        int bv = -1;
        for (int v = 0; v < n; v++) {
            ll d = ins[v] ? -gain[v] : gain[v];
            if (bv < 0 || d > m) m = d, bv = v;
        }
        if (m <= 0) return;
        flip(bv);
    }
}

ll heuristic(vector<int> &group, int iters = 20000) {
    ins.assign(n, 0);
    gain.assign(n, 0);
    cur = 0;
    climb();
    ll best = cur;
    vector<int> bestSet = ins;
    for (int it = 0; it < iters; it++) {
        vector<int> sIns = ins;
        vector<ll> sGain = gain;
        ll sCur = cur;
        bool restart = it % 500 == 499;
        if (restart) {
            // khởi tạo lại từ một tập ngẫu nhiên
            for (int v = 0; v < n; v++)
                if ((int)(rnd() & 1) != ins[v]) flip(v);
        } else {
            // nhiễu: đổi trạng thái 1..4 học sinh ngẫu nhiên
            int cnt = 1 + rnd() % 4;
            for (int t = 0; t < cnt; t++) flip(rnd() % n);
        }
        climb();
        if (!restart && cur < sCur) ins = sIns, gain = sGain, cur = sCur;  // tệ hơn thì quay lại
        if (cur > best) best = cur, bestSet = ins;
    }
    for (int i = 0; i < n; i++)
        if (bestSet[i]) group.push_back(i + 1);
    return best;
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
    int m;
    cin >> n >> m;
    // Tổng tới m * 10^9 -> long long
    W.assign(n, vector<ll>(n, 0));
    for (int k = 0; k < m; k++) {
        int i, j;
        ll c;
        cin >> i >> j >> c;
        if (i != j) {  // (giả định) bỏ qua cặp i = j; cặp lặp lại thì cộng dồn
            W[i - 1][j - 1] += c;
            W[j - 1][i - 1] += c;
        }
    }
    vector<int> group;
    ll value = (n <= 20) ? exact(group) : heuristic(group);
    if (value <= 0) group.assign(1, 1);  // không có nhóm tổng dương: chọn 1 học sinh (tổng 0)
    cout << group.size() << "\n";
    for (size_t i = 0; i < group.size(); i++) cout << group[i] << (i + 1 < group.size() ? " " : "\n");
    return 0;
}
