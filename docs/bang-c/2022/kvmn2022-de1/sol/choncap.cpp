#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int n, X, sz;
vector<long long> P, vals;
vector<int> rk;
vector<long long> bc, bs;

// Đếm số cặp có trọng số >= T, tổng trọng số của chúng ghi vào sm (nếu needSum)
long long countPairs(long long T, bool needSum, long long &sm) {
    fill(bc.begin(), bc.end(), 0);
    if (needSum) fill(bs.begin(), bs.end(), 0);
    long long cnt = 0;
    sm = 0;
    for (int j = X; j <= n; j++) {
        // đưa P[j - X] vào cây: các i = 0..j-X là đầu trái hợp lệ cho j
        long long v = P[j - X];
        for (int i = rk[j - X]; i <= sz; i += i & -i) {
            bc[i]++;
            if (needSum) bs[i] += v;
        }
        // các P[i] <= P[j] - T
        int i = upper_bound(vals.begin(), vals.end(), P[j] - T) - vals.begin();
        long long c = 0, s = 0;
        for (; i > 0; i -= i & -i) {
            c += bc[i];
            if (needSum) s += bs[i];
        }
        cnt += c;
        if (needSum) sm += c * P[j] - s;
    }
    return cnt;
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
    long long k;
    cin >> n >> k >> X;
    // P[i] = a1 + ... + ai; trọng số cặp (l, r) = P[r] - P[l-1], cần r - (l-1) >= X
    P.assign(n + 1, 0);
    long long absSum = 0;
    for (int i = 1; i <= n; i++) {
        long long x;
        cin >> x;
        P[i] = P[i - 1] + x;
        absSum += (x < 0 ? -x : x);
    }
    vals = P;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    sz = vals.size();
    rk.resize(n + 1);
    for (int i = 0; i <= n; i++) rk[i] = upper_bound(vals.begin(), vals.end(), P[i]) - vals.begin();
    bc.assign(sz + 1, 0);
    bs.assign(sz + 1, 0);

    long long total = (long long)(n - X + 1) * (n - X + 2) / 2;  // số cặp hợp lệ
    k = min(k, total);  // (giả định) k không vượt quá số cặp

    // Tìm ngưỡng T lớn nhất mà số cặp có trọng số >= T vẫn >= k
    long long lo = -2 * absSum - 1, hi = absSum + 1, sm;
    while (hi - lo > 1) {
        long long mid = lo + (hi - lo) / 2;
        if (countPairs(mid, false, sm) >= k) lo = mid;
        else hi = mid;
    }
    long long T = lo;
    // Lấy hết các cặp > T, phần còn thiếu đều có trọng số đúng bằng T
    long long c = countPairs(T + 1, true, sm);
    // Kết quả tới khoảng 10^7 * 3 * 10^10 = 3 * 10^17 -> long long
    cout << sm + (k - c) * T << "\n";
    return 0;
}
