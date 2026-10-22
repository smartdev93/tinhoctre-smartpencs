#include <cstdio>
#include <deque>
#include <iostream>
#include <vector>
using namespace std;

// Con trỏ e chạy tới vị trí đầu tiên r >= l thỏa max(a[l..r]) - min(b[l..r]) >= nguong.
// Cửa sổ [l, e) được giữ bằng hai hàng đợi đơn điệu: max của a và min của b.
struct ConTro {
    const vector<long long> &a, &b;
    long long nguong;
    int e = 0;
    deque<int> qa, qb;  // qa: a giảm dần, qb: b tăng dần

    ConTro(const vector<long long> &a_, const vector<long long> &b_, long long ng)
        : a(a_), b(b_), nguong(ng) {}

    int tim(int l) {
        int n = a.size();
        while (!qa.empty() && qa.front() < l) qa.pop_front();
        while (!qb.empty() && qb.front() < l) qb.pop_front();
        if (e < l) e = l;
        while (e < n) {
            long long ma = (qa.empty() || a[qa.front()] < a[e]) ? a[e] : a[qa.front()];
            long long mb = (qb.empty() || b[qb.front()] > b[e]) ? b[e] : b[qb.front()];
            if (ma - mb >= nguong) break;
            // Chưa thỏa: đưa e vào cửa sổ rồi xét e + 1
            while (!qa.empty() && a[qa.back()] <= a[e]) qa.pop_back();
            qa.push_back(e);
            while (!qb.empty() && b[qb.back()] >= b[e]) qb.pop_back();
            qb.push_back(e);
            e++;
        }
        return e;
    }
};

long long solve_pai(const vector<long long> &a, const vector<long long> &b) {
    int n = a.size();
    // Cố định l: f(r) = max a - min b không giảm theo r.
    // p = r đầu tiên có f >= 0, q = r đầu tiên có f > 0 -> có q - p đoạn với f = 0.
    // Khi l tăng, f giảm hoặc giữ nguyên nên p, q chỉ tăng (hai con trỏ).
    ConTro cp(a, b, 0), cq(a, b, 1);
    long long dem = 0;  // tới n(n+1)/2 ~ 5*10^9 -> long long
    for (int l = 0; l < n; l++) dem += cq.tim(l) - cp.tim(l);
    return dem;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // Có pai.inp thì đọc/ghi file, không thì dùng bàn phím/màn hình
    if (FILE *f = fopen("pai.inp", "r")) {
        fclose(f);
        freopen("pai.inp", "r", stdin);
        freopen("pai.out", "w", stdout);
    }
    int n;
    cin >> n;
    vector<long long> a(n), b(n);
    for (long long &x : a) cin >> x;
    for (long long &x : b) cin >> x;
    cout << solve_pai(a, b) << "\n";
    return 0;
}
