"""Generates the blog, legal pages, sitemap and robots.txt for the GTA6 PC site."""
import json, os, sys, html

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..")
SITE = "https://gta6pc.buzz"   # replace once the domain is bought
NAME = "GTA6 PC"
AUTHOR = "GTA6 PC Editorial"
TODAY = "2026-11-27"
TODAY_H = "November 27, 2026"

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@125,800;125,900&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">'

def nav(depth, current=""):
    up = "/" if depth < 0 else "../" * depth
    def a(href, label, key, cls=""):
        cur = ' aria-current="page"' if key == current else ""
        c = f' class="{cls}"' if cls else ""
        return f'<a href="{up}{href}"{cur}{c}>{label}</a>'
    return f'''<nav><div class="wrap">
  <a href="{up}" class="logo">GTA6<b>PC</b></a>
  <div class="nav-links">{a("", "Home", "home", "hide-sm")}{a("blog/", "Blog", "blog")}{a("about/", "About", "about")}{a("contact/", "Contact", "contact", "hide-sm")}</div>
</div></nav>'''

def footer(depth):
    up = "/" if depth < 0 else "../" * depth
    return f'''<footer><div class="wrap">
  <div class="foot-top">
    <div><a href="{up}" class="logo">GTA6<b>PC</b></a><p>GTA 6 PC news, release info and guides · unofficial fan site</p></div>
    <div class="foot-links"><a href="{up}blog/">Blog</a><a href="{up}blog/topic/">Topics</a><a href="{up}about/">About</a><a href="{up}contact/">Contact</a><a href="{up}privacy-policy/">Privacy</a><a href="{up}terms/">Terms</a><a href="{up}disclaimer/">Disclaimer</a><a href="{up}feed.xml">RSS</a></div>
  </div>
  <p class="legal">{NAME} is an unofficial fan site. It is not affiliated with, endorsed by or sponsored by Rockstar Games or Take-Two Interactive. Grand Theft Auto and related marks are trademarks of Take-Two Interactive Software, Inc. Artwork credited to Rockstar Games is used for news reporting and commentary.</p>
</div></footer>'''

