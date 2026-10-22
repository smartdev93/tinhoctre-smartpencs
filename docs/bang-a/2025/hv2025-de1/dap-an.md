# Đáp án - Bảng A Huyện Hòa Vang 2025

Lời giải tham khảo bằng Python 3 và C++ (C++17). Xem lại [đề bài](index.md).

Đề không yêu cầu đọc/ghi file, nên các chương trình đọc từ bàn phím và in ra màn hình. Lời giải viết theo kiểu dễ chuyển sang Scratch (vòng lặp, biến, không dùng thư viện).

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Trang trí | Bài vẽ Scratch: lặp vẽ $n \times n$ ô hoa văn | – |
| 2 | Tặng sữa | Mua gần tối đa số thùng, thử mọi số lốc cho phần tiền dư | $O(1)$ |
| 3 | Đồng phục | Duyệt chuỗi, cộng 2 / 3 / 4 theo cỡ áo | $O(N)$ |
| 4 | Từ vựng | Mỗi tuần trọn 27 từ, cộng thêm các ngày lẻ | $O(1)$ |

---

## 1. Trang trí

!!! info "Bài thực hành ứng dụng"
    Bài yêu cầu vẽ hình bằng Scratch (khối bút vẽ), không có lời giải Python.

**Gợi ý hướng làm.**

- Viết một khối tự định nghĩa vẽ **một ô** hoa văn tại vị trí hiện tại: một hình vuông và 4 cánh hoa hình lá hướng về 4 góc (mỗi cánh lá có thể vẽ bằng hai cung tròn đối xứng, mỗi cung là nhiều đoạn ngắn với góc quay nhỏ).
- Nhập $n$, dùng hai vòng lặp lồng nhau theo hàng và cột (mỗi vòng lặp $n$ lần) để gọi khối vẽ một ô tại từng vị trí, mỗi ô dịch đi một khoảng bằng cạnh ô.
- Chọn cạnh ô sao cho $n \times$ cạnh vừa với sân khấu (ví dụ chia cạnh khung hình cho $n$).
- Tô màu cánh hoa: đổi màu bút và vẽ nhiều nét sát nhau bên trong cánh, hoặc tăng độ dày bút.

## 2. Tặng sữa

**Ý tưởng.** Giá mỗi hộp: mua thùng $285 / 48 \approx 5{,}94$, mua lốc $25 / 4 = 6{,}25$, mua lẻ $7$ nghìn đồng. Thùng rẻ nhất nên mua tối đa $\lfloor N / 285 \rfloor$ thùng. Phần tiền dư nhỏ hơn 285, nên thử mọi số lốc ($0..11$) rồi mua lẻ bằng phần còn lại, lấy kết quả lớn nhất.

Vì sao không nên bớt thùng: 285 nghìn nếu không mua thùng thì chỉ mua được tối đa 45 hộp (11 lốc + 1 hộp lẻ), ít hơn 48 hộp. Lời giải vẫn thử bớt tới 5 thùng để chắc chắn; kết quả đã được đối chiếu với quy hoạch động (vét mọi cách mua) cho mọi $N$ đến 700 và 300 giá trị ngẫu nhiên đến 3000.

!!! warning "Bẫy thường gặp"
    - Với bộ giá của đề, tham lam cả ba bước (mua tối đa thùng, rồi tối đa lốc, rồi lẻ) cho kết quả đúng (đã đối chiếu với quy hoạch động đến $N = 3000$). Nhưng với bộ giá khác, tham lam có thể sai vì phần tiền dư bị lãng phí; thử mọi số lốc cho phần tiền dư là cách an toàn.
    - Duyệt hai vòng lặp lồng nhau theo số thùng và số lốc cho kết quả đúng nhưng chậm khi $N$ lớn.

!!! note "Nếu viết bằng C++"
    Đề không cho giới hạn $N$. Lời giải dùng `long long`; mọi giá trị trung gian không vượt $N$ nên chạy đúng với $N$ đến $10^{18}$.

=== "Python"

    ```python title="bai2.py"
    --8<-- "bang-a/2025/hv2025-de1/sol/bai2.py"
    ```

=== "C++"

    ```cpp title="bai2.cpp"
    --8<-- "bang-a/2025/hv2025-de1/sol/bai2.cpp"
    ```

## 3. Đồng phục

**Ý tưởng.** Duyệt từng ký tự của chuỗi: gặp `S` cộng 2, `M` cộng 3, `L` cộng 4.

!!! warning "Bẫy thường gặp"
    Chuỗi nhập vào có thể có khoảng trắng hoặc ký tự xuống dòng ở cuối; lời giải bỏ qua các ký tự không phải S, M, L.

=== "Python"

    ```python title="bai3.py"
    --8<-- "bang-a/2025/hv2025-de1/sol/bai3.py"
    ```

=== "C++"

    ```cpp title="bai3.cpp"
    --8<-- "bang-a/2025/hv2025-de1/sol/bai3.cpp"
    ```

## 4. Từ vựng

**Ý tưởng.** Quy ước thứ trong tuần theo đề: 0 = Chủ nhật, 2 = Thứ Hai, ..., 7 = Thứ Bảy. Ngày tiếp theo của 7 là 0, của 0 là 2, còn lại là cộng 1. Ngày Chủ nhật nhớ 0 từ, ngày thứ $K$ nhớ $K$ từ.

- Cứ 7 ngày liên tiếp thì đi đủ một vòng tuần, nhớ được $2 + 3 + 4 + 5 + 6 + 7 = 27$ từ.
- Vậy kết quả $= \lfloor N / 7 \rfloor \times 27$ cộng với số từ của $N \bmod 7$ ngày còn lại, bắt đầu từ ngày mai.

Ví dụ 2: $K = 2$, $N = 8$: một tuần trọn được 27 từ, ngày còn lại là ngày thứ 8 kể từ ngày mai, tức Thứ Ba (3 từ), tổng 30.

!!! warning "Bẫy thường gặp"
    - Ngày đầu tiên là **ngày mai**, không phải hôm nay.
    - Không có giá trị $K = 1$: sau Thứ Bảy (7) là Chủ nhật (0), sau Chủ nhật là Thứ Hai (2).

!!! note "Nếu viết bằng C++"
    Đề không cho giới hạn $N$. Kết quả khoảng $27N/7$ có thể vượt `int`, nên lời giải dùng `long long` (đúng với $N$ đến khoảng $2{,}3 \cdot 10^{18}$).

=== "Python"

    ```python title="bai4.py"
    --8<-- "bang-a/2025/hv2025-de1/sol/bai4.py"
    ```

=== "C++"

    ```cpp title="bai4.cpp"
    --8<-- "bang-a/2025/hv2025-de1/sol/bai4.cpp"
    ```
