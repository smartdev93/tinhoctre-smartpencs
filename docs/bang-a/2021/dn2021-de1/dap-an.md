# Đáp án - Bảng A TP Đà Nẵng 2021

Gợi ý hướng làm. Xem lại [đề bài](index.md).

Cả 4 bài của đề đều là bài thực hành trên Scratch (vẽ hình, thiết kế trò chơi), nên **không có lời giải Python**. Phần dưới đây là gợi ý hướng làm và các phép tính cần thiết.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Chu vi và diện tích hình tô màu | Vẽ bằng bút; ghép phần tô màu từ các phần hình tròn | – |
| 2 | Mảnh ghép | Khối vẽ hình có tham số (biến độ dài), ghép ô tô, chế độ Turbo | – |
| 3 | Khối lập phương | Vẽ K1, K2; suy luận mặt kề / mặt đối diện | – |
| 4 | Phần mềm học tập | Trò chơi kéo thả, biến điểm, đếm lỗi, đồng hồ 60 giây | – |

---

## 1. Chu vi và diện tích hình tô màu

!!! info "Bài thực hành ứng dụng"
    Bài vẽ hình bằng bút vẽ (Pen) trong Scratch, không có lời giải Python.

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    Đề không ghi tâm của các cung tròn; nhóm biên soạn đọc từ hình vẽ trên bản scan như sau. Gọi A là hình vuông trên bên trái, B là hình vuông trên bên phải, C là hình vuông bên dưới B (cạnh 100).

    - Trong A: cung ¼ đường tròn tâm là **góc dưới bên trái** của A, bán kính 100; phần tô màu là phần của A **nằm ngoài** cung (phía trên bên phải).
    - Trong B: cung ¼ đường tròn tâm là **góc dưới bên trái** của B, bán kính 100; phần tô màu là ¼ hình tròn này.
    - Trong C: nửa đường tròn đường kính là cạnh trên của C (bán kính 50); phần tô màu là nửa hình tròn.

    Nếu hình vẽ trong đề thi thật khác cách đọc này thì các con số dưới đây phải tính lại.

**Diện tích phần tô màu** (theo cách hiểu trên):

- Phần trong A: $100^2 - \dfrac{\pi \cdot 100^2}{4} = 10000 - 2500\pi$.
- Phần trong B: $\dfrac{\pi \cdot 100^2}{4} = 2500\pi$.
- Phần trong C: $\dfrac{\pi \cdot 50^2}{2} = 1250\pi$.

Tổng: $S = 10000 + 1250\pi \approx 13\,926{,}99$ (đơn vị diện tích), với $\pi \approx 3{,}14159$. Nếu lấy $\pi = 3{,}14$ thì $S = 13\,925$.

**Chu vi phần tô màu.** Các đoạn chung giữa A và B, giữa B và C nằm bên trong phần tô màu nên không tính. Đường bao gồm:

- Cạnh trên của A: 100.
- Cung ¼ trong B: $\dfrac{2\pi \cdot 100}{4} = 50\pi$.
- Nửa đường tròn trong C: $\dfrac{2\pi \cdot 50}{2} = 50\pi$.
- Cung ¼ trong A: $50\pi$.

Tổng: $P = 100 + 150\pi \approx 571{,}24$ (đơn vị độ dài). Nếu lấy $\pi = 3{,}14$ thì $P = 571$.

Diện tích đã được kiểm tra lại bằng cách đếm điểm lưới (lưới $2000 \times 2000$ điểm), cho kết quả xấp xỉ 13 927.

**Gợi ý hướng làm.**

- Vẽ 3 hình vuông bằng `lặp lại 4 [di chuyển 100, xoay 90 độ]`.
- Vẽ cung tròn bằng cách đi nhiều bước nhỏ: cung ¼ bán kính $r$ có thể vẽ bằng `lặp lại 90 [di chuyển (r × π / 180), xoay 1 độ]` (mỗi bước đi một đoạn bằng độ dài cung 1°). Nửa đường tròn thì lặp 180 lần.
- Tô màu: Scratch không có lệnh tô vùng; có thể tô bằng cách vẽ nhiều nét bút dày hoặc nhiều đường song song lấp kín vùng, hoặc vẽ phần tô màu thành hình (costume) rồi dùng bút vẽ đường viền.
- In chu vi và diện tích bằng khối `nói` hoặc biến hiển thị trên sân khấu.

---

## 2. Mảnh ghép

!!! info "Bài thực hành ứng dụng"
    Bài vẽ và ghép hình trong Scratch, không có lời giải Python.

**Gợi ý hướng làm.**

