#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

long long solve_khongthich(long long k) {
    // Trong mỗi đoạn 30 số liên tiếp có đúng 18 số Polycarp thích
    vector<long long> mau;
    for (int x = 1; x <= 30; x++) {
        if (x % 3 != 0 && x % 10 != 3) {
            mau.push_back(x);
        }
    }
    // mau = {1, 2, 4, 5, 7, 8, 10, 11, 14, 16, 17, 19, 20, 22, 25, 26, 28, 29}
    long long nhom = (k - 1) / 18;
    long long vi_tri = (k - 1) % 18;
    return 30 * nhom + mau[vi_tri];
}

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    long long k;
    cin >> k;
    cout << solve_khongthich(k) << "\n";
    return 0;
}
