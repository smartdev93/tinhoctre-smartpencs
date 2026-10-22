#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

typedef __int128 i128;

// In số __int128 (cout không in trực tiếp được)
string to_str(i128 x) {
    if (x == 0) return "0";
    bool am = x < 0;
    if (am) x = -x;
    string s;
    while (x > 0) {
        s = char('0' + (int)(x % 10)) + s;
        x /= 10;
    }
    return am ? "-" + s : s;
}

i128 solve_bai3(long long n) {
    // Hàng n có 2n - 1 số, số cuối là n*n, số đầu là (n-1)*(n-1) + 1
    i128 dau = (i128)(n - 1) * (n - 1) + 1;
    i128 cuoi = (i128)n * n;
    i128 so_luong = 2 * (i128)n - 1;
    // Tổng dãy số liên tiếp = (số đầu + số cuối) * số lượng / 2
    // Với n = 10^7, tổng khoảng 2 * 10^21, vượt long long nên dùng __int128
    return (dau + cuoi) * so_luong / 2;
}

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    long long n;
    cin >> n;
    cout << to_str(solve_bai3(n)) << "\n";
    return 0;
}
