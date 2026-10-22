# Đáp án - Bảng C Vòng sơ khảo 2022 (26/06/2022)

Lời giải tham khảo bằng Python 3 và C++ (C++17). Xem lại [đề bài](index.md).

Đề chính thức đọc từ bàn phím và in ra màn hình. Để đồng bộ với các đề khác trên site, mỗi chương trình đọc `input.inp` và ghi `output.out` nếu có file `input.inp`; nếu không có thì đọc từ bàn phím và in ra màn hình, đúng như đề yêu cầu.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Biến đổi xâu | Cây phân đoạn lười trên các khối 64 ký tự, nhãn là ánh xạ 26 chữ cái | $O(m \cdot (26 \log n + 64) + 26 \cdot n / 64 + n)$ |
| 2 | Ma trận | Thuật toán Freivalds: so sánh $A(A(Av))$ với $Bv$ cho vectơ ngẫu nhiên $v$, tính theo mô-đun $2^{61} - 1$ | $O(T \cdot n^2)$ |
| 3 | Cắt ghép xâu | Tham lam: lặp lại việc ghép đoạn chung dài nhất (băm xâu), thử 4 biến thể, lấy phương án tốt nhất | khoảng $O(n \log n)$ mỗi lượt độ dài |
| 4 | Dãy cấp số nhân | Quy hoạch động theo giá trị cuối và độ dài; dãy dài tối đa 30 phần tử | $O(30 \cdot n)$ |

---

## 1. Biến đổi xâu

**Ý tưởng.** Thao tác $(i, j, c_1, c_2)$ có thể xem là áp một **ánh xạ** $g$ trên 26 chữ cái lên mọi vị trí trong $[i, j]$: $g(c_1) = c_2$, các chữ khác giữ nguyên. Áp lần lượt nhiều thao tác lên cùng một vị trí tương đương áp **hợp** các ánh xạ, và hợp hai ánh xạ chỉ tốn 26 phép gán: $h(x) = g(f(x))$.

Vì vậy ta dùng cây phân đoạn lười (lazy segment tree): mỗi nút giữ một ánh xạ "chưa đẩy xuống". Gán thao tác cho một đoạn thì chỉ cần hợp $g$ vào $O(\log n)$ nút phủ đoạn đó. Thứ tự quan trọng: thao tác ở nút cha luôn mới hơn thao tác đang chờ ở nút con, nên trước khi gán phải đẩy (push) nhãn của các nút tổ tiên xuống, rồi khi đẩy thì áp nhãn cha **sau** nhãn con. Cuối cùng đẩy hết nhãn xuống lá và áp vào xâu.

Để giảm bộ nhớ và thời gian, lá của cây không phải từng ký tự mà là **khối 64 ký tự**. Khối chỉ bị phủ một phần ở hai đầu đoạn thì đẩy nhãn xuống khối đó, áp vào các ký tự, rồi sửa trực tiếp các ký tự trong đoạn (tối đa $2 \cdot 64$ ký tự mỗi thao tác). Bản Python dùng bảng dịch 256 byte và `bytes.translate` để hợp ánh xạ và sửa cả khối bằng code C của thư viện chuẩn.

Ví dụ: sau thao tác `0 2 a y`, đoạn $[0, 2]$ mang ánh xạ $a \to y$. Thao tác `1 3 a z` trên $[1, 3]$ hợp $a \to z$ sau đó, nhưng với vị trí 1, 2 thì ký tự lúc này là `y` (vì $a \to y$ đã áp trước) nên không đổi, chỉ vị trí 3 đổi `a` thành `z`.

