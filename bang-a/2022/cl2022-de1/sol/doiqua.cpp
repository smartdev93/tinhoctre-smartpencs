#include <iostream>
using namespace std;

void doi_qua() {
    long long k;
    cin >> k;

    // Cộng dần 1 + 2 + 3 + ... cho tới khi tổng đạt ít nhất k điểm
    long long n = 1;
    long long tong = 1;
    while (tong < k) {
        n = n + 1;
        tong = tong + n;
    }

    cout << n << "\n";
    cout << tong << "\n";
}

int main() {
    doi_qua();
    return 0;
}
