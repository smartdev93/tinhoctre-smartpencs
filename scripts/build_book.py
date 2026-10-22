#!/usr/bin/env python3
"""Build sách PDF tuyển tập đề thi Tin học trẻ từ docs/.

Bố cục: Phần I - Đề thi (theo bảng, theo thứ tự menu trong mkdocs.yml),
        Phần II - Đáp án (cùng thứ tự). Code lời giải Python và C++.

Yêu cầu: pandoc (>= 2.9), XeLaTeX (TeX Live có fontspec, polyglossia, fvextra,
         tcolorbox), font TeX Gyre Pagella / DejaVu Sans Mono, PyYAML.

Chạy:   python3 scripts/build_book.py              # -> book/tin-hoc-tre.pdf
        python3 scripts/build_book.py --tex        # chỉ sinh book/tin-hoc-tre.md (để xem)
"""
import datetime
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = ROOT / "book"
NAME = "tin-hoc-tre"

# Nhóm cấp cao nhất trong nav được đưa vào sách (theo đúng thứ tự trong nav).
SKIP_TOP = {"Trang chủ"}

ADMON_TITLES = {
    "note": "Ghi chú",
    "info": "Thông tin",
    "tip": "Gợi ý",
    "warning": "Lưu ý",
}


class SafeLoader(yaml.SafeLoader):
    pass


# mkdocs.yml có thể có tag !!python/name ...; bỏ qua.
SafeLoader.add_multi_constructor("tag:yaml.org,2002:python/", lambda l, s, n: None)


def collect():
    """Trả về [(tên bảng, [(nhãn đề, đường dẫn index.md, đường dẫn dap-an.md)])]."""
    cfg = yaml.load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"), Loader=SafeLoader)
    books = []
    for item in cfg["nav"]:
        (top, val), = item.items()
        if top in SKIP_TOP or not isinstance(val, list):
            continue
        exams = []

        def walk(nodes):
            for n in nodes:
                if not isinstance(n, dict):
                    continue
                (label, v), = n.items()
                if isinstance(v, list):
                    pages = {}
                    for x in v:
                        if isinstance(x, dict):
                            (k, p), = x.items()
                            if isinstance(p, str):
                                pages[k] = p
                    if "Đề bài" in pages:
                        exams.append((label, pages["Đề bài"], pages.get("Đáp án")))
                    else:
                        walk(v)

        walk(val)
        if exams:
            books.append((top, exams))
    return books


def tex_escape(s):
    rep = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
           "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(rep.get(c, c) for c in s)


def strip_inline_md(s):
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"\*\*([^*]*)\*\*", r"\1", s)
    s = re.sub(r"\*([^*]*)\*", r"\1", s)
    return s


def dedent_block(lines, n=4):
    return [l[n:] if l.startswith(" " * n) else l.lstrip() if not l.strip() else l for l in lines]


