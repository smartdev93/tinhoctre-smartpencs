# Đáp án - Bảng A Quận Thanh Khê 2022

Lời giải tham khảo bằng Python 3 và C++ (C++17), viết đơn giản để dễ chuyển sang Scratch. Xem lại [đề bài](index.md).

Mỗi chương trình đọc `input.inp` và ghi `output.out`. Nếu không có file `input.inp`, chương trình đọc từ bàn phím và in ra màn hình để tiện thử. (Đề gốc làm bằng Scratch, nhập từ bàn phím và in ra màn hình.)

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Chia quà | Phần dư của phép chia | $O(1)$ |
| 2 | Tổng 3K | Công thức số hạng của cấp số cộng | $O(1)$ |
| 3 | Màu chữ | Chu kỳ 17 chữ và chu kỳ 4 màu | $O(1)$ |
| 4 | Môi trường | Trò chơi Scratch điều khiển bằng phím | – |

---

## 1. Chia quà

**Ý tưởng.** Gọi $r = N \bmod M$.

- Nếu $r = 0$: chia đều được, in `0`.
- Ngược lại: cần mua thêm $M - r$ cuốn để số sách thành bội tiếp theo của $M$.

Ví dụ $N = 30, M = 8$: $30 \bmod 8 = 6$, cần thêm $8 - 6 = 2$ cuốn.

!!! warning "Bẫy thường gặp"
    - Dùng vòng lặp tăng dần số sách đến khi chia hết: đúng nhưng chậm khi $M$ lớn (đến $10^{12}$).
    - Quên trường hợp chia hết: in $M - 0 = M$ thay vì `0`.

!!! note "Nếu làm bằng Scratch hoặc C++"
    $N, M < 10^{12}$: trong Scratch dùng khối `phần dư của` (mod) vẫn chính xác với số cỡ này. C++ dùng `long long`.

=== "Python"

    ```python title="chiaqua.py"
    --8<-- "bang-a/2022/tk2022-de1/sol/chiaqua.py"
    ```

=== "C++"

    ```cpp title="chiaqua.cpp"
    --8<-- "bang-a/2022/tk2022-de1/sol/chiaqua.cpp"
    ```

## 2. Tổng 3K

**Ý tưởng.** Dãy 11, 14, 17, ... tăng đều 3 đơn vị, nên số hạng thứ $k$ là $a_k = 11 + 3(k - 1) = 3k + 8$. Tổng ba số hạng liên tiếp:

$$a_k + a_{k+1} + a_{k+2} = 3a_k + 9 = 9k + 33.$$

Kiểm tra với $k = 3$: $9 \cdot 3 + 33 = 60$.

!!! warning "Bẫy thường gặp"
    Dùng vòng lặp sinh từng số hạng đến số thứ $k$ chỉ qua được nhóm test $k < 100$; với $k$ đến $10^{12}$ phải dùng công thức.

!!! note "Nếu viết bằng C++"
    $k$ đến $10^{12}$ vượt `int`, nên đọc $k$ bằng `long long`.

=== "Python"

    ```python title="tong3k.py"
    --8<-- "bang-a/2022/tk2022-de1/sol/tong3k.py"
    ```

=== "C++"

    ```cpp title="tong3k.cpp"
    --8<-- "bang-a/2022/tk2022-de1/sol/tong3k.cpp"
    ```

## 3. Màu chữ

**Ý tưởng.** Bỏ dấu cách, dòng chữ là `TINHOCTRETHANHKHE` gồm 17 chữ cái, lặp lại liên tục. Màu lặp lại theo chu kỳ 4: Blue, Red, White, Yellow.

- Chữ thứ $k$ là chữ ở vị trí $(k - 1) \bmod 17$ (đếm từ 0) của `TINHOCTRETHANHKHE`.
- Màu thứ $k$ là màu ở vị trí $(k - 1) \bmod 4$ của danh sách màu.

Ví dụ $k = 23$: $(23 - 1) \bmod 17 = 5$ → `C`; $(23 - 1) \bmod 4 = 2$ → `White`.

!!! warning "Bẫy thường gặp"
    - Tính cả dấu cách vào chu kỳ (21 kí tự thay vì 17) sẽ sai ví dụ: dãy trong đề viết liền, không có dấu cách.
    - Trong Scratch, danh sách và `kí tự thứ ... của ...` đánh số từ 1, nên dùng $((k - 1) \bmod 17) + 1$.

!!! note "Nếu viết bằng C++"
    $k$ đến $10^{12}$ vượt `int`, nên đọc $k$ bằng `long long`.

=== "Python"

    ```python title="mauchu.py"
    --8<-- "bang-a/2022/tk2022-de1/sol/mauchu.py"
    ```

=== "C++"

    ```cpp title="mauchu.cpp"
    --8<-- "bang-a/2022/tk2022-de1/sol/mauchu.cpp"
    ```

## 4. Môi trường

!!! info "Bài thực hành ứng dụng"
    Bài làm sản phẩm Scratch (trò chơi điều khiển bằng phím), chấm theo sản phẩm, không có lời giải Python. Đề gốc trong nguồn bị cắt mất phần lớn mục "Yêu cầu", nên gợi ý dưới đây chỉ dựa trên phần đề còn đọc được.

**Gợi ý hướng làm.**

- Nhân vật: Robot, 3 thùng rác (NHỰA, THỦY TINH, GIẤY), các quả rác N, T, G.
- Robot: khi nhấn phím mũi tên thì `thay đổi x`/`thay đổi y` tương ứng; khi bấm lá cờ xanh đưa Robot về vị trí Xuất phát.
- Rác: khi Robot chạm vào rác thì rác `đi tới` Robot liên tục (Robot đang mang rác); khi rác chạm thùng đúng loại (theo chữ cái và màu trong hình, có thể hiểu N → NHỰA, T → THỦY TINH, G → GIẤY) thì rác biến mất và cộng điểm.
- Thời gian chơi 01 phút: dùng biến đếm ngược từ 60 (hoặc khối `đồng hồ bấm giờ`), hết giờ thì `dừng tất cả`.