!!! warning "Bẫy thường gặp"
    - Duyệt thẳng từng vị trí trong đoạn tốn $O(n \cdot m)$, tới $1.5 \cdot 10^{11}$ phép tính với test lớn nhất. Chỉ qua được 2 subtask đầu.
    - Hợp ánh xạ sai thứ tự: thao tác mới phải áp **sau** thao tác cũ. Với $g$: $a \to b$ rồi $h$: $b \to c$, chữ `a` phải thành `c`; đảo thứ tự thì `a` chỉ thành `b`.
    - Quên đẩy nhãn của nút tổ tiên trước khi gán nhãn mới cho nút con làm đảo thứ tự hai thao tác.
    - Subtask chỉ có `'a'`/`'b'` có lời giải riêng đơn giản hơn, nhưng lời giải tổng quát ở đây qua luôn subtask đó.

!!! note "Nếu viết bằng Python"
    Trên máy kiểm thử, bản C++ chạy test lớn nhất ($n = 10^6$, $m = 1.5 \cdot 10^5$) khoảng 0,55 giây, còn bản Python khoảng 3 giây, vượt giới hạn 1 giây. Bản Python đúng thuật toán nhưng có thể chỉ qua các subtask nhỏ.

=== "Python"

    ```python title="biendoixau.py"
    --8<-- "bang-c/2022/20220626-de1/sol/biendoixau.py"
    ```

=== "C++"

    ```cpp title="biendoixau.cpp"
    --8<-- "bang-c/2022/20220626-de1/sol/biendoixau.cpp"
    ```

## 2. Ma trận

**Ý tưởng (Freivalds).** Tính $A^3$ trực tiếp tốn $O(n^3)$, với $n = 500$ và $T = 20$ là $2 \cdot 20 \cdot 500^3 = 5 \cdot 10^9$ phép nhân, quá chậm. Thay vào đó chọn ngẫu nhiên vectơ $v$ và so sánh

$$A \cdot (A \cdot (A \cdot v)) \quad \text{với} \quad B \cdot v.$$

Mỗi phép nhân ma trận với vectơ chỉ tốn $O(n^2)$, tổng cộng 4 lần. Nếu $A^3 = B$ thì hai vế luôn bằng nhau. Nếu $A^3 \ne B$, gọi $D = A^3 - B \ne 0$, hai vế chỉ bằng nhau khi $Dv = 0$, xác suất rất nhỏ khi $v$ ngẫu nhiên.

Phần tử của $Bv$ có thể tới $500 \cdot 10^{18} \cdot |v_i|$, tràn `long long`, nên mọi phép tính lấy dư theo số nguyên tố $P = 2^{61} - 1 \approx 2.3 \cdot 10^{18}$ và chọn $v_i$ ngẫu nhiên trong $[0, P)$:

- Phần tử của $A^3$ có trị tuyệt đối không quá $n^2 \cdot 1000^3 = 2.5 \cdot 10^{14}$, của $B$ không quá $10^{18}$, nên $|d_{i,j}| < P$. Phần tử $d_{i,j} \ne 0$ thì vẫn khác 0 khi lấy dư $P$.
- Trên trường số dư theo $P$, với $D \ne 0$ và $v$ ngẫu nhiên đều, xác suất $Dv \equiv 0$ không quá $1/P$. Lời giải thử 2 lần cho mỗi bộ dữ liệu.

!!! warning "Bẫy thường gặp"
    - Nhân ma trận $O(n^3)$ chỉ qua subtask $n \le 10$.
    - Freivalds với $v$ gồm 0/1 và không lấy dư: $Bv$ tràn `long long` vì $|b_{i,j}|$ tới $10^{18}$.
    - Số âm khi lấy dư trong C++: `x % P` có thể âm, phải cộng thêm $P$.
    - Đọc dữ liệu: test lớn nhất có $20 \cdot 2 \cdot 500^2 = 10^7$ số, hơn 100 MB. `cin` thường không kịp 0,5 giây; bản C++ đọc bằng `fread`.

!!! note "Nếu viết bằng C++"
    Nhân hai số dư theo $2^{61} - 1$ cần `unsigned __int128` (có trên GCC/Clang). Trên máy kiểm thử, bản C++ chạy test 20 bộ $n = 500$ khoảng 0,15 giây; bản Python mất 3-7 giây (riêng việc đọc $10^7$ số đã quá 0,5 giây), nên Python chỉ hợp với subtask $n \le 10$.

