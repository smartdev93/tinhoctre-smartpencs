#include <iostream>
using namespace std;

void solve_tinh_toan() {
    long long n, a;
    cin >> n;  // số hình vuông
    cin >> a;  // cạnh hình vuông nhỏ nhất

    long long tong = 0;
    long long canh = a;
    for (long long i = 0; i < n; i++) {
        tong = tong + canh * canh;  // cộng diện tích hình vuông thứ i+1
        canh = canh + 20;           // hình sau lớn hơn hình trước 20 đơn vị
    }

    cout << tong << "\n";
}

int main() {
    solve_tinh_toan();
    return 0;
}
