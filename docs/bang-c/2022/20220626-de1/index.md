# Đề thi Bảng C - Vòng sơ khảo 2022 (26/06/2022)

Hội thi Tin học trẻ toàn quốc năm 2022, **vòng sơ khảo** (thi trực tuyến trên hệ thống chấm tinhoctre.vn), ngày **26/06/2022**, **Bảng C1** và **Bảng C2** (THPT). Thời gian làm bài: tài liệu không ghi. Ngôn ngữ cho phép: **Pascal / C++ / Python**.

Mỗi bài 100 điểm. Dữ liệu vào từ **thiết bị vào chuẩn** (bàn phím), kết quả ghi ra **thiết bị ra chuẩn** (màn hình). Giới hạn ghi trên trang bài của hệ thống chấm: bộ nhớ **512 MB**, thời gian **1 giây** (riêng bài Ma trận **0,5 giây**).

!!! warning "Nguồn đề"
    Đề được chép từ bản PDF của 4 bài vòng sơ khảo 2022 được **công khai** trên hệ thống chấm chính thức [tinhoctre.vn](https://www.tinhoctre.vn/problems/) (mã bài `tht2022_biendoixau`, `tht2022_matran`, `tht2022_catghepxau`, `tht2022_daycapsonhan`). Bảng thi, ngày thi, điểm mỗi bài, giới hạn thời gian/bộ nhớ, thiết bị vào/ra và ngôn ngữ lấy từ trang của từng bài trên hệ thống chấm. Đây **chỉ là các bài đang công khai**; đề thi đầy đủ của mỗi bảng có thể còn bài khác chưa được công khai. Trang không có thông tin thời gian làm bài và thứ tự bài trong đề gốc. Phần "Giải thích (bổ sung)" do nhóm biên soạn site thêm vào, **không có trong đề**.

## Tổng quan bài thi

| STT | Bài | Bảng | Chủ đề | Điểm |
| ---: | --- | --- | --- | ---: |
| 1 | Biến đổi xâu | C1, C2 | Cây phân đoạn lười với nhãn là ánh xạ ký tự | 100 |
| 2 | Ma trận | C1, C2 | Kiểm tra tích ma trận ngẫu nhiên (Freivalds) | 100 |
| 3 | Cắt ghép xâu | C1 | Tối ưu tổ hợp (chấm theo tỉ lệ), tham lam + băm xâu | 100 |
| 4 | Dãy cấp số nhân | C2 (và Bảng B) | Quy hoạch động, độ dài dãy không quá 30 | 100 |

---

## 1. Biến đổi xâu

*Bảng C1, C2 - 100 điểm. Thời gian 1 giây, bộ nhớ 512 MB.*

Cho chuỗi kí tự $s$ có độ dài $n$ chỉ bao gồm các kí tự in thường. Các kí tự được đánh số từ $0$ đến $n - 1$, $s = s_0, s_1, \ldots, s_{n-1}$.

Chuỗi này sẽ được áp dụng lần lượt các thao tác thay đổi $(i, j, c_1, c_2)$ là biến đổi các vị trí là kí tự $c_1$ thành kí tự $c_2$ trong đoạn từ $i$ đến $j$.

**Yêu cầu:** Cho biết chuỗi $s$ ban đầu và $m$ thao tác biến đổi, hãy đưa ra chuỗi cuối cùng sau biến đổi.

### Dữ liệu

Vào từ thiết bị vào chuẩn có khuôn dạng:

* Dòng đầu chứa chuỗi $s$ có độ dài $n$ ($1 \le n \le 10^6$), xâu $s$ chỉ chứa kí tự thường;
* Dòng thứ hai chứa số $m$ ($1 \le m \le 1.5 \times 10^5$);
* $m$ dòng tiếp theo mỗi dòng chứa $i, j, c_1, c_2$ ($0 \le i \le j < n$; $c_1 \ne c_2$).

### Kết quả

* Ghi ra thiết bị ra chuẩn xâu $s$ sau $m$ biến đổi.

### Ràng buộc

* Có 20% số test ứng với 20% số điểm của bài có $n, m \le 2000$;
* Có 20% số test khác ứng với 20% số điểm của bài có $n, m \le 5 \times 10^4$;
* Có 20% số test khác ứng với 20% số điểm của bài có $n \le 3 \times 10^5$;
* Có 20% số test khác ứng với 20% số điểm của bài có các kí tự trong xâu và biến đổi chỉ là `'a'` hoặc `'b'`;
* Có 20% số test còn lại ứng với 20% số điểm của bài không có ràng buộc gì thêm.

### Ví dụ

#### Nhập vào

```
aaaabbbbcccc
3
0 2 a y
5 9 b c
1 3 a z
```

#### In ra

```
yyyzbccccccc
```

#### Giải thích

* Sau bước 1 xâu $s$ là `yyyabbbbcccc`.
* Sau bước 2 xâu $s$ là `yyyabccccccc`.
* Sau bước 3 xâu $s$ là `yyyzbccccccc`.

---

## 2. Ma trận

*Bảng C1, C2 - 100 điểm. Thời gian 0,5 giây, bộ nhớ 512 MB.*

Phép nhân hai ma trận chỉ thực hiện được khi số cột của ma trận bên trái bằng số dòng của ma trận bên phải. Nếu ma trận $A$ có kích thước $m \times n$ và ma trận $B$ có kích thước $n \times p$, thì ma trận tích $C = A \times B$ có kích thước $m \times p$, phần tử đứng ở hàng thứ $i$, cột thứ $j$ xác định bởi:

$$c_{i,j} = a_{i,1} b_{1,j} + a_{i,2} b_{2,j} + \ldots + a_{i,n} b_{n,j}$$

Phép nhân ma trận có các tính chất kết hợp: $(A \times B) \times C = A \times (B \times C)$;

Ví dụ,

$$A = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix};\quad A^2 = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix};\quad A^3 = \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix};$$

