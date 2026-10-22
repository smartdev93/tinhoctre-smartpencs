# Đề thi HSG Tin học THCS - Quảng Ninh 2026

Kỳ thi chọn học sinh giỏi cấp tỉnh THCS năm 2026, Sở Giáo dục và Đào tạo tỉnh Quảng Ninh. **Đề thi chính thức**, môn Tin học, ngày thi **22/01/2026**. Thời gian làm bài: **150 phút** (không kể thời gian giao đề), ngôn ngữ **C++ / Python**.

!!! info "Đề học sinh giỏi"
    Đây là đề thi chọn học sinh giỏi cấp tỉnh, **không thuộc hội thi Tin học trẻ**. Đề được đưa lên site để tham khảo, luyện tập.

## Tổng quan bài thi

| Bài | Tên bài | Tệp chương trình | Tệp dữ liệu | Tệp kết quả | Bộ nhớ | Thời gian / test | Điểm |
| ---: | --- | --- | --- | --- | --- | --- | ---: |
| 1 | Tiền công | `sal.*` | `sal.inp` | `sal.out` | 1024 MB | 1 giây | 6,0 |
| 2 | Giá trị | `val.*` | `val.inp` | `val.out` | 1024 MB | 1 giây | 6,0 |
| 3 | Dãy số | `arr.*` | `arr.inp` | `arr.out` | 1024 MB | 1 giây | 5,0 |
| 4 | Số cặp | `pai.*` | `pai.inp` | `pai.out` | 1024 MB | 2 giây | 3,0 |

Dấu `*` được thay thế bởi `cpp` hoặc `py` của ngôn ngữ lập trình được sử dụng tương ứng là C++ hoặc Python.

---

## 1. Tiền công (6,0 điểm)

Một công nhân tham gia một đợt làm thêm kéo dài liên tiếp trong $d$ ngày. Ngày bắt đầu của đợt làm thêm này là ngày thứ $k$ trong tuần. Tiền công làm việc hàng ngày được quy định như sau:

- Các ngày từ thứ Hai đến thứ Sáu: Tiền công là $a$ đồng mỗi ngày;
- Các ngày thứ Bảy và Chủ Nhật: Tiền công là $b$ đồng mỗi ngày.

**Yêu cầu:** Cho biết các giá trị $k$, $d$, $a$ và $b$, hãy tính tổng số tiền công mà người công nhân đó nhận được sau khi kết thúc $d$ ngày làm việc.

### Dữ liệu

Từ tệp văn bản `sal.inp` gồm một dòng duy nhất chứa 4 số nguyên $k$, $d$, $a$, $b$:

* $k$ là thứ bắt đầu ($2 \le k \le 8$, trong đó 2 là thứ Hai, 3 là thứ Ba, ..., 8 là Chủ Nhật);
* $d$ là tổng số ngày làm việc ($1 \le d \le 1000$);
* $a$, $b$ là tiền công tương ứng ($1 \le a, b \le 10^5$).

### Kết quả

* Ghi ra tệp văn bản `sal.out` một dòng duy nhất chứa một số nguyên là tổng số tiền công nhận được.

Các số trên một dòng của dữ liệu vào được ghi cách nhau bởi một dấu cách.

### Ví dụ

| `sal.inp` | `sal.out` |
| --- | --- |
| `2 4 3 5` | `12` |
| `2 7 2 4` | `18` |
| `4 14 2 3` | `32` |
| `3 12 1 2` | `15` |

### Ràng buộc

* **Ràng buộc 1:** 80% số test ứng với 80% số điểm của bài có $1 \le d \le 5$, $k = 2$;
* **Ràng buộc 2:** 20% số test ứng với 20% số điểm của bài có $6 \le d \le 1000$.

---

## 2. Giá trị (6,0 điểm)

Cho một dãy gồm $n$ số nguyên $a_1, a_2, \ldots, a_n$. Một dãy con liên tiếp là dãy có dạng $a_i, a_{i+1}, \ldots, a_j$ ($1 \le i \le j \le n$), $j - i + 1$ được gọi là độ dài của dãy con đó.

**Yêu cầu:** Hãy tìm độ dài lớn nhất của dãy con liên tiếp chỉ bao gồm đúng $k$ giá trị.

### Dữ liệu

Từ file văn bản `val.inp`:

* Dòng đầu chứa hai số nguyên $n$, $k$ ($2 \le n \le 10^5$; $1 \le k \le 2$);
* Dòng thứ hai chứa $n$ số nguyên $a_1, a_2, \ldots, a_n$ ($1 \le a_i \le 3$; $i = 1, 2, \ldots, n$).

### Kết quả

* Ghi ra file văn bản `val.out` một số nguyên duy nhất là độ dài lớn nhất của dãy con liên tiếp chỉ bao gồm đúng $k$ giá trị.

