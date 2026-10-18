# Đề thi Bảng A - Quận Ngũ Hành Sơn 2025

Hội thi Tin học trẻ quận Ngũ Hành Sơn, năm học 2024–2025 (vòng chọn đội tuyển dự thi cấp TP. Đà Nẵng). Thời gian làm bài: **90 phút**, công cụ **Scratch 3.0**.

!!! warning "Nguồn đề"
    Đề được trích từ tài liệu *Tổng hợp chi tiết đề thi Tin học trẻ Ngũ Hành Sơn 2025*. Tài liệu chỉ **mô tả tóm tắt** từng bài, không có định dạng dữ liệu vào/ra và không có ví dụ. Phần "Dữ liệu", "Kết quả" và "Ví dụ" của Bài 2 do nhóm biên soạn bổ sung để luyện tập, **không phải đề gốc**.

## Tổng quan bài thi

| STT | Bài | Nội dung | Điểm |
| ---: | --- | --- | ---: |
| 1 | Vẽ hình học & họa tiết đan lưới | Vẽ hình nghệ thuật, khối tự tạo | 30% |
| 2 | Xử lý danh sách & số học | Danh sách (List) | 40% |
| 3 | Mô phỏng trò chơi tương tác 2D | Game & tọa độ | 30% |

---

## 1. Vẽ hình học & họa tiết đan lưới

Lập trình vẽ họa tiết đan lưới gồm các đường xoay quanh tâm và đan chéo các hình đa giác đều biến thiên theo bán kính.

- **Yêu cầu:** Sử dụng khối tự tạo (Custom Block) có nhận tham số bán kính và số cánh hoa.
- **Điểm kỹ thuật:** Thiết lập vị trí nét vẽ chuẩn xác, sử dụng thuật toán nhấc bút/đặt bút hợp lý để hình không bị lem nét khi đổi vị trí.

---

## 2. Xử lý danh sách & số học

Nhập vào một dãy $N$ số nguyên. Hãy lọc ra các số đối xứng, tính tổng các số lẻ và sắp xếp lại danh sách kết quả theo thứ tự tăng dần.

- **Yêu cầu:** Tạo các danh sách phụ để tách dữ liệu. Không dùng thuật toán sắp xếp quá phức tạp làm vỡ khung hình Scratch.
- **Đánh giá:** Kiểm tra khả năng tư duy logic và thao tác biến số, mảng linh hoạt.

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    Đề gốc không nói rõ "tổng các số lẻ" tính trên cả dãy hay chỉ trên các số đối xứng. Lời giải hiểu là **tổng các số lẻ trong danh sách số đối xứng**. Số đối xứng là số đọc xuôi hay ngược đều như nhau (ví dụ 7, 22, 121).

### Dữ liệu (bổ sung)

* Dòng 1: số nguyên $N$ ($1 \le N \le 100$).
* Dòng 2: $N$ số nguyên không âm.

### Kết quả (bổ sung)

* Dòng 1: các số đối xứng sắp xếp tăng dần, cách nhau một dấu cách. Nếu không có số nào, in `-1`.
* Dòng 2: tổng các số lẻ trong danh sách số đối xứng.

### Ví dụ 1

#### Nhập vào

```
7
121 34 7 1331 22 45 909
```

#### In ra

```
7 22 121 909 1331
2368
```

#### Giải thích

* Số đối xứng: **121, 7, 1331, 22, 909** → sắp xếp: **7, 22, 121, 909, 1331**
* Số lẻ trong đó: $7 + 121 + 909 + 1331 = 2368$

### Ví dụ 2

#### Nhập vào

```
3
12 35 40
```

#### In ra

```
-1
0
```

---

## 3. Mô phỏng trò chơi tương tác 2D

Thiết kế trò chơi hứng/né vật thể rơi tự do. Yêu cầu tính điểm, giới hạn thời gian và tăng độ khó theo level.

- **Yêu cầu:** Xử lý va chạm chính xác theo khoảng cách tọa độ $(x, y)$, thiết lập âm thanh và hiệu ứng thắng/thua.

---

!!! tip "Đáp án"
    Tự làm trước, sau đó xem [lời giải tham khảo](dap-an.md).
