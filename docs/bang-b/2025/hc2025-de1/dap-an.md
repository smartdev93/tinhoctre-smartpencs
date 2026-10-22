# Đáp án - Bảng B Quận Hải Châu 2025

Lời giải tham khảo bằng Python 3 và C++ (C++17). Xem lại [đề bài](index.md).

Mỗi chương trình đọc từ bàn phím và in ra màn hình như code mẫu của tài liệu. Nếu có file `input.inp`, chương trình đọc từ file và ghi kết quả ra `output.out`.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | Cặp số thân thiện | Tính tổng ước bằng cách duyệt đến $\sqrt{N}$, kiểm tra $A \ne B$ | $O(\sqrt{N})$ |
| 2 | Nén xâu đảo ngược | Đếm từng đoạn ký tự giống nhau, rồi đảo xâu | $O(N)$ |
| 3 | Đoạn con có tổng lớn nhất | Kadane | $O(N)$ |
| 4 | Sắp đặt hàng hóa | Sắp xếp + hai con trỏ | $O(N \log N)$ |

---

## 1. Cặp số thân thiện

**Ý tưởng.** Ước của $n$ đi theo cặp $(i, n/i)$ với $i \le \sqrt{n}$. Duyệt $i$ từ 2 đến $\sqrt{n}$, mỗi lần $i$ chia hết $n$ thì cộng cả $i$ và $n/i$ (chỉ cộng một lần nếu $i = n/i$). Cộng thêm ước 1, không cộng chính $n$.

Với $N = 10^{12}$, vòng lặp chạy khoảng $10^6$ bước thay vì $10^{12}$.

Đáp án là `YES` khi $A \ne B$, tổng ước thực sự của $A$ bằng $B$ và tổng ước thực sự của $B$ bằng $A$. Lời giải kiểm tra $A \ne B$ trước, và chỉ tính tổng ước của $B$ khi tổng ước của $A$ đã bằng $B$, nên phần lớn test chỉ tốn một vòng $\sqrt{N}$.

!!! warning "Bẫy thường gặp"
    - Quên điều kiện $A \ne B$: test `6 6` (số hoàn hảo) sẽ in sai `YES`.
    - $n = 1$ không có ước thực sự nào, tổng là 0. Nếu duyệt từ $i = 1$ và cộng cả $i$ lẫn $n / i$ mà không xử lý riêng, tổng ước của 1 thành 1. Code mẫu trong tài liệu *Tổng hợp đề thi & đáp án* mắc lỗi này. Lời giải này trả về 0 khi $n \le 1$.
    - Duyệt đến $n - 1$ hoặc $n / 2$ quá chậm với $N = 10^{12}$.
    - Điều kiện dừng `i * i <= n` tránh dùng `sqrt` số thực (có thể sai số với số lớn).

!!! note "Nếu viết bằng C++"
    $A, B$ và tổng ước có thể vượt $2^{31}$, phải dùng `long long` cho cả biến chạy `i` (vì `i * i` lên tới $10^{12}$).

=== "Python"

    ```python title="friend.py"
    --8<-- "bang-b/2025/hc2025-de1/sol/friend.py"
    ```

=== "C++"

    ```cpp title="friend.cpp"
    --8<-- "bang-b/2025/hc2025-de1/sol/friend.cpp"
    ```

## 2. Nén xâu đảo ngược

**Ý tưởng.** Duyệt xâu, tại mỗi vị trí $i$ tìm $j$ là vị trí đầu tiên có ký tự khác $S[i]$. Đoạn $S[i..j-1]$ nén thành `str(j - i) + S[i]`. Nhảy $i = j$ và lặp lại. Cuối cùng đảo ngược cả xâu kết quả.

Mỗi ký tự được duyệt đúng một lần nên độ phức tạp $O(N)$.

!!! warning "Bẫy thường gặp"
    - Nối xâu bằng `res = res + ...` trong vòng lặp có thể thành $O(N^2)$ trong một số ngôn ngữ. Python nên gom vào danh sách rồi `"".join(...)`; C++ dùng `res += ...` là ổn.
    - Số lần lặp có thể có nhiều chữ số (`12a`). Đề yêu cầu đảo **toàn bộ** xâu nên chữ số cũng bị đảo (`a21`), không đảo theo từng cụm.

=== "Python"

    ```python title="compress.py"
    --8<-- "bang-b/2025/hc2025-de1/sol/compress.py"
    ```

=== "C++"

    ```cpp title="compress.cpp"
    --8<-- "bang-b/2025/hc2025-de1/sol/compress.cpp"
    ```

## 3. Đoạn con có tổng lớn nhất

**Ý tưởng (Kadane).** Gọi $cur$ là tổng lớn nhất của đoạn con **kết thúc tại** phần tử đang xét $x$. Có hai lựa chọn: nối $x$ vào đoạn tốt nhất kết thúc ở phần tử trước, hoặc bắt đầu đoạn mới chỉ gồm $x$:

$$cur = \max(x,\ cur + x)$$

Đáp án là giá trị lớn nhất của $cur$ trong quá trình duyệt.

!!! warning "Bẫy thường gặp"
    - Khởi tạo đáp án bằng 0 sẽ sai khi mọi phần tử đều âm (đáp án đúng là phần tử lớn nhất, không phải 0).
    - Vét cạn mọi đoạn $O(N^2)$ hoặc $O(N^3)$ quá chậm với $N = 10^5$.

!!! note "Nếu viết bằng C++"
    Tổng có thể tới $10^5 \cdot 10^9 = 10^{14}$, phải dùng `long long`.

=== "Python"

    ```python title="maxsub.py"
    --8<-- "bang-b/2025/hc2025-de1/sol/maxsub.py"
    ```

=== "C++"

    ```cpp title="maxsub.cpp"
    --8<-- "bang-b/2025/hc2025-de1/sol/maxsub.cpp"
    ```

## 4. Sắp đặt hàng hóa

**Ý tưởng.** Sắp xếp các kiện tăng dần. Kiện nặng nhất (con trỏ `right`) chắc chắn chiếm một thùng. Nó nên đi cùng kiện nhẹ nhất (con trỏ `left`) nếu vừa: nếu kiện nhẹ nhất không ghép được với kiện nặng nhất thì không kiện nào ghép được, còn nếu ghép được thì chọn kiện nhẹ nhất là an toàn nhất (để dành các kiện nặng hơn cho những kiện còn lại, vốn nhẹ hơn kiện nặng nhất).

Mỗi bước, `right` giảm 1 và số thùng tăng 1; nếu ghép được thì `left` tăng 1.

!!! warning "Lưu ý về giả định của đề"
    Thuật toán này chỉ đúng khi **mỗi thùng chứa tối đa 2 kiện**, đúng như giả định bổ sung của tài liệu. Lời giải đã được đối chiếu với vét cạn trên 400 test ngẫu nhiên nhỏ theo giả định đó.

!!! note "Nếu viết bằng C++"
    $W_{left} + W_{right}$ có thể tới $2 \cdot 10^9$, vượt `int`; lời giải lưu trọng lượng bằng `long long`.

=== "Python"

    ```python title="arrange.py"
    --8<-- "bang-b/2025/hc2025-de1/sol/arrange.py"
    ```

=== "C++"

    ```cpp title="arrange.cpp"
    --8<-- "bang-b/2025/hc2025-de1/sol/arrange.cpp"
    ```
