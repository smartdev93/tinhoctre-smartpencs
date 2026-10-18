# Đáp án - Đề 1 Bảng A Tiểu học

Lời giải tham khảo bằng Python 3. Xem lại [đề bài](index.md).

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Tặng bánh | Tham lam + thử phần dư | $O(1)$ |
| 2 | Chia kẹo | Chẵn / lẻ | $O(N \log N)$ |
| 3 | Chuỗi lặp đều | Đếm tần suất ký tự | $O(\text{len}(S))$ |
| 4 | Tính tích | Tổng tiền tố | $O(N)$ |

---

## 1. Tặng bánh

**Ý tưởng.** Giá mỗi cái: hộp lớn $210/30 = 7$, hộp nhỏ $38/5 = 7{,}6$, mua lẻ $9$ nghìn đồng. Hộp lớn rẻ nhất nên mua tối đa $\lfloor N / 210 \rfloor$ hộp lớn. Phần tiền dư nhỏ hơn 210, nên chỉ cần thử mua $0..5$ hộp nhỏ, còn lại mua lẻ, rồi lấy kết quả lớn nhất.

Vì sao không nên bớt hộp lớn: 210 nghìn nếu không mua hộp lớn thì chỉ mua được tối đa 27 cái (5 hộp nhỏ + 2 cái lẻ), ít hơn 30 cái.

!!! warning "Bẫy thường gặp"
    Duyệt hai vòng lặp lồng nhau theo số hộp lớn và số hộp nhỏ cho kết quả đúng, nhưng với $N = 10^9$ sẽ chạy quá thời gian.

```python title="hinchchunhat.py"
--8<-- "bang-a/2026/20260920-de1/sol/hinchchunhat.py"
```

## 2. Chia kẹo

**Ý tưởng.** Hai số liên tiếp luôn có một số chẵn và một số lẻ. Vì vậy **2 hộp luôn đủ**: hộp số chẵn và hộp số lẻ.

- Nếu trong dãy có hai số màu liên tiếp → cần **2** hộp.
- Ngược lại → **1** hộp.

Sắp xếp dãy rồi kiểm tra hai phần tử kề nhau có chênh lệch đúng 1 hay không.

```python title="bangcuuchuong.py"
--8<-- "bang-a/2026/20260920-de1/sol/bangcuuchuong.py"
```

## 3. Chuỗi lặp đều

**Ý tưởng.** Chuỗi kết quả gồm $k$ bản sao của một chuỗi con $T$, nên mỗi ký tự phải xuất hiện số lần chia hết cho $k$.

- Nếu có ký tự nào có số lần xuất hiện không chia hết cho $k$ → in `-1`.
- Ngược lại, $T$ gồm mỗi ký tự `c` lặp lại $\text{cnt}(c)/k$ lần; in $T$ lặp $k$ lần.

Đề cho phép in **một** chuỗi thỏa mãn bất kỳ; lời giải dưới đây in chuỗi có $T$ đã sắp xếp theo thứ tự chữ cái.

```python title="santruong.py"
--8<-- "bang-a/2026/20260920-de1/sol/santruong.py"
```

## 4. Tính tích

**Ý tưởng.** Gọi $T$ là tổng cả dãy. Khi cắt sau phần tử thứ $i$, phần trái có tổng $P_i$ (tổng tiền tố) và phần phải có tổng $T - P_i$. Duyệt mọi vị trí cắt $i = 1..N-1$ và lấy giá trị lớn nhất của $P_i \times (T - P_i)$.

!!! note "Nếu viết bằng C++/Pascal"
    Tích có thể lên tới khoảng $(5 \cdot 10^7)^2 = 2{,}5 \cdot 10^{15}$, vượt kiểu `int` 32-bit. Hãy dùng `long long` (C++) hoặc `int64` (Pascal).

```python title="dongho.py"
--8<-- "bang-a/2026/20260920-de1/sol/dongho.py"
```