Các số trên một dòng của dữ liệu vào được ghi cách nhau bởi một dấu cách. Dữ liệu đầu vào đảm bảo bài toán luôn tồn tại đáp án.

### Ví dụ 1

#### Nhập vào (`val.inp`)

```
8 1
1 1 1 2 2 2 2 2
```

#### In ra (`val.out`)

```
5
```

#### Giải thích

* Dãy con thỏa mãn: `2 2 2 2 2`

### Ví dụ 2

#### Nhập vào (`val.inp`)

```
10 1
1 2 2 3 2 3 3 3 1 1
```

#### In ra (`val.out`)

```
3
```

#### Giải thích

* Dãy con thỏa mãn: `3 3 3`

### Ví dụ 3

#### Nhập vào (`val.inp`)

```
10 2
1 3 2 3 3 1 1 3 1 2
```

#### In ra (`val.out`)

```
6
```

#### Giải thích

* Dãy con thỏa mãn: `3 3 1 1 3 1`

### Ràng buộc

* **Ràng buộc 1:** 40% số test ứng với 40% số điểm của bài có $k = 1$; $1 \le a_i \le 2$ với mọi $i = 1, 2, \ldots, n$ và $a_i \le a_{i+1}$ với mọi $i = 1, 2, \ldots, n - 1$;
* **Ràng buộc 2:** 40% số test ứng với 40% số điểm của bài có $k = 1$;
* **Ràng buộc 3:** 20% số test ứng với 20% số điểm của bài có $k = 2$.

!!! note "Ghi chú biên soạn"
    Đề gốc ghi "Cho dãy một gồm $n$ số nguyên", là lỗi đánh máy; site sửa thành "Cho một dãy gồm". "Đúng $k$ giá trị" hiểu là dãy con có đúng $k$ giá trị **khác nhau** (khớp với cả ba ví dụ).

---

## 3. Dãy số (5,0 điểm)

Cho một dãy gồm $n$ số nguyên $a_1, a_2, \ldots, a_n$ và các số nguyên $b$, $k_1$, $k_2$. Bạn được thực hiện tối đa $k_1 + k_2$ phép toán trên các phần tử của dãy để giảm tổng các phần tử của dãy số đã cho.

- **Phép toán loại 1:** Chọn một số $a_i$ bất kì của dãy và thay thế số $a_i$ bằng số $\lfloor a_i / 2 \rfloor$ (chia đôi và lấy phần nguyên, ví dụ: $\lfloor 17 / 2 \rfloor = 8$). Bạn được sử dụng tối đa $k_1$ phép toán loại 1.
- **Phép toán loại 2:** Chọn một số $a_i$ bất kì của dãy và thay thế $a_i$ bằng giá trị lớn nhất của hai số $a_i - b$ và 0 (trừ đi $b$ đơn vị, nếu kết quả âm thì lấy bằng 0). Bạn được sử dụng tối đa $k_2$ phép toán loại 2.

*Quy tắc:* Với mỗi số $a_i$ trong dãy, bạn có thể chọn: không phép toán nào, chỉ phép toán loại 1, chỉ phép toán loại 2, hoặc dùng cả hai phép toán, mỗi phép toán được thực hiện tối đa 1 lần với số $a_i$. Nếu dùng cả hai loại trên cùng một số, bạn có thể thực hiện theo thứ tự nào tùy ý.

**Yêu cầu:** Hãy tìm tổng nhỏ nhất của dãy số sau khi sử dụng tối đa $k_1$ phép toán loại 1 và $k_2$ phép toán loại 2.

### Dữ liệu

Từ tệp văn bản `arr.inp`:

* Dòng đầu chứa 4 số nguyên $n$, $b$, $k_1$, $k_2$ ($1 \le n \le 300$, $1 \le b \le 10^9$, $0 \le k_1, k_2 \le n$);
* Dòng thứ hai chứa $n$ số nguyên dương $a_i$ ($1 \le a_i \le 10^9$).

### Kết quả

Ghi ra tệp văn bản `arr.out`:

* Một số nguyên duy nhất là tổng nhỏ nhất tìm được.

Các số trên một dòng của dữ liệu vào được ghi cách nhau bởi một dấu cách.

### Ví dụ 1

#### Nhập vào (`arr.inp`)

```
7 4 2 0
1 2 1 8 3 5 7
```

#### In ra (`arr.out`)

```
19
```

### Ví dụ 2

#### Nhập vào (`arr.inp`)

```
7 4 2 1
1 2 1 8 3 5 7
```

#### In ra (`arr.out`)

```
15
```

### Ví dụ 3

#### Nhập vào (`arr.inp`)

```
7 9 4 5
19 2 1 8 8 5 5
```

#### In ra (`arr.out`)

```
1
```

#### Giải thích

