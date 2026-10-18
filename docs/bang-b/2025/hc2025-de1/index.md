# Đề thi Bảng B - Quận Hải Châu 2025

Hội thi Tin học trẻ quận Hải Châu (TP. Đà Nẵng), năm 2025. Thời gian làm bài: **120 phút**, ngôn ngữ **C++ / Python**.

Thi lập trình trực tuyến, chấm tự động trên hệ thống CodeMath, môi trường Linux (GCC 11.2 / Python 3.10). Giới hạn thời gian **1.0 giây/test (C++)** và **2.0 giây/test (Python)**, bộ nhớ **256 MB**. Code mẫu trong tài liệu đọc dữ liệu từ bàn phím và in ra màn hình.

!!! warning "Nguồn đề"
    Đề được tổng hợp từ hai tài liệu: *Đề thi chi tiết - Bảng B (THCS), Hội thi Tin học trẻ quận Hải Châu 2025* (bản có ghi chú biên soạn) và *Tổng hợp đề thi & đáp án - Quận Hải Châu 2025*. Đây là tài liệu ôn luyện **tổng hợp lại**, không phải văn bản đề chính thức của ban tổ chức: tài liệu tự ghi là có "các ví dụ minh họa và giả định thuật toán chuẩn hóa bổ sung" (điều kiện $A \ne B$ ở Bài 1, tối đa 2 kiện/thùng ở Bài 4). Những phần ghi "(bổ sung)" bên dưới do nhóm biên soạn site thêm vào, **không có trong tài liệu**.

## Tổng quan bài thi

| STT | Bài | Tên file | Chủ đề | Điểm |
| ---: | --- | --- | --- | ---: |
| 1 | Cặp số thân thiện | `FRIEND.CPP` / `.PY` | Lý thuyết số / phân tích ước số | 25 |
| 2 | Nén xâu đảo ngược | `COMPRESS.CPP` / `.PY` | Xử lý xâu | 25 |
| 3 | Đoạn con có tổng lớn nhất | `MAXSUB.CPP` / `.PY` | Mảng / Kadane / quy hoạch động | 25 |
| 4 | Sắp đặt hàng hóa | `ARRANGE.CPP` / `.PY` | Tham lam / hai con trỏ (tối đa 2 kiện/thùng) | 25 |

---

## 1. Cặp số thân thiện (FRIEND)

Hai số nguyên dương được gọi là thân thiện nếu tổng các ước số thực sự (không kể chính nó) của số này bằng số kia và ngược lại. Cho hai số $A$ và $B$. Hãy kiểm tra xem $A$ và $B$ có phải là cặp số thân thiện hay không.

- **Ràng buộc:** $1 \le A, B \le 10^{12}$. Yêu cầu độ phức tạp $O(\sqrt{N})$.

### Dữ liệu

* Hai số nguyên $A$ và $B$ (bổ sung: trên một dòng).

### Kết quả

* In `YES` nếu tổng ước thực sự của $A$ bằng $B$, tổng ước thực sự của $B$ bằng $A$, **đồng thời $A \ne B$**. Ngược lại in `NO`.

!!! note "Lưu ý đính chính của tài liệu"
    Test `1 1` in `NO` vì tổng ước thực sự của 1 bằng 0. Test `6 6` in `NO` do điều kiện $A \ne B$ (6 là số hoàn hảo: $1 + 2 + 3 = 6$).

### Ví dụ 1 (bổ sung)

#### Nhập vào

```
220 284
```

#### In ra

```
YES
```

#### Giải thích

* Ước thực sự của 220: $1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284$.
* Ước thực sự của 284: $1 + 2 + 4 + 71 + 142 = 220$.

### Ví dụ 2 (bổ sung)

#### Nhập vào

```
10 20
```

#### In ra

```
NO
```

### Ví dụ 3

#### Nhập vào

```
6 6
```

#### In ra

```
NO
```

#### Giải thích

* Tổng ước thực sự của 6 bằng 6, nhưng $A = B$ nên không phải cặp số thân thiện.

---

## 2. Nén xâu đảo ngược (COMPRESS)