def head(title, desc, path, depth, og_image=None, og_type="website", extra_ld=None, noindex=False):
    up = "/" if depth < 0 else "../" * depth
    url = f"{SITE}/{path}"
    img = og_image or f"{SITE}/assets/og-default.jpg"
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (extra_ld or []))
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{"noindex, follow" if noindex else "index, follow, max-image-preview:large"}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta name="theme-color" content="#0f0b1e">
{FONTS}
<link rel="stylesheet" href="{up}assets/site.css">
<link rel="alternate" type="application/rss+xml" title="GTA6 PC news" href="{SITE}/feed.xml">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7088404924117690" crossorigin="anonymous"></script>
{ld}
</head>
<body>
'''

# ---------------------------------------------------------------- posts
POSTS = [
dict(
slug="gta-6-pc-release-date",
updated="2026-11-26",
short="When on PC?",
title="When Is GTA 6 Coming to PC? Release Date Status (November 2026)",
h1="When is GTA 6 coming to PC?",
desc="GTA 6 is out on PS5 and Xbox Series X|S, but Rockstar hasn't set a PC date. Here's the reported Q1 2027 window, what Rockstar's history suggests, and what to watch for.",
kicker="Release date",
lede="GTA 6 launched on consoles on November 19, 2026. PC players are still waiting, and Rockstar hasn't said for how long. Here's everything that's actually known.",
img_alt="GTA 6 PC release date status graphic showing the reported Q1 2027 window",
tldr="There is <strong>no official GTA 6 PC release date</strong>. Rockstar has only released the game on PS5 and Xbox Series X|S. A GamesBeat report from October 2026 says Rockstar is aiming for <strong>the first quarter of 2027</strong>, but Rockstar hasn't confirmed it.",
faq=[("When is GTA 6 coming to PC?", "There is no official date. Rockstar has only announced GTA 6 for PlayStation 5 and Xbox Series X|S. A GamesBeat report from October 13, 2026 says Rockstar is aiming for the first quarter of 2027, but Rockstar has not confirmed it."), ("What did Take-Two say about a PC version on November 9?", "On the November 9, 2026 earnings call, chief executive Strauss Zelnick was asked about PC and other platforms and said information about new versions always comes from Take-Two's labels, meaning Rockstar. He gave no date and announced nothing."), ("Could the leak bring the PC version forward?", "Some commentators in South Korea have suggested the Xbox build leak could push Rockstar to release the PC version earlier, but that is speculation. Nothing official supports it, and Take-Two's release table through March 2027 lists no PC version."), ("Is the Q1 2027 window reliable?", "It is the most specific window in circulation, from four anonymous industry sources cited by GamesBeat, and the outlet stood by it in a November 18 update. It is still a report, not an announcement, and GTA 6 has already slipped twice."), ("Where will the PC date be announced?", "Rockstar announces release dates on the Rockstar Newswire and its official social accounts. Store pages on Steam, the Epic Games Store and the Rockstar Games Launcher usually appear around the same time.")],
body="""
<h2>What Rockstar has officially said</h2>
<p>Rockstar has only ever announced GTA 6 for PlayStation 5 and Xbox Series X|S. The game went through two delays before it shipped: first from 2025 to May 26, 2026, then to November 19, 2026, when it finally launched on both consoles.</p>
<p>No PC version, PC store page or PC system requirements have been announced. Until Rockstar posts something on its own site, any exact PC date you see online is a guess.</p>

<h2>Confirmed, reported or rumor? The status at a glance</h2>
<p>Most GTA 6 PC headlines mix three very different kinds of claim. Here is how each one stands today.</p>
<div class="table-wrap"><table>
<tr><th>Claim</th><th>Status</th><th>Who says so</th></tr>
<tr><td>GTA 6 is out on PS5 and Xbox Series X|S</td><td><strong>Confirmed</strong></td><td>Rockstar (launched November 19, 2026)</td></tr>
<tr><td>A PC version exists or is planned</td><td><strong>Not confirmed</strong></td><td>Rockstar has never announced one</td></tr>
<tr><td>PC release in Q1 2027 (January to March)</td><td><strong>Reported</strong></td><td>GamesBeat, citing four unnamed industry sources</td></tr>
<tr><td>PC version listed in Take-Two's release plan to March 2027</td><td><strong>No</strong></td><td>Take-Two's fiscal 2027 release table lists no PC version</td></tr>
<tr><td>The leak will speed up the PC release</td><td><strong>Speculation</strong></td><td>Commentary in South Korean media, not a company statement</td></tr>
<tr><td>You can buy, pre-order or download GTA 6 for PC</td><td><strong>False</strong></td><td>No store sells it. Every "download" is fake (see <a href="../gta-6-pc-download-scams/">our scam guide</a>)</td></tr>
</table></div>

<h2>The Q1 2027 report</h2>
<p>On October 13, 2026, GamesBeat reported that Rockstar plans to bring GTA 6 to PC in the first three months of 2027. The outlet cited four industry sources who asked not to be named. Rockstar didn't comment on the report.</p>
<p>That makes Q1 2027 the most specific window in circulation. Treat it as a strong rumor, not a date. Plans like this can move, and GTA 6 has already slipped twice.</p>

<h2>What Rockstar's history suggests</h2>
<p>Rockstar has a long habit of launching on consoles first and bringing the PC version later. Here's how long PC players waited for its last three big releases:</p>
<div class="table-wrap"><table>
<tr><th>Game</th><th>Console launch</th><th>PC launch</th><th>Wait</th></tr>
<tr><td>GTA IV</td><td>April 2008</td><td>December 2008</td><td>~7 months</td></tr>
<tr><td>GTA V</td><td>September 2013</td><td>April 2015</td><td>~19 months</td></tr>
<tr><td>Red Dead Redemption 2</td><td>October 2018</td><td>November 2019</td><td>~13 months</td></tr>
<tr><td>GTA 6</td><td>November 19, 2026</td><td>Not announced</td><td>Q1 2027 would be ~2–4 months</td></tr>
</table></div>
<figure class="hero-img"><img src="../../assets/blog/rockstar-pc-wait-times.jpg" alt="Chart of how long Rockstar PC versions took after console launch: GTA IV about 7 months, GTA V about 19 months, Red Dead Redemption 2 about 13 months" width="1280" height="720" loading="lazy"><figcaption>Graphic: GTA6 PC, based on each game's console and PC release dates</figcaption></figure>
<p>If the Q1 2027 report is right, this would be the shortest console-to-PC gap Rockstar has ever had. If Rockstar sticks to its usual pattern, late 2027 is more likely.</p>

<h2>Where the announcement will come from</h2>
<p>Rockstar announces release dates on the <a href="https://www.rockstargames.com/newswire" rel="noopener">Rockstar Newswire</a> and its official social accounts. Store pages on Steam, the Epic Games Store and the Rockstar Games Launcher usually appear around the same time.</p>

<h2>Be careful with "GTA 6 PC download" sites</h2>
<p>A leaked Xbox build started circulating around the console launch, and sites offering GTA 6 PC downloads, installers or "ports" followed right behind it. There is no legitimate way to play GTA 6 on PC yet. Those downloads are at best unofficial and at worst malware. We cover this in more detail in our <a href="../gta-6-pc-leak/">GTA 6 PC leak explainer</a>.</p>

<h2>What Take-Two said on November 9</h2>
<p>Take-Two reported its fiscal second-quarter results on November 9, 2026, ten days before launch. Pre-orders were "far in excess" of the company's initial expectations, according to chief executive Strauss Zelnick. On the earnings call that evening, Zelnick was asked about a PC version, a Switch 2 version and streaming, and he gave no date. His answer, reported by several outlets, was that information about new versions always comes from Take-Two's labels, meaning Rockstar. Any PC announcement will come from Rockstar itself, not from Take-Two's investor calls.</p>
<p>The Q1 2027 report still stands. GamesBeat updated its October 13 report on November 18, and the window still reads the first quarter of 2027. But there is a point against it too: Take-Two's own fiscal 2027 release table, which runs to March 31, 2027, lists no PC version of GTA 6, and a January to March launch would fall inside that year. The next official checkpoint is Take-Two's third-quarter call, expected around early February 2027.</p>

<h2>Could the leak bring the PC date forward?</h2>
<p>South Korean outlets covering the leak have raised the idea. Chosun Biz reported on November 25 that the leaked Xbox build raises the prospect of an unofficial PC version, and that some expect Rockstar to bring the official PC release forward to the first quarter of next year. Aju Press made the same point the same day, noting that an unofficial version could reach PC-heavy markets long before any official release.</p>
<p>That is speculation, not a report of a decision, and nothing official supports it. Rockstar and Take-Two have said nothing about changing their plans because of the leak. There is an older hint pointing the same way, though. In February 2025, Corsair Gaming chief executive Andrew Paul told investors he expected GTA 6 to arrive in early 2026, when the console game was still targeting autumn 2025. The console launch slipped a year, but Wccftech notes the logic still fits: the industry has expected a fast PC release for a while. VGC's Andy Robinson has also said rising console prices are pressuring Rockstar to get the PC version out earlier than usual. None of that is a date, but it explains why the Q1 2027 window keeps coming up.</p>

<h2>Every GTA 6 PC signal so far, in order</h2>
<p>If you only want to know what has changed and when, this is the full timeline of PC-related news we track. We add to it whenever something new happens.</p>
<div class="table-wrap"><table>
<tr><th>Date</th><th>What happened</th><th>Weight</th></tr>
<tr><td>February 2025</td><td>Corsair CEO Andrew Paul tells investors he expects GTA 6 on PC in early 2026, when consoles were still targeting autumn 2025</td><td>Industry hint</td></tr>
<tr><td>October 13, 2026</td><td>GamesBeat reports Rockstar is aiming for a PC release in Q1 2027, citing four industry sources</td><td>Strongest report</td></tr>
<tr><td>November 9, 2026</td><td>Take-Two earnings call: Strauss Zelnick says new versions are announced by Rockstar, gives no PC date</td><td>Official, no news</td></tr>
<tr><td>November 18, 2026</td><td>GamesBeat updates its report and keeps the Q1 2027 window</td><td>Report repeated</td></tr>
<tr><td>November 19, 2026</td><td>GTA 6 launches on PS5 and Xbox Series X|S. No PC announcement</td><td>Official</td></tr>
<tr><td>November 25, 2026</td><td>Chosun Biz and Aju Press suggest the leaked Xbox build could push Rockstar to release on PC sooner</td><td>Speculation</td></tr>
<tr><td>Early February 2027 (expected)</td><td>Take-Two's next earnings call, the next official checkpoint</td><td>Watch this</td></tr>
</table></div>

<h2>What PC players can do while they wait</h2>
<p>Waiting for an official PC version doesn't mean you can't plan. Here is what actually works right now:</p>
<ul>
<li><strong>Play on your PC screen today.</strong> If you or a friend own a PS5, <a href="../play-gta-6-on-pc-remote-play/">PS Remote Play</a> streams the console version to your PC. Our <a href="../gta-6-remote-play-lag-fix/">lag fix guide</a> covers the common problems.</li>
<li><strong>Check your hardware early.</strong> Rockstar hasn't published PC requirements, but our <a href="../gta-6-pc-system-requirements/">expected system requirements</a> and <a href="../best-pc-build-for-gta-6/">PC build guide</a> show where the bar is likely to sit.</li>
<li><strong>Know where it will be sold.</strong> See what is known about <a href="../gta-6-pc-steam/">Steam</a>, <a href="../gta-6-pc-pre-order/">pre-orders</a> and <a href="../gta-6-pc-price/">the likely PC price</a>.</li>
<li><strong>Think about your progress.</strong> If you start on console now, read our <a href="../gta-6-save-transfer-ps5-xbox-pc/">save transfer explainer</a> first.</li>
</ul>

<h2>Quick answers</h2>
<h3>Is GTA 6 on Steam?</h3>
<p>Not yet. Rockstar hasn't announced any PC store listing.</p>
<h3>Can I pre-order GTA 6 for PC?</h3>
<p>No. There's no official PC pre-order. Any site taking PC pre-orders right now isn't selling a real product.</p>
<h3>Will my console save carry over to PC?</h3>
<p>Rockstar hasn't said. When GTA V moved to PC, players could transfer their GTA Online progress, but nothing is confirmed for GTA 6.</p>
<h3>When is GTA 6 coming to PC?</h3>
<p>There is no official date. Rockstar has only announced GTA 6 for PlayStation 5 and Xbox Series X|S. A GamesBeat report from October 13, 2026 says Rockstar is aiming for the first quarter of 2027, but Rockstar has not confirmed it.</p>
<h3>What did Take-Two say about a PC version on November 9?</h3>
<p>On the November 9, 2026 earnings call, chief executive Strauss Zelnick was asked about PC and other platforms and said information about new versions always comes from Take-Two's labels, meaning Rockstar. He gave no date and announced nothing.</p>
<h3>Could the leak bring the PC version forward?</h3>
<p>Some commentators in South Korea have suggested the Xbox build leak could push Rockstar to release the PC version earlier, but that is speculation. Nothing official supports it, and Take-Two's release table through March 2027 lists no PC version.</p>
<h3>Is the Q1 2027 window reliable?</h3>
<p>It is the most specific window in circulation, from four anonymous industry sources cited by GamesBeat, and the outlet stood by it in a November 18 update. It is still a report, not an announcement, and GTA 6 has already slipped twice.</p>
<h3>Where will the PC date be announced?</h3>
<p>Rockstar announces release dates on the Rockstar Newswire and its official social accounts. Store pages on Steam, the Epic Games Store and the Rockstar Games Launcher usually appear around the same time.</p>
""",
sources=[
("GamesBeat: Grand Theft Auto VI's PC release is slated for Q1 2027", "https://gamesbeat.com/grand-theft-auto-vis-pc-release-is-slated-for-q1-2027/"),
("VGC: GTA 6 PC release date guide", "https://www.videogameschronicle.com/guide/gta-6-pc-version/"),
("PCWorld: We guessed late 2027 for GTA 6 on PC, a report says Q1 2027", "https://www.pcworld.com/article/3260660/we-guessed-late-2027-for-gta-6-on-pc-a-report-says-q1-2027.html"),
("Yahoo Tech: GTA 6 PC release date", "https://tech.yahoo.com/gaming/articles/gta-6-pc-release-date-150338948.html"),
("VGC: The PC version of GTA 6 is reportedly coming before the end of March 2027", "https://www.videogameschronicle.com/news/the-pc-version-of-grand-theft-auto-6-is-reportedly-coming-before-the-end-of-march-2027/"),
("Chosun Biz: GTA 6 leak raises prospect of unofficial PC port and earlier official release", "https://biz.chosun.com/en/en-it/2026/11/25/CUNAZ7EHNRDODCVOZ4JV5MBC6M/"),
("Aju Press: Hacker leak opens door to unofficial GTA 6 PC port", "https://www.ajupress.com/view/20261125092504279"),
("Wccftech: Corsair CEO's early GTA 6 PC release hint looks prescient", "https://wccftech.com/corsair-ceo-gta-6-pc-release-hint-gamesbeat-q1-2027/amp/"),
("Hone: GTA 6 PC release date, November 9 earnings call", "https://hone.gg/blog/gta-6-pc-release-date"),
("Sixshore: Take-Two says GTA 6 pre-orders are far above its expectations", "https://sixshore.com/news/take-two-q2-fy27-gta6-preorders/"),
],
),
dict(
slug="gta-6-pc-launch",
short="PC launch",
title="GTA 6 PC Launch: What to Expect When It Arrives",
h1="GTA 6 PC launch: what to expect",
desc="What the GTA 6 PC launch will probably look like: which stores, which PC features, what hardware you'll need, and which claims to ignore until Rockstar confirms them.",
kicker="PC launch",
lede="Rockstar hasn't announced the PC version yet, but its last two PC launches give a decent idea of how this one will go. Here's what to expect, and what's still unknown.",
img_alt="GTA 6 PC launch graphic showing likely stores and PC features",
tldr="GTA 6 has <strong>no announced PC launch</strong> yet. Based on GTA V and Red Dead Redemption 2, expect it on the <strong>Rockstar Games Launcher, Steam and Epic</strong>, with PC extras like unlocked frame rates and ultrawide support. Official system requirements haven't been published.",
body="""
<h2>Where it will probably launch</h2>
<p>Rockstar's recent PC releases have shipped on its own Rockstar Games Launcher, with Steam and the Epic Games Store alongside it. Red Dead Redemption 2 launched on the Rockstar Games Launcher and Epic in November 2019, and arrived on Steam about a month later. It's reasonable to expect GTA 6 to follow a similar path, though Rockstar hasn't said so.</p>

<h2>PC features players can expect</h2>
<p>Rockstar's PC versions have usually been more than straight copies of the console game. GTA V and RDR2 on PC both added:</p>
<ul>
<li>Unlocked frame rates and support for high refresh rate monitors</li>
<li>Ultrawide and multi-monitor support</li>
<li>A much longer list of graphics settings</li>
<li>Full mouse and keyboard controls</li>
<li>Higher-resolution textures and longer draw distances</li>
</ul>
<p>None of this is confirmed for GTA 6 yet, but it's the pattern.</p>

<h2>What about mods and roleplay?</h2>
<p>PC is where GTA modding and roleplay servers live. In 2023, Rockstar bought Cfx.re, the team behind the FiveM and RedM roleplay platforms. That's a strong sign Rockstar wants community servers to be part of GTA's future on PC, but it hasn't said anything specific about GTA 6.</p>

<h2>System requirements</h2>
<p>Rockstar hasn't published PC system requirements for GTA 6. Lists claiming to show the official minimum or recommended specs are made up, so don't buy hardware based on them.</p>
<p>What's safe to say: GTA 6 is a current-gen-only game, so expect a modern 6- or 8-core CPU, a recent graphics card, 16 GB of RAM or more, and an SSD. Storage will be large. The leaked Xbox build was reported at around 209 GB, so plan for well over 200 GB of free space.</p>

<h2>Price and editions</h2>
<p>PC pricing and editions haven't been announced. Console editions are already on sale, and PC versions of Rockstar games have usually launched at a similar price to consoles.</p>

<h2>GTA 6 Online on PC</h2>
<p>Rockstar hasn't set a date for GTA 6's online mode on any platform yet, so there's no PC date for it either.</p>

<h2>How to get the news first</h2>
<p>Keep an eye on the <a href="https://www.rockstargames.com/newswire" rel="noopener">Rockstar Newswire</a>. We'll update our <a href="../gta-6-pc-release-date/">GTA 6 PC release date</a> page as soon as anything official is announced.</p>
""",
sources=[
("GamesBeat: Grand Theft Auto VI's PC release is slated for Q1 2027", "https://gamesbeat.com/grand-theft-auto-vis-pc-release-is-slated-for-q1-2027/"),
("VGC: GTA 6 PC release date guide", "https://www.videogameschronicle.com/guide/gta-6-pc-version/"),
("Rockstar Newswire", "https://www.rockstargames.com/newswire"),
("PC Guide: GTA 6 could be playable on PC by next week, say modders", "https://www.pcguide.com/news/gta-6-could-be-playable-on-pc-by-next-week-say-modders/"),
],
),
dict(
slug="gta-6-pc-leak",
short="PC leaks",
title="GTA 6 PC Leak Explained: The Cyberleek Xbox Build and What's Real",
h1="GTA 6 PC leak explained: what's real and what isn't",
desc="A hacker group says it leaked a near-complete GTA 6 Xbox build. Here's what was released, whether it can run on PC, the fake videos going around, and the malware risk.",
kicker="Leaks",
lede="Around the console launch, a group called Cyberleek said it had put a near-complete Xbox build of GTA 6 online. Since then the internet has been full of \"GTA 6 on PC\" claims. Here's what's actually going on.",
img_alt="Graphic of the leaked GTA 6 Xbox build with encrypted files and a missing executable",
tldr="Cyberleek says it released a <strong>~209 GB Xbox build</strong> of GTA 6, labeled version 1.0.2.1, but held back the main executable. The files haven't been fully verified, <strong>no one has shown it running on PC</strong>, and a viral \"PC port\" video turned out to be GTA V footage.",
body="""
<h2>What happened</h2>
<p>Around November 19, 2026, the hacker group Cyberleek said it had published what it called a near-complete GTA 6 Xbox build, about 209 GB in size. Reports say the build is labeled as Xbox version 1.0.2.1.</p>
<p>The group held back one key file: the game's main executable. It tied releasing that file to the market value of its own crypto token, and later said it would release it on November 23 regardless. As of this writing, there's no confirmed report that a working executable is out.</p>

<h2>Is the leak real?</h2>
<p>Partly checked, not confirmed. Some people in the hacking community have looked through the files and say they appear genuine. Nobody has fully verified the build, and Rockstar hasn't commented on it.</p>

<h2>Does this mean GTA 6 is on PC?</h2>
<p>No. A console build isn't a PC game. Cyberleek claimed modders could get it running on PC within a week, but there are big obstacles:</p>
<ul>
<li>The game's files are reported to be encrypted, with the key tied to the withheld executable.</li>
<li>The build relies on Xbox-specific system functions that Windows doesn't have.</li>
<li>No working Xbox Series X|S emulator exists, and community projects are at a very early stage. GTA 6 doesn't boot in any of them.</li>
</ul>
<p>We go deeper on this in <a href="../gta-6-xbox-build-on-pc/">Can the leaked Xbox build run on PC?</a></p>

<h2>The fake "GTA 6 PC port" video</h2>
<p>One widely shared clip claimed to show GTA 6 running on PC. XDA Developers found it was a hoax put together from recycled GTA V footage. Expect more fakes like this while people are searching for GTA 6 on PC.</p>

<h2>The real risk: malware and scams</h2>
<div class="warn"><strong>Don't download "GTA 6 PC" files, installers or "ports."</strong> Fake installers and phishing pages are circulating alongside the leak. Leaked game files are also a common way to spread malware, and downloading or sharing them can carry legal risk.</div>
<p>We don't link to leaked files, and we won't.</p>

<h2>GTA 6 has leaked before</h2>
<p>This isn't the first big GTA 6 leak. In September 2022, more than 90 early development videos were posted online. Rockstar confirmed that leak and said it was "extremely disappointed." The person responsible was later dealt with by the UK courts. Cyberleek also claimed earlier GTA 6 leaks before this one.</p>

<h2>What PC players should do</h2>
<p>Wait for Rockstar's official PC version. A GamesBeat report says it's targeting early 2027. See our <a href="../gta-6-pc-release-date/">GTA 6 PC release date</a> page for the latest.</p>
""",
sources=[
("PC Gamer: Cyberleek drops what they claim is a near-complete GTA 6 Xbox build online", "https://www.pcgamer.com/games/grand-theft-auto/cyberleek-drops-what-they-claim-is-a-near-complete-gta-6-xbox-build-online/"),
("VGC: Cyberleek claims to release development build of GTA 6", "https://www.videogameschronicle.com/news/cyberleek-claims-to-release-development-build-of-gta-6/"),
("XDA: GTA 6's notorious leaker claims to have released a dumped Xbox build", "https://www.xda-developers.com/gta-6s-notorious-leaker-claims-to-have-released-dumped-xbox-build-on-internet/"),
("XDA: That viral unofficial GTA 6 PC port video is a hoax", "https://www.xda-developers.com/that-viral-gta-6-pc-port-video-hoax-made-from-recycled-gta-5-footage/"),
("GamesRadar: GTA 6 PC port could come from hackers before Rockstar", "https://www.gamesradar.com/games/grand-theft-auto/gta-6-pc-port-could-come-from-hackers-before-rockstar-if-cyberleek-makes-good-on-its-latest-threat-this-community-will-have-it-emulated-inside-a-week/"),
("PC Guide: GTA 6 could be playable on PC by next week, say modders", "https://www.pcguide.com/news/gta-6-could-be-playable-on-pc-by-next-week-say-modders/"),
],
),
dict(
slug="gta-6-built-for-pc",
short="Built for PC",
title="Is GTA 6 Built for PC? Native Port vs Emulation vs Recompilation",
h1="Is GTA 6 built for PC? Native, emulated and recompiled explained",
desc="\"Native PC build\", \"emulated\" and \"recompiled\" mean very different things. Here's what each one means for GTA 6, and which kind of PC version is actually real.",
kicker="Explainer",
lede="You'll see a lot of phrases thrown around about GTA 6 on PC: native, built for PC, emulated, recompiled, port. They aren't the same thing. Here's a plain-English breakdown.",
img_alt="Diagram comparing native PC builds, emulation and static recompilation",
tldr="The only real <strong>\"built for PC\"</strong> version of GTA 6 will be Rockstar's official one, which hasn't been announced. <strong>Emulation</strong> and <strong>static recompilation</strong> are fan techniques. They have worked for older consoles, but nobody has made them work for GTA 6.",
body="""
<h2>1. Native PC build (the official version)</h2>
<p>A native PC build is made by the developer from the game's original source code and compiled to run on Windows. It talks directly to your graphics card and CPU, ships with PC graphics settings, and gets official patches and support.</p>
<p>This is what Rockstar did for GTA V and Red Dead Redemption 2, and it's what GTA 6 will get when Rockstar releases it. A report says that's planned for early 2027, but it isn't announced.</p>

<h2>2. Emulation</h2>
<p>An emulator pretends to be a console. It takes the console version of a game and translates its instructions while the game is running. This works well for older consoles, but it costs a lot of performance, and it only works once someone has built an emulator for that console.</p>
<p>There's no working emulator for Xbox Series X|S or PS5 today. That's the main reason emulating GTA 6 isn't possible right now.</p>

<h2>3. Static recompilation ("recomp")</h2>
<p>Static recompilation takes a console game's compiled code and translates it ahead of time into a new program that runs on PC. Fan projects have used this successfully on older games: N64Recomp for Nintendo 64 titles, and XenonRecomp for some Xbox 360 games.</p>
<p>Modern consoles are much harder. Games are encrypted, depend on console-only system services, and are enormous. A GTA 6 recomp would need a complete, decrypted build plus a huge amount of work. Nobody has publicly shown one working.</p>

<h2>4. Relinking: the AnyPS5 approach</h2>
<p>A newer open-source project called AnyPS5 takes another route for PS5 games. Because the PS5 uses the same type of processor as a PC, it relinks a game's PS5 program into a PC program, then reimplements the console's system libraries and recompiles its graphics shaders. Some smaller PS5 games already reach gameplay this way. GTA 6 isn't one of them, because it hasn't been dumped from a PS5. Full story: <a href="../anyps5-gta-6-pc/">AnyPS5 and GTA 6</a>.</p>

<h2>Why the Xbox version gets so much attention</h2>
<p>Modern Xbox games are built with Microsoft's Game Development Kit (GDK), which shares a lot with Windows. Both use x86-64 processors and DirectX 12. That's why people think an Xbox build is easier to bring to PC than a PS5 one. It's still far from simple. See <a href="../gta-6-xbox-build-on-pc/">Can the leaked Xbox build run on PC?</a></p>

<h2>Quick comparison</h2>
<div class="table-wrap"><table>
<tr><th></th><th>Native PC</th><th>Emulation</th><th>Recompilation / relinking</th></tr>
<tr><td>Who makes it</td><td>Rockstar</td><td>Fans</td><td>Fans</td></tr>
<tr><td>Needs game files</td><td>No, you buy it</td><td>Yes, from a console</td><td>Yes, from a console</td></tr>
<tr><td>Performance</td><td>Best</td><td>Heavy overhead</td><td>Can be good</td></tr>
<tr><td>Exists for GTA 6</td><td>Not yet (reported Q1 2027)</td><td>No</td><td>No (AnyPS5 exists, GTA 6 not dumped)</td></tr>
</table></div>

<h2>How to spot a fake "native GTA 6 PC" claim</h2>
<ul>
<li>It's not on Rockstar's site, Steam, Epic or the Rockstar Games Launcher.</li>
<li>It asks you to download files from a forum, a Discord server or a file host.</li>
<li>It says you don't need to own the game.</li>
<li>Its "proof" is a short video with no source.</li>
</ul>
<p>If any of those apply, skip it.</p>
""",
sources=[
("TweakTown: Cyberleek claims modders could get GTA 6 running on PC within a week", "https://www.tweaktown.com/news/114815/cyberleek-claims-modders-could-get-gta-6-running-on-pc-within-a-week-after-reported-xbox-build-leak/index.html"),
("XDA: GTA 6's notorious leaker claims to have released a dumped Xbox build", "https://www.xda-developers.com/gta-6s-notorious-leaker-claims-to-have-released-dumped-xbox-build-on-internet/"),
("Windows Forum: GTA 6 Xbox leak sparks Windows emulation efforts", "https://windowsforum.com/news/gta-6-xbox-leak-sparks-windows-emulation-efforts-scarlettx-leonida-and-malware-risks.453563/"),
("GamesBeat: Grand Theft Auto VI's PC release is slated for Q1 2027", "https://gamesbeat.com/grand-theft-auto-vis-pc-release-is-slated-for-q1-2027/"),
],
),
dict(
slug="gta-6-xbox-build-on-pc",
short="Xbox build on PC",
title="Can the Leaked GTA 6 Xbox Build Run on PC? (November 2026)",
h1="Can the leaked GTA 6 Xbox build run on PC?",
desc="A leaked GTA 6 Xbox build has people asking whether it can run on Windows. Here's why it can't yet, what stands in the way, and why fake download sites are the real danger.",
kicker="Xbox build",
lede="The leaked GTA 6 Xbox build has sparked a wave of \"play GTA 6 on PC today\" posts. Here's an honest look at whether that's possible.",
img_alt="Graphic listing why the leaked GTA 6 Xbox build cannot run on PC yet",
tldr="<strong>Not right now.</strong> The leaked Xbox build is reportedly missing its main executable, its files are encrypted, and no Xbox Series X|S emulator exists. Community projects are early, and GTA 6 doesn't boot in any of them.",
body="""
<h2>Why people think it might work</h2>
<p>Xbox Series X|S games are built with Microsoft's GDK, which shares much of its design with Windows. The hardware is also PC-like, with an x86-64 AMD processor and DirectX 12 graphics. On paper, that's a much shorter jump than bringing a PS5 game to PC.</p>

<h2>What's actually in the way</h2>
<h3>The missing executable</h3>
<p>The leak reportedly doesn't include the main program file. Without it there's nothing to run, and the leakers tied its release to their crypto token's price.</p>
<h3>Encryption</h3>
<p>The game's assets are reported to be encrypted, with the key taken from that executable. Even with every other file, you can't load the world without it.</p>
<h3>Xbox-only system calls</h3>
<p>Console games call into system services that only exist on the console: storage, user accounts, online features and more. A PC version needs every one of those rebuilt or faked.</p>
<h3>No emulator</h3>
<p>There's no working Xbox Series X|S emulator. A few community projects have started since the leak, but they're at a very early stage and GTA 6 doesn't boot in them.</p>

<h2>What about the "it'll be playable in a week" claim?</h2>
<p>That came from the leakers themselves, who have an obvious reason to build hype. Several outlets have pointed out that the timeline doesn't hold up without an emulator. So far, nobody has publicly shown the build running on a PC.</p>

<h2>Sites offering a GTA 6 PC "recomp" or download</h2>
<div class="warn"><strong>Be very careful.</strong> Since the leak, sites and Discord servers have popped up promising GTA 6 on PC through "recomps", "ports" or ready-made downloads. Fake installers and phishing pages are already circulating. Running unknown files to "get GTA 6 on PC" is one of the easiest ways to get your PC or accounts compromised.</div>
<p>Using leaked builds can also carry legal risk, and Rockstar has a long history of acting against leaks.</p>

<h2>The bottom line</h2>
<p>For now, the only way to play GTA 6 is on PS5 or Xbox Series X|S. The official PC version is reported to be targeting the first quarter of 2027. Check our <a href="../gta-6-pc-release-date/">release date page</a> for updates.</p>
""",
sources=[
("PC Gamer: Cyberleek drops what they claim is a near-complete GTA 6 Xbox build online", "https://www.pcgamer.com/games/grand-theft-auto/cyberleek-drops-what-they-claim-is-a-near-complete-gta-6-xbox-build-online/"),
("TweakTown: Cyberleek claims modders could get GTA 6 running on PC within a week", "https://www.tweaktown.com/news/114815/cyberleek-claims-modders-could-get-gta-6-running-on-pc-within-a-week-after-reported-xbox-build-leak/index.html"),
("XDA: GTA 6's notorious leaker claims to have released a dumped Xbox build", "https://www.xda-developers.com/gta-6s-notorious-leaker-claims-to-have-released-dumped-xbox-build-on-internet/"),
("Windows Forum: GTA 6 Xbox leak sparks Windows emulation efforts and malware risks", "https://windowsforum.com/news/gta-6-xbox-leak-sparks-windows-emulation-efforts-scarlettx-leonida-and-malware-risks.453563/"),
("Gameluster: GTA 6 PC port leak", "https://gameluster.com/gta-6-pc-port-leak-cyberleak-threat/"),
],
),
]

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from posts2 import POSTS2, NEW
from posts3 import NEW2
from posts4 import POSTS4
from posts_daily_20261123_b2 import POSTS_DAILY_20261123_B2
from posts_daily_20261123_b3 import POSTS_DAILY_20261123_B3
from posts_daily_20261123_b4 import POSTS_DAILY_20261123_B4
from posts_daily_20261123_b5 import POSTS_DAILY_20261123_B5
from posts_daily_20261124_b1 import POSTS_DAILY_20261124_B1
from posts_daily_20261124_b2 import POSTS_DAILY_20261124_B2
from posts_daily_20261124_b2_muse import POSTS_DAILY_20261124_B2_MUSE
from posts_daily_20261124_b3 import POSTS_DAILY_20261124_B3
from posts_daily_20261124_b4 import POSTS_DAILY_20261124_B4
from posts_daily_20261124_b5 import POSTS_DAILY_20261124_B5
from posts_daily_20261125_b1 import POSTS_DAILY_20261125_B1
from posts_daily_20261125_b2 import POSTS_DAILY_20261125_B2
from posts_daily_20261125_b3 import POSTS_DAILY_20261125_B3
from posts_daily_20261125_b5 import POSTS_DAILY_20261125_B5
from posts_daily_20261126_b1 import POSTS_DAILY_20261126_B1
from posts_daily_20261126_b2 import POSTS_DAILY_20261126_B2
from posts_daily_20261126_b3 import POSTS_DAILY_20261126_B3
from posts_daily_20261126_b4 import POSTS_DAILY_20261126_B4
from posts_daily_20261126_b5 import POSTS_DAILY_20261126_B5
from posts_daily_20261127_b1 import POSTS_DAILY_20261127_B1
from posts_daily_20261127_b2 import POSTS_DAILY_20261127_B2
RELATED = {
    "gta-6-pc-release-date": ["gta-6-pc-vs-console", "rockstar-pc-ports-history", "gta-6-pc-price"],
    "gta-6-pc-launch": ["gta-6-pc-system-requirements", "gta-6-pc-price", "gta-6-pc-mods-fivem"],
    "gta-6-pc-leak": ["gta-6-pc-download-scams", "gta-6-xbox-build-on-pc", "gta-6-built-for-pc"],
    "gta-6-built-for-pc": ["anyps5-gta-6-pc", "gta-6-xbox-build-on-pc", "gta-6-pc-leak"],
    "gta-6-xbox-build-on-pc": ["gta-6-pc-download-scams", "gta-6-pc-leak", "gta-6-built-for-pc"],
}
for _p in POSTS:
    _p.setdefault("related", RELATED.get(_p["slug"], []))
# Newest first, so the homepage and blog index lead with the latest news.
POSTS = POSTS_DAILY_20261127_B2 + POSTS_DAILY_20261127_B1 + POSTS_DAILY_20261126_B5 + POSTS_DAILY_20261126_B4 + POSTS_DAILY_20261126_B3 + POSTS_DAILY_20261126_B2 + POSTS_DAILY_20261126_B1 + POSTS_DAILY_20261125_B5 + POSTS_DAILY_20261125_B3 + POSTS_DAILY_20261125_B2 + POSTS_DAILY_20261125_B1 + POSTS_DAILY_20261124_B5 + POSTS_DAILY_20261124_B4 + POSTS_DAILY_20261124_B3 + POSTS_DAILY_20261124_B2_MUSE + POSTS_DAILY_20261124_B1 + POSTS_DAILY_20261124_B2 + NEW2 + NEW + POSTS + POSTS2 + POSTS4 + POSTS_DAILY_20261123_B2 + POSTS_DAILY_20261123_B3 + POSTS_DAILY_20261123_B4 + POSTS_DAILY_20261123_B5
BY_SLUG = {q["slug"]: q for q in POSTS}

# Stable per-post dates. A post keeps its first publish date forever; "modified" only
# moves when a post's content really changes (set updated="YYYY-MM-DD" on the post).
# New slugs are added here automatically with today's date.
import datetime
_DATES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "post_dates.json")
POST_DATES = json.load(open(_DATES_FILE)) if os.path.exists(_DATES_FILE) else {}
for q in POSTS:
    d = POST_DATES.setdefault(q["slug"], [TODAY, TODAY])
    if q.get("updated") and q["updated"] > d[1]:
        d[1] = q["updated"]
    q["published"], q["modified"] = d
json.dump(POST_DATES, open(_DATES_FILE, "w"), indent=1, sort_keys=True)
def human(d):
    x = datetime.date.fromisoformat(d)
    return f"{x.strftime('%B')} {x.day}, {x.year}"
LATEST_MOD = max(q["modified"] for q in POSTS)

TOPICS = [
    ("leaks-and-ports", "Leaks & PC ports", "Cyberleek, the leaked Xbox build, AnyPS5, Leonida, dumps and every unofficial route to GTA 6 on PC.",
     ["leak", "cyberleek", "leonida", "xbox", "dump", "anyps5", "emulator", "ps5-build", "native-build", "built-for-pc", "modders"]),
    ("hardware", "PC hardware & performance", "System requirements, file size, frame rates and what kind of PC you'll need for GTA 6.",
     ["requirements", "file-size", "fps", "best-pc", "system", "ray"]),
    ("guides", "Guides & safety", "How to play GTA 6 on PC today, avoiding scams and fake videos, price, stores and mods.",
     ["scam", "fake", "remote-play", "vs-console", "price", "steam", "mods"]),
    ("release-news", "Release date & news", "The GTA 6 PC release date, launch expectations, GTA 6 Online, sales and Take-Two news.",
     [""]),
]
def topic_of(p):
    for key, name, blurb, words in TOPICS:
        if any(w and w in p["slug"] for w in words):
            return key
    return "release-news"
TOPIC_NAME = {k: n for k, n, _, _ in TOPICS}

def share_bar(p):
    from urllib.parse import quote
    u = quote(f"{SITE}/blog/{p['slug']}/", safe=""); t = quote(p["title"], safe="")
    links = [("X", f"https://twitter.com/intent/tweet?url={u}&text={t}"),
             ("Facebook", f"https://www.facebook.com/sharer/sharer.php?u={u}"),
             ("WhatsApp", f"https://api.whatsapp.com/send?text={t}%20{u}"),
             ("Reddit", f"https://www.reddit.com/submit?url={u}&title={t}")]
    return '<div class="share"><span>Share</span>' + "".join(f'<a href="{h}" target="_blank" rel="noopener nofollow">{n}</a>' for n, h in links) + "</div>"

def related_for(p):
    picks = [BY_SLUG[s] for s in p.get("related", []) if s in BY_SLUG]
    for q in POSTS:
        if len(picks) >= 3: break
        if q is not p and q not in picks: picks.append(q)
    return picks[:3]

def img_block(p, depth, cls="hero-img"):
    up = "../" * depth
    return (f'<figure class="{cls}"><img src="{up}assets/blog/{p["slug"]}.jpg" alt="{html.escape(p.get("img_alt", p["title"]))}" width="1600" height="900" '
            f'onerror="this.closest(\'figure\').remove()"><figcaption>{p.get("caption", "Graphic: GTA6 PC")}</figcaption></figure>')

def card(p, depth):
    up = "../" * depth
    return f'''<a class="card" href="{up}blog/{p["slug"]}/">
  <div class="thumb"><img src="{up}assets/blog/{p["slug"]}.jpg" alt="" loading="lazy" onerror="this.remove()"><span>{p["short"]}</span></div>
  <div class="body"><div class="meta">{p["kicker"]} · {human(p["published"])}</div><h2>{p["title"]}</h2><p>{p["desc"]}</p></div>
