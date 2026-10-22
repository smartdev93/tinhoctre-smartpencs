# Đáp án - Bảng C Vòng khu vực 2021

Lời giải tham khảo bằng Python 3 và C++ (C++17). Xem lại [đề bài](index.md).

Đề chính thức đọc từ bàn phím và in ra màn hình. Để đồng bộ với các đề khác trên site, mỗi chương trình đọc `input.inp` và ghi `output.out` nếu có file `input.inp`; nếu không có thì đọc từ bàn phím và in ra màn hình như đề yêu cầu.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Số hoàn hảo | QHĐ theo vị trí, trạng thái là (tổng, tập tổng con) của các đoạn đang mở | $O(n \cdot k \cdot S)$, $S$ = số trạng thái |
| 2 | Thi đấu cầu lông | Tham lam: xét VĐV Trái đất tăng dần theo $a$, ghép với VĐV Z có $y$ lớn nhất còn thắng được | $O(Q \cdot n \log n)$ |
| 3 | Hoán vị không bất động | Đếm $u$ số áo bị cấm đứng yên, bao hàm - loại trừ | $O(m + T)$ |

---

## 1. Số hoàn hảo

**Nhận xét.** Điều kiện của một đoạn hoàn hảo chỉ phụ thuộc vào **tập hợp** (đa tập) 10 chữ số của đoạn: tổng bằng 20 và có nhóm con tổng bằng $20 / 2 = 10$. Thứ tự chữ số trong đoạn không quan trọng.

**Ý tưởng.** Duyệt các vị trí $i = 1 \ldots n$, mỗi vị trí chọn một chữ số $x \in [1, k]$. Với mỗi đoạn $[p_j, p_j + 9]$ đang "mở" (đã bắt đầu, chưa kết thúc) ta chỉ cần nhớ:

- $s$: tổng các chữ số đã chọn trong đoạn;
- $mask$: tập các tổng con đạt được, bit $t$ bật nếu chọn được một nhóm chữ số có tổng $t$. Thêm chữ số $x$: $mask \leftarrow mask \mid (mask \ll x)$. Chỉ cần giữ các bit $0..10$.

Trạng thái QHĐ là bộ $(s, mask)$ của mọi đoạn đang mở (tối đa 5 đoạn vì $m \le 5$), giá trị là số cách mod $D$.

- Tại vị trí $p_j$: mở đoạn mới với $(0, \{0\})$.
- Chọn chữ số $x$: cập nhật mọi đoạn đang mở, bỏ trạng thái có tổng vượt 20.
- Tại vị trí $p_j + 9$: đoạn mở sớm nhất kết thúc, chỉ giữ trạng thái có $s = 20$ và bit 10 của $mask$ bật, rồi xóa đoạn này khỏi trạng thái.
- Vị trí không thuộc đoạn nào: nhân số cách với $k$.

Số trạng thái thực tế rất nhỏ (vài nghìn). Trường hợp nặng nhất $n = 50$, $k = 9$, $p = 1, 2, 3, 4, 5$ chạy khoảng 0,3 giây bằng Python.

**Nhận xét thêm.** Duyệt hết mọi dãy 10 chữ số từ 1 đến 9 có tổng 20 (có $\binom{19}{9} - 100 = 92\,278$ dãy; 100 dãy bị loại là những dãy cần một "chữ số" 10 hoặc 11) thì thấy **dãy nào cũng chia được thành hai nhóm tổng 10**. Nghĩa là với chữ số từ 1 đến 9, điều kiện 2 của đề luôn đúng khi điều kiện 1 đúng. Lời giải vẫn giữ $mask$ để bám sát đề và để tự kiểm chứng, nhưng chỉ theo dõi tổng $s$ cũng cho cùng đáp án.

!!! warning "Bẫy thường gặp"
    - Hiểu "có $m$ đoạn hoàn hảo" thành "có **đúng** $m$ đoạn": ví dụ của đề cho đáp án 8, chỉ khớp khi các đoạn khác được phép hoàn hảo hay không tùy ý.
    - Các đoạn có thể chồng lên nhau ($p_{j+1} - p_j < 10$), nên không thể nhân độc lập số cách của từng đoạn. Chỉ khi các đoạn rời nhau thì đáp án mới là $V^m \cdot k^{n - 10m}$ với $V$ là số dãy 10 chữ số từ 1 đến $k$ tạo thành đoạn hoàn hảo.
    - $D$ có thể bằng 1, khi đó đáp án là 0.

!!! note "Nếu viết bằng C++"
    Số cách lấy mod $D \le 10^9$ và nhân với $k \le 9$, dùng `long long` là đủ. Trạng thái là `vector<int>`, mỗi phần tử mã hóa $s \cdot 2048 + mask$.

=== "Python"

    ```python title="pnum.py"
    --8<-- "bang-c/2021/20211010-de1/sol/pnum.py"
    ```

=== "C++"

    ```cpp title="pnum.cpp"
    --8<-- "bang-c/2021/20211010-de1/sol/pnum.cpp"
    ```

## 2. Thi đấu cầu lông

**Mô hình.** Mỗi truy vấn là bài toán ghép cặp cực đại trên đồ thị hai phía: VĐV Trái đất $i$ nối với VĐV Z $j$ khi $a_i > x_j$ và $b_i > y_j$. Các VĐV không thắng chắc được ghép tùy ý với những người còn lại, nên đáp án chính là kích thước ghép cặp cực đại. Với $n \le 6$ có thể thử mọi hoán vị, với $n \le 100$ dùng thuật toán ghép cặp Kuhn, nhưng $n = 30\,000$ cần tham lam.

