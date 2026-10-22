# Đề thi Bảng C - Khu vực miền Nam 2022

Hội thi Tin học trẻ toàn quốc năm 2022, vòng khu vực miền Nam, **Bảng C1** và **Bảng C2** (THPT). Ngày thi, thời gian làm bài, ngôn ngữ lập trình: tài liệu không ghi.

Mỗi bài 100 điểm. Dữ liệu vào từ **thiết bị vào chuẩn** (bàn phím), kết quả ghi ra **thiết bị ra chuẩn** (màn hình). Tài liệu không ghi giới hạn thời gian/bộ nhớ.

!!! warning "Nguồn đề"
    Đề được chép từ hai tài liệu *THT toàn quốc 2022 - Bảng C1 - Khu vực miền Nam* và *THT toàn quốc 2022 - Bảng C2 - Khu vực miền Nam* (bản PDF có watermark chuyentin.pro). Tài liệu không ghi ngày thi, thời gian làm bài, ngôn ngữ, tên file chương trình và giới hạn thời gian/bộ nhớ, nên trang này không ghi các thông tin đó. Hai bài **Bộ ba** và **Chọn cặp** có mặt ở cả hai bảng với nội dung giống hệt nhau, nên chỉ chép một lần. Phần "Giải thích (bổ sung)" do nhóm biên soạn site thêm vào, **không có trong tài liệu**.

## Tổng quan bài thi

| STT | Bài | Bảng | Chủ đề | Điểm |
| ---: | --- | --- | --- | ---: |
| 1 | Bộ ba | C1, C2 | Toán / chia khối theo giá trị $\lfloor N/x \rfloor$ | 100 |
| 2 | Chọn cặp | C1, C2 | Tổng tiền tố, tìm kiếm nhị phân theo đáp án, cây Fenwick | 100 |
| 3 | Chọn nhóm | C1 | Tối ưu tổ hợp (chấm theo tỉ lệ), vét cạn bitmask + tìm kiếm cục bộ | 100 |
| 4 | Xe buýt | C2 | Đường đi ngắn nhất trên trục số, tham lam | 100 |

Thứ tự bài trong tài liệu: Bảng C1 gồm Bộ ba, Chọn cặp, Chọn nhóm; Bảng C2 gồm Bộ ba, Xe buýt, Chọn cặp.

---

## 1. Bộ ba

*Bảng C1, C2 - 100 điểm.*

Cho các số nguyên không âm $a_1, b_1, a_2, b_2, a_3, b_3$, hãy đếm số bộ ba $(x, y, z)$ thỏa mãn:

- $a_1 \le x \le b_1$;
- $a_2 \le y \le b_2$;
- $a_3 \le z \le b_3$;
- $x \times y = z$.

### Dữ liệu

* Vào từ thiết bị vào chuẩn gồm 6 số nguyên không âm $a_1, b_1, a_2, b_2, a_3, b_3$, các số có giá trị không vượt quá $10^9$.

### Kết quả

* Ghi ra thiết bị ra chuẩn một số duy nhất là số bộ thỏa mãn đếm được.

### Ràng buộc

* Có 8% số test ứng với 8% số điểm có $b_1, b_2, b_3 \le 300$;
* Có 12% số test khác ứng với 12% số điểm có $b_1, b_2, b_3 \le 3000$;
* Có 20% số test khác ứng với 20% số điểm có $b_1, b_2, b_3 \le 10^5$;
* Có 20% số test khác ứng với 20% số điểm có $b_1, b_2, b_3 \le 10^7$;
* Có 16% số test khác ứng với 16% số điểm có $a_1 = b_1$;
* Có 24% số test còn lại ứng với 24% số điểm không có ràng buộc gì thêm.

### Ví dụ

#### Nhập vào

```
6 8 4 5 27 35
```

#### In ra

```
4
```

#### Giải thích

* Có 4 bộ thỏa mãn là: $(6, 5, 30)$; $(7, 4, 28)$; $(7, 5, 35)$; $(8, 4, 32)$.

---

## 2. Chọn cặp

*Bảng C1, C2 - 100 điểm.*

Cho dãy số nguyên $A = (a_1, a_2, \ldots, a_n)$. Với hai số nguyên dương $l, r$ ($1 \le l \le r \le n$), gọi trọng số của cặp $(l, r)$ là tổng giá trị của các phần tử liên tiếp từ $l$ đến $r$ của dãy $A$.

**Yêu cầu:** Cho dãy $A$ và hai số nguyên dương $k, X$, hãy chọn ra $k$ cặp $(l_1, r_1), (l_2, r_2), \ldots, (l_k, r_k)$ thỏa mãn:

