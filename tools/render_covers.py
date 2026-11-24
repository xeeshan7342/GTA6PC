"""Draws the original cover graphic for every post that has a "cover" dict.

Usage: python3 tools/render_covers.py   (needs Node + Playwright)
Writes assets/blog/<slug>.jpg at 1280x720.
"""
import html, json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
sys.path.insert(0, HERE)
from posts2 import POSTS2, NEW
from posts3 import NEW2

CSS = open(os.path.join(HERE, "cover-base.css")).read()
TPL = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@125,800;125,900&display=block" rel="stylesheet">
<style>{css}
.wrap{{display:grid;grid-template-columns:1fr 500px;gap:44px;align-items:center;height:100%}}
h1{{font-size:{size}px;margin:16px 0 22px}}
.sub{{font-size:22px;color:#b2a8cf;line-height:1.45}}
.card{{background:#1b1533;border:1.5px solid #2f2752;border-radius:16px;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,.35)}}
.row{{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:20px 24px;border-top:1px solid #2f2752}}
.row:first-child{{border-top:0}}
.row .l{{font-size:19px;color:#d9d0ec}}
.row .v{{font-family:"JetBrains Mono",monospace;font-size:19px;font-weight:600;white-space:nowrap}}
.row.hot .v{{color:#ff8a4c}}
</style></head><body><div class="wrap"><div>
<div class="eb">{eyebrow}</div><h1>{title}</h1><div class="sub">{sub}</div>
</div><div class="card">{rows}</div></div>
<div class="mark">GTA6<b> PC</b> · gta6pc.buzz</div></body></html>"""

jobs = []
tmp = tempfile.mkdtemp()
import importlib
if len(sys.argv) == 3:  # e.g. render_covers.py posts_daily_20261124_b2 POSTS_DAILY_20261124_B2
    _todo = getattr(importlib.import_module(sys.argv[1]), sys.argv[2])
else:
    _todo = NEW2 + NEW + POSTS2
for p in _todo:
    c = p.get("cover")
    if not c: continue
    rows = "".join(f'<div class="row{" hot" if hot else ""}"><span class="l">{html.escape(l)}</span><span class="v">{html.escape(v)}</span></div>' for l, v, hot in c["rows"])
    size = 58 if len(c["title"]) <= 26 else 50
    page = TPL.format(css=CSS, size=size, eyebrow=html.escape(c["eyebrow"]), title=html.escape(c["title"]), sub=html.escape(c["sub"]), rows=rows)
    f = os.path.join(tmp, p["slug"] + ".html"); open(f, "w").write(page)
    jobs.append([f, os.path.abspath(os.path.join(ROOT, "assets/blog", p["slug"] + ".jpg"))])

js = """const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:720}});
for (const [f,o] of %s){await p.goto('file://'+f);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:o,type:'jpeg',quality:88});}
await b.close();})();""" % json.dumps(jobs)
jf = os.path.join(tmp, "r.js"); open(jf, "w").write(js)
subprocess.run(["node", jf], check=True)
print("rendered", len(jobs), "covers")