def convert(md_path: Path, shift: int, drop_answer_tip: bool):
    """Chuyển markdown MkDocs Material sang markdown pandoc + raw LaTeX."""
    base = md_path.parent
    text = md_path.read_text(encoding="utf-8")

    # Snippets: --8<-- "path" (đường dẫn tính từ docs/)
    def snip(m):
        indent, rel = m.group(1), m.group(2)
        p = DOCS / rel
        if not p.exists():
            sys.exit(f"{md_path}: không thấy snippet {rel}")
        return "\n".join(indent + l for l in p.read_text(encoding="utf-8").rstrip("\n").split("\n"))

    text = re.sub(r'^([ \t]*)--8<--\s+"([^"]+)"[ \t]*$', snip, text, flags=re.M)

    lines = text.split("\n")
    out = []
    i = 0
    first_h1 = None
    in_fence = None
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Code fence (giữ nguyên nội dung, chỉ chuẩn hoá dòng mở)
        m = re.match(r"^(\s*)(```+|~~~+)\s*([A-Za-z0-9_+-]*)\s*(.*)$", line)
        if in_fence is None and m:
            indent, fence, lang, rest = m.groups()
            tm = re.search(r'title="([^"]+)"', rest)
            if tm:
                out.append(f"{indent}\\codetitle{{{tex_escape(tm.group(1))}}}")
                out.append("")
            lang = {"cpp": "cpp", "c++": "cpp", "py": "python", "": "", "text": ""}.get(lang.lower(), lang.lower())
            out.append(f"{indent}{fence}{('{.' + lang + '}') if lang else ''}")
            in_fence = (indent, fence)
            i += 1
            continue
        if in_fence is not None:
            out.append(line)
            if stripped.startswith(in_fence[1]) and stripped.strip("`~") == "":
                in_fence = None
            i += 1
            continue

        # Admonition !!! type "Title"
        m = re.match(r'^(\s*)(?:!!!|\?\?\?\+?)\s*([a-z]+)(?:\s+"([^"]*)")?\s*$', line)
        if m:
            indent, kind, title = m.groups()
            title = title if title is not None else ADMON_TITLES.get(kind, kind.capitalize())
            block = []
            j = i + 1
            ind = len(indent) + 4
            while j < len(lines) and (not lines[j].strip() or lines[j].startswith(" " * ind)):
                block.append(lines[j])
                j += 1
            while block and not block[-1].strip():
                block.pop()
            i = j
            if drop_answer_tip and title.strip() in ("Đáp án", "Bài giảng"):
                continue
            inner = "\n".join(convert_lines(dedent_block([l[len(indent):] for l in block], 4)))
            out.append(f"{indent}\\admonbegin{{{kind}}}{{{tex_escape(strip_inline_md(title))}}}")
            out.append("")
            out.extend(indent + l if l else l for l in inner.split("\n"))
            out.append("")
            out.append(f"{indent}\\admonend")
            out.append("")
            continue

        # Content tabs === "Python"
        m = re.match(r'^(\s*)===\s+"([^"]+)"\s*$', line)
        if m:
            indent, label = m.groups()
            out.append(f"{indent}\\tablabel{{{tex_escape(label)}}}")
            out.append("")
            j = i + 1
            ind = len(indent) + 4
            block = []
            while j < len(lines) and (not lines[j].strip() or lines[j].startswith(" " * ind)):
                block.append(lines[j])
                j += 1
            while block and not block[-1].strip():
                block.pop()
            i = j
            inner = "\n".join(convert_lines(dedent_block([l[len(indent):] for l in block], 4)))
            out.extend(indent + l if l else l for l in inner.split("\n"))
            out.append("")
            continue

        # Heading
        m = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
        if m:
            level = len(m.group(1))
            title = re.sub(r"\s*\{[^}]*\}\s*$", "", m.group(2))
            if level == 1 and first_h1 is None:
                first_h1 = title
                i += 1
                continue
            lv = min(level + shift, 6)
            out.append("#" * lv + " " + title)
            i += 1
            continue

        # Đường kẻ ngang ngay sau một dòng chữ sẽ bị pandoc hiểu là heading (setext).
        if re.match(r"^\s*(-{3,}|={3,})\s*$", line) and out and out[-1].strip():
            out.append("")
        out.append(line)
        i += 1

    body = "\n".join(out)
    body = fix_inline(body, base)
    return first_h1, body


def convert_lines(lines):
    # Nội dung trong admonition/tab: xử lý lại bằng chính convert (không đổi cấp heading).
    tmp = "\n".join(lines)
    return CONVERT_INNER(tmp).split("\n")


def CONVERT_INNER(text):
    # Ghi tạm ra chuỗi rồi chạy lại các bước dòng (không có H1 ở đây).
    fake = _Fake(text)
    _, body = convert(fake, 0, False)
    return body


class _Fake:
    """Đối tượng giả Path để convert() đọc chuỗi trong bộ nhớ."""

    def __init__(self, text):
        self._t = text
        self.parent = CURRENT_BASE[0]

    def read_text(self, encoding=None):
        return self._t

    def __str__(self):
        return "<inline>"


CURRENT_BASE = [DOCS]


