#include <cstdio>
#include <iostream>
using namespace std;

long long solve_tong3k(long long k) {
    // Số hạng thứ i của dãy 11, 14, 17, ... là 11 + 3*(i - 1) = 3*i + 8
    long long a = 3 * k + 8;
    // Tổng ba số hạng liên tiếp a, a + 3, a + 6
    long long tong = a + (a + 3) + (a + 6);
    return tong;
}

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    long long k;
    cin >> k;
    cout << solve_tong3k(k) << "\n";
    return 0;
}