- $1 \le l_i \le r_i \le n$;
- Các cặp này đôi một khác nhau;
- $r_i - l_i + 1 \ge X$;
- Tổng trọng số của $k$ cặp đã chọn là lớn nhất.

### Dữ liệu

* Dòng đầu chứa ba số nguyên dương $n, k, X$ ($X \le n$);
* Dòng thứ hai chứa $n$ số nguyên $a_i$ ($|a_i| \le 10^5$).

### Kết quả

* Ghi ra thiết bị ra chuẩn một số nguyên duy nhất là tổng trọng số lớn nhất tìm được.

### Ràng buộc

* Có 10% số test ứng với 10% số điểm có $n \le 100$; $k \le 1000$;
* Có 15% số test khác ứng với 15% số điểm có $n \le 1000$; $k \le 10^5$;
* Có 20% số test khác ứng với 20% số điểm có $n, k \le 10^4$;
* Có 20% số test khác ứng với 20% số điểm có $n, k \le 5 \times 10^4$;
* Có 20% số test khác ứng với 20% số điểm có $n, k \le 3 \times 10^5$;
* Có 15% số test còn lại ứng với 15% số điểm có $n \le 3 \times 10^5$; $k \le 10^7$.

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    Đề không nói $k$ luôn nhỏ hơn hoặc bằng số cặp hợp lệ, là $\frac{(n - X + 1)(n - X + 2)}{2}$. Lời giải giả định điều này luôn đúng; nếu $k$ lớn hơn thì lời giải chọn tất cả các cặp hợp lệ.

### Ví dụ

#### Nhập vào

```
4 4 2
3 2 -6 8
```

#### In ra

```
18
```

#### Giải thích (bổ sung)

* Các cặp có độ dài $\ge 2$ và trọng số: $(1, 4) = 7$, $(1, 2) = 5$, $(2, 4) = 4$, $(3, 4) = 2$, $(1, 3) = -1$, $(2, 3) = -4$.
* Chọn 4 cặp lớn nhất: $7 + 5 + 4 + 2 = 18$.

---

## 3. Chọn nhóm

*Bảng C1 - 100 điểm.*

Một lớp học có $n$ học sinh, các học sinh được đánh số từ 1 đến $n$. Thầy giáo chủ nhiệm muốn chọn ra một nhóm bạn để tham gia một trò chơi, một trò chơi cần sự phối hợp nhịp nhàng giữa các thành viên trong nhóm. Là một giáo viên nhiều kinh nghiệm, thầy giáo chủ nhiệm đã biết được sự phối hợp của $m$ cặp học sinh, một cặp học sinh $i$ ($1 \le i \le n$) và học sinh $j$ ($1 \le i \le n$) có sự phối hợp là giá trị $c(i, j)$, điều này có nghĩa là nếu học sinh $i$ và học sinh $j$ cùng được chọn vào nhóm thì tổng sự phối hợp của nhóm sẽ được cộng giá trị $c(i, j)$, biết rằng $-10^9 \le c(i, j) \le 10^9$.

**Yêu cầu:** Cho $n$ học sinh và $m$ cặp học sinh mà thầy giáo chủ nhiệm đã biết, hãy giúp thầy giáo chủ nhiệm chọn ra một nhóm để tổng sự phối hợp của nhóm là lớn nhất.

### Dữ liệu

* Dòng đầu tiên gồm các số nguyên $n, m$;
* Dòng thứ $k$ ($1 \le k \le m$) trong $m$ dòng tiếp theo chứa ba số nguyên $i_k, j_k, c(i_k, j_k)$.

### Kết quả

* Dòng đầu tiên chứa số nguyên $s$ là số lượng học sinh trong nhóm;
* Dòng thứ hai gồm $s$ số là chỉ số các bạn học sinh được chọn.

### Ràng buộc

* Có 30% số test ứng với 30% số điểm có $n \le 20$;
* Có 40% số test khác ứng với 40% số điểm có $n \le 200$ và giá trị $c(i, j)$ chỉ nhận một trong hai loại giá trị $1$ hoặc $-10^9$;
* Có 30% số test còn lại ứng với 30% số điểm có $n \le 200$.

### Cách tính điểm

Có 20 test, mỗi test 5.0 điểm. Với mỗi test, gọi tổng sự phối hợp của nhóm do thí sinh tìm được là $c$, $q$ là tổng sự phối hợp của nhóm trong lời giải của Ban giám khảo, nếu $c \le 0$ thí sinh sẽ được 0 điểm, ngược lại số điểm của thí sinh đạt được là $5.0 \times \min\left\{1, \frac{c^3}{q^3}\right\}$.

### Ví dụ

#### Nhập vào

```
5 3
1 5 1
1 2 -1
2 5 3
1 4 -1
```

#### In ra

```
3
1 2 5
```

#### Giải thích (bổ sung)

