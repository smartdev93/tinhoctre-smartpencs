# Đáp án - Bảng A Quận Ngũ Hành Sơn 2017

Gợi ý hướng làm. Xem lại [đề bài](index.md).

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Gà và thỏ | Giả sử tất cả là gà, phần chân dư chia 2 ra số thỏ | – |
| 2 | Vòng quay mặt trời | Vẽ vòng tròn lớn, lặp vẽ nan và hình tròn nhỏ, vẽ hai trụ | – |
| 3 | Chia đất | Chia phần chữ L thành 4 hình chữ L nhỏ | – |
| 4 | Ước mơ của em | Bài trình chiếu PowerPoint | – |

!!! info "Bài thực hành ứng dụng"
    Cả 4 bài của đề này làm bằng MSWLogo, Word và PowerPoint, chấm theo sản phẩm, nên không có lời giải Python. Dưới đây chỉ là gợi ý hướng làm.

---

## 1. Gà và thỏ

**Ý tưởng.** Giả sử cả 700 con đều là gà thì có $700 \times 2 = 1400$ chân, thiếu $1800 - 1400 = 400$ chân. Mỗi con thỏ hơn con gà 2 chân, nên số thỏ là $400 : 2 = 200$, số gà là $700 - 200 = 500$.

Trong MSWLogo, gán số đầu và số chân vào biến (lệnh `MAKE`), tính số thỏ, số gà theo công thức trên rồi in ra bằng lệnh `PRINT` đúng mẫu "So con ga la: ..." và "So con tho la: ...". Chụp màn hình kết quả và dán cùng các câu lệnh vào `gatho.doc`.

!!! warning "Bẫy thường gặp"
    Tự nhẩm đáp số rồi chỉ in ra hằng số: đề yêu cầu viết chương trình **tính** số gà, số thỏ.

## 2. Vòng quay mặt trời

**Ý tưởng.** Đặt rùa ở tâm vòng quay, màu bút xanh (`SETPC 1`).

* Vẽ vòng tròn lớn bán kính 100 quanh tâm.
* Dùng `REPEAT` theo số nan của hình mẫu: mỗi lần đi tới 100 bước (vẽ nan), vẽ hình tròn nhỏ bán kính 15 ở đầu nan, quay về tâm rồi quay một góc bằng $360$ chia số nan.
* Vẽ hai trụ dài 300 đơn vị chéo xuống hai bên từ tâm.
* Viết dòng chữ VONG QUAY MAT TROI bằng lệnh `LABEL`.

Đếm số cabin trong hình mẫu ở bản scan để chọn số lần lặp.

## 3. Chia đất

**Ý tưởng.** Mảnh vườn là hình vuông cạnh 100 đơn vị, chia làm 4 ô vuông cạnh 50; người cha giữ một ô (tô màu 3). Phần còn lại là hình chữ L gồm 3 ô vuông cạnh 50.

Chia mỗi ô vuông cạnh 50 thành 4 ô vuông cạnh 25 thì phần chữ L gồm 12 ô nhỏ. Có thể chia thành 4 hình chữ L nhỏ, mỗi hình gồm 3 ô nhỏ và đồng dạng với hình chữ L lớn (cách giải quen thuộc của bài toán này). Vẽ các đường chia bằng `FD`, `RT`/`LT`, `PU`/`PD`.

Diện tích mỗi phần: $3 \times 25 \times 25 = 1875$ (đơn vị vuông), bằng $\tfrac{3}{4} \times 100 \times 100 : 4$. In kết quả bằng `PRINT`.

## 4. Ước mơ của em

**Ý tưởng.** Ít nhất 5 slide, phông Times New Roman hoặc Arial cỡ từ 14 trở lên, có hình tự vẽ minh họa, có hiệu ứng ở các slide. Lưu đúng tên `uocmo.ppt` và không ghi tên trường, họ tên.
