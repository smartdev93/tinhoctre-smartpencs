# Đáp án - Bảng A Quận Liên Chiểu 2016

Xem lại [đề bài](index.md).

Đây là đề thực hành ứng dụng (MSWLogo, PowerPoint), không phải bài lập trình giải thuật, nên không có lời giải Python. Dưới đây là gợi ý hướng làm.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Chong chóng | Lặp 6 lần vẽ cánh từ tam giác đều cạnh 100, xoay 60° | – |
| 2 | Biển báo giao thông | Hai tam giác đều lồng nhau, tô đỏ và vàng | – |
| 3 | Tính toán | 60 ngày = 30 lần nhân đôi: $2^{30}$ gam | – |
| 4 | Bảo vệ môi trường xanh sạch đẹp | Trình chiếu PowerPoint tối thiểu 5 slide | – |

---

## 1. Chong chóng

!!! info "Bài vẽ MSWLogo"
    Bài yêu cầu vẽ bằng MSWLogo, không có lời giải Python.

**Gợi ý hướng làm.**

- Tam giác đều cạnh 100: `REPEAT 3 [FD 100 RT 120]`.
- Hình 1 có tính đối xứng xoay: 6 cánh giống nhau quanh tâm. Quan sát hình mẫu để tìm **một cánh** (gồm những tam giác đều nào, ghép với nhau ra sao), viết một thủ tục vẽ một cánh bắt đầu và kết thúc ở tâm, rồi lặp 6 lần, mỗi lần quay rùa 60°.
- Nếu theo hình mẫu phần lõi ở giữa là lục giác đều cạnh 100 gồm 6 tam giác đều chung đỉnh ở tâm, có thể vẽ bằng `REPEAT 6 [REPEAT 3 [FD 100 RT 120] RT 60]`.

Ảnh scan có độ phân giải thấp nên trang này không ghi sẵn câu lệnh cho phần cánh; hãy đối chiếu với [hình mẫu](index.md#de-goc-ban-scan).

## 2. Biển báo giao thông

!!! info "Bài vẽ MSWLogo"
    Bài yêu cầu vẽ và tô màu bằng MSWLogo, không có lời giải Python.

**Gợi ý hướng làm** (theo cách hiểu: tam giác ngoài cạnh 300, tam giác trong cạnh 240, cùng tâm).

- Biển báo là tam giác đều có một đỉnh hướng xuống. Có thể bắt đầu ở đỉnh trên bên trái, quay rùa sang phải (`RT 90`) rồi vẽ `REPEAT 3 [FD 300 RT 120]`: cạnh đầu nằm ngang ở trên, đỉnh thứ ba ở phía dưới.
- Viền đỏ đều nhau thì hai tam giác phải cùng tâm. Khoảng cách từ tâm tới cạnh của tam giác đều cạnh $a$ là $\dfrac{a}{2\sqrt{3}}$, nên độ dày viền là $\dfrac{300 - 240}{2\sqrt{3}} \approx 17{,}3$ bước rùa. Nhấc bút (`PU`), dịch rùa vào trong đúng khoảng đó theo hướng về tâm rồi vẽ tam giác cạnh 240 cùng hướng.
- Tô màu: chọn màu tô bằng `SETFLOODCOLOR`, đưa rùa vào phần viền (giữa hai tam giác) rồi `FILL` màu đỏ; đưa rùa vào trong tam giác nhỏ rồi `FILL` màu vàng.

## 3. Tính toán

!!! info "Bài thực hành ứng dụng"
    Bài yêu cầu tính bằng câu lệnh MSWLogo, không có lời giải Python.

**Gợi ý hướng làm.** Cứ 2 ngày bèo tấm tăng gấp đôi, nên trong 60 ngày bèo tăng gấp đôi $60 / 2 = 30$ lần. Từ 1 gam ban đầu:

$$1 \times 2^{30} = 1\,073\,741\,824 \text{ gam} = 1\,073\,741{,}824 \text{ kg}.$$

Trong MSWLogo, dùng một biến bắt đầu bằng 1, lặp 30 lần nhân đôi, rồi chia cho 1000 để đổi ra kí-lô-gam:

```text
MAKE "x 1
REPEAT 30 [MAKE "x :x * 2]
PRINT :x / 1000
```

!!! note "Cách hiểu đề dùng cho gợi ý"
    Hiểu là ngày thả bèo là thời điểm bắt đầu, và sau mỗi 2 ngày trọn thì khối lượng bèo nhân đôi, nên 60 ngày ứng với 30 lần nhân đôi. Kết quả $2^{30}$ đã được kiểm tra bằng Python.

## 4. Bảo vệ môi trường xanh sạch đẹp

!!! info "Bài thực hành ứng dụng"
    Bài soạn trình chiếu PowerPoint, không có lời giải Python.

**Gợi ý hướng làm.**

- Tối thiểu 5 slide, ví dụ: (1) tiêu đề và tên em; (2) vì sao cần bảo vệ môi trường; (3)–(4) các việc nhỏ em làm hằng ngày (bỏ rác đúng chỗ, phân loại rác, tiết kiệm điện nước, trồng và chăm sóc cây, không xả rác nơi công cộng...); (5) lời kêu gọi / kết thúc.
- Có **hình tự vẽ** để minh họa (vẽ bằng công cụ Shapes trong PowerPoint hoặc vẽ bằng Paint rồi chèn vào).
- Dùng **hiệu ứng** chuyển trang (Transitions) và hiệu ứng cho đối tượng (Animations), không lạm dụng quá nhiều.
- Lưu đúng tên tệp `moitruong.ppt`.
