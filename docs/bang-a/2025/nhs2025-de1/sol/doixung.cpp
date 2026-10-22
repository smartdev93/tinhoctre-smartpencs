#include <iostream>
#include <string>
#include <vector>
using namespace std;

unsigned long long dao_nguoc(unsigned long long x) {
    // Đảo chữ số bằng phép chia lấy dư - cách làm giống trên Scratch
    // (unsigned long long: số đảo của số 19 chữ số vẫn không tràn)
    unsigned long long r = 0;
    while (x > 0) {
        r = r * 10 + x % 10;
        x /= 10;
    }
    return r;
}

// In số __int128 (cout không in trực tiếp được)
void in_so(__int128 v) {
    if (v == 0) { cout << 0; return; }
    string s;
    while (v > 0) { s += char('0' + v % 10); v /= 10; }
    for (int i = (int)s.size() - 1; i >= 0; i--) cout << s[i];
}

void solve_so_doi_xung() {
    int n;
    cin >> n;
    vector<long long> arr(n);
    for (auto &x : arr) cin >> x;

    // Danh sách phụ: chỉ giữ các số đối xứng
    vector<long long> doi_xung;
    for (long long x : arr) {
        if (dao_nguoc(x) == (unsigned long long)x) doi_xung.push_back(x);
    }

    // Sắp xếp chèn: đơn giản, dễ chuyển sang Scratch
    for (int i = 1; i < (int)doi_xung.size(); i++) {
        long long x = doi_xung[i];
        int j = i - 1;
        while (j >= 0 && doi_xung[j] > x) {
            doi_xung[j + 1] = doi_xung[j];
            j--;
        }
        doi_xung[j + 1] = x;
    }

    // Tổng có thể vượt long long (100 số cỡ 1e18) nên dùng __int128
    __int128 tong_le = 0;
    for (long long x : doi_xung) {
        if (x % 2 == 1) tong_le += x;
    }

    if (!doi_xung.empty()) {
        for (int i = 0; i < (int)doi_xung.size(); i++) {
            if (i > 0) cout << " ";
            cout << doi_xung[i];
        }
        cout << "\n";
    } else {
        cout << -1 << "\n";
    }
    in_so(tong_le);
    cout << "\n";
}

int main() {
    solve_so_doi_xung();
    return 0;
}
