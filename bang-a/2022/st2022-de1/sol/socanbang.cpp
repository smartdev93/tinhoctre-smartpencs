#include <algorithm>
#include <cstdio>
#include <iostream>
using namespace std;

long long solve_socanbang(long long n) {
    long long dem = 0;
    // Số cân bằng có 2L chữ số = x * (10^L + 1), với x có đúng L chữ số
    long long nho = 1;                  // 10^(L-1): số nhỏ nhất có L chữ số
    while (true) {
        long long lon = nho * 10 - 1;   // số lớn nhất có L chữ số
        long long he_so = nho * 10 + 1; // 10^L + 1
        // nho * he_so > n, viết dạng chia để không tràn số
        if (nho > n / he_so) {          // số cân bằng nhỏ nhất đã vượt n
            break;
        }
        long long x_max = min(lon, n / he_so);
        dem += x_max - nho + 1;
        nho = nho * 10;
    }
    return dem;
}

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    long long n;
    cin >> n;
    cout << solve_socanbang(n) << "\n";
    return 0;
}
