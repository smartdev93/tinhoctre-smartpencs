#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

string solve_tinh() {
    // Thử mọi số có hai chữ số x = 10..99
    // Viết thêm chữ số 9 vào bên trái x được số 900 + x
    string ket_qua;
    for (int x = 10; x < 100; x++) {
        if (900 + x == 16 * x) {
            if (!ket_qua.empty()) ket_qua += " ";
            ket_qua += to_string(x);
        }
    }
    return ket_qua;
}

int main() {
    // Đề không có dữ liệu vào; nếu có input.inp thì ghi kết quả ra output.out
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    cout << solve_tinh() << "\n";
    return 0;
}
