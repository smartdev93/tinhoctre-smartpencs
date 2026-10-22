# Đề thi Bảng C - Vòng khu vực 2021

Hội thi Tin học trẻ toàn quốc năm 2021, **đề chính thức vòng khu vực**, Bảng C - Trung học phổ thông. Ngày thi: **10/10/2021**. Thời gian làm bài: **150 phút** (không kể thời gian phát đề), ngôn ngữ **Pascal / C++ / Python**.

Dữ liệu vào từ thiết bị vào chuẩn (bàn phím), kết quả ghi ra thiết bị ra chuẩn (màn hình). Đề không ghi giới hạn thời gian và bộ nhớ cho mỗi test.

!!! warning "Nguồn đề"
    Đề được chép từ bản PDF đề chính thức do chuyentin.pro đăng lại (có watermark). Phần "Giải thích (bổ sung)" ở Bài 1 và Bài 2 do nhóm biên soạn site thêm vào, **không có trong đề gốc**.

## Tổng quan bài thi

| STT | Bài | File chương trình | Chủ đề | Điểm |
| ---: | --- | --- | --- | ---: |
| 1 | Số hoàn hảo | `pnum.*` | Quy hoạch động đếm, tổng tập con | 100 |
| 2 | Thi đấu cầu lông | `badmi.*` | Tham lam, ghép cặp, cấu trúc dữ liệu | 200 |
| 3 | Hoán vị không bất động | `permu.*` | Tổ hợp, bao hàm - loại trừ | 200 |

Dấu `*` được thay thế bởi `pas`/`cpp`/`py` của ngôn ngữ lập trình được sử dụng tương ứng là Pascal/C++/Python.

---

## 1. Số hoàn hảo (pnum)

Một bài toán trong đại hội Toán-Tin của Thiên hà như sau: Xét các số nguyên dương có dạng $\overline{a_1 a_2 \ldots a_n}$, trong đó $a_i$ nhận giá trị từ 1 đến $k$. Một đoạn chữ số từ vị trí thứ $L$ đến vị trí thứ $L + 9$ được gọi là đoạn hoàn hảo nếu:

1. $a_L + a_{L+1} + \cdots + a_{L+9} = 20$;
2. Các chữ số $a_L, a_{L+1}, \ldots, a_{L+9}$ có thể chia làm 2 nhóm có tổng bằng nhau.

**Yêu cầu:** Cho $n, k$ và $m$ vị trí $p_1, p_2, \ldots, p_m$, hãy đếm số lượng số nguyên dương có dạng $\overline{a_1 a_2 \ldots a_n}$ ($a_i$ nhận giá trị từ 1 đến $k$) mà có $m$ đoạn hoàn hảo lần lượt bắt đầu từ $p_1, p_2, \ldots, p_m$.

### Dữ liệu

* Dòng đầu gồm bốn số nguyên dương $n, k, m, D$ ($9 < n \le 50$; $k \le 9$; $D \le 10^9$);
* Dòng thứ hai gồm $m$ số nguyên $p_1, p_2, \ldots, p_m$ ($1 \le p_1 < p_2 < \cdots < p_m \le n - 9$).

### Kết quả

* Một dòng chứa một số nguyên $r$, trong đó $r$ là phần dư của số lượng số thỏa mãn chia cho $D$.

### Ràng buộc

* Có 20% số test ứng với 20% số điểm của bài có $m = 1$;
* Có 20% số test khác ứng với 20% số điểm của bài có $m = 2$;
* Có 60% số test còn lại ứng với 60% số điểm của bài có $m \le 5$.

### Ví dụ

#### Nhập vào

```
15 2 2 123
1 3
```

#### In ra

```
8
```

#### Giải thích (bổ sung)

