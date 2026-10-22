# Đáp án - Bảng C Chung kết toàn quốc 2021

Lời giải tham khảo bằng Python 3 và C++ (C++17). Xem lại [đề bài](index.md).

Đề chính thức đọc/ghi chuẩn. Để đồng bộ với các đề khác trên site, mỗi chương trình đọc `input.inp` và ghi `output.out` nếu có file `input.inp`; nếu không có thì đọc từ bàn phím và in ra màn hình, đúng như đề yêu cầu.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Bài tập | Sắp xếp; $m < n$: cửa sổ trượt lấy max; $m > n$: chặt nhị phân $d$ | $O(n \log n + n \log C)$ |
| 2 | Bài khó | Tìm kiếm sâu dần theo $k$, hai số cuối giải bằng duyệt ước | tìm kiếm có cắt nhánh |
| 3 | Xâu con | Đếm cặp cách chọn cho cùng một xâu con, quy hoạch động 2 chiều + tổng tiền tố | $O(N^2)$ |
| 4 | Cắt bánh | Thêm từng đường cắt, số miếng tăng $1 +$ số giao điểm phân biệt mới | $O(m + D^2 \log D)$, $D \le 1225$ |

---

## 1. Bài tập

**Ý tưởng.** Sắp xếp độ khó tăng dần, gọi $g_i = c_{i+1} - c_i$ là chênh lệch giữa hai bài liền kề.

*Trường hợp $m < n$ (bỏ bài).* Giữ lại $m$ bài **liên tiếp** trong dãy đã sắp xếp luôn tốt nhất. Giả sử giữ các bài có chỉ số $i_1 < i_2 < \ldots < i_m$. Xét $m$ bài liên tiếp $i_1, i_1 + 1, \ldots, i_1 + m - 1$: mọi chênh lệch giữa chúng là một $g_j$ nằm trong đoạn $[i_1, i_m]$, và $g_j$ đó không vượt quá chênh lệch của cặp bài giữ lại "bao" nó. Vậy đáp án là

$$\min_{\text{cửa sổ } m - 1 \text{ khoảng liên tiếp}} \ \max g_j,$$

tính bằng max trên cửa sổ trượt (deque) trong $O(n)$.

*Trường hợp $m > n$ (thêm bài).* Muốn mọi chênh lệch $\le d$ thì khoảng $g$ cần chen thêm $\lceil g / d \rceil - 1$ bài. Đặt thêm bài ra ngoài khoảng $[c_{\min}, c_{\max}]$ chỉ tạo thêm chênh lệch, còn bài thừa có thể đặt trùng độ khó sẵn có (chênh lệch 0). Nên $d$ khả thi khi $\sum \lceil g_i / d \rceil - 1 \le m - n$. Điều kiện này đơn điệu theo $d$, nên chặt nhị phân $d$ trên $[1, \max g]$. Nếu mọi bài cùng độ khó thì đáp án là 0.

Ví dụ 2: sắp xếp được $6, 8, 9$; thêm một bài độ khó 7 thì dãy $6, 7, 8, 9$ có $d = 1$.

!!! warning "Bẫy thường gặp"
    - Khi $m < n$, chọn tham lam "bỏ bài gây chênh lệch lớn nhất" là sai; bài bỏ ở giữa còn làm gộp hai khoảng lại.
    - Với $g = 0$ (hai bài trùng độ khó), công thức $\lfloor (g - 1) / d \rfloor$ cho $-1$ trong Python. Lời giải chỉ cộng khi $g > d$.
    - Đáp án có thể là 0 (ví dụ có hai bài trùng độ khó và $m < n$).

!!! note "Nếu viết bằng C++"
    $c_i \le 10^9$ nên chênh lệch vừa `int`, nhưng tổng số bài cần chen thêm có thể lớn; lời giải dùng `long long` cho chắc.

=== "Python"

    ```python title="tasks.py"
    --8<-- "bang-c/2021/20211121-de1/sol/tasks.py"
    ```

=== "C++"

    ```cpp title="tasks.cpp"
    --8<-- "bang-c/2021/20211121-de1/sol/tasks.cpp"
    ```

## 2. Bài khó

**Ý tưởng.** Chia hai vế cho $a_1 a_2 \cdots a_k$:

$$\prod_{i=1}^{k} \frac{a_i + t}{a_i} = n, \qquad \frac{a_i + t}{a_i} = 1 + \frac{t}{a_i} \in (1,\ t + 1].$$

*Luôn có nghiệm khi $n \ge 2$.* Chọn $a = j \cdot t$ thì $\frac{a + t}{a} = \frac{j + 1}{j}$, và $\frac{2}{1} \cdot \frac{3}{2} \cdots \frac{n}{n - 1} = n$. Vậy chỉ có $n = 1$ là in $-1$ (mỗi thừa số đều lớn hơn 1).

