# Đáp án - Bảng A TP Đà Nẵng 2022

Lời giải tham khảo bằng Python 3 và C++ (C++17). Xem lại [đề bài](index.md).

Đề gốc nhập từ bàn phím và in ra màn hình. Mỗi chương trình dưới đây đọc `input.inp` và ghi `output.out` nếu có file `input.inp`; nếu không có thì đọc từ bàn phím và in ra màn hình như đề yêu cầu. Code viết theo kiểu dễ chuyển sang Scratch.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Tổng dãy số | Tổng các bội của $k$: $k \cdot m(m+1)/2$ với $m = \lfloor n/k \rfloor$ | $O(1)$ |
| 2 | Đếm số ký tự | Đếm trong 1 lần lặp (26 ký tự), nhân số lần lặp, cộng phần dư | $O(26)$ |
| 3 | Tam giác số | Hàng $n$ là các số liên tiếp từ $(n-1)^2 + 1$ đến $n^2$ | $O(1)$ |
| 4 | Luyện phép toán | Bài thực hành ứng dụng (trò chơi Scratch) | – |

---

## 1. Tổng dãy số

**Ý tưởng.** Các số chia hết cho $k$ trong đoạn $[1, n]$ là $k, 2k, \dots, mk$ với $m = \lfloor n / k \rfloor$. Tổng của chúng là

$$S = k \cdot (1 + 2 + \dots + m) = k \cdot \frac{m(m+1)}{2}.$$

Ví dụ $n = 20, k = 3$: $m = 6$, $S = 3 \cdot 21 = 63$.

!!! warning "Bẫy thường gặp"
    - Duyệt từ 1 đến $n$ và cộng các số chia hết cho $k$ là đúng nhưng với $n = 10^9$ phải lặp một tỉ lần, quá giới hạn 5 giây (đặc biệt trên Scratch). Nếu muốn dùng vòng lặp thì lặp theo bước $k$ cũng vẫn tới $10^9$ lần khi $k = 1$; nên dùng công thức.
    - Kết quả lớn nhất khoảng $5 \cdot 10^{17}$ ($n = 10^9, k = 1$). Python không bị tràn số. Scratch lưu số dạng số thực, chỉ chính xác tuyệt đối đến khoảng $9 \cdot 10^{15}$, nên với $n$ rất lớn kết quả trên Scratch có thể lệch ở các chữ số cuối.

!!! note "Nếu viết bằng C++"
    Lời giải C++ dùng `long long` và tính `m * (m + 1) / 2` trước rồi mới nhân `k`, nên không tràn (kết quả lớn nhất khoảng $5 \cdot 10^{17}$).

=== "Python"

    ```python title="bai1.py"
    --8<-- "bang-a/2022/dn2022-de1/sol/bai1.py"
    ```

=== "C++"

    ```cpp title="bai1.cpp"
    --8<-- "bang-a/2022/dn2022-de1/sol/bai1.cpp"
    ```

## 2. Đếm số ký tự

**Ý tưởng.** Dòng chữ không dấu cách `HOITHITINHOCTRECAPTHANHPHO` dài 26 ký tự và lặp lại liên tục. Gọi $c$ là số lần ký tự $ch$ xuất hiện trong 26 ký tự này. Trong $n$ ký tự đầu có $\lfloor n / 26 \rfloor$ lần lặp đầy đủ, cộng thêm $n \bmod 26$ ký tự đầu của lần lặp tiếp theo:

$$\text{kết quả} = \lfloor n/26 \rfloor \cdot c + (\text{số } ch \text{ trong } n \bmod 26 \text{ ký tự đầu}).$$

Ví dụ $n = 40$, $ch = $ 'O': dòng chữ có $c = 3$ chữ O; $40 = 1 \cdot 26 + 14$, trong 14 ký tự đầu `HOITHITINHOCTR` có 2 chữ O. Kết quả $3 + 2 = 5$.

!!! warning "Bẫy thường gặp"
    - Quên bỏ dấu cách: dòng chữ trong đề có dấu cách nhưng dãy ký tự thì không.
    - Ví dụ trong đề bản in ghi 4, bản scan đã được sửa bằng bút đỏ thành 5; đáp án đúng là **5**.
    - Tạo cả dãy dài $n$ ký tự rồi đếm vẫn đúng, nhưng với $n = 10^7$ trên Scratch sẽ rất chậm.

