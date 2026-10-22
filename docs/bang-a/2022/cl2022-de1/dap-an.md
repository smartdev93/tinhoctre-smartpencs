# Đáp án - Bảng A Quận Cẩm Lệ 2022

Lời giải tham khảo bằng Python 3 và C++ (C++17). Xem lại [đề bài](index.md).

Đề gốc dành cho Scratch: nhập bằng câu hỏi (khối "hỏi và đợi") và trả lời bằng cách cho nhân vật nói. Các chương trình dưới đây đọc từ bàn phím và in ra màn hình, viết theo kiểu dễ chuyển sang Scratch.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Đếm kí tự số | Duyệt từng ký tự, đếm chữ số | $O(\text{len}(S))$ |
| 2 | Đổi quà | Cộng dồn 1 + 2 + … đến khi tổng ≥ k | $O(\sqrt{k})$ |
| 3 | Chinh phục đỉnh Olympia | Thiết kế trò chơi Scratch | – |

---

## 1. Đếm kí tự số

**Ý tưởng.** Duyệt lần lượt từng ký tự của chuỗi. Ký tự nào nằm trong khoảng `"0"` đến `"9"` thì tăng biến đếm lên 1.

Trong Scratch: dùng biến `i` chạy từ 1 đến `độ dài của (trả lời)`, lấy `ký tự thứ i của (trả lời)`, kiểm tra nó có phải chữ số không (ví dụ so với từng chữ số trong danh sách `0..9`, hoặc kiểm tra `"0123456789" chứa (ký tự)`).

!!! warning "Bẫy thường gặp"
    - Trong Scratch, phép so sánh `<` / `>` với chữ cái không phân biệt hoa thường và có thể so như số; cách an toàn là kiểm tra ký tự có nằm trong chuỗi `0123456789` hay không.
    - Chuỗi có thể chứa dấu cách, nên đọc cả dòng, không tách theo từ.

!!! note "Nếu viết bằng C++"
    Đọc cả dòng bằng `getline(cin, s)`, không dùng `cin >> s` (dừng ở dấu cách). Chữ có dấu (UTF-8) chiếm nhiều byte, nhưng không byte nào nằm trong khoảng `'0'..'9'`, nên đếm theo byte vẫn cho kết quả giống Python.

=== "Python"

    ```python title="demkituso.py"
    --8<-- "bang-a/2022/cl2022-de1/sol/demkituso.py"
    ```

=== "C++"

    ```cpp title="demkituso.cpp"
    --8<-- "bang-a/2022/cl2022-de1/sol/demkituso.cpp"
    ```

## 2. Đổi quà

**Ý tưởng.** Sau lần mua thứ n, tổng điểm là $1 + 2 + \dots + n$. Bắt đầu với `n = 1`, `tong = 1`; chừng nào `tong < k` thì tăng n và cộng thêm n vào tổng. Khi dừng, n là lần mua đầu tiên đủ điều kiện và `tong` là tổng điểm lúc đó.

Ví dụ $k = 10$: tổng lần lượt là 1, 3, 6, 10 → dừng ở $n = 4$, tổng $10$.

Vì tổng tăng như $n^2/2$, vòng lặp chỉ chạy khoảng $\sqrt{2k}$ lần.

!!! warning "Bẫy thường gặp"
    - Điều kiện là **lớn hơn hoặc bằng** k: với $k = 10$ phải dừng ở tổng 10, không đi tiếp đến 15.
    - In đúng thứ tự: n trước, tổng điểm sau. Trong Scratch dùng "nói (n) trong 3 giây" rồi "nói (tổng) trong 3 giây".

!!! note "Nếu viết bằng C++"
    Đề không ghi giới hạn của k. Lời giải C++ dùng `long long`, đủ cho $k \le 10^{18}$.

=== "Python"

    ```python title="doiqua.py"
    --8<-- "bang-a/2022/cl2022-de1/sol/doiqua.py"
    ```

=== "C++"

    ```cpp title="doiqua.cpp"
    --8<-- "bang-a/2022/cl2022-de1/sol/doiqua.cpp"
    ```

## 3. Chinh phục đỉnh Olympia

!!! info "Bài thực hành ứng dụng"
    Đây là bài thiết kế trò chơi bằng Scratch, không có lời giải Python. Dưới đây là gợi ý hướng làm.

**Gợi ý hướng làm.**

- **Nền:** vẽ đường đi có ô Xuất phát và đủ 10 ô tròn. Ghi lại tọa độ $(x, y)$ tâm từng ô vào hai danh sách `X` và `Y` (phần tử 1 là ô Xuất phát).
- **Nhân vật Sơn:** khi bấm lá cờ xanh, đặt biến `vi_tri = 1` và đi tới ô Xuất phát. Khi nhận tin nhắn "đúng", tăng `vi_tri` thêm 1 rồi lướt tới `(phần tử vi_tri của X, phần tử vi_tri của Y)`; nếu đã ở ô cuối thì không đi tiếp.
- **Nhân vật cô Hoa:** khi bấm lá cờ xanh, đặt lại đồng hồ bấm giờ. Lặp lại cho đến khi `đồng hồ bấm giờ > 60`:
    - đặt `a` và `b` là số ngẫu nhiên (ví dụ từ 0 đến 10; đề chỉ ghi "trong phạm vi 10");
    - hỏi `a + " + " + b + " = ?"` và đợi;
    - nếu `trả lời = a + b` thì phát tin nhắn "đúng", ngược lại báo sai và Sơn đứng yên.
- Hết 1 phút: thông báo kết thúc và dừng tất cả.

!!! note "Lưu ý"
    Khối "hỏi và đợi" sẽ chờ học sinh trả lời, nên nếu đang hỏi đúng lúc hết 60 giây thì trò chơi chỉ dừng sau khi trả lời xong. Muốn dừng đúng 1 phút, dùng thêm một kịch bản riêng: đợi đến khi `đồng hồ bấm giờ > 60` rồi "dừng tất cả".
