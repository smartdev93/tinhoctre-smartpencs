# Đáp án - HSG Tin học THCS Quảng Ninh 2026

Lời giải tham khảo bằng Python 3 và C++ (C++17). Xem lại [đề bài](index.md).

Mỗi chương trình đọc và ghi đúng tên tệp đề yêu cầu (`sal.inp` / `sal.out`, `val.inp` / `val.out`, ...). Nếu không có tệp dữ liệu vào, chương trình đọc từ bàn phím và in ra màn hình để tiện thử.

| Bài | Tên bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Tiền công | Tính theo số tuần trọn vẹn, cộng thêm tối đa 6 ngày lẻ | $O(1)$ |
| 2 | Giá trị | Hai con trỏ, đếm số giá trị khác nhau trong cửa sổ | $O(n)$ |
| 3 | Dãy số | Quy hoạch động cái túi hai chiều, mỗi phần tử có 4 lựa chọn | $O(n \cdot k_1 \cdot k_2)$ |
| 4 | Số cặp | Với mỗi $i$, $\max a - \min b$ không giảm theo $j$; hai con trỏ + hàng đợi đơn điệu | $O(n)$ |

---

## 1. Tiền công

**Ý tưởng.** Mỗi tuần trọn vẹn (7 ngày liên tiếp, bắt đầu từ thứ nào cũng vậy) có đúng 5 ngày thường và 2 ngày cuối tuần, nên $\lfloor d / 7 \rfloor$ tuần đầu cho $\lfloor d / 7 \rfloor \cdot (5a + 2b)$ đồng. Còn lại $d \bmod 7 \le 6$ ngày, duyệt từng ngày bắt đầu từ thứ $k$: thứ 7 (thứ Bảy) và 8 (Chủ Nhật) được $b$, còn lại được $a$; sau thứ 8 quay về thứ 2.

Ví dụ 4: $k = 3$, $d = 12$. Một tuần trọn: $5 \cdot 1 + 2 \cdot 2 = 9$. Còn 5 ngày từ thứ Ba đến thứ Bảy: $4 \cdot 1 + 2 = 6$. Tổng $15$.

!!! warning "Bẫy thường gặp"
    - Quên quay vòng sau Chủ Nhật ($k = 8$ thì ngày kế tiếp là thứ Hai, mã 2).
    - Chỉ làm đúng ràng buộc 1 ($k = 2$, $d \le 5$, toàn ngày thường, đáp án $d \cdot a$) rồi quên trường hợp tổng quát.

=== "Python"

    ```python title="sal.py"
    --8<-- "hsg-thcs/2026/qn2026-de1/sol/sal.py"
    ```

=== "C++"

    ```cpp title="sal.cpp"
    --8<-- "hsg-thcs/2026/qn2026-de1/sol/sal.cpp"
    ```

## 2. Giá trị

**Ý tưởng.** Hai con trỏ (cửa sổ trượt). Duyệt đầu phải $r$, thêm $a_r$ vào cửa sổ và cập nhật `dem[v]` (số lần giá trị $v$ xuất hiện), `khac` (số giá trị khác nhau). Khi `khac > k` thì dịch đầu trái $l$ sang phải cho đến khi `khac` $\le k$. Lúc này $[l, r]$ là đoạn dài nhất kết thúc tại $r$ có không quá $k$ giá trị; nếu `khac == k` thì cập nhật đáp án.

Vì $l$ chỉ tăng, mỗi phần tử vào và ra cửa sổ tối đa một lần: $O(n)$.

Với $k = 1$, bài toán chính là tìm đoạn dài nhất gồm các số bằng nhau. Ràng buộc 1 (dãy không giảm, chỉ có 1 và 2) có thể đếm số lượng số 1 và số 2 rồi lấy max.

!!! warning "Bẫy thường gặp"
    - "Đúng $k$ giá trị" chứ không phải "không quá $k$": với $k = 2$, đoạn chỉ gồm một giá trị không được tính. Lời giải chỉ cập nhật khi `khac == k`.
    - Duyệt mọi cặp $(i, j)$ là $O(n^2) = 10^{10}$ phép, quá chậm với $n = 10^5$.

