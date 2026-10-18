# Đáp án - Bảng A Quận Hải Châu 2025

Lời giải tham khảo bằng Python 3. Xem lại [đề bài](index.md).

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Vẽ hoa văn ngôi sao 8 cánh | Chưa có lời giải (thiếu đề chi tiết) | - |
| 2 | Đếm số chia hết cho 3 và 5 | Chia hết cho 3 và 5 ⇔ chia hết cho 15; tổng cấp số cộng | $O(1)$ |
| 3 | Sắp xếp sách trong thư viện | Chưa có lời giải (thiếu đề chi tiết) | - |

---

## 1. Vẽ hoa văn ngôi sao 8 cánh

Chưa có lời giải: tài liệu nguồn không mô tả hình cần vẽ. Hướng chung khi vẽ hình lặp có 8 cánh trên Scratch: vẽ một cánh, xoay $360° / 8 = 45°$, lặp lại 8 lần; nhấc bút khi di chuyển giữa các phần để nét không bị lem.

## 2. Đếm số chia hết cho 3 và 5

**Cách 1 - duyệt (dễ làm trên Scratch).** Cho biến $i$ chạy từ 1 đến $N$, nếu $i$ chia hết cho 3 **và** chia hết cho 5 thì cộng $i$ vào tổng.

**Cách 2 - công thức.** 3 và 5 không có ước chung lớn hơn 1, nên một số chia hết cho cả 3 và 5 khi và chỉ khi nó chia hết cho 15. Các số cần cộng là $15, 30, \ldots, 15k$ với $k = \lfloor N / 15 \rfloor$:

$$15 + 30 + \cdots + 15k = 15 \cdot (1 + 2 + \cdots + k) = 15 \cdot \frac{k(k+1)}{2}$$

Ví dụ $N = 100$: $k = 6$, tổng $= 15 \cdot 21 = 315$.

!!! warning "Bẫy thường gặp"
    - Cộng các số chia hết cho 3 **hoặc** 5 (sai điều kiện): đề yêu cầu chia hết cho **cả** 3 và 5.
    - Với $N$ rất lớn (ví dụ $10^9$), cách duyệt chạy rất lâu; dùng công thức.

```python title="tongchiahet.py"
--8<-- "bang-a/2025/hc2025-de1/sol/tongchiahet.py"
```

## 3. Sắp xếp sách trong thư viện

Chưa có lời giải: tài liệu nguồn không mô tả đề bài.
