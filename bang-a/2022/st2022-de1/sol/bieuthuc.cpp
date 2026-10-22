#include <cstdio>
#include <iostream>
using namespace std;

// b, c không ảnh hưởng tới kết quả
long long solve_bieuthuc(long long a, long long /*b*/, long long /*c*/, long long d) {
    // x - y nhỏ nhất khi x nhỏ nhất (x = a) và y lớn nhất (y = d)
    return a - d;
}

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    long long a, b, c, d;
    cin >> a >> b >> c >> d;
    cout << solve_bieuthuc(a, b, c, d) << "\n";
    return 0;
}
