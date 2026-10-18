---
name: tinhoctre-docs
description: Extract đề thi Tin học trẻ từ các PDF trong data/new_pdfs/, viết thành trang đề bài + đáp án + lời giải Python trong docs/, cập nhật nav/index, build mkdocs --strict, rồi chuyển PDF đã xử lý sang data/pdfs/. PDF trùng kỳ thi đã có thì tổ hợp thông tin vào đề hiện có và ghi đè PDF bản cũ. Dùng khi người dùng gọi /tinhoctre-docs, hoặc nhờ "thêm đề mới", "extract đề từ PDF", "đưa đề lên site", "cập nhật đề bản mới".
argument-hint: "[tên file PDF trong data/new_pdfs (bỏ trống = xử lý tất cả)]"
---

# /tinhoctre-docs

Biến PDF đề thi trong `data/new_pdfs/` thành trang docs trên site, rồi chuyển PDF sang `data/pdfs/`.

Đọc `CLAUDE.md` ở gốc repo trước nếu chưa có trong ngữ cảnh. Template trang ở [templates.md](templates.md).

## Nguyên tắc bắt buộc

1. **Không bịa đề.** Chỉ chép những gì PDF ghi. Thứ gì tự thêm (định dạng vào/ra, ví dụ, ràng buộc, giả định) phải đánh dấu `(bổ sung)` và giải thích trong admonition `Nguồn đề`.
2. **Code trong PDF không đáng tin.** Tài liệu tổng hợp thường có code sai, thiếu điều kiện hoặc lệch với mô tả. Tự kiểm chứng; nếu sai, viết lời giải đúng và ghi chú lỗi trong `dap-an.md`.
3. **Bài thiếu thông tin** (không rõ yêu cầu, chỉ có tên bài): vẫn liệt kê trong bảng tổng quan, ghi `!!! info "Thiếu đề chi tiết"`, không viết lời giải đoán mò.
4. Chỉ chuyển PDF sang `data/pdfs/` khi mọi bài trong PDF đã được đưa vào docs (kể cả dạng "thiếu đề chi tiết") **và** `mkdocs build --strict` pass. PDF trùng tên trong `data/pdfs/` thì ghi đè bản cũ (xem bước 11).
5. Không commit, không push trừ khi người dùng yêu cầu.

## Quy trình

### 1. Liệt kê đầu vào

```bash
ls -la data/new_pdfs/
```

Có `$ARGUMENTS` thì chỉ xử lý file đó. Thư mục rỗng thì báo và dừng.

### 2. Đọc PDF

Dùng công cụ **Read** trên từng PDF (đọc được tiếng Việt và ảnh trang; PDF trên 10 trang thì truyền `pages`, mỗi lần tối đa 20 trang). Repo không có `pdftotext`/`pypdf`, không cần cài.

Với mỗi PDF, ghi nhận:

- Đơn vị tổ chức (phường/quận/TP), năm học, **ngày thi** (nếu có), vòng thi.
- Các bảng thi có trong PDF (một PDF có thể chứa nhiều bảng).
- Mỗi bài: tên, tên file code (nếu có), điểm, chủ đề, đề bài, ràng buộc, subtask, định dạng vào/ra, ví dụ, code mẫu.
- Thời gian làm bài, ngôn ngữ, giới hạn thời gian/bộ nhớ, cách đọc/ghi dữ liệu.

Nhiều PDF có thể mô tả **cùng một kỳ thi**: gộp lại thành một đề, lấy bản chi tiết hơn làm chính, đối chiếu các bản và ghi chú chỗ lệch nhau.

### 3. Kiểm tra trùng

```bash
grep -rn "<tên đơn vị>" docs/ mkdocs.yml
```

Nếu kỳ thi đã có trên site (cùng tên file trong `data/pdfs/`, hoặc cùng đơn vị + năm + bảng): **không tạo thư mục mới**, mà tổ hợp thông tin vào đề hiện có theo mục "Tổ hợp với đề đã có" bên dưới.

#### Tổ hợp với đề đã có

Nguồn để tổ hợp: trang docs hiện có (`index.md`, `dap-an.md`, `sol/`), PDF mới, và PDF cũ trong `data/pdfs/` nếu còn (đọc trước khi bị ghi đè ở bước 11).

Với từng bài, gộp theo quy tắc:

- **Thêm vào** những gì bản mới có mà docs chưa có: đề chi tiết thay cho "Thiếu đề chi tiết", định dạng vào/ra, ràng buộc, ví dụ, đính chính, giả định.
- **Giữ lại** những gì docs đang có mà bản mới không nhắc tới, vì PDF cũ sắp bị ghi đè và docs là nơi duy nhất còn lưu thông tin đó.
- **Mâu thuẫn** giữa các bản: lấy bản mới hơn nếu nó tự ghi là đính chính. Nếu không rõ bản nào đúng, ghi cả hai cách trong `!!! note` và nêu trong báo cáo.
- **Nhãn nguồn:** phần trước đây ghi "(bổ sung)" mà nay tài liệu đã có thì bỏ nhãn. "Cách hiểu đề dùng cho lời giải tham khảo" mà nay tài liệu đã chốt thì đổi thành ghi chú dẫn theo tài liệu (ví dụ `!!! note "Lưu ý đính chính của tài liệu"`). Ví dụ do site tự thêm vẫn giữ nhãn "(bổ sung)".
- Cập nhật admonition "Nguồn đề" cho đúng các tài liệu đã dùng.
- Điều kiện đề thay đổi thì sửa lời giải và `dap-an.md`, rồi chạy lại toàn bộ bước 7. Ví dụ trong đề phải khớp với output của lời giải mới.
- Số bài thay đổi thì cập nhật cột "Số bài" ở các trang index (bước 9).