</a>'''

def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(text)

for p in POSTS:
    path = f"blog/{p['slug']}/"
    url = f"{SITE}/{path}"
    article_ld = {
        "@context": "https://schema.org", "@type": "NewsArticle",
        "headline": p["title"], "description": p["desc"],
        "image": [f"{SITE}/assets/blog/{p['slug']}.jpg"],
        "datePublished": p["published"], "dateModified": p["modified"],
        "author": {"@type": "Organization", "name": AUTHOR, "url": f"{SITE}/about/"},
        "publisher": {"@type": "Organization", "name": NAME, "url": SITE},
        "mainEntityOfPage": url,
    }
    crumbs_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}/blog/"},
        {"@type": "ListItem", "position": 3, "name": TOPIC_NAME[topic_of(p)], "item": f"{SITE}/blog/topic/{topic_of(p)}/"},
        {"@type": "ListItem", "position": 4, "name": p["h1"], "item": url}]}
    lds = [article_ld, crumbs_ld]
    if p.get("faq"):
        lds.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]})
    sources = "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{html.escape(t)}</a></li>' for t, u in p["sources"])
    related = "".join(card(q, 2) for q in related_for(p))
    page = head(p["title"], p["desc"], path, 2, f"{SITE}/assets/blog/{p['slug']}.jpg", "article", lds) + nav(2, "blog") + f'''
