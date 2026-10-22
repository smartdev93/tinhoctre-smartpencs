# Đáp án - Bảng C Khu vực miền Nam 2022

Lời giải tham khảo bằng Python 3 và C++ (C++17). Xem lại [đề bài](index.md).

Đề chính thức đọc từ bàn phím và in ra màn hình. Để đồng bộ với các đề khác trên site, mỗi chương trình đọc `input.inp` và ghi `output.out` nếu có file `input.inp`; nếu không có file thì đọc từ bàn phím và in ra màn hình như đề yêu cầu.

| STT | Bài | Bảng | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- | --- |
| 1 | Bộ ba | C1, C2 | Với mỗi $x$, đếm $y$ trong một đoạn; gom các $x$ có cùng $\lfloor b_3/x \rfloor$ và $\lceil a_3/x \rceil$ | $O(\sqrt{a_3} + \sqrt{b_3})$ |
| 2 | Chọn cặp | C1, C2 | Tìm nhị phân ngưỡng $T$ (trọng số của cặp thứ $k$), đếm và cộng các cặp $\ge T$ bằng cây Fenwick | $O(n \log n \log V)$ |
| 3 | Chọn nhóm | C1 | $n \le 20$: vét cạn bitmask (chính xác). $n \le 200$: tìm kiếm cục bộ lặp (**heuristic**) | $O(2^n)$ / $O(\text{lần lặp} \cdot n)$ |
| 4 | Xe buýt | C2 | Nếu $b < a$: thử 2 trạm đặc biệt kề $x$ và 2 trạm kề $y$ | $O(n + q)$ |

---

## 1. Bộ ba

**Ý tưởng.** Với mỗi $x$ cố định thì $z = xy$, nên chỉ cần đếm $y$:

- $x = 0$: $z = 0$, cần $a_3 = 0$; khi đó mọi $y \in [a_2, b_2]$ đều được.
- $x \ge 1$: $a_3 \le xy \le b_3 \iff \lceil a_3/x \rceil \le y \le \lfloor b_3/x \rfloor$. Số $y$ hợp lệ là độ dài đoạn $[\max(a_2, \lceil a_3/x \rceil),\ \min(b_2, \lfloor b_3/x \rfloor)]$ (0 nếu đoạn rỗng).

Duyệt từng $x$ tới $10^9$ thì quá chậm. Nhưng $\lfloor b_3/x \rfloor$ chỉ nhận khoảng $2\sqrt{b_3}$ giá trị khác nhau, và các $x$ cùng giá trị nằm liền nhau: với $f = \lfloor b_3/x \rfloor > 0$, khối kéo dài tới $x' = \lfloor b_3/f \rfloor$. Tương tự $\lceil a_3/x \rceil = \lfloor (a_3-1)/x \rfloor + 1$. Trong một khối mà cả hai giá trị không đổi, số $y$ hợp lệ cũng không đổi, nên nhân với độ dài khối. Tổng số khối khoảng $2(\sqrt{a_3} + \sqrt{b_3}) \approx 1.3 \times 10^5$.

Ví dụ `6 8 4 5 27 35`: $x = 6$: $y \in [\max(4, 5), \min(5, 5)] = \{5\}$; $x = 7$: $y \in [4, 5]$; $x = 8$: $y \in [4, 4]$. Tổng $1 + 2 + 1 = 4$.

!!! warning "Bẫy thường gặp"
    - Quên trường hợp $x = 0$ (hoặc chia cho 0). Khi $a_1 = 0$, $a_3 = 0$ thì mọi $y$ đều ghép được với $x = 0$.
    - Quên trường hợp $y = 0$: khi $x > b_3$ thì $\lfloor b_3/x \rfloor = 0$, vẫn đếm được $y = 0$ nếu $a_2 = a_3 = 0$. Công thức đoạn ở trên tự xử lý được.
    - Subtask $a_1 = b_1$ chỉ cần một phép tính, nhưng lời giải chia khối đã bao luôn.

!!! note "Nếu viết bằng C++"
    Đáp án tới khoảng $(10^9 + 1)^2 \approx 10^{18}$, vẫn vừa `long long` (tối đa khoảng $9.2 \times 10^{18}$). Tích `(hi - lo + 1) * (end - x + 1)` cũng phải tính bằng `long long`.

