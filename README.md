# tinhoctre-smartpencs

Tuyển tập đề thi **Tin học trẻ** kèm lời giải tham khảo, xuất bản dạng website bằng [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

Website: https://tinhoctre.smart-pens.com/

## Cấu trúc

```
docs/
  index.md                     # trang chủ + tổng quan các bảng thi
  <bảng>/index.md              # giới thiệu bảng + danh sách đề (bang-a, bang-b, bang-c, bang-m, bang-d)
  <bảng>/<năm>/index.md        # danh sách đề theo năm
  <bảng>/<năm>/<yyyymmdd>-de<n>/
    index.md                   # đề bài
    dap-an.md                  # đáp án (nhúng code từ sol/)
    sol/*.py                   # lời giải chạy được
mkdocs.yml                     # cấu hình site + menu (nav)
```

## Chạy local

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve        # mở http://127.0.0.1:8000
```

## Thêm đề mới

1. Tạo thư mục `docs/<bảng>/<năm>/<yyyymmdd>-de<n>/` với `index.md`, `dap-an.md`, `sol/`.
2. Trong `dap-an.md`, nhúng code bằng snippet: `--8<-- "<bảng>/<năm>/<thư mục>/sol/<file>.py"`.
3. Thêm đề vào `nav` trong `mkdocs.yml`, bảng ở `docs/index.md`, `docs/<bảng>/index.md` và `docs/<bảng>/<năm>/index.md`.
4. Push lên `main`: GitHub Actions tự build và deploy lên nhánh `gh-pages`.

## Bài giảng (slide)

Site con riêng tại https://tinhoctre.smart-pens.com/slides/. Nguồn slide nằm ở `slides/<bảng>/<slug>/` (`deck.json`, `meta.json`, `slides/*.html`). Sau khi sửa, build lại rồi commit cả `docs/slides/`:

```bash
python3 scripts/build_slides.py     # sinh docs/slides/ (trang danh sách + trình chiếu)
```

## Sách PDF

`python3 scripts/build_book.py` gom toàn bộ đề trong nav của `mkdocs.yml` thành `book/tin-hoc-tre.pdf` (Phần I đề thi, Phần II đáp án, cùng thứ tự menu; code Python và C++). Cần pandoc, XeLaTeX (TeX Live) và PyYAML. Script tự đổi admonition, content tabs, snippet `--8<--`, ảnh và công thức sang LaTeX; link nội bộ thành chữ thường. Thêm đề mới vào nav là sách tự có, chỉ cần build lại.
