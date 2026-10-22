# Đề thi Bảng C - Chung kết toàn quốc 2021

Hội thi Tin học trẻ toàn quốc năm 2021, **đề chính thức vòng chung kết**, Bảng C - Trung học phổ thông. Ngày thi: **21/11/2021**. Thời gian làm bài: **180 phút** (không kể thời gian phát đề), ngôn ngữ **Pascal / C++ / Python**.

Dữ liệu vào từ thiết bị vào chuẩn, kết quả ghi ra thiết bị ra chuẩn. Đề không ghi giới hạn thời gian và bộ nhớ.

## Tổng quan bài thi

| STT | Bài | Tên file | Điểm |
| ---: | --- | --- | ---: |
| 1 | Bài tập | `tasks.*` | 100 |
| 2 | Bài khó | `dtask.*` | 100 |
| 3 | Xâu con | `subseq.*` | 100 |
| 4 | Cắt bánh | `cutcake.*` | 100 |

Dấu `*` được thay thế bởi `pas`/`cpp`/`py` của ngôn ngữ lập trình được sử dụng tương ứng là Pascal/C++/Python.

---

## 1. Bài tập

Hồng đã soạn được $n$ bài tập Tin học, bài thứ $i$ $(1 \le i \le n)$ có độ khó là số nguyên dương $c_i$. Hồng được cô giáo yêu cầu gửi $m$ bài tập lên hệ thống luyện tập trực tuyến để tập huấn cho một nhóm các em học sinh khóa dưới. Nếu $m < n$, khi đó, Hồng phải loại bỏ $n - m$ bài tập, ngược lại nếu $m > n$ thì Hồng phải soạn thêm $m - n$ bài tập với độ khó là số nguyên dương. Khi đưa lên hệ thống $m$ bài tập, Hồng sẽ sắp xếp các bài theo độ khó tăng dần, gọi $d$ là chênh lệch độ khó lớn nhất của hai bài tập liên tiếp. Hồng mong muốn giá trị $d$ nhỏ nhất có thể.

**Yêu cầu:** Cho $n$ bài tập với độ khó là $c_1, c_2, \ldots, c_n$ và số $m$, hãy tìm giá trị $d$ nhỏ nhất.

### Dữ liệu

* Dòng đầu gồm hai số nguyên dương $n, m$ $(2 \le m, n \le 10^5;\ m \ne n)$;
* Dòng thứ hai gồm $n$ số nguyên dương $c_1, c_2, \ldots, c_n$ $(c_i \le 10^9,\ 1 \le i \le n)$.

### Kết quả

* Một dòng chứa một số nguyên $d$ tìm được.

### Ví dụ 1

#### Nhập vào

```
5 4
8 5 9 10 10
```

#### In ra

```
1
```

### Ví dụ 2

#### Nhập vào

```
3 4
8 6 9
```

#### In ra

```
1
```

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    Đề không nói bài soạn thêm có được trùng độ khó với bài đã có hay không. Lời giải cho phép trùng (đề chỉ yêu cầu độ khó là số nguyên dương, và ví dụ 1 cũng có hai bài cùng độ khó 10), nên khi $m > n$ các bài thừa có thể đặt trùng một độ khó sẵn có mà không làm tăng $d$. Theo cách hiểu này, $d$ có thể bằng 0.

---

## 2. Bài khó

Một bài toán khó trong danh sách các bài mà Hồng lựa chọn để tập huấn cho các em học sinh khóa dưới như sau:

Cho hai số nguyên dương $n, t$, cần tìm một bộ gồm ít số nguyên dương nhất, giả sử bộ tìm được gồm $k$ số nguyên dương $a_1, a_2, \ldots, a_k$ thì:

$$(a_1 + t) \times (a_2 + t) \times \ldots \times (a_k + t) = n \times a_1 \times a_2 \times \ldots \times a_k.$$

**Yêu cầu:** Cho hai số nguyên dương $n, t$, hãy tìm số nguyên dương $k$ nhỏ nhất thỏa mãn.

### Dữ liệu

* Một dòng chứa hai số nguyên $n, t$ $(n, t \le 1000)$.

### Kết quả

* Một dòng chứa một số nguyên $k$ là số lượng số ít nhất để tồn tại bộ gồm $k$ số nguyên dương thỏa mãn, nếu không tồn tại ghi số $-1$.

### Ví dụ

#### Nhập vào

```
4 1
```

#### In ra

```
2
```

#### Giải thích (bổ sung)

* Chọn $a_1 = a_2 = 1$: $(1 + 1) \times (1 + 1) = 4 = 4 \times 1 \times 1$. Với $k = 1$ thì $(a_1 + 1) = 4 a_1$ vô nghiệm nguyên dương.

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    Đề yêu cầu $k$ là số nguyên dương. Mỗi thừa số $\frac{a_i + t}{a_i}$ luôn lớn hơn 1, nên với $n = 1$ không có bộ nào thỏa mãn và lời giải in $-1$. Với $n \ge 2$ luôn có nghiệm (xem đáp án), nên $-1$ chỉ xảy ra khi $n = 1$.

---

