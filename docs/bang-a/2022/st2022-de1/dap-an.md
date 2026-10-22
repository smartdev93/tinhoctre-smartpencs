# Đáp án - Bảng A Quận Sơn Trà 2022

Lời giải tham khảo bằng Python 3 và C++ (C++17). Xem lại [đề bài](index.md).

Đề gốc nhập từ bàn phím và in ra màn hình. Mỗi chương trình dưới đây đọc `input.inp` và ghi `output.out` nếu có file `input.inp`; nếu không có thì đọc từ bàn phím và in ra màn hình như đề yêu cầu.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Bóng đèn | Chu vi chia khoảng cách: $8a$ | $O(1)$ |
| 2 | Biểu thức nhỏ nhất | $x$ nhỏ nhất, $y$ lớn nhất: $a - d$ | $O(1)$ |
| 3 | Không thích số 3 | Dãy lặp lại theo chu kỳ 30 (18 số mỗi chu kỳ) | $O(1)$ |
| 4 | Số cân bằng | Đếm theo số chữ số của nửa trái | $O(\log n)$ |

---

## 1. Bóng đèn

**Ý tưởng.** Đổi đơn vị: cạnh $a$ dm $= 10a$ cm, chu vi hình vuông $= 40a$ cm. Các bóng xếp thành một vòng khép kín, cứ 5 cm một bóng, nên số bóng bằng số khoảng: $40a / 5 = 8a$.

Kiểm tra: $a = 1$ → 8 bóng; $a = 3$ → 24 bóng.

!!! warning "Bẫy thường gặp"
    - Quên đổi dm sang cm.
    - Cộng thêm 1 bóng như bài trồng cây trên đoạn thẳng. Đây là đường khép kín nên số bóng bằng số khoảng.

=== "Python"

    ```python title="bongden.py"
    --8<-- "bang-a/2022/st2022-de1/sol/bongden.py"
    ```

=== "C++"

    ```cpp title="bongden.cpp"
    --8<-- "bang-a/2022/st2022-de1/sol/bongden.cpp"
    ```

## 2. Biểu thức nhỏ nhất

**Ý tưởng.** $x - y$ nhỏ nhất khi $x$ nhỏ nhất và $y$ lớn nhất, tức $x = a$, $y = d$. Đáp án là $a - d$.

Ví dụ: $a = 10, d = 7$ → $3$.

!!! warning "Bẫy thường gặp"
    - Duyệt mọi cặp $(x, y)$: với giá trị tới $10^{12}$ sẽ chạy mãi không xong.
    - Kết quả có thể âm (ví dụ $a = 1$, $d = 5$ → $-4$).

!!! note "Nếu viết bằng C++"
    Giá trị tới $10^{12}$ nên lời giải dùng `long long`.

=== "Python"

    ```python title="bieuthuc.py"
    --8<-- "bang-a/2022/st2022-de1/sol/bieuthuc.py"
    ```

=== "C++"

    ```cpp title="bieuthuc.cpp"
    --8<-- "bang-a/2022/st2022-de1/sol/bieuthuc.cpp"
    ```

## 3. Không thích số 3

**Ý tưởng.** Một số có được thích hay không chỉ phụ thuộc vào số dư khi chia cho 3 và chữ số tận cùng (số dư khi chia cho 10), nên dãy lặp lại theo chu kỳ $30$. Trong các số từ 1 đến 30 có 18 số được thích:

1, 2, 4, 5, 7, 8, 10, 11, 14, 16, 17, 19, 20, 22, 25, 26, 28, 29.

Số thứ $k$ là $30 \cdot \lfloor (k-1)/18 \rfloor + \text{mau}[(k-1) \bmod 18]$ (đánh số danh sách `mau` từ 0).

Ví dụ: $k = 9$ → nhóm 0, vị trí 8 → $14$. $k = 20$ → nhóm 1, vị trí 1 → $30 + 2 = 32$.

!!! warning "Bẫy thường gặp"
    - Duyệt từng số cho đến khi đếm đủ $k$ số: với $k = 10^9$ phải duyệt khoảng $1{,}67 \cdot 10^9$ số, quá chậm (đặc biệt trong Scratch). Cách duyệt chỉ đủ cho $k$ nhỏ.
    - Ví dụ 2 trong đề gốc ghi Output 17 là sai, đáp án đúng là 14.

=== "Python"

    ```python title="khongthich.py"
    --8<-- "bang-a/2022/st2022-de1/sol/khongthich.py"
    ```

=== "C++"

    ```cpp title="khongthich.cpp"
    --8<-- "bang-a/2022/st2022-de1/sol/khongthich.cpp"
    ```

## 4. Số cân bằng

**Ý tưởng.** Số cân bằng có $2L$ chữ số là số viết nửa trái $x$ ($x$ có đúng $L$ chữ số) hai lần liền nhau, tức bằng $x \cdot (10^L + 1)$. Ví dụ $12 \cdot 101 = 1212$.

Với mỗi $L = 1, 2, \dots$: $x$ chạy từ $10^{L-1}$ đến $\min(10^L - 1, \lfloor n / (10^L + 1) \rfloor)$; cộng số giá trị đó vào kết quả. Dừng khi số cân bằng nhỏ nhất có $2L$ chữ số đã vượt $n$. Với $n \le 10^{12}$ chỉ cần $L \le 6$.

Ví dụ $n = 1333$: $L = 1$ cho 9 số (11..99); $L = 2$: $\lfloor 1333/101 \rfloor = 13$ → $x = 10..13$, thêm 4 số. Tổng 13.

!!! warning "Bẫy thường gặp"
    - Duyệt mọi số từ 1 đến $n$ và kiểm tra: với $n = 10^{12}$ là quá chậm.
    - Một cách vừa đủ nhanh và dễ viết trong Scratch: cho $x$ chạy $1, 2, 3, \dots$, ghép $x$ với chính nó thành số cân bằng, dừng khi số đó vượt $n$ (tối đa khoảng $10^6$ lần lặp).

!!! note "Nếu viết bằng C++"
    $n$ tới $10^{12}$ nên lời giải dùng `long long`. Điều kiện dừng viết dạng `nho > n / he_so` thay cho `nho * he_so > n` để phép nhân không tràn số.

=== "Python"

    ```python title="socanbang.py"
    --8<-- "bang-a/2022/st2022-de1/sol/socanbang.py"
    ```

=== "C++"

    ```cpp title="socanbang.cpp"
    --8<-- "bang-a/2022/st2022-de1/sol/socanbang.cpp"
    ```
