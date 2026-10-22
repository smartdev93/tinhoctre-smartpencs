#include <algorithm>
#include <array>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int B = 64;  // kích thước một khối ký tự (lá của cây phân đoạn)
typedef array<unsigned char, 26> Map;  // ánh xạ "ký tự gốc -> ký tự hiện tại"

int n, sz, lg;
string s;
vector<Map> tag;      // thao tác chưa đẩy xuống của mỗi nút
vector<char> has;     // has[k] = 1 nếu tag[k] khác ánh xạ đồng nhất

void compose(int k, const Map &t) {  // áp t sau tag[k]
    for (int x = 0; x < 26; x++) tag[k][x] = t[tag[k][x]];
    has[k] = 1;
}

void push(int k) {
    if (!has[k]) return;
    // thao tác ở nút cha mới hơn thao tác đang chờ ở nút con -> áp sau
    compose(2 * k, tag[k]);
    compose(2 * k + 1, tag[k]);
    for (int x = 0; x < 26; x++) tag[k][x] = x;
    has[k] = 0;
}

void apply_block(int blk) {  // áp tag của lá vào các ký tự của khối
    int k = blk + sz;
    if (!has[k]) return;
    int a = blk * B, b = min(a + B, n);
    for (int p = a; p < b; p++) s[p] = 'a' + tag[k][s[p] - 'a'];
    for (int x = 0; x < 26; x++) tag[k][x] = x;
    has[k] = 0;
}

void materialize(int blk) {  // đẩy hết thao tác đang chờ xuống khối blk
    int k = blk + sz;
    for (int h = lg; h > 0; h--) push(k >> h);
    apply_block(blk);
}

void change(int l, int r, char c1, char c2) {  // đổi c1 -> c2 trên s[l..r]
    for (int p = l; p <= r; p++)
        if (s[p] == c1) s[p] = c2;
}

string solve_biendoixau(const vector<int> &qi, const vector<int> &qj,
                        const vector<char> &qc1, const vector<char> &qc2) {
    n = s.size();
    int nb = (n + B - 1) / B;
    sz = 1, lg = 0;
    while (sz < nb) sz *= 2, lg++;
    Map id;
    for (int x = 0; x < 26; x++) id[x] = x;
    tag.assign(2 * sz, id);
    has.assign(2 * sz, 0);
    for (size_t q = 0; q < qi.size(); q++) {
        int i = qi[q], j = qj[q];
        char c1 = qc1[q], c2 = qc2[q];
        int bi = i / B, bj = j / B;
        if (bi == bj) {
            materialize(bi);
            change(i, j, c1, c2);
            continue;
        }
        int lo = bi, hi = bj;
        if (i != bi * B) {  // khối trái chỉ phủ một phần
            materialize(bi);
            change(i, (bi + 1) * B - 1, c1, c2);
            lo = bi + 1;
        }
        if (j + 1 != min((bj + 1) * B, n)) {  // khối phải chỉ phủ một phần
            materialize(bj);
            change(bj * B, j, c1, c2);
            hi = bj - 1;
        }
        if (lo > hi) continue;
        Map g = id;
        g[c1 - 'a'] = c2 - 'a';
        // gán thao tác cho các khối nguyên [lo, hi] (cây phân đoạn lười, kiểu từ dưới lên)
        int l = lo + sz, r = hi + 1 + sz;
        for (int h = lg; h > 0; h--) {
            if (((l >> h) << h) != l) push(l >> h);
            if (((r >> h) << h) != r) push((r - 1) >> h);
        }
        while (l < r) {
            if (l & 1) compose(l++, g);
            if (r & 1) compose(--r, g);
            l >>= 1;
            r >>= 1;
        }
    }
    // đẩy mọi thao tác xuống lá rồi áp vào từng khối
    for (int k = 1; k < sz; k++) push(k);
    for (int blk = 0; blk < nb; blk++) apply_block(blk);
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // Có input.inp thì đọc/ghi file, không thì dùng bàn phím/màn hình
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    int m;
    cin >> s >> m;
    vector<int> qi(m), qj(m);
    vector<char> qc1(m), qc2(m);
    for (int q = 0; q < m; q++) cin >> qi[q] >> qj[q] >> qc1[q] >> qc2[q];
    cout << solve_biendoixau(qi, qj, qc1, qc2) << "\n";
    return 0;
}
