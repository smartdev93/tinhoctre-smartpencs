#include <iostream>
#include <string>
using namespace std;

// Bỏ khoảng trắng hai đầu (giống strip() của Python)
string strip(const string &s) {
    const string ws = " \t\r\n\v\f";
    size_t dau = s.find_first_not_of(ws);
    if (dau == string::npos) {
        return "";
    }
    size_t cuoi = s.find_last_not_of(ws);
    return s.substr(dau, cuoi - dau + 1);
}

void solve_dong_phuc() {
    string dong;
    getline(cin, dong);
    long long n = stoll(strip(dong));
    string s;
    getline(cin, s);   // đọc cả dòng (kể cả dấu cách nếu có)
    s = strip(s);

    // Áo S cần 2 mét, M cần 3 mét, L cần 4 mét vải
    long long tong = 0;
    for (long long i = 0; i < n && i < (long long)s.size(); i++) {
        if (s[i] == 'S') {
            tong += 2;
        } else if (s[i] == 'M') {
            tong += 3;
        } else if (s[i] == 'L') {
            tong += 4;
        }
    }

    cout << tong << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve_dong_phuc();
    return 0;
}
