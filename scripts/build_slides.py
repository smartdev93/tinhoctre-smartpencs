#!/usr/bin/env python3
"""Build site con bài giảng (slide) tại /slides/.

Nguồn:  slides/<bảng>/<slug>/deck.json         tiêu đề, thứ tự slide, font
        slides/<bảng>/<slug>/meta.json         thông tin hiện ở trang danh sách
        slides/<bảng>/<slug>/slides/<id>.html  mỗi file một <section> 1920x1080
Đích:   docs/slides/index.html                 trang danh sách bài giảng
        docs/slides/<bảng>/<slug>/index.html   trình chiếu

MkDocs chép nguyên thư mục docs/slides/ ra site (không qua menu), nên trang
chạy ở https://tinhoctre.smart-pens.com/slides/ như một site riêng.

Chạy:   python3 scripts/build_slides.py
"""
import html
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "slides"
OUT = ROOT / "docs" / "slides"
SITE = "https://tinhoctre.smart-pens.com/"

# Icon dùng trong slide (thẻ <x-icon name="...">), vẽ lại bằng SVG nét đơn.
ICONS = {
    "Code": '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    "Check": '<polyline points="20 6 9 17 4 12"/>',
    "Lightbulb": '<path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7V17h8v-2.3A7 7 0 0 0 12 2z"/>',
    "Warning": '<path d="M12 3 2 21h20L12 3z"/><path d="M12 10v5M12 18h.01"/>',
    "Star": '<polygon points="12 2 15 9 22 9.3 16.5 14 18.5 21 12 17 5.5 21 7.5 14 2 9.3 9 9"/>',
}

# CSS dựng slide (dùng chung cho trình chiếu và ảnh bìa ở trang danh sách).
SLIDE_CSS = """
.stage{position:absolute;width:1920px;height:1080px;transform-origin:0 0;overflow:hidden}
.stage section{position:absolute;inset:0;box-sizing:border-box;overflow:hidden;display:flex}
.stage *{box-sizing:border-box}
.stage h1,.stage h2,.stage h3,.stage p,.stage ul,.stage ol,.stage table{margin:0}
.stage div:not([style*="display:"]){display:flex;flex-direction:column}
.stage table{border-collapse:collapse;width:100%}
.stage th,.stage td{padding:.35em .6em;text-align:left;border-bottom:1px solid rgba(29,43,83,.18)}
.stage th{font-weight:800}
.stage aside{display:none}
.stage x-shape,.stage x-icon{display:block;flex:none}
.stage x-shape[kind=ellipse]{border-radius:50%}
.stage x-shape[kind=arrow-right]{clip-path:polygon(0 30%,60% 30%,60% 0,100% 50%,60% 100%,60% 70%,0 70%)}
.stage x-shape[kind=arrow-left]{clip-path:polygon(100% 30%,40% 30%,40% 0,0 50%,40% 100%,40% 70%,100% 70%)}
.stage x-icon svg{width:100%;height:100%}
"""

ICON_JS = """
var ICONS=__ICONS__;
document.querySelectorAll('.stage x-icon').forEach(function(el){
  el.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+(ICONS[el.getAttribute('name')]||'')+'</svg>';
});
"""

