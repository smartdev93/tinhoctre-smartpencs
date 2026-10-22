#include <iostream>
#include <string>
using namespace std;

void dem_ki_tu_so() {
    string s;
    getline(cin, s);  // đọc cả dòng, chuỗi có thể chứa dấu cách

    // Duyệt từng ký tự, gặp chữ số '0'..'9' thì tăng biến đếm
    int dem = 0;
    for (char c : s) {
        if (c >= '0' && c <= '9') {
            dem = dem + 1;
        }
    }

    cout << dem << "\n";
}

int main() {
    dem_ki_tu_so();
    return 0;
}
