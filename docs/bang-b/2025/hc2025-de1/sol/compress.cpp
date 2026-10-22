#include <algorithm>
#include <cstdio>
#include <iostream>
#include <iterator>
#include <string>
using namespace std;

string solve_compress(const string &data) {
    // Bỏ khoảng trắng / xuống dòng ở hai đầu (giống strip() của Python)
    const string ws = " \t\r\n\v\f";
    size_t l = data.find_first_not_of(ws);
    if (l == string::npos) return "";
    size_t r = data.find_last_not_of(ws);
    string s = data.substr(l, r - l + 1);

    int n = s.size();
    string res;
    int i = 0;
    while (i < n) {
        // Đếm đoạn ký tự giống nhau bắt đầu tại i
        int j = i;
        while (j < n && s[j] == s[i]) j++;
        res += to_string(j - i);
        res += s[i];
        i = j;
    }
    // Nối bằng += (O(N)), rồi đảo ngược cả xâu kết quả
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string data((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());
    cout << solve_compress(data) << "\n";
    return 0;
}
