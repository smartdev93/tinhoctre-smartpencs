# Đề thi Bảng B - Quận Ngũ Hành Sơn 2025

Hội thi Tin học trẻ quận Ngũ Hành Sơn, năm học 2024–2025 (vòng chọn đội tuyển dự thi cấp TP. Đà Nẵng). Thời gian làm bài: **120 phút**, ngôn ngữ **C++ / Python**.

Thí sinh làm bài trên hệ thống chấm tự động, đọc dữ liệu từ file `input.inp` và ghi kết quả ra file `output.out`.

!!! warning "Nguồn đề"
    Đề được trích từ tài liệu *Tổng hợp chi tiết đề thi Tin học trẻ Ngũ Hành Sơn 2025*. Tài liệu chỉ **mô tả tóm tắt** từng bài, không có định dạng dữ liệu vào/ra và không có ví dụ. Phần "Dữ liệu", "Kết quả" và "Ví dụ" của Bài 2 và Bài 3 do nhóm biên soạn bổ sung để luyện tập, **không phải đề gốc**.

## Tổng quan bài thi

| STT | Bài | Chủ đề | Điểm |
| ---: | --- | --- | ---: |
| 1 | Phân bổ tài nguyên & tối ưu hóa | Số học / vét cạn | 6.0 |
| 2 | Ghép thẻ tạo số lớn nhất | Xâu & sắp xếp tùy biến | 7.0 |
| 3 | Biến đổi xâu đối xứng | Quy hoạch động | 7.0 |

---

## 1. Phân bổ tài nguyên & tối ưu hóa

Bài toán tiếp tế tài nguyên. Tính toán sao cho số lượng sản phẩm chế tạo là lớn nhất dựa trên các điều kiện nguyên liệu đầu vào $N, M$.

- **Ràng buộc:** Subtask 1 (50%): $N, M \le 10^3$; Subtask 2 (50%): $N, M \le 10^9$.
- **Gợi ý của tài liệu gốc:** Subtask 1 dùng vòng lặp vét cạn $O(N)$. Subtask 2 bắt buộc lập công thức toán học $O(1)$ để tránh chạy quá thời gian.

!!! info "Thiếu đề chi tiết"
    Tài liệu nguồn không ghi công thức chế tạo sản phẩm (mỗi sản phẩm cần bao nhiêu nguyên liệu loại nào), nên chưa thể viết đề đầy đủ hay lời giải. Nếu bạn có đề gốc, hãy gửi qua issue trên GitHub.

---

## 2. Ghép thẻ tạo số lớn nhất

Cho $N$ thẻ bài, trên mỗi thẻ ghi một số. Hãy ghép các thẻ bài lại (đặt cạnh nhau theo thứ tự tùy chọn) để tạo thành một số nguyên có giá trị lớn nhất có thể.

### Dữ liệu (bổ sung)

* Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$).
* Dòng 2: $N$ số nguyên không âm, mỗi số có không quá 10 chữ số.

### Kết quả (bổ sung)

* Số lớn nhất tạo được.

### Ví dụ 1

#### Nhập vào

```
3
9 31 34
```

#### In ra

```
93431
```

### Ví dụ 2

#### Nhập vào

```
5
3 30 34 5 9
```

#### In ra

```
9534330
```

### Ví dụ 3

#### Nhập vào

```
3
0 0 0
```

#### In ra

```
0
```

---

## 3. Biến đổi xâu đối xứng

Cho chuỗi $S$. Tìm số lượng ký tự ít nhất cần chèn vào $S$ (ở vị trí bất kỳ) để chuỗi trở thành xâu đối xứng (palindrome).

- **Ràng buộc:** độ dài $N \le 1000$. Độ phức tạp yêu cầu $O(N^2)$.

### Dữ liệu (bổ sung)

* Một dòng chứa chuỗi $S$ gồm các chữ cái thường, không có dấu cách.

### Kết quả (bổ sung)

* Số ký tự ít nhất cần chèn.

### Ví dụ 1

#### Nhập vào

```
abca
```

#### In ra

```
1
```

#### Giải thích

* Chèn `b` hoặc `c`: `abcba` hoặc `acbca`.

### Ví dụ 2

#### Nhập vào

```
abcd
```

#### In ra

```
3
```

#### Giải thích

* Ví dụ: `abcdcba`.

---

!!! tip "Đáp án"
    Tự làm trước, sau đó xem [lời giải tham khảo](dap-an.md).