**Yêu cầu:** Cho ma trận $A$ kích thước $n \times n$ và ma trận $B$, hãy kiểm tra xem $A^3$ có bằng $B$ hay không?

### Dữ liệu

Vào từ thiết bị vào chuẩn có khuôn dạng:

* Dòng thứ nhất chứa số nguyên dương $T$ ($T \le 20$) là số lượng bộ dữ liệu;
* Tiếp theo là $T$ nhóm dòng, mỗi nhóm dòng tương ứng với một bộ dữ liệu có dạng:
    - Dòng đầu chứa số nguyên $n$;
    - $n$ dòng tiếp theo, mỗi dòng chứa $n$ số nguyên mô tả ma trận $A$, các số có giá trị tuyệt đối không vượt quá $1000$;
    - $n$ dòng tiếp theo, mỗi dòng chứa $n$ số nguyên mô tả ma trận $B$, các số có giá trị tuyệt đối không vượt quá $10^{18}$.

### Kết quả

* Ghi ra thiết bị ra chuẩn gồm $T$ dòng, mỗi dòng là kết quả tương ứng với một bộ dữ liệu theo thứ tự xuất hiện trong file dữ liệu vào: ghi thông báo `YES` nếu $A^3 = B$ và ghi `NO` trong trường hợp ngược lại.

### Ràng buộc

* Có 50% số test ứng với 50% số điểm của bài thỏa mãn: $n \le 10$;
* 50% số test còn lại ứng với 50% số điểm của bài thỏa mãn: $n \le 500$.

### Ví dụ

#### Nhập vào

```
2
2
0 1
1 1
1 2
2 2
2
0 1
1 1
1 2
2 3
```

#### In ra

```
NO
YES
```

#### Giải thích (bổ sung)

* Cả hai bộ dữ liệu đều có $A = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$, nên $A^3 = \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}$ như ví dụ trong đề.
* Bộ thứ nhất có $b_{2,2} = 2 \ne 3$ nên in `NO`; bộ thứ hai có $B = A^3$ nên in `YES`.

---

## 3. Cắt ghép xâu

*Bảng C1 - 100 điểm. Thời gian 1 giây, bộ nhớ 512 MB.*

Tin sinh học (Bioinformatics) là một lĩnh vực khoa học sử dụng các công nghệ của các ngành để giải quyết các vấn đề sinh học. Một bài toán được nghiên cứu để sử dụng phân tích dữ liệu sinh học như sau: Cho hai xâu $S_1, S_2$, hãy tìm cách cắt xâu $S_1$ thành ít đoạn nhất sau đó ghép tất cả các đoạn lại theo một thứ tự nào đó để nhận được xâu $S_2$.

Ví dụ: $S_1 =$ `"abcabc"`, $S_2 =$ `"aabbcc"`, một phương án cắt $S_1$ tại các vị trí sau kí tự thứ 1, thứ 3, thứ 5 nhận được bốn xâu `"a"`, `"bc"`, `"ab"`, `"c"` để ghép được xâu $S_2 =$ `"aabbcc"`.

### Dữ liệu

Vào từ thiết bị vào chuẩn có khuôn dạng:

* Dòng đầu chứa xâu $S_1$ chỉ gồm các kí tự `'a'` đến `'z'`;
* Dòng thứ hai chứa xâu $S_2$ chỉ gồm các kí tự `'a'` đến `'z'`.

### Kết quả

Ghi ra thiết bị ra chuẩn theo khuôn dạng: Ghi $-1$ nếu không tồn tại cách cắt thỏa mãn; ngược lại, gọi $c$ là số điểm cắt và các vị trí cắt là $1 \le p_1 < p_2 < \cdots < p_c < n$, đánh số các đoạn được cắt ra theo thứ tự từ đầu đến cuối bắt đầu từ $1$ đến $c + 1$, trường hợp này cần ghi ra ba dòng theo khuôn dạng:

