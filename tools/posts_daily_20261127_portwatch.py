"""November 27, 2026 (PortWatch batch): takedown tracker, private builds on Rumble,
and the hardware the unofficial GTA 6 PC builds are running on."""

PW = "https://portwatch-vi.xyz"

POSTS_DAILY_20261127_PORTWATCH = [
dict(
slug="gta-6-pc-ports-taken-down",
short="Takedown tracker",
title="Every GTA 6 PC Port Taken Down So Far: Leonida, ZETTROX and More",
h1="Every GTA 6 PC port taken down so far",
desc="Leonida, ZETTROX, americas-recomp and omonkey have all gone offline since November 23. Here is which GTA 6 PC projects are gone, when, and whether Take-Two was behind it.",
kicker="Tracker",
lede="In the week since GTA 6 launched on consoles, the community projects trying to run the leaked Xbox build on PC have started disappearing. Some were hit by a Take-Two DMCA notice. Others vanished with no notice at all. This page keeps one running list of every project that has gone offline, and what is known about why.",
img_alt="Tracker graphic listing GTA 6 PC port projects taken down since November 23, 2026",
tldr="As of November 27, 2026, <strong>four GTA 6 PC projects</strong> tracked by PortWatch have gone offline: <strong>Leonida</strong> (deleted November 23, then 3,007 forks disabled by a Take-Two DMCA notice on November 24), <strong>americas-recomp</strong> (404 since November 23), <strong>ZETTROX</strong> (404 on November 25, account gone) and the private <strong>omonkey</strong> build (taken down November 25). Only Leonida has a published DMCA notice. Projects such as VIctory and XCL are still online.",
faq=[("Which GTA 6 PC ports have been taken down?", "As of November 27, 2026: Leonida, americas-recomp, ZETTROX and the private omonkey build. Leonida's fork network of 3,007 repositories was disabled by a Take-Two DMCA notice. The other three went offline without a published DMCA notice."),
     ("Did Take-Two file a DMCA notice against GTA 6 PC ports?", "Yes, one so far. Take-Two's notice dated November 24, 2026 targeted the Leonida repository, and GitHub applied it to the project's entire network of 3,007 forks. Take-Two argued Leonida is a derivative work of GTA 6 and that its 'bring your own files' approach could only mean the leaked Xbox build."),
     ("Is VIctory or XCL still online?", "Yes, as of November 27, 2026. They are not GitHub forks of Leonida, so the November 24 notice did not cover them. PortWatch warns the same legal argument could be used against them."),
     ("Why did ZETTROX disappear?", "Nobody knows yet. The repository and the Zettrox GitHub account both returned 404 errors by 17:26 UTC on November 25, 2026, and no DMCA notice has been published. It could have been deleted by its owner or removed for another reason."),
     ("Can I still download a GTA 6 PC port?", "There is no legitimate GTA 6 PC download. Re-uploads of removed projects are circulating, but they still need the leaked game files and many 'ready to play' packages are malware. We do not link to any of them.")],
body=f"""
<h2>The takedown list</h2>
<p>This table covers projects on the PortWatch board that are now offline. We update it as new ones go down.</p>
<div class="table-wrap"><table>
<tr><th>Project</th><th>Approach</th><th>Went offline</th><th>What happened</th><th>DMCA notice?</th></tr>
<tr><td>Leonida</td><td>Static recompilation</td><td>November 23</td><td>GitHub repo deleted, 179,000-member Discord gone, creator quit. Fork network disabled the next day</td><td><strong>Yes</strong>, Take-Two, November 24</td></tr>
<tr><td>americas-recomp</td><td>Relinker and shader recompiler</td><td>About 22:00 UTC, November 23</td><td>Repository returns 404. Owner's account still active, so likely deleted or made private</td><td>None published</td></tr>
<tr><td>ZETTROX</td><td>Compatibility layer</td><td>By 17:26 UTC, November 25</td><td>Repository and the whole Zettrox account return 404</td><td>None published</td></tr>
<tr><td>omonkey</td><td>Private build (never public)</td><td>November 25</td><td>Owner reported it taken down. It had only ever been shown on Rumble streams</td><td>None published</td></tr>
</table></div>
<p>One more entry is unclear. PortWatch's data shows CGBJ's repository returning a 404, while CGBJ's own November 26 update says it is public. Until that is resolved we are not counting it as removed.</p>

<h2>Leonida: the only confirmed Take-Two takedown</h2>
<p>Leonida was the biggest GTA 6 PC project by far, with more than 32,000 GitHub stars. On the night of November 23 its Discord server stopped resolving, its repository was deleted and its creator said he was stepping away, all within about an hour. At the time, nobody had published a legal notice.</p>
<p>That came the next day. Take-Two's first DMCA notice against a GTA 6 port appeared in GitHub's public DMCA log on November 24. Because Leonida's fork network was larger than 100 repositories, GitHub processed the notice against all of it: <strong>3,007 repositories</strong> now show GitHub's "unavailable" page.</p>
<p>Take-Two's notice made three arguments. It said Leonida is a derivative work of GTA 6, that it breaks the reverse-engineering ban in Rockstar's terms of service, and that its "bring your own files" disclaimer is misleading, because at this point the files users must supply can only come from the leaked Xbox build. We covered the notice in more detail in <a href="../gta-6-pc-port-rockstar-crackdown/">Take-Two confirms the DMCA takedown that shut down Leonida</a>.</p>

<h2>The quiet disappearances</h2>
<p>The other three removals are harder to read. ZETTROX was briefly one of the most talked-about builds, reported to run from Lucia's prologue into Jason's first mission without crashing. Then on November 25 both the repository and the developer's GitHub account disappeared. americas-recomp went offline two days earlier while its owner's account stayed active, which points to the owner pulling it rather than GitHub.</p>
<p>omonkey never had public code at all. Its progress was shown through live streams on a Rumble channel run by someone else, and its owner said it was taken down on November 25. Private builds like this are a growing part of the story, which we look at in <a href="../gta-6-pc-private-builds-rumble/">why the furthest GTA 6 PC builds are private</a>.</p>
<p>Without a published notice, we can't say whether Take-Two, a platform or the developers themselves were behind these. It is common for developers to delete their own work once a large project in the same space receives a legal notice.</p>

<h2>Take-Two had already set the pattern with GTA V</h2>
<p>None of this came out of nowhere. On November 18, the day before GTA 6 launched, Take-Two sent GitHub four DMCA notices against unofficial GTA V ports, including iOS, macOS and Android versions. Reports counted from 349 disabled forks of one project to more than 600 projects in total. Three of the four projects shipped no game files, and Take-Two argued that telling users to bring their own copy did not excuse them.</p>
<p>That is the same argument it used against Leonida, and every GTA 6 project on the PortWatch board uses a similar "use your own copy" line. Developers can file a counter-notice, which forces GitHub to restore the code unless Take-Two sues. Take-Two did exactly that over the re3 and reVC GTA III and Vice City projects in 2021.</p>

<h2>Who is still online</h2>
<p>VIctory, XCL and the builds forked from them are still up as of November 27, along with separately uploaded copies of Leonida. They are not GitHub forks of Leonida, so the November 24 notice did not reach them. PortWatch's own assessment is that the same argument could be applied to any of them. Our explainer <a href="../take-two-shut-down-gta-6-pc-ports/">Will Take-Two shut down every GTA 6 PC port?</a> covers what could happen next.</p>

<h2>What this means for you</h2>
<p>The takedowns don't change the basics. None of these projects is a finished, legitimate way to play GTA 6 on PC, all of them depend on leaked game files, and re-uploads of removed projects are exactly the kind of thing scammers repackage with malware. If you want the official version, the <a href="../gta-6-pc-release-date/">PC release date page</a> has the latest, and our <a href="../gta-6-pc-download-scams/">scam guide</a> explains how to spot fake downloads.</p>
""",
cover=dict(eyebrow="Tracker · Nov 27", title="GTA 6 PC ports taken down",
           sub="Which unofficial GTA 6 PC projects are gone, when, and whether Take-Two filed a notice.",
           rows=[("Leonida + 3,007 forks", "DMCA", True), ("americas-recomp", "404", False), ("ZETTROX", "404", False), ("omonkey (private)", "Down", False)]),
related=["gta-6-pc-port-rockstar-crackdown", "take-two-shut-down-gta-6-pc-ports", "gta-6-pc-port-tracker-portwatch"],
sources=[
("PortWatch VI: Take-Two's first GTA VI port takedown disables Leonida and 3,007 forks", f"{PW}/news/2026-11-24-take-two-dmca-leonida-forks.html"),
("GitHub DMCA repository: Take-Two notice, 2026-11-24", "https://github.com/github/dmca/blob/master/2026/11/2026-11-24-take-two.md"),
("PortWatch VI: Leonida is nuked", f"{PW}/news/2026-11-23-leonida-nuked.html"),
("PortWatch VI: Leonida's Discord server disappears", f"{PW}/news/2026-11-23-leonida-discord-down.html"),
("PortWatch VI: tracker data (project status)", f"{PW}/data/tracker.json"),
("PortWatch VI: Take-Two hits GTA V ports on GitHub", f"{PW}/news/2026-11-18-take-two-dmca.html"),
("TorrentFreak: Take-Two targets hundreds of GTA V mobile ports on GitHub", "https://torrentfreak.com/take-two-targets-hundreds-of-gta-v-mobile-ports-on-github-ahead-of-gta-vi-launch/"),
],
),
dict(
slug="gta-6-pc-private-builds-rumble",
short="Private builds",
title="Why the Furthest GTA 6 PC Builds Are Private (and How to Spot a Fake Stream)",
h1="Why the furthest GTA 6 PC builds are private, and how to spot a fake stream",
desc="Some of the GTA 6 PC builds that reach free roam have no public code and only appear on Rumble or X streams. Here is who they are, what has been verified, and how to tell a real stream from a fake.",
kicker="Explainer",
lede="If you have watched GTA 6 running on a PC this week, there is a good chance it came from a build nobody else can test. Several of the furthest-along unofficial builds have no public code at all. They exist as Rumble streams, X clips and claims. Here is what that means, and how to judge what you are watching.",
img_alt="Graphic comparing private GTA 6 PC builds shown on Rumble and X streams with public projects",
tldr="Several unofficial GTA 6 PC builds, including <strong>darkworldhm, NotNozy, Doomsday and suri</strong>, have <strong>no public code</strong> and are shown only through streams on <strong>Rumble</strong> and clips on <strong>X</strong>. Some claim free roam at 12 to 15 fps, but most of their progress is <strong>self-reported</strong>, and PortWatch has verified only parts of it. A stream is not a download: anyone offering you a private build is very likely running a scam.",
faq=[("What are private GTA 6 PC builds?", "They are unofficial builds of the leaked Xbox version of GTA 6 running on PC whose code has not been published. Their developers show progress through livestreams and video clips instead, so nobody else can test them."),
     ("Why are GTA 6 PC builds streamed on Rumble?", "The streams do not say why. A likely reason is that Rumble has a reputation for lighter moderation than YouTube or Twitch, at a time when Take-Two is filing takedown notices against GTA 6 port projects."),
     ("Which private GTA 6 PC build is furthest?", "As of November 27, 2026, darkworldhm's build was streamed in free roam at about 12 to 15 fps on what is reported to be an NVIDIA RTX 50-series card. That progress is self-reported. Doomsday's build is one of the few private ones PortWatch has verified."),
     ("Can I download a private GTA 6 PC build?", "No. Private means the code has not been released. Anyone selling or sharing a 'private build', or asking you to join a paid Discord or buy a token for access, is very likely running a scam."),
     ("How can I tell if a GTA 6 PC stream is fake?", "Look for long, unedited runs with the PC's desktop or performance overlay visible, independent verification from trackers like PortWatch, and no download links or payment requests. Short clips, GTA V-looking footage and pressure to pay are red flags.")],
body=f"""
<h2>The builds you can watch but not test</h2>
<p>Most GTA 6 PC projects that make the news have public code on GitHub, such as VIctory, XCL and the forks built on them. A growing group does not. These builds are shown off through livestreams and short clips, and their developers have not released anything others can run. PortWatch tracks them, but lists private builds without a rank because their progress can't be checked independently.</p>
<div class="table-wrap"><table>
<tr><th>Build</th><th>Where it's shown</th><th>Furthest point</th><th>Frame rate</th><th>Verified?</th></tr>
<tr><td>darkworldhm</td><td>Rumble stream (November 25)</td><td>Free roam</td><td>About 12 to 15 fps, swinging 5 to 24</td><td>Self-reported</td></tr>
<tr><td>NotNozy</td><td>Rumble ("GTA6 Modding Stream")</td><td>World reached, owner claims 80% of story</td><td>No measured figure</td><td>Self-reported</td></tr>
<tr><td>Doomsday</td><td>X</td><td>Owner claims 80% of story</td><td>About 3 to 5 fps with ray tracing</td><td><strong>Verified by PortWatch</strong></td></tr>
<tr><td>suri</td><td>Not stated</td><td>Lucia's prologue confirmed</td><td>About 3 fps</td><td>Prologue only</td></tr>
<tr><td>omonkey</td><td>Rumble (another person's channel)</td><td>Opening prison scene</td><td>About 5 fps</td><td>Self-reported, now taken down</td></tr>
</table></div>
<p>Notice the pattern: several owners rate their own story progress at 80%, while independent confirmation, where it exists, usually covers much less.</p>

<h2>Why keep a build private?</h2>
<p>None of these developers has explained it publicly, but the timing explains a lot. On November 24, Take-Two's DMCA notice against Leonida took down 3,007 GitHub repositories in one go, and other public projects disappeared in the days around it (see our <a href="../gta-6-pc-ports-taken-down/">takedown tracker</a>). Code that was never published can't be taken down from GitHub. Streaming gameplay without releasing anything keeps the developer in the spotlight while lowering that risk.</p>
<p>The platform choice likely fits the same logic. Rumble is widely seen as more lenient than YouTube or Twitch, which tend to act quickly on publisher copyright claims. Even so, that is no guarantee: omonkey's build, which was streamed on Rumble, was taken down on November 25.</p>
<p>There is also a less charitable reason. A private build can't be checked, so its owner can claim more than it really does. That doesn't make every private build fake, but it means you should treat their claims as claims.</p>

<h2>Several private builds come from public code</h2>
<p>Private doesn't always mean built from scratch. In a November 25 report, PortWatch said several private builds that reach Jason's first mission, "Gone Fishing", appear to be built on hyphennn's victory-fork, a public fork of VIctory, with their own changes kept private. One group's multiplayer video ran on a private fork of CGBJ's build, which we covered in <a href="../gta-6-pc-port-multiplayer-video/">the GTA 6 PC multiplayer video</a>. In practice, the public projects do much of the groundwork and the private builds add fixes on top.</p>

<h2>How to tell a real stream from a fake</h2>
<p>Fake GTA 6 PC footage was everywhere before these builds existed, and it hasn't gone away. Some checks that help:</p>
<ol>
<li><strong>Long and unedited beats short and cut.</strong> Real builds at 3 to 15 fps look rough, stutter and crash. A smooth 30-second clip with music is more likely edited, or <a href="../gta-6-pc-fake-videos/">GTA V footage passed off as GTA 6</a>.</li>
<li><strong>Look for the PC around the game.</strong> Real test streams usually show a desktop, a console window, a frame counter or a performance overlay.</li>
<li><strong>Check an independent tracker.</strong> PortWatch marks which claims it has verified and which are self-reported. A build no tracker has seen deserves extra doubt.</li>
<li><strong>Watch for money.</strong> Paid Discord access, "donate to unlock", crypto tokens or a download link in the chat are the clearest red flags. The Cyberleek leak itself came wrapped in paid votes and token goals.</li>
<li><strong>A stream is never a download.</strong> If a private build is real, its developer isn't selling it to strangers. Anyone offering you one is almost certainly <a href="../gta-6-pc-download-scams/">distributing malware or running a scam</a>.</li>
</ol>

<h2>The bottom line</h2>
<p>Private builds are where some of the most impressive GTA 6 PC footage is coming from, but they are also the hardest to trust and impossible to use. Even the best of them run far below playable frame rates, and all of them depend on the leaked Xbox files. For the real thing, keep an eye on our <a href="../gta-6-pc-release-date/">GTA 6 PC release date</a> page.</p>
""",
cover=dict(eyebrow="Explainer · Nov 27", title="Private GTA 6 PC builds",
           sub="Builds that only exist as Rumble and X streams, and how to judge what you're watching.",
           rows=[("darkworldhm (Rumble)", "Free roam", False), ("Doomsday (X)", "Verified", False), ("NotNozy (Rumble)", "Self-reported", True), ("Public download", "None", True)]),
related=["gta-6-pc-ports-taken-down", "gta-6-pc-fake-videos", "is-gta-6-playable-on-pc"],
sources=[
("PortWatch VI: tracker data (private builds)", f"{PW}/data/tracker.json"),
("PortWatch VI: GTA VI builds clear Lucia's prologue and reach Jason's first mission", f"{PW}/news/2026-11-25-prologue-gone-fishing.html"),
("PortWatch VI: GTA VI's shaders start loading on omonkey's build, streamed live on Rumble", f"{PW}/news/2026-11-24-omonkey-shaders-prison.html"),
("PortWatch VI: Take-Two's first GTA VI port takedown", f"{PW}/news/2026-11-24-take-two-dmca-leonida-forks.html"),
("PortWatch VI: The missing GTA VI executable is due Monday, and votes cost money", f"{PW}/news/2026-11-22-exe-deadline-time.html"),
],
),
dict(
slug="gta-6-pc-port-hardware-amd-vs-nvidia",
short="Port hardware",
title="What PC Do the GTA 6 Port Builds Run On? AMD vs NVIDIA Results So Far",
h1="What PC do the GTA 6 port builds run on? AMD vs NVIDIA so far",
desc="The unofficial GTA 6 PC builds are being tested on cards from the RTX 3050 to the RX 7900 XTX. Here is every reported spec and frame rate, why AMD builds lead, and why none of it tells you what the real PC version will need.",
kicker="Hardware",
lede="Every GTA 6 PC build clip comes with the same question in the comments: what PC is that running on? The developers have shared more than you might think. Here is every spec and frame rate reported so far, and what you can and can't take from them.",
img_alt="Chart of hardware and frame rates reported for unofficial GTA 6 PC builds, AMD and NVIDIA",
tldr="The fastest verified unofficial GTA 6 PC build, <strong>AvatarManz's</strong>, averages about <strong>16 fps</strong> on an <strong>AMD RX 7900 XTX</strong> with a Core i9-12900K and 64 GB of RAM. Most builds run at <strong>1 to 10 fps</strong>, and the leading <strong>Belobug</strong> build needs about <strong>22 GB of RAM and more than 16 GB of VRAM</strong>. AMD builds lead because the leaked game was made for the Xbox's AMD graphics. None of this reflects what the official PC version will need.",
faq=[("What PC runs the GTA 6 PC port builds best?", "As of November 27, 2026, the fastest build PortWatch has verified is AvatarManz's, at about 16 fps average on an AMD Radeon RX 7900 XTX with an Intel Core i9-12900K and 64 GB of RAM. Most other builds run at 1 to 10 fps."),
     ("Do GTA 6 PC port builds run better on AMD or NVIDIA?", "Most of the leading builds are tuned for AMD Radeon cards. The leaked build was made for the Xbox Series consoles, which use AMD graphics, so AMD GPUs need less translation. NVIDIA-tuned builds exist, such as Kelvaroq and the earlier ZETTROX build, but they have generally rendered less accurately so far."),
     ("How much RAM do the GTA 6 PC builds need?", "A lot. Belobug's build needs about 22 GB of system RAM and more than 16 GB of VRAM, and AvatarManz's build uses 40 to 46 GB of memory. Testers mostly use 64 GB machines."),
     ("Are these the GTA 6 PC system requirements?", "No. These builds run a console version through unfinished compatibility layers, which is far less efficient than a real PC port. Rockstar has not published official PC requirements."),
     ("Should I upgrade my PC for GTA 6 now?", "Not because of these builds. Wait for Rockstar's official PC requirements before spending money on hardware specifically for GTA 6.")],
body=f"""
<h2>Every reported spec so far</h2>
<p>These figures come from PortWatch's tracker and from the projects' own notes, as of November 27, 2026. Frame rates vary a lot by scene, so treat each one as a rough guide.</p>
<div class="table-wrap"><table>
<tr><th>Build</th><th>GPU</th><th>Other hardware</th><th>Reported frame rate</th></tr>
<tr><td>AvatarManz</td><td>AMD RX 7900 XTX</td><td>Core i9-12900K, 64 GB RAM</td><td><strong>About 16 fps average</strong> (PortWatch-verified). 19 to 22 on the first boat mission, 6 to 10 in busy chases</td></tr>
<tr><td>darkworldhm (private)</td><td>NVIDIA RTX 50-series (reported)</td><td>Not stated</td><td>About 12 to 15 fps in free roam (self-reported)</td></tr>
<tr><td>Kelvaroq</td><td>NVIDIA (RTX 4090 in one playtest)</td><td>Not stated</td><td>About 10 fps in the prologue, 7 to 8 in heavier views</td></tr>
<tr><td>Belobug</td><td>AMD RX 9070 XT 16 GB</td><td>Ryzen 7 9800X3D, 64 GB RAM</td><td>About 3 to 5 fps, about 3 while driving</td></tr>
<tr><td>Uilian (VItoriaBr)</td><td>NVIDIA RTX 5060 Ti</td><td>Not stated</td><td>Up to 4 fps on stream</td></tr>
<tr><td>DexNom</td><td>AMD RX 7900 XTX</td><td>Not stated</td><td>About 3 to 4 fps, about 1 with ray tracing on</td></tr>
<tr><td>hyphennn victory-fork</td><td>NVIDIA RTX 4070</td><td>Not stated</td><td>About 3 fps on streams</td></tr>
<tr><td>ZETTROX (now offline)</td><td>NVIDIA RTX 3050</td><td>Not stated</td><td>About 1 to 3 fps</td></tr>
<tr><td>VIctory (Marvis)</td><td>AMD RX 6700 XT</td><td>Not stated</td><td>About 1 fps in the world</td></tr>
</table></div>
<p>The headline is simple: even on top-end PCs, none of these builds is close to a playable frame rate in the open world yet.</p>

<h2>Why AMD builds are ahead</h2>
<p>GTA 6 was made for the PS5 and Xbox Series X|S, and the leaked build is the Xbox version. Both consoles use AMD graphics, so the game's shaders and rendering are written for AMD's architecture. A compatibility layer running on a Radeon card has less to translate than one running on a GeForce card.</p>
<p>The results reflect that. Belobug's AMD-tuned build took the top spot on PortWatch's board at 77.4%, with the best rendering score PortWatch has given so far. The previous leader, ZETTROX's NVIDIA-tuned build, scored 64.2% and drew anything in shadow as black. NVIDIA builds aren't far behind on frame rate, though: Kelvaroq and darkworldhm both report around 10 to 15 fps.</p>

<h2>The real bottleneck is memory</h2>
<p>Frame rate gets the attention, but memory is what stops most people from running these builds. Belobug's build needs about 22 GB of system RAM and more VRAM than the 16 GB on its RX 9070 XT. AvatarManz's build uses 40 to 46 GB of memory. Most testers are on 64 GB machines.</p>
<p>That most likely comes from how the builds work. A console shares one pool of fast memory between CPU and GPU, and the compatibility layers emulate that on PC with extra copies and translation along the way. It is one of the clearest signs that these are experiments, not ports.</p>

<h2>What this tells you about the real PC version</h2>
<p>Very little. An official PC version would be compiled for Windows and PC graphics APIs, with no translation layer in between, so it would run far better on the same hardware. Rockstar hasn't published PC requirements, and the leaked builds can't stand in for them.</p>
<p>What the builds do show is that GTA 6 is a heavy game, and that 16 GB of VRAM and plenty of system RAM are a sensible baseline for anyone planning a new PC. For realistic guidance, see our <a href="../gta-6-pc-system-requirements/">expected GTA 6 PC system requirements</a> and <a href="../best-gpu-for-gta-6-pc/">best GPU for GTA 6</a>. Our advice hasn't changed: don't buy hardware for GTA 6 until Rockstar publishes the real numbers.</p>

<h2>Can you run one of these builds?</h2>
<p>We don't recommend it. Every build needs the leaked Xbox game files, several projects have already been <a href="../gta-6-pc-ports-taken-down/">taken down</a>, and "ready to play" packages are a common <a href="../gta-6-pc-download-scams/">malware trap</a>. If you want to play GTA 6 on your PC screen today, <a href="../play-gta-6-on-pc-remote-play/">PS Remote Play</a> from a PS5 is the safe route.</p>
""",
cover=dict(eyebrow="Hardware · Nov 27", title="GTA 6 port builds: AMD vs NVIDIA",
           sub="Every reported GPU, RAM figure and frame rate from the unofficial GTA 6 PC builds.",
           rows=[("RX 7900 XTX (AvatarManz)", "~16 fps", False), ("RTX 4090 (Kelvaroq)", "~10 fps", False), ("RX 9070 XT (Belobug)", "3-5 fps", False), ("RAM needed (Belobug)", "~22 GB", True)]),
related=["gta-6-pc-system-requirements", "best-gpu-for-gta-6-pc", "gta-6-pc-port-ray-tracing-dexnom"],
sources=[
("PortWatch VI: tracker data (hardware and frame rates)", f"{PW}/data/tracker.json"),
("PortWatch VI: We've seen Belobug's AMD build, and it's way ahead", f"{PW}/news/2026-11-25-belobug-way-ahead.html"),
("PortWatch VI: ZETTROX's GTA VI build looks uncrashable so far", f"{PW}/news/2026-11-25-zettrox-no-crashes.html"),
("PortWatch VI: Scoring method", f"{PW}/#method"),
],
),
]
