# Đáp án - Bảng A Huyện Hòa Vang 2019

Xem lại [đề bài](index.md).

Cả 3 bài là bài thực hành Scratch (vẽ hình, làm hoạt hình), không phải bài lập trình giải thuật có dữ liệu vào/ra, nên không có lời giải Python. Dưới đây là gợi ý hướng làm.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Vẽ hình | Lặp vẽ lục giác đều cạnh 25, 50, 75, 100 quanh cùng tâm + 3 đường chéo | – |
| 2 | Lưới ô vuông | Hai vòng lặp vẽ lưới $5 \times 5$, tô ô trên đường chéo; diện tích $20 \times 40 \times 40$ | – |
| 3 | Mô phỏng bể cá | Nhiều nhân vật, mỗi nhân vật một kịch bản chuyển động; điều khiển cá mập bằng phím | – |

---

## 1. Vẽ hình

!!! info "Bài thực hành ứng dụng"
    Bài vẽ hình bằng Scratch (khối bút vẽ), không có lời giải Python.

**Gợi ý hướng làm.**

- Một lục giác đều cạnh $a$: lặp 6 lần [đi $a$ bước, quay 60°]. Lục giác đều có bán kính (khoảng cách từ tâm đến đỉnh) **bằng đúng cạnh** $a$.
- Vì vậy, để vẽ lục giác cạnh $a$ có tâm ở điểm O: từ O đi thẳng $a$ bước tới một đỉnh, quay 120°, rồi vẽ lục giác; xong quay về O (nhấc bút khi đi về).
- Lặp với $a = 25, 50, 75, 100$ (mỗi lần tăng 25).
- Ba đường chéo đi qua tâm: từ O vẽ 6 đoạn dài 100 bước theo các hướng cách nhau 60° (mỗi đoạn đi ra rồi quay về O), chúng nối tâm với 6 đỉnh của lục giác lớn nhất và đi qua đỉnh của các lục giác nhỏ hơn.

## 2. Lưới ô vuông

!!! info "Bài thực hành ứng dụng"
    Bài vẽ hình bằng Scratch, không có lời giải Python.

**Gợi ý hướng làm.**

- a) Dùng hai vòng lặp lồng nhau theo hàng $i$ và cột $j$ (từ 1 đến 5), vẽ ô vuông cạnh 40 tại vị trí tương ứng. Ô có $i = j$ thì tô màu (ví dụ vẽ nhiều nét sát nhau hoặc dùng bút có độ dày lớn).
- b) Lưới có $5 \times 5 = 25$ ô, trong đó 5 ô trên đường chéo được tô màu, còn $25 - 5 = 20$ ô không tô màu. Mỗi ô có diện tích $40 \times 40 = 1600$ (đơn vị vuông). Tổng diện tích các ô không tô màu là $20 \times 1600 = 32\,000$ (đơn vị vuông).

Chương trình Scratch có thể dùng biến đếm số ô không tô màu rồi cho nhân vật "nói" kết quả.

!!! note "Cách hiểu đề dùng cho gợi ý"
    Số ô tô màu (5 ô trên đường chéo của lưới $5 \times 5$) được đếm trên hình 2 của bản scan. Đề không nói đơn vị diện tích, nên kết quả ghi theo "đơn vị vuông" (bình phương của đơn vị độ dài trong đề).

## 3. Mô phỏng bể cá

!!! info "Bài thực hành ứng dụng"
    Bài làm hoạt hình bằng Scratch, không có lời giải Python.

**Gợi ý hướng làm.**

- a) Chọn hoặc vẽ phông nền dưới nước cho sân khấu.
- b) Thêm các nhân vật: cá mập, các loại cá, sao biển, sứa, bong bóng; mỗi nhân vật có vài trang phục để đổi hình dạng (tạo cảm giác đang bơi).
- c) Kịch bản cho từng nhân vật, dùng vòng lặp liên tục:
    - Cá mập và sao biển: di chuyển từ trái qua phải (tăng $x$), chạm cạnh phải thì quay lại bên trái.
    - Cá nhỏ: di chuyển từ phải qua trái (giảm $x$).
    - Sứa và bong bóng: trôi từ dưới lên (tăng $y$), lên tới mặt nước thì quay lại đáy.
    - Cá mập: khi bấm phím mũi tên lên / xuống thì thay đổi $y$ để bơi lên / bơi xuống. Khi chạm cá nhỏ thì cá nhỏ ẩn đi (bị bắt) hoặc xuất hiện lại ở vị trí khác.