def fix_inline(body, base):
    # Ảnh: đường dẫn tương đối -> tuyệt đối; giới hạn kích thước.
    def img(m):
        alt, src = m.group(1), m.group(2)
        if not re.match(r"https?://", src):
            src = str((base / src).resolve())
        return f"![{alt}]({src}){{width=90%}}"

    body = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)(\{[^}]*\})?", img, body)
    # Link nội bộ (.md, #anchor) -> chữ thường; link ngoài giữ nguyên.
    body = re.sub(r"(?<!!)\[([^\]]+)\]\((?!https?://)[^)]*\)(\{[^}]*\})?", r"\1", body)
    # attr_list còn sót trên link ngoài
    body = re.sub(r"(\]\(https?://[^)]*\))\{[^}]*\}", r"\1", body)
    body = re.sub("[\U0001F000-\U0001FFFF\u2600-\u27BF\uFE0F]", "", body)  # emoji: font in không có
    body = body.replace("<br>", "\\\n").replace("<br/>", "\\\n").replace("<br />", "\\\n")
    return body


PREAMBLE = r"""
\usepackage{fvextra}
\DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,breakanywhere,commandchars=\\\{\},fontsize=\small}
\usepackage[most]{tcolorbox}
\definecolor{admnote}{HTML}{448AFF}
\definecolor{adminfo}{HTML}{00B8D4}
\definecolor{admtip}{HTML}{00A86B}
\definecolor{admwarning}{HTML}{FF9100}
\newcommand{\admonbegin}[2]{\begin{tcolorbox}[enhanced,breakable,colback=white,colframe=adm#1,boxrule=0pt,leftrule=3pt,arc=1pt,left=8pt,right=8pt,top=4pt,bottom=4pt,fonttitle=\bfseries\small,coltitle=black,colbacktitle=adm#1!12,title={#2},before skip=8pt,after skip=8pt]}
\newcommand{\admonend}{\end{tcolorbox}}
\newcommand{\codetitle}[1]{\par\noindent{\small\ttfamily\color{black!60}#1}\par\nopagebreak}
\newcommand{\tablabel}[1]{\par\medskip\noindent{\bfseries\color{admnote!80!black}#1}\par\nopagebreak}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE]{\small\leftmark}
\fancyhead[RO]{\small\rightmark}
\fancyfoot[C]{\small\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\small\thepage}\renewcommand{\headrulewidth}{0pt}}
\setkeys{Gin}{keepaspectratio}
\usepackage{etoolbox}
\AtBeginEnvironment{longtable}{\small}
\setlength{\emergencystretch}{3em}
\raggedbottom
\setcounter{secnumdepth}{0}
"""

COVER = r"""
\begin{titlepage}
\centering
\vspace*{3cm}
{\Huge\bfseries TUYỂN TẬP ĐỀ THI\\[6pt] TIN HỌC TRẺ\par}
\vspace{1cm}
{\Large Kèm lời giải tham khảo bằng Python và C++\par}
\vspace{2cm}
{\large __BOARDS__\par}
\vfill
{\large Nhóm biên soạn tinhoctre.smart-pens.com\par}
\vspace{4pt}
{\normalsize Bản __DATE__\par}
\vspace{1cm}
\end{titlepage}
"""

FOREWORD = """
# Lời nói đầu {-}

Cuốn sách tập hợp các đề thi thực hành **Tin học trẻ** đã đăng trên trang https://tinhoctre.smart-pens.com/, kèm lời giải tham khảo bằng Python 3 và C++ (C++17). Sách dùng cho học sinh tự luyện và giáo viên tham khảo.

Sách gồm hai phần:

- **Phần I - Đề thi:** các đề xếp theo bảng thi, trong mỗi bảng xếp từ năm mới đến năm cũ.
- **Phần II - Đáp án:** ý tưởng và code lời giải cho từng đề, cùng thứ tự với Phần I. Đầu mỗi đáp án có ghi trang của đề tương ứng.

**Cách luyện tập**

1. Đọc đề, tự viết lời giải trước.
2. Thử với các ví dụ trong đề, sau đó tự nghĩ thêm test biên (giá trị nhỏ nhất, lớn nhất).
3. Mở phần đáp án để so sánh ý tưởng và độ phức tạp.

**Lưu ý**

- Đáp án là lời giải **tham khảo** do nhóm biên soạn, không phải đáp án chính thức của ban tổ chức.
- Một số đề được chép lại từ ảnh scan hoặc thiếu chi tiết; những chỗ nhóm biên soạn tự bổ sung hoặc diễn giải đều có ghi chú rõ trong khung *Nguồn đề* hoặc *Cách hiểu đề*.
- Đề thi thuộc bản quyền của đơn vị ra đề. Lời giải phát hành theo giấy phép Apache-2.0.
"""