*Tìm $k$ nhỏ nhất.* Thử lần lượt $k = 1, 2, 3, \ldots$ (tìm kiếm sâu dần), $k$ đầu tiên tìm được là đáp án. Với mỗi $k$, kiểm tra phân số $r = p/q$ (tối giản, ban đầu $r = n$) có viết được thành tích $k$ thừa số dạng $\frac{a + t}{a}$ hay không, với $a_1 \le a_2 \le \ldots \le a_k$ (thừa số giảm dần):

- **Còn 1 thừa số:** $\frac{a + t}{a} = \frac{p}{q} \iff a = \frac{t q}{p - q}$, kiểm tra chia hết và $a \ge a_{\text{trước}}$.
- **Còn 2 thừa số** $a \le b$: biến đổi $p a b = q (a + t)(b + t)$ thành
  $$(a u - q t)(b u - q t) = p \, q \, t^2, \qquad u = p - q.$$
  Duyệt các ước $X \le \sqrt{p q t^2}$, thử $X \equiv -q t \pmod u$ để lấy $a = \frac{X + q t}{u}$, $b = \frac{p q t^2 / X + q t}{u}$. Để sinh ước nhanh, chương trình lưu sẵn phân tích thừa số nguyên tố của $p/q$ (cộng/trừ số mũ của $a$ và $a + t$ mỗi lần đi xuống).
- **Còn $k \ge 3$ thừa số:** thừa số đầu là lớn nhất nên $\frac{a + t}{a} < r$ (các thừa số còn lại đều $> 1$) và $\left(\frac{a + t}{a}\right)^k \ge r$. Suy ra
  $$\frac{t}{r - 1} < a \le \frac{t}{r^{1/k} - 1},$$
  duyệt $a$ trong đoạn này rồi đệ quy với $r \cdot \frac{a}{a + t}$, $k - 1$.

Ví dụ $n = 4, t = 1$: $k = 1$ cần $a = \frac{1}{3}$, không nguyên. $k = 2$: $u = 3$, $p q t^2 = 4$, ước $X = 2$ thỏa $2 \equiv -1 \pmod 3$, cho $a = b = 1$. Đáp án 2.

Đáp án có thể khá lớn khi $t$ nhỏ: $n = 997, t = 1$ cần $k = 13$, với bộ $a = (1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 26, 12960)$. Các $a_i$ cũng có thể rất lớn: $n = 526, t = 829$ cần $k = 4$ với $a = (2, 3119, 6799443, 4684700580528)$. Vì vậy không thể giới hạn $a_i$ bằng một hằng số nhỏ rồi vét cạn.

!!! info "Kiểm chứng trên toàn bộ miền dữ liệu"
    Vì $n, t \le 1000$ nên chỉ có $10^6$ bộ dữ liệu. Nhóm biên soạn đã chạy bản C++ trên **toàn bộ** $10^6$ bộ: đáp án lớn nhất là 14, mỗi bộ chạy không quá khoảng 0,1 giây, và các phép tính với `__int128` không tràn ở bộ nào. Kết quả trùng với bản tìm kiếm không dùng mẹo duyệt ước (chậm hơn nhiều) trên 400 bộ ngẫu nhiên cộng toàn bộ $n, t \le 100$.

!!! warning "Bẫy thường gặp"
    - Nghĩ rằng đáp án luôn là $\lceil \log_{t+1} n \rceil$. Sai: $n = 29, t = 58$ có $\lceil \log_{59} 29 \rceil = 1$ nhưng đáp án là 4.
    - Giới hạn $a_i \le$ vài nghìn rồi vét: bỏ sót nghiệm vì $a_i$ thực tế có thể lên tới $10^{12}$.
    - Cận trên của $a$ tính bằng số thực: cộng thêm biên an toàn (lời giải cộng 2) để không cắt nhầm nghiệm khi $\left(\frac{a + t}{a}\right)^k$ đúng bằng $r$.

!!! note "Nếu viết bằng C++"
    $p$, $q$ và $p q t^2$ vượt `long long`, lời giải dùng `__int128` (có sẵn trong GCC/Clang, không cần header riêng). Bản Python dùng số nguyên lớn nên không lo tràn, nhưng chậm hơn: vài bộ khó nhất (như $n = 685, t = 821$) mất khoảng 1 giây trên máy kiểm thử, có thể vượt giới hạn 1 giây nếu chấm như bản đề trên VNOJ; bản C++ chạy dưới 0,11 giây với mọi bộ.

=== "Python"

    ```python title="dtask.py"
    --8<-- "bang-c/2021/20211121-de1/sol/dtask.py"
    ```

=== "C++"

    ```cpp title="dtask.cpp"
    --8<-- "bang-c/2021/20211121-de1/sol/dtask.cpp"
    ```

## 3. Xâu con