=== "Python"

    ```python title="matran.py"
    --8<-- "bang-c/2022/20220626-de1/sol/matran.py"
    ```

=== "C++"

    ```cpp title="matran.cpp"
    --8<-- "bang-c/2022/20220626-de1/sol/matran.cpp"
    ```

## 3. Cắt ghép xâu

**Nhận xét.** Có cách cắt ghép khi và chỉ khi $S_1$ và $S_2$ có cùng tập ký tự (cùng độ dài, mỗi chữ cái xuất hiện cùng số lần): khi đó cắt $S_1$ thành từng ký tự là ghép được. Ngược lại in `-1`.

Tìm số đoạn **ít nhất** là bài toán phân hoạch xâu chung nhỏ nhất (Minimum Common String Partition), được biết là NP-khó, nên đề chấm theo tỉ lệ $\min\{1, q^5/c^5\}$ so với kết quả của Ban giám khảo. Lời giải tham khảo dùng **tham lam**, không bảo đảm tối ưu.

**Ý tưởng tham lam.** Lặp lại: tìm độ dài $L$ lớn nhất mà phần **chưa dùng** của $S_1$ và $S_2$ còn chung một đoạn độ dài $L$, rồi ghép cặp các đoạn đó và đánh dấu đã dùng.

- Kiểm tra "có đoạn chung độ dài $L$" bằng băm xâu (hash đa thức mô-đun $2^{61} - 1$): đưa giá trị băm của mọi cửa sổ độ dài $L$ chưa dùng của $S_1$ vào tập, rồi tra các cửa sổ của $S_2$. Mỗi lần kiểm tra $O(n)$.
- $L$ chỉ giảm dần qua các lượt nên tìm $L$ bằng cách dò lùi với bước nhân đôi rồi chặt nhị phân.
- Với $L$ đã chọn, duyệt các cửa sổ của $S_2$, mỗi cửa sổ còn trống thì ghép với một vị trí còn trống ở $S_1$ có cùng giá trị băm (so sánh trực tiếp để tránh trùng băm). Sau một lượt như vậy không còn cặp đoạn chung độ dài $L$ nào, sang $L$ nhỏ hơn.
- Bỏ hai đoạn giống nhau khỏi $S_1$ và $S_2$ thì phần còn lại vẫn cùng tập ký tự, nên đến $L = 1$ luôn ghép hết.
- Cuối cùng gộp hai đoạn liền nhau trong $S_1$ mà cũng liền nhau, đúng thứ tự trong $S_2$ (giảm thêm điểm cắt).

Kết quả tham lam phụ thuộc cách chọn khi có nhiều đoạn cùng độ dài, nên chạy 4 biến thể (duyệt $S_2$ từ trái hoặc từ phải; ưu tiên vị trí đầu tiên hoặc cuối cùng ở $S_1$) và lấy phương án ít đoạn nhất.

Với ví dụ `abcabc` / `aabbcc`: đoạn chung dài nhất có độ dài 2 (`ab`, `bc`), ghép xong hai đoạn đó còn lại `a`, `c`; tổng 4 đoạn, $c = 3$ bằng ví dụ của đề (cách cắt có thể khác).

!!! warning "Bẫy thường gặp"
    - Quên trường hợp `-1`: hai xâu khác độ dài hoặc khác số lần xuất hiện của một chữ cái.
    - In vị trí cắt sai quy ước: $p$ là "cắt sau ký tự thứ $p$", đánh số từ 1. Đoạn bắt đầu ở chỉ số $a$ (đánh số từ 0) ứng với vị trí cắt $p = a$.
    - Dòng thứ ba là thứ tự **ghép** các đoạn (đoạn nào đứng đầu $S_2$, rồi đoạn nào...), không phải vị trí của mỗi đoạn trong $S_2$.
    - Băm trùng giá trị: luôn so sánh thật hai đoạn trước khi ghép, nếu không có thể in phương án sai.

