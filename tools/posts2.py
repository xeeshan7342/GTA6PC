"""Second batch of GTA6 PC blog posts. Imported by build_blog.py.

Each post may carry a "cover" dict, used by render_covers.py to draw its
original cover graphic: eyebrow, title, sub, and rows of (label, value, hot).
"""

POSTS2 = [
dict(
slug="gta-6-pc-system-requirements",
short="System requirements",
title="GTA 6 PC System Requirements: What We Know and What to Expect",
h1="GTA 6 PC system requirements: what we know",
desc="Rockstar hasn't published GTA 6 PC requirements yet. Here's what the console hardware tells us, our estimated specs, and how much storage to plan for.",
kicker="Hardware",
lede="Everyone wants to know if their PC can run GTA 6. Rockstar hasn't said yet, but the console versions give us a solid starting point.",
tldr="There are <strong>no official GTA 6 PC system requirements</strong> yet. The game was built for PS5 and Xbox Series X|S, so expect to need a <strong>modern 8-core CPU, a current-gen graphics card, 16 GB of RAM or more</strong> and <strong>well over 200 GB on an SSD</strong>. Treat any \"official spec list\" you see right now as fake.",
related=["gta-6-file-size", "gta-6-pc-launch", "gta-6-pc-vs-console"],
cover=dict(eyebrow="PC hardware · estimate", title="GTA 6 PC system requirements", sub="Not announced yet. Here's what the consoles tell us.",
           rows=[("CPU", "Modern 8-core", False), ("GPU", "Current-gen card", False), ("RAM", "16 GB+", False), ("Storage", "200+ GB SSD", True), ("Official specs", "Not announced", True)]),
body="""
<h2>Why there's no official list yet</h2>
<p>Rockstar publishes PC requirements when it announces a PC version, and it hasn't announced one for GTA 6. A GamesBeat report says a PC release is planned for early 2027, so requirements could appear in the weeks before that.</p>

<h2>What the console hardware tells us</h2>
<p>GTA 6 is a current-gen-only game. It skipped PS4 and Xbox One completely, so it's built around the PS5 and Xbox Series X|S. Those consoles use:</p>
<ul>
<li>An 8-core AMD Zen 2 processor</li>
<li>An AMD RDNA 2 graphics chip, roughly 10 teraflops on PS5 and 12 on Series X</li>
<li>16 GB of shared memory</li>
<li>A fast NVMe SSD, which the game relies on to stream its world</li>
</ul>
<p>PC versions usually need a bit more than the console to match it, because Windows and PC drivers add overhead, and because PC players want higher frame rates and resolutions.</p>

<h2>Our estimated specs</h2>
<p>These are our estimates based on the console hardware and Rockstar's past PC releases. They are not official.</p>
<div class="table-wrap"><table>
<tr><th></th><th>Minimum (estimate)</th><th>Recommended (estimate)</th></tr>
<tr><td>CPU</td><td>6-core, Ryzen 5 / Core i5 from recent years</td><td>8-core, Ryzen 7 / Core i7 from recent years</td></tr>
<tr><td>GPU</td><td>Graphics card with 8 GB VRAM, roughly RTX 3060 / RX 6600 class</td><td>12 GB+ VRAM, roughly RTX 4070 / RX 7800 XT class</td></tr>
<tr><td>RAM</td><td>16 GB</td><td>32 GB</td></tr>
<tr><td>Storage</td><td>SSD, 230+ GB free</td><td>NVMe SSD, 250+ GB free</td></tr>
<tr><td>OS</td><td>Windows 10/11 64-bit</td><td>Windows 11 64-bit</td></tr>
</table></div>

<h2>Storage is the safest prediction</h2>
<p>On consoles, GTA 6 is reported to be around a 210 GB download. PC versions are often a little larger once high-resolution textures are included, so plan for well over 200 GB. A hard drive will very likely be too slow, since the game was designed for console SSDs. More in our <a href="../gta-6-file-size/">GTA 6 file size guide</a>.</p>

<h2>Should you upgrade now?</h2>
<p>Not yet. Prices change, and the real requirements could be higher or lower than anyone expects. If you're building a PC anyway, an 8-core CPU, 32 GB of RAM, a 1 TB or 2 TB NVMe SSD and a current graphics card is a safe target for GTA 6 and other big games.</p>

<h2>Beware fake "official" spec lists</h2>
<p>Spec sheets claiming to be official GTA 6 PC requirements have been circulating for months. Rockstar hasn't released any. The only place official requirements will appear is Rockstar's own site and the store pages once the PC version is announced.</p>
""",
sources=[
("GamesBeat: Grand Theft Auto VI's PC release is slated for Q1 2027", "https://gamesbeat.com/grand-theft-auto-vis-pc-release-is-slated-for-q1-2027/"),
("GamesRadar: GTA 6 GB size", "https://www.gamesradar.com/games/grand-theft-auto/gta-6-gb-size/"),
("TweakTown: GTA 6 download size revealed, and it's over 200 GB", "https://www.tweaktown.com/news/114341/grand-theft-auto-6-download-size-revealed-and-yes-its-over-200-gb/index.html"),
],
),
dict(
slug="gta-6-pc-price",
short="PC price",
title="GTA 6 PC Price: How Much Will It Cost? (Editions Explained)",
h1="How much will GTA 6 cost on PC?",
desc="GTA 6 costs $79.99 on PS5 and Xbox, with a $99.99 Ultimate Edition. Here's what that means for the PC price, and why you shouldn't buy PC keys yet.",
kicker="Price",
lede="GTA 6 launched at a higher price than most games. PC pricing hasn't been announced, but Rockstar's history makes a good guess possible.",
tldr="On consoles, GTA 6 costs <strong>$79.99 (Standard)</strong> and <strong>$99.99 (Ultimate, digital only)</strong>. PC pricing <strong>hasn't been announced</strong>, but Rockstar has usually priced PC versions the same as consoles. <strong>Don't buy GTA 6 PC keys</strong> anywhere right now, because they don't exist.",
related=["gta-6-pc-release-date", "gta-6-pc-launch", "gta-6-pc-download-scams"],
cover=dict(eyebrow="Price · editions", title="GTA 6 price on PC", sub="Console prices are set. PC is not announced.",
           rows=[("Standard (console)", "$79.99", False), ("Ultimate (console)", "$99.99", False), ("Physical copy", "Code in a box", False), ("PC price", "Not announced", True)]),
body="""
<h2>GTA 6 console prices</h2>
<p>Rockstar confirmed GTA 6's pricing in June 2026, ahead of pre-orders. In the US, on PS5 and Xbox Series X|S:</p>
<div class="table-wrap"><table>
<tr><th>Edition</th><th>Price</th><th>Notes</th></tr>
<tr><td>Standard</td><td>$79.99</td><td>Digital, or physical as a download code in a box (no disc)</td></tr>
<tr><td>Ultimate</td><td>$99.99</td><td>Digital only, includes extra content</td></tr>
<tr><td>Ultimate upgrade</td><td>$20.00</td><td>For Standard owners</td></tr>
</table></div>
<p>Pre-orders came with a Vintage Vice City pack, and digital pre-orders also included a month of GTA+.</p>

<h2>What will GTA 6 cost on PC?</h2>
<p>Rockstar hasn't announced PC pricing. Its recent history points to the same price as consoles:</p>
<ul>
<li><strong>GTA V</strong> launched on PC in 2015 at $59.99, the same as the console versions.</li>
<li><strong>Red Dead Redemption 2</strong> launched on PC in 2019 at $59.99, again matching consoles.</li>
</ul>
<p>If Rockstar follows that pattern, expect <strong>around $79.99 for Standard and $99.99 for Ultimate</strong> on PC, with regional prices varying. That's our expectation, not an announcement.</p>

<h2>Will PC get extra content?</h2>
<p>Rockstar's PC versions have often added features, like the Rockstar Editor in GTA V and extra graphics options in RDR2, without raising the price. Nothing is confirmed for GTA 6.</p>

<h2>Don't buy GTA 6 PC keys yet</h2>
<div class="warn"><strong>There is no GTA 6 PC key for sale anywhere.</strong> Rockstar hasn't opened PC pre-orders. Sites selling "GTA 6 PC keys" or "PC pre-order codes" are scams, and some are built to steal payment details.</div>
<p>When PC pre-orders open, they'll be on Rockstar's store, Steam and the Epic Games Store. See our guide to <a href="../gta-6-pc-download-scams/">spotting fake GTA 6 PC downloads and stores</a>.</p>

<h2>Should you buy on console now or wait?</h2>
<p>If you own a PS5 or Xbox Series X|S and can't wait, the console version is available now. If you only game on PC, waiting is the only official option. We compare both in <a href="../gta-6-pc-vs-console/">GTA 6: wait for PC or play on console?</a></p>
""",
sources=[
("Windows Central: GTA VI price confirmed at $79.99 with a $99.99 Ultimate Edition", "https://www.windowscentral.com/gaming/grand-theft-auto-vi-price-confirmed-at-usd79-99-with-a-feature-locking-ultimate-edition-at-usd99-99-and-the-physical-edition-is-just-a-code-in-a-box"),
("TechRadar: We finally know the official GTA 6 price", "https://www.techradar.com/gaming/we-finally-know-the-official-gta-6-price-its-expensive-but-not-too-bad"),
("Engadget: Rockstar reveals pricing for Grand Theft Auto 6", "https://engadget.com/2200483/rockstar-reveals-gta-6-pricing-launch/"),
],
),
dict(
slug="gta-6-online-pc",
short="GTA 6 Online",
title="GTA 6 Online on PC: Release Date and What We Know",
h1="GTA 6 Online on PC: release date and what we know",
desc="GTA 6 launched without an online mode. Reports point to a 2027 release for GTA 6 Online. Here's what that means for PC players and GTA Online.",
kicker="Online",
lede="GTA 6 launched as a single-player game. The online mode that made GTA V a decade-long hit hasn't arrived yet, on any platform.",
tldr="<strong>GTA 6 Online has no release date.</strong> Bloomberg reported in October 2026 that it's expected in <strong>2027</strong>, but Rockstar hasn't announced it. PC players will need the PC version first, which is reported for early 2027.",
related=["gta-6-pc-release-date", "gta-6-pc-mods-fivem", "gta-6-pc-launch"],
cover=dict(eyebrow="Online mode · status", title="GTA 6 Online on PC", sub="Launched single-player only. Online is reported for 2027.",
           rows=[("GTA 6 story mode", "Out on console", False), ("GTA 6 Online", "Not announced", True), ("Reported window", "2027", True), ("GTA Online (V)", "Still supported", False)]),
body="""
<h2>GTA 6 launched without online</h2>
<p>When GTA 6 arrived on PS5 and Xbox Series X|S on November 19, 2026, it was a single-player game. Rockstar hasn't officially announced an online mode, let alone a date for one.</p>

<h2>What the reports say</h2>
<ul>
<li><strong>Bloomberg:</strong> in an October 14, 2026 report, Jason Schreier wrote that GTA 6's online component is expected in 2027. Coverage noted that Bloomberg said "expected," not "confirmed."</li>
<li><strong>Twitch's CEO</strong> told Bloomberg in September 2026 that the multiplayer mode would arrive "next year," without giving a date.</li>
<li>A later Bloomberg video suggested online would come about a year after launch. Schreier clarified that this wasn't a confirmed date.</li>
</ul>
<p>Put together, 2027 looks likely, but nothing is official.</p>

<h2>What it means for PC players</h2>
<p>PC players need the PC version of the game first. A GamesBeat report says that's targeting the first quarter of 2027. If both reports are right, PC players may not miss much online time at all, because the online mode could land after the PC version.</p>
<p>When GTA V came to PC in 2015, players could carry their GTA Online characters and progress over from PS3 and Xbox 360. Rockstar hasn't said whether anything like that will happen for GTA 6.</p>

<h2>What happens to GTA Online?</h2>
<p>Take-Two has said it will keep supporting GTA Online after GTA 6 launches, without giving a timeline. For now, GTA Online on PC is still the place to play Rockstar's online world.</p>

<h2>What about roleplay servers?</h2>
<p>Many PC players spend their GTA time on roleplay servers rather than GTA Online. Rockstar bought the team behind FiveM in 2023, which hints at plans for GTA 6 roleplay. We cover that in <a href="../gta-6-pc-mods-fivem/">GTA 6 mods and FiveM on PC</a>.</p>
""",
sources=[
("Digital Trends: GTA VI's online mode could arrive in 2027", "https://digitaltrends.com/gaming/gta-vis-online-mode-could-arrive-in-2027-well-after-the-single-player-campaign-begins/"),
("Digital Trends: Yet another report claims GTA 6 online arrives next year", "https://digitaltrends.com/gaming/yet-another-report-claims-gta-6-online-multiplayer-experience-arrives-next-year"),
("Beebom: Rockstar has GTA 6's online mode planned for 2027", "https://beebom.com/rockstar-has-gta-6-online-mode-planned-for-2027/"),
("GamesBeat: Grand Theft Auto VI's PC release is slated for Q1 2027", "https://gamesbeat.com/grand-theft-auto-vis-pc-release-is-slated-for-q1-2027/"),
],
),
dict(
slug="gta-6-file-size",
short="File size",
title="GTA 6 File Size: How Many GB on PS5, Xbox and PC?",
h1="How big is GTA 6? File size on PS5, Xbox and PC",
desc="GTA 6 is reported to be about a 210 GB download on PS5. Here's what that means for Xbox Series S owners, and how much space to plan for on PC.",
kicker="File size",
lede="GTA 6 is one of the biggest games ever released. Here's how much space it takes, and how much to clear for the PC version.",
tldr="GTA 6 is reported at <strong>about 210 GB on PS5</strong>, and the leaked Xbox build was reported at about 209 GB. For PC, <strong>plan for 230–250 GB free on an SSD</strong>. Rockstar hasn't published a PC size yet.",
related=["gta-6-pc-system-requirements", "gta-6-pc-launch", "gta-6-pc-vs-console"],
cover=dict(eyebrow="Storage · how many GB", title="GTA 6 file size", sub="Clear space now. It's one of the biggest games ever.",
           rows=[("PS5 (reported)", "~210 GB", False), ("Xbox build (leak)", "~209 GB", False), ("PC (our estimate)", "230–250 GB", True), ("Drive type", "SSD", True)]),
body="""
<h2>GTA 6 size on PS5</h2>
<p>Before launch, the PlayStation Game Size tracker reported GTA 6 as roughly a 210 GB download on PS5. Other reports put the space needed at around 212 GB. Day-one patches can add more on top.</p>

<h2>GTA 6 size on Xbox</h2>
<p>There's no widely reported official Xbox figure. The leaked Xbox build was reported at about 209 GB, which is in line with PS5. Series S owners should note that the 512 GB console only has about 364 GB free for games, so GTA 6 takes up more than half of it.</p>

<h2>How big will GTA 6 be on PC?</h2>
<p>Rockstar hasn't said. PC versions are often a bit larger than console versions because they ship higher-resolution textures and don't use the consoles' hardware decompression in the same way. Red Dead Redemption 2 needed 150 GB on PC, more than its console install.</p>
<p>Our estimate: <strong>plan for 230–250 GB of free space</strong>, and more if you want room for patches.</p>

<h2>Do you need an SSD?</h2>
<p>Very likely, yes. GTA 6 was designed around the fast SSDs in PS5 and Xbox Series X|S, which stream the open world as you move. On a hard drive, expect long loads and pop-in, if it's supported at all. An NVMe SSD is the safest choice.</p>

<h2>How to get ready</h2>
<ul>
<li>Check your free space now, and clear old games you don't play.</li>
<li>If you're buying a new drive, a 1 TB or 2 TB NVMe SSD gives room for GTA 6 and future patches.</li>
<li>Don't download anything claiming to be the "GTA 6 PC files." One fake 113 GB "PC ISO" turned out to be malware. More in our <a href="../gta-6-pc-download-scams/">scam guide</a>.</li>
</ul>
""",
sources=[
("GamesRadar: GTA 6 GB size", "https://www.gamesradar.com/games/grand-theft-auto/gta-6-gb-size/"),
("TweakTown: GTA 6 download size revealed, and it's over 200 GB", "https://www.tweaktown.com/news/114341/grand-theft-auto-6-download-size-revealed-and-yes-its-over-200-gb/index.html"),
("Dexerto: GTA 6 file size revealed", "https://dexerto.com/gta/gta-6-file-size-revealed-and-players-may-want-to-start-clearing-storage-space-3422258"),
("Cybernews: Scammers post fake pre-release build to spread malware", "https://cybernews.com/security/gta-six-game-build-fake-leak/"),
],
),
dict(
slug="gta-6-pc-download-scams",
short="Scam warning",
title="Fake GTA 6 PC Downloads: How to Spot the Scams and Stay Safe",
h1="Fake GTA 6 PC downloads: how to spot the scams",
desc="There is no GTA 6 PC download. Fake installers, demos and ISOs are spreading infostealers and ransomware. Here's how to spot them and what to do if you clicked one.",
kicker="Safety",
lede="GTA 6 is the biggest game in years, and scammers know it. Fake PC downloads, demos and \"early access\" pages have been spreading malware for months.",
tldr="<strong>There is no legitimate GTA 6 PC download.</strong> Security firms have found fake installers, demos and ISOs carrying <strong>password stealers, remote access tools and ransomware</strong>. If you ran one, disconnect from the internet, scan your PC and change your passwords from another device.",
related=["gta-6-pc-leak", "gta-6-xbox-build-on-pc", "gta-6-pc-release-date"],
cover=dict(eyebrow="Safety warning", title="Fake GTA 6 PC downloads", sub="There is no real GTA 6 PC download yet.",
           rows=[("\"Free PC download\"", "Fake", True), ("\"PC demo / early access\"", "Fake", True), ("\"113 GB PC ISO\"", "Malware", True), ("Official PC version", "Not out yet", False)]),
body="""
<h2>The short version</h2>
<p>Rockstar hasn't released or announced GTA 6 for PC. That means every "GTA 6 PC download," crack, repack, keygen, installer or "PS5 emulator" is fake. Many of them are worse than fake: they're malware.</p>

<h2>What security researchers have found</h2>
<ul>
<li><strong>Password stealers:</strong> McAfee reported fake GTA 6 downloads that installed information-stealing malware, including one pushed through Google Colab.</li>
<li><strong>Fake demo sites:</strong> Malwarebytes found sites copying Rockstar's style with a "Play Now" button that delivered an infostealer.</li>
<li><strong>Fake ISOs:</strong> Cybernews reported a 113 GB "GTA 6 PC ISO" that users found to be fake and malicious.</li>
<li><strong>Remote access and ransomware:</strong> TechRadar reported fake ISOs carrying remote access trojans, infostealers and ransomware.</li>
<li><strong>Pre-order and beta scams:</strong> phishing pages offering pre-orders, beta access or "early access" to steal payment details and game account logins.</li>
</ul>

<h2>How to spot a GTA 6 scam</h2>
<ol>
<li><strong>It offers GTA 6 on PC today.</strong> That alone means it's fake.</li>
<li><strong>It's free, cracked or "no ownership required."</strong></li>
<li><strong>It asks you to turn off your antivirus</strong> or "allow" a file Windows blocked.</li>
<li><strong>It sends you to a file host, Discord server or Google Drive link</strong> instead of Steam, Epic or Rockstar's store.</li>
<li><strong>It asks you to complete surveys</strong> or enter your phone number to "unlock" the download.</li>
<li><strong>Its only proof is a short video</strong>. One viral "GTA 6 PC port" clip was GTA V footage.</li>
</ol>

<h2>If you already downloaded or ran something</h2>
<ol>
<li>Disconnect the PC from the internet.</li>
<li>Run a full scan with Windows Security or another trusted antivirus.</li>
<li>From a different, clean device, change the passwords for your email, banking, Steam, Rockstar, Discord and other important accounts. Turn on two-factor authentication.</li>
<li>Watch your bank statements for charges you don't recognize.</li>
<li>If the scan finds something serious, consider resetting Windows.</li>
</ol>

<h2>Where the real PC version will be</h2>
<p>When GTA 6 comes to PC, it'll be sold on Rockstar's own store and launcher, and very likely Steam and the Epic Games Store. Nowhere else. Check our <a href="../gta-6-pc-release-date/">release date page</a> for the latest.</p>
""",
sources=[
("McAfee: GTA 6 is here, so are the scams", "https://www.mcafee.com/blogs/mcafee-news/gta-6-meccha-chameleon-gaming-scams-fall-gaming-releases/"),
("Malwarebytes: Fake GTA 6 demo sites deliver an infostealer", "https://www.malwarebytes.com/?p=456116"),
("Cybernews: Scammers post fake pre-release build to spread malware", "https://cybernews.com/security/gta-six-game-build-fake-leak/"),
("TechRadar: Fake GTA 6 malware is on the rise", "https://techradar.com/pro/security/fake-gta-6-malware-is-on-the-rise-as-release-date-nears-here-are-some-of-the-worst-scams-to-look-out-for"),
("Tom's Guide: GTA 6 pre-order scams are stealing users' info", "https://www.tomsguide.com/gaming/gta-6-warning-pre-order-scams-are-stealing-users-info-and-spreading-malware-how-to-stay-safe"),
],
),
dict(
slug="gta-6-pc-vs-console",
short="PC vs console",
title="GTA 6: Wait for PC or Play on PS5/Xbox Now?",
h1="GTA 6: wait for PC or play on console now?",
desc="GTA 6 is out on PS5 and Xbox, while PC is reportedly coming in early 2027. Here's how to decide whether to wait, based on what Rockstar's PC versions usually add.",
kicker="Buying guide",
lede="GTA 6 is out on consoles and PC players are stuck waiting. Is it worth buying a console version now, or should you hold out?",
tldr="If you already own a <strong>PS5 or Xbox Series X|S</strong> and want to play now, buy it on console. If you <strong>only play on PC</strong> and can wait, the PC version is reported for <strong>early 2027</strong> and Rockstar's PC versions usually add higher frame rates, more settings and mod support.",
related=["gta-6-pc-release-date", "gta-6-pc-system-requirements", "gta-6-pc-price"],
cover=dict(eyebrow="Buying guide", title="Wait for PC or play on console?", sub="It depends on what you own and how long you can wait.",
           rows=[("PS5 / Xbox", "Out now", False), ("PC", "Reported Q1 2027", True), ("Higher FPS & settings", "PC (usually)", False), ("Mods & roleplay", "PC (usually)", False)]),
body="""
<h2>Play on console now if…</h2>
<ul>
<li>You already own a PS5 or Xbox Series X|S.</li>
<li>You don't want to avoid spoilers for months.</li>
<li>You're happy with console performance and settings.</li>
</ul>
<p>GTA 6 costs $79.99 on console, or $99.99 for the Ultimate Edition. See our <a href="../gta-6-pc-price/">price guide</a>.</p>

<h2>Wait for PC if…</h2>
<ul>
<li>You only game on PC and don't want to buy a console.</li>
<li>You care about high frame rates, ultrawide screens or mouse and keyboard.</li>
<li>You want mods or roleplay servers.</li>
</ul>

<h2>What Rockstar's PC versions usually add</h2>
<div class="table-wrap"><table>
<tr><th></th><th>Console</th><th>PC (based on GTA V and RDR2)</th></tr>
<tr><td>Frame rate</td><td>Set by Rockstar per console mode</td><td>Unlocked, high refresh rate support</td></tr>
<tr><td>Graphics settings</td><td>A few modes</td><td>Dozens of options</td></tr>
<tr><td>Screens</td><td>TV, 16:9</td><td>Ultrawide and multi-monitor</td></tr>
<tr><td>Controls</td><td>Controller</td><td>Controller or mouse and keyboard</td></tr>
<tr><td>Mods and roleplay</td><td>No</td><td>Usually yes</td></tr>
<tr><td>Available</td><td>Now</td><td>Reported Q1 2027, not confirmed</td></tr>
</table></div>
<p>Nothing on the PC side is confirmed for GTA 6 yet. It's the pattern from Rockstar's last two PC releases.</p>

<h2>Can you buy on console and play on PC later?</h2>
<p>Rockstar hasn't said whether GTA 6 purchases or progress will carry over to PC. When GTA V moved to PC, players had to buy it again, though GTA Online progress could be transferred. Plan on buying twice if you do both.</p>

<h2>Our take</h2>
<p>If you own a current console, play it now. The story will be spoiled everywhere long before PC arrives. If you're PC-only, the wait is likely a few months, not years, and you'll probably get the best-looking version of the game.</p>
""",
sources=[
("GamesBeat: Grand Theft Auto VI's PC release is slated for Q1 2027", "https://gamesbeat.com/grand-theft-auto-vis-pc-release-is-slated-for-q1-2027/"),
("Windows Central: GTA VI price confirmed at $79.99", "https://www.windowscentral.com/gaming/grand-theft-auto-vi-price-confirmed-at-usd79-99-with-a-feature-locking-ultimate-edition-at-usd99-99-and-the-physical-edition-is-just-a-code-in-a-box"),
("VGC: GTA 6 PC release date guide", "https://www.videogameschronicle.com/guide/gta-6-pc-version/"),
],
),
dict(
slug="gta-6-pc-mods-fivem",
short="Mods & FiveM",
title="GTA 6 PC Mods and FiveM Roleplay: What to Expect",
h1="Will GTA 6 have mods and roleplay servers on PC?",
desc="Mods and roleplay servers kept GTA V alive on PC for over a decade. Rockstar bought the FiveM team in 2023. Here's what that could mean for GTA 6 on PC.",
kicker="Mods",
lede="On PC, GTA V lived a second life through mods and roleplay servers. GTA 6 on PC could go even further, because Rockstar now owns the biggest roleplay platform.",
tldr="Rockstar hasn't announced mod support for GTA 6. But in <strong>2023 Rockstar bought Cfx.re</strong>, the team behind the <strong>FiveM and RedM</strong> roleplay platforms, which strongly suggests roleplay will be part of GTA 6's future on PC.",
related=["gta-6-online-pc", "gta-6-pc-launch", "rockstar-pc-ports-history"],
cover=dict(eyebrow="Mods · roleplay", title="GTA 6 PC mods & FiveM", sub="Rockstar now owns the team behind FiveM.",
           rows=[("Cfx.re (FiveM)", "Owned by Rockstar", False), ("Roleplay on GTA V", "Huge on PC", False), ("GTA 6 mod support", "Not announced", True), ("Platform", "PC first", False)]),
body="""
<h2>Why PC matters for mods</h2>
<p>Consoles don't allow mods for GTA. On PC, GTA V became a platform for graphics overhauls, new cars, new missions and, most of all, roleplay servers where players act out life in Los Santos. Roleplay streams have been some of the most-watched GTA content on Twitch for years.</p>

<h2>Rockstar bought FiveM's team</h2>
<p>In August 2023, Rockstar announced that Cfx.re, the team behind FiveM for GTA V and RedM for Red Dead Redemption 2, had officially joined Rockstar. Those platforms run the custom multiplayer servers that most GTA roleplay happens on.</p>
<p>Rockstar said the move was about supporting the roleplay community. Nobody buys a team like that for a game it's about to retire, so it's widely seen as a sign that roleplay will matter for GTA 6.</p>

<h2>What we don't know</h2>
<ul>
<li>Whether GTA 6 will support mods at all on PC.</li>
<li>Whether there will be an official roleplay mode, a FiveM-style platform, or both.</li>
<li>How Rockstar will handle mods that clash with GTA 6 Online once it launches.</li>
</ul>

<h2>Be careful with "GTA 6 mods" today</h2>
<p>Since there's no PC version yet, any "GTA 6 mod" you find right now is either a GTA V mod using GTA 6 names, or a scam. Don't download "GTA 6 mod packs" that claim to unlock the game on PC. See our <a href="../gta-6-pc-download-scams/">scam guide</a>.</p>

<h2>When will we know more?</h2>
<p>Likely when Rockstar announces the PC version, which a GamesBeat report says is targeting early 2027. Check our <a href="../gta-6-pc-release-date/">release date page</a> for updates.</p>
""",
sources=[
("Rockstar Newswire", "https://www.rockstargames.com/newswire"),
("GamesBeat: Grand Theft Auto VI's PC release is slated for Q1 2027", "https://gamesbeat.com/grand-theft-auto-vis-pc-release-is-slated-for-q1-2027/"),
],
),
dict(
slug="rockstar-pc-ports-history",
short="Rockstar PC history",
title="Every Rockstar PC Port and What It Says About GTA 6 on PC",
h1="Every Rockstar PC port, and what it says about GTA 6",
desc="From GTA IV to Red Dead Redemption 2, here's how long Rockstar's PC versions took, how they launched, and what that history suggests for GTA 6 on PC.",
kicker="History",
lede="Rockstar almost always releases on consoles first. Looking back at its PC ports shows how long PC players usually wait, and what tends to go right and wrong at launch.",
tldr="Rockstar's big games have reached PC anywhere from <strong>2 weeks to 19 months</strong> after consoles, and one, the original Red Dead Redemption, took <strong>14 years</strong>. A reported Q1 2027 date for GTA 6 would be one of Rockstar's faster big PC ports.",
related=["gta-6-pc-release-date", "gta-6-pc-launch", "gta-6-pc-vs-console"],
cover=dict(eyebrow="Rockstar history", title="Rockstar's PC ports", sub="How long PC players have waited before.",
           rows=[("Max Payne 3", "~2 weeks", False), ("L.A. Noire", "~6 months", False), ("GTA IV", "~7 months", False), ("Red Dead 2", "~13 months", False), ("GTA V", "~19 months", True)]),
body="""
<h2>The timeline</h2>
<div class="table-wrap"><table>
<tr><th>Game</th><th>Console</th><th>PC</th><th>Wait</th></tr>
<tr><td>GTA IV</td><td>April 2008</td><td>December 2008</td><td>~7 months</td></tr>
<tr><td>L.A. Noire</td><td>May 2011</td><td>November 2011</td><td>~6 months</td></tr>
<tr><td>Max Payne 3</td><td>May 2012</td><td>Late May / June 2012</td><td>~2 weeks</td></tr>
<tr><td>GTA V</td><td>September 2013</td><td>April 2015</td><td>~19 months</td></tr>
<tr><td>Red Dead Redemption 2</td><td>October 2018</td><td>November 2019</td><td>~13 months</td></tr>
<tr><td>Red Dead Redemption</td><td>May 2010</td><td>October 2024</td><td>~14 years</td></tr>
<tr><td>GTA 6</td><td>November 2026</td><td>Not announced</td><td>Q1 2027 reported</td></tr>
</table></div>

<h2>GTA IV: the rough one</h2>
<p>GTA IV's PC version was notorious for poor performance at launch and for relying on Games for Windows Live. It's still remembered as a warning about rushed ports.</p>

<h2>GTA V: late, but worth it</h2>
<p>GTA V took the longest of Rockstar's GTA ports, but it arrived as the best version of the game: higher frame rates, 4K support and the Rockstar Editor for making videos, which debuted on PC. It went on to sell for over a decade, helped by mods and roleplay.</p>

<h2>Red Dead Redemption 2: great game, bumpy launch</h2>
<p>RDR2 on PC looked fantastic and added plenty of settings, but its first days were hit by crashes and launcher problems. Rockstar patched most of it within weeks.</p>

<h2>What this means for GTA 6</h2>
<ul>
<li><strong>The wait:</strong> a Q1 2027 release would be one of Rockstar's quickest big PC ports, matching the reported plans.</li>
<li><strong>The launch:</strong> expect a strong PC version with plenty of extras, and be ready for some early bugs.</li>
<li><strong>The long run:</strong> if GTA 6 follows GTA V, PC will be where the game lives longest, thanks to mods and roleplay.</li>
</ul>
<p>More on what to expect in our <a href="../gta-6-pc-launch/">GTA 6 PC launch guide</a>.</p>
""",
sources=[
("GamesBeat: Grand Theft Auto VI's PC release is slated for Q1 2027", "https://gamesbeat.com/grand-theft-auto-vis-pc-release-is-slated-for-q1-2027/"),
("PCWorld: We guessed late 2027 for GTA 6 on PC, a report says Q1 2027", "https://www.pcworld.com/article/3260660/we-guessed-late-2027-for-gta-6-on-pc-a-report-says-q1-2027.html"),
("Rockstar Newswire", "https://www.rockstargames.com/newswire"),
],
),
]
