# Đáp án - Bảng A TP Đà Nẵng 2020

Gợi ý hướng làm. Xem lại [đề bài](index.md).

Cả 4 bài của đề đều là bài thực hành trên Scratch (vẽ hình, thiết kế trò chơi), nên **không có lời giải Python**. Phần dưới đây là gợi ý hướng làm và các phép tính cần thiết.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Cờ Gánh | Vẽ lưới 4 × 4 có đường chéo; tạo bản sao quân cờ tại các giao điểm | – |
| 2 | Mảnh ghép | Bộ 7 mảnh (tangram) trong hình vuông 200; tính độ dài cạnh từng mảnh | – |
| 3 | Tô màu | Tối đa 9 hình chữ L, diện tích không tô 25 200 | – |
| 4 | Trò chơi: Bảo vệ biển đảo | Xoay pháo, bắn bản sao viên đạn, tàu địch ngẫu nhiên, biến điểm | – |

---

## 1. Cờ Gánh

!!! info "Bài thực hành ứng dụng"
    Bài vẽ hình và sắp xếp nhân vật trong Scratch, không có lời giải Python.

**Gợi ý hướng làm.**

- Bàn cờ có 4 × 4 ô vuông cạnh 75, tức là hình vuông lớn cạnh $4 \times 75 = 300$, lưới 5 × 5 giao điểm.
- Vẽ 16 ô vuông bằng 2 vòng lặp lồng nhau (hàng, cột), mỗi ô: `lặp lại 4 [di chuyển 75, xoay 90 độ]`. Hai đường chéo của mỗi ô dài $75\sqrt{2}$ (công thức ở cuối đề), hoặc dùng `lướt đến x, y` từ góc này đến góc đối diện.
- Quân cờ: 2 nhân vật (quân đen, quân sáng viền đen). Dùng vòng lặp `đi tới x, y` của từng giao điểm rồi `tạo bản sao của chính tôi`: 10 quân đen ở 2 hàng giao điểm trên cùng, 10 quân sáng ở 2 hàng dưới cùng (như hình H2).

---

## 2. Mảnh ghép

!!! info "Bài thực hành ứng dụng"
    Bài vẽ hình trong Scratch, không có lời giải Python.

**Kích thước các mảnh.** Hình H3 trên bản scan là bộ 7 mảnh ghép kiểu tangram. Với bộ tangram chuẩn ghép thành hình vuông cạnh 200 (đường chéo $200\sqrt{2}$), các mảnh có kích thước:

| Mảnh | Số lượng | Kích thước | Diện tích mỗi mảnh |
| --- | ---: | --- | ---: |
| Tam giác vuông cân lớn | 2 | cạnh góc vuông $100\sqrt{2}$, cạnh huyền 200 | 10 000 |
| Tam giác vuông cân vừa | 1 | cạnh góc vuông 100, cạnh huyền $100\sqrt{2}$ | 5 000 |
| Tam giác vuông cân nhỏ | 2 | cạnh góc vuông $50\sqrt{2}$, cạnh huyền 100 | 2 500 |
| Hình vuông | 1 | cạnh $50\sqrt{2}$ | 5 000 |
| Hình bình hành | 1 | cạnh 100 và $50\sqrt{2}$, góc 45° | 5 000 |

Tổng diện tích $2 \cdot 10000 + 5000 + 2 \cdot 2500 + 5000 + 5000 = 40000 = 200^2$.