**Ý tưởng.** $r(s)^2$ là số **cặp** cách chọn $(I, J)$ (mỗi cách chọn là một dãy chỉ số tăng) cùng cho ra xâu con $s$. Vậy

$$f(S) = \sum_{\text{cặp } (I, J) \text{ cùng cho một xâu con}} |I|.$$

Hai dãy chỉ số $i_1 < \ldots < i_\ell$ và $j_1 < \ldots < j_\ell$ cho cùng một xâu khi $S[i_x] = S[j_x]$ với mọi $x$. Đếm theo cặp vị trí **cuối cùng** $(i, j)$ với $S[i] = S[j]$:

- $cnt[i][j] = 1 + \sum_{i' < i,\ j' < j} cnt[i'][j']$ (cặp chỉ gồm $(i, j)$, hoặc nối $(i, j)$ vào sau một cặp trước đó);
- $len[i][j] = cnt[i][j] + \sum_{i' < i,\ j' < j} len[i'][j']$ (mỗi cặp được nối dài thêm 1).

Đáp án là $\sum len[i][j]$. Hai tổng $\sum_{i' < i, j' < j}$ lấy bằng tổng tiền tố 2 chiều nên cả bài là $O(N^2)$, với $N = 200$ chỉ $4 \cdot 10^4$ ô.

Kiểm tra với $S = ABAB$: chương trình in 48, khớp ví dụ.

!!! warning "Bẫy thường gặp"
    - Sinh tất cả $2^N - 1$ xâu con chỉ qua được subtask $|S| \le 20$.
    - Trừ trong tổng tiền tố có thể ra số âm khi lấy modulo; C++ phải cộng thêm `MOD` trước khi `%`.

=== "Python"

    ```python title="subseq.py"
    --8<-- "bang-c/2021/20211121-de1/sol/subseq.py"
    ```

=== "C++"

    ```cpp title="subseq.cpp"
    --8<-- "bang-c/2021/20211121-de1/sol/subseq.cpp"
    ```

## 4. Cắt bánh

**Ý tưởng.** Bỏ các lần cắt trùng nhau và các lần cắt dọc theo cạnh bánh (hai đỉnh kề nhau), còn $D \le 1225$ đường cắt khác nhau. Thêm lần lượt từng đường cắt: nếu đường mới cắt các đường cũ tại $x$ điểm **phân biệt** bên trong bánh, nó đi qua $x + 1$ miếng và chia đôi mỗi miếng, nên số miếng tăng $x + 1$. Đáp án là $1 + \sum (x + 1)$.

- Hai dây cung $(i, j)$ và $(a, b)$ cắt nhau bên trong bánh khi và chỉ khi đầu mút xen kẽ: đúng một trong $a, b$ nằm giữa $i$ và $j$ (theo thứ tự đỉnh), và không chung đỉnh. Phần này dùng số nguyên nên chính xác.
- Để biết các giao điểm có trùng nhau không (nhiều đường cắt đồng quy, chuyện thường gặp ở đa giác đều), tính vị trí giao điểm trên đường mới dưới dạng tham số $t \in (0, 1)$, sắp xếp và đếm các giá trị khác nhau với sai số $10^{-9}$.

Ví dụ: hình vuông cắt theo đường chéo $1$–$3$ thì $x = 0$, số miếng $1 + 1 = 2$.

!!! info "Vì sao sai số $10^{-9}$ là an toàn"
    Nhóm biên soạn đã chạy cho mọi $n \le 50$ với **tất cả** đường chéo: hai giao điểm trùng nhau lệch nhau tối đa khoảng $4{,}4 \cdot 10^{-15}$ trên tham số $t$, còn hai giao điểm khác nhau cách nhau ít nhất khoảng $2{,}6 \cdot 10^{-6}$. Tập con đường cắt bất kỳ chỉ có ít giao điểm hơn nên khoảng cách này vẫn đúng. Số miếng khi cắt mọi đường chéo khớp dãy OEIS [A007678](https://oeis.org/A007678) với mọi $3 \le n \le 50$ (ví dụ $n = 50$ cho 220600 miếng).

!!! warning "Bẫy thường gặp"
    - Dùng công thức $1 + D + (\text{số cặp đường cắt nhau})$: chỉ đúng với 30% test không có ba đường đồng quy. Đa giác đều có rất nhiều điểm đồng quy (ví dụ ba đường chéo chính của lục giác đều).
    - Quên bỏ lần cắt trùng nhau hoặc ghi ngược (`3 1` và `1 3`), hoặc lần cắt dọc theo cạnh.
    - Đếm cả giao điểm tại đỉnh của bánh.

=== "Python"

    ```python title="cutcake.py"
    --8<-- "bang-c/2021/20211121-de1/sol/cutcake.py"
    ```

=== "C++"

    ```cpp title="cutcake.cpp"
    --8<-- "bang-c/2021/20211121-de1/sol/cutcake.cpp"
    ```