!!! note "Kết quả kiểm chứng"
    Trên 345 test ngẫu nhiên $|S_1| \le 9$ so với vét cạn mọi cách cắt, lời giải luôn in phương án hợp lệ, đạt tối ưu ở 337 test (8 test thừa 1 điểm cắt), điểm trung bình theo công thức của đề khoảng 98%. Với test $|S_1| = 10^4$ tạo bằng cách cắt $S_1$ tại 30 điểm rồi xáo trộn các đoạn, lời giải tìm được 32 điểm cắt, chỉ đạt khoảng $(30/32)^5 \approx 72\%$ số điểm của test đó nếu Ban giám khảo tìm ra 30 điểm cắt. Bản C++ chạy test lớn nhất trong khoảng 0,1-0,5 giây; bản Python 1-5 giây, có thể vượt giới hạn 1 giây ở subtask $10^4$.

=== "Python"

    ```python title="catghepxau.py"
    --8<-- "bang-c/2022/20220626-de1/sol/catghepxau.py"
    ```

=== "C++"

    ```cpp title="catghepxau.cpp"
    --8<-- "bang-c/2022/20220626-de1/sol/catghepxau.cpp"
    ```

## 4. Dãy cấp số nhân

**Nhận xét.** Vì $q \ge 2$ và $1 \le a_i \le 10^9 < 2^{30}$, một dãy cấp số nhân công bội $q$ trong dãy có tối đa $30$ phần tử (dài nhất là $1, 2, 4, \ldots, 2^{29}$). Lời giải dùng mảng độ dài 32 cho an toàn; mọi $k$ lớn hơn có đáp án 0.

**Ý tưởng (quy hoạch động).** Duyệt $a_1, a_2, \ldots$ theo thứ tự. Gọi $cnt[v][L]$ là số dãy con cấp số nhân độ dài $L$ **kết thúc bằng giá trị $v$** trong phần đã duyệt. Khi gặp $a_i = v$:

- $v$ tự nó là dãy độ dài 1;
- nếu $q \mid v$, mọi dãy độ dài $L - 1$ kết thúc bằng $v / q$ nối thêm $v$ thành dãy độ dài $L$: thêm $cnt[v/q][L-1]$ dãy.

Cộng các số mới vào $cnt[v][\cdot]$ và vào tổng $total[L]$. Lưu $cnt$ trong từ điển (`dict` / `unordered_map`) theo giá trị vì $a_i$ tới $10^9$.

Với ví dụ `1 2 8 4 2`, $q = 2$: gặp $2$ (vị trí 2) nối sau $1$ được 1 dãy độ dài 2; gặp $4$ nối sau các dãy kết thúc bằng 2 được $(2, 4)$ và $(1, 2, 4)$; gặp $2$ (vị trí 5) nối sau $1$ được thêm $(1, 2)$. Tổng: độ dài 2 có 3 dãy, độ dài 3 có 1 dãy.

!!! warning "Bẫy thường gặp"
    - Nối sai chiều: chỉ được nối $v$ vào sau dãy kết thúc bằng $v/q$ **đã xuất hiện trước** $v$. Duyệt theo thứ tự chỉ số và cập nhật $cnt[v]$ **sau** khi tính xong là đúng.
    - Tính $v \cdot q$ thay vì $v / q$ có thể tràn kiểu 32 bit ($10^9 \cdot 10^9$).
    - Phải in đủ $n - 1$ số, kể cả các số 0 với $k > 30$.
    - Hai phần tử bằng nhau ở hai vị trí khác nhau tạo hai dãy khác nhau (ví dụ có hai dãy $(1, 2)$).

=== "Python"

    ```python title="daycapsonhan.py"
    --8<-- "bang-c/2022/20220626-de1/sol/daycapsonhan.py"
    ```

=== "C++"

    ```cpp title="daycapsonhan.cpp"
    --8<-- "bang-c/2022/20220626-de1/sol/daycapsonhan.cpp"
    ```