* Nhóm $\{1, 2, 5\}$ có tổng sự phối hợp $c(1,5) + c(1,2) + c(2,5) = 1 - 1 + 3 = 3$.
* Nhóm $\{2, 5\}$ cũng có tổng bằng 3, nên đáp án không duy nhất. Lời giải tham khảo in `2` / `2 5`.

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    - Dòng đầu của ví dụ ghi $m = 3$ nhưng bên dưới có **4 dòng** cặp học sinh. Đây là lỗi trong tài liệu nguồn (trang này giữ nguyên ví dụ gốc). Đọc 3 hay 4 cặp thì tổng lớn nhất vẫn là 3, vì học sinh 4 không được chọn.
    - Đề có thể có nhiều nhóm đạt tổng lớn nhất; in nhóm nào cũng được (bài chấm theo tổng $c$).
    - Đề không nói gì về cặp có $i = j$ hay một cặp xuất hiện nhiều lần. Lời giải bỏ qua cặp $i = j$ và cộng dồn giá trị nếu một cặp lặp lại.
    - Khi mọi nhóm đều có tổng $\le 0$ (thí sinh nào cũng được 0 điểm ở test đó), lời giải in nhóm chỉ gồm học sinh 1 (tổng bằng 0).
    - Tài liệu ghi điều kiện của học sinh $j$ là "$(1 \le i \le n)$" (giữ nguyên ở trên), có lẽ là lỗi đánh máy của $1 \le j \le n$.

---

## 4. Xe buýt

*Bảng C2 - 100 điểm.*

Trên một trục đường dài thẳng có $n$ trạm xe buýt cách đều nhau, các trạm được đánh số từ 1 đến $n$. Để đi lại giữa hai trạm liên tiếp bất kì bằng xe buýt mất $a$ đồng. Trong $n$ trạm có $m$ trạm đặc biệt là các trạm $p_1, p_2, \ldots, p_m$ ($1 \le p_1, p_2, \ldots, p_m \le n$). Có loại xe buýt nhanh sẽ chỉ dừng đỗ tại các trạm đặc biệt này, nếu sử dụng xe buýt nhanh để đi từ trạm đặc biệt $p_i$ đến trạm đặc biệt $p_j$ sẽ mất $b \times |p_i - p_j|$ đồng.

**Yêu cầu:** Cho $q$ câu hỏi, câu hỏi thứ $k$ ($1 \le k \le q$) cần trả lời đi từ trạm $x_k$ ($1 \le x_k \le n$) tới trạm $y_k$ ($1 \le y_k \le n$) hết ít nhất bao nhiêu tiền.

### Dữ liệu

* Dòng đầu chứa các số nguyên dương $n, m, q, a, b$ ($a, b \le 10^6$; $2 \le m \le n$);
* Dòng thứ hai chứa $m$ số nguyên dương $p_1, p_2, \ldots, p_m$;
* Dòng thứ $k$ ($1 \le k \le q$) chứa hai số nguyên dương $x_k, y_k$.

### Kết quả

* Ghi ra thiết bị ra chuẩn gồm $q$ dòng, dòng thứ $k$ chứa một số là câu trả lời cho câu hỏi thứ $k$.

### Ràng buộc

* Có 25% số test ứng với 25% số điểm có $n, m, q \le 100$; $a = b$;
* Có 25% số test khác ứng với 25% số điểm có $n, q \le 100$; $m = 2$; $p_1 = 1$; $p_2 = n$;
* Có 25% số test khác ứng với 25% số điểm có $n, m, q \le 100$;
* Có 25% số test còn lại ứng với 25% số điểm có $n, m, q \le 10^6$.

### Ví dụ

#### Nhập vào

```
5 2 2 2 1
2 4
1 5
2 3
```

#### In ra

```
6
2
```

#### Giải thích (bổ sung)

* Câu hỏi 1 (từ trạm 1 tới trạm 5): xe thường $1 \to 2$ mất 2 đồng, xe nhanh $2 \to 4$ mất $1 \times 2 = 2$ đồng, xe thường $4 \to 5$ mất 2 đồng, tổng 6. Chỉ đi xe thường thì mất $4 \times 2 = 8$.
* Câu hỏi 2 (từ trạm 2 tới trạm 3): đi xe thường mất 2 đồng.

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    "Dòng thứ $k$ ($1 \le k \le q$)" được hiểu là $q$ dòng cuối, mỗi dòng một câu hỏi. Đề không nói các $p_i$ khác nhau hay đã sắp xếp; lời giải chấp nhận cả trường hợp trùng hoặc chưa sắp xếp. Câu hỏi có $x_k = y_k$ có đáp án 0.

---

!!! tip "Đáp án"
    Tự làm trước, sau đó xem [lời giải tham khảo](dap-an.md).
