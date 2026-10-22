#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

const string DONG_CHU = "HOITHITINHOCTRECAPTHANHPHO";

long long solve_bai2(long long n, const string &ch) {
    long long L = DONG_CHU.size();  // 26 ký tự
    // Đếm ch trong một lần lặp của dòng chữ
    long long dem_mot_lan = 0;
    for (char c : DONG_CHU) {
        if (string(1, c) == ch) dem_mot_lan++;
    }
    // n ký tự = (n / L) lần lặp đầy đủ + (n % L) ký tự đầu của lần tiếp theo
    long long ans = (n / L) * dem_mot_lan;
    for (long long i = 0; i < n % L; i++) {
        if (string(1, DONG_CHU[i]) == ch) ans++;
    }
    return ans;
}

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    long long n;
    string ch;
    cin >> n >> ch;
    cout << solve_bai2(n, ch) << "\n";
    return 0;
}