Cho xâu $S$ gồm các chữ cái tiếng Anh viết thường. Hãy thực hiện nén xâu theo quy tắc: các ký tự liên tiếp giống nhau sẽ được thay thế bằng số lượng lặp lại + ký tự đó, sau đó đảo ngược **toàn bộ** xâu kết quả (bao gồm cả chữ số).

- **Ràng buộc:** độ dài $|S| \le 10^5$.

### Dữ liệu (bổ sung)

* Một dòng chứa xâu $S$.

### Kết quả (bổ sung)

* Xâu sau khi nén và đảo ngược.

### Ví dụ 1

#### Nhập vào

```
aabccc
```

#### In ra

```
c3b1a2
```

#### Giải thích

* Nén: `aa` → `2a`, `b` → `1b`, `ccc` → `3c`, được `2a1b3c`.
* Đảo ngược toàn bộ: `c3b1a2`.

### Ví dụ 2 (bổ sung)

#### Nhập vào

```
aaaaaaaaaaaa
```

#### In ra

```
a21
```

#### Giải thích

* 12 chữ `a` nén thành `12a`, đảo ngược toàn bộ được `a21` (chữ số của 12 cũng bị đảo).

---

## 3. Đoạn con có tổng lớn nhất (MAXSUB)

Cho mảng $A$ gồm $N$ số nguyên. Tìm đoạn con (gồm các phần tử liên tiếp) có tổng lớn nhất.

- **Ràng buộc:** $N \le 10^5$. Áp dụng thuật toán Kadane $O(N)$.

### Dữ liệu

* Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$).
* Dòng 2: $N$ số nguyên $A_1, A_2, \ldots, A_N$ ($|A_i| \le 10^9$).

### Kết quả

* Tổng lớn nhất của một đoạn con liên tiếp **khác rỗng**.

### Ví dụ 1 (bổ sung)

#### Nhập vào

```
9
-2 1 -3 4 -1 2 1 -5 4
```

#### In ra

```
6
```

#### Giải thích

* Đoạn `4 -1 2 1` có tổng 6.

### Ví dụ 2 (bổ sung)

#### Nhập vào

```
3
-5 -2 -8
```

#### In ra

```
-2
```

#### Giải thích

* Mọi phần tử đều âm, đoạn tốt nhất chỉ gồm phần tử lớn nhất là $-2$.

---

## 4. Sắp đặt hàng hóa (ARRANGE)

Cho $N$ kiện hàng có trọng lượng $W_i$ và các thùng hàng có tải trọng tối đa $K$. Tìm số thùng tối thiểu.

- **Gợi ý của tài liệu:** tham lam + hai con trỏ.

!!! note "Giả định bổ sung của tài liệu"
    Thuật toán hai con trỏ chỉ đúng khi **mỗi thùng chứa tối đa 2 kiện hàng**. Nếu mỗi thùng chứa được nhiều kiện tùy ý, bài trở thành bài toán xếp thùng (Bin Packing), thuộc lớp NP-khó, và cách hai con trỏ cho kết quả sai (ví dụ $K = 10$, ba kiện nặng $1$: cần 1 thùng, hai con trỏ ra 2). Đề dưới đây theo giả định tối đa 2 kiện/thùng.

### Dữ liệu (bổ sung)

* Dòng 1: hai số nguyên $N$ và $K$ ($1 \le N \le 10^5$, $1 \le K \le 10^9$).
* Dòng 2: $N$ số nguyên $W_1, \ldots, W_N$ ($1 \le W_i \le K$).
* Mỗi thùng chứa **tối đa 2 kiện** và tổng trọng lượng không vượt quá $K$.

### Kết quả (bổ sung)

* Số thùng ít nhất cần dùng.

### Ví dụ 1 (bổ sung)

#### Nhập vào

```
4 10
1 2 9 8
```

#### In ra

```
2
```

#### Giải thích

* Thùng 1: kiện 9 và 1. Thùng 2: kiện 8 và 2.

### Ví dụ 2 (bổ sung)

#### Nhập vào

```
5 10
5 5 5 5 5
```

#### In ra

```
3
```

#### Giải thích

* Hai thùng chứa 2 kiện 5, thùng thứ ba chứa kiện còn lại.

---

!!! tip "Đáp án"
    Tự làm trước, sau đó xem [lời giải tham khảo](dap-an.md).
