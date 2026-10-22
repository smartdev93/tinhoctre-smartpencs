# Đáp án - Bảng A Quận Ngũ Hành Sơn 2019

Lời giải tham khảo bằng Python 3 và C++ (C++17) cho Bài 2, gợi ý hướng làm cho Bài 1 và Bài 3. Xem lại [đề bài](index.md).

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Viên gạch hoa | Thủ tục vẽ ngũ giác đều, lặp giảm cạnh 10, xoay quanh tâm | – |
| 2 | Tính | Thử mọi số có hai chữ số | $O(90)$ |
| 3 | Luyện gõ phím ở hàng cơ sở | Danh sách, ngẫu nhiên, đồng hồ bấm giờ | – |

---

## 1. Viên gạch hoa

!!! info "Bài vẽ Scratch"
    Bài chấm theo hình vẽ trong Scratch nên không có lời giải Python.

**Gợi ý hướng làm.**

* Vẽ hình vuông cạnh 250 có tâm ở giữa sân khấu.
* Tạo khối "ngũ giác đều" có tham số độ dài cạnh: lặp 5 lần (đi cạnh, quay 72 độ).
* Hình cơ sở: các ngũ giác đều lồng vào nhau, cạnh lớn nhất $250 / 4 = 62{,}5$, mỗi ngũ giác sau có cạnh nhỏ hơn 10 ($62{,}5$; $52{,}5$; $42{,}5$; ...). Xem hình cơ sở ở bản scan để biết các ngũ giác lồng nhau tại điểm nào và có bao nhiêu ngũ giác.
* Đặt hình cơ sở tại điểm chính giữa hình vuông, vẽ hình cơ sở rồi quay một góc và vẽ lại cho đến đủ một vòng (số lần lặp đếm theo hình mẫu).

## 2. Tính

**Ý tưởng.** Gọi số cần tìm là $x$ ($10 \le x \le 99$). Viết thêm chữ số 9 vào bên trái $x$ được số $900 + x$. Điều kiện: $900 + x = 16x$, tức $15x = 900$, $x = 60$.

Kiểm tra: $960 = 16 \times 60$.

Trong Scratch, cách dễ làm nhất là cho biến $x$ chạy từ 10 đến 99 và kiểm tra $900 + x = 16 \times x$, rồi cho nhân vật nói số tìm được.

!!! warning "Bẫy thường gặp"
    Viết thêm chữ số 9 vào **bên trái** số có hai chữ số là cộng thêm 900, không phải nhân 10 rồi cộng 9 (đó là viết vào bên phải).

=== "Python"

    ```python title="tinh.py"
    --8<-- "bang-a/2019/nhs2019-de1/sol/tinh.py"
    ```

=== "C++"

    ```cpp title="tinh.cpp"
    --8<-- "bang-a/2019/nhs2019-de1/sol/tinh.cpp"
    ```

## 3. Luyện gõ phím ở hàng cơ sở

!!! info "Bài thực hành ứng dụng"
    Bài làm trò chơi trong Scratch, chấm theo sản phẩm nên không có lời giải Python.

**Gợi ý hướng làm.**

* Tạo danh sách các chữ cái hàng cơ sở (a, s, d, f, g, h, j, k, l).
* Khi bấm lá cờ: mèo lần lượt nói 3 câu hướng dẫn.
* Nhân vật nút Start: khi được bấm thì phát tin "bắt đầu".
* Khi nhận "bắt đầu": đặt điểm = 0, đặt lại đồng hồ bấm giờ; lặp cho đến khi đồng hồ bấm giờ > 60: ghép 3 chữ cái lấy ngẫu nhiên từ danh sách thành cụm chữ, hỏi cụm chữ đó và đợi; nếu câu trả lời bằng cụm chữ thì cộng 10 điểm, ngược lại trừ 10 điểm.
* Hết giờ: mèo nói "Bạn được: (điểm) điểm".
