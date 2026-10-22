# Đáp án - Bảng A Quận Sơn Trà 2016

Gợi ý hướng làm. Xem lại [đề bài](index.md).

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Ngôi sao | Lặp 5 lần: đi 100, quay phải 144, đi 100, quay trái 72 | – |
| 2 | Đèn lồng | Lặp quanh tâm: hình vuông và tam giác đều cạnh 100 | – |
| 3 | Cắt ghép | Cắt bậc thang 2 mảnh, ghép thành hình vuông cạnh 240 | – |
| 4 | Thuyền buồm trên sông Hàn | Bài trình chiếu PowerPoint | – |

!!! info "Bài vẽ MSWLogo"
    Bài 1–3 là bài vẽ MSWLogo, Bài 4 là bài PowerPoint. Các bài chấm theo sản phẩm nên không có lời giải Python. Dưới đây là gợi ý hướng làm.

---

## 1. Ngôi sao

**Ý tưởng.** Đường viền ngôi sao gồm 10 đoạn dài 100. Rùa đi dọc đường viền:

* Ở đỉnh cánh sao (góc $36^\circ$): rùa quay phải $180^\circ - 36^\circ = 144^\circ$.
* Ở chỗ lõm giữa hai cánh: rùa quay trái $72^\circ$.

Mỗi cánh rùa quay tổng cộng $144^\circ - 72^\circ = 72^\circ$, 5 cánh đủ $360^\circ$ nên rùa về đúng chỗ xuất phát:

```
REPEAT 5 [FD 100 RT 144 FD 100 LT 72]
```

Sau đó nhấc bút (`PU`), đưa rùa vào bên trong ngôi sao, đặt màu tô vàng (`SETFC`) và dùng lệnh `FILL`.

## 2. Đèn lồng

**Ý tưởng.** Xem Hình 2 ở bản scan: các hình vuông và tam giác đều cạnh 100 xếp vòng quanh tâm, tam giác đều phía ngoài tô hồng. Viết thủ tục vẽ một hình vuông cạnh 100 (`REPEAT 4 [FD 100 RT 90]`) và thủ tục vẽ một tam giác đều cạnh 100 (`REPEAT 3 [FD 100 RT 120]`), sau đó dùng `REPEAT` để vẽ lặp quanh tâm, mỗi lần quay một góc bằng $360^\circ$ chia số lần lặp (đếm theo hình mẫu). Tô màu hồng các tam giác ngoài bằng `SETFC` và `FILL`.

## 3. Cắt ghép

**Ý tưởng.** Diện tích hình chữ nhật là $360 \times 160 = 57600 = 240 \times 240$, nên hình vuông ghép được có cạnh 240.

Chia hình chữ nhật thành lưới 3 cột × 2 hàng, mỗi ô rộng 120, cao 80. Cắt theo đường bậc thang (2 mảnh): từ điểm trên cạnh trên cách góc trái 120, đi xuống 80, sang phải 120, rồi đi xuống 80 tới cạnh dưới.

* Mảnh trái gồm 3 ô: cột 1 (cả hai hàng) và ô hàng dưới của cột 2.
* Mảnh phải gồm 3 ô còn lại.

Trượt mảnh phải sang trái 120 và lên trên 80: hai mảnh khớp thành hình vuông 2 cột × 3 hàng, tức $240 \times 240$.

Trong MSWLogo: vẽ hình chữ nhật, vẽ đường cắt bậc thang (có thể dùng nét khác màu); sau đó vẽ hình vuông cạnh 240 và vẽ lại đường cắt ở vị trí mới.

## 4. Thuyền buồm trên sông Hàn

**Ý tưởng.** Ít nhất 5 slide giới thiệu buổi biểu diễn thuyền buồm, có hình tự vẽ minh họa, có hiệu ứng PowerPoint. Lưu đúng tên `thuyenbuom.ppt`.
