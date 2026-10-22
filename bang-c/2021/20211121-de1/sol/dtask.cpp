#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <utility>
#include <vector>
using namespace std;

typedef __int128 lll;  // p, q, p*q*t^2 có thể vượt long long

long long T;
map<long long, int> mu;                // số mũ nguyên tố của p/q (dương: thuộc p, âm: thuộc q)
vector<pair<long long, int>> tmu;      // phân tích t
vector<pair<long long, int>> ds;       // phân tích N = p*q*t^2
lll N, U, QT;
long long AMIN;

void phan_tich(long long x, int dau) {
    // Cộng (dau = +1) hoặc trừ (dau = -1) số mũ các thừa số nguyên tố của x vào mu
    for (long long d = 2; d * d <= x; d++)
        while (x % d == 0) {
            mu[d] += dau;
            x /= d;
        }
    if (x > 1) mu[x] += dau;
}

lll gcd128(lll a, lll b) {
    while (b) {
        lll c = a % b;
        a = b;
        b = c;
    }
    return a;
}

bool gen(size_t i, lll X) {
    if (X * X > N) return false;
    if (i == ds.size())
        return (X + QT) % U == 0 && (X + QT) / U >= AMIN && (N / X + QT) % U == 0;
    for (int e = 0; e <= ds[i].second; e++) {
        if (X * X > N) break;
        if (gen(i + 1, X)) return true;
        X *= ds[i].first;
    }
    return false;
}

bool hai_so(lll p, lll q, long long amin) {
    // Còn đúng 2 thừa số, a <= b: (a*u - q*t) * (b*u - q*t) = p*q*t^2 với u = p - q.
    // Duyệt ước X <= căn(N) của N, thử X ≡ -q*t (mod u).
    U = p - q;
    QT = q * T;
    N = p * q * T * T;
    AMIN = amin;
    map<long long, int> f;
    for (auto &x : mu)
        if (x.second) f[x.first] += abs(x.second);
    for (auto &x : tmu) f[x.first] += 2 * x.second;
    ds.assign(f.begin(), f.end());
    return gen(0, 1);
}

bool dfs(lll p, lll q, int k, long long amin) {
    // Viết được p/q thành tích k thừa số (a+t)/a với amin <= a1 <= a2 <= ... ?
    lll u = p - q;
    if (k == 1) return (T * q) % u == 0 && T * q / u >= amin;
    if (k == 2) return hai_so(p, q, amin);
    // Thừa số đầu là lớn nhất: (a+t)/a < p/q và ((a+t)/a)^k >= p/q
    long long lo = (long long)(T * q / u) + 1;
    if (lo < amin) lo = amin;
    long double r = (long double)p / (long double)q;
    long long hi = (long long)((long double)T / (powl(r, 1.0L / k) - 1)) + 2;  // +2 phòng sai số
    for (long long a = lo; a <= hi; a++) {
        lll np = p * a, nq = q * (a + T), g = gcd128(np, nq);
        np /= g;
        nq /= g;
        if (np <= nq) continue;
        phan_tich(a, 1);
        phan_tich(a + T, -1);
        bool ok = dfs(np, nq, k - 1, a);
        phan_tich(a, -1);
        phan_tich(a + T, 1);
        if (ok) return true;
    }
    return false;
}

int solve_dtask(int n, int t) {
    if (n == 1) return -1;  // mỗi thừa số (a+t)/a > 1 nên tích luôn > 1
    T = t;
    tmu.clear();
    long long x = t;
    for (long long d = 2; d * d <= x; d++) {
        int c = 0;
        while (x % d == 0) {
            c++;
            x /= d;
        }
        if (c) tmu.push_back({d, c});
    }
    if (x > 1) tmu.push_back({x, 1});
    // Tăng dần k (iterative deepening), k đầu tiên tìm được là nhỏ nhất
    for (int k = 1;; k++) {
        mu.clear();
        phan_tich(n, 1);
        if (dfs(n, 1, k, 1)) return k;
    }
}

int main() {
    // Có input.inp thì đọc/ghi file, không thì dùng bàn phím/màn hình
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    int n, t;
    cin >> n >> t;
    cout << solve_dtask(n, t) << "\n";
    return 0;
}