* Với $k = 2$, đoạn 10 chữ số có tổng 20 chỉ có thể gồm toàn chữ số 2 (chia được thành hai nhóm năm chữ số 2). Hai đoạn bắt đầu tại 1 và 3 buộc $a_1 = a_2 = \cdots = a_{12} = 2$.
* Ba chữ số $a_{13}, a_{14}, a_{15}$ tự do, mỗi chữ số có 2 cách: $2^3 = 8$.

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    "Có $m$ đoạn hoàn hảo lần lượt bắt đầu từ $p_1, \ldots, p_m$" được hiểu là **các đoạn bắt đầu tại $p_1, \ldots, p_m$ đều hoàn hảo**; các đoạn bắt đầu ở vị trí khác có hoàn hảo hay không đều được. Ví dụ của đề xác nhận cách hiểu này: số $222222222222\,\ldots$ ở trên cũng có đoạn hoàn hảo bắt đầu tại vị trí 2, nếu bắt buộc "đúng $m$ đoạn" thì đáp án sẽ là 0 chứ không phải 8.

---

## 2. Thi đấu cầu lông (badmi)

Tham gia đại hội thể thao toàn Thiên hà, đội Trái đất có $n$ vận động viên tham gia bộ môn cầu lông. Vận động viên thứ $i$ ($1 \le i \le n$) có chỉ số thể lực là $a_i$ và chỉ số kĩ thuật là $b_i$. Theo thông tin thu nhận được, có $m$ ($n \le m$) vận động viên của hành tinh Z cũng tham gia bộ môn cầu lông, vận động viên thứ $j$ ($1 \le j \le m$) có chỉ số thể lực và kĩ thuật tương ứng là $x_j, y_j$. Đội hành tinh Z sẽ cử $n$ vận động viên, gồm các vận động viên liên tiếp từ vận động viên thứ $k$ đến vận động viên thứ $k + n - 1$ để đấu với $n$ vận động viên của đội Trái đất và sẽ thi đấu đúng $n$ trận đấu (mỗi vận động viên thi đấu một trận). Nếu vận động viên thứ $i$ của đội Trái đất muốn chắc chắn thắng vận động viên thứ $j$ của đội hành tinh Z thì $a_i > x_j$ và $b_i > y_j$. Đội Trái đất muốn lên phương án sắp xếp các vận động viên tương ứng thi đấu với $n$ vận động viên được cử của đội hành tinh Z để có nhiều trận chắc chắn thắng nhất.

**Yêu cầu:** Cho thông tin về $n$ vận động viên của đội Trái đất, thông tin $m$ vận động viên của đội hành tinh Z và $Q$ khả năng cử vận động viên bắt đầu từ các vận động viên $k_1, k_2, \ldots, k_Q$, với mỗi khả năng cử vận động viên của hành tinh Z, hãy giúp đội Trái đất lên phương án sắp xếp các vận động viên để có nhiều trận chắc chắn thắng nhất.

### Dữ liệu

* Dòng thứ nhất chứa ba số nguyên dương $n, m, Q$ ($m \le 10^5$; $Q \le 100$);
* Dòng thứ hai chứa $n$ số nguyên dương $a_1, a_2, \ldots, a_n$ ($a_i \le 10^9$ với $1 \le i \le n$);
* Dòng thứ ba chứa $n$ số nguyên dương $b_1, b_2, \ldots, b_n$ ($b_i \le 10^9$ với $1 \le i \le n$);
* Dòng thứ tư chứa $m$ số nguyên dương $x_1, x_2, \ldots, x_m$ ($x_j \le 10^9$ với $1 \le j \le m$);
* Dòng thứ năm chứa $m$ số nguyên dương $y_1, y_2, \ldots, y_m$ ($y_j \le 10^9$ với $1 \le j \le m$);
* Dòng cuối chứa $Q$ số nguyên dương $k_1, k_2, \ldots, k_Q$ ($1 \le k_t \le k_t + n - 1 \le m$ với $1 \le t \le Q$).

### Kết quả

* Gồm $Q$ dòng, mỗi dòng một số nguyên là số trận chắc chắn thắng lần lượt tương ứng với $Q$ khả năng cử vận động viên của đội hành tinh Z trong dữ liệu vào.

### Ràng buộc

* Có 25% số test ứng với 25% số điểm của bài có $n \le 6$;
* Có 25% số test khác ứng với 25% số điểm của bài có $n \le 100$;
* Có 25% số test khác ứng với 25% số điểm của bài có $n \le 5000$;
* Có 25% số test còn lại ứng với 25% số điểm của bài có $n \le 30000$.

### Ví dụ

#### Nhập vào

```
3 6 4
10 20 30
10 20 30
10 20 30 40 50 60
10 20 30 40 50 60
1 2 3 4
```

