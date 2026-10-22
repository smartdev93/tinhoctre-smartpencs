# Đề thi Bảng A - Quận Sơn Trà 2022

Hội thi Tin học trẻ cấp quận, UBND quận Sơn Trà, năm học 2021–2022. Đề thi Bảng A - Khối Tiểu học (đề chính thức). Thời gian làm bài: **100 phút** (không kể thời gian giao đề).

Ngôn ngữ: **Scratch** (`.sb2`/`.sb3`) hoặc **Python** (`.py`). Tất cả các bài nhập dữ liệu **từ bàn phím** và in kết quả ra **màn hình**.

!!! warning "Nguồn đề"
    Đề được chép từ ảnh chụp đề thi (`DA NANG/SƠN TRÀ/SƠN TRÀ 2022 (1).jpg` và `SƠN TRÀ 2022 (2).jpg`), gồm 2 trang. Ảnh chụp không ghi ngày thi. Đề gốc không ghi điểm trong bảng tổng quan; điểm lấy theo tiêu đề từng bài. Phần "Dữ liệu" và "Kết quả" của Bài 2 trong đề gốc bị chép nhầm (xem ghi chú ở Bài 2).

## Tổng quan bài thi

| STT | Bài | File chương trình | Dữ liệu vào | Dữ liệu ra | Điểm |
| ---: | --- | --- | --- | --- | ---: |
| 1 | Bóng đèn | `BONGDEN.*` | Từ bàn phím | Màn hình | 30 |
| 2 | Biểu thức nhỏ nhất | `BIEUTHUC.*` | Từ bàn phím | Màn hình | 30 |
| 3 | Không thích số 3 | `KHONGTHICH.*` | Từ bàn phím | Màn hình | 100 |
| 4 | Số cân bằng | `SOCANBANG.*` | Từ bàn phím | Màn hình | 20 |

*Chú ý: Dấu \* có thể là sb2/sb3 hoặc py tương ứng với ngôn ngữ lập trình là Scratch hoặc Python.*

---

## 1. Bóng đèn

Người ta mắc bóng đèn màu xung quanh một bảng quảng cáo hình vuông có chiều dài $a$ (dm), hai bóng đèn liên tiếp cách nhau 5 (cm). Em hãy viết chương trình để đưa ra màn hình số lượng bóng đèn cần mắc.

Ví dụ: $a = 1$, thì số bóng đèn cần mắc là 8.

### Dữ liệu

* Một số nguyên dương $a$ ($a \le 10^7$).

### Kết quả

* Một số nguyên duy nhất là số lượng bóng đèn cần mắc.

### Ví dụ 1

#### Nhập vào

```
3
```

#### In ra

```
24
```

#### Giải thích

* Đề gốc minh họa bằng hình các bóng đèn (dấu chấm) xếp quanh cạnh hình vuông.

---

## 2. Biểu thức nhỏ nhất

Cho trước 4 số nguyên $a, b, c, d$. Chúng ta sẽ chọn các số nguyên $x$ và $y$ sao cho $a \le x \le b$ và $c \le y \le d$.

**Yêu cầu:** Tìm giá trị nhỏ nhất có thể có của biểu thức $x - y$.

### Dữ liệu

Đề gốc ghi:

* Một số nguyên dương $n$ ($n \le 10^{18}$).
* Dòng đầu tiên chứa số nguyên dương $a$.
* Dòng đầu tiên chứa số nguyên dương $b$.
* Dòng đầu tiên chứa số nguyên dương $c$.
* Dòng đầu tiên chứa số nguyên dương $d$.
* $1 \le a, b, c, d \le 10^{12}$.

### Kết quả

Đề gốc ghi: Một số nguyên duy nhất là số lượng ngày có ít nhất một máy hoạt động.

!!! note "Cách hiểu đề dùng cho lời giải tham khảo"
    Mục "Dữ liệu" và "Kết quả" của bài này trong đề gốc có chỗ chép nhầm từ bài khác: dòng "Một số nguyên dương $n$ ($n \le 10^{18}$)" và câu "số lượng ngày có ít nhất một máy hoạt động" không liên quan tới bài; cả bốn dòng đều ghi "Dòng đầu tiên". Theo ví dụ, lời giải tham khảo hiểu là:

    * Dữ liệu: 4 dòng, lần lượt là $a$, $b$, $c$, $d$ ($1 \le a \le b \le 10^{12}$, $1 \le c \le d \le 10^{12}$).
    * Kết quả: một số nguyên là giá trị nhỏ nhất của $x - y$ (có thể âm).

### Ví dụ 1

#### Nhập vào

```
10
20
1
7
```

#### In ra

```
3
```

#### Giải thích

* Chọn $x = 10$, $y = 7$ thì ta có biểu thức $x - y = 10 - 7 = 3$ là nhỏ nhất.

---

## 3. Không thích số 3

Polycarp không thích các số nguyên chia hết cho 3 hay có tận cùng bằng 3. Các số thỏa mãn cả hai điều kiện, Polycarp cũng không thích. Polycarp bắt đầu viết các số nguyên dương (lớn hơn 0) mà anh ấy thích: 1, 2, 4, 5, 7, 8, 10, 11, 14, 16, ...

**Yêu cầu:** Hãy in ra số thứ $k$ trong dãy này (các số được đánh thứ tự từ 1).

### Dữ liệu

* Một số nguyên dương $k$ ($k \le 10^9$).

### Kết quả

* Một số nguyên duy nhất là số thứ $k$ trong dãy trên.

### Ví dụ 1

#### Nhập vào

```
5
```

#### In ra

```
7
```

#### Giải thích

* 1, 2, 4, 5, **7**, 8, 10, 11, 14, 16, ...

### Ví dụ 2

#### Nhập vào

```
9
```

#### In ra

```
14
```

#### Giải thích

* 1, 2, 4, 5, 7, 8, 10, 11, **14**, 16, ...

!!! warning "Lỗi trong ví dụ của đề gốc"
    Bản in ghi Output của Ví dụ 2 là **17**, nhưng cột "Giải thích" của chính ví dụ đó gạch chân số **14**, và đếm trực tiếp thì số thứ 9 của dãy là 14 (lời giải tham khảo cũng cho 14). Trang này ghi Output là 14.

---

## 4. Số cân bằng

*Số cân bằng* là số:

* Có số lượng các chữ số là chẵn.
* Nửa nhóm ký tự bên trái giống nửa nhóm bên phải.

*Ví dụ:* 66, 1212; 348348 là số cân bằng; 666, 1221; 334488 không phải là số cân bằng.

**Yêu cầu:** Cho giá trị $n$, hãy tìm các số cân bằng không vượt quá $n$.

### Dữ liệu

* Một số nguyên dương $n$ ($n \le 10^{12}$).

### Kết quả

* Một số nguyên duy nhất là số lượng số cân bằng.

### Ví dụ 1

#### Nhập vào

```
33
```

#### In ra

```
3
```

#### Giải thích

* 3 số cân bằng là: 11; 22; 33.

### Ví dụ 2

#### Nhập vào

```
1333
```

#### In ra

```
13
```

#### Giải thích

* 13 số cân bằng là: 11; 22; 33; 44; 55; 66; 77; 88; 99; 1010; 1111; 1212; 1313.

---

!!! tip "Đáp án"
    Tự làm trước, sau đó xem [lời giải tham khảo](dap-an.md).
