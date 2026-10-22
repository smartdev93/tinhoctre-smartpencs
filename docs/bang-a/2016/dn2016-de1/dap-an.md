# Đáp án - Bảng A TP Đà Nẵng 2016

Gợi ý hướng làm. Xem lại [đề bài](index.md).

Cả 4 bài đều là bài thực hành bằng MSWLogo hoặc PowerPoint, chấm theo sản phẩm (tệp `.lgo`/`.doc`/`.ppt`), nên không có lời giải Python. Các kết quả số ở Bài 3 đã được kiểm tra lại bằng chương trình vét cạn.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Bậc thang | Thủ tục đệ quy vẽ hình chữ nhật, mỗi bậc ngắn đi 30 | – |
| 2 | Thiệp mừng | Hình vuông nghiêng 45 độ + các đường tròn xoay quanh tâm | – |
| 3 | Tính toán | $3S = 45 + (\text{tổng 3 số ở đỉnh})$ | – |
| 4 | Hoạt động Đội | Bài trình chiếu PowerPoint | – |

---

## 1. Bậc thang

!!! info "Bài vẽ MSWLogo"
    Bài chấm theo hình vẽ và câu lệnh, không có lời giải Python.

**Gợi ý hướng làm.** Cả hình cao 300 gồm 10 bậc nên mỗi bậc cao $300 / 10 = 30$. Bậc dưới dài hơn bậc trên đúng 30, nên chiều ngang các bậc từ dưới lên là $300, 270, 240, \ldots, 30$, thẳng hàng ở mép phải.

Mỗi lần vẽ xong một hình chữ nhật, rùa nhích lên 30 và sang phải 30 rồi vẽ hình ngắn hơn 30. Ví dụ (rùa đặt ở góc dưới trái, hướng lên trên):

```
TO BAC :W
  IF :W < 30 [STOP]
  REPEAT 2 [FD 30 RT 90 FD :W RT 90]
  PU FD 30 RT 90 FD 30 LT 90 PD
  BAC :W - 30
END

CS
BAC 300
```

## 2. Thiệp mừng

!!! info "Bài vẽ MSWLogo"
    Bài chấm theo hình vẽ và câu lệnh, không có lời giải Python.

**Gợi ý hướng làm.**

- Hình vuông nghiêng: `RT 45 REPEAT 4 [FD 300 RT 90]`, rồi đưa rùa về tâm hình vuông (nhấc bút khi di chuyển).
- Bông hoa: các đường tròn bán kính 50 có tâm nằm trên một vòng tròn nhỏ quanh tâm hình, xoay đều quanh tâm. Đếm số đường tròn trên Hình 2 (xem [bản scan](index.md#de-goc-ban-scan)) để chọn góc xoay $360 / n$.
- Tô màu từng vùng: nhấc bút đưa rùa vào trong vùng, `SETFLOODCOLOR` (vàng cho nhụy, đỏ cho cánh hoa, xanh cho lá viền ngoài) rồi `FILL`.

## 3. Tính toán

!!! info "Bài vẽ MSWLogo"
    Bài chấm theo hình vẽ, các số điền vào và câu lệnh, không có lời giải Python.

**Gợi ý hướng làm.**

- Vẽ lục giác đều cạnh 20: `REPEAT 6 [FD 20 RT 60]`. Viết thành thủ tục rồi gọi 9 lần ở 9 vị trí theo hình tam giác; ghi số vào giữa ô bằng `LABEL`.

**Điền số với tổng 20.** Gọi các ô trên cạnh trái (giữa 5 và 2) là $a, b$, cạnh phải (giữa 5 và 8) là $c, d$, cạnh đáy (giữa 2 và 8) là $e, f$. Cần:

- $a + b = 20 - 5 - 2 = 13$,
- $c + d = 20 - 5 - 8 = 7$,
- $e + f = 20 - 2 - 8 = 10$,

với $a, b, c, d, e, f$ là các số $1, 3, 4, 6, 7, 9$. Có đúng 2 cách chia nhóm:

| Cạnh trái (13) | Cạnh phải (7) | Cạnh đáy (10) |
| --- | --- | --- |
| 4, 9 | 1, 6 | 3, 7 |
| 6, 7 | 3, 4 | 1, 9 |

Trong mỗi cạnh có thể đổi chỗ hai số cho nhau, nên có tổng cộng 16 cách điền.

**Tổng nhỏ nhất, lớn nhất.** Gọi tổng mỗi cạnh là $S$. Cộng 3 cạnh lại thì mỗi số ở giữa cạnh được tính 1 lần, mỗi số ở đỉnh được tính 2 lần:

$$3S = (1 + 2 + \ldots + 9) + (\text{tổng 3 số ở đỉnh}) = 45 + (\text{tổng 3 số ở đỉnh}).$$

- Nhỏ nhất: đỉnh là $1, 2, 3$ thì $3S = 51$, $S = 17$. Ví dụ ba cạnh: $1 + 5 + 9 + 2$, $1 + 6 + 7 + 3$, $2 + 4 + 8 + 3$.
- Lớn nhất: đỉnh là $7, 8, 9$ thì $3S = 69$, $S = 23$. Ví dụ ba cạnh: $7 + 2 + 6 + 8$, $7 + 3 + 4 + 9$, $8 + 1 + 5 + 9$.

Vậy tổng **nhỏ nhất là 17**, **lớn nhất là 23**. Chương trình vét cạn cả $9! = 362\,880$ cách đặt cho thấy các tổng có thể đạt được là 17, 19, 20, 21, 23 (không có 18 và 22).

## 4. Hoạt động Đội

!!! info "Bài thực hành ứng dụng"
    Bài làm là tệp trình chiếu PowerPoint, chấm theo sản phẩm, không có lời giải Python.

**Gợi ý hướng làm.**

- Tối thiểu 5 slide: trang tiêu đề (75 năm thành lập Đội, 15/5/1941 - 15/5/2016), các slide giới thiệu từng hoạt động em đã tham gia, slide cảm nghĩ.
- Có ít nhất một hình tự vẽ (Paint hoặc Shapes trong PowerPoint).
- Thêm hiệu ứng chuyển trang và hiệu ứng cho chữ, hình.
- Lưu đúng tên `hoatdongdoi.ppt`.