=== "Python"

    ```python title="val.py"
    --8<-- "hsg-thcs/2026/qn2026-de1/sol/val.py"
    ```

=== "C++"

    ```cpp title="val.cpp"
    --8<-- "hsg-thcs/2026/qn2026-de1/sol/val.cpp"
    ```

## 3. Dãy số

**Ý tưởng.** Mỗi phần tử $x$ chỉ có 4 kết cục, không phụ thuộc phần tử khác:

| Lựa chọn | Giá trị mới | Tốn |
| --- | --- | --- |
| Không làm gì | $x$ | 0 phép |
| Chỉ loại 1 | $\lfloor x / 2 \rfloor$ | 1 phép loại 1 |
| Chỉ loại 2 | $\max(x - b, 0)$ | 1 phép loại 2 |
| Cả hai | $\min\big(\max(\lfloor x/2 \rfloor - b, 0),\ \lfloor \max(x - b, 0) / 2 \rfloor\big)$ | 1 phép mỗi loại |

Ràng buộc duy nhất giữa các phần tử là tổng số phép mỗi loại, nên đây là bài **cái túi hai chiều**. Gọi $dp[j_1][j_2]$ là lượng giảm lớn nhất khi dùng tối đa $j_1$ phép loại 1 và $j_2$ phép loại 2 trên các phần tử đã xét. Thêm phần tử $x$ với lượng giảm $g_1, g_2, g_{12}$ của ba lựa chọn có làm gì đó:

$$
dp[j_1][j_2] = \max\big(dp[j_1][j_2],\ dp[j_1][j_2-1] + g_2,\ dp[j_1-1][j_2] + g_1,\ dp[j_1-1][j_2-1] + g_{12}\big)
$$

(vế phải dùng giá trị **trước** khi thêm $x$). Đáp án là $\sum a_i - dp[k_1][k_2]$. Khởi tạo toàn 0 vì "tối đa" cho phép không dùng hết số phép.

Với hai loại trên cùng một số, chia đôi trước rồi trừ luôn không tệ hơn (vì $b \ge 1$), nhưng lời giải lấy $\min$ của hai thứ tự cho chắc. Trong ví dụ 3, $a_1 = 19$: chia đôi trước $\to 9 \to 0$; trừ trước $\to 10 \to 5$.

Vì sao không tham lam: một phần tử lớn có thể đáng dùng cả hai phép, hoặc đáng để dành phép loại 1 cho số khác; thứ tự ưu tiên giữa hai loại phụ thuộc vào $b$ và cả dãy, nên phải xét hết bằng quy hoạch động.

Độ phức tạp $O(n \cdot k_1 \cdot k_2) \le 300^3 = 2{,}7 \cdot 10^7$, C++ chạy dưới 0,1 giây.

**Bản Python** cần thêm hai tối ưu để kịp 1 giây:

- Chỉ cập nhật các ô còn có thể dẫn tới $dp[k_1][k_2]$: sau phần tử thứ $i$ (đếm từ 0) còn $n - 1 - i$ phần tử, mỗi phần tử tăng $j_1$ tối đa 1, nên chỉ cần $j_1 \ge k_1 - (n - 1 - i)$; đồng thời $j_1 \le i + 1$. Tương tự với $j_2$. Số ô thực sự cập nhật giảm mạnh (khi $k_1 = k_2 = n$ chỉ còn 1 ô mỗi phần tử; trường hợp nặng nhất là khoảng $k_1 = k_2 = n/2$).
- Cập nhật cả một hàng bằng list comprehension (tính từ giá trị cũ rồi gán một lần), duyệt $j_1$ giảm dần để hàng $j_1 - 1$ vẫn là giá trị cũ.

Thử trên máy biên soạn với $n = 300$ và nhiều cặp $(k_1, k_2)$: bản Python chạy tối đa khoảng 0,45 giây (trường hợp $k_1 = k_2 = 150$), bản C++ khoảng 0,02 giây.