def build_markdown():
    books = collect()
    parts = [FOREWORD]
    n_exams = sum(len(e) for _, e in books)
    for title_part, kind in (("Đề thi", "de"), ("Đáp án", "dap-an")):
        parts.append(f"\n\\part{{{title_part}}}\n")
        for board, exams in books:
            parts.append(f"\n# {board}\n")
            for label, de, da in exams:
                slug = re.sub(r"[^A-Za-z0-9]+", "-", de.rsplit("/", 1)[0])
                path = DOCS / (de if kind == "de" else da) if (kind == "de" or da) else None
                if path is None:
                    continue
                CURRENT_BASE[0] = path.parent
                h1, body = convert(path, 1, drop_answer_tip=True)
                if kind == "de":
                    parts.append(f"\n## {label}\n\n\\label{{de-{slug}}}\n")
                    if h1:
                        parts.append(f"*{h1}*\n")
                else:
                    parts.append(f"\n## Đáp án: {label}\n\n\\label{{da-{slug}}}\n")
                    parts.append(f"\\noindent\\textit{{Đề ở trang \\pageref{{de-{slug}}}.}}\n")
                parts.append(body)
                parts.append("\n\\clearpage\n" if kind == "de" else "\n")
    return "\n".join(parts), books, n_exams


# Font có đủ dấu tiếng Việt; chọn font đầu tiên có trên máy.
FONT_CANDIDATES = {
    "mainfont": ["TeX Gyre Pagella", "Times New Roman", "DejaVu Serif"],
    "sansfont": ["TeX Gyre Heros", "Arial", "DejaVu Sans"],
    "monofont": ["Noto Sans Mono", "Liberation Mono", "Menlo", "Courier New"],
}


def pick_font(kind):
    cands = FONT_CANDIDATES[kind]
    if not shutil.which("fc-list"):
        return cands[0]
    have = subprocess.run(["fc-list", ":", "family"], capture_output=True, text=True).stdout
    names = {n.strip() for line in have.splitlines() for n in line.split(",")}
    return next((c for c in cands if c in names), cands[0])


def main():
    md, books, n = build_markdown()
    OUT.mkdir(exist_ok=True)
    md_file = OUT / f"{NAME}.md"
    md_file.write_text(md, encoding="utf-8")
    boards = " · ".join(b for b, _ in books)
    (OUT / "preamble.tex").write_text(PREAMBLE, encoding="utf-8")
    (OUT / "cover.tex").write_text(
        COVER.replace("__BOARDS__", tex_escape(boards) + f"\\\\[4pt]{n} đề")
        .replace("__DATE__", datetime.date.today().strftime("%m/%Y")),
        encoding="utf-8",
    )
    print(f"{n} đề -> {md_file.relative_to(ROOT)}")
    if "--tex" in sys.argv:
        return
    if not shutil.which("pandoc") or not shutil.which("xelatex"):
        sys.exit("Cần cài pandoc và xelatex.")
    pdf = OUT / f"{NAME}.pdf"
    cmd = [
        "pandoc", str(md_file), "-o", str(pdf),
        "--from", "markdown+tex_math_dollars+raw_tex+pipe_tables+fenced_code_attributes-implicit_figures",
        "--pdf-engine=xelatex", "--toc", "--toc-depth=2", "--top-level-division=chapter",
        "--highlight-style=tango",
        "-H", str(OUT / "preamble.tex"), "-B", str(OUT / "cover.tex"),
        "-V", "documentclass=book", "-V", "classoption=oneside", "-V", "papersize=a4",
        "-V", "geometry:margin=2.2cm", "-V", "fontsize=11pt", "-V", "lang=vi",
        "-V", f"mainfont={pick_font('mainfont')}", "-V", f"sansfont={pick_font('sansfont')}",
        "-V", f"monofont={pick_font('monofont')}", "-V", "monofontoptions=Scale=0.85",
        "-V", "toc-title=Mục lục", "-V", "colorlinks=true", "-V", "linkcolor=black",
        "-V", "urlcolor=blue!50!black",
        "--resource-path", str(DOCS),
    ]
    subprocess.run(cmd, check=True, cwd=OUT)
    print(f"-> {pdf.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
