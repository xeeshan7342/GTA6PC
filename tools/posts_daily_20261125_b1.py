"""Batch 1, November 25, 2026: GTA 6 reaches in-game rendering on PC, and how to read the Portwatch tracker."""

POSTS_DAILY_20261125_B1 = [
dict(
slug="gta-6-pc-port-in-game-rendering",
short="In-game on PC",
title="GTA 6 Reaches In-Game Rendering on PC, a Day After the Xbox Executable Leak",
h1="GTA 6 reaches in-game rendering on PC",
desc="One day after the missing GTA 6 Xbox executable leaked, the unofficial PC port projects moved past the menus. VIctory now renders in-game graphics, and a private build called CGBJ reportedly lets a player move and talk to NPCs. Nothing is playable yet.",
kicker="PC ports",
lede="The unofficial race to run GTA 6 on PC took its biggest step yet on November 24, 2026. One day after the missing Xbox executable leaked, the compatibility project VIctory moved past the menus and started rendering the game world, and a private build called CGBJ reportedly reached actual in-game movement. The progress is real, and so are its limits: the game runs at about 1 frame per second, most of the scene is missing, and nothing here is playable.",
img_alt="GTA 6 PC port poster showing first in-game rendering with menus at 30 fps and in-game frames at about 1 fps",
tldr="Unofficial PC port projects have moved past the menus. <strong>VIctory</strong> now renders in-game graphics from the leaked Xbox build, with menus at <strong>30 fps</strong> and in-game frames at roughly <strong>0.6 to 2 fps</strong>. A private build called <strong>CGBJ</strong> reportedly goes further, with a player moving and talking to NPCs. There is still <strong>no verified playable build</strong> of GTA 6 on PC.",
faq=[("Has GTA 6 reached in-game on PC?", "Reportedly, yes, in a limited sense. The VIctory project renders in-game graphics from the leaked Xbox build, and a private build called CGBJ reportedly lets a player move and talk to NPCs. Most of the scene is missing, the frame rate is about 1 fps, and nothing is playable."), ("What is VIctory?", "VIctory is an open-source compatibility layer that runs the Xbox Series X|S build of GTA 6 on Windows. It executes the game's original x86-64 code directly and reimplements console system functions while translating GPU shaders to DirectX Intermediate Language (DXIL)."), ("What is CGBJ?", "CGBJ is a private build based on VIctory, using some work from the XCL project. It reportedly reaches in-game, with controller movement, NPC interaction and an open in-game menu. It is not public and cannot be downloaded."), ("Can I play GTA 6 on PC now?", "No. No project has a verified playable build. The furthest public progress is a loaded world that renders at roughly 0.6 to 2 frames per second, with most of the scene missing and frequent GPU hangs."), ("Is it safe to download a GTA 6 PC port?", "No. There is no legitimate GTA 6 PC download. Files claiming to be a working port are usually fake installers or malware, and the leaked build itself carries legal risk. Do not download anything claiming to be GTA 6 for PC.")],
body="""
<h2>What happened on November 24</h2>
<p>On November 24, 2026, TweakTown reported that unofficial GTA 6 PC projects had moved beyond the menus, with newly shared footage showing early 3D environments and partially working shaders. The step came just one day after Cyberleek released the missing executable for the leaked Xbox build on November 23, the file modders needed before any of the game's code could run on Windows at all.</p>
<p>XDA Developers reported the same day that VIctory, the most promising of the new projects, had not only booted the game on PC but was rendering in-game graphics. Clips shared on social media showed the game booting, menus running at 30 frames per second, and some of the early cutscenes rendering. XDA noted it had not independently verified the clips.</p>
<p>That is a genuine step past where the race stood a day earlier, when modders had only reached the settings screens. Our <a href="../gta-6-boots-on-pc-executable-leak/">boot report</a> covers that first milestone, and our <a href="../gta-6-pc-port-race-victory-xcl/">port race report</a> covers the projects that picked up the work after Leonida shut down.</p>

<h2>The numbers from VIctory's test</h2>
<p>According to VIctory's November 23 development update, reported by TweakTown, testing on a Windows 11 PC with an AMD Radeon RX 6700 XT graphics card showed menus running at 30 frames per second, working save functionality, and intro video playback with audio. The project loads into the game world in about 50 seconds and reaches the first mission's introductory sequence.</p>
<p>Past that point, the picture changes sharply. Most of the scene still fails to render, and individual frames take between 0.5 and 1.8 seconds to draw, which works out to roughly 0.6 to 2 frames per second. Entering the game world can also cause GPU hangs and display driver resets. In other words, the game loads, but it does not play.</p>
<div class="table-wrap"><table>
<tr><th>What VIctory reports</th><th>Status on November 24</th></tr>
<tr><td>Boots on Windows</td><td>Yes</td></tr>
<tr><td>Menus</td><td>30 fps</td></tr>
<tr><td>Intro video with audio</td><td>Yes</td></tr>
<tr><td>Saves and profiles</td><td>Working</td></tr>
<tr><td>Loads into the game world</td><td>Yes, in about 50 seconds</td></tr>
<tr><td>In-game rendering</td><td>Partial, most of the scene missing</td></tr>
<tr><td>In-game frame rate</td><td>About 0.6 to 2 fps</td></tr>
<tr><td>Player control</td><td>Not in the public build</td></tr>
</table></div>
<p>VIctory works by running the Xbox build's original x86-64 code directly on Windows, reimplementing the console-only functions the game calls, and translating its GPU shaders into DirectX Intermediate Language (DXIL) for Direct3D 12. That is the same idea as Leonida in spirit, but Leonida translated shaders to SPIR-V for Vulkan instead. The shared x86-64 processor design between Xbox Series X|S and modern PCs is why this progress came so fast: there is no processor to emulate, only console graphics and system functions to rebuild.</p>

<h2>CGBJ: the private build that went further</h2>
<p>DSOGaming reported on November 24 that a private build called CGBJ has gone further than any public project. CGBJ is based on VIctory and uses some work from XCL, and it reportedly reaches in-game: a player can move with a controller, talk to NPCs, and open the in-game menu.</p>
<p>The limits are still severe. PortWatch lists the build at about 4 frames per second, with no lighting yet, and the graphics are flat-colored and mostly untextured, according to the tracker that XDA cites for the claim. DSOGaming itself urges readers to take the report with a grain of salt, noting that PortWatch has reportedly confirmed it but that the footage could still be fake. A separate clip shared on Reddit, showing partially working shaders, character models and environmental rendering, comes from yet another private project, according to TweakTown, and may eventually be folded into one of the public projects or released on its own.</p>
<p>CGBJ is private and cannot be downloaded. There are no public releases of VIctory or XCL either, though both projects are open source and can be built from their GitHub pages by people who want to try.</p>

<h2>The five projects, and where each stands</h2>
<p>DSOGaming counts five major efforts in the race. Here is where each one reportedly stands as of November 24.</p>
<div class="table-wrap"><table>
<tr><th>Project</th><th>Approach</th><th>Reported status</th></tr>
<tr><td>CGBJ</td><td>Private build on VIctory, with XCL work</td><td>In-game: movement, NPC talk, menu, about 4 fps, no lighting</td></tr>
<tr><td>VIctory</td><td>Open-source compatibility layer</td><td>Menus at 30 fps, early in-game rendering at 0.6 to 2 fps</td></tr>
<tr><td>XCL</td><td>Open-source Wine-style layer</td><td>Menus at 30 fps, crashes on the way in-game</td></tr>
<tr><td>Xbox2Windows</td><td>Compatibility layer</td><td>Boots, shows a first frame</td></tr>
<tr><td>TuxBox</td><td>Compatibility layer</td><td>Boots, shows a first frame</td></tr>
</table></div>
<p>Leonida, the static recompilation project that led the race for its first three days, is no longer in active development after its developer stepped away and its pages went down. Our <a href="../gta-6-pc-port-rockstar-crackdown/">crackdown report</a> has the full story.</p>

<h2>How Portwatch scores the race</h2>
<p>Portwatch is a live tracker that scores every project on one shared scale. TweakTown reports VIctory at 67 percent, and the leading project at 72 percent. The scale is not linear: 55 percent means the main menu, 70 percent means in-game, 85 percent means 30 fps, and 100 percent means stable. The jump from in-game to a stable 30 fps is the long part of the race, and the tracker notes the last stretch will need much more development time. Our <a href="../gta-6-pc-port-tracker-portwatch/">Portwatch guide</a> explains how to read the tracker and what each milestone means.</p>

<h2>Why it still is not playable</h2>
<p>Despite the headlines, TweakTown's conclusion is blunt: no verified, fully playable public build of GTA 6 for PC exists. The public projects crash when they try to reach the game world, and the private build that gets there runs at about 4 frames per second with no lighting. The game also has a watchdog timer that ends the process roughly 30 seconds after the world loads, which the projects are still working around.</p>
<p>The next milestone is not a higher number on a tracker. It is correct, artifact-free visuals at a frame rate a person could actually play at, and DSOGaming says that is now the big question for every project in the race.</p>

<h2>The dump problem nobody has solved</h2>
<p>There is still no known way for Xbox Series X|S owners on up-to-date firmware to extract their own decrypted copy of GTA 6, according to XDA. All of the port work is being done on the leaked copy, which means these projects cannot grow into something ordinary players can use legally. Anyone offering a ready-made download is either sharing leaked files or, more often, running a scam. Our <a href="../gta-6-pc-download-scams/">download scams guide</a> explains the risks in detail.</p>

<h2>What to watch next</h2>
<p>DSOGaming expects XCL and VIctory to close on CGBJ within hours or days, because the projects share work and crash at the same wall. Watch for a public project reaching the game world without crashing, for lighting and textures appearing in footage, and for the frame rate climbing out of single digits. Until then, every "GTA 6 on PC" video deserves the same check: is it on the tracker, is there code behind it, and has anyone independent confirmed it?</p>
<div class="warn"><strong>Do not download anything claiming to be GTA 6 for PC.</strong> There is no legitimate download, and fake installers using the leak as bait are already circulating. The unofficial port projects are open-source code on GitHub, not game downloads, and they need leaked files to run.</div>

<h2>Quick answers</h2>
<h3>Has GTA 6 reached in-game on PC?</h3>
<p>Reportedly, yes, in a limited sense. VIctory renders in-game graphics, and the private build CGBJ reportedly lets a player move and talk to NPCs. Most of the scene is missing, the frame rate is about 1 fps, and nothing is playable.</p>
<h3>What is VIctory?</h3>
<p>VIctory is an open-source compatibility layer that runs the Xbox Series X|S build of GTA 6 on Windows. It executes the game's original x86-64 code directly and reimplements console system functions while translating GPU shaders to DirectX Intermediate Language (DXIL).</p>
<h3>What is CGBJ?</h3>
<p>CGBJ is a private build based on VIctory, using some work from the XCL project. It reportedly reaches in-game, with controller movement, NPC interaction and an open in-game menu. It is not public and cannot be downloaded.</p>
<h3>Can I play GTA 6 on PC now?</h3>
<p>No. No project has a verified playable build. The furthest public progress is a loaded world that renders at roughly 0.6 to 2 frames per second, with most of the scene missing and frequent GPU hangs.</p>
<h3>Is it safe to download a GTA 6 PC port?</h3>
<p>No. There is no legitimate GTA 6 PC download. Files claiming to be a working port are usually fake installers or malware, and the leaked build itself carries legal risk. Do not download anything claiming to be GTA 6 for PC.</p>
""",
cover=dict(eyebrow="Port update · Nov 24", title="GTA 6 Renders In-Game on PC", sub="Menus at 30 fps, a loaded world, but 0.6 to 2 fps in-game.", rows=[("In-game", "first visuals", True), ("Menu frame rate", "30 fps", False), ("In-game fps", "0.6-2 fps", True)]),
sources=[
("TweakTown: GTA 6 reportedly reaches in-game rendering on PC just a day after Xbox executable leak", "https://www.tweaktown.com/news/114853/gta-6-reportedly-reaches-in-game-rendering-on-pc-just-a-day-after-xbox-executable-leak/index.html"),
("XDA: An unofficial GTA 6 PC port is making progress, and developers have the first in-game visuals to show for it", "https://www.xda-developers.com/unofficial-gta-6-pc-port-making-progress-developers-have-first-in-game-visuals/"),
("DSOGaming: Grand Theft Auto 6 unofficial PC port CGBJ now reaches in-game", "https://www.dsogaming.com/news/grand-theft-auto-6-unofficial-pc-port-cgbj-now-reaches-in-game/"),
],
related=["gta-6-boots-on-pc-executable-leak", "gta-6-pc-port-race-victory-xcl", "gta-6-pc-download-scams"],
),
dict(
slug="gta-6-pc-port-tracker-portwatch",
short="Port tracker",
title="GTA 6 PC Port Tracker: How Portwatch Scores the Race to Play on PC",
h1="How to follow the GTA 6 PC port race with Portwatch",
desc="Portwatch is a live scoreboard for every unofficial attempt to run GTA 6 on PC. Here is how its scale works, what each milestone means, which projects it tracks, and how to tell a real milestone from a fake download.",
kicker="Guides",
lede="Every few hours, the unofficial race to run GTA 6 on PC moves, and the claims move faster than the code. Portwatch is the community scoreboard that tracks it all in one place: which projects have booted the game, which have reached the menus, and which have rendered the world. Here is how to read it, what its numbers actually mean, and what it cannot tell you.",
img_alt="GTA 6 PC port tracker poster showing Portwatch scores with CGBJ at 72 percent and VIctory at 67 percent",
tldr="<strong>Portwatch</strong> is a live tracker that scores every unofficial GTA 6 PC port project on one scale, from first boot to stable 30 fps. As of November 24, the leader is the private build <strong>CGBJ at 72 percent</strong>, with the open-source project <strong>VIctory at 67 percent</strong>. The tracker lists milestones and sources, but it hosts <strong>no downloads</strong> and no project on it is playable yet.",
faq=[("What is Portwatch?", "Portwatch is a community-run live scoreboard at portwatch-vi.xyz that tracks every serious attempt to run the leaked GTA 6 Xbox build on PC. It scores each project on one shared scale and links to the evidence behind each milestone."), ("How does Portwatch score progress?", "On a scale where 55 percent means the main menu, 70 percent means in-game, 85 percent means 30 fps, and 100 percent means stable. The scale is not linear, so the last stretch takes far longer than the first."), ("Which project is leading?", "As of November 24, 2026, the private build CGBJ leads at 72 percent, reportedly in-game. The leading open-source project is VIctory at 67 percent, with menus at 30 fps and early in-game rendering."), ("Can I download a GTA 6 PC port from Portwatch?", "No. Portwatch hosts no game files and links to no downloads. Projects like VIctory and XCL are open source and can be built from their GitHub pages, but they need the leaked Xbox build to run, which carries legal risk."), ("How do I know a port claim is real?", "Check whether Portwatch lists it with a source, whether the project's GitHub page shows matching commits, and whether independent outlets have reported it. A claim with no tracker entry, no code and only a short video is not verified.")],
body="""
<h2>What Portwatch is</h2>
<p>Portwatch is a community-run live scoreboard for the unofficial race to run GTA 6 on PC. Its site, portwatch-vi.xyz, tracks every serious attempt to recompile, emulate or port the leaked Xbox Series X|S build to PC, and scores each one on a single shared scale. TweakTown describes it as the tracker that monitors the whole race, and XDA cites its numbers when reporting which project is ahead.</p>
<p>The tracker exists because the race moves fast and the claims move faster. In the first two days after the executable leaked, five projects appeared, one shut down, and a private build reportedly went from menus to in-game. Portwatch puts each claim in one place with the evidence behind it, so readers can check a headline against the tracker's own list instead of taking a video at its word.</p>

<h2>How the scale works</h2>
<p>Portwatch scores progress from 0 to 100 percent, but the scale is not linear. The milestones are spaced out so that the hard parts count for more than the easy ones.</p>
<div class="table-wrap"><table>
<tr><th>Score</th><th>Milestone</th><th>What it means</th></tr>
<tr><td>55%</td><td>Main menu</td><td>The game boots and its menus run</td></tr>
<tr><td>70%</td><td>In-game</td><td>The game world loads and renders, even badly</td></tr>
<tr><td>85%</td><td>30 fps</td><td>The game holds 30 frames per second in-game</td></tr>
<tr><td>100%</td><td>Stable</td><td>The game runs reliably at playable performance</td></tr>
</table></div>
<p>The gap between 70 and 85 percent is the whole race. Getting a world to load is one job; getting it to render correctly, with lighting, textures and a steady frame rate, is a much bigger one. TweakTown notes the last stretch will likely need much more development time, effort and AI tokens. A project can sit at 72 percent for a long time while the work underneath it barely moves.</p>

<h2>Where the race stands on November 24</h2>
<p>Here is what the tracker reported on November 24, 2026. Scores move daily, so check the live page for the current numbers.</p>
<div class="table-wrap"><table>
<tr><th>Project</th><th>Score</th><th>Milestone</th><th>Public?</th></tr>
<tr><td>CGBJ</td><td>72%</td><td>In-game</td><td>No, private build</td></tr>
<tr><td>VIctory</td><td>67%</td><td>Past the main menu, early in-game rendering</td><td>Yes, open source</td></tr>
<tr><td>XCL</td><td>Menu stage</td><td>Menus at 30 fps</td><td>Yes, open source</td></tr>
<tr><td>Xbox2Windows</td><td>Early</td><td>Boots, first frame</td><td>Yes</td></tr>
<tr><td>TuxBox</td><td>Early</td><td>Boots, first frame</td><td>Yes</td></tr>
</table></div>
<p>CGBJ leads because it reportedly gets a player moving and talking to NPCs, even at about 4 frames per second with no lighting. VIctory is the leading public project: menus at 30 fps, saves working, and early in-game rendering at roughly 0.6 to 2 frames per second. Our <a href="../gta-6-pc-port-in-game-rendering/">in-game rendering report</a> has the full details on both.</p>

<h2>What each milestone actually means</h2>
<p>A milestone on Portwatch is a technical checkpoint, not a promise that the game is close to playable. Here is how to read the four big ones.</p>
<p><strong>Main menu (55 percent).</strong> The game boots and its menus respond. This is where most projects spent their first day. It proves the executable runs, but it says nothing about the game world.</p>
<p><strong>In-game (70 percent).</strong> The world loads and something renders. At this stage the image is usually flat, unlit and missing most of its detail, and the frame rate is measured in seconds per frame. CGBJ reached this with a player moving and talking to NPCs, but at about 4 frames per second.</p>
<p><strong>30 fps (85 percent).</strong> The game holds 30 frames per second inside the world. No project is close to this yet. This is the milestone that would turn a demo into something a person could watch, though not necessarily play.</p>
<p><strong>Stable (100 percent).</strong> The game runs reliably, with working graphics, audio, input and saves. Nothing in the race is near this, and the tracker is clear that the last stretch is the longest.</p>

<h2>What Portwatch does not do</h2>
<p>Portwatch is a scoreboard, not a download site. It hosts no game files, links to no downloads, and offers no playable build of GTA 6. The projects it tracks are code on GitHub, and they need the leaked Xbox build to run at all. There is still no known way to dump the game from an Xbox on current firmware, so the work depends on leaked files, which carries legal risk.</p>
<p>The tracker also does not verify every claim itself. DSOGaming, reporting on the CGBJ in-game claim, noted that PortWatch had reportedly confirmed it, while urging readers to take the footage with a grain of salt. XDA was careful in the same way, saying it had not independently verified the clips it reported on. Treat a tracker entry as a lead, not a verdict.</p>

<h2>How to spot a fake milestone</h2>
<p>The port race has become a magnet for fake videos and download scams, and the tracker is only useful if you read it skeptically. A claim is worth believing when several of these check out.</p>
<ul>
<li>The project is listed on Portwatch with a milestone and a source, not just a video.</li>
<li>The project's GitHub page shows commits that match the claim, with recent activity from more than one contributor.</li>
<li>An established outlet such as TweakTown, XDA or DSOGaming has reported the same milestone.</li>
<li>The footage shows the game's own screens, menus or world, and not a recycled clip from GTA 5.</li>
</ul>
<p>Walk away when a claim has no tracker entry, no public code, and only a short video; when it asks you to download an installer, a "port" or a "crack"; or when it promises a playable game today. Every one of those is a known scam pattern, and our <a href="../gta-6-pc-download-scams/">download scams guide</a> lists them in detail.</p>
<div class="warn"><strong>Do not download anything claiming to be GTA 6 for PC.</strong> Portwatch itself hosts nothing to download. Any site using the tracker's name or numbers to sell you a download is using the race as bait.</div>

<h2>Quick answers</h2>
<h3>What is Portwatch?</h3>
<p>Portwatch is a community-run live scoreboard at portwatch-vi.xyz that tracks every serious attempt to run the leaked GTA 6 Xbox build on PC. It scores each project on one shared scale and links to the evidence behind each milestone.</p>
<h3>How does Portwatch score progress?</h3>
<p>On a scale where 55 percent means the main menu, 70 percent means in-game, 85 percent means 30 fps, and 100 percent means stable. The scale is not linear, so the last stretch takes far longer than the first.</p>
<h3>Which project is leading?</h3>
<p>As of November 24, 2026, the private build CGBJ leads at 72 percent, reportedly in-game. The leading open-source project is VIctory at 67 percent, with menus at 30 fps and early in-game rendering.</p>
<h3>Can I download a GTA 6 PC port from Portwatch?</h3>
<p>No. Portwatch hosts no game files and links to no downloads. Projects like VIctory and XCL are open source and can be built from their GitHub pages, but they need the leaked Xbox build to run, which carries legal risk.</p>
<h3>How do I know a port claim is real?</h3>
<p>Check whether Portwatch lists it with a source, whether the project's GitHub page shows matching commits, and whether independent outlets have reported it. A claim with no tracker entry, no code and only a short video is not verified.</p>
""",
cover=dict(eyebrow="Guide · Nov 25", title="Track the GTA 6 PC Port Race", sub="Portwatch scores every project from boot to stable 30 fps.", rows=[("Leader", "CGBJ, 72%", True), ("VIctory", "67%", False), ("Playable yet", "no", True)]),
sources=[
("TweakTown: GTA 6 reportedly reaches in-game rendering on PC just a day after Xbox executable leak", "https://www.tweaktown.com/news/114853/gta-6-reportedly-reaches-in-game-rendering-on-pc-just-a-day-after-xbox-executable-leak/index.html"),
("XDA: An unofficial GTA 6 PC port is making progress, and developers have the first in-game visuals to show for it", "https://www.xda-developers.com/unofficial-gta-6-pc-port-making-progress-developers-have-first-in-game-visuals/"),
("DSOGaming: Grand Theft Auto 6 unofficial PC port CGBJ now reaches in-game", "https://www.dsogaming.com/news/grand-theft-auto-6-unofficial-pc-port-cgbj-now-reaches-in-game/"),
("NextGenUpdate: GTA 6 PC port progress continues to be made after multiple project shutdowns", "https://nextgenupdate.com/articles/467/gta-6-pc-port-progress-continues-to-be-made-after-multiple-project-shutdowns"),
],
related=["gta-6-pc-port-in-game-rendering", "gta-6-pc-port-race-victory-xcl", "gta-6-pc-download-scams"],
),
]