<main>
<div class="narrow">
  <div class="crumbs"><a href="../../">Home</a> / <a href="../">Blog</a> / <a href="../topic/{topic_of(p)}/">{TOPIC_NAME[topic_of(p)]}</a></div>
  <article>
    <header>
      <div class="eyebrow">{p["kicker"]}</div>
      <h1 class="display">{p["h1"]}</h1>
      <div class="byline"><span>By <a href="../../about/">{AUTHOR}</a></span><span>Published <time datetime="{p["published"]}">{human(p["published"])}</time></span>{f'<span>Updated <time datetime="{p["modified"]}">{human(p["modified"])}</time></span>' if p["modified"] != p["published"] else ""}</div>
      <p class="lede">{p["lede"]}</p>
    </header>
    {img_block(p, 2)}
    <div class="tldr"><strong class="t">Short answer</strong>{p["tldr"]}</div>
    <div class="prose">
      {p["body"]}
      <!-- Google AdSense: in-article ad unit can go here -->
      <p class="updated">Last updated <time datetime="{p["modified"]}">{human(p["modified"])}</time>. We update this page when Rockstar announces anything new.</p>
      <div class="sources"><h2>Sources</h2><ul>{sources}</ul></div>
      {share_bar(p)}
    </div>
  </article>
</div>
<div class="wrap related"><h2>More GTA 6 PC news</h2><div class="grid" style="padding-bottom:0">{related}</div></div>
</main>
''' + footer(2) + "\n</body>\n</html>\n"
    write(path + "index.html", page)

# blog index
blog_ld = {"@context": "https://schema.org", "@type": "Blog", "name": f"{NAME} Blog", "url": f"{SITE}/blog/",
           "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": f"{SITE}/blog/{p['slug']}/", "datePublished": p["published"], "dateModified": p["modified"]} for p in POSTS]}
write("blog/index.html", head("GTA 6 PC News: Release Date, Requirements, Native Builds and Leaks | GTA6 PC Blog",
      "The latest GTA 6 PC news: release date status, the leaked Xbox build, what a native PC version means, and how to avoid fake GTA 6 PC downloads.",
      "blog/", 1, None, "website", [blog_ld]) + nav(1, "blog") + f'''
