# Đáp án - Bảng A TP Đà Nẵng 2019

Lời giải tham khảo bằng Python 3 và C++ (C++17) cho phần tính toán của Bài 2 và Bài 3, viết theo kiểu dễ chuyển sang Scratch. Bài 1, Bài 4 và phần vẽ của Bài 2 chỉ có gợi ý hướng làm. Xem lại [đề bài](index.md).

Chương trình đọc dữ liệu từ bàn phím và in kết quả ra màn hình, theo định dạng bổ sung ở trang đề.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Biển cấm đỗ xe ngày chẵn | Vẽ hình tròn tô màu, hình chữ nhật, nét chéo dày | – |
| 2 | Tính toán | Cộng dồn diện tích, cạnh tăng 20 mỗi lần | $O(n)$ |
| 3 | Bảng số | Duyệt danh sách một lần, đếm/cộng theo điều kiện | $O(n)$ |
| 4 | Trò chơi vui học toán | Nhiều nhân vật, biến đếm vòng, đồng hồ bấm giờ | – |

---

## 1. Biển cấm đỗ xe ngày chẵn

!!! info "Bài thực hành ứng dụng"
    Bài vẽ bằng Scratch, chấm theo sản phẩm, không có lời giải Python.

**Gợi ý hướng làm.**

- Hình tròn tô kín: đặt kích thước bút bằng 1 và vẽ nhiều đường tròn đồng tâm, hoặc đặt bút thật to (kích thước bút bằng đường kính) rồi chấm một điểm tại tâm. Vẽ hình tròn đỏ bán kính 100 trước, hình tròn xanh bán kính 90 sau.
- Hai hình chữ nhật trắng: rộng 10, dài $\frac{7}{5} \times 90 = 126$, đặt đứng song song, đối xứng qua tâm.
- Đường chéo đỏ: đặt kích thước bút 10, màu đỏ, xoay $45^\circ$ rồi kẻ một đoạn đi qua tâm, dài bằng đường kính hình tròn xanh (180).

## 2. Tính toán

**Ý tưởng.** Cạnh các hình vuông là $a, a + 20, a + 40, \ldots, a + 20(n - 1)$. Lặp $n$ lần: cộng `cạnh × cạnh` vào tổng, rồi tăng cạnh thêm 20.

Phần a) (vẽ hình) trong Scratch: trong cùng vòng lặp, đặt màu bút ngẫu nhiên (`đặt màu bút thành (lấy ngẫu nhiên từ 0 đến 100)`), vẽ hình vuông cạnh hiện tại bằng `lặp lại 4 [di chuyển (cạnh) bước, xoay 90 độ]`. Để các hình vuông lồng nhau và cùng tâm như Hình 2, trước mỗi hình vuông dịch điểm bắt đầu ra ngoài 10 bước theo cả hai chiều.

!!! warning "Bẫy thường gặp"
    - Cộng tổng các cạnh thay vì tổng diện tích.
    - Lặp $n + 1$ lần hoặc tăng cạnh trước khi cộng hình đầu tiên (bỏ mất hình vuông cạnh $a$).

=== "Python"

    ```python title="tinhtoan.py"
    --8<-- "bang-a/2019/dn2019-de1/sol/tinhtoan.py"
    ```

=== "C++"

    ```cpp title="tinhtoan.cpp"
    --8<-- "bang-a/2019/dn2019-de1/sol/tinhtoan.cpp"
    ```

## 3. Bảng số

**Ý tưởng.** Nhập $n$, rồi lặp $n$ lần, mỗi lần hỏi một số và thêm vào danh sách **Số**. Sau đó duyệt danh sách một lần:

- số lớn hơn 5 thì tăng biến đếm;
- số lớn hơn `lớn nhất` thì gán lại `lớn nhất` (khởi tạo bằng phần tử đầu tiên);
- số lẻ (chia 2 dư 1) thì cộng vào `tổng lẻ`, ngược lại tăng `đếm chẵn`.

Cuối cùng thêm 4 kết quả vào danh sách **Kết quả**.

!!! warning "Bẫy thường gặp"
    - Khởi tạo `lớn nhất` bằng 0 vẫn đúng ở bài này vì các số đều lớn hơn 0, nhưng khởi tạo bằng phần tử đầu tiên an toàn hơn.
    - Trong Scratch, phép chia lấy dư là khối `( ) chia lấy dư ( )` (`mod`).
    - Đề yêu cầu nhập các số lớn hơn 0; nếu muốn chặt chẽ, khi người dùng nhập số không lớn hơn 0 thì hỏi lại.

!!! note "Nếu viết bằng C++"
    Đề không giới hạn độ lớn các số. Lời giải C++ dùng `long long`, đủ khi tổng các số lẻ không vượt khoảng $9{,}2 \cdot 10^{18}$.

=== "Python"

    ```python title="bangso.py"
    --8<-- "bang-a/2019/dn2019-de1/sol/bangso.py"
    ```

=== "C++"

    ```cpp title="bangso.cpp"
    --8<-- "bang-a/2019/dn2019-de1/sol/bangso.cpp"
    ```

## 4. Trò chơi vui học toán

!!! info "Bài thực hành ứng dụng"
    Bài lập trình trò chơi bằng Scratch, chấm theo sản phẩm, không có lời giải Python.

**Gợi ý hướng làm.**

- Nhân vật: học sinh, giáo viên, bảng, phần quà. Biến: `vòng`, `số 1`, `số 2`, `loại phép tính`, `đáp án`.
- Khi bấm cờ xanh: `đặt lại đồng hồ`, `vòng = 1`, giấu phần quà.
- Mỗi vòng: hiện giáo viên và bảng; lấy ngẫu nhiên hai số từ 0 đến 20 và một loại phép tính (1: cộng, 2: trừ, 3: nhân); `hỏi` câu hỏi và `lặp lại cho đến khi` câu trả lời bằng đáp án đúng. Trả lời đúng thì giấu giáo viên và bảng, cho học sinh chạy từ mép trái sang mép phải (`lướt` hoặc lặp `di chuyển`), rồi đưa về mép trái và tăng `vòng`.
- Ở vòng 5: hiện phần quà ở cuối đường chạy; khi học sinh `chạm vào` phần quà thì `nói "Chiến thắng"`, ghi lại giá trị `đồng hồ bấm giờ` làm thời gian chơi và `dừng tất cả`.
- Phép trừ: có thể đổi chỗ hai số để kết quả không âm (phù hợp học sinh tiểu học).
