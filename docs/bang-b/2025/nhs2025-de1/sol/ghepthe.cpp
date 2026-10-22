#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool so_sanh(const string &a, const string &b) {
    // a đứng trước b nếu a + b tạo số lớn hơn b + a
    return a + b > b + a;
}

string solve_ghep_the(vector<string> the) {
    sort(the.begin(), the.end(), so_sanh);
    string ket_qua;
    for (const string &t : the) ket_qua += t;

    // Mọi thẻ đều là 0 -> in "0" thay vì "000..."
    return ket_qua[0] == '0' ? "0" : ket_qua;
}

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<string> the(n);  // đọc mỗi số dưới dạng xâu
    for (auto &t : the) cin >> t;
    cout << solve_ghep_the(the) << "\n";
    return 0;
}
