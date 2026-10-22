# Đáp án - Bảng A TP Đà Nẵng 2015

Gợi ý hướng làm. Xem lại [đề bài](index.md).

Cả 4 bài đều là bài thực hành bằng MSWLogo hoặc PowerPoint, chấm theo sản phẩm (tệp `.doc`/`.ppt`), nên không có lời giải Python. Cách chia hình ở Bài 3 đã được kiểm tra lại bằng chương trình.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Chào mừng Hội thi | Hai hình chữ nhật lồng nhau + `LABEL` | – |
| 2 | Hoa trang trí | Thủ tục vẽ ngũ giác đều, lặp 5 lần quanh tâm | – |
| 3 | Chia hình | Chia lưới ô $50 \times 50$, ghép 4 hình chữ T | – |
| 4 | Văn minh đô thị | Bài trình chiếu PowerPoint | – |

---

## 1. Chào mừng Hội thi

!!! info "Bài vẽ MSWLogo"
    Bài chấm theo hình vẽ và câu lệnh, không có lời giải Python.

**Gợi ý hướng làm.**

- Hình chữ nhật ngoài rộng 400, cao 200; hình trong rộng 380, cao 180, nên mỗi phía cách nhau 10 đơn vị.
- Đặt rùa ở góc dưới trái, hướng lên trên:

```
CS
REPEAT 2 [FD 200 RT 90 FD 400 RT 90]
PU RT 90 FD 10 LT 90 FD 10 PD
REPEAT 2 [FD 180 RT 90 FD 380 RT 90]
```

- Viết chữ: nhấc bút (`PU`), đưa rùa tới vị trí dòng chữ, quay rùa sang phải (`RT 90`) để chữ nằm ngang, rồi dùng `LABEL [CHAO MUNG HOI THI TIN HOC TRE]`; làm tương tự với dòng thứ hai.
- Dán câu lệnh và ảnh chụp hình vẽ vào `chaomung.doc`.

## 2. Hoa trang trí

!!! info "Bài vẽ MSWLogo"
    Bài chấm theo hình vẽ và câu lệnh, không có lời giải Python.

**Gợi ý hướng làm.**

- Ngũ giác đều cạnh $a$: `REPEAT 5 [FD a RT 72]` (góc ngoài $360 / 5 = 72$ độ).
- Viết thủ tục `TO NGUGIAC :A` rồi gọi với cạnh 100 và 75.
- Quan sát Hình 2 (xem [bản scan](index.md#de-goc-ban-scan)): hình có đối xứng xoay bậc 5, nên chỉ cần vẽ một phần (ngũ giác lớn và ngũ giác nhỏ ở đúng vị trí) rồi xoay quanh tâm 5 lần, mỗi lần $72$ độ, ví dụ `REPEAT 5 [NGUGIAC 100 RT 72]`. Thử và chỉnh vị trí xuất phát của rùa cho khớp hình mẫu.
- Tô màu tùy ý: nhấc bút đưa rùa vào trong vùng cần tô, `SETFLOODCOLOR` rồi `FILL`.

## 3. Chia hình

!!! info "Bài vẽ MSWLogo"
    Bài chấm theo hình vẽ và câu lệnh, không có lời giải Python.

**Gợi ý hướng làm.** Dùng cách hiểu hình 3 ghi ở [đề bài](index.md#3-chia-hinh): phần nhô lên là ô $50 \times 50$. Diện tích hình 3 là $40\,000$, nên mỗi phần có diện tích $10\,000$, tức là **4 ô** $50 \times 50$.

Chia hình 3 thành lưới ô $50 \times 50$ (4 cột, 5 hàng, có 16 ô thuộc hình). Có một cách chia thành 4 hình **chữ T** (mỗi hình 4 ô), các hình này xoay vào nhau được. Mỗi chữ cái là một phần (hàng trên cùng là phần nhô lên, `.` là ô nằm ngoài hình):

```
. C . .
. C C D
A C D D
A A B D
A B B B
```

Chương trình vét cạn trên lưới ô 50 cho thấy đây là **cách chia duy nhất** (chỉ cho phép xoay, không lật hình).

- a) Vẽ hình mẫu: đi theo viền hình 3 bắt đầu từ góc dưới trái, ví dụ `FD 150 RT 90 FD 50 LT 90 FD 100 RT 90 FD 50 RT 90 FD 50 LT 90 FD 100 RT 90 FD 200 RT 90 FD 200 RT 90` (lệnh `RT 90` cuối đưa rùa về hướng ban đầu).
- b) Vẽ lại hình mẫu, rồi vẽ thêm các đoạn ranh giới giữa các phần A, B, C, D theo lưới ở trên (mỗi đoạn dài 50 hoặc bội của 50).

## 4. Văn minh đô thị

!!! info "Bài thực hành ứng dụng"
    Bài làm là tệp trình chiếu PowerPoint, chấm theo sản phẩm, không có lời giải Python.

**Gợi ý hướng làm.**

- Tối thiểu 5 slide: trang tiêu đề "Năm văn hóa, văn minh đô thị 2015", rồi các slide về cảnh đẹp, an toàn giao thông, môi trường, con người Đà Nẵng, và slide kết (em sẽ làm gì).
- Hình tự vẽ: tối đa 3 hình (vẽ bằng Paint hoặc công cụ Shapes của PowerPoint).
- Thêm hiệu ứng chuyển trang (Transitions) và hiệu ứng cho chữ, hình (Animations).
- Lưu đúng tên `VMDT.ppt`.
