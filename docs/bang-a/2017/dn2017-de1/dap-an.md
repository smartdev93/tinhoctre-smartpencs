# Đáp án - Bảng A TP Đà Nẵng 2017

Gợi ý hướng làm. Xem lại [đề bài](index.md).

Cả 4 bài đều là bài thực hành bằng MSWLogo hoặc PowerPoint, chấm theo sản phẩm, nên không có lời giải Python. Lệnh vẽ ở Bài 2 và cách điền số ở Bài 3 đã được kiểm tra lại bằng chương trình.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Chiếc lá | Thủ tục vẽ chiếc lá bằng `ARC2`, lặp 30 lần quay 12 độ | – |
| 2 | Cái ô | Đường gấp khúc quay 12 lần, mỗi lần 30 độ | – |
| 3 | Điền số | Xếp các số theo số dư khi chia cho 3 | – |
| 4 | An toàn thực phẩm | Bài trình chiếu PowerPoint | – |

---

## 1. Chiếc lá

!!! info "Bài vẽ MSWLogo"
    Bài chấm theo hình vẽ và câu lệnh, không có lời giải Python.

**Gợi ý hướng làm.**

- Viết thủ tục `TO CHIECLA` vẽ hai cung tròn 90 độ bán kính 100 bằng `ARC2`, giữa hai cung quay rùa sao cho hai cung gặp nhau ở hai *đỉnh* như Hình 1a. Thử với góc quay ghi trong đề rồi chỉnh cho khớp hình mẫu; sau khi vẽ xong, đưa rùa về đúng vị trí và hướng ban đầu để dễ lặp.
- Hình 2 có 30 chiếc lá, mỗi lần quay 12 độ ($30 \times 12 = 360$ độ). Mỗi lần lặp: vẽ chiếc lá, rồi di chuyển *đỉnh* xuất phát đi 30 đơn vị (nhấc bút) và quay 12 độ để được *hai chiếc lá kề nhau* như Hình 1b.
- Xem các hình mẫu trong [bản scan](index.md#de-goc-ban-scan).

## 2. Cái ô

!!! info "Bài vẽ MSWLogo"
    Bài chấm theo hình vẽ và câu lệnh, không có lời giải Python.

**Gợi ý hướng làm.** "Hai đoạn lệch nhau 150 độ" là góc giữa hai đoạn bằng 150 độ, tức rùa quay 30 độ; "lệch nhau 90 độ" thì rùa quay 90 độ. Xuất phát từ tâm, đường gấp khúc gồm: `FD 100 RT 30 FD 100 RT 90 FD 100`.

- Điểm cuối đoạn thứ hai và điểm cuối đoạn thứ ba cùng cách tâm khoảng $193{,}2$ đơn vị, và đoạn thứ ba nhìn từ tâm dưới góc 30 độ. Vì vậy đoạn thứ ba là một cạnh của hình 12 cạnh đều cạnh 100, và cần quay **12 lần, mỗi lần 30 độ** ($12 \times 30 = 360$).
- Sau mỗi đường gấp khúc, cho rùa đi lùi về tâm rồi quay 30 độ:

```
CS
REPEAT 12 [FD 100 RT 30 FD 100 RT 90 FD 100 BK 100 LT 90 BK 100 LT 30 BK 100 RT 30]
```

- Tô màu: nhấc bút đưa rùa vào giữa từng ô, `SETFLOODCOLOR` rồi `FILL`; hai ô cạnh nhau dùng hai màu khác nhau (ví dụ xen kẽ hai màu).

## 3. Điền số

!!! info "Bài vẽ MSWLogo"
    Bài chấm theo hình vẽ, các số điền vào và câu lệnh, không có lời giải Python.

**Gợi ý hướng làm.**

- a) Viết thủ tục vẽ ô vuông cạnh 40 (`REPEAT 4 [FD 40 RT 90]`), gọi ở 13 vị trí theo hình chữ thập; ô giữa tô đen bằng `SETFLOODCOLOR` và `FILL`.
- b) Chỉ cần quan tâm **số dư khi chia cho 3**: các số 1..12 có đúng 4 số chia hết cho 3 (3, 6, 9, 12), 4 số dư 1 (1, 4, 7, 10), 4 số dư 2 (2, 5, 8, 11). Tổng ba số chia hết cho 3 khi ba số dư là $0, 1, 2$ hoặc giống nhau cả ba.

Hình chữ thập có 12 bộ *ba ô vuông liền kề* (mỗi bộ là ba ô gặp nhau tại một đỉnh). Một cách điền thỏa mãn (`#` là ô tô đen):

```
          3
     1    2    4
5    6    #    9    8
     7   11   10
         12
```

Tổng 12 bộ ba ô liền kề lần lượt là: $3+1+2$, $3+2+4$, $1+5+6$, $1+2+6$, $2+4+9$, $4+9+8$, $5+6+7$, $6+7+11$, $9+11+10$, $9+8+10$, $7+11+12$, $11+10+12$, đều chia hết cho 3. Chương trình vét cạn theo số dư cho thấy có 6 cách xếp số dư thỏa mãn; mỗi cách lại hoán vị được các số cùng số dư.

- Ghi số vào ô bằng `LABEL` sau khi đưa rùa (nhấc bút) tới giữa ô.

## 4. An toàn thực phẩm

!!! info "Bài thực hành ứng dụng"
    Bài làm là tệp trình chiếu PowerPoint, chấm theo sản phẩm, không có lời giải Python.

**Gợi ý hướng làm.**

- Tối thiểu 5 slide: tiêu đề, thực phẩm bẩn là gì, tác hại, cách nhận biết và chọn thực phẩm an toàn, biện pháp bảo vệ sức khỏe, lời kết.
- Hình tự vẽ: tối đa 3 hình.
- Thêm hiệu ứng chuyển trang và hiệu ứng cho chữ, hình.
- Lưu đúng tên `antoan.ppt`.