=== "Python"

    ```python title="boba.py"
    --8<-- "bang-c/2022/kvmn2022-de1/sol/boba.py"
    ```

=== "C++"

    ```cpp title="boba.cpp"
    --8<-- "bang-c/2022/kvmn2022-de1/sol/boba.cpp"
    ```

## 2. Chọn cặp

**Ý tưởng.** Đặt tổng tiền tố $P_0 = 0$, $P_i = a_1 + \cdots + a_i$. Cặp $(l, r)$ ứng với cặp chỉ số $(i, j) = (l - 1, r)$, có trọng số $P_j - P_i$ và điều kiện độ dài thành $j - i \ge X$. Bài toán thành: lấy tổng $k$ giá trị $P_j - P_i$ lớn nhất trong các cặp $j - i \ge X$.

Vì $k$ tới $10^7$, không lấy từng cặp ra được. Thay vào đó tìm **ngưỡng** $T$ = trọng số của cặp lớn thứ $k$:

1. Hàm $\text{cnt}(T)$ = số cặp có trọng số $\ge T$. Duyệt $j$ từ $X$ tới $n$, đưa $P_{j-X}$ vào cây Fenwick (theo thứ hạng giá trị), rồi đếm số $P_i \le P_j - T$ đã có trong cây. Mất $O(n \log n)$.
2. $\text{cnt}(T)$ giảm khi $T$ tăng, nên tìm nhị phân $T$ lớn nhất có $\text{cnt}(T) \ge k$. Trọng số nằm trong $[-3 \times 10^{10}, 3 \times 10^{10}]$, cần khoảng 37 lần.
3. Tính thêm tổng trọng số các cặp $> T$ (cây Fenwick thứ hai lưu tổng $P_i$; mỗi $j$ góp $c \cdot P_j - \sum P_i$). Các cặp $> T$ đều được chọn, số cặp còn thiếu là $k - \text{cnt}(T+1)$, và chúng đều có trọng số đúng bằng $T$.

Đáp án $= \text{tổng}(> T) + (k - \text{cnt}(T + 1)) \cdot T$.

Ví dụ: $P = (0, 3, 5, -1, 7)$, $X = 2$. Các trọng số: $7, 5, 4, 2, -1, -4$. Với $k = 4$, ngưỡng $T = 2$; các cặp $> 2$ là $7, 5, 4$ (tổng 16), thiếu 1 cặp bằng 2. Đáp án $16 + 2 = 18$.

!!! warning "Bẫy thường gặp"
    - Dùng hàng đợi ưu tiên lấy từng cặp (kiểu bài "Super Piano") chạy $O((n + k) \log n)$: được các subtask $k \le 3 \times 10^5$, nhưng chậm với $k = 10^7$.
    - Nhiều cặp có cùng trọng số $T$: không được cộng tất cả các cặp $\ge T$, phải cộng đúng $k - \text{cnt}(T+1)$ lần $T$.
    - Điều kiện độ dài: cặp $(l, r)$ hợp lệ khi $r - (l - 1) \ge X$, tức là khi xét $j$ thì chỉ đưa vào cây các $P_i$ với $i \le j - X$.

!!! note "Nếu viết bằng C++"
    Trọng số tới $3 \times 10^{10}$ và đáp án tới $10^7 \cdot 3 \times 10^{10} = 3 \times 10^{17}$: dùng `long long` cho tổng tiền tố, cây Fenwick lưu tổng, và biến đếm. Lời giải C++ chạy các test lớn nhất ($n = 3 \times 10^5$) trong khoảng 0.8 đến 1 giây trên máy thử.

!!! info "Về tốc độ bản Python"
    Bản Python cùng thuật toán chạy khoảng 2 giây với $n = 5 \times 10^4$, nhưng khoảng 20 giây với $n = 3 \times 10^5$. Như vậy bản Python chỉ kịp các subtask $n \le 5 \times 10^4$; subtask lớn cần C++.

=== "Python"

    ```python title="choncap.py"
    --8<-- "bang-c/2022/kvmn2022-de1/sol/choncap.py"
    ```

=== "C++"

    ```cpp title="choncap.cpp"
    --8<-- "bang-c/2022/kvmn2022-de1/sol/choncap.cpp"
    ```

