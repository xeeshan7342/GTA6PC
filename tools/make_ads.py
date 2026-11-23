"""Renders Google Display banner ads for gta6pc.buzz.

Usage: python3 tools/make_ads.py   (needs Node + Playwright + Pillow)
Writes marketing/display-ads/<variant>/<w>x<h>.jpg, each under 150 KB.
"""
import json, os, subprocess, tempfile
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "marketing", "display-ads")

VARIANTS = {
    "a-coming-to-pc": dict(head="Is GTA 6 coming to PC?", sub="Release date status, leaks & PC news", cta="Get the facts", tiny="GTA 6 on PC: get the facts"),
    "b-play-today": dict(head="Play GTA 6 on PC today", sub="Legal Remote Play guide for PS5 & Xbox owners", cta="Read the guide", tiny="Play GTA 6 on PC today"),
    "c-xbox-leak": dict(head="GTA 6 Xbox build leaked", sub="What's real, and why it doesn't run on PC", cta="Read the facts", tiny="GTA 6 Xbox leak: what's real"),
}
# (w, h, layout) — v = stacked, h = horizontal, t = tiny one-liner
SIZES = [(300, 250, "v"), (336, 280, "v"), (300, 600, "v"), (160, 600, "v"), (1200, 1200, "v"),
         (728, 90, "h"), (970, 250, "h"), (468, 60, "t"), (320, 50, "t"), (320, 100, "h"), (1200, 628, "h"), (1200, 300, "h")]

SUN = '''<svg viewBox="0 0 64 64" class="sun"><defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="0" y1="12" x2="0" y2="56"><stop offset="0" stop-color="#ffc24d"/><stop offset=".55" stop-color="#ff8a4c"/><stop offset="1" stop-color="#ff4fa3"/></linearGradient><clipPath id="c"><circle cx="32" cy="34" r="22"/></clipPath></defs><g clip-path="url(#c)" fill="url(#g)"><rect x="8" y="10" width="48" height="25"/><rect x="8" y="38" width="48" height="4"/><rect x="8" y="45" width="48" height="3.5"/><rect x="8" y="51.5" width="48" height="3"/></g></svg>'''

TYPE = {
    (300, 250): (25, 12, 13, 12, 8), (336, 280): (28, 13, 14, 13, 8.5), (300, 600): (34, 15, 16, 14, 9),
    (160, 600): (21, 11, 11, 11, 7), (1200, 1200): (104, 40, 44, 40, 24),
    (728, 90): (25, 11.5, 13, 9, 7), (970, 250): (52, 20, 22, 16, 11), (320, 100): (15, 0, 10.5, 8, 6.5),
    (1200, 628): (74, 26, 28, 22, 13), (1200, 300): (54, 21, 22, 16, 11),
}