<main class="wrap">
  <div class="page-head"><div class="eyebrow">Blog</div><h1 class="display">GTA 6 PC news</h1>
  <p>Release date updates, leak coverage and plain-English explainers for everyone waiting on GTA 6 for PC. Every article links to its sources.</p><div class="chips">{"".join(f'<a href="topic/{k}/">{n}</a>' for k, n, _, _ in TOPICS)}</div><p style="margin-top:14px">Popular searches: <a href="gta-6-pc-release-date/">release date</a> · <a href="gta-6-pc-system-requirements/">system requirements</a> · <a href="gta-6-pc-download-scams/">PC download</a> · <a href="gta-6-pc-native-build/">native build tracker</a> · <a href="anyps5-gta-6-pc/">AnyPS5</a> · <a href="gta-6-ps5-build-on-pc/">PS5 build on PC</a> · <a href="gta-6-pc-emulator/">emulator</a> · <a href="gta-6-pc-steam/">Steam</a></p></div>
  <div class="grid">{"".join(card(p, 1) for p in POSTS)}</div>
</main>
''' + footer(1) + "\n</body>\n</html>\n")

# simple pages
def simple(path, key, title, desc, h1, body):
    write(path + "index.html", head(title, desc, path, 1) + nav(1, key) + f'''
<main class="narrow">
  <div class="page-head"><h1 class="display">{h1}</h1></div>
  <div class="prose" style="padding-bottom:90px">{body}</div>
