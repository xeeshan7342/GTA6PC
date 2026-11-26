"""Batch 3, November 26, 2026: AnyXboxX Neptune, the Xbox emulator fork in the GTA 6 PC port race, and GTA 6 VR support on PC."""

POSTS_DAILY_20261126_B3 = [
dict(
slug="anyxboxx-neptune-gta-6-pc-port",
short="AnyXboxX Neptune",
title="AnyXboxX Neptune: The Xbox Emulator Fork Running GTA 6 at 14 to 17 FPS on PC",
h1="What is AnyXboxX Neptune, and how far has it got with GTA 6 on PC?",
desc="AnyXboxX is the Xbox Series X emulator fork in the GTA 6 PC port race. Its Neptune build reports 14 to 17 fps on an RTX 4070 SUPER, but it needs 32 GB of memory and the leaked Xbox build to run at all.",
kicker="PC ports",
lede="AnyXboxX is the quietest project near the top of the GTA 6 PC port race. It is not a fork chasing frame rates in public. It is a prototype Xbox Series X emulator that builds on VIctory's code, and on November 25 it moved to a packaged edition it calls Neptune. Its own README reports 14 to 17 frames per second in the game world on an RTX 4070 SUPER, with a median of 13.7. Nothing about it is playable yet, and two outside runs disagree with its numbers, but it is the only project in the race that approaches the problem as emulation first.",
img_alt="GTA 6 PC port poster for AnyXboxX Neptune, reporting 14 to 17 fps on an RTX 4070 SUPER",
tldr="AnyXboxX is a prototype Xbox Series X emulator built on VIctory's code. Its Neptune edition reports <strong>14 to 17 fps</strong> in the game world on an RTX 4070 SUPER, with a median of 13.7. It is in-game but <strong>not playable</strong>, it needs the leaked Xbox build, and its own README says a 32 GB machine is short of memory.",
faq=[("What is AnyXboxX?", "AnyXboxX is a prototype Xbox Series X emulator that builds on VIctory's compatibility-layer code. It can run console code directly on the host CPU or inside the Unicorn CPU emulator in an isolated mode. On November 25, 2026 it moved to a packaged edition of VIctory it calls Neptune."), ("How fast does AnyXboxX run GTA 6?", "Its README reports about 14 to 17 frames per second in the game world on an RTX 4070 SUPER with default settings, a median of 13.7 over 7 minutes and 13.8 over automated 13-minute runs without a crash. A mode that favours the picture runs at about 7 to 9 fps. Two outside runs are on record and neither is verified."), ("What PC do you need to run AnyXboxX?", "More than most people have. Its README says a 32 GB machine is short of memory and a 12 GB graphics card runs out of texture room. The frame rate also dips to 1 to 6 fps while the world streams in. The project is tested on Windows and Linux, on NVIDIA and AMD cards."), ("Is AnyXboxX playable?", "No. The PortWatch tracker rates it 2 steps short of its playable bar, which is 20 frames per second with 30 minutes without a crash. It is in-game at stage 6 of 7, with even stand-in light indoors and some parts missing."), ("Can I download AnyXboxX and play GTA 6 on PC?", "No. AnyXboxX is open-source code, not a game download, and it needs the leaked Xbox build to run at all. There is no legitimate GTA 6 download for PC, and sites offering one are scams.")],
body="""
<h2>What AnyXboxX is</h2>
<p>Most of the projects in the GTA 6 PC port race are compatibility layers. VIctory, the project that started the race, builds a fake Xbox around the leaked Xbox build: a loader, shims for the console libraries a PC does not have, and a fake Direct3D device that records draw commands and replays them through Vulkan. Leonida took the recompilation route, translating the game's code so it runs natively. AnyXboxX is different from both. Notebookcheck describes it as a prototype Xbox Series X emulator, and that is the honest label. It can run console code directly on the host CPU, because the Xbox Series X uses the same x86-64 instruction set as a PC, or inside the Unicorn CPU emulator in an isolated mode.</p>
<p>That approach gives it a different set of problems. Before the missing executable surfaced, AnyXboxX inventoried the leaked package and found 103 of the 104 expected files, with only the main executable missing. Its shader work so far covers a Microsoft ray-tracing library shipped with the game rather than the game's own shaders. Its research notes add that the game's mesh shaders carry no root signatures, the tables that map shaders to their resources, and that those sit inside the missing executable. In other words, the emulator could see the files before it could run them, and some of what it needs to draw the game correctly was locked inside the one file Cyberleek held back.</p>

<h2>What changed on November 25: Neptune</h2>
<p>On November 25, AnyXboxX moved to a packaged edition of VIctory it calls Neptune. The tracker that reads each project's README every 15 minutes puts it plainly: AnyXboxX builds on VIctory's code, is kept in its own repository, and moved on November 25 to a packaged edition it calls Neptune. The tracker adds that Neptune's author has no public contact, which is worth knowing, because it means nobody outside the project can ask what changed or check the packaging.</p>
<p>The README updated at 23:53 UTC on November 25 reports about 14 to 17 frames a second in the game world on an RTX 4070 SUPER with its default settings, a median of 13.7 over 7 minutes and 13.8 over automated 13-minute runs without a crash. A mode that favours the picture over speed runs at about 7 to 9. Those are the project's own measurements on its own machines, and the tracker notes them as such. Two outside runs are on record and neither is verified: a reader's 12-minute run on an RTX 4090 with earlier settings measured a median of 2 that rose to about 7 in its last two minutes, and a launcher project's 10-minute run of an earlier build on an RTX 4060 with 8 GB reported about 14. The gap between those two runs is the whole story of this race in miniature: same project, different machines, different builds, different numbers.</p>

<h2>How AnyXboxX compares on November 26</h2>
<p>Here is where the leading public builds stand as the tracker reads their READMEs on November 26. Every figure is self-reported, from one machine, and none of it has been reproduced by a second machine.</p>
<div class="table-wrap"><table>
<tr><th>Project</th><th>Reported speed</th><th>Hardware</th><th>Session</th></tr>
<tr><td>AnyXboxX (Neptune)</td><td>14 to 17 fps, median 13.7</td><td>RTX 4070 SUPER</td><td>13-minute runs, no crash</td></tr>
<tr><td>VIctory-7900XTX</td><td>13 to 17 fps in a city street, about 19 with patches off by default</td><td>RX 7900 XTX</td><td>41 minutes, reported Nov 25</td></tr>
<tr><td>victory-fork</td><td>8 to 9.5 fps at the boat mission, 10 to 14 in lighter views</td><td>RTX 4070</td><td>Up to 49 minutes, then the card is lost</td></tr>
<tr><td>DexNom RayTime</td><td>3.5 to 4 fps, about 1 with ray tracing</td><td>RX 7900 XTX</td><td>No session length reported</td></tr>
</table></div>
<p>Our <a href="../gta-6-pc-port-ray-tracing-dexnom/">ray tracing report</a> covers DexNom RayTime, the first fork to run the game's ray tracing, and our <a href="../gta-6-pc-port-race-victory-xcl/">port race report</a> covers VIctory, XCL and the other projects chasing a playable build.</p>
<p>Two things stand out. First, AnyXboxX is the fastest NVIDIA result in the table that comes with a clean no-crash run attached, even if the run is only 13 minutes. Second, it is the only project in the leading group that runs on Linux as well as Windows, and on AMD cards as well as NVIDIA, which matters for anyone hoping this work spreads beyond one graphics card.</p>

<h2>The memory problem</h2>
<p>The README is blunt about the cost. It says a 32 GB machine is short of memory and a 12 GB card runs out of texture room, with dips to 1 to 6 frames a second while the world streams in. That is the number that decides whether a frame rate is real. A median of 13.7 over 7 minutes means little if the game stalls to 1 fps every time you drive into a new district.</p>
<p>It is not alone. Vice-Tay, another fork rebuilt on November 26, says the frame rate fell from about 20 to under 10 as the game's memory grew from 33 to 52 GB, past the 43 GB its PC has. The pattern is consistent across the race: these builds hold tens of gigabytes in memory, and a normal gaming PC with 16 or 32 GB of RAM and a 12 GB card is below what they need. AnyXboxX saying so in its README is more useful than the headline frame rate, because it tells you what to buy if you want to reproduce the result, and it tells most readers they cannot.</p>

<h2>What the picture looks like</h2>
<p>The tracker rates AnyXboxX at picture 3 of 5: lit in light and shade, with visible faults. Its words are even stand-in light indoors, with some parts missing. The stand-in light is the same compromise every leading fork makes. The game's ray-traced lighting does not run in these builds, so the projects fake the ambient light and the picture looks right in sunlight and wrong in shadow. DexNom RayTime is the one exception, and its ray tracing costs it nearly all of its speed. The mode that favours the picture on AnyXboxX runs at about 7 to 9 fps, which is the trade in one number: prettier, slower.</p>

<h2>Why the emulator route matters</h2>
<p>There is a reason to watch an emulator even while the compatibility layers post faster numbers. A compatibility layer has to reimplement every Xbox system call the game uses, one shim at a time, and it breaks whenever the game uses a call nobody has shimmed yet. An emulator has a different ceiling: if it can run the console's code faithfully, the game should behave like it does on the console, including the parts nobody has looked at yet. The price is speed, because emulation does more work per frame, and accuracy, because the Xbox GPU speaks a dialect of graphics that PC cards do not.</p>
<p>Neptune is a step toward the middle of that trade. It is a packaged edition of VIctory, which means AnyXboxX is now building on the compatibility layer's work instead of duplicating it, while keeping its own emulator approach. If the packaging holds, the project gets VIctory's fixes for free and keeps its own way of running the code. If it does not, it inherits VIctory's bugs too. The tracker will show which one it is within days, because it reads the README every 15 minutes.</p>

<h2>What to watch next</h2>
<p>Watch for a second machine reproducing the 14 to 17 fps figures, which would turn AnyXboxX from a claim into a baseline. Watch for a fix to the memory problem, because 32 GB being short is the number that keeps this out of reach of normal PCs. And watch for a 30-minute session at 20 fps, the tracker's playable bar, which is the first number that would mean someone actually played the game rather than watched it run.</p>
<p>Watch Take-Two as well. The publisher has already had GitHub remove Leonida and 3,006 forks, and our <a href="../take-two-shut-down-gta-6-pc-ports/">Take-Two crackdown report</a> has the full story. AnyXboxX is open-source code on GitHub, the same place Leonida lived, and the same notice could reach it. Until then, the honest summary is the one the tracker prints at the top of its page: playable, no. The emulator fork is in the game, it is fast for its approach, and it still needs leaked files that nobody can legally download.</p>
<div class="warn"><strong>Do not download anything claiming to be GTA 6 for PC.</strong> There is no legitimate download, and fake installers using the leak as bait are already circulating. The unofficial port projects are open-source code on GitHub, not game downloads, and they need leaked files to run.</div>

<h2>Quick answers</h2>
<h3>What is AnyXboxX?</h3>
<p>AnyXboxX is a prototype Xbox Series X emulator that builds on VIctory's compatibility-layer code. It can run console code directly on the host CPU or inside the Unicorn CPU emulator in an isolated mode. On November 25, 2026 it moved to a packaged edition of VIctory it calls Neptune.</p>
<h3>How fast does AnyXboxX run GTA 6?</h3>
<p>Its README reports about 14 to 17 frames per second in the game world on an RTX 4070 SUPER with default settings, a median of 13.7 over 7 minutes and 13.8 over automated 13-minute runs without a crash. A mode that favours the picture runs at about 7 to 9 fps. Two outside runs are on record and neither is verified.</p>
<h3>What PC do you need to run AnyXboxX?</h3>
<p>More than most people have. Its README says a 32 GB machine is short of memory and a 12 GB graphics card runs out of texture room. The frame rate also dips to 1 to 6 fps while the world streams in. The project is tested on Windows and Linux, on NVIDIA and AMD cards.</p>
<h3>Is AnyXboxX playable?</h3>
<p>No. The PortWatch tracker rates it 2 steps short of its playable bar, which is 20 frames per second with 30 minutes without a crash. It is in-game at stage 6 of 7, with even stand-in light indoors and some parts missing.</p>
<h3>Can I download AnyXboxX and play GTA 6 on PC?</h3>
<p>No. AnyXboxX is open-source code, not a game download, and it needs the leaked Xbox build to run at all. There is no legitimate GTA 6 download for PC, and sites offering one are scams.</p>
""",
cover=dict(eyebrow="PC ports · Nov 26", title="AnyXboxX Neptune", sub="The Xbox emulator fork runs GTA 6 at 14 to 17 fps.", rows=[("Frame rate", "14-17 fps", True), ("GPU", "RTX 4070 SUPER", False), ("Playable", "not yet", True)]),
sources=[
("GTA VI PC Race: live tracker of unofficial PC ports", "https://vuyp.github.io/gta6-pc-race/"),
("Notebookcheck: Can Cyberleek's leaked GTA 6 Xbox build become a PC port?", "https://www.notebookcheck.net/Can-Cyberleek-s-leaked-GTA-6-Xbox-build-become-a-PC-port-Three-GitHub-projects-are-trying-without-the-executable.1456848.0.html"),
("TweakTown: The state of GTA 6 on PC, everything you need to know", "https://www.tweaktown.com/articles/11693/the-state-of-gta-6-on-pc-everything-you-need-to-know/index.html"),
],
related=["gta-6-pc-port-race-victory-xcl", "gta-6-xbox-build-on-pc", "gta-6-pc-port-ray-tracing-dexnom"],
),
dict(
slug="gta-6-vr-pc-support",
short="GTA 6 in VR",
title="Will GTA 6 Support VR on PC? No VR Mode, No VR Mod, Only a Virtual Screen",
h1="Will GTA 6 support VR on PC?",
desc="GTA 6 has no VR mode and no VR mod, and Rockstar has announced nothing for headsets. The only way to play it in a headset today is the flat game on a virtual screen through PS VR2 Cinematic Mode or Quest Remote Play.",
kicker="VR and headsets",
lede="GTA 6 has no VR mode, no VR version and no headset support of any kind. Rockstar has announced nothing for headsets, and the only VR headset in the game's official material is a joke: a character wearing a 2019 Quest in the August Extended Look. A VR mod is no closer, because a mod needs a PC version to run on, and there is no PC version. What a headset can do today is show the flat game on a big virtual screen, and only if you already own a console.",
img_alt="GTA 6 VR support poster showing no VR mode and no VR mod, with a virtual screen as the only headset option",
tldr="GTA 6 has <strong>no VR mode</strong> and <strong>no VR mod</strong>. Rockstar has announced no headset support. The only headset option today is the flat game on a virtual screen through PS VR2 Cinematic Mode or Quest Remote Play, and every route needs a console you own.",
faq=[("Does GTA 6 have VR?", "No. GTA 6 came out on November 19, 2026 for PlayStation 5 and Xbox Series X|S as a flat game, and Rockstar has announced no VR mode, VR version or headset support. The PlayStation Store listing carries no PS VR2 label."), ("Is there a GTA 6 VR mod?", "No. A VR mod needs a version of the game modders can open up, in practice a PC one, and GTA 6 has no PC version announced. Any download promising a GTA 6 VR mod today is not real."), ("Can I play GTA 6 on a Meta Quest 3?", "Not in VR, but on a big virtual screen, yes, with a console you own. Xbox owners can stream it with Remote Play to the free Xbox app on Quest. PS5 owners can feed it through Meta's HDMI Link app and a USB capture card, with HDCP switched off."), ("Can I play GTA 6 on PS VR2?", "On a virtual screen, yes. PS VR2 Cinematic Mode shows any non-VR PS5 game on a 1920x1080 virtual screen with no setup. The TV goes dark while it is on. It is not VR support."), ("Will GTA 6 ever get VR?", "Nothing official points that way. Rockstar has shipped one VR game, L.A. Noire: The VR Case Files in 2017, and Meta's GTA San Andreas for Quest has been on hold indefinitely since August 2024. A VR mod would need a PC version first, then years of modding work, and Take-Two has sent DMCA notices over VR mods before.")],
body="""
<h2>The short answer: no VR anywhere</h2>
<p>Rockstar's official GTA VI page lists two platforms, PlayStation 5 and Xbox Series X|S, and no headset. The pre-load post Rockstar published on November 10 set out what each console gets: a 30fps target, a sharper image and ray-traced shadows on PS5 Pro, Xbox Cloud Gaming on Xbox consoles, and Remote Play on PlayStation and Xbox. It says nothing about VR or headsets. The PlayStation Store listing carries no PS VR2 label, which Sony applies to games with genuine headset support. On the Xbox side the question answers itself at the hardware level, because Microsoft sells no VR headset for Series X|S and supports none. A VR mode on Xbox is not merely unannounced. On current hardware it is impossible.</p>

<h2>The only headset in GTA 6 is a joke</h2>
<p>The single piece of official footage fuelling the VR conversation is a gag. In Grand Theft Auto VI: An Extended Look, the 26-minute video Rockstar released on August 27, 2026 and captured in-game on PlayStation 5, a character turns up around the 17:27 mark wearing what reads as a 2019 Quest, fabric front and all, at the expense of people who wear headsets indoors. Road to VR and VR.org both describe the prop as modelled on the original Oculus Quest. Rockstar did not model a Quest 3 or a Vision Pro. It reached back to the 2019 headset, the silhouette a general audience reads as slightly embarrassing. Leonida is satire, and the headset is part of the joke, not a feature announcement. There is no sign of actual VR support in GTA 6 anywhere in Rockstar's material.</p>

<h2>Why there is no VR mod yet</h2>
<p>A VR mod needs a version of the game that modders can open up. In practice that means PC, and GTA 6 exists only on PS5 and Xbox Series X|S, with no PC version announced. Any download promising a GTA 6 VR mod today is not real, so do not run it. Our <a href="../gta-6-pc-mods-fivem/">mods guide</a> explains what modders are actually waiting for.</p>
<p>The precedent says the wait is long. GTA V reached consoles in September 2013 and PC in April 2015, about nineteen months later, and its VR mod came years after that, from Luke Ross, who funds his R.E.A.L. VR mods through Patreon. In July 2022 Take-Two, Rockstar's parent company, sent a DMCA notice over his GTA V, Red Dead Redemption 2 and Mafia VR mods, and Road to VR reported that he took them down to comply. CD Projekt did the same to his Cyberpunk 2077 mod in January 2026, which PC Gamer covered. So even after a PC version arrives, a GTA 6 VR mod would need years of work, and it would face a publisher that has already acted against VR mods once.</p>

<h2>Rockstar and VR: a short history</h2>
<p>Rockstar has shipped exactly one VR game. L.A. Noire: The VR Case Files, seven cases from L.A. Noire rebuilt for roomscale VR, launched on Steam on December 15, 2017. It has not shipped another. Red Dead Redemption 2 shipped without VR. GTA 6 ships without it.</p>
<p>The other GTA in VR never shipped either. Meta announced Grand Theft Auto: San Andreas for Quest 2 in October 2021, and UploadVR reported on August 15, 2024 that Meta had put it on hold indefinitely. In August 2026 a modder released an early San Andreas VR source kit for Quest 3 that ships no game files and needs your own copy of the game. That is the closest thing to a GTA VR release in five years, and it is a fan kit for a 2004 game, not a Rockstar product.</p>

<h2>How to play GTA 6 in a headset today</h2>
<p>Every route shows the flat game on a virtual screen, and every route starts with a console you own. None of this is VR, and none of it is a reason to buy a headset for GTA 6. If you already own one, it is a private screen bigger than the TV.</p>
<div class="table-wrap"><table>
<tr><th>Route</th><th>What you need</th><th>Extra cost</th></tr>
<tr><td>PS VR2 Cinematic Mode</td><td>PS5 and PS VR2</td><td>None</td></tr>
<tr><td>Quest plus Xbox Remote Play</td><td>Xbox Series X|S, a Quest, a gamepad, the free Xbox app</td><td>None if you own a gamepad</td></tr>
<tr><td>Quest plus PS5 via HDMI Link</td><td>PS5, a Quest, a USB capture card, HDCP off on the PS5</td><td>The capture card</td></tr>
</table></div>
<p>Each route puts a 1080p picture in the headset. PS VR2 owners have the simplest route: Cinematic Mode needs no setup and runs over the headset's own cable, though Sony turns the TV off while it is in use. On a Quest, Xbox Remote Play is free, and it worked with GTA 6 from day one. The PS5 route goes through Meta's HDMI Link app and a capture card, and the card shows nothing until HDCP is switched off in the PS5's HDMI settings. The difference between consoles mostly disappears at 1080p, so pick the route by the console you own.</p>

<h2>Cloud streaming will not help a headset</h2>
<p>Microsoft's Xbox Wire post puts GTA 6 on Xbox Cloud Gaming from day one on Xbox One and Xbox Series X|S, using Series S graphics settings, and names no other devices. Windows Central, which played it over the cloud at launch, found it blocked on PC and mobile. The Xbox app on Quest is not on Microsoft's list, although Xbox's page for VR headsets says the app can stream select games you own. Microsoft has not said whether GTA 6 will become one of them. Until then, a Quest needs a console in the house. Our <a href="../gta-6-pc-geforce-now-cloud-gaming/">cloud gaming guide</a> covers the console-only limits in full.</p>
<p>Sony added cloud streaming on November 23. GTA 6's PlayStation Store page now lists streaming support, and owners with PS Plus Premium can stream it from Sony's servers to a PS5 or a PlayStation Portal. You still have to own the game. Neither company lists a Quest, so the answer for a headset has not changed: it starts with a console you own.</p>

<h2>What would have to change</h2>
<p>Three things would have to happen, in order. First, Rockstar would have to announce a PC version. Take-Two's chief executive has said that information about new versions always comes from Rockstar, so the announcement will come from there or not at all. Our <a href="../gta-6-pc-release-date/">release date page</a> tracks the status. Second, modders would need years with that PC version to build a VR mod on the scale of Luke Ross's GTA V work. Third, Take-Two would have to leave it alone, which its July 2022 DMCA notice makes doubtful.</p>
<p>There is also a hardware reason to be sceptical. GTA 6 runs at 30 frames per second on every console, PS5 Pro included, with no 40 or 60fps mode. Rockstar told Kotaku the Pro's processor is not powerful enough to run the game's complex simulation at higher frame rates. VR needs high, steady frame rates to feel right, and a game locked at 30fps on consoles would need a PC version with serious headroom before a headset made sense. Until a PC version exists, there is no VR route of any kind, and the honest advice is to plan for a flat screen.</p>
<div class="warn"><strong>Do not download anything promising a GTA 6 VR mod.</strong> There is no VR mod and no PC version for one to run on. Fake installers using the leak and the VR rumour as bait are already circulating.</div>

<h2>Quick answers</h2>
<h3>Does GTA 6 have VR?</h3>
<p>No. GTA 6 came out on November 19, 2026 for PlayStation 5 and Xbox Series X|S as a flat game, and Rockstar has announced no VR mode, VR version or headset support. The PlayStation Store listing carries no PS VR2 label.</p>
<h3>Is there a GTA 6 VR mod?</h3>
<p>No. A VR mod needs a version of the game modders can open up, in practice a PC one, and GTA 6 has no PC version announced. Any download promising a GTA 6 VR mod today is not real.</p>
<h3>Can I play GTA 6 on a Meta Quest 3?</h3>
<p>Not in VR, but on a big virtual screen, yes, with a console you own. Xbox owners can stream it with Remote Play to the free Xbox app on Quest. PS5 owners can feed it through Meta's HDMI Link app and a USB capture card, with HDCP switched off.</p>
<h3>Can I play GTA 6 on PS VR2?</h3>
<p>On a virtual screen, yes. PS VR2 Cinematic Mode shows any non-VR PS5 game on a 1920x1080 virtual screen with no setup. The TV goes dark while it is on. It is not VR support.</p>
<h3>Will GTA 6 ever get VR?</h3>
<p>Nothing official points that way. Rockstar has shipped one VR game, L.A. Noire: The VR Case Files in 2017, and Meta's GTA San Andreas for Quest has been on hold indefinitely since August 2024. A VR mod would need a PC version first, then years of modding work, and Take-Two has sent DMCA notices over VR mods before.</p>
""",
cover=dict(eyebrow="VR · Nov 26", title="GTA 6 in VR?", sub="No VR mode and no VR mod. A headset shows the flat game only.", rows=[("VR mode", "none", True), ("VR mod", "no route yet", False), ("In a headset", "virtual screen", True)]),
sources=[
("VR.org: GTA 6 VR, VR mode, VR mod and PC version status", "https://vr.org/gta-6-vr"),
("GTA Snaps: Is GTA 6 Coming to VR? Every claim checked", "https://gtasnaps.com/is-gta-6-coming-to-vr/"),
("AR VR Tips: GTA 6 on Meta Quest and Steam Frame, how to play in VR", "https://arvrtips.com/gta-6-on-meta-quest-steam-frame/"),
],
related=["gta-6-pc-release-date", "gta-6-pc-mods-fivem", "gta-6-pc-geforce-now-cloud-gaming"],
),
]