#### In ra

```
2
1
0
0
```

#### Giải thích (bổ sung)

* $k = 1$: đội Z cử các VĐV $(10, 10), (20, 20), (30, 30)$. VĐV $(20, 20)$ của Trái đất thắng chắc $(10, 10)$, VĐV $(30, 30)$ thắng chắc $(20, 20)$: 2 trận.
* $k = 2$: đội Z cử $(20, 20), (30, 30), (40, 40)$, chỉ VĐV $(30, 30)$ thắng chắc $(20, 20)$: 1 trận.
* $k = 3, 4$: mọi VĐV đội Z đều có chỉ số $\ge 30$, không trận nào chắc thắng.

---

## 3. Hoán vị không bất động (permu)

Huấn luyện viên của đội hành tinh Z biết rằng, đội Trái Đất đã nắm rõ các chỉ số thể lực và chỉ số kĩ thuật của các vận động viên đội mình, vì vậy ông ta quyết định thay đổi số áo nhằm làm sai lệch những tính toán của đội Trái đất.

Đội hành tinh Z có $m$ vận động viên đánh số từ 1 tới $m$, ban đầu vận động viên thứ $i$ mang số áo là $i$ ($1 \le i \le m$). Huấn luyện viên chọn $T$ đoạn, đoạn thứ $s$ ($1 \le s \le T$) mô tả bằng cặp số $L_s, R_s$ ($1 \le L_s \le R_s \le m$), rồi hoán vị số áo của các vận động viên (có thể cả $m$ vận động viên) sao cho tất cả các vận động viên có số áo nằm trong một trong $T$ đoạn phải mang số áo khác với số áo ban đầu của mình. Cụ thể, với một vận động viên mang số áo $i$ mà tồn tại $s$ ($1 \le s \le T$) để $L_s \le i \le R_s$ thì sau khi hoán vị vận động viên này phải mang số áo khác với số áo ban đầu của mình.

**Yêu cầu:** Hãy cho biết huấn luyện viên của đội hành tinh Z có bao nhiêu cách khác nhau để hoán vị số áo cho các vận động viên theo quy tắc trên, hai cách hoán vị số áo được gọi là khác nhau nếu có một vận động viên mang hai số áo khác nhau trong hai cách hoán vị.

### Dữ liệu

* Dòng đầu chứa số nguyên dương $m, T$;
* Dòng thứ $s$ ($1 \le s \le T$) trong $T$ dòng tiếp theo chứa hai số nguyên dương $L_s, R_s$ ($1 \le L_s \le R_s \le m$).

### Kết quả

* Một dòng chứa một số nguyên duy nhất là số dư của phép chia: số cách hoán vị số áo cho $(10^9 + 7)$.

### Ràng buộc

* Có 20% số test ứng với 20% số điểm của bài có $m \le 10$ và $T = 0$;
* Có 20% số test khác ứng với 20% số điểm của bài có $m \le 10$ và $T = 1$;
* Có 20% số test khác ứng với 20% số điểm của bài có $m \le 10^3$ và $T = 1$; $R_1 - L_1 \le 10$;
* Có 20% số test khác ứng với 20% số điểm của bài có $m \le 10^3$ và $T \le 10^3$;
* Có 20% số test còn lại ứng với 20% số điểm của bài có $m \le 10^5$ và $T \le 10^5$.

### Ví dụ

#### Nhập vào

```
3 1
1 2
```

#### In ra

```
3
```

#### Giải thích

* Có 3 cách hoán vị là:
    1. `2 1 3`
    2. `2 3 1`
    3. `3 1 2`

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    - Đề ghi "mô bằng cặp số", hiểu là "mô tả bằng cặp số".
    - Dòng đầu ghi "số nguyên dương $m, T$" nhưng subtask 1 có $T = 0$: khi đó không có dòng đoạn nào và đáp án là $m!$ (mọi hoán vị đều hợp lệ). Lời giải chấp nhận $T = 0$.
    - Các đoạn có thể giao nhau; một số áo thuộc nhiều đoạn chỉ tính là một vị trí "không được đứng yên".

---

!!! tip "Đáp án"
    Tự làm trước, sau đó xem [lời giải tham khảo](dap-an.md).
