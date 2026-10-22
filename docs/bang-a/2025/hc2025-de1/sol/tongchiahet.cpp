#include <iostream>
using namespace std;

long long tong_cong_thuc(long long n) {
    // Chia hết cho cả 3 và 5 <=> chia hết cho 15: 15, 30, ..., 15k
    long long k = n / 15;
    return 15 * (k * (k + 1) / 2);
}

int main() {
    long long n;
    cin >> n;
    cout << tong_cong_thuc(n) << "\n";
    return 0;
}
