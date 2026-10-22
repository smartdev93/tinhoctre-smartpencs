#include <chrono>
#include <cstdio>
#include <random>
#include <string>
#include <vector>
using namespace std;

typedef unsigned long long ull;
const ull P = (1ULL << 61) - 1;  // số nguyên tố Mersenne, lớn hơn mọi |A^3 - B| có thể xảy ra
const int ROUNDS = 2;            // số lần thử Freivalds cho mỗi bộ dữ liệu

ull mulmod(ull a, ull b) {
    unsigned __int128 x = (unsigned __int128)a * b;
    ull r = (ull)(x & P) + (ull)(x >> 61);
    return r >= P ? r - P : r;
}

ull to_mod(long long x) {  // đưa số âm về [0, P)
    long long r = x % (long long)P;
    return (ull)(r < 0 ? r + (long long)P : r);
}

// Nhân ma trận m (n x n, lưu phẳng) với vectơ v, lấy dư P
vector<ull> mat_vec(const vector<ull> &m, const vector<ull> &v, int n) {
    vector<ull> r(n);
    for (int i = 0; i < n; i++) {
        ull s = 0;
        const ull *row = &m[(size_t)i * n];
        for (int j = 0; j < n; j++) {
            s += mulmod(row[j], v[j]);
            if (s >= P) s -= P;
        }
        r[i] = s;
    }
    return r;
}

// Đọc số nguyên nhanh bằng fread: dữ liệu vào tới khoảng 10^7 số (hơn 100 MB)
static char buf[1 << 16];
size_t buf_len = 0, buf_pos = 0;

int read_char() {
    if (buf_pos == buf_len) {
        buf_len = fread(buf, 1, sizeof(buf), stdin);
        buf_pos = 0;
        if (buf_len == 0) return -1;
    }
    return buf[buf_pos++];
}

long long read_int() {
    int c = read_char();
    while (c != '-' && (c < '0' || c > '9')) c = read_char();
    bool neg = false;
    if (c == '-') {
        neg = true;
        c = read_char();
    }
    long long x = 0;
    while (c >= '0' && c <= '9') {
        x = x * 10 + (c - '0');
        c = read_char();
    }
    return neg ? -x : x;
}

mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());

string solve_matran(int n, const vector<ull> &a, const vector<ull> &b) {
    for (int k = 0; k < ROUNDS; k++) {
        // Freivalds: so sánh A(A(Av)) với Bv cho vectơ ngẫu nhiên v
        vector<ull> v(n);
        for (auto &x : v) x = rng() % P;
        if (mat_vec(a, mat_vec(a, mat_vec(a, v, n), n), n) != mat_vec(b, v, n)) return "NO";
    }
    return "YES";
}

int main() {
    // Có input.inp thì đọc/ghi file, không thì dùng bàn phím/màn hình
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    int t = read_int();
    while (t--) {
        int n = read_int();
        vector<ull> a((size_t)n * n), b((size_t)n * n);
        // phần tử B tới 10^18 vẫn vừa long long
        for (auto &e : a) e = to_mod(read_int());
        for (auto &e : b) e = to_mod(read_int());
        printf("%s\n", solve_matran(n, a, b).c_str());
    }
    return 0;
}
