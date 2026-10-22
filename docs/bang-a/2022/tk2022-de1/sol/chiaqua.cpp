#include <cstdio>
#include <iostream>
using namespace std;

long long solve_chiaqua(long long n, long long m) {
    // n: số sách đang có, m: số bạn
    long long du = n % m;
    // Nếu chia hết thì không cần mua thêm, ngược lại mua thêm m - du cuốn
    if (du == 0) return 0;
    return m - du;
}

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    long long n, m;
    cin >> n >> m;
    cout << solve_chiaqua(n, m) << "\n";
    return 0;
}