!!! warning "Bẫy thường gặp"
    - Quên lựa chọn "cả hai phép trên cùng một số" (ví dụ 3 cần dùng cả hai phép cho $a_1$).
    - Áp dụng một phép nhiều lần lên cùng một số: đề chỉ cho mỗi loại tối đa 1 lần trên mỗi $a_i$.
    - Duyệt $j_1, j_2$ tăng dần khi dùng mảng hai chiều: một phần tử bị dùng nhiều lần.

!!! note "Nếu viết bằng C++"
    Tổng dãy lên tới $300 \cdot 10^9 = 3 \cdot 10^{11}$, vượt `int`: dùng `long long` cho $a_i$, $b$, tổng và mảng $dp$.

=== "Python"

    ```python title="arr.py"
    --8<-- "hsg-thcs/2026/qn2026-de1/sol/arr.py"
    ```

=== "C++"

    ```cpp title="arr.cpp"
    --8<-- "hsg-thcs/2026/qn2026-de1/sol/arr.cpp"
    ```

## 4. Số cặp

**Ý tưởng.** Cố định đầu trái $i$, đặt $f_i(j) = \max(a_i..a_j) - \min(b_i..b_j)$. Khi $j$ tăng, $\max a$ không giảm và $\min b$ không tăng, nên $f_i(j)$ **không giảm** theo $j$. Vậy các $j$ có $f_i(j) = 0$ tạo thành một đoạn liên tiếp $[p_i, q_i)$, với:

- $p_i$ = vị trí $j \ge i$ đầu tiên có $f_i(j) \ge 0$,
- $q_i$ = vị trí $j \ge i$ đầu tiên có $f_i(j) > 0$ (hoặc $n$ nếu không có),

và đáp án là $\sum_i (q_i - p_i)$.

Khi $i$ tăng lên $i + 1$, đoạn $[i+1, j]$ nằm trong $[i, j]$ nên $\max a$ không tăng, $\min b$ không giảm, tức $f_{i+1}(j) \le f_i(j)$. Do đó $p_{i+1} \ge p_i$ và $q_{i+1} \ge q_i$: hai con trỏ chỉ chạy về phía trước. Mỗi con trỏ giữ cửa sổ $[i, p)$ (hoặc $[i, q)$) bằng hai **hàng đợi đơn điệu** (deque) để biết ngay $\max a$ và $\min b$ của cửa sổ. Mỗi chỉ số vào và ra mỗi deque tối đa một lần: tổng $O(n)$.

Cách khác cũng đạt: dựng sparse table cho max $a$ và min $b$, rồi với mỗi $i$ chặt nhị phân tìm $p_i$, $q_i$, độ phức tạp $O(n \log n)$; bản Python của cách này chậm hơn đáng kể.

Thử trên máy biên soạn với $n = 10^5$ (giá trị nhỏ nhiều trùng, toàn bằng nhau, dãy tăng, giá trị âm/dương lớn): bản Python khoảng 0,2 giây, bản C++ khoảng 0,1–0,3 giây (phần lớn là đọc dữ liệu).

!!! warning "Bẫy thường gặp"
    - Phần tử có thể **âm** ($1 \le |a_i|, |b_i| \le 10^9$): không khởi tạo max bằng 0.
    - Đáp án có thể tới $n(n+1)/2 \approx 5 \cdot 10^9$ (ví dụ hai dãy toàn số 7), vượt `int`.
    - Duyệt mọi cặp $(i, j)$ và cập nhật max/min dần là $O(n^2)$: chỉ đủ cho ràng buộc 1 và 2.

!!! note "Nếu viết bằng C++"
    Dùng `long long` cho biến đếm. Hiệu $\max a - \min b$ có thể tới $2 \cdot 10^9$, lời giải lưu $a$, $b$ bằng `long long` để không tràn khi trừ.

=== "Python"

    ```python title="pai.py"
    --8<-- "hsg-thcs/2026/qn2026-de1/sol/pai.py"
    ```

=== "C++"

    ```cpp title="pai.cpp"
    --8<-- "hsg-thcs/2026/qn2026-de1/sol/pai.cpp"
    ```