def page(w, h, lay, v):
    u = min(w, h)
    hs, ss, cs, ls, ds = TYPE.get((w, h), (20, 10, 11, 9, 7))
    if lay == "v":
        sun = min(w * .4, h * .24)
        css = f""".ad{{flex-direction:column;justify-content:space-between;align-items:center;padding:{h*.05}px {w*.06}px {h*.04}px}}
.logo{{font-size:{ls}px;align-self:flex-start}} .sun{{width:{sun}px;height:{sun}px}}
h1{{font-size:{hs}px;text-align:center}} p{{font-size:{ss}px;text-align:center}}
.cta{{font-size:{cs}px;padding:{cs*.6}px {cs*1.3}px}} .disc{{font-size:{ds}px}} .mid{{display:flex;flex-direction:column;align-items:center;gap:{h*.025}px}}"""
        body = f'<div class="logo">GTA6<b>PC</b></div><div class="mid">{SUN}<h1>{v["head"]}</h1><p>{v["sub"]}</p></div><div class="bot"><span class="cta">{v["cta"]} →</span><div class="disc">Unofficial fan site · gta6pc.buzz</div></div>'
    elif lay == "h":
        sun = min(h * .66, w * .2); gap = min(h * .14, w * .025); pad = min(h * .16, w * .045)
        css = f""".ad{{flex-direction:row;align-items:center;gap:{gap}px;padding:0 {pad}px}}
.sun{{width:{sun}px;height:{sun}px;flex:none}} .txt{{flex:1;min-width:0}}
h1{{font-size:{hs}px}} p{{font-size:{ss}px;margin-top:{ss*.35}px}} .logo{{font-size:{ls}px;margin-bottom:{ls*.3}px}}
.cta{{font-size:{cs}px;padding:{cs*.6}px {cs*1.1}px;flex:none}}
.disc{{position:absolute;right:{h*.1}px;bottom:{h*.05}px;font-size:{ds}px}}"""
        if not ss:
            css += " p{display:none}"
        body = f'{SUN}<div class="txt"><div class="logo">GTA6<b>PC</b></div><h1>{v["head"]}</h1><p>{v["sub"]}</p></div><span class="cta">{v["cta"]} →</span><div class="disc">Unofficial fan site</div>'
    else:
        s = h / 50
        css = f""".ad{{flex-direction:row;align-items:center;gap:{8*s}px;padding:0 {8*s}px}}
.sun{{width:{h*.7}px;height:{h*.7}px;flex:none}} h1{{flex:1;min-width:0;font-size:{min(13*s, w/29)}px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.cta{{font-size:{10*s}px;padding:{6*s}px {9*s}px;flex:none}}"""
        body = f'{SUN}<h1>{v["tiny"]}</h1><span class="cta">{v["cta"].split()[0]} →</span>'
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@125,800;125,900&display=block" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{w}px;height:{h}px;overflow:hidden}}
.ad{{position:relative;width:{w}px;height:{h}px;display:flex;overflow:hidden;color:#f6f0fb;font-family:Inter,sans-serif;
background:radial-gradient(ellipse at 85% 0%,rgba(255,138,76,.22),transparent 60%),linear-gradient(160deg,#2a2148 0%,#151029 60%,#0f0b1e 100%);
border:1px solid #2f2752}}
h1{{font-family:Archivo,sans-serif;font-stretch:125%;font-weight:900;line-height:1.05;letter-spacing:-.3px}}
p{{color:#d0c6e6;line-height:1.3}}
.logo{{font-family:"JetBrains Mono",monospace;font-weight:600}} .logo b{{color:#ff8a4c;font-weight:600;margin-left:.35em}}
.cta{{background:#ff8a4c;color:#1a0b05;font-weight:700;border-radius:999px;white-space:nowrap;display:inline-block}}
.bot{{display:flex;flex-direction:column;align-items:center;gap:6px}}
.disc{{color:#9d92b8;font-family:"JetBrains Mono",monospace}}
{css}</style></head><body><div class="ad">{body}</div></body></html>"""

tmp = tempfile.mkdtemp(); jobs = []
for key, v in VARIANTS.items():
    os.makedirs(os.path.join(OUT, key), exist_ok=True)
    for w, h, lay in SIZES:
        f = os.path.join(tmp, f"{key}-{w}x{h}.html"); open(f, "w").write(page(w, h, lay, v))
        jobs.append([f, os.path.join(tmp, f"{key}-{w}x{h}.png"), w, h, os.path.abspath(os.path.join(OUT, key, f"{w}x{h}.jpg"))])
js = """const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for (const [f,o,w,h] of %s){const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:1});await p.goto('file://'+f);
await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(250);await p.screenshot({path:o});await p.close();}
await b.close();})();""" % json.dumps([j[:4] for j in jobs])
jf = os.path.join(tmp, "r.js"); open(jf, "w").write(js); subprocess.run(["node", jf], check=True)
for f, png, w, h, out in jobs:
    im = Image.open(png).convert("RGB")
    for q in (92, 85, 78, 70, 60):
        im.save(out, quality=q, optimize=True)
        if os.path.getsize(out) < 150_000: break
    print(os.path.relpath(out, OUT), os.path.getsize(out) // 1024, "KB")