## 3. Chọn nhóm

Đây là bài **tối ưu tổ hợp khó** (tìm tập đỉnh có tổng trọng số cạnh bên trong lớn nhất, có cạnh âm; bài toán này NP-khó nói chung). Đề chấm theo tỉ lệ $\min\{1, c^3/q^3\}$ so với đáp án của Ban giám khảo, nên không cần tối ưu tuyệt đối để có điểm. Lời giải tham khảo gồm hai phần.

**Phần 1, $n \le 20$: vét cạn (chính xác).** Gọi $\text{val}[S]$ là tổng sự phối hợp của tập $S$. Với $v$ là học sinh có chỉ số lớn nhất trong $S$ và $R = S \setminus \{v\}$:

$$\text{val}[S] = \text{val}[R] + \sum_{u \in R} c(v, u)$$

Tổng $\sum_{u \in R} c(v, u)$ tra bảng: tách $R$ thành 10 bit thấp và 10 bit cao, mỗi phần lập sẵn bảng 1024 phần tử cho từng $v$. Tổng cộng $O(2^n + n \cdot 1024)$, khoảng $10^6$ phép tính. In tập có tổng lớn nhất.

**Phần 2, $n \le 200$: tìm kiếm cục bộ lặp (heuristic, KHÔNG đảm bảo tối ưu).**

- Giữ $\text{gain}[v] = \sum_{u \in S} c(v, u)$. Đổi trạng thái $v$ (thêm vào hoặc bỏ ra) làm tổng thay đổi $+\text{gain}[v]$ hoặc $-\text{gain}[v]$; cập nhật $\text{gain}$ mất $O(n)$.
- **Leo đồi:** lặp lại việc đổi trạng thái học sinh làm tổng tăng nhiều nhất, tới khi không còn bước nào làm tăng.
- **Nhiễu:** đổi trạng thái 1 tới 4 học sinh ngẫu nhiên rồi leo đồi lại; nếu kết quả tệ hơn trước khi nhiễu thì quay về trạng thái cũ. Cứ 500 lần thì khởi tạo lại từ một tập ngẫu nhiên. Tổng cộng 20000 lần, luôn ghi nhớ tập tốt nhất đã gặp.
- Bộ sinh số ngẫu nhiên là LCG 64 bit với seed cố định, viết giống hệt nhau ở hai bản, nên chạy lại luôn ra cùng kết quả và bản Python, C++ in ra **cùng một nhóm**.

Nhóm in ra luôn hợp lệ (chỉ số khác nhau, trong $[1, n]$) và tổng in ra đúng là tổng của nhóm đó. Nếu không tìm được nhóm có tổng dương, lời giải in nhóm chỉ gồm học sinh 1 (tổng 0).

Kết quả thử nghiệm của nhóm biên soạn: với 150 test ngẫu nhiên $12 \le n \le 20$, heuristic (chỉ chạy 1000 lần lặp) đều tìm được đúng tối ưu của vét cạn. Với $n = 200$, dạng test $c \in \{1, -10^9\}$ trên đồ thị đầy đủ thì đáp án đúng là $\binom{t}{2}$ với $t$ là clique lớn nhất của các cặp $+1$, nên so được với thuật toán tìm clique chính xác. Ở một test có 50% cặp $+1$, lời giải đạt đúng tối ưu (clique 11, tổng 55). Ở một test có 60% cặp $+1$, lời giải chỉ tìm được nhóm 13 người (tổng 78) trong khi tối ưu là 14 người (tổng 91), tỉ lệ $78/91 \approx 0.86$, tức là chỉ được khoảng 63% điểm test đó. Vậy lời giải **không tối ưu** ở các test lớn và có thể mất điểm đáng kể.

Ví dụ: các nhóm $\{1, 2, 5\}$ và $\{2, 5\}$ cùng có tổng 3 (lớn nhất). Lời giải tham khảo in `2` / `2 5`, khác ví dụ của đề nhưng cùng tổng nên cùng điểm.