**Tham lam.** Sắp VĐV Trái đất tăng dần theo $a$, sắp $n$ VĐV Z được cử tăng dần theo $x$. Duyệt VĐV Trái đất theo thứ tự đó:

1. Đưa vào tập "mở" mọi VĐV Z có $x < a_i$ (một con trỏ chạy trên dãy đã sắp).
2. Trong tập mở, tìm VĐV có $y$ **lớn nhất mà vẫn $< b_i$**. Có thì ghép, xóa khỏi tập, tăng đáp án.

**Vì sao đúng.** VĐV Z đã vào tập mở thì mọi VĐV Trái đất xét sau (có $a$ lớn hơn hoặc bằng) đều thắng được về thể lực, chỉ còn điều kiện $y < b$. Giữa các ứng viên có $y < b_i$, lấy ứng viên $y$ lớn nhất là an toàn: ai ở sau dùng được ứng viên đó thì cũng dùng được mọi ứng viên có $y$ nhỏ hơn còn lại. Lập luận đổi chỗ cho thấy luôn có một ghép cặp tối ưu chứa lựa chọn tham lam.

Ví dụ $k = 1$: Trái đất $(10,10), (20,20), (30,30)$; Z $(10,10), (20,20), (30,30)$. VĐV $(10, 10)$ không có ai mở. VĐV $(20, 20)$: mở $(10, 10)$, ghép. VĐV $(30, 30)$: mở thêm $(20, 20)$, ghép. Đáp án 2.

Tập mở cần thêm, tìm "phần tử lớn nhất nhỏ hơn $b$" và xóa: C++ dùng `multiset`, Python dùng cây Fenwick trên thứ hạng của $y$ (tìm phần tử thứ $c$ với $c$ là số phần tử mở có $y < b$).

!!! warning "Bẫy thường gặp"
    - Điều kiện thắng là **lớn hơn hẳn** ở cả hai chỉ số: dùng `lower_bound(b)` rồi lùi một bước (không dùng `upper_bound`), và chỉ mở VĐV Z có $x < a$ chứ không phải $x \le a$.
    - Ghép VĐV Trái đất với VĐV Z có $y$ **nhỏ nhất** là sai: nó "phí" một đối thủ dễ mà người sau có $b$ nhỏ cần đến.
    - Mỗi truy vấn sắp xếp lại $n$ VĐV Z của cửa sổ, tổng $O(Q \cdot n \log n) \approx 100 \cdot 30\,000 \cdot 15$ phép, ổn với C++.

!!! note "Python chậm ở subtask lớn nhất"
    Thuật toán giống bản C++ nhưng Python chạy test $n = 30\,000$, $m = 10^5$, $Q = 100$ mất khoảng 14 giây (bản C++ dưới 1 giây). Với $n \le 5000$ bản Python chạy khoảng 2 giây. Đề không ghi giới hạn thời gian; nếu thi bằng Python thì nhiều khả năng chỉ đạt 3 subtask đầu.

=== "Python"

    ```python title="badmi.py"
    --8<-- "bang-c/2021/20211010-de1/sol/badmi.py"
    ```

=== "C++"

    ```cpp title="badmi.cpp"
    --8<-- "bang-c/2021/20211010-de1/sol/badmi.cpp"
    ```

## 3. Hoán vị không bất động

**Ý tưởng.** Gọi $U$ là tập số áo thuộc ít nhất một đoạn, $u = |U|$. Cần đếm hoán vị $p$ của $1..m$ sao cho $p_i \ne i$ với mọi $i \in U$ (các số áo ngoài $U$ thì tự do).

Tính $u$ bằng mảng hiệu: `diff[L] += 1`, `diff[R + 1] -= 1`, cộng dồn, đếm vị trí có giá trị dương.

Bao hàm - loại trừ: gọi $A_i$ là tập hoán vị giữ nguyên $i$. Chọn $j$ vị trí trong $U$ bắt buộc đứng yên có $\binom{u}{j}$ cách, còn lại $(m - j)!$ hoán vị tùy ý:

$$\text{đáp án} = \sum_{j=0}^{u} (-1)^j \binom{u}{j} (m - j)!$$

Với ví dụ $m = 3$, $U = \{1, 2\}$: $3! - 2 \cdot 2! + 1 \cdot 1! = 6 - 4 + 1 = 3$.

Khi $u = m$ công thức thành số mất thứ tự (derangement) quen thuộc; khi $T = 0$ thì $u = 0$ và đáp án là $m!$.

Tính sẵn giai thừa và nghịch đảo giai thừa mod $10^9 + 7$ (dùng định lý Fermat nhỏ) để có $\binom{u}{j}$ trong $O(1)$.

!!! warning "Bẫy thường gặp"
    - Cộng độ dài các đoạn thay vì đếm hợp của chúng: các đoạn có thể giao nhau.
    - $T = 0$: không có dòng đoạn nào phía sau, đừng cố đọc thêm.
    - Số hạng mang dấu trừ: trong C++ cộng thêm $MOD$ trước khi lấy dư để không ra số âm.

!!! note "Nếu viết bằng C++"
    Tích hai số dưới $10^9 + 7$ vượt `int`, dùng `long long` và lấy mod sau mỗi phép nhân.

=== "Python"

    ```python title="permu.py"
    --8<-- "bang-c/2021/20211010-de1/sol/permu.py"
    ```

=== "C++"

    ```cpp title="permu.cpp"
    --8<-- "bang-c/2021/20211010-de1/sol/permu.cpp"
    ```
