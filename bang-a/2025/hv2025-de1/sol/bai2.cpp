#include <iostream>
using namespace std;

void solve_tang_sua() {
    long long n;
    cin >> n;

    // Thùng rẻ nhất (285/48 nghìn mỗi hộp) nên mua gần tối đa số thùng.
    // Để chắc chắn, thử bớt 0..5 thùng; với tiền còn lại thử mọi số lốc,
    // phần dư mua lẻ.
    long long max_thung = n / 285;
    long long ans = 0;
    long long thung = max_thung;
    while (thung >= 0 && thung >= max_thung - 5) {
        long long con_lai = n - thung * 285;
        long long loc = 0;
        while (loc * 25 <= con_lai) {
            long long le = (con_lai - loc * 25) / 7;
            long long hop = thung * 48 + loc * 4 + le;
            if (hop > ans) {
                ans = hop;
            }
            loc++;
        }
        thung--;
    }

    cout << ans << "\n";
}

int main() {
    solve_tang_sua();
    return 0;
}
