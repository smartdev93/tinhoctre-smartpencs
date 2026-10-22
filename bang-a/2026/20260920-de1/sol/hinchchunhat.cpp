#include <iostream>
using namespace std;

void solve_tang_banh() {
    long long n;
    cin >> n;

    // Hộp lớn rẻ nhất (7 nghìn/cái) nên mua tối đa hộp lớn,
    // phần tiền dư (< 210) thử từng số hộp nhỏ, còn lại mua lẻ.
    long long box_large = n / 210;
    long long remaining = n - box_large * 210;
    long long ans = 0;

    for (long long box_small = 0; box_small <= remaining / 38; box_small++) {
        long long left = remaining - box_small * 38;
        long long cakes = box_large * 30 + box_small * 5 + left / 9;
        if (cakes > ans) ans = cakes;
    }

    cout << ans << "\n";
}

int main() {
    solve_tang_banh();
    return 0;
}
