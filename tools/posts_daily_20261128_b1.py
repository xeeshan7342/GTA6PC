"""Batch 1, November 28, 2026: GitHub removes Belobug, the top-ranked unofficial
GTA 6 PC port, and its author account; plus the first footage claiming 30 FPS
from an unofficial port, and what the trackers say about that number."""

POSTS_DAILY_20261128_B1 = [
dict(
slug="gta-6-pc-port-belobug-removed",
short="Belobug removed, Nov 28",
title="Belobug GTA 6 PC Port Removed: GitHub Deletes the Leading Build and Its Author Account",
h1="Belobug removed: GitHub deletes the leading GTA 6 PC port and its author account",
desc="GitHub removed Belobug, the top-ranked unofficial GTA 6 PC port, and its author account on November 27, 2026. Here is what happened, why it was not a DMCA takedown, and who leads the race now.",
kicker="Port Race",
lede="The fastest unofficial GTA 6 PC port is gone from GitHub. Belobug, the AMD fork of VIctory that led the PortWatch VI tracker at 91.3 percent toward playable, stopped answering on November 27, 2026. By the next morning both the repository and the author account returned 404 errors. It was not a DMCA takedown, and the code had already spread further than GitHub.",
img_alt="GTA 6 PC port poster showing the Belobug project removed from GitHub",
tldr="On November 27, 2026, GitHub removed the <strong>Belobug</strong> repository and the Belobug author account. PortWatch VI reported at 18:33 UTC that GitHub removed them for a <strong>Terms of Service violation</strong>, not a DMCA takedown, and no public GitHub notice names the project. Belobug led the tracker at <strong>91.3 percent</strong> toward playable, with a reported 22 frames per second. <strong>VIctory-NVIDIA</strong> now leads the board at 90.0 percent and about 20 frames per second. There is still no official PC version and no legitimate download.",
faq=[("What happened to Belobug?", "GitHub removed the Belobug repository (Belobug/VIctory-Belobug-AMD) and the Belobug author account on November 27, 2026. Both addresses returned 404 errors when checked on November 28. PortWatch VI reported the removal was for a Terms of Service violation, not a DMCA takedown."), ("Was Belobug taken down by Take-Two?", "No public evidence says so. Take-Two's DMCA notice of November 24 targeted Leonida and its fork network. No DMCA notice names Belobug, and GitHub publishes notices for DMCA removals but not for Terms of Service removals. PortWatch reported the Belobug removal as a Terms of Service action by GitHub."), ("How fast was Belobug?", "Two different numbers are reported, and they measure different things. The project's own README, dated November 25, said the world ran at 5 to 8 frames per second on a Radeon RX 9070 XT, with menus at 30. Playground.ru, citing PortWatch, reported about 22 frames per second on average without crashes in a later private build. The README figure is the project's own measurement, the 22 figure is a tracker report."), ("Who leads the GTA 6 PC port race now?", "VIctory-NVIDIA leads the PortWatch VI board at 90.0 percent and about 20 frames per second after Belobug was removed. The private CGBJ build sits behind it at 89.6 percent with a reported 25 frames per second. Tracker channels citing PortWatch also report that AvatarManz, ranked at 81.8 percent, was removed the same day."), ("Can I still download Belobug?", "No. The public repository is gone, and there is no legitimate download. Copies circulating online are unverified, and packages offered as a GTA 6 PC download have carried malware. We do not link to any of them.")],
body="""
<h2>What happened on November 27</h2>
<p>Belobug was a fork of VIctory, the open-source project that runs GTA 6's Xbox code on Windows, tuned for AMD graphics cards. By November 26 it led the PortWatch VI tracker at 91.3 percent toward playable, ahead of every other project on the board, with story progress rated around 80 percent. Then it vanished. The public repository stopped answering on November 27, 2026, and a check on November 28 found both the repository address and the author's GitHub profile returning 404 errors.</p>
<p>PortWatch VI reported the removal in a news post timed 18:33 UTC on November 27, saying GitHub had removed the repository and the author's account for a Terms of Service violation, and that it had confirmed the removal. Playground.ru reported the same thing, citing PortWatch. The Belobug project site, which tracks the fork, confirmed both addresses were still returning 404 on November 28.</p>
<p>It is the second big disappearance in four days. Take-Two's DMCA notice on November 24 disabled Leonida and 3,007 related repositories. Belobug is different: it is the first leading project to go down without a DMCA notice behind it.</p>

<h2>A Terms of Service removal, not a DMCA takedown</h2>
<p>The distinction matters, because it decides what paper trail exists. When GitHub acts on a DMCA notice, it publishes the notice in its public log, which is how the Leonida takedown could be verified the same day. GitHub does not publish a notice for a Terms of Service removal. That is why no public GitHub document names Belobug, and why the Belobug project site is careful not to call the removal a copyright takedown.</p>
<p>What is confirmed is the outcome, not the trigger. The repository is gone, the account is gone, and PortWatch says GitHub removed them for a Terms of Service violation. Whether GitHub acted on a complaint or on its own review is not public. Take-Two has not claimed the removal, and no notice connects it to the November 24 DMCA action.</p>
<p>The pattern around Belobug is not unique. The ZETTROX project and its author account also went to 404 on November 25 with no published notice, and a comparison site noted on November 27 that the ZETTROX author's whole account had stopped loading a day earlier. Removals without public notices are becoming a regular feature of this race, which makes tracker reports and direct checks the only way to confirm what happened.</p>

<h2>The two frame rates, and why both are reported</h2>
<p>Belobug leaves behind a confusing pair of numbers, and they are worth keeping separate. The project's own README, in a section dated November 25, 2026, said the fork was not playable yet. On the one PC it named, a Windows 11 machine with a Radeon RX 9070 XT, a Ryzen 7 9800X3D and 64 GB of RAM, the open world ran at 5 to 8 frames per second, with menus at 30. That is the project's own measurement, in its own words, and it is the conservative figure.</p>
<p>The faster number, about 22 frames per second on average without crashes, comes from Playground.ru citing PortWatch, and it was repeated by PCQuest, which added that the build used about 30 GB of system memory and 12 GB of video memory. PortWatch's leaderboard also carried the 22 figure. It describes a later private build, not the build the README measured, and nobody outside the project has independently tested it. Both numbers stay in the record because they describe different builds at different times, and collapsing them into one would hide that.</p>
<p>The same caution applies to the tracker score itself. The 91.3 percent is PortWatch's own scoring, built from the project's README, commits and stream footage, with self-reported claims labelled as such. A second tracker, GTA6 Recomp, scored the same project at 62 percent on its own scale. Scores are a tracker's opinion, not a benchmark.</p>

<h2>Who leads now</h2>
<p>With Belobug off the ranked board, VIctory-NVIDIA takes first place on PortWatch at 90.0 percent, running at about 20 frames per second. The private CGBJ build follows at 89.6 percent, with the best reported frame rate on the board at about 25 frames per second, but it is private, so nobody outside its group can test it. Tracker channels citing PortWatch also report that AvatarManz, the AMD fork ranked at 81.8 percent, had its repository and account removed the same day as Belobug.</p>
<p>The public projects that remain online are VIctory itself and XCL, the two open-source layers most of the private builds sit on. Our <a href="../gta-6-pc-ports-taken-down/">takedown tracker</a> lists every project that has gone offline so far, and our <a href="../gta-6-pc-port-tracker-portwatch/">PortWatch guide</a> explains how the tracker scores each project. The board changes daily: Belobug led it by a single day, and its removal moved the leader without a single line of code being written.</p>

<h2>Does a removal kill the project?</h2>
<p>Not necessarily. When CGBJ went public briefly on November 26, it gathered 293 stars and 82 forks before its page went dark, and several forks stayed active. Code that has been forked, starred and streamed does not disappear when one repository does. Private groups and smaller forks keep working, which is also why so many of the claims now come with no public code to check.</p>
<p>What a removal does kill is verification. While Belobug was public, anyone could read its README, check its commits and measure its claims. Once the repository is gone, the only record is what trackers and reporters saved before it vanished. That is why the 22 frames per second figure can no longer be checked against the code, and why the README's 5 to 8 figure is now the last measurement the project itself published.</p>
<div class="warn"><strong>Do not download anything offered as the Belobug build.</strong> The public repository is gone, the project has no official download, and packages using the port race as bait have carried malware. The only safe position is to watch and wait.</div>

<h2>The bottom line</h2>
<p>Belobug was the closest thing to a playable unofficial GTA 6 PC port, and GitHub removed it and its author's account on November 27 without a public notice. The removal was reported as a Terms of Service action, not a Take-Two DMCA takedown, and the distinction is real: one leaves a paper trail and the other does not. VIctory-NVIDIA now leads the tracker at 90.0 percent, and the race goes on in private forks, as it has after every removal so far. Rockstar has announced no official PC version, and nothing about this changes that.</p>

<h2>Quick answers</h2>
<h3>What happened to Belobug?</h3>
<p>GitHub removed the Belobug repository (Belobug/VIctory-Belobug-AMD) and the Belobug author account on November 27, 2026. Both addresses returned 404 errors when checked on November 28. PortWatch VI reported the removal was for a Terms of Service violation, not a DMCA takedown.</p>
<h3>Was Belobug taken down by Take-Two?</h3>
<p>No public evidence says so. Take-Two's DMCA notice of November 24 targeted Leonida and its fork network. No DMCA notice names Belobug, and GitHub publishes notices for DMCA removals but not for Terms of Service removals. PortWatch reported the Belobug removal as a Terms of Service action by GitHub.</p>
<h3>How fast was Belobug?</h3>
<p>Two different numbers are reported, and they measure different things. The project's own README, dated November 25, said the world ran at 5 to 8 frames per second on a Radeon RX 9070 XT, with menus at 30. Playground.ru, citing PortWatch, reported about 22 frames per second on average without crashes in a later private build. The README figure is the project's own measurement, the 22 figure is a tracker report.</p>
<h3>Who leads the GTA 6 PC port race now?</h3>
<p>VIctory-NVIDIA leads the PortWatch VI board at 90.0 percent and about 20 frames per second after Belobug was removed. The private CGBJ build sits behind it at 89.6 percent with a reported 25 frames per second. Tracker channels citing PortWatch also report that AvatarManz, ranked at 81.8 percent, was removed the same day.</p>
<h3>Can I still download Belobug?</h3>
<p>No. The public repository is gone, and there is no legitimate download. Copies circulating online are unverified, and packages offered as a GTA 6 PC download have carried malware. We do not link to any of them.</p>
""",
cover=dict(eyebrow="Port Race · Nov 28", title="Belobug Removed", sub="GitHub deleted the top-ranked GTA 6 PC port and its author account. The race has a new leader.", rows=[("Leader before removal", "91.3%", True), ("New leader", "VIctory-NVIDIA", False), ("Removal", "Nov 27", False)]),
related=["gta-6-pc-ports-taken-down", "take-two-shut-down-gta-6-pc-ports", "gta-6-pc-port-tracker-portwatch"],
sources=[
("Belobug GTA 6: repository and account return 404, PortWatch reports Terms of Service removal", "https://belobug.org/"),
("PCQuest: GTA 6 PC race intensifies as 30 projects compete, one reaches 91.3 percent", "https://www.pcquest.com/gaming/gta-6-pc-race-intensifies-as-30-community-projects-compete-one-reaches-913-completion-12844777"),
("TalkEsport: GTA 6 PC port gets multiplayer, how it works and what is fake", "https://www.talkesport.com/gta-6/gta-6-pc-port-multiplayer-how-it-works/"),
("XDA Developers: new frontrunner in the race to bring GTA 6 to PC", "https://www.xda-developers.com/new-frontrunner-race-to-unofficially-bring-gta6-to-pc-already-hitting-5-7fps/"),
("HotRepo: GTA 6 GitHub projects, PC port progress compared", "https://hotrepo.ai/stories/gta-6-github"),
("PortWatch VI: GTA 6 PC port tracker", "https://portwatch-vi.xyz"),
],
),
dict(
slug="gta-6-pc-port-30-fps",
short="30 FPS claim, Nov 28",
title="GTA 6 PC Port Hits 30 FPS: XCL Footage, the Boat Scene Claim and What Is Real",
h1="GTA 6 PC port hits 30 fps in new footage: what the claim really shows",
desc="A Reddit clip shows an unofficial GTA 6 PC port running past 30 FPS in the opening boat scene, and a second build averages 27 FPS on open water. Here is what was measured, what was not, and why trackers still say 20 FPS.",
kicker="Performance",
lede="An unofficial GTA 6 PC port has been filmed running past 30 frames per second for the first time. The footage, posted to Reddit on November 26, 2026, shows the opening boat sequence with the user claiming 30 FPS and above. A second build averaged 27 FPS on open water the same week. It is the fastest footage yet, and it comes with limits that matter more than the number.",
img_alt="GTA 6 PC port poster showing the 30 FPS claim from the opening boat scene",
tldr="Reddit user u/Rima_Mashiro-Hina posted footage of the <strong>XCL</strong> port running at <strong>30 FPS and above</strong> in the opening boat scene, and a second build from Group BoYoo averaged <strong>27 FPS</strong> on a boat mission. Both clips show light open-water scenes, shader stutter is still visible, and performance in the city is untested. Trackers that rely on logged measurements still put the best credible frame rate at about <strong>20 FPS</strong>. No official PC version exists.",
faq=[("Has a GTA 6 PC port reached 30 FPS?", "A Reddit clip shows an XCL-based port at 30 FPS and above in the opening boat scene, according to Twisted Voxel and Polygon. It is a claim in footage, not a logged benchmark, and it covers one light scene only. Trackers that rely on logged measurements still put the best credible frame rate at about 20 FPS."), ("Which build hit 30 FPS?", "The clip was posted by Reddit user u/Rima_Mashiro-Hina in r/FitGirlRepack and shows the XCL port, one of the main forks of the unofficial effort. A separate build from Group BoYoo averaged 27 FPS on a boat mission, on a Ryzen 7 9800X3D with an RTX 5070 Ti."), ("Does 30 FPS in the boat scene mean the game is playable?", "No. The boat scene is open water with few characters and little geometry, the lightest scene in the game. The same trackers report 6 to 13 FPS in the city on the fastest builds, and the dense centre of Vice City has not been tested at these frame rates."), ("Why do trackers still say 20 FPS?", "Trackers such as VGNW count logged measurements, not clip titles. Their best logged figure is about 20 FPS, with 19 to 23 FPS in light scenes and drops to 6 to 13 FPS in the city. A clip claiming 30 FPS in one scene does not change the logged average."), ("Are the 60 FPS and 4K 120 FPS videos real?", "No. Those videos show the game running at 30 FPS on a console, captured to a PC and smoothed, according to VGNW. No unofficial build has been measured at 60 FPS, and no build has been measured at 4K 120 FPS.")],
body="""
<h2>The clip: 30 FPS in the boat scene</h2>
<p>Twisted Voxel reported on November 26, 2026 that new gameplay footage shared on Reddit shows an unofficial GTA VI PC port exceeding 30 frames per second in certain sections. The video shows the opening boat sequence, with the user claiming they are now reaching 30 FPS and above in the scene. The post came from Reddit user u/Rima_Mashiro-Hina in r/FitGirlRepack. Polygon reported the same footage, writing that one Reddit user had got the XCL port running at over 30 fps, a pretty respectable, stable frame rate.</p>
<p>XCL is one of the main forks in the unofficial effort, a compatibility layer for Xbox Series games that reimplements the console's system libraries. The clip matters because of where it sits in the week's climb. A few days earlier, the leading projects were managing 1 to 5 frames per second in the prologue, and VIctory's own README still listed the first mission intro at 1 to 2 seconds per frame. Going from that to 30 in a week is the fastest progress the race has shown.</p>
<p>But the clip itself carries its own warning. Twisted Voxel notes that shader-related stuttering remains visible, and that performance beyond the opening sequence has yet to be established. The number in the clip is a claim attached to footage, not a benchmark run with a published method, scene and hardware list. Treat it as a claim with video attached, not a measurement.</p>

<h2>The second data point: 27 FPS on open water</h2>
<p>The 30 FPS clip is not the only fast footage from the same days. The Ukrainian outlet dev.ua reported that a team called Group BoYoo showed a mission on a motorboat in open waters, with the water surface, reflections, daylight, clouds and interface elements all rendering correctly. The average frame rate was 27 FPS, with the minimum dropping to 21 to 22 FPS and frame times of 33.4 to 40.7 milliseconds. Testing ran on a Ryzen 7 9800X3D with a GeForce RTX 5070 Ti and 32 GB of RAM.</p>
<p>That report is stronger than a clip title, because it names the hardware, the scene and the frame time range. It is also narrower: the same report notes the build has not been tested in the dense urban development of the centre of Vice City, which loads the hardware far more than open water. Dev.ua also notes that videos are appearing in pirate subreddits claiming stable 30 to 40 frames per second, including one from a user called agentvirat. Those claims have no published measurements behind them.</p>
<p>Two builds in the same week, both on water, both in the high twenties. That is a real pattern. It is also a pattern with one scene in common, and that scene is the easiest in the game.</p>

<h2>Why the trackers still say 20 FPS</h2>
<p>If two builds are filming the high twenties, why does the tracker VGNW, updated November 27, still put the best credible frame rate at around 20 FPS? The answer is method. VGNW counts logged measurements, and its best logged figures are 19 to 23 FPS in light scenes on the most powerful cards, such as the RTX 4090 and RX 7900 XTX, dropping to 6 to 13 FPS in the city. Its page states plainly that no logged measurement has reached 30 FPS.</p>
<p>The two views are not contradictory. A clip can show 30 FPS in one light scene while the logged average across scenes sits at 20. The boat scene has open water, few pedestrians and little geometry. The city has crowds, traffic, reflections and dense buildings, and it is where every build slows down. Until a build logs 30 FPS in the city, with hardware named and a run long enough to trust, the trackers are right to hold the line at 20.</p>
<p>Our <a href="../gta-6-pc-port-fps-explained/">FPS explainer</a> covers why one tracker says 20 FPS and another says 5 FPS: different projects, different scenes, different hardware. The 30 FPS claim fits the same pattern. It is a scene-specific peak, not a new average.</p>

<h2>From one frame every two seconds to 30</h2>
<p>The speed of the climb is what makes the claim believable as a direction, even while the number itself is unverified. On November 23, Cyberleek released the missing 57 MB executable, version 1.0.2.1, for the leaked 209 GB Xbox build, and the porting work began. Early builds rendered the prologue at 1 to 5 frames per second. Within days, community forks were reporting about 20 frames per second, and a multiplayer demo on a private CGBJ fork ran at a reported 25 to 30 FPS at an airport, which the console versions target at 30.</p>
<p>Modders are using AI coding tools, including Claude and Codex, to accelerate the work, according to Twisted Voxel, parsing error logs and fixing crashes far faster than manual debugging would allow. That explains the pace. It does not explain away the gaps: shader stutter, missing water in some builds, broken lighting, and crashes are still reported across the board.</p>
<p>The console comparison is the honest yardstick. The PlayStation 5 and Xbox Series X versions target 30 frames per second. A PC build that holds 30 in the boat scene has matched the console target in one scene. A PC build that holds 30 in Vice City at rush hour has not been shown yet, by anyone.</p>

<h2>The fake 120 FPS videos</h2>
<p>The 30 FPS claim arrives alongside louder fakes, and they are worth separating. VGNW reports that most videos showing 60 FPS or 4K 120 FPS are not the game running on PC at all, but console footage passed through a PC and smoothed. TalkEsport reported the same split: the most shared performance claim said the port had reached 4K at 120 frames per second, patched by AI tools, and that claim is fake.</p>
<p>The difference between the real clips and the fakes is evidence. The boat scene clips name a project, show a frame counter, and come with hardware details or a tracker verification. The 4K 120 FPS videos show console footage with no build, no code and no measurement. If a video promises 120 FPS and cannot name the project behind it, it is not a port, it is a render.</p>
<div class="warn"><strong>Do not download anything offered as a 30 FPS GTA 6 PC build.</strong> No project has released a public build at this performance, the builds in these clips are private or unreleased, and packages offered as a GTA 6 PC download have carried malware.</div>

<h2>The bottom line</h2>
<p>A Reddit clip shows an unofficial GTA 6 PC port past 30 frames per second in the opening boat scene, and a second build averaged 27 on open water. Both are real steps, and both are confined to the lightest scene in the game. The logged measurements still say about 20 frames per second, with the city at 6 to 13, and no build has been measured at 30 where it counts. The race has gone from one frame every two seconds to 30 in a single scene in five days. The next test is the city, and nobody has passed it yet.</p>

<h2>Quick answers</h2>
<h3>Has a GTA 6 PC port reached 30 FPS?</h3>
<p>A Reddit clip shows an XCL-based port at 30 FPS and above in the opening boat scene, according to Twisted Voxel and Polygon. It is a claim in footage, not a logged benchmark, and it covers one light scene only. Trackers that rely on logged measurements still put the best credible frame rate at about 20 FPS.</p>
<h3>Which build hit 30 FPS?</h3>
<p>The clip was posted by Reddit user u/Rima_Mashiro-Hina in r/FitGirlRepack and shows the XCL port, one of the main forks of the unofficial effort. A separate build from Group BoYoo averaged 27 FPS on a boat mission, on a Ryzen 7 9800X3D with an RTX 5070 Ti.</p>
<h3>Does 30 FPS in the boat scene mean the game is playable?</h3>
<p>No. The boat scene is open water with few characters and little geometry, the lightest scene in the game. The same trackers report 6 to 13 FPS in the city on the fastest builds, and the dense centre of Vice City has not been tested at these frame rates.</p>
<h3>Why do trackers still say 20 FPS?</h3>
<p>Trackers such as VGNW count logged measurements, not clip titles. Their best logged figure is about 20 FPS, with 19 to 23 FPS in light scenes and drops to 6 to 13 FPS in the city. A clip claiming 30 FPS in one scene does not change the logged average.</p>
<h3>Are the 60 FPS and 4K 120 FPS videos real?</h3>
<p>No. Those videos show the game running at 30 FPS on a console, captured to a PC and smoothed, according to VGNW. No unofficial build has been measured at 60 FPS, and no build has been measured at 4K 120 FPS.</p>
""",
cover=dict(eyebrow="Performance · Nov 28", title="30 FPS on PC, At Last?", sub="A Reddit clip shows the unofficial port past 30 fps in the boat scene. The rest of the game is a different story.", rows=[("Claimed peak", "30+ FPS", True), ("Boat scene average", "27 FPS", False), ("City scenes", "6-13 FPS", False)]),
related=["gta-6-pc-port-fps-explained", "gta-6-pc-port-november-27-update", "gta-6-pc-port-multiplayer-video"],
sources=[
("Twisted Voxel: GTA VI running at over 30 FPS on PC in new footage of unofficial port", "https://twistedvoxel.com/gta-vi-pc-port-30-fps/"),
("Polygon: GTA 6 PC port takes a massive leap forward in just days", "https://www.polygon.com/gta-6-pc-port-update-progress-unofficial-cyberleek-leak/"),
("dev.ua: enthusiasts launched an unofficial port of GTA VI on PC with stable 25-30 FPS", "https://dev.ua/en/news/gta-6-na-pc-vzhe-vydaie-30-fps-1795694795"),
("VGNW: is GTA 6 on PC? Fans got there before Rockstar", "https://vgnw.net/news/is-gta-6-on-pc/"),
("TweakTown: GTA 6 PC port now has multiplayer running at 30FPS", "https://www.tweaktown.com/news/114929/gta-6-pc-port-now-has-multiplayer-running-at-30fps/index.html"),
],
),
]