=== "Python"

    ```python title="bai2.py"
    --8<-- "bang-a/2022/dn2022-de1/sol/bai2.py"
    ```

=== "C++"

    ```cpp title="bai2.cpp"
    --8<-- "bang-a/2022/dn2022-de1/sol/bai2.cpp"
    ```

## 3. Tam giác số

**Ý tưởng.** Hàng $i$ có $2i - 1$ số. Tổng số lượng số của $n$ hàng đầu là $1 + 3 + \dots + (2n-1) = n^2$, nên hàng $n$ kết thúc bằng số $n^2$ và bắt đầu bằng $(n-1)^2 + 1$. Tổng các số liên tiếp:

$$S = \frac{\big((n-1)^2 + 1 + n^2\big) \cdot (2n - 1)}{2} = (2n - 1)(n^2 - n + 1).$$

Kiểm tra $n = 4$: hàng 4 từ 10 đến 16, $S = (10 + 16) \cdot 7 / 2 = 91$.

!!! warning "Bẫy thường gặp"
    - Với $n = 10^7$, $S \approx 2 \cdot 10^{21}$. Python tính chính xác (kết quả `1999999700000029999999`). Scratch chỉ chính xác đến khoảng $9 \cdot 10^{15}$, nên với $n$ lớn hơn khoảng $1{,}6 \cdot 10^5$ Scratch sẽ in kết quả làm tròn (dạng số thực).
    - Cộng từng số của hàng $n$ bằng vòng lặp cần $2n - 1 \approx 2 \cdot 10^7$ lần, chậm trên Scratch.

!!! note "Nếu viết bằng C++"
    $S$ có thể vượt `long long` (khoảng $9{,}2 \cdot 10^{18}$) khi $n$ lớn hơn khoảng $1{,}6 \cdot 10^6$. Lời giải C++ tính bằng `__int128` (có sẵn trong GCC/Clang) và tự viết hàm `to_str` để in, vì `cout` không in trực tiếp được `__int128`.

=== "Python"

    ```python title="bai3.py"
    --8<-- "bang-a/2022/dn2022-de1/sol/bai3.py"
    ```

=== "C++"

    ```cpp title="bai3.cpp"
    --8<-- "bang-a/2022/dn2022-de1/sol/bai3.cpp"
    ```

## 4. Trò chơi: Luyện phép toán

!!! info "Bài thực hành ứng dụng"
    Đây là bài thiết kế trò chơi trên Scratch, không có lời giải Python. Dưới đây chỉ là gợi ý hướng làm.

**Gợi ý hướng làm.**

- Chọn nền *Backdrops 3* (theo đề) và nhân vật *Balloon1*. Tạo các biến `Score`, `Time`, `a`, `b`, `phep`, `dap_an`.
- Đồng hồ: khi bấm lá cờ, đặt `Time = 60`, lặp `đợi 1 giây` rồi giảm `Time` 1 đến khi `Time = 0`; khi đó phát tin "hết giờ", dừng trò chơi và cho quả bóng nói "Số điểm của bạn là: ..." (như hình minh họa).
- Mỗi câu hỏi: chọn ngẫu nhiên `a`, `b` trong 0..100 và chọn ngẫu nhiên cộng hay trừ. Với phép trừ, nếu `a` không lớn hơn `b` thì đổi chỗ hoặc chọn lại cho đến khi `a > b`. Tính sẵn `dap_an`. Đổi hiệu ứng màu của quả bóng, đặt bóng ở đáy màn hình rồi cho bóng bay dần lên.
- Dùng khối `hỏi ... và đợi` để hiện ô nhập câu trả lời. So sánh `trả lời` với `dap_an`: đúng thì `Score` tăng 3; sai thì giảm 1 chỉ khi `Score > 0`. Sau đó ẩn bóng và sang câu hỏi mới.
- Nếu bóng chạm cạnh trên trước khi trả lời thì cũng ẩn bóng và sang câu mới. Lưu ý khối `hỏi và đợi` dừng script đang chạy, nên phần bay lên của bóng cần chạy ở một script riêng (ví dụ nhận tin "câu mới" thì bay lên).
