# Đáp án - Bảng A Quận Thanh Khê 2016

Gợi ý hướng làm. Xem lại [đề bài](index.md).

Cả 4 bài đều là bài thực hành bằng MSWLogo hoặc PowerPoint, chấm theo sản phẩm (tệp `.doc`/`.ppt`), nên không có lời giải Python.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Trang trí | Vẽ hình lặp bằng `REPEAT`, tô màu bằng `SETFLOODCOLOR` + `FILL` | – |
| 2 | Tìm đường đi | Đường đi qua mỗi cạnh đúng một lần (đường Euler) | – |
| 3 | Tính tổng | Biến đếm + biến tổng trong vòng lặp | – |
| 4 | Thành lập Đoàn TNCS Hồ Chí Minh | Bài trình chiếu PowerPoint | – |

---

## 1. Trang trí

!!! info "Bài vẽ MSWLogo"
    Bài chấm theo hình vẽ và câu lệnh, không có lời giải Python.

**Gợi ý hướng làm.**

- Quan sát Hình 1 (xem [bản scan](index.md#de-goc-ban-scan)): khung ngoài là một bát giác đều cạnh 100; bên trong có các hình vuông cạnh 50 và các cánh hoa hình thoi xếp quanh tâm.
- Bát giác đều có góc ngoài $360° / 8 = 45°$, nên vẽ khung ngoài bằng `REPEAT 8 [FD 100 RT 45]`.
- Các phần bên trong lặp lại 8 lần quanh tâm: viết một thủ tục (`TO ... END`) vẽ một phần, rồi gọi trong `REPEAT 8 [...]` kèm lệnh quay $45°$.
- Tô màu: nhấc bút (`PU`) đưa rùa vào bên trong vùng cần tô, dùng `SETFLOODCOLOR 6` (vàng) hoặc `SETFLOODCOLOR 4` (đỏ) rồi `FILL`, sau đó đưa rùa về vị trí cũ và hạ bút (`PD`).
- Dán các câu lệnh và ảnh chụp hình vẽ vào `trangtri.doc`.

## 2. Tìm đường đi

!!! info "Bài vẽ MSWLogo"
    Bài chấm theo hình vẽ và câu lệnh, không có lời giải Python.

**Ý tưởng.** Đây là bài vẽ hình "một nét": đi qua mỗi cạnh đúng một lần. Đếm số cạnh tại mỗi đỉnh của Hình 2:

| Đỉnh | A | B | C | D | E | F |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Số cạnh | 2 | 4 | 4 | 2 | 4 | 4 |

Mọi đỉnh đều có số cạnh chẵn, nên có thể vẽ một nét, xuất phát ở đỉnh nào cũng được và kết thúc tại chính đỉnh đó. Đường đi ví dụ của đề ($A \to B \to C \to D \to E \to C \to F \to E \to B \to F \to A$) đi qua đủ 10 cạnh, mỗi cạnh một lần.

**Số liệu hình học** (tính từ độ dài đề cho):

- Tam giác ABF, CDE đều cạnh 100 nên mỗi góc $60°$; BF và CE là hai cạnh đứng dài 100.
- BCEF là hình chữ nhật $200 \times 100$.
- Hai đường chéo CF và EB dài $\sqrt{200^2 + 100^2} \approx 223{,}61$; mỗi đường chéo lệch so với cạnh nằm ngang một góc $\approx 26{,}57°$.

**Gợi ý hướng làm.** Đi theo thứ tự đỉnh của ví dụ; ở mỗi đỉnh dùng `RT`/`LT` để quay theo góc đã tính, `FD` theo độ dài cạnh, chèn `WAIT 20` giữa các lệnh vẽ như đề yêu cầu. Chạy thử và chỉnh góc quay nếu nét vẽ không khép kín.

## 3. Tính tổng

!!! info "Bài lập trình MSWLogo"
    Đề yêu cầu viết lệnh MSWLogo, không có lời giải Python.

**Ý tưởng.** Dãy $2, 4, 6, \ldots, 98$ là các số chẵn từ 2 đến 98.

- Số số hạng: $(98 - 2) / 2 + 1 = 49$.
- Tổng: $(2 + 98) \times 49 / 2 = 2450$.

Kết quả mong đợi trên màn hình MSWLogo:

```
So so hang cua day so la: 49
Tong cua day so la: 2450
```

**Gợi ý hướng làm.** Dùng `MAKE` tạo biến đếm và biến tổng bằng 0, một biến số hạng bắt đầu từ 2; lặp 49 lần (hoặc lặp đến khi số hạng vượt 98): cộng số hạng vào tổng, tăng biến đếm, tăng số hạng thêm 2. Cuối cùng dùng `PRINT` in hai dòng kết quả theo đúng mẫu.

## 4. Thành lập Đoàn TNCS Hồ Chí Minh

!!! info "Bài thực hành ứng dụng"
    Bài chấm theo sản phẩm PowerPoint, không có lời giải Python.

**Gợi ý hướng làm.**

- Tối thiểu 5 slide, ví dụ: slide tiêu đề; ý nghĩa ngày 26/3 (85 năm, 1931–2016); các hoạt động của trường (mỗi hoạt động một slide); slide kết.
- Tự vẽ tối đa 3 hình minh họa (bằng công cụ vẽ hình của PowerPoint hoặc Paint).
- Thêm hiệu ứng chuyển trang và hiệu ứng cho đối tượng.
- **Không** ghi tên trường và họ tên; lưu đúng tên `thanhlapdoan.ppt`.