## 3. Xâu con

Xét xâu $S$ là một xâu chỉ gồm các kí tự in hoa. Một xâu con của xâu $S$ là xâu thu được khi xoá một số kí tự (hoặc có thể là không xóa kí tự nào) khỏi xâu $S$ và giữ nguyên thứ tự các kí tự còn lại. Ví dụ, xâu $ABC$ có các xâu con là $A, AC, BC, ABC$ nhưng $BA$ hay $CAB$ không phải là xâu con của xâu $ABC$. Dễ thấy, xâu $S$ độ dài $N$ sẽ có $2^N - 1$ xâu con không rỗng.

Để đánh giá độ lặp lại của các xâu con này, Hồng định nghĩa hàm $f$: $f(S) = \sum_{s \in w(S)} r(s)^2 \times |s|$, trong đó $w(S)$ là tập các xâu con khác rỗng của $S$, $r(s)$ là số lần lặp của $s$, $|s|$ là độ dài xâu $s$.

Ví dụ xét $S = ABAB$, các xâu con của $S$ bao gồm $A$ (2 lần), $B$ (2 lần), $AB$ (3 lần) và $AA, BB, BA, AAB, ABB, ABA, BAB, ABAB$ mỗi xâu xuất hiện 1 lần. Khi đó:

$$
\begin{aligned}
f(S) = {} & 2^2 \times 1 + 2^2 \times 1 + 3^2 \times 2 \\
& + 1^2 \times 2 + 1^2 \times 2 + 1^2 \times 2 \\
& + 1^2 \times 3 + 1^2 \times 3 + 1^2 \times 3 + 1^2 \times 3 + 1^2 \times 4 = 48
\end{aligned}
$$

**Yêu cầu:** Cho xâu $S$, hãy tính $f(S)$. Vì $f(S)$ có thể rất lớn, Hồng cần đưa ra $f(S) \,\%\, (10^9 + 7)$, trong đó $\%$ là phép chia lấy dư.

### Dữ liệu

* Một dòng chứa xâu $S$ chỉ gồm kí tự in hoa có độ dài không quá 200.

### Kết quả

* Một dòng chứa một số nguyên là giá trị $f(S) \,\%\, (10^9 + 7)$.

### Ví dụ

#### Nhập vào

```
ABAB
```

#### In ra

```
48
```

### Ràng buộc

* Có 20% số test ứng với 20% số điểm của bài thỏa mãn: $|S| \le 20$;
* Có 15% số test khác ứng với 15% số điểm của bài thỏa mãn: $S$ gồm các kí tự giống nhau;
* Có 30% số test khác ứng với 30% số điểm của bài thỏa mãn: $s_i \le s_j$ nếu $i < j$;
* Có 35% số test còn lại ứng với 35% số điểm của bài thỏa mãn: $|S| \le 200$.

---

## 4. Cắt bánh

Vào ngày nhà giáo Việt Nam 20.11 năm nay, Hồng đã làm một chiếc bánh để chúc mừng mẹ. Chiếc bánh có dạng là một hình đa giác đều gồm $n$ đỉnh, các đỉnh được đánh số từ 1 đến $n$ theo chiều kim đồng hồ. Sau khi chúc mừng mẹ, em Phúc đề xuất cắt bánh bằng $m$ lần cắt bánh, lần cắt thứ $k$ đi qua hai đỉnh phân biệt $i_k, j_k$ $(1 \le k \le m)$ và đố mọi người có bao nhiêu miếng bánh sau khi cắt.

**Yêu cầu:** Cho biết các lần cắt bánh, hãy đếm số miếng bánh sau khi thực hiện $m$ lần cắt bánh.

### Dữ liệu

* Dòng đầu chứa hai số nguyên $n, m$ $(n \le 50)$;
* Dòng thứ $k$ $(1 \le k \le m)$ chứa hai số nguyên $i_k, j_k$ mô tả lần cắt thứ $k$ $(1 \le i_k, j_k \le n$ và $i_k \ne j_k)$.

### Kết quả

* Một dòng chứa một số nguyên là số miếng bánh sau khi thực hiện $m$ lần cắt bánh.

### Ví dụ

#### Nhập vào

```
4 1
1 3
```

#### In ra

```
2
```

**Chú ý:** Có 30% số lượng test ứng với 30% số điểm mà ba đường cắt bất kì không cắt nhau tại một điểm bên trong chiếc bánh.

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    - Đề không cho cận trên của $m$. Lời giải không phụ thuộc vào $m$: các lần cắt trùng nhau (kể cả ghi ngược $j_k\ i_k$) chỉ tính một lần, nên sau khi gộp còn tối đa $\frac{n(n-1)}{2} \le 1225$ đường cắt khác nhau. Phần đọc dữ liệu là $O(m)$.
    - Lần cắt qua hai đỉnh kề nhau trùng với cạnh của bánh nên không tạo thêm miếng nào.
    - Đề không ghi cận dưới của $n$; lời giải giả định $n \ge 3$ (đa giác).

---

!!! tip "Đáp án"
    Tự làm trước, sau đó xem [lời giải tham khảo](dap-an.md).
