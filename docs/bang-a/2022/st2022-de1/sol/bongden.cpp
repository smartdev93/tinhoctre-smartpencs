#include <cstdio>
#include <iostream>
using namespace std;

long long solve_bongden(long long a) {
    // Chu vi bảng: 4 * a dm = 40 * a cm, cứ 5 cm một bóng
    long long so_bong = 40 * a / 5;
    return so_bong;
}

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    long long a;
    cin >> a;
    cout << solve_bongden(a) << "\n";
    return 0;
}
