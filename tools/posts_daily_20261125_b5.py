"""Batch 5, November 25, 2026: the November 25 port race update (forks at 12 fps, Take-Two DMCA takedown)."""

POSTS_DAILY_20261125_B5 = [
dict(
slug="gta-6-pc-port-november-25-update",
short="Forks race on",
title="GTA 6 PC Port Update, Nov 25: Forks Hit 12 FPS as Take-Two Takes Down 3,007 Repos",
h1="GTA 6 PC port update, November 25: forks hit 12 fps as Take-Two takes down 3,007 repos",
desc="One day after in-game rendering, GTA 6 PC forks report 5 to 12 fps and a 77-minute play session. Take-Two answered with a DMCA takedown of the Leonida network, 3,007 repositories in total.",
kicker="PC ports",
lede="The unofficial race to run GTA 6 on PC moved fast again on November 25, 2026, and the publisher moved fast too. Forks of the VIctory project now report frame rates of 5 to 12 per second and play sessions of more than an hour, a day after the first in-game rendering. On the same day, Take-Two confirmed it had GitHub take down Leonida, the project that started the race, along with its network of 3,007 repositories. Nothing is playable yet, and nothing here is downloadable.",
img_alt="GTA 6 PC port poster showing forks at 7 to 12 fps, a 77-minute session, and 3,007 repositories taken down",
tldr="Forks of the <strong>VIctory</strong> project now run GTA 6 in-game at <strong>5 to 12 fps</strong>, with the longest reported session at <strong>77 minutes</strong> on a Radeon RX 9070 XT. Take-Two had GitHub disable the <strong>Leonida</strong> network, <strong>3,007 repositories</strong>, under a DMCA notice on November 24. The community tracker estimates a playable build is about <strong>a day away</strong>, but that is an estimate, and no project meets the 20 fps bar yet.",
faq=[("Is GTA 6 playable on PC now?", "No. The furthest public builds run in-game at roughly 5 to 12 frames per second, with black shadows and missing effects. The tracker's playable bar is 20 frames per second for 30 minutes without a crash, and no project has met it."), ("What did Take-Two take down?", "Take-Two's DMCA notice, published by GitHub on November 24, 2026, disabled Leonida, the static recompilation project, and its network of forks, 3,007 repositories in total. Leonida's Discord server was also taken down."), ("Why did Take-Two target Leonida?", "The notice says stolen files from an Xbox Series build of GTA 6 were publicly distributed on November 20, 2026, and Leonida's repository opened the next day. Take-Two calls the project a derivative work that breaks Rockstar's terms of service, which bar decompiling, decrypting or reverse engineering its games."), ("Which fork is furthest now?", "The community tracker puts klbf-lab first: a 77-minute session on a Radeon RX 9070 XT, playing the opening mission and the second mission to the end, at about 5.2 frames per second on average. Flamingo reports the highest frame rate, 9 to 12 fps on an RTX 4070, but that is unconfirmed and from one machine."), ("Can I download one of these builds?", "No. There is no public download of a working build, and the projects need the leaked Xbox build to run at all. Any site offering a GTA 6 PC download is not selling a real product, and the files going around are often malware.")],
related=["gta-6-pc-port-in-game-rendering", "gta-6-pc-port-tracker-portwatch", "gta-6-pc-port-rockstar-crackdown"],
cover=dict(eyebrow="PC ports · November 25", title="Forks hit 12 fps", sub="Take-Two takes down 3,007 repos.",
           rows=[("Longest session", "77 minutes", False), ("Fastest reported fps", "7 to 12", False), ("Repos taken down", "3,007", True), ("Playable yet", "No", True)]),
body="""
<h2>What changed on November 25</h2>
<p>On November 24, the story was that GTA 6 had reached in-game rendering on PC at about 1 frame per second. On November 25, the numbers moved sharply. The community tracker that reads every public port project every 15 minutes now lists 34 open-source projects and four private builds, and 19 of them are in-game. The leading build, klbf-lab, reports a 77-minute session with no crash, playing the opening mission and the whole second mission to the end, then free roaming, at about 5.2 frames per second on average on a Radeon RX 9070 XT.</p>
<p>The frame rate is still far from playable, but the direction is clear. A day earlier the best public result was roughly 0.6 to 2 frames per second. Now the fastest reported build, Flamingo, claims 9 to 12 frames per second on an RTX 4070, and victory-fork reports 7 to 12 frames per second by view, with an open pull request describing a 30-minute run at about 7.6 frames per second on an RTX 4090. Our <a href="../gta-6-pc-port-in-game-rendering/">in-game rendering report</a> covers where the race stood a day ago, and our <a href="../gta-6-pc-port-tracker-portwatch/">Portwatch guide</a> explains how the trackers score each milestone.</p>

<h2>Take-Two's DMCA takedown: 3,007 repositories</h2>
<p>Take-Two Interactive confirmed on November 24 that it was behind the removal of Leonida, the biggest fan project working to run the leaked Xbox Series build of GTA 6 natively on PC. GitHub published the company's DMCA notice that day, and GitHub said it processed the takedown against Leonida's entire network of 3,007 repositories, covering the main project and its forks.</p>
<p>The notice fills in the timeline. Take-Two says stolen game files from an Xbox Series build of GTA 6 were publicly distributed on November 20, 2026, and the Leonida repository opened the following day. Leonida itself did not include the leaked game files. Its instructions told users to supply their own Xbox Series files. Take-Two called that approach intentionally misleading, and argued the project is a derivative work built on stolen files that violates Rockstar's ban on reverse engineering. Section 2.3 of Rockstar's terms of service bars users from decompiling, decrypting or reverse engineering its games.</p>
<p>The action went beyond GitHub. Leonida's Discord server was also taken down, and its lead developer, who goes by NotRexed, posted a screenshot of a Discord notice limiting his access to servers until November 30, 2026. Our <a href="../gta-6-pc-port-rockstar-crackdown/">crackdown report</a> has the full story of Leonida's shutdown.</p>

<h2>The forks kept going anyway</h2>
<p>The takedown hit Leonida, but the projects that picked up its work are built on VIctory, a different codebase, and they kept moving. Here is where the leading builds stand as of November 25, according to the community tracker, which checked them at 16:07 UTC.</p>
<div class="table-wrap"><table>
<tr><th>Build</th><th>Card tested on</th><th>Reported frame rate</th><th>Longest session</th></tr>
<tr><td>klbf-lab</td><td>Radeon RX 9070 XT</td><td>About 5.2 fps average</td><td>77 minutes, no crash</td></tr>
<tr><td>Flamingo</td><td>RTX 4070</td><td>9 to 12 fps, unconfirmed</td><td>24 minutes</td></tr>
<tr><td>victory-fork</td><td>RTX 4070 / RTX 4090</td><td>7 to 12 fps</td><td>30 minutes (pull request)</td></tr>
<tr><td>ztrx</td><td>RTX 3050 8GB</td><td>1 to 3 fps</td><td>Over 90 minutes</td></tr>
<tr><td>AnyXboxX</td><td>RTX 4070 SUPER</td><td>5.3 to 6.9 fps</td><td>45 minutes (relayed)</td></tr>
<tr><td>VIctory-Belobug-AMD</td><td>Radeon RX 9070 XT</td><td>3 to 4.9 fps</td><td>15 minute drive</td></tr>
</table></div>
<p>Every figure above comes from one machine, or from a maintainer relaying another user's report, and the tracker says so plainly. The frame rates are real measurements, but they are not independently verified, and they vary a lot by scene. The most complete picture comes from klbf-lab, which reports the world lit with tints and faint lines, vegetation and thin translucent materials turning magenta, and the ground staying very dark at night. Flamingo's higher numbers come with missing shadows, dark rooms and black rectangles in places.</p>

<h2>Dozens of people are now running it</h2>
<p>The work is no longer one developer's project. By 02:55 UTC on November 25, 67 machine reports from 63 accounts had run a fork of VIctory on their own machines, and the fork's first nine hours saw 483 pull requests, three of them merged. The code is being written in the open, and a lot of it is being written with AI help, which is part of why it is moving this fast.</p>
<p>One tester's log line shows where the time goes. On an RTX 5060 Ti, a single frame took 390.6 milliseconds, about 2.6 frames per second: 129.6 milliseconds preparing the frame, 187.3 on the graphics card, and 66.3 copying it back. That breakdown is why the frame rate is stuck in single digits. The card is not the only bottleneck, and fixing one part alone moves the frame rate by only 0 to 7 percent, according to victory-fork's own notes. About 24,000 shader programs need translating, and roughly 100 to 300 are still untranslated, depending on the count.</p>

<h2>What "playable" still means</h2>
<p>The tracker defines playable as 20 frames per second or better for 30 minutes without a crash, and no project has met it. Its best estimate is that a project reaches that bar in about a day, around the evening of November 26. That is the tracker's estimate, not a promise, and it is based on the current rate of progress holding. The gap is real: the fastest confirmed runs are at roughly half the frame rate bar, and the longest sessions are at a third of it.</p>
<p>The picture is also still wrong in ways that matter. Shadowed areas are black in most builds, because the game's ray-traced lighting has no direct equivalent on PC graphics cards. Some forks use a stand-in light instead, which lights the scene but flattens it. VIctory-Belobug-AMD reports the closest picture so far, lit and whole with the game's own sun and lamp shadows drawn, at 3 to 5 frames per second, but its in-game phone is broken and about 380 draws per frame are dropped.</p>

<h2>A reported letter from Rockstar</h2>
<p>One private build's developer has reportedly stopped showing his work. The tracker reports that omonkey, a private build based on victory-fork running at about 5 frames per second in the opening prison scene, stopped streaming after its developer said he had received a letter from Rockstar. The letter is unpublished and Rockstar has not commented, so treat the report as unconfirmed. It fits the pattern of the last two days, though: Take-Two moved against Leonida on GitHub and Discord, and the projects still standing are the ones that stay quiet or stay open source.</p>

<h2>What this means for you</h2>
<p>Nothing about this changes what you can actually do today. There is no public download of a working build, no playable version, and no official PC version. The projects need the leaked Xbox build to run at all, and the only way to get that build is a leak Rockstar and Take-Two are actively taking down. Any site offering a GTA 6 PC download, installer or "port" is not selling a real product, and the files going around are often malware. Our <a href="../gta-6-pc-leak/">leak explainer</a> covers the fake download sites in detail.</p>
<p>The official PC version is still unannounced. GamesBeat reported in October that Rockstar is aiming for the first quarter of 2027, and the outlet stood by that window in a November 18 update, but Rockstar has not confirmed it. We update this page when the race moves or when Rockstar says anything new.</p>
""",
sources=[
("TweakTown: GTA 6 PC port takedown confirmed, Take-Two cites Rockstar's ban on reverse engineering", "https://www.tweaktown.com/news/114877/gta-6-pc-port-takedown-confirmed-take-two-cites-rockstars-ban-on-reverse-engineering/index.html"),
("Decrypt: Take-Two hits GTA 6 PC port Leonida with DMCA, taking down 3,007 GitHub repos", "https://decrypt.co/383935/take-two-hits-gta-6-pc-port-leonida-with-dmca-taking-down-3007-github-repos"),
("NotebookCheck: GTA 6 PC ports reach gameplay despite Take-Two's GitHub DMCA", "https://www.notebookcheck.net/GTA-6-PC-ports-reach-gameplay-despite-Take-Two-s-GitHub-DMCA.1459752.0.html"),
("GTA VI PC Race tracker: live standings of unofficial PC ports, checked November 25, 2026", "https://vuyp.github.io/gta6-pc-race/"),
],
),
]