### 4. Xác định vị trí

`docs/<bảng>/<năm>/<slug>/` với:

- `<năm>`: năm diễn ra kỳ thi (năm học 2024–2025 thi đầu năm 2025 → `2025`).
- `<slug>`: `yyyymmdd-de<n>` nếu biết ngày thi; nếu không, `<viết tắt đơn vị><năm>-de<n>` (`nhs` Ngũ Hành Sơn, `hc` Hải Châu, `tk` Thanh Khê, `st` Sơn Trà, `lc` Liên Chiểu, `cl` Cẩm Lệ, `hv` Hòa Vang...). Đơn vị mới thì lấy chữ cái đầu mỗi từ, không dấu.
- Tên hiển thị: `Quận <Tên> <năm>` hoặc `Đề <n> (dd/mm/yyyy)`.

### 5. Viết đề bài `index.md`

Theo template trong [templates.md](templates.md). Công thức dùng `$...$` (MathJax). Dùng `* ` cho gạch đầu dòng trong mục Dữ liệu/Kết quả, ví dụ trong code block không ngôn ngữ.

Khi đề chỉ có mô tả tóm tắt mà bài đủ rõ để giải: bổ sung "Dữ liệu (bổ sung)", "Kết quả (bổ sung)", 2–3 ví dụ (có ví dụ biên). Đầu ra ví dụ phải lấy từ **lời giải đã chạy**, không tính nhẩm.

Chỗ mơ hồ/mâu thuẫn trong đề gốc (tiêu đề nói "đếm" nhưng yêu cầu "tính tổng", ràng buộc ngầm trong code mẫu...): ghi `!!! note "Cách hiểu đề dùng cho lời giải tham khảo"` nêu rõ cách hiểu đã chọn.

### 6. Viết lời giải `sol/*.py`

- Tên file: tên file code chính thức viết thường nếu đề có (`FRIEND.PY` → `friend.py`), nếu không thì tên bài không dấu viết liền (`ghepthe.py`).
- Python 3, chỉ thư viện chuẩn. Hàm `solve_<ten>(data)` nhận toàn bộ input dạng chuỗi, trả về chuỗi kết quả. Khối `__main__` đọc `input.inp` / ghi `output.out`, fallback stdin/stdout (xem template).
- Bài Bảng A (Scratch): viết kiểu dễ chuyển sang Scratch (vòng lặp, danh sách, tránh thư viện), có thể dùng `input()` trực tiếp như các đề Bảng A hiện có.
- Đạt độ phức tạp đề yêu cầu cho subtask lớn nhất. Ghi lưu ý cho C++ khi có tràn số.

### 7. Kiểm chứng lời giải

Bắt buộc, cho mọi bài có lời giải:

1. Chạy từng ví dụ: `printf '<input>' | .venv/bin/python docs/<...>/sol/<file>.py` và so với đầu ra mong đợi.
2. Bài có thể vét cạn: viết brute force + sinh test ngẫu nhiên nhỏ trong scratchpad (không bỏ vào repo), đối chiếu vài trăm test.
3. Thử test lớn nhất để ước lượng thời gian so với giới hạn của đề.
4. Nếu code mẫu trong PDF cho kết quả khác lời giải của bạn: tìm nguyên nhân, ghi vào `dap-an.md` (admonition `warning` "Lỗi trong code mẫu của tài liệu").

### 8. Viết `dap-an.md`

Theo template: bảng tóm tắt (STT, Bài, Ý tưởng, Độ phức tạp), mỗi bài có **Ý tưởng**, bẫy thường gặp, lưu ý C++ nếu cần, rồi nhúng code bằng snippet `--8<-- "<bảng>/<năm>/<slug>/sol/<file>.py"`.

### 9. Cập nhật index và nav

- `mkdocs.yml`: thêm mục dưới đúng bảng/năm (năm mới hơn đứng trước; năm chưa có thì tạo nhóm năm kèm `<bảng>/<năm>/index.md`).
- `docs/<bảng>/<năm>/index.md`: tạo mới nếu chưa có, thêm dòng đề.
- `docs/<bảng>/index.md`: thêm dòng vào "Danh sách đề" (mới nhất lên đầu).
- `docs/index.md`: tăng cột "Số đề" của bảng, thêm link vào "Đề mới nhất".

### 10. Build

```bash
.venv/bin/mkdocs build --strict
```

Lỗi thì sửa đến khi pass. Không bỏ `--strict` (CI dùng `--strict`).

### 11. Chuyển PDF

Chỉ khi bước 10 pass:

```bash
mkdir -p data/pdfs && mv -f "data/new_pdfs/<file>.pdf" data/pdfs/
```

PDF trùng tên trong `data/pdfs/` được coi là **bản cũ của cùng tài liệu**: ghi đè luôn, không cần hỏi, nhưng chỉ sau khi đã tổ hợp xong thông tin của bản cũ vào docs (bước 3). PDF mới cùng kỳ thi mà khác tên thì chuyển vào bình thường, không xóa PDF cũ. Kiểm tra lại bằng `ls data/new_pdfs data/pdfs`.

### 12. Báo cáo

Ngắn gọn, gồm:

- Bảng: PDF → đề đã tạo hoặc đã cập nhật (đường dẫn) → số bài (có lời giải / thiếu đề).
- Với đề đã có: những gì đã thêm, đã đổi, mâu thuẫn giữa các bản và cách đã chọn.
- Những gì đã **bổ sung** hoặc **giả định** (không có trong đề gốc).
- Lỗi phát hiện trong đề/code mẫu của tài liệu.
- Kết quả kiểm chứng (số test, ví dụ pass) và build.
- PDF đã chuyển (ghi rõ file nào đã ghi đè bản cũ) / còn lại trong `new_pdfs` kèm lý do.
