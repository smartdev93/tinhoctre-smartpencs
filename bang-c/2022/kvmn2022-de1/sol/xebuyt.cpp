#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
using namespace std;

// Đọc số nhanh bằng fread (tới 3 * 10^6 số, cin trên một số máy khá chậm)
static char buf[1 << 16];
size_t bufLen = 0, bufPos = 0;
int readChar() {
    if (bufPos == bufLen) {
        bufLen = fread(buf, 1, sizeof(buf), stdin);
        bufPos = 0;
        if (bufLen == 0) return -1;
    }
    return buf[bufPos++];
}
long long readInt() {
    int c = readChar();
    while (c != -1 && c != '-' && (c < '0' || c > '9')) c = readChar();
    bool neg = (c == '-');
    if (neg) c = readChar();
    long long x = 0;
    while (c >= '0' && c <= '9') x = x * 10 + (c - '0'), c = readChar();
    return neg ? -x : x;
}

int main() {
    // Có input.inp thì đọc/ghi file, không thì dùng bàn phím/màn hình
    if (FILE *f = fopen("input.inp", "r")) {
        fclose(f);
        freopen("input.inp", "r", stdin);
        freopen("output.out", "w", stdout);
    }
    int n = readInt(), m = readInt(), q = readInt();
    long long a = readInt(), b = readInt();
    vector<char> special(n + 2, 0);
    for (int i = 0; i < m; i++) {
        special[readInt()] = 1;
    }
    // pre[i] = trạm đặc biệt gần nhất <= i, nxt[i] = trạm đặc biệt gần nhất >= i (0 nếu không có)
    vector<int> pre(n + 2, 0), nxt(n + 2, 0);
    for (int i = 1; i <= n; i++) pre[i] = special[i] ? i : pre[i - 1];
    for (int i = n; i >= 1; i--) nxt[i] = special[i] ? i : nxt[i + 1];

    string out;
    for (int k = 0; k < q; k++) {
        int x = readInt(), y = readInt();
        // Chi phí tới 10^6 * 10^6 = 10^12 -> long long
        long long best = a * llabs((long long)x - y);  // chỉ đi xe thường
        if (b < a) {
            // xe thường x -> s, xe nhanh s -> u, xe thường u -> y;
            // s chỉ cần thử 2 trạm đặc biệt kề x, u chỉ cần thử 2 trạm kề y
            int cs[2] = {pre[x], nxt[x]}, cu[2] = {pre[y], nxt[y]};
            for (int s : cs) {
                if (s == 0) continue;
                for (int u : cu) {
                    if (u == 0) continue;
                    long long c = a * llabs((long long)x - s) + b * llabs((long long)s - u) +
                                  a * llabs((long long)u - y);
                    if (c < best) best = c;
                }
            }
        }
        out += to_string(best);
        out += '\n';
    }
    fputs(out.c_str(), stdout);
    return 0;
}
