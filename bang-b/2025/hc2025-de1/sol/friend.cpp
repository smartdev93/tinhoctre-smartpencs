#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

long long tong_uoc_thuc_su(long long n) {
    // Tổng các ước của n, không kể chính n. Duyệt i đến căn n -> O(√n).
    if (n <= 1) return 0;
    long long s = 1;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            s += i;
            if (i * i != n) s += n / i;  // ước đối xứng n / i
        }
    }
    return s;
}

string solve_friend(long long a, long long b) {
    // Cặp thân thiện phải gồm hai số khác nhau (6 6 là số hoàn hảo -> NO).
    // Kiểm tra A trước, chỉ tính tổng ước của B khi cần -> đỡ một lần O(√N)
    if (a != b && tong_uoc_thuc_su(a) == b && tong_uoc_thuc_su(b) == a) return "YES";
    return "NO";
}

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    long long a, b;  // A, B tới 10^12 -> long long
    cin >> a >> b;
    cout << solve_friend(a, b) << "\n";
    return 0;
}