- Tạo 3 khối lệnh tự định nghĩa (My Blocks) có tham số: `hình chữ nhật (dài) (rộng)`, `tam giác vuông cân (cạnh góc vuông)`, `hình tròn (bán kính)`. Đề yêu cầu dùng biến cho độ dài để có thể vẽ nhiều kích thước.
- Tam giác vuông cân cạnh góc vuông $a$: đi $a$, xoay 135°, đi $a\sqrt{2}$ (cạnh huyền, theo công thức ở cuối đề), xoay 135°, đi $a$. Hình tròn: lặp 360 lần đi một bước nhỏ và xoay 1°.
- Ghép ô tô theo hình: thân là hình chữ nhật, đầu xe là tam giác vuông cân, hai bánh là hình tròn. Tô màu bằng nét bút dày hoặc dùng costume.
- Cho ô tô chạy: gom ô tô vào một nhân vật (hoặc vẽ lại tại vị trí mới sau mỗi lần `xóa tất cả`), lặp di chuyển cho tổng quãng đường ít nhất 100 đơn vị. Bật chế độ Turbo (Shift + bấm lá cờ trong Scratch 2; menu *Edit → Turbo mode* trong Scratch 3) để vẽ nhanh.

---

## 3. Khối lập phương

!!! info "Bài thực hành ứng dụng"
    Bài vẽ hình khối trong Scratch kèm câu hỏi suy luận, không có lời giải Python.

**Câu hỏi H6 đối diện với hình nào.** Theo cách đọc hình trên bản scan:

- K1 thấy 3 mặt H1 (hình vuông đen, mặt trên), H2 (lục giác lồng nhau, mặt trước), H3 (chữ L, mặt bên phải).
- K2 thấy 3 mặt H4 (hình tia, mặt trước), H3 (chữ L) và H5 (chữ T) ở mặt trên và mặt bên.

Ba mặt nhìn thấy cùng lúc trên một khối lập phương luôn đôi một kề nhau. Vậy H3 kề với H1, H2 (từ K1) và kề với H4, H5 (từ K2), tức là H3 kề với 4 mặt. Một mặt của khối lập phương chỉ kề đúng 4 mặt, mặt còn lại là mặt đối diện. Do đó **H6 đối diện với H3**.

!!! note "Lưu ý"
    Kết luận chỉ dựa vào việc H3 xuất hiện ở cả K1 và K2, còn hai mặt còn lại của K2 là H4 và H5; hướng xoay của từng hình không ảnh hưởng đến kết luận. Hãy đối chiếu lại với hình gốc trong [bản scan](index.md#de-goc-ban-scan).

**Gợi ý vẽ.** Vẽ khối lập phương nhìn xiên: mặt trước là hình vuông, mặt trên và mặt bên là hình bình hành (đi xiên 45°). Vẽ các hình mẫu lên từng mặt bằng costume hoặc bút vẽ; hình trên mặt trên và mặt bên cần được vẽ xiên theo mặt đó.

---

## 4. Phần mềm học tập

!!! info "Bài thực hành ứng dụng"
    Bài thiết kế trò chơi trên Scratch, không có lời giải Python.

**Gợi ý hướng làm.**

- Màn hình chọn mức: phông nền có 2 nút "Mức độ dễ", "Mức độ khó" (là 2 nhân vật). Bấm nút nào thì phát tin `de` hoặc `kho` và chuyển phông nền bức tranh có cả vùng nước và vùng đất.
- Mỗi con vật là một nhân vật, có biến riêng (biến "chỉ cho nhân vật này") `noi_song` = "nước" hoặc "cạn". Cho phép kéo thả (`đặt chế độ kéo thả có thể kéo`).
- Kiểm tra đúng/sai khi thả chuột: dùng màu ở vị trí thả (`chạm vào màu ...?` với màu nước / màu đất) hoặc so tọa độ với vùng nước trên phông nền.
- Mức dễ: hiện ngẫu nhiên 1 con vật kèm thông báo. Thả đúng → "Đúng rồi. Giỏi lắm!" rồi hiện con khác. Thả sai → "Sai rồi. Làm lại nhé!"; sai tiếp thì kết thúc trò chơi.
- Mức khó: hiện 5 con vật ngẫu nhiên, biến `Diem` (+1 khi đúng, −2 khi sai) và biến `SoLanSai`. Đồng hồ 60 giây; hết giờ (hoặc khi đã thả xong cả 5 con) thì nếu `SoLanSai ≤ 3` đổi sang phông nền "Em đã hoàn thành nhiệm vụ", ngược lại phông nền "Em cần cố gắng hơn!", rồi dừng trò chơi.
