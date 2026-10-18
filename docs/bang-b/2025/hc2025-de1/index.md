# Đề thi Bảng B - Quận Hải Châu 2025

Hội thi Tin học trẻ quận Hải Châu (TP. Đà Nẵng), năm 2025. Thời gian làm bài: **120 phút**, ngôn ngữ **C++ / Python**.

Thi lập trình trực tuyến, chấm tự động trên hệ thống CodeMath, môi trường Linux (GCC 11.2 / Python 3.10). Giới hạn thời gian **1.0 giây/test (C++)** và **2.0 giây/test (Python)**, bộ nhớ **256 MB**. Code mẫu trong tài liệu đọc dữ liệu từ bàn phím và in ra màn hình.

!!! warning "Nguồn đề"
    Đề được tổng hợp từ hai tài liệu: *Đề thi chi tiết - Bảng B (THCS), Hội thi Tin học trẻ quận Hải Châu 2025* và *Tổng hợp đề thi & đáp án - Quận Hải Châu 2025*. Tài liệu chỉ **mô tả tóm tắt** từng bài kèm code mẫu, không có định dạng dữ liệu vào/ra và không có ví dụ. Các phần "Dữ liệu", "Kết quả", "Ví dụ" do nhóm biên soạn bổ sung dựa trên code mẫu, **không phải đề gốc**.

## Tổng quan bài thi

| STT | Bài | Tên file | Chủ đề | Điểm |
| ---: | --- | --- | --- | ---: |
| 1 | Cặp số thân thiện | `FRIEND.CPP` / `.PY` | Lý thuyết số / phân tích ước số | 25 |
| 2 | Nén xâu đảo ngược | `COMPRESS.CPP` / `.PY` | Xử lý xâu | 25 |
| 3 | Đoạn con có tổng lớn nhất | `MAXSUB.CPP` / `.PY` | Mảng / Kadane / quy hoạch động | 25 |
| 4 | Sắp đặt hàng hóa | `ARRANGE.CPP` / `.PY` | Tham lam / hai con trỏ | 25 |

---

## 1. Cặp số thân thiện (FRIEND)

Hai số nguyên dương được gọi là thân thiện nếu tổng các ước số thực sự (không kể chính nó) của số này bằng số kia và ngược lại. Cho hai số $A$ và $B$. Hãy kiểm tra xem $A$ và $B$ có phải là cặp số thân thiện hay không.

- **Ràng buộc:** $A, B \le 10^{12}$. Yêu cầu độ phức tạp $O(\sqrt{N})$.

### Dữ liệu (bổ sung)

* Một dòng gồm hai số nguyên dương $A$ và $B$.

### Kết quả (bổ sung)

* In `YES` nếu $A$ và $B$ là cặp số thân thiện, ngược lại in `NO`.

### Ví dụ 1

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

### Ví dụ 2

#### Nhập vào

```
10 20
```

#### In ra

```
NO
```

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    Đề không nói $A$ và $B$ có phải khác nhau hay không. Theo đúng câu chữ của đề và code mẫu, $A = B = 6$ (số hoàn hảo, $1 + 2 + 3 = 6$) cho kết quả `YES`. Trong toán học, "cặp số thân thiện" thường yêu cầu hai số khác nhau; nếu đề chính thức yêu cầu vậy thì cần thêm điều kiện $A \ne B$.

---

## 2. Nén xâu đảo ngược (COMPRESS)

Cho xâu $S$ gồm các chữ cái tiếng Anh viết thường. Hãy thực hiện nén xâu theo quy tắc: các ký tự liên tiếp giống nhau sẽ được thay thế bằng số lượng lặp lại + ký tự đó, sau đó đảo ngược xâu kết quả.

- **Ràng buộc:** độ dài $|S| \le 10^5$.

### Dữ liệu (bổ sung)

* Một dòng chứa xâu $S$.

### Kết quả (bổ sung)

* Xâu sau khi nén và đảo ngược.

### Ví dụ 1

#### Nhập vào

```
aaabcc
```

#### In ra

```
c2b1a3
```

#### Giải thích

* Nén: `aaa` → `3a`, `b` → `1b`, `cc` → `2c`, được `3a1b2c`.
* Đảo ngược cả xâu: `c2b1a3`.

### Ví dụ 2

#### Nhập vào

```
aaaaaaaaaaaa
```

#### In ra

```
a21
```

#### Giải thích

* 12 chữ `a` nén thành `12a`, đảo ngược từng ký tự được `a21` (chữ số của 12 cũng bị đảo).

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    "Đảo ngược xâu kết quả" được hiểu là đảo **từng ký tự** của xâu nén, đúng như code mẫu của tài liệu (`reverse` cả xâu). Vì vậy khi một ký tự lặp từ 10 lần trở lên, các chữ số của số lần lặp cũng bị đảo (ví dụ `12a` → `a21`).

---

## 3. Đoạn con có tổng lớn nhất (MAXSUB)

Cho mảng $A$ gồm $N$ số nguyên. Tìm đoạn con (gồm các phần tử liên tiếp) có tổng lớn nhất.

- **Ràng buộc:** $N \le 10^5$. Áp dụng thuật toán Kadane $O(N)$.

### Dữ liệu (bổ sung)

* Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$).
* Dòng 2: $N$ số nguyên $A_1, A_2, \ldots, A_N$ ($|A_i| \le 10^9$).

### Kết quả (bổ sung)

* Tổng lớn nhất của một đoạn con **khác rỗng**.

### Ví dụ 1

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

### Ví dụ 2

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

Có $N$ kiện hàng, kiện thứ $i$ có trọng lượng $W_i$, cần xếp vào các thùng có tải trọng $K$. Tìm số thùng tối thiểu.

- **Gợi ý của tài liệu:** tham lam + hai con trỏ.

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    Tài liệu không ghi giới hạn số kiện mỗi thùng, nhưng code mẫu (hai con trỏ, mỗi thùng nhận kiện nặng nhất và tối đa thêm một kiện nhẹ nhất) chỉ đúng khi **mỗi thùng chứa tối đa 2 kiện**. Nếu không có giới hạn này, bài trở thành bài toán xếp thùng (bin packing) tổng quát, không có thuật toán nhanh, và cách hai con trỏ cho kết quả sai (ví dụ $K = 10$, ba kiện nặng $1$: cần 1 thùng, hai con trỏ ra 2). Đề dưới đây dùng giả định mỗi thùng tối đa 2 kiện.

### Dữ liệu (bổ sung)

* Dòng 1: hai số nguyên $N$ và $K$ ($1 \le N \le 10^5$, $1 \le K \le 10^9$).
* Dòng 2: $N$ số nguyên $W_1, \ldots, W_N$ ($1 \le W_i \le K$).
* Mỗi thùng chứa **tối đa 2 kiện** và tổng trọng lượng không vượt quá $K$.

### Kết quả (bổ sung)

* Số thùng ít nhất cần dùng.

### Ví dụ 1

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

### Ví dụ 2

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