!!! note "Lưu ý"
    Bảng trên dựa trên bộ tangram chuẩn; ảnh chụp đề mờ nên hãy đối chiếu cách chia trong hình H3 ở [bản scan](index.md#de-goc-ban-scan).

**Gợi ý hướng làm.**

- Viết các khối lệnh tự định nghĩa có tham số: `tam giác vuông cân (cạnh góc vuông)`, `hình vuông (cạnh)`, `hình bình hành (cạnh 1) (cạnh 2)`. Ví dụ tam giác vuông cân cạnh góc vuông $a$: đi $a$, xoay 135°, đi $a\sqrt{2}$, xoay 135°, đi $a$.
- Vẽ H3: đặt từng mảnh vào đúng vị trí và hướng trong hình vuông 200, mỗi mảnh một màu.
- Vẽ H4: dùng lại đúng các khối lệnh trên, chỉ thay vị trí bắt đầu và hướng xoay của từng mảnh theo hình H4.

---

## 3. Tô màu

!!! info "Bài thực hành ứng dụng"
    Bài vẽ và tô màu trong Scratch kèm câu hỏi suy luận, không có lời giải Python cho thí sinh.

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    Theo bản scan, mỗi hình H6/H7 là chữ L gồm **4 ô**. "Theo nhiều hướng khác nhau" được hiểu là được xoay chữ L (H6) và chữ L ngược (H7) theo mọi hướng, tức là cả 8 cách đặt. Hai hình được phép chạm nhau ở góc ô, chỉ không được có chung một cạnh ô vuông.

**Đáp số: tối đa 9 hình.** Một cách tô cụ thể (mỗi chữ cái là một hình, dấu `.` là ô không tô):

```
AAA.BBB.
..A...B.
CC.DDD.E
C.F..D.E
C.F.G.EE
.FF.G...
H..GG..I
HHH..III
```

Phần không được tô gồm $64 - 9 \times 4 = 28$ ô, mỗi ô có diện tích $30 \times 30 = 900$, nên **diện tích phần không được tô màu là $28 \times 900 = 25\,200$** (đơn vị diện tích).

!!! note "Kiểm chứng"
    Con số 9 được nhóm biên soạn kiểm tra bằng chương trình vét cạn (duyệt mọi cách đặt chữ L 4 ô theo 8 hướng trên lưới 8 × 8, cắt nhánh khi số ô còn trống không đủ). Chương trình vét cạn được đối chiếu với một cách vét cạn khác trên lưới 3 × 3 đến 6 × 6 và cho cùng kết quả. Không đặt được 10 hình.

**Gợi ý hướng làm.**

- Vẽ lưới 8 × 8 ô cạnh 30 bằng 2 vòng lặp lồng nhau (hoặc vẽ 9 đường ngang và 9 đường dọc dài 240).
- Viết khối lệnh `tô ô (hàng) (cột)` tô kín một ô (ví dụ đặt cỡ bút 30 và vẽ một đoạn ngắn ở giữa ô, hoặc vẽ nhiều đường song song). Mỗi hình chữ L là 4 lần gọi khối này.
- Tính diện tích phần không tô bằng biến: `64 × 30 × 30 − số_hình × 4 × 30 × 30`.

---

## 4. Trò chơi: Bảo vệ biển đảo

!!! info "Bài thực hành ứng dụng"
    Bài thiết kế trò chơi trên Scratch, không có lời giải Python.

**Gợi ý hướng làm.**

- Phông nền: đất liền, biển, cây (tự vẽ). Nhân vật: Pháo, Đạn, Đảo, Tàu địch.
- Pháo: `khi bấm phím mũi tên phải` → `xoay phải 15 độ`; `khi bấm phím mũi tên trái` → `xoay trái 15 độ`; `khi bấm phím Space` → phát tin "bắn".
- Đạn: nhận tin "bắn" thì `tạo bản sao`; bản sao đi tới vị trí pháo, `hướng về` theo hướng của pháo (`hướng của Pháo` trong khối cảm biến), rồi lặp di chuyển đến khi chạm cạnh hoặc chạm tàu địch thì xóa bản sao.
- Tàu địch: xuất hiện ở vị trí ngẫu nhiên phía ngoài khơi, `hướng về Đảo` và di chuyển dần. Nếu chạm Đạn: tăng biến `Điểm` 1, ẩn tàu (và đạn), cho tàu xuất hiện lại ở vị trí ngẫu nhiên. Nếu chạm Đảo: hiện chữ GAME OVER và `dừng tất cả`.
- Khi `Điểm = 5` (đã bắn hết 5 chiếc tàu) thì hiện chữ WIN và dừng trò chơi. Chữ WIN / GAME OVER có thể là nhân vật hoặc phông nền riêng.
