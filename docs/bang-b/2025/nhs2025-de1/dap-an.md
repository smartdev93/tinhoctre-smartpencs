# Đáp án - Bảng B Quận Ngũ Hành Sơn 2025

Lời giải tham khảo bằng Python 3. Xem lại [đề bài](index.md).

Mỗi chương trình đọc `input.inp` và ghi `output.out` như đề yêu cầu. Nếu không có file `input.inp`, chương trình đọc từ bàn phím và in ra màn hình để tiện thử.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Phân bổ tài nguyên | Chưa có lời giải (thiếu đề chi tiết) | - |
| 2 | Ghép thẻ tạo số lớn nhất | Sắp xếp với phép so sánh $A + B > B + A$ | $O(N \log N)$ |
| 3 | Biến đổi xâu đối xứng | Quy hoạch động trên đoạn | $O(N^2)$ |

---

## 1. Phân bổ tài nguyên & tối ưu hóa

Chưa có lời giải: tài liệu nguồn không cho biết công thức chế tạo sản phẩm. Hướng chung theo gợi ý của đề:

- **Subtask 1** ($N, M \le 10^3$): thử mọi số lượng của một loại sản phẩm, tính phần còn lại cho loại kia.
- **Subtask 2** ($N, M \le 10^9$): vòng lặp $10^9$ bước chạy quá thời gian, cần rút ra công thức (thường dạng `min(...)` và phép chia nguyên).

## 2. Ghép thẻ tạo số lớn nhất

**Ý tưởng.** Coi mỗi số là một xâu. Thẻ `a` nên đứng trước thẻ `b` khi `a + b > b + a` (phép `+` là nối xâu). Ví dụ `"9" + "31" = "931"` lớn hơn `"31" + "9" = "319"`, nên `9` đứng trước `31`. Sắp xếp theo phép so sánh này rồi nối lại.

Phép so sánh này có tính bắc cầu nên dùng được để sắp xếp: nếu `ab > ba` và `bc > cb` thì `ac > ca`.

!!! warning "Bẫy thường gặp"
    - Sắp xếp xâu theo thứ tự từ điển thông thường sai: `"3"` và `"30"` cho `"303"` thay vì `"330"`.
    - Sắp xếp theo giá trị số cũng sai: `9` đứng sau `31` khi so số.
    - Khi mọi thẻ là `0`, phải in `0`, không in `000`.

!!! note "Nếu viết bằng C++"
    Kết quả có thể dài tới $10^6$ chữ số, không lưu được trong `long long`. Hãy dùng `std::string` và `sort` với hàm so sánh `return a + b > b + a;`.

```python title="ghepthe.py"
--8<-- "bang-b/2025/nhs2025-de1/sol/ghepthe.py"
```

## 3. Biến đổi xâu đối xứng

**Ý tưởng.** Gọi $DP[i][j]$ là số ký tự ít nhất cần chèn vào đoạn $S[i..j]$ để thành xâu đối xứng.

- Đoạn có 0 hoặc 1 ký tự: $DP = 0$.
- Nếu $S[i] = S[j]$: hai đầu đã khớp, $DP[i][j] = DP[i+1][j-1]$.
- Ngược lại: chèn thêm một ký tự để khớp một trong hai đầu, $DP[i][j] = 1 + \min(DP[i+1][j],\ DP[i][j-1])$.

Đáp án là $DP[0][N-1]$. Có $N^2 / 2$ trạng thái, mỗi trạng thái tính trong $O(1)$.

Vì $DP[i][\cdot]$ chỉ cần hàng $i+1$, lời giải dùng **một mảng một chiều** (bộ nhớ $O(N)$), duyệt $i$ từ cuối lên.

!!! tip "Cách nhìn khác"
    Đáp án bằng $N$ trừ độ dài **xâu con đối xứng dài nhất** (LPS), cũng bằng $N$ trừ độ dài xâu con chung dài nhất của $S$ và $S$ đảo ngược.

```python title="xaudoixung.py"
--8<-- "bang-b/2025/nhs2025-de1/sol/xaudoixung.py"
```
