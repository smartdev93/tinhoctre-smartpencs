# CLAUDE.md

Website tuyển tập đề thi **Tin học trẻ** kèm lời giải tham khảo bằng Python, build bằng MkDocs Material, deploy lên https://tinhoctre.smart-pens.com/ qua GitHub Actions khi push `main`.

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
mkdocs.yml       nav (menu) phải khai báo thủ công từng trang
site/            output build, đã gitignore
```

Bảng: `bang-a` (Tiểu học), `bang-b` (THCS), `bang-c` (THPT), `bang-m` (Tư duy thuật toán), `bang-d` (Sáng tạo).

Slug thư mục đề: `yyyymmdd-de<n>` nếu biết ngày thi; nếu không, `<viết tắt đơn vị><năm>-de<n>` (ví dụ `nhs2025-de1` = Ngũ Hành Sơn, `hc2025-de1` = Hải Châu).

## Quy ước nội dung

- Không bịa đề. Phần nào nhóm biên soạn tự bổ sung (định dạng vào/ra, ví dụ, ràng buộc) phải ghi `(bổ sung)` trong tiêu đề và có admonition `!!! warning "Nguồn đề"` giải thích. Bài thiếu đề chi tiết thì ghi `!!! info "Thiếu đề chi tiết"`, không viết lời giải đoán mò.
- Đề gốc có chỗ mơ hồ hoặc mâu thuẫn: ghi `!!! note "Cách hiểu đề dùng cho lời giải tham khảo"`.
- Code mẫu trong PDF có thể sai; luôn kiểm chứng trước khi dùng.
- Lời giải: Python 3, đọc `input.inp` / ghi `output.out`, fallback stdin/stdout khi không có file; comment tiếng Việt, ngắn.
- Thêm đề mới phải cập nhật đủ: `mkdocs.yml` (nav), `docs/index.md` (cột "Số đề" + "Đề mới nhất"), `docs/<bảng>/index.md`, `docs/<bảng>/<năm>/index.md`.

## Skill

- `/tinhoctre-docs`: extract đề từ `data/new_pdfs/`, viết docs + lời giải, build kiểm tra, rồi chuyển PDF sang `data/pdfs/`.