</main>
''' + footer(1) + "\n</body>\n</html>\n")

simple("about/", "about", "About GTA6 PC", "Who runs GTA6 PC, what we cover and how we source our GTA 6 PC news.", "About GTA6 PC", """
<p>GTA6 PC is an independent fan site for people waiting to play Grand Theft Auto VI on PC. We cover the PC release date, official announcements, leaks and the claims going around about GTA 6 on PC.</p>
<h2>How we write</h2>
<ul>
<li>We separate what Rockstar has confirmed from reports and rumors, and we say which is which.</li>
<li>Every article links to its sources.</li>
<li>We never link to leaked game files or unofficial downloads.</li>
<li>We update articles when the facts change and show the date of the last update.</li>
</ul>
<h2>Editorial policy</h2>
<ul>
<li><strong>Confirmed vs reported:</strong> we only call something confirmed when Rockstar, Take-Two, Sony or Microsoft has said it. Everything else is labeled as a report, a rumor or our estimate.</li>
<li><strong>Sources:</strong> we link to the original reporting, and we prefer established outlets and official announcements.</li>
<li><strong>Images:</strong> cover graphics are made by us. Official artwork is credited to Rockstar Games and used for news and commentary.</li>
<li><strong>No piracy:</strong> we never link to leaked builds, game files, cracks or jailbreak tools, and we warn readers about fake downloads.</li>
</ul>
<h2>Corrections</h2>
<p>If we get something wrong, we fix it and update the article's date. Send corrections to <a href="mailto:contact@gta6pc.buzz">contact@gta6pc.buzz</a> with the article link.</p>
<h2>Independence</h2>
<p>GTA6 PC isn't affiliated with Rockstar Games or Take-Two Interactive. The site is supported by advertising, and advertisers have no say over what we write.</p>
<p>Spotted a mistake? <a href="../contact/">Let us know</a>.</p>
""")

simple("contact/", "contact", "Contact GTA6 PC", "Get in touch with the GTA6 PC team for corrections, tips or questions.", "Contact", """
<p>For corrections, news tips or general questions, email us at <a href="mailto:contact@gta6pc.buzz">contact@gta6pc.buzz</a>.</p>
<p>We read everything and usually reply within a few days. If you're reporting an error in an article, please include the link and what needs fixing.</p>
""")

simple("privacy-policy/", "", "Privacy Policy | GTA6 PC", "How GTA6 PC handles data, cookies and advertising, including Google AdSense.", "Privacy Policy", f"""
<p><em>Last updated {TODAY_H}</em></p>
<p>This policy explains what information GTA6 PC ("we", "us") collects when you visit this website and how it's used.</p>
<h2>Information we collect</h2>
<p>We don't ask you to create an account. If you email us, we receive your email address and whatever you include in your message, and we use it only to reply.</p>
<p>Like most websites, our hosting provider may log basic technical information such as your IP address, browser type and the pages you visit, for security and to keep the site running.</p>
<h2>Cookies and advertising</h2>
<p>We use Google AdSense to show ads. Third-party vendors, including Google, use cookies to serve ads based on your previous visits to this website or other websites.</p>
<p>Google's use of advertising cookies enables it and its partners to serve ads to you based on your visits to this site and/or other sites on the internet.</p>
<p>You can opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" rel="noopener">Google Ads Settings</a>. You can also opt out of some third-party vendors' use of cookies for personalized advertising at <a href="https://www.aboutads.info/choices/" rel="noopener">www.aboutads.info</a>.</p>
<p>To learn how Google uses information from sites that use its services, see <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">How Google uses information from sites or apps that use our services</a>.</p>
<h2>Analytics</h2>
<p>If we add an analytics service, it may use cookies to measure how visitors use the site. We'll list it here when we do.</p>
<h2>Your choices</h2>
<p>You can block or delete cookies in your browser settings. If you're in the EEA, UK or Switzerland, you'll be asked for consent before personalized ads are shown.</p>
<h2>Children</h2>
<p>This site isn't directed at children under 13, and we don't knowingly collect their information.</p>
<h2>Changes</h2>
<p>We may update this policy. The date at the top shows when it last changed.</p>
<h2>Contact</h2>
<p>Questions about this policy? Email <a href="mailto:contact@gta6pc.buzz">contact@gta6pc.buzz</a>.</p>
""")

# topic hub pages
for key, name, blurb, _ in TOPICS:
    items = [q for q in POSTS if topic_of(q) == key]
    path = f"blog/topic/{key}/"
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": f"GTA 6 PC: {name}", "url": f"{SITE}/{path}"}
    cards = "".join(card(q, 3) for q in items)
    write(path + "index.html", head(f"GTA 6 PC {name}: All Articles | {NAME}", f"{blurb} {len(items)} sourced articles.", path, 3, None, "website", [ld]) + nav(3, "blog") + f'''
