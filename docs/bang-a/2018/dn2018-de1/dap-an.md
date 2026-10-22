# Đáp án - Bảng A TP Đà Nẵng 2018

Gợi ý hướng làm. Xem lại [đề bài](index.md).

Cả 3 bài đều là bài vẽ MSWLogo, chấm theo hình vẽ và câu lệnh, nên không có lời giải Python. Các kết quả số ở Bài 2 và Bài 3 đã được kiểm tra lại bằng chương trình.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Hình vẽ | Thủ tục vẽ đa giác đều, thu nhỏ $\frac{2}{3}$, quay quanh đỉnh chung | – |
| 2 | Tam giác kì ảo | Tam giác Sierpinski; đếm số *mẫu vật* | – |
| 3 | Hoa tre | Số nụ hoa là $1, 9, 25, 49, \ldots = (2n-1)^2$ | – |

---

## 1. Hình vẽ

!!! info "Bài vẽ MSWLogo"
    Bài chấm theo hình vẽ và câu lệnh, không có lời giải Python.

**Gợi ý hướng làm.**

- Đa giác đều $n$ cạnh, cạnh $a$: `REPEAT :N [FD :A RT 360 / :N]`.
- Hình cơ sở: vẽ đa giác cạnh 100, rồi các đa giác cạnh $100 \cdot \frac{2}{3}$, $100 \cdot \left(\frac{2}{3}\right)^2, \ldots$ cùng xuất phát từ một đỉnh chung (như Hình 1a–4a). Viết thủ tục đệ quy, ví dụ:

```
TO LONG :N :A
  IF :A < 10 [STOP]
  REPEAT :N [FD :A RT 360 / :N]
  LONG :N :A * 2 / 3
END
```

Điều kiện dừng (`:A < 10`) chọn theo số đa giác đếm được trên hình mẫu.
- Hình 1b–4b: lặp lại hình cơ sở nhiều lần, mỗi lần quay rùa quanh đỉnh chung một góc bằng nhau (ví dụ $360 / k$ nếu có $k$ hình cơ sở). Đếm số lần lặp trên hình mẫu ở [bản scan](index.md#de-goc-ban-scan).

## 2. Tam giác kì ảo

!!! info "Bài vẽ MSWLogo"
    Bài chấm theo hình vẽ, câu lệnh và kết quả tính, không có lời giải Python.

**Gợi ý vẽ.** *Mẫu vật*: `REPEAT 3 [FD 20 RT 120]` rồi tô kín. *Hình cơ sở* là tam giác cạnh 40 gồm 3 mẫu vật (ở giữa là lỗ trắng cạnh 20). Hình 2 xây theo cùng cách: 3 hình cơ sở ghép thành tam giác cạnh 80, 3 tam giác cạnh 80 ghép thành tam giác cạnh 160, 3 tam giác cạnh 160 ghép thành tam giác cạnh 320 (đáy có 8 hình cơ sở). Thủ tục đệ quy:

```
TO KIAO :A
  IF :A = 20 [MAUVAT STOP]
  REPEAT 3 [KIAO :A / 2 FD :A RT 120]
END
```

trong đó `MAUVAT` là thủ tục vẽ và tô một mẫu vật (vẽ xong phải đưa rùa về đúng vị trí và hướng ban đầu), rồi gọi `KIAO 320`.

**Diện tích phần không tô màu.** Diện tích một mẫu vật: $\frac{20 \times 17{,}3}{2} = 173$.

- Hình 2 là tam giác đều cạnh $320 = 16 \times 20$, chia được thành $16^2 = 256$ tam giác bằng mẫu vật.
- Số mẫu vật được tô: $3 \times 3 \times 3 \times 3 = 81$ (hình cơ sở có 3, mỗi lần ghép nhân 3, ghép 3 lần).
- Phần không tô màu gồm $256 - 81 = 175$ tam giác cỡ mẫu vật.

Diện tích phần không tô màu: $175 \times 173 = 30\,275$ (đơn vị diện tích).

Kiểm tra lại bằng cách cộng các lỗ trắng: 27 lỗ cạnh 20 (1 mẫu vật), 9 lỗ cạnh 40 (4 mẫu vật), 3 lỗ cạnh 80 (16 mẫu vật), 1 lỗ cạnh 160 (64 mẫu vật): $27 + 36 + 48 + 64 = 175$ mẫu vật.

!!! warning "Bẫy thường gặp"
    - Dùng chiều cao 17,3 như đề cho (giá trị gần đúng của $10\sqrt{3}$); nếu dùng $\sqrt{3}$ chính xác thì kết quả lệch đi một chút.
    - Đếm sai số tầng của Hình 2. Đếm số hình cơ sở ở cạnh đáy (8 hình) để suy ra cạnh tam giác lớn.

## 3. Hoa tre

!!! info "Bài vẽ MSWLogo"
    Bài chấm theo hình vẽ, câu lệnh và kết quả tính, không có lời giải Python.

**Gợi ý vẽ.**

- a) Nụ hoa (hình thoi cạnh 10, góc 60 độ và 120 độ): `REPEAT 2 [FD 10 RT 60 FD 10 RT 120]`, sau đó tô đỏ.
- b) Thân cây: `FD 150`; mỗi cành dài $150 / 4 = 37{,}5$ đơn vị, xòe đều từ ngọn thân; ở cuối mỗi cành vẽ một bông gồm nhiều nụ hoa xoay đều quanh một điểm (`REPEAT :K [NUHOA RT 360 / :K]`).

**c) Quy luật.** Dùng cách đếm ghi ở [đề bài](index.md#3-hoa-tre): hình $n$ có $2n - 1$ cành, mỗi cành có $2n - 1$ nụ, nên số nụ hoa là

$$1, \; 9, \; 25, \; 49, \; \ldots, \; (2n - 1)^2.$$

- Số hạng thứ 50: $(2 \times 50 - 1)^2 = 99^2 = 9\,801$.
- Tổng 50 số hạng đầu: $1^2 + 3^2 + 5^2 + \ldots + 99^2 = \frac{50 \times 99 \times 101}{3} = 166\,650$.

Trong MSWLogo có thể tính bằng vòng lặp cộng dồn thay cho công thức:

```
MAKE "S 0
FOR [I 1 50] [MAKE "S :S + (2 * :I - 1) * (2 * :I - 1)]
PRINT :S
```