VIEWER = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__ · Bài giảng Tin học trẻ</title>
__FONTS__
<style>
html,body{margin:0;height:100%;background:#0f1630;overflow:hidden;font-family:Nunito,Verdana,sans-serif}
__SLIDE_CSS__
#stage{left:50%;top:50%;box-shadow:0 10px 40px rgba(0,0,0,.4)}
#stage section:not(.on){display:none !important}
#bar{position:fixed;left:50%;bottom:10px;transform:translateX(-50%);display:flex;gap:8px;align-items:center;padding:6px 8px;border-radius:10px;background:rgba(15,22,48,.85);color:#c9d3ea;font-size:14px;opacity:.15;transition:opacity .2s}
#bar:hover{opacity:1}
#bar button,#bar a{background:#2a3a6b;color:#fff8ec;border:0;border-radius:6px;padding:6px 12px;font:inherit;cursor:pointer;text-decoration:none}
#notes{position:fixed;left:16px;right:16px;bottom:48px;max-height:30vh;overflow:auto;background:#fff8ec;color:#1d2b53;border-radius:10px;padding:14px 18px;font-size:17px;line-height:1.5;display:none}
</style>
</head>
<body>
<div id="stage" class="stage">
__SLIDES__
</div>
<div id="notes"></div>
<div id="bar">
<a href="__BACK__" title="Về danh sách bài giảng">☰ Danh sách</a>
<button id="prev" title="Trang trước (←)">◀</button>
<span id="count"></span>
<button id="next" title="Trang sau (→)">▶</button>
<button id="fs" title="Toàn màn hình (F)">Toàn màn hình</button>
<button id="nt" title="Ghi chú giáo viên (N)">Ghi chú</button>
</div>
<script>
(function(){
__ICON_JS__
var stage=document.getElementById('stage'),slides=[].slice.call(stage.children),i=0;
var notes=document.getElementById('notes'),count=document.getElementById('count');
function fit(){var s=Math.min(innerWidth/1920,innerHeight/1080);stage.style.transform='scale('+s+') translate(-50%,-50%)';}
function show(n){
  i=Math.max(0,Math.min(slides.length-1,n));
  slides.forEach(function(s,k){s.classList.toggle('on',k===i);});
  var a=slides[i].querySelector('aside');notes.textContent=a?a.textContent:'(Không có ghi chú)';
  count.textContent=(i+1)+' / '+slides.length;
  history.replaceState(null,'','#'+(i+1));
}
function fs(){var d=document.documentElement;if(!document.fullscreenElement){d.requestFullscreen&&d.requestFullscreen();}else{document.exitFullscreen();}}
function nt(){notes.style.display=notes.style.display==='block'?'none':'block';}
document.getElementById('prev').onclick=function(){show(i-1);};
document.getElementById('next').onclick=function(){show(i+1);};
document.getElementById('fs').onclick=fs;
document.getElementById('nt').onclick=nt;
stage.onclick=function(e){show(e.clientX<innerWidth/3?i-1:i+1);};
addEventListener('keydown',function(e){
  if(['ArrowRight','PageDown',' ','Enter'].indexOf(e.key)>=0){e.preventDefault();show(i+1);}
  else if(['ArrowLeft','PageUp','Backspace'].indexOf(e.key)>=0){e.preventDefault();show(i-1);}
  else if(e.key==='Home')show(0);
  else if(e.key==='End')show(slides.length-1);
  else if(e.key==='f'||e.key==='F')fs();
  else if(e.key==='n'||e.key==='N')nt();
});
addEventListener('resize',fit);fit();
addEventListener('hashchange',function(){var n=(parseInt(location.hash.slice(1),10)||1)-1;if(n!==i)show(n);});
show((parseInt(location.hash.slice(1),10)||1)-1);
})();
</script>
</body>
</html>
"""

INDEX = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bài giảng Tin học trẻ</title>
<meta name="description" content="Slide chữa đề Tin học trẻ để trình chiếu trên lớp.">
__FONTS__
<style>
:root{--bg:#f6f4ef;--card:#ffffff;--ink:#1d2b53;--muted:#5a6478;--line:#e4dfd4;--accent:#3f51b5}
@media (prefers-color-scheme:dark){:root{--bg:#141a2e;--card:#1d2540;--ink:#eef0f7;--muted:#a9b1c7;--line:#2c3657;--accent:#9fa8da}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:Nunito,Verdana,sans-serif;line-height:1.5}
header{max-width:1100px;margin:0 auto;padding:48px 16px 8px}
header a{color:var(--accent);text-decoration:none;font-weight:700}
h1{font-size:40px;line-height:1.15;margin:12px 0 8px}
header p{color:var(--muted);margin:0;font-size:18px}
main{max-width:1100px;margin:0 auto;padding:24px 16px 64px}
h2{font-size:22px;margin:32px 0 16px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:24px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;display:flex;flex-direction:column}
.thumb{position:relative;display:block;aspect-ratio:16/9;overflow:hidden;background:#1d2b53}
.thumb .stage{left:0;top:0;pointer-events:none}
.body{padding:16px 18px 18px;display:flex;flex-direction:column;gap:8px;flex:1}
.body h3{margin:0;font-size:19px;line-height:1.3}
.body h3 a{color:inherit;text-decoration:none}
.body p{margin:0;color:var(--muted);font-size:15px}
.tags{display:flex;flex-wrap:wrap;gap:6px}
.tag{font-size:13px;font-weight:700;padding:2px 10px;border-radius:999px;background:var(--bg);border:1px solid var(--line)}
.links{margin-top:auto;display:flex;gap:14px;font-size:15px;font-weight:700}
.links a{color:var(--accent);text-decoration:none}
footer{max-width:1100px;margin:0 auto;padding:0 16px 48px;color:var(--muted);font-size:14px}
__SLIDE_CSS__
</style>
</head>
<body>
<header>
<a href="../">← Đề thi &amp; đáp án Tin học trẻ</a>
<h1>Bài giảng Tin học trẻ</h1>
<p>Slide chữa đề để trình chiếu trên lớp. Phím ←/→ chuyển slide, F toàn màn hình, N mở ghi chú cho giáo viên.</p>
</header>
<main>
__GROUPS__
</main>
<footer>Đề thi thuộc bản quyền của đơn vị ra đề. Lời giải và bài giảng là tài liệu tham khảo của nhóm biên soạn.</footer>
<script>
(function(){
__ICON_JS__
function fit(){document.querySelectorAll('.thumb').forEach(function(t){t.querySelector('.stage').style.transform='scale('+(t.clientWidth/1920)+')';});}
addEventListener('resize',fit);fit();
})();
</script>
</body>
</html>
"""

BANG_NAMES = {
    "bang-a": "Bảng A - Tiểu học",
    "bang-b": "Bảng B - THCS",
    "bang-c": "Bảng C - THPT",
    "bang-m": "Bảng M - Tư duy thuật toán",
    "bang-d": "Bảng D - Sáng tạo",
}


def fonts_html(faces):
    return "\n".join(
        f'<link rel="stylesheet" href="{html.escape(f["href"])}">'
        for f in faces.values()
        if f.get("href", "").startswith("https://fonts.googleapis.com/")
    )


def load(deck_dir: Path):
    deck = json.loads((deck_dir / "deck.json").read_text(encoding="utf-8"))
    meta_file = deck_dir / "meta.json"
    meta = json.loads(meta_file.read_text(encoding="utf-8")) if meta_file.exists() else {}
    slides = []
    for sid in deck["order"]:
        f = deck_dir / "slides" / f"{sid}.html"
        if not f.exists():
            sys.exit(f"Thiếu slide: {f}")
        slides.append(f.read_text(encoding="utf-8").strip())
    return deck, meta, slides


def build_viewer(deck_dir: Path, deck, slides) -> Path:
    rel = deck_dir.relative_to(SRC)
    depth = len(rel.parts)
    page = (
        VIEWER.replace("__SLIDE_CSS__", SLIDE_CSS)
        .replace("__ICON_JS__", ICON_JS)
        .replace("__ICONS__", json.dumps(ICONS))
        .replace("__TITLE__", html.escape(deck["title"]))
        .replace("__FONTS__", fonts_html(deck.get("faces", {})))
        .replace("__BACK__", "../" * depth)
        .replace("__SLIDES__", "\n".join(slides))
    )
    out = OUT / rel / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return out


def card(deck_dir: Path, deck, meta, slides) -> str:
    rel = deck_dir.relative_to(SRC).as_posix()
    title = html.escape(meta.get("title", deck["title"]))
    tags = [f"{len(slides)} slide"] + meta.get("tags", [])
    links = [f'<a href="{rel}/">Trình chiếu</a>']
    if meta.get("de"):
        links.append(f'<a href="../{html.escape(meta["de"])}">Đề bài</a>')
    if meta.get("dap_an"):
        links.append(f'<a href="../{html.escape(meta["dap_an"])}">Đáp án</a>')
    return f"""<article class="card">
<a class="thumb" href="{rel}/" aria-label="{title}"><div class="stage">{slides[0]}</div></a>
<div class="body">
<h3><a href="{rel}/">{title}</a></h3>
<p>{html.escape(meta.get("description", ""))}</p>
<div class="tags">{"".join(f'<span class="tag">{html.escape(t)}</span>' for t in tags)}</div>
<div class="links">{"".join(links)}</div>
</div>
</article>"""


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    groups, faces = {}, {}
    for deck_dir in sorted(p.parent for p in SRC.glob("*/*/deck.json")):
        deck, meta, slides = load(deck_dir)
        faces.update(deck.get("faces", {}))
        out = build_viewer(deck_dir, deck, slides)
        groups.setdefault(deck_dir.parent.name, []).append(
            (meta.get("date", ""), card(deck_dir, deck, meta, slides))
        )
        print(f"{deck_dir.relative_to(ROOT)} -> {out.relative_to(ROOT)}")
    parts = []
    for bang in sorted(groups, key=lambda b: list(BANG_NAMES).index(b) if b in BANG_NAMES else 99):
        cards = [c for _, c in sorted(groups[bang], key=lambda x: x[0], reverse=True)]
        parts.append(f'<h2>{html.escape(BANG_NAMES.get(bang, bang))}</h2>\n<div class="grid">\n' + "\n".join(cards) + "\n</div>")
    index = (
        INDEX.replace("__SLIDE_CSS__", SLIDE_CSS)
        .replace("__ICON_JS__", ICON_JS)
        .replace("__ICONS__", json.dumps(ICONS))
        .replace("__FONTS__", fonts_html(faces))
        .replace("__GROUPS__", "\n".join(parts) or "<p>Chưa có bài giảng.</p>")
    )
    (OUT / "index.html").write_text(index, encoding="utf-8")
    print(f"-> {(OUT / 'index.html').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
