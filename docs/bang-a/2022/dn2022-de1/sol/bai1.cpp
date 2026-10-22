#include <cstdio>
#include <iostream>
using namespace std;

long long solve_bai1(long long n, long long k) {
    // Các số chia hết cho k trong [1, n]: k, 2k, ..., m*k với m = n / k
    long long m = n / k;
    // Tổng = k * (1 + 2 + ... + m); tính m*(m+1)/2 trước để không tràn
    return k * (m * (m + 1) / 2);
}

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    long long n, k;
    cin >> n >> k;
    cout << solve_bai1(n, k) << "\n";
    return 0;
}
