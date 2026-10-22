#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void solve_chia_keo() {
    int n;
    cin >> n;
    vector<long long> arr(n);
    for (auto &x : arr) cin >> x;
    sort(arr.begin(), arr.end());

    for (int i = 1; i < n; i++) {
        if (arr[i] - arr[i - 1] == 1) {
            cout << 2 << "\n";
            return;
        }
    }

    cout << 1 << "\n";
}

int main() {
    solve_chia_keo();
    return 0;
}