* Thực hiện phép toán loại 1 với $a_1$ thì $a_1 = \lfloor 19 / 2 \rfloor = 9$.
* Tiếp theo thực hiện 5 phép toán loại 2 với các phần tử $a_1, a_4, a_5, a_6, a_7$ ta được dãy mới: `0, 2, 1, 0, 0, 0, 0`.
* Sau đó thực hiện 3 phép toán loại 1 với các phần tử $a_2, a_3, a_4$ ta được dãy mới: `0, 1, 0, 0, 0, 0, 0` có tổng bằng 1.

### Ví dụ 4

#### Nhập vào (`arr.inp`)

```
7 9 4 4
8 8 8 8 8 8 8
```

#### In ra (`arr.out`)

```
12
```

### Ràng buộc

* **Ràng buộc 1:** 30% số test ứng với 30% số điểm của bài có $k_2 = 0$;
* **Ràng buộc 2:** 30% số test ứng với 30% số điểm của bài có $a_1 = a_2 = \ldots = a_n$;
* **Ràng buộc 3:** 40% số test ứng với 40% số điểm của bài có $n, k_1, k_2 \le 300$, các giá trị đầu vào khác không có ràng buộc gì thêm.

!!! note "Ghi chú biên soạn"
    Bản PDF bị lỗi phông ở ký hiệu phần nguyên (hiển thị thành ký tự lạ, kèm một chữ "số ·" thừa); site viết lại là $\lfloor a_i / 2 \rfloor$. Trong giải thích ví dụ 3, phép loại 1 thứ ba áp dụng cho $a_4$ khi $a_4$ đã bằng 0 nên không làm giảm tổng; cách làm vẫn hợp lệ (dùng đúng 4 phép loại 1 và 5 phép loại 2) và tổng 1 là tối ưu.

---

## 4. Số cặp (3,0 điểm)

Cho hai dãy gồm $n$ số nguyên, dãy thứ nhất gồm các số $a_1, a_2, \ldots, a_n$, dãy thứ hai gồm các số $b_1, b_2, \ldots, b_n$.

**Yêu cầu:** Hãy đếm số cặp chỉ số $(i, j)$ ($1 \le i \le j \le n$) mà số lớn nhất của các số $a_i, a_{i+1}, \ldots, a_j$ bằng số nhỏ nhất của các số $b_i, b_{i+1}, \ldots, b_j$.

### Dữ liệu

Từ tệp văn bản `pai.inp`:

* Dòng đầu tiên chứa số nguyên $n$ ($1 \le n \le 10^5$);
* Dòng thứ hai chứa $n$ số nguyên $a_1, a_2, \ldots, a_n$ ($1 \le |a_i| \le 10^9$);
* Dòng thứ ba chứa $n$ số nguyên $b_1, b_2, \ldots, b_n$ ($1 \le |b_i| \le 10^9$).

### Kết quả

Ghi ra tệp văn bản `pai.out`:

* Một dòng duy nhất là kết quả của bài toán.

Các số trên một dòng của dữ liệu vào được ghi cách nhau bởi một dấu cách.

### Ví dụ 1

#### Nhập vào (`pai.inp`)

```
6
1 2 3 2 1 4
6 7 1 2 3 2
```

#### In ra (`pai.out`)

```
2
```

### Ví dụ 2

#### Nhập vào (`pai.inp`)

```
3
3 3 3
3 3 3
```

#### In ra (`pai.out`)

```
6
```

### Ví dụ 3

#### Nhập vào (`pai.inp`)

```
7
1 2 3 4 8 8 9
2 4 6 8 8 8 9
```

#### In ra (`pai.out`)

```
8
```

### Ví dụ 4

#### Nhập vào (`pai.inp`)

```
10
1 2 3 2 1 3 2 1 2 1
6 7 1 2 3 2 2 3 1 2
```

#### In ra (`pai.out`)

```
4
```

### Ràng buộc

* **Ràng buộc 1:** 25% số test ứng với 25% số điểm của bài có $n \le 100$;
* **Ràng buộc 2:** 25% số test ứng với 25% số điểm của bài có $n \le 5000$;
* **Ràng buộc 3:** 25% số test ứng với 25% số điểm của bài có $n \le 10^5$, $a_1 \le a_2 \le \ldots \le a_n$, $b_1 \le b_2 \le \ldots \le b_n$;
* **Ràng buộc 4:** 25% số test còn lại ứng với 25% số điểm của bài không có ràng buộc gì thêm.

!!! note "Ghi chú biên soạn"
    Ràng buộc $1 \le |a_i|, |b_i| \le 10^9$ nghĩa là các phần tử có thể **âm** (nhưng khác 0).

---

!!! tip "Đáp án"
    Tự làm trước, sau đó xem [lời giải tham khảo](dap-an.md).
