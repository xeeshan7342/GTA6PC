"""Generates the blog, legal pages, sitemap and robots.txt for the GTA6 PC site."""
import json, os, sys, html

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..")
SITE = "https://gta6pc.buzz"   # replace once the domain is bought
NAME = "GTA6 PC"
AUTHOR = "GTA6 PC Editorial"
TODAY = "2026-11-23"
TODAY_H = "November 23, 2026"

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@125,800;125,900&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">'

def nav(depth, current=""):
    up = "../" * depth
    def a(href, label, key, cls=""):
        cur = ' aria-current="page"' if key == current else ""
        c = f' class="{cls}"' if cls else ""
        return f'<a href="{up}{href}"{cur}{c}>{label}</a>'
    return f'''<nav><div class="wrap">
  <a href="{up}" class="logo">GTA6<b>PC</b></a>
  <div class="nav-links">{a("", "Home", "home", "hide-sm")}{a("blog/", "Blog", "blog")}{a("about/", "About", "about")}{a("contact/", "Contact", "contact", "hide-sm")}</div>
</div></nav>'''

def footer(depth):
    up = "../" * depth
    return f'''<footer><div class="wrap">
  <div class="foot-top">
    <div><a href="{up}" class="logo">GTA6<b>PC</b></a><p>GTA 6 PC news, release info and guides · unofficial fan site</p></div>
    <div class="foot-links"><a href="{up}blog/">Blog</a><a href="{up}about/">About</a><a href="{up}contact/">Contact</a><a href="{up}privacy-policy/">Privacy Policy</a></div>
  </div>
  <p class="legal">{NAME} is an unofficial fan site. It is not affiliated with, endorsed by or sponsored by Rockstar Games or Take-Two Interactive. Grand Theft Auto and related marks are trademarks of Take-Two Interactive Software, Inc. Artwork credited to Rockstar Games is used for news reporting and commentary.</p>
</div></footer>'''

def head(title, desc, path, depth, og_image=None, og_type="website", extra_ld=None):
    up = "../" * depth
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
<meta name="robots" content="index, follow, max-image-preview:large">
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
<!-- Google AdSense: paste the AdSense <script> tag here once your site is approved -->
{ld}
</head>
<body>
'''

# ---------------------------------------------------------------- posts
POSTS = [
dict(
slug="gta-6-pc-release-date",
short="When on PC?",
title="When Is GTA 6 Coming to PC? Release Date Status (November 2026)",
h1="When is GTA 6 coming to PC?",
desc="GTA 6 is out on PS5 and Xbox Series X|S, but Rockstar hasn't set a PC date. Here's the reported Q1 2027 window, what Rockstar's history suggests, and what to watch for.",
kicker="Release date",
lede="GTA 6 launched on consoles on November 19, 2026. PC players are still waiting, and Rockstar hasn't said for how long. Here's everything that's actually known.",
img_alt="GTA 6 PC release date status graphic showing the reported Q1 2027 window",
tldr="There is <strong>no official GTA 6 PC release date</strong>. Rockstar has only released the game on PS5 and Xbox Series X|S. A GamesBeat report from October 2026 says Rockstar is aiming for <strong>the first quarter of 2027</strong>, but Rockstar hasn't confirmed it.",
body="""
<h2>What Rockstar has officially said</h2>
<p>Rockstar has only ever announced GTA 6 for PlayStation 5 and Xbox Series X|S. The game went through two delays before it shipped: first from 2025 to May 26, 2026, then to November 19, 2026, when it finally launched on both consoles.</p>
<p>No PC version, PC store page or PC system requirements have been announced. Until Rockstar posts something on its own site, any exact PC date you see online is a guess.</p>

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

<h2>Quick answers</h2>
<h3>Is GTA 6 on Steam?</h3>
<p>Not yet. Rockstar hasn't announced any PC store listing.</p>
<h3>Can I pre-order GTA 6 for PC?</h3>
<p>No. There's no official PC pre-order. Any site taking PC pre-orders right now isn't selling a real product.</p>
<h3>Will my console save carry over to PC?</h3>
<p>Rockstar hasn't said. When GTA V moved to PC, players could transfer their GTA Online progress, but nothing is confirmed for GTA 6.</p>
""",
sources=[
("GamesBeat: Grand Theft Auto VI's PC release is slated for Q1 2027", "https://gamesbeat.com/grand-theft-auto-vis-pc-release-is-slated-for-q1-2027/"),
("VGC: GTA 6 PC release date guide", "https://www.videogameschronicle.com/guide/gta-6-pc-version/"),
("PCWorld: We guessed late 2027 for GTA 6 on PC, a report says Q1 2027", "https://www.pcworld.com/article/3260660/we-guessed-late-2027-for-gta-6-on-pc-a-report-says-q1-2027.html"),
("Yahoo Tech: GTA 6 PC release date", "https://tech.yahoo.com/gaming/articles/gta-6-pc-release-date-150338948.html"),
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
RELATED = {
    "gta-6-pc-release-date": ["gta-6-pc-vs-console", "rockstar-pc-ports-history", "gta-6-pc-price"],
    "gta-6-pc-launch": ["gta-6-pc-system-requirements", "gta-6-pc-price", "gta-6-pc-mods-fivem"],
    "gta-6-pc-leak": ["gta-6-pc-download-scams", "gta-6-xbox-build-on-pc", "gta-6-built-for-pc"],
    "gta-6-built-for-pc": ["anyps5-gta-6-pc", "gta-6-xbox-build-on-pc", "gta-6-pc-leak"],
    "gta-6-xbox-build-on-pc": ["gta-6-pc-download-scams", "gta-6-pc-leak", "gta-6-built-for-pc"],
}
for _p in POSTS:
    _p.setdefault("related", RELATED.get(_p["slug"], []))
POSTS = NEW2 + NEW + POSTS + POSTS2 + POSTS4
BY_SLUG = {q["slug"]: q for q in POSTS}

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
  <div class="body"><div class="meta">{p["kicker"]} · {TODAY_H}</div><h2>{p["title"]}</h2><p>{p["desc"]}</p></div>
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
        "datePublished": TODAY, "dateModified": TODAY,
        "author": {"@type": "Organization", "name": AUTHOR, "url": f"{SITE}/about/"},
        "publisher": {"@type": "Organization", "name": NAME, "url": SITE},
        "mainEntityOfPage": url,
    }
    crumbs_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}/blog/"},
        {"@type": "ListItem", "position": 3, "name": p["h1"], "item": url}]}
    lds = [article_ld, crumbs_ld]
    if p.get("faq"):
        lds.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]})
    sources = "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{html.escape(t)}</a></li>' for t, u in p["sources"])
    related = "".join(card(q, 2) for q in related_for(p))
    page = head(p["title"], p["desc"], path, 2, f"{SITE}/assets/blog/{p['slug']}.jpg", "article", lds) + nav(2, "blog") + f'''