<main class="wrap">
  <div class="crumbs"><a href="../../../">Home</a> / <a href="../../">Blog</a> / {name}</div>
  <div class="page-head" style="padding-top:40px"><div class="eyebrow">Topic</div><h1 class="display">{name}</h1><p>{blurb}</p>
  <div class="chips">{"".join(f'<a href="../{k}/"{" aria-current=page" if k == key else ""}>{n}</a>' for k, n, _, _ in TOPICS)}</div></div>
  <div class="grid">{cards}</div>
</main>
''' + footer(3) + "\n</body>\n</html>\n")
write("blog/topic/index.html", head(f"GTA 6 PC Topics | {NAME}", "Browse GTA 6 PC news by topic: leaks and ports, PC hardware, guides and safety, and release date news.", "blog/topic/", 2) + nav(2, "blog") + f'''
<main class="wrap">
  <div class="page-head"><div class="eyebrow">Topics</div><h1 class="display">Browse by topic</h1></div>
  <div class="grid" style="padding-bottom:100px">{"".join(f'<a class="card" href="{k}/"><div class="body"><div class="meta">{len([q for q in POSTS if topic_of(q) == k])} articles</div><h2>{n}</h2><p>{b}</p></div></a>' for k, n, b, _ in TOPICS)}</div>
