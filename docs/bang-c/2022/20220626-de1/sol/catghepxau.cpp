#include <algorithm>
#include <array>
#include <cstdio>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

typedef unsigned long long ull;
typedef array<int, 3> Piece;  // (vị trí trong S1, vị trí trong S2, độ dài)
const ull M = (1ULL << 61) - 1;  // mô-đun băm
const ull BASE = 131;

ull mulmod(ull a, ull b) {
    unsigned __int128 x = (unsigned __int128)a * b;
    ull r = (ull)(x & M) + (ull)(x >> 61);
    return r >= M ? r - M : r;
}

vector<ull> prefix_hash(const string &s) {
    vector<ull> h(s.size() + 1, 0);
    for (size_t i = 0; i < s.size(); i++) {
        h[i + 1] = mulmod(h[i], BASE) + (unsigned char)s[i];
        if (h[i + 1] >= M) h[i + 1] -= M;
    }
    return h;
}

// Tham lam: lặp lại việc ghép đoạn chung DÀI NHẤT còn lại của S1 và S2.
// rev: duyệt S2 từ phải sang; last: ưu tiên vị trí xuất hiện sau cùng ở S1.
vector<Piece> greedy(const string &s1, const string &s2, bool rev, bool last) {
    int n = s1.size();
    vector<ull> h1 = prefix_hash(s1), h2 = prefix_hash(s2), pw(n + 1, 1);
    for (int i = 0; i < n; i++) pw[i + 1] = mulmod(pw[i], BASE);
    vector<char> used1(n, 0), used2(n, 0);
    vector<int> pu1(n + 1, 0), pu2(n + 1, 0);
    vector<Piece> pieces;
    int remain = n, hi = n;

    // (băm, vị trí) của các cửa sổ độ dài L chưa dùng ký tự nào
    auto windows = [&](const vector<ull> &h, const vector<int> &pu, int L) {
        vector<pair<ull, int>> w;
        for (int i = 0; i + L <= n; i++)
            if (pu[i + L] == pu[i]) w.push_back({(h[i + L] + M - mulmod(h[i], pw[L])) % M, i});
        return w;
    };
    while (remain > 0) {
        for (int i = 0; i < n; i++) {
            pu1[i + 1] = pu1[i] + used1[i];
            pu2[i + 1] = pu2[i] + used2[i];
        }
        auto exists = [&](int L) {
            unordered_set<ull> st;
            for (auto &e : windows(h1, pu1, L)) st.insert(e.first);
            for (auto &e : windows(h2, pu2, L))
                if (st.count(e.first)) return true;
            return false;
        };
        // tìm độ dài L lớn nhất còn đoạn chung: L chỉ giảm dần nên dò lùi
        // từ hi với bước nhân đôi, rồi chặt nhị phân trong khoảng tìm được
        int L = hi;
        if (!exists(hi)) {
            int bad = hi, step = 1, c;
            while (true) {
                c = max(1, hi - step);
                if (c == 1 || exists(c)) break;  // độ dài 1 luôn có đoạn chung
                bad = c;
                step *= 2;
            }
            int lo = c, up = bad - 1;
            while (lo < up) {
                int mid = (lo + up + 1) / 2;
                if (exists(mid)) lo = mid;
                else up = mid - 1;
            }
            L = lo;
        }
        // lấy mọi cặp đoạn chung độ dài L không chồng nhau
        unordered_map<ull, vector<int>> cand;
        for (auto &e : windows(h1, pu1, L)) cand[e.first].push_back(e.second);
        if (last)
            for (auto &kv : cand) reverse(kv.second.begin(), kv.second.end());
        vector<pair<ull, int>> w2 = windows(h2, pu2, L);
        if (rev) reverse(w2.begin(), w2.end());
        for (auto &e : w2) {
            int p = e.second;
            if (used2[p] || used2[p + L - 1]) continue;  // chồng lên đoạn vừa lấy trong lượt này
            auto it = cand.find(e.first);
            if (it == cand.end()) continue;
            vector<int> &lst = it->second;
            size_t k = 0;
            while (k < lst.size()) {
                int a = lst[k];
                if (used1[a] || used1[a + L - 1]) {  // đoạn đã bị dùng: bỏ khỏi danh sách
                    lst.erase(lst.begin() + k);
                    continue;
                }
                if (s1.compare(a, L, s2, p, L) == 0) {  // kiểm tra thật, tránh trùng băm
                    fill(used1.begin() + a, used1.begin() + a + L, 1);
                    fill(used2.begin() + p, used2.begin() + p + L, 1);
                    pieces.push_back({a, p, L});
                    remain -= L;
                    lst.erase(lst.begin() + k);
                    break;
                }
                k++;
            }
        }
        hi = max(1, L - 1);
    }
    // gộp hai đoạn kề nhau ở S1 mà cũng kề nhau, đúng thứ tự ở S2
    sort(pieces.begin(), pieces.end());
    vector<Piece> merged = {pieces[0]};
    for (size_t k = 1; k < pieces.size(); k++) {
        Piece &lp = merged.back();
        if (lp[1] + lp[2] == pieces[k][1]) lp[2] += pieces[k][2];
        else merged.push_back(pieces[k]);
    }
    return merged;
}

string solve_catghepxau(const string &s1, const string &s2) {
    string t1 = s1, t2 = s2;
    sort(t1.begin(), t1.end());
    sort(t2.begin(), t2.end());
    if (t1 != t2) return "-1";  // khác tập ký tự thì không thể cắt ghép
    vector<Piece> best;
    for (int rev = 0; rev < 2; rev++)  // chạy 4 biến thể, giữ phương án ít đoạn nhất
        for (int last = 0; last < 2; last++) {
            vector<Piece> cur = greedy(s1, s2, rev, last);
            if (best.empty() || cur.size() < best.size()) best = cur;
        }
    int c = best.size() - 1;
    string out = to_string(c) + "\n";
    for (int k = 1; k <= c; k++) {  // cắt sau ký tự thứ a (đánh số từ 1)
        if (k > 1) out += ' ';
        out += to_string(best[k][0]);
    }
    vector<int> order(c + 1);
    for (int k = 0; k <= c; k++) order[k] = k;
    sort(order.begin(), order.end(), [&](int x, int y) { return best[x][1] < best[y][1]; });
    out += "\n";
    for (int k = 0; k <= c; k++) {
        if (k) out += ' ';
        out += to_string(order[k] + 1);
    }
    return out;
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
    string s1, s2;
    cin >> s1 >> s2;
    cout << solve_catghepxau(s1, s2) << "\n";
    return 0;
}
