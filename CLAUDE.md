# CLAUDE.md

Website tuyển tập đề thi **Tin học trẻ** kèm lời giải tham khảo bằng Python và C++, build bằng MkDocs Material, deploy lên https://tinhoctre.smart-pens.com/ qua GitHub Actions khi push `main`.

Nội dung site viết bằng **tiếng Việt**.

## Lệnh

```bash
source .venv/bin/activate          # hoặc gọi trực tiếp .venv/bin/mkdocs
mkdocs serve                       # xem local tại http://127.0.0.1:8000
mkdocs build --strict              # CI chạy --strict: link hỏng hay snippet sai là fail
```

## Cấu trúc

```
data/new_pdfs/   PDF đề mới, chưa đưa lên site (đầu vào của skill /tinhoctre-docs)
data/pdfs/       PDF đã extract xong thành docs
docs/<bảng>/<năm>/<slug>/
  index.md       đề bài
  dap-an.md      đáp án, nhúng code bằng --8<-- "<bảng>/<năm>/<slug>/sol/<file>.py"
  sol/*.py       lời giải Python 3 chạy được
  sol/*.cpp      lời giải C++17 cùng thuật toán, cùng tên file
mkdocs.yml       nav (menu) phải khai báo thủ công từng trang
site/            output build, đã gitignore
```

Bảng: `bang-a` (Tiểu học), `bang-b` (THCS), `bang-c` (THPT), `bang-m` (Tư duy thuật toán), `bang-d` (Sáng tạo).

Slug thư mục đề: `yyyymmdd-de<n>` nếu biết ngày thi; nếu không, `<viết tắt đơn vị><năm>-de<n>` (ví dụ `nhs2025-de1` = Ngũ Hành Sơn, `hc2025-de1` = Hải Châu).

## Quy ước nội dung

- Không bịa đề. Phần nào nhóm biên soạn tự bổ sung (định dạng vào/ra, ví dụ, ràng buộc) phải ghi `(bổ sung)` trong tiêu đề và có admonition `!!! warning "Nguồn đề"` giải thích. Bài thiếu đề chi tiết thì ghi `!!! info "Thiếu đề chi tiết"`, không viết lời giải đoán mò.
- Đề gốc có chỗ mơ hồ hoặc mâu thuẫn: ghi `!!! note "Cách hiểu đề dùng cho lời giải tham khảo"`.
- Code mẫu trong PDF có thể sai; luôn kiểm chứng trước khi dùng.
- Lời giải: Python 3 và C++17 (chỉ header chuẩn cụ thể, không `<bits/stdc++.h>` vì máy dev dùng Apple clang), đọc `input.inp` / ghi `output.out`, fallback stdin/stdout khi không có file; comment tiếng Việt, ngắn. `dap-an.md` nhúng hai bản trong content tabs `=== "Python"` / `=== "C++"`.
- Thêm đề mới phải cập nhật đủ: `mkdocs.yml` (nav), `docs/index.md` (cột "Số đề" + "Đề mới nhất"), `docs/<bảng>/index.md`, `docs/<bảng>/<năm>/index.md`.

## Bài giảng (slide)

Site con riêng tại `/slides/` (không nằm trong menu MkDocs; MkDocs chỉ chép nguyên `docs/slides/` ra site).

```
slides/<bảng>/<slug>/
  deck.json          tiêu đề, thứ tự slide (order), font
  meta.json          tiêu đề, mô tả, ngày, tags, link đề / đáp án (hiện ở trang danh sách)
  slides/<id>.html   mỗi file một <section> 1920×1080, style inline
scripts/build_slides.py   sinh docs/slides/index.html (danh sách) và docs/slides/<bảng>/<slug>/index.html (trình chiếu)
```

- Không sửa tay `docs/slides/`; sửa trong `slides/` rồi chạy `python3 scripts/build_slides.py` và commit cả `docs/slides/` (CI không chạy script này).
- Thêm bài giảng mới: tạo thư mục trong `slides/` (slug trùng slug đề) kèm `meta.json`, chạy script, thêm admonition `!!! info "Bài giảng"` ở trang đề tương ứng. Không cần sửa `mkdocs.yml`.
- Code trên slide có thể viết gọn (stdin/stdout) nhưng phải cùng thuật toán và đã chạy thử với ví dụ của đề.

## Sách PDF

`python3 scripts/build_book.py` gom toàn bộ đề trong nav của `mkdocs.yml` thành `book/tin-hoc-tre.pdf` (Phần I đề thi, Phần II đáp án, cùng thứ tự menu; code Python và C++). Cần pandoc, XeLaTeX (TeX Live) và PyYAML. Script tự đổi admonition, content tabs, snippet `--8<--`, ảnh và công thức sang LaTeX; link nội bộ thành chữ thường. Thêm đề mới vào nav là sách tự có, chỉ cần build lại.

## Skill

- `/tinhoctre-docs`: extract đề từ `data/new_pdfs/`, viết docs + lời giải, build kiểm tra, rồi chuyển PDF sang `data/pdfs/`.
