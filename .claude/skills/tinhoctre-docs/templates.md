# Templates cho /tinhoctre-docs

Mẫu tham chiếu thật: `docs/bang-b/2025/nhs2025-de1/` (đề tóm tắt, có phần bổ sung) và `docs/bang-a/2026/20260920-de1/` (đề đầy đủ).

## `index.md` (đề bài)

````markdown
# Đề thi Bảng <X> - <Tên kỳ thi>

Hội thi Tin học trẻ <đơn vị>, năm học <yyyy–yyyy> (<vòng thi nếu có>). Thời gian làm bài: **<n> phút**, ngôn ngữ **<C++ / Python>**.

<Hình thức chấm, giới hạn thời gian/bộ nhớ, cách đọc/ghi dữ liệu nếu đề có ghi.>

!!! warning "Nguồn đề"
    Đề được trích từ tài liệu *<tên tài liệu/PDF>*. <Tài liệu thiếu gì.> Phần "<...>" do nhóm biên soạn bổ sung để luyện tập, **không phải đề gốc**.

## Tổng quan bài thi

| STT | Bài | Chủ đề | Điểm |
| ---: | --- | --- | ---: |
| 1 | <Tên bài> | <Chủ đề> | <điểm> |

---

## 1. <Tên bài>

<Đề bài, chép sát nguyên văn.>

- **Ràng buộc:** ...

### Dữ liệu

* ...

### Kết quả

* ...

### Ví dụ 1

#### Nhập vào

```
...
```

#### In ra

```
...
```

#### Giải thích

* ...

---

!!! tip "Đáp án"
    Tự làm trước, sau đó xem [lời giải tham khảo](dap-an.md).
````

Bỏ admonition "Nguồn đề" nếu đề gốc đầy đủ. Tiêu đề mục tự thêm ghi `### Dữ liệu (bổ sung)`. Bài thiếu đề:

```markdown
!!! info "Thiếu đề chi tiết"
    Tài liệu nguồn chỉ ghi <...>, nên chưa thể viết đề đầy đủ hay lời giải. Nếu bạn có đề gốc, hãy gửi qua issue trên GitHub.
```

## `dap-an.md`

````markdown
# Đáp án - Bảng <X> <Tên kỳ thi>

Lời giải tham khảo bằng Python 3. Xem lại [đề bài](index.md).

Mỗi chương trình đọc `input.inp` và ghi `output.out` như đề yêu cầu. Nếu không có file `input.inp`, chương trình đọc từ bàn phím và in ra màn hình để tiện thử.

| STT | Bài | Ý tưởng | Độ phức tạp |
| ---: | --- | --- | --- |
| 1 | <Tên bài> | <ý tưởng 1 dòng> | $O(...)$ |

---

## 1. <Tên bài>

**Ý tưởng.** <Giải thích ngắn, có ví dụ minh họa.>

!!! warning "Bẫy thường gặp"
    - ...

!!! note "Nếu viết bằng C++"
    <tràn số, kiểu dữ liệu, I/O nhanh...>

```python title="<file>.py"
--8<-- "<bảng>/<năm>/<slug>/sol/<file>.py"
```
````

## `sol/<file>.py`

```python
import sys


def solve_<ten>(data):
    tokens = data.split()
    # ...
    return str(ans)


if __name__ == "__main__":
    try:
        with open("input.inp") as f:
            data = f.read()
        with open("output.out", "w") as f:
            f.write(solve_<ten>(data) + "\n")
    except FileNotFoundError:
        print(solve_<ten>(sys.stdin.read()))
```

## Dòng index

`docs/<bảng>/index.md`:

```markdown
| <dd/mm/yyyy hoặc yyyy> | [<Tên hiển thị>](<năm>/<slug>/index.md) | <số bài> | [Xem](<năm>/<slug>/dap-an.md) |
```

`docs/<bảng>/<năm>/index.md`:

```markdown
| <Kỳ thi hoặc ngày> | [Đề](<slug>/index.md) · [Đáp án](<slug>/dap-an.md) | <số bài> |
```

`docs/index.md` mục "Đề mới nhất":

```markdown
- [Bảng <X> - <Tên hiển thị>](<bảng>/<năm>/<slug>/index.md) · [Đáp án](<bảng>/<năm>/<slug>/dap-an.md)
```

`mkdocs.yml` nav:

```yaml
          - "<Tên hiển thị>":
              - Đề bài: <bảng>/<năm>/<slug>/index.md
              - Đáp án: <bảng>/<năm>/<slug>/dap-an.md
```