<main>
<div class="narrow">
  <div class="crumbs"><a href="../../">Home</a> / <a href="../">Blog</a> / {p["short"]}</div>
  <article>
    <header>
      <div class="eyebrow">{p["kicker"]}</div>
      <h1 class="display">{p["h1"]}</h1>
      <div class="byline"><span>By {AUTHOR}</span><span>Published <time datetime="{TODAY}">{TODAY_H}</time></span></div>
      <p class="lede">{p["lede"]}</p>
    </header>
    {img_block(p, 2)}
    <div class="tldr"><strong class="t">Short answer</strong>{p["tldr"]}</div>
    <div class="prose">
      {p["body"]}
      <!-- Google AdSense: in-article ad unit can go here -->
      <p class="updated">Last updated <time datetime="{TODAY}">{TODAY_H}</time>. We update this page when Rockstar announces anything new.</p>
      <div class="sources"><h2>Sources</h2><ul>{sources}</ul></div>
    </div>
  </article>
</div>
<div class="wrap related"><h2>More GTA 6 PC news</h2><div class="grid" style="padding-bottom:0">{related}</div></div>
</main>
''' + footer(2) + "\n</body>\n</html>\n"
    write(path + "index.html", page)

# blog index
blog_ld = {"@context": "https://schema.org", "@type": "Blog", "name": f"{NAME} Blog", "url": f"{SITE}/blog/",
           "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": f"{SITE}/blog/{p['slug']}/", "datePublished": TODAY} for p in POSTS]}
write("blog/index.html", head("GTA 6 PC News: Release Date, Requirements, Native Builds and Leaks | GTA6 PC Blog",
      "The latest GTA 6 PC news: release date status, the leaked Xbox build, what a native PC version means, and how to avoid fake GTA 6 PC downloads.",
      "blog/", 1, None, "website", [blog_ld]) + nav(1, "blog") + f'''
<main class="wrap">
  <div class="page-head"><div class="eyebrow">Blog</div><h1 class="display">GTA 6 PC news</h1>
  <p>Release date updates, leak coverage and plain-English explainers for everyone waiting on GTA 6 for PC. Every article links to its sources.</p><p style="margin-top:14px">Popular searches: <a href="gta-6-pc-release-date/">release date</a> · <a href="gta-6-pc-system-requirements/">system requirements</a> · <a href="gta-6-pc-download-scams/">PC download</a> · <a href="gta-6-pc-native-build/">native build tracker</a> · <a href="anyps5-gta-6-pc/">AnyPS5</a> · <a href="gta-6-ps5-build-on-pc/">PS5 build on PC</a> · <a href="gta-6-pc-emulator/">emulator</a> · <a href="gta-6-pc-steam/">Steam</a></p></div>
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
<h2>Independence</h2>
<p>GTA6 PC isn't affiliated with Rockstar Games or Take-Two Interactive. The site is supported by advertising.</p>
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
urls = ["", "blog/"] + [f"blog/{p['slug']}/" for p in POSTS] + ["about/", "contact/", "privacy-policy/"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
write("sitemap.xml", sm)
write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print("ok", len(POSTS), "posts")
