# Đáp án - Bảng A Huyện Hòa Vang 2016

Xem lại [đề bài](index.md).

Đây là đề thực hành vẽ hình bằng MSWLogo và trình chiếu PowerPoint, không phải bài lập trình giải thuật, nên không có lời giải Python. Dưới đây là gợi ý hướng làm.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Chia hình | Nối trung điểm 3 cạnh, tạo 4 tam giác đều cạnh 75 | – |
| 2 | Viên gạch hoa | Hình vuông 200 + lặp ngũ giác đều cạnh 50 quanh tâm, tô màu | – |
| 3 | Tính toán | Chưa có (thiếu đề chi tiết) | – |
| 4 | Mùa hè của em | Chưa có (thiếu đề chi tiết) | – |

---

## 1. Chia hình

!!! info "Bài vẽ MSWLogo"
    Bài yêu cầu vẽ bằng MSWLogo và nộp tệp `.doc`, không có lời giải Python.

**Ý tưởng.** Nối trung điểm của 3 cạnh, tam giác đều cạnh 150 được chia thành **4 tam giác đều cạnh 75**. Bốn tam giác này bằng nhau: ba tam giác ở ba góc, và tam giác ở giữa chính là một tam giác góc được xoay 180°.

Vẽ tam giác đều cạnh 150:

```text
REPEAT 3 [FD 150 RT 120]
```

Vẽ tam giác đã chia: tại mỗi đỉnh, vẽ một tam giác nhỏ cạnh 75 nằm trong góc, rồi đi tiếp sang đỉnh sau. Ba tam giác góc tạo luôn ba cạnh của tam giác ở giữa.

```text
REPEAT 3 [REPEAT 3 [FD 75 RT 120] FD 150 RT 120]
```

Câu lệnh trên đã được kiểm tra bằng mô phỏng rùa: các đoạn vẽ ra đi qua đúng 3 đỉnh và 3 trung điểm cạnh, rùa trở về vị trí và hướng ban đầu.

## 2. Viên gạch hoa

!!! info "Bài vẽ MSWLogo"
    Bài yêu cầu vẽ và tô màu bằng MSWLogo, không có lời giải Python.

**Gợi ý hướng làm.**

- Vẽ hình vuông cạnh 200: `REPEAT 4 [FD 200 RT 90]`, tô nền màu vàng (đặt màu tô bằng `SETFLOODCOLOR`, đưa rùa vào bên trong hình rồi dùng `FILL`).
- Ngũ giác đều cạnh 50: `REPEAT 5 [FD 50 RT 72]`.
- Đưa rùa (nhấc bút bằng `PU`, hạ bút bằng `PD`) tới tâm viên gạch. Theo hình mẫu, bông hoa gồm nhiều ngũ giác đều xếp xoay quanh tâm (các ngũ giác dường như chung một đỉnh ở tâm): vẽ một ngũ giác có một đỉnh ở tâm, rồi xoay rùa một góc bằng $360°$ chia cho số ngũ giác và lặp lại.
- Tô màu đỏ / trắng cho từng phần như hình mẫu: đưa rùa vào giữa phần cần tô rồi dùng `FILL`.

Đếm số ngũ giác và góc xoay trực tiếp trên hình trong [bản scan](index.md#de-goc-ban-scan); ảnh chụp có độ phân giải thấp nên trang này không ghi sẵn câu lệnh hoàn chỉnh.

## 3. Tính toán

Chưa có gợi ý: ảnh chụp thiếu trang 2 của đề.

## 4. Mùa hè của em

Chưa có gợi ý: ảnh chụp thiếu trang 2 của đề. Tên tệp `muahecuaem.ppt` cho thấy đây là bài trình chiếu PowerPoint.
