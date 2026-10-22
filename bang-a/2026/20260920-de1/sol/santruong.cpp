#include <iostream>
#include <string>
using namespace std;

void solve_chuoi_lap_deu() {
    int k;
    string s;
    cin >> k >> s;

    if (s.size() % k != 0) {
        cout << -1 << "\n";
        return;
    }

    // Đếm số lần xuất hiện của từng ký tự
    int cnt[256] = {0};
    for (unsigned char ch : s) cnt[ch]++;

    string base;
    for (int ch = 0; ch < 256; ch++) {  // duyệt theo thứ tự chữ cái
        if (cnt[ch] == 0) continue;
        if (cnt[ch] % k != 0) {
            cout << -1 << "\n";
            return;
        }
        base += string(cnt[ch] / k, (char)ch);
    }

    string result;
    for (int i = 0; i < k; i++) result += base;
    cout << result << "\n";
}

int main() {
    solve_chuoi_lap_deu();
    return 0;
}
