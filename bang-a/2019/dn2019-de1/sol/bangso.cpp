#include <iostream>
#include <vector>
using namespace std;

void solve_bang_so() {
    int n;
    cin >> n;  // số lượng các số
    vector<long long> so;
    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;  // nhập từng số vào danh sách Số
        so.push_back(x);
    }

    long long dem_lon_hon_5 = 0;
    long long lon_nhat = so[0];
    long long tong_le = 0;
    long long dem_chan = 0;
    for (long long x : so) {
        if (x > 5) dem_lon_hon_5 = dem_lon_hon_5 + 1;
        if (x > lon_nhat) lon_nhat = x;
        if (x % 2 != 0) {
            tong_le = tong_le + x;
        } else {
            dem_chan = dem_chan + 1;
        }
    }

    // danh sách Kết quả
    vector<long long> ket_qua = {dem_lon_hon_5, lon_nhat, tong_le, dem_chan};
    for (long long v : ket_qua) cout << v << "\n";
}

int main() {
    solve_bang_so();
    return 0;
}
