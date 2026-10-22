#include <iostream>
using namespace std;

int so_tu(int thu) {
    // Chủ nhật (0) nghỉ, thứ K (2..7) nhớ K từ
    if (thu == 0) {
        return 0;
    }
    return thu;
}

int ngay_mai(int thu) {
    if (thu == 0) {
        return 2;  // Chủ nhật -> Thứ Hai
    }
    if (thu == 7) {
        return 0;  // Thứ Bảy -> Chủ nhật
    }
    return thu + 1;
}

void solve_tu_vung() {
    int k;
    long long n;
    cin >> k >> n;

    // Mỗi tuần trọn vẹn (7 ngày) nhớ được 2+3+4+5+6+7 = 27 từ
    long long tong = (n / 7) * 27;

    // Các ngày lẻ còn lại (< 7 ngày), bắt đầu từ ngày mai
    int thu = ngay_mai(k);
    for (int i = 0; i < n % 7; i++) {
        tong += so_tu(thu);
        thu = ngay_mai(thu);
    }

    cout << tong << "\n";
}

int main() {
    solve_tu_vung();
    return 0;
}