!!! warning "Bẫy thường gặp"
    - Chỉ thêm học sinh mà không bao giờ bỏ ra: dễ kẹt ở nghiệm kém khi có cạnh âm lớn.
    - Subtask $c \in \{1, -10^9\}$: một cạnh $-10^9$ làm tổng âm ngay, nên thực chất là chọn tập không chứa cặp "xung khắc" nào và có nhiều cặp $+1$ nhất. Tìm kiếm cục bộ tự tránh các cặp này vì đổi trạng thái tạo ra cặp $-10^9$ không bao giờ làm tăng tổng.
    - Điểm tính theo lập phương tỉ lệ: đạt 90% tổng của giám khảo chỉ được khoảng 73% điểm test.

!!! note "Nếu viết bằng C++"
    Tổng tới $m \cdot 10^9 \approx 2 \times 10^{13}$, dùng `long long`. Bản C++ chạy 20000 lần lặp với $n = 200$ dưới 0.1 giây, bản Python khoảng 1.5 đến 2 giây. Với C++ có thể tăng số lần lặp (hoặc chạy theo thời gian) để kết quả tốt hơn, khi đó hai bản sẽ không còn in ra cùng nhóm.

=== "Python"

    ```python title="chonnhom.py"
    --8<-- "bang-c/2022/kvmn2022-de1/sol/chonnhom.py"
    ```

=== "C++"

    ```cpp title="chonnhom.cpp"
    --8<-- "bang-c/2022/kvmn2022-de1/sol/chonnhom.cpp"
    ```

## 4. Xe buýt

**Ý tưởng.** Đi xe thường giữa hai trạm $u, v$ bất kỳ mất $a|u - v|$, đi xe nhanh giữa hai trạm đặc biệt mất $b|u - v|$.

- Nếu $b \ge a$: xe nhanh không bao giờ rẻ hơn, đáp án $a|x - y|$.
- Nếu $b < a$: hành trình tốt nhất có dạng xe thường $x \to s$, xe nhanh $s \to u$, xe thường $u \to y$ ($s, u$ là trạm đặc biệt). Nhiều chặng xe nhanh liên tiếp gộp được thành một chặng (cùng giá $b$ mỗi đoạn), còn chen chặng xe thường vào giữa chỉ đắt hơn.

Với $u$ cố định, chi phí $a|x - s| + b|s - u|$ là hàm lồi theo $s$ và nhỏ nhất tại $s = x$ (vì $a > b$). Do đó trong các trạm đặc biệt, $s$ tốt nhất là trạm đặc biệt gần nhất bên trái hoặc bên phải $x$. Tương tự với $u$ và $y$. Chỉ cần thử $2 \times 2 = 4$ tổ hợp, cộng với phương án đi toàn xe thường.

Lập sẵn $\text{pre}[i]$ (trạm đặc biệt gần nhất $\le i$) và $\text{nxt}[i]$ (gần nhất $\ge i$) trong $O(n)$, mỗi câu hỏi trả lời $O(1)$.

Ví dụ: câu hỏi $1 \to 5$ với trạm đặc biệt $\{2, 4\}$, $a = 2$, $b = 1$: $s = 2$, $u = 4$, chi phí $2 \cdot 1 + 1 \cdot 2 + 2 \cdot 1 = 6$.

!!! warning "Bẫy thường gặp"
    - Chỉ thử trạm đặc biệt gần $x$ nhất về một phía: có thể cần đi lùi một chút để lên xe nhanh.
    - Chạy Dijkstra cho từng câu hỏi chỉ được các subtask $n, q \le 100$.
    - Các $p_i$ không chắc đã sắp xếp hay khác nhau; đánh dấu bằng mảng thì không cần quan tâm.

!!! note "Nếu viết bằng C++"
    Chi phí tới $10^6 \cdot 10^6 = 10^{12}$, dùng `long long`. Dữ liệu tới $3 \times 10^6$ số: bản C++ đọc bằng `fread` tự viết, vì `cin` của một số thư viện chuẩn (ví dụ libc++ trên macOS) mất khoảng 2.5 giây chỉ để đọc. Bản Python chạy test $n = m = q = 10^6$ khoảng 2.3 giây.

=== "Python"

    ```python title="xebuyt.py"
    --8<-- "bang-c/2022/kvmn2022-de1/sol/xebuyt.py"
    ```

=== "C++"

    ```cpp title="xebuyt.cpp"
    --8<-- "bang-c/2022/kvmn2022-de1/sol/xebuyt.cpp"
    ```
