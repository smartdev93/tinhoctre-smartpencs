# Đáp án - Bảng A Quận Ngũ Hành Sơn 2025

Lời giải tham khảo bằng Python 3. Xem lại [đề bài](index.md).

Đề thi chính thức làm bằng **Scratch 3.0**. Code Python dưới đây giúp hiểu thuật toán; khi làm trên Scratch, mỗi hàm Python tương ứng một khối tự tạo, mỗi `list` tương ứng một Danh sách.

| STT | Bài | Ý tưởng | Lời giải Python |
| ---: | --- | --- | --- |
| 1 | Họa tiết đan lưới | Khối tự tạo vẽ đa giác đều, xoay quanh tâm | Minh họa bằng `turtle` |
| 2 | Xử lý danh sách | Đảo chữ số + sắp xếp chèn | Có, $O(N^2)$ |
| 3 | Trò chơi 2D | Va chạm theo khoảng cách tọa độ | Không (bài thiết kế game trên Scratch) |

---

## 1. Vẽ hình học & họa tiết đan lưới

**Ý tưởng.**

- Khối `đa giác (bán kính, số cạnh)`: từ tâm, nhấc bút đi ra một đoạn bằng bán kính, đặt bút và vẽ đa giác đều. Cạnh đa giác nội tiếp có độ dài $2R \sin(\pi / n)$, mỗi lần quay $360 / n$ độ.
- Khối `họa tiết (bán kính, số cánh hoa)`: lặp *số cánh hoa* lần, mỗi lần vẽ một đa giác rồi quay $360 / \text{số cánh hoa}$ độ quanh tâm.
- Gọi khối họa tiết với nhiều bán kính khác nhau để tạo lưới đan.

!!! warning "Bẫy thường gặp"
    Quên **nhấc bút** khi đưa bút về tâm hoặc quên trả lại **hướng ban đầu** sau mỗi đa giác. Hình sau sẽ bị lệch hoặc có nét thừa. Trên Scratch, lưu `x`, `y`, `hướng` vào biến trước khi vẽ và khôi phục sau khi vẽ.

Bài này không có đáp án duy nhất; code dưới đây chỉ là một cách minh họa bằng thư viện `turtle` (chạy trên máy tính, mở cửa sổ vẽ).

```python title="hoatiet.py"
--8<-- "bang-a/2025/nhs2025-de1/sol/hoatiet.py"
```

## 2. Xử lý danh sách & số học

**Ý tưởng.**

1. **Kiểm tra số đối xứng** bằng cách đảo chữ số: lặp lấy `x mod 10` ghép vào số đảo, rồi chia nguyên `x` cho 10. Số đối xứng khi số đảo bằng chính nó. Trên Scratch có thể dùng khối `chữ cái thứ i của` để so sánh từ hai đầu.
2. **Danh sách phụ:** duyệt dãy, số nào đối xứng thì thêm vào danh sách `đối xứng`.
3. **Sắp xếp chèn:** với $N \le 100$, sắp xếp chèn hoặc sắp xếp chọn là đủ nhanh và dễ dựng bằng khối `lặp lại cho đến khi`.
4. **Tổng số lẻ:** duyệt danh sách đã lọc, cộng các số có `x mod 2 = 1`.

!!! note "Cách hiểu đề"
    Lời giải theo cách hiểu đã ghi ở [đề bài](index.md): tổng các số lẻ **trong danh sách số đối xứng**. Nếu ban tổ chức yêu cầu tổng các số lẻ của **cả dãy**, chỉ cần đổi vòng cộng sang duyệt `arr`.

```python title="doixung.py"
--8<-- "bang-a/2025/nhs2025-de1/sol/doixung.py"
```

## 3. Mô phỏng trò chơi tương tác 2D

Bài thiết kế game trên Scratch, chấm theo sản phẩm nên không có đáp án Python. Gợi ý các điểm kỹ thuật:

- **Vật rơi:** dùng bản sao (clone), xuất hiện ở `x` ngẫu nhiên trên đỉnh sân khấu, mỗi khung hình giảm `y` theo biến `tốc độ`.
- **Va chạm theo tọa độ:** coi là chạm khi $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2} < r_1 + r_2$ (hoặc dùng khối `khoảng cách đến`).
- **Level:** khi điểm đạt mốc, tăng `tốc độ` hoặc giảm thời gian giữa hai lần tạo vật rơi.
- **Thời gian:** dùng `đồng hồ bấm giờ` có sẵn, hết giờ thì phát tín hiệu thắng/thua.
