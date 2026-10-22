# Đáp án - Bảng A Quận Thanh Khê 2017

Gợi ý hướng làm. Xem lại [đề bài](index.md).

Cả 4 bài đều là bài thực hành bằng MSWLogo hoặc PowerPoint, chấm theo sản phẩm (tệp `.doc`/`.ppt`), nên không có lời giải Python. Các kết quả số bên dưới đã được kiểm tra lại bằng chương trình.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Hoa văn | Vẽ cung tròn lặp lại, tô đỏ bằng `FILL` | – |
| 2 | Đổi tiền | Duyệt số tờ từng loại, in phương án có tổng 100.000 | – |
| 3 | Hộp sữa | Cộng dồn $1 + 2 + \ldots$ đến khi đủ 120 | – |
| 4 | Mùa hè vui | Bài trình chiếu PowerPoint | – |

---

## 1. Hoa văn

!!! info "Bài vẽ MSWLogo"
    Bài chấm theo hình vẽ và câu lệnh, không có lời giải Python.

**Gợi ý hướng làm.**

- Quan sát Hình 1 (xem [bản scan](index.md#de-goc-ban-scan)): hình vuông cạnh 200 được chia lưới, các cánh hoa màu đỏ tạo bởi các cung tròn giao nhau.
- Vẽ hình vuông ngoài bằng `REPEAT 4 [FD 200 RT 90]`.
- Mỗi cánh hoa là phần chung của hai cung tròn; vẽ một cung bằng nhiều bước ngắn (`REPEAT ... [FD ... RT ...]`), viết thành thủ tục rồi lặp lại cho các vị trí.
- Tô màu: nhấc bút đưa rùa vào trong cánh hoa, `SETFLOODCOLOR 4` rồi `FILL`.
- Dán câu lệnh và ảnh chụp hình vẽ vào `hoavan.doc`.

## 2. Đổi tiền

!!! info "Bài lập trình MSWLogo"
    Đề yêu cầu viết lệnh MSWLogo, không có lời giải Python.

**Ý tưởng.** Gọi $a, b, c$ là số tờ loại 10.000, 20.000, 50.000. Cần $10a + 20b + 50c = 100$ (đơn vị nghìn đồng), với $0 \le c \le 2$, $0 \le b \le 5$, $0 \le a \le 10$. Duyệt ba vòng lặp lồng nhau (hoặc duyệt $b, c$ rồi tính $a$), mỗi bộ thỏa mãn thì tăng số thứ tự và in một dòng.

Có tất cả **10 phương án**:

```
1. Loai 10.000: 10 to.     Loai 20.000: 0 to     Loai 50.000: 0 to
2. Loai 10.000: 8 to.     Loai 20.000: 1 to     Loai 50.000: 0 to
3. Loai 10.000: 6 to.     Loai 20.000: 2 to     Loai 50.000: 0 to
4. Loai 10.000: 4 to.     Loai 20.000: 3 to     Loai 50.000: 0 to
5. Loai 10.000: 2 to.     Loai 20.000: 4 to     Loai 50.000: 0 to
6. Loai 10.000: 0 to.     Loai 20.000: 5 to     Loai 50.000: 0 to
7. Loai 10.000: 5 to.     Loai 20.000: 0 to     Loai 50.000: 1 to
8. Loai 10.000: 3 to.     Loai 20.000: 1 to     Loai 50.000: 1 to
9. Loai 10.000: 1 to.     Loai 20.000: 2 to     Loai 50.000: 1 to
10. Loai 10.000: 0 to.     Loai 20.000: 0 to     Loai 50.000: 2 to
```

Thứ tự các dòng phụ thuộc thứ tự vòng lặp; chỉ cần đủ 10 phương án, không trùng.

!!! warning "Bẫy thường gặp"
    - Bỏ sót phương án có một loại tiền bằng 0 tờ (ví dụ chỉ dùng 2 tờ 50.000).
    - Quên đánh số thứ tự ở đầu mỗi dòng.

## 3. Hộp sữa

!!! info "Bài lập trình MSWLogo"
    Đề yêu cầu viết lệnh MSWLogo và vẽ hình, không có lời giải Python.

**Ý tưởng.** Hàng thứ $i$ (tính từ trên xuống) có $i$ hộp. Cộng dồn $1 + 2 + 3 + \ldots$ đến khi tổng bằng 120: $1 + 2 + \ldots + 15 = 15 \times 16 / 2 = 120$, nên hàng dưới cùng có **15 hộp** (15 hàng).

**Gợi ý hướng làm.**

- Dùng biến `n` (số hàng) và biến `tong`; lặp: tăng `n` thêm 1, cộng `n` vào `tong`, dừng khi `tong` = 120; in `n`.
- Vẽ minh họa: viết thủ tục vẽ ô vuông `REPEAT 4 [FD 20 RT 90]`; hàng $i$ vẽ $i$ ô liền nhau, các hàng chồng lên nhau tạo thành hình bậc thang/tam giác (hàng dưới 15 ô, hàng trên cùng 1 ô).

## 4. Mùa hè vui

!!! info "Bài thực hành ứng dụng"
    Bài chấm theo sản phẩm PowerPoint, không có lời giải Python.

**Gợi ý hướng làm.**

- Tối thiểu 5 slide, ví dụ: slide tiêu đề; các dự định (vui chơi, hoạt động hè, về quê thăm ông bà...), mỗi dự định một slide; slide kết.
- Tự vẽ tối đa 3 hình minh họa.
- Thêm hiệu ứng chuyển trang và hiệu ứng cho đối tượng.
- **Không** ghi tên trường và họ tên; lưu đúng tên `muahevui.ppt`.