</main>
''' + footer(2) + "\n</body>\n</html>\n")

# RSS feed
from email.utils import format_datetime
import datetime
_pub = format_datetime(datetime.datetime(2026, 11, 23, 12, 0, tzinfo=datetime.timezone.utc))
rss_items = "".join(f"""  <item><title>{html.escape(q['title'])}</title><link>{SITE}/blog/{q['slug']}/</link><guid>{SITE}/blog/{q['slug']}/</guid><pubDate>{format_datetime(datetime.datetime.fromisoformat(q["published"] + "T12:00:00+00:00"))}</pubDate><description>{html.escape(q['desc'])}</description><enclosure url="{SITE}/assets/blog/{q['slug']}.jpg" type="image/jpeg" length="0"/></item>\n""" for q in POSTS)
write("feed.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>GTA6 PC news</title>
  <link>{SITE}/</link>
  <atom:link href="{SITE}/feed.xml" rel="self" type="application/rss+xml"/>
  <description>GTA 6 PC release date, leaks, ports and guides.</description>
  <language>en</language>
  <lastBuildDate>{_pub}</lastBuildDate>
{rss_items}</channel>
</rss>
""")

# 404 page (served by GitHub Pages for any missing URL, so links are absolute)
write("404.html", head(f"Page not found | {NAME}", "This page doesn't exist.", "404.html", -1, noindex=True) + nav(-1) + f'''
<main class="wrap">
  <div class="page-head"><div class="eyebrow">404</div><h1 class="display">Page not found</h1><p>That page doesn't exist, or it moved. Try one of these instead.</p></div>
  <div class="grid">{"".join(card(q, 0).replace('href="blog/', 'href="/blog/').replace('src="assets/', 'src="/assets/') for q in POSTS[:6])}</div>
</main>
''' + footer(-1) + "\n</body>\n</html>\n")

simple("terms/", "", "Terms of Use | GTA6 PC", "The terms for using the GTA6 PC website.", "Terms of Use", f"""
<p><em>Last updated {TODAY_H}</em></p>
<p>By using GTA6 PC ("the site"), you agree to these terms.</p>
<h2>Use of the site</h2>
<p>The site is provided for general information about Grand Theft Auto VI and its PC release. You may read, link to and share our articles. You may not copy our articles or graphics in full onto other sites without permission.</p>
<h2>Accuracy</h2>
<p>We work to keep articles accurate and up to date, but news about unreleased products changes quickly. Information is provided "as is," without guarantees. Always check official sources before making purchases.</p>
<h2>External links</h2>
<p>We link to other websites as sources. We aren't responsible for their content or practices.</p>
<h2>Trademarks</h2>
<p>Grand Theft Auto, GTA, Rockstar Games and related marks belong to Take-Two Interactive Software, Inc. and its subsidiaries. PlayStation, Xbox and other product names belong to their owners. Their use here is for identification and commentary only.</p>
<h2>Advertising</h2>
<p>The site shows ads from third parties such as Google AdSense. See our <a href="../privacy-policy/">Privacy Policy</a> for how cookies are used.</p>
<h2>Changes</h2>
<p>We may update these terms. The date at the top shows the latest version.</p>
<h2>Contact</h2>
<p>Questions? Email <a href="mailto:contact@gta6pc.buzz">contact@gta6pc.buzz</a>.</p>
""")

simple("disclaimer/", "", "Disclaimer | GTA6 PC", "GTA6 PC is an unofficial fan site. Read our disclaimer on affiliation, accuracy and downloads.", "Disclaimer", f"""
<p><em>Last updated {TODAY_H}</em></p>
<h2>Unofficial fan site</h2>
<p>GTA6 PC is an independent, unofficial fan site. It is not affiliated with, endorsed by or sponsored by Rockstar Games, Take-Two Interactive, Sony Interactive Entertainment or Microsoft.</p>
<h2>No downloads</h2>
<p>We do not offer, host or link to GTA 6 game files, leaked builds, cracks, emulators loaded with games, or jailbreak tools. Any site claiming to offer a GTA 6 PC download today is not legitimate.</p>
<h2>Estimates and reports</h2>
<p>Where we give estimates, such as PC system requirements or install size, they are clearly labeled as estimates. Reports from other outlets are attributed and linked. Only announcements from the companies involved are described as confirmed.</p>
<h2>Advertising</h2>
<p>The site is supported by ads. Ads are served by third parties and don't represent an endorsement by us.</p>
""")

# homepage structured data
home = os.path.join(ROOT, "index.html")
h = open(home).read()
la, lb = "<!--LD-->", "<!--/LD-->"
if la in h:
    org = {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": f"{SITE}/#org", "name": NAME, "url": f"{SITE}/", "logo": f"{SITE}/assets/icon-512.png",
         "email": "contact@gta6pc.buzz"},
        {"@type": "WebSite", "@id": f"{SITE}/#site", "name": NAME, "url": f"{SITE}/", "publisher": {"@id": f"{SITE}/#org"}, "inLanguage": "en"}]}
    h = h[:h.index(la) + len(la)] + f'<script type="application/ld+json">{json.dumps(org)}</script>' + h[h.index(lb):]
    open(home, "w").write(h)

# homepage "latest news" block
home = os.path.join(ROOT, "index.html")
h = open(home).read()
a, b = "<!--LATEST-->", "<!--/LATEST-->"
if a in h:
    items = "".join(
        f'<a class="lcard" href="blog/{q["slug"]}/"><img src="assets/blog/{q["slug"]}.jpg" alt="" loading="lazy" width="1280" height="720"><span class="lk">{q["kicker"]}</span><span class="lt">{html.escape(q["title"])}</span></a>'
        for q in POSTS[:6])
    h = h[:h.index(a) + len(a)] + items + h[h.index(b):]
    open(home, "w").write(h)

# sitemap + robots
urls = ["", "blog/", "blog/topic/"] + [f"blog/topic/{k}/" for k, _, _, _ in TOPICS] + ["about/", "contact/", "privacy-policy/", "terms/", "disclaimer/"]
def _img(u):
    return f"<image:image><image:loc>{SITE}/{u}</image:loc></image:image>"
sm_rows = [f"  <url><loc>{SITE}/</loc><lastmod>{LATEST_MOD}</lastmod>{_img('assets/og-default.jpg')}</url>\n"]
sm_rows += [f"  <url><loc>{SITE}/{u}</loc>" + (f"<lastmod>{LATEST_MOD}</lastmod>" if u.startswith("blog/") else "") + "</url>\n" for u in urls[1:]]
sm_rows += [f"  <url><loc>{SITE}/blog/{q['slug']}/</loc><lastmod>{q['modified']}</lastmod>{_img('assets/blog/' + q['slug'] + '.jpg')}</url>\n" for q in POSTS]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + "".join(sm_rows) + "</urlset>\n"
write("sitemap.xml", sm)
write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /marketing/\nDisallow: /tools/\n\nSitemap: {SITE}/sitemap.xml\n")
print("ok", len(POSTS), "posts")
