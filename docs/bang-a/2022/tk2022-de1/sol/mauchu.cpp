#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

string solve_mauchu(long long k) {
    string chu = "TINHOCTRETHANHKHE";  // 17 chữ cái, không tính dấu cách
    string mau[4] = {"Blue", "Red", "White", "Yellow"};
    // Chữ thứ k lặp lại theo chu kỳ 17, màu lặp lại theo chu kỳ 4
    char ki_tu = chu[(k - 1) % 17];
    string mau_chu = mau[(k - 1) % 4];
    return string(1, ki_tu) + "-" + mau_chu;
}

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    long long k;
    cin >> k;
    cout << solve_mauchu(k) << "\n";
    return 0;
}