* Dòng đầu chứa số nguyên dương $c$;
* Dòng thứ hai gồm $c$ số nguyên là các vị trí cắt $p_1, p_2, \ldots, p_c$;
* Dòng thứ ba gồm $c + 1$ là một hoán vị của $1, 2, \ldots, c + 1$ mô tả cách ghép các đoạn, các số cách nhau bởi dấu cách.

### Ràng buộc

* Có 30% số test ứng với 30% số điểm có độ dài xâu $S_1, S_2$ đều không vượt quá $20$;
* Có 30% số test khác ứng với 30% số điểm có độ dài xâu $S_1, S_2$ đều không vượt quá $60$;
* Có 40% số test còn lại ứng với 40% số điểm có độ dài xâu $S_1, S_2$ đều không vượt quá $10^4$.

### Cách tính điểm

Có $20$ test, mỗi test $5.0$ điểm. Gọi số điểm cắt do thí sinh tìm được là $c$, số điểm cắt của Ban giám khảo là $q$, khi đó số điểm bạn đạt được cho mỗi test là $5.0 \times \min\{1, \frac{q^5}{c^5}\}$.

### Ví dụ

#### Nhập vào

```
abcabc
aabbcc
```

#### In ra

```
3
1 3 5
1 3 2 4
```

#### Giải thích (bổ sung)

* Cắt $S_1$ sau kí tự thứ 1, 3, 5 được 4 đoạn: (1) `a`, (2) `bc`, (3) `ab`, (4) `c`.
* Ghép theo thứ tự 1, 3, 2, 4: `a` + `ab` + `bc` + `c` = `aabbcc` $= S_2$.

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    - Đề không định nghĩa $n$ trong điều kiện $p_c < n$; lời giải hiểu $n$ là độ dài $S_1$.
    - Bài có thể có nhiều đáp án: chương trình được chấm theo số điểm cắt $c$ so với của Ban giám khảo, nên mọi cách cắt ghép đúng có cùng $c$ đều được điểm như nhau. Lời giải tham khảo in ra một phương án khác ví dụ nhưng cũng có $c = 3$.
    - Đề yêu cầu $c$ nguyên dương nhưng không nói trường hợp $S_1 = S_2$ (không cần cắt). Lời giải in `0`, một dòng trống, rồi `1`. Hệ thống chấm có thể xử lý trường hợp này khác.

---

## 4. Dãy cấp số nhân

*Bảng C2 (đề cũng dùng cho Bảng B) - 100 điểm. Thời gian 1 giây, bộ nhớ 512 MB.*

Cho dãy gồm $n$ số nguyên dương $a_1, a_2, \ldots, a_n$.

Dãy số $b_1, b_2, \ldots, b_k$ được gọi là dãy cấp số nhân công bội $q$ khi và chỉ khi $b_{i+1} = b_i \times q$ với mọi $1 \le i < k$.

**Yêu cầu:** Cho số nguyên $q$, với mỗi $k$ ($1 < k \le n$), hãy đếm số dãy con (không nhất thiết liên tiếp) độ dài $k$ của dãy $a_1, a_2, \ldots, a_n$ là dãy cấp số nhân công bội $q$.

### Dữ liệu

Vào từ thiết bị vào chuẩn có khuôn dạng:

* Dòng đầu tiên gồm hai số nguyên $n, q$ ($1 \le n \le 10^5$; $2 \le q \le 10^9$).
* Dòng thứ hai chứa $n$ số nguyên $a_1, a_2, \ldots, a_n$ ($1 \le a_i \le 10^9$).

### Kết quả

* Ghi ra thiết bị ra chuẩn một dòng gồm $n - 1$ số nguyên, số thứ $s$ ($1 \le s < n$) là số dãy con độ dài $(s + 1)$ là dãy cấp số nhân công bội $q$ chia dư cho $(10^9 + 7)$.

### Ràng buộc

* Có 25% số test ứng với 25% số điểm của bài thỏa mãn: $n \le 20$;
* 25% số test khác ứng với 25% số điểm của bài thỏa mãn: $n \le 100$;
* 25% số test khác ứng với 25% số điểm của bài thỏa mãn: $n \le 1000$;
* 25% số test còn lại ứng với 25% số điểm của bài không có ràng buộc gì thêm.

### Ví dụ

#### Nhập vào

```
5 2
1 2 8 4 2
```

#### In ra

```
3 1 0 0
```

#### Giải thích (bổ sung)

* Độ dài 2: $(a_1, a_2) = (1, 2)$, $(a_1, a_5) = (1, 2)$, $(a_2, a_4) = (2, 4)$, tổng cộng 3 dãy. Hai dãy $(1, 2)$ được đếm riêng vì lấy ở các vị trí khác nhau.
* Độ dài 3: chỉ có $(a_1, a_2, a_4) = (1, 2, 4)$. Số $8$ đứng trước $4$ nên không nối được $(1, 2, 4, 8)$.
* Độ dài 4 và 5: không có dãy nào.

---

!!! tip "Đáp án"
    Tự làm trước, sau đó xem [lời giải tham khảo](dap-an.md).
