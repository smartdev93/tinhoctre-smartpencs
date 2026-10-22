#include <cstdio>
#include <iostream>
using namespace std;

long long solve_sal(long long k, long long d, long long a, long long b) {
    // Mỗi tuần trọn vẹn có 5 ngày thường và 2 ngày cuối tuần
    long long tong = (d / 7) * (5 * a + 2 * b);
    // Duyệt các ngày lẻ còn lại (tối đa 6 ngày)
    long long thu = k;
    for (long long i = 0; i < d % 7; i++) {
        tong += (thu >= 7) ? b : a;  // 7 = thứ Bảy, 8 = Chủ Nhật
        thu = (thu < 8) ? thu + 1 : 2;
    }
    return tong;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // Có sal.inp thì đọc/ghi file, không thì dùng bàn phím/màn hình
    if (FILE *f = fopen("sal.inp", "r")) {
        fclose(f);
        freopen("sal.inp", "r", stdin);
        freopen("sal.out", "w", stdout);
    }
    long long k, d, a, b;
    cin >> k >> d >> a >> b;
    cout << solve_sal(k, d, a, b) << "\n";
    return 0;
}
