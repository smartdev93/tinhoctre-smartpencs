# Đáp án - Bảng A Quận Ngũ Hành Sơn (chưa rõ năm)

Gợi ý hướng làm. Xem lại [đề bài](index.md).

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Lật đật | Vẽ hai hình tròn chồng nhau, thêm mắt, miệng, nút áo | – |
| 2 | Vòng đeo cổ | Lặp 18 lần: vẽ một hạt tròn bán kính 5, dịch rùa theo cung tròn | – |
| 3 | Vẽ hình và tính diện tích | Cạnh $DC = 80000 / (a + b)$, diện tích $MDC = 40000b / (a + b)$ | – |
| 4 | Trường học xanh | Bài trình chiếu PowerPoint, hình vẽ bằng Paint | – |

!!! info "Bài thực hành ứng dụng"
    Cả 4 bài của đề này làm bằng MSWLogo, Word, PowerPoint và Paint, chấm theo sản phẩm, nên không có lời giải Python/C++. Dưới đây chỉ là gợi ý hướng làm.

---

## 1. Lật đật

**Ý tưởng.** Kích thước tùy ý, nên chọn số dễ tính: thân là hình tròn bán kính 80, đầu là hình tròn bán kính 30 đặt ngay trên thân (tâm đầu cách tâm thân $80 + 30 = 110$ bước).

* Vẽ thân, nhấc bút (`PU`) đi lên 110 bước, hạ bút (`PD`) vẽ đầu.
* Mắt và miệng là các hình tròn nhỏ; các nút áo là hình tròn nhỏ dọc trục giữa thân.
* Mỗi lần di chuyển giữa hai chi tiết đều nhấc bút để không để lại nét thừa.

## 2. Vòng đeo cổ

**Ý tưởng.** Các hạt xếp dọc một cung tròn hình chữ U. Đặt rùa ở tâm cung, mỗi hạt cách tâm cùng một khoảng $R$. Với 18 hạt trải trên khoảng $200°$, hai hạt liền nhau cách nhau góc khoảng $200° / 17 \approx 11,8°$.

* `SETPC 4` (màu đỏ). Mỗi hạt: nhấc bút đi ra $R$ bước, vẽ hình tròn bán kính 5, quay về tâm, quay góc giữa hai hạt. Lặp 18 lần bằng `REPEAT`.
* Muốn hạt nằm sát nhau thì khoảng cách giữa hai tâm hạt liền nhau phải gần bằng $2 \times 5 = 10$, tức $R \approx 10 / (2\sin(5,9°)) \approx 49$.
* Muốn hạt tô đặc màu đỏ thì sau khi vẽ đường tròn, đưa rùa vào trong hạt và dùng `FILL` với màu tô đỏ.

## 3. Vẽ hình và tính diện tích

**Ý tưởng.** $AD = AM + MD = a + b$. Diện tích hình chữ nhật là 80000 nên

$$DC = AB = \frac{80000}{a + b}.$$

Tam giác MDC vuông tại D, có hai cạnh góc vuông $MD = b$ và $DC$:

$$S_{MDC} = \frac{MD \times DC}{2} = \frac{b}{2} \cdot \frac{80000}{a + b} = \frac{40000\, b}{a + b}.$$

Ví dụ $a = 100$, $b = 300$: $DC = 200$, $S_{MDC} = 300 \times 200 / 2 = 30000$.

Gợi ý thủ tục, đặt D tại gốc tọa độ, AD dọc trục đứng, DC dọc trục ngang:

```
TO CHUNHAT :A :B
  MAKE "W 80000 / (:A + :B)
  PU HOME PD
  SETXY 0 :A + :B
  SETXY :W :A + :B
  SETXY :W 0
  SETXY 0 0
  SETXY 0 :B
  SETXY :W 0
  PU SETXY :W / 4 :B / 4
  SETFLOODCOLOR 3 FILL
  SETXY 0 -30
  LABEL SE [Dien tich phan to mau la:] 40000 * :B / (:A + :B)
END
```

Gọi thủ tục, ví dụ `CHUNHAT 100 300`.

!!! note "Về đoạn lệnh trên"
    Phần hình học và công thức diện tích đã được kiểm tra bằng chương trình trên 1000 cặp $(a, b)$, bao gồm cả điểm tô màu $(W/4,\ b/4)$ luôn nằm trong tam giác MDC. Đoạn lệnh chưa được chạy trên MSWLogo. Nếu bản MSWLogo của em không nhận mã màu dạng số cho `SETFLOODCOLOR` thì dùng dạng `[R G B]`. Với $a + b$ nhỏ, cạnh $DC$ rất dài và vượt khỏi màn hình; khi đó cần chọn $a, b$ lớn hơn.

!!! warning "Bẫy thường gặp"
    - Nhầm diện tích tam giác thành $MD \times DC$ (quên chia 2).
    - Dùng cạnh $AD$ thay cho $MD$: tam giác cần tô là MDC, cạnh góc vuông là $MD = b$.
    - Gán cứng số đo: đề yêu cầu thủ tục nhận $a$, $b$ khi gọi, nên mọi độ dài phải tính từ $a$, $b$.

## 4. Trường học xanh

**Ý tưởng.** Ít nhất 5 slide nói về cảm nghĩ trong buổi trồng cây, có hiệu ứng hoạt hình (Animations) và hiệu ứng chuyển trang (Transitions), có hình minh họa tự vẽ bằng Paint lưu đúng tên `trongcay.bmp` rồi chèn vào slide. Lưu bài đúng tên `trinhdien.ppt` và không ghi tên mình, tên trường.
