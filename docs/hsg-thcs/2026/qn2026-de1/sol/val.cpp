#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int solve_val(int k, const vector<int> &a) {
    int n = a.size();
    int dem[4] = {0, 0, 0, 0};  // dem[v] = số lần giá trị v xuất hiện trong cửa sổ
    int khac = 0;               // số giá trị khác nhau trong cửa sổ a[l..r]
    int l = 0, best = 0;
    for (int r = 0; r < n; r++) {
        if (dem[a[r]] == 0) khac++;
        dem[a[r]]++;
        // Thu hẹp bên trái khi cửa sổ có hơn k giá trị
        while (khac > k) {
            dem[a[l]]--;
            if (dem[a[l]] == 0) khac--;
            l++;
        }
        if (khac == k && r - l + 1 > best) best = r - l + 1;
    }
    return best;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // Có val.inp thì đọc/ghi file, không thì dùng bàn phím/màn hình
    if (FILE *f = fopen("val.inp", "r")) {
        fclose(f);
        freopen("val.inp", "r", stdin);
        freopen("val.out", "w", stdout);
    }
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (int &x : a) cin >> x;
    cout << solve_val(k, a) << "\n";
    return 0;
}
