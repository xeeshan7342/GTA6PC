"""Batch 1, November 27, 2026: the first unofficial GTA 6 PC mod menu (Viper trainer) and
dedicated launcher, plus the sentencing of Arion Kurtaj, the hacker behind the 2022 GTA 6 leak."""

POSTS_DAILY_20261127_B1 = [
dict(
slug="gta-6-pc-mod-menu-launcher",
short="Mod menu, Nov 27",
title="GTA 6 PC Mod Menu and Launcher: Viper Trainer and the Suco Launcher Explained",
h1="GTA 6 PC mod menu and launcher explained: Viper trainer and the Suco launcher",
desc="The first unofficial GTA 6 PC mod menu, Viper, and a dedicated launcher appeared on November 26, 2026. Here is what they do, how they perform, and why they are debugging tools, not a playable PC version.",
kicker="Port Race",
lede="Three days after the missing GTA 6 Xbox executable surfaced, the unofficial PC port effort grew its first tools. A mod menu called Viper and a dedicated PC launcher were both demonstrated on November 26, 2026. Neither makes the game playable, and neither is something you should download, but together they show how fast the fan effort is moving.",
img_alt="GTA 6 PC mod menu poster showing the Viper trainer and the Suco launcher",
tldr="On November 26, 2026, community developers demonstrated the first unofficial GTA 6 PC mod menu, a trainer called <strong>Viper</strong>, and a dedicated PC launcher. Both run on top of unfinished unofficial builds: the launcher demo averaged about <strong>10 fps</strong>, and the fastest community forks run at about <strong>20 fps</strong> with visual bugs. There is still no official PC version, no public release of these tools, and nothing safe to download.",
faq=[("What is the GTA 6 PC mod menu?", "It is a trainer called Viper, the first unofficial mod menu for the fan-made GTA 6 PC port, demonstrated on November 26, 2026 in footage shared by X user cccurrenccc. Its interface resembles GTA 5 mod menus, and it was built mainly for debugging, with five categories covering vehicle spawning, character stats, vehicle customization, weapon assignment, and world customization."), ("Can I download the Viper trainer?", "No. No public release of Viper has been confirmed. Only demo footage has been shown. Anything offered as a Viper download is unverified and should be treated as a likely scam or malware risk."), ("What is the Suco launcher?", "It is a dedicated launcher for the unofficial GTA 6 PC build, demonstrated by Brazilian streamer Suco on November 26, 2026. In the demo the game averaged about 10 frames per second and occasionally dropped to 2 fps, on a PC with a Radeon RX 7900 XTX graphics card and 64 GB of RAM."), ("Does the mod menu mean GTA 6 is playable on PC?", "No. The tools run on top of unfinished unofficial builds. The fastest community forks report about 20 fps with missing water, broken lighting, and other visual bugs, and the main VIctory project still lists its first mission intro at 1 to 2 seconds per frame. Rockstar has announced no official PC version."), ("What happened to the CGBJ launcher?", "CGBJ published a Windows launcher and runtime in a public GitHub repository early on November 26, 2026, and the repository returned a 404 error on a later check. The cause is unknown, and GitHub had published no takedown notice naming the repository as of November 27. PortWatch moved CGBJ back to its list of private builds.")],
body="""
<h2>What the Viper trainer is</h2>
<p>GameGPU reported on November 26, 2026 that a demo of the first working mod menu for the unofficial GTA 6 PC port had appeared online. The menu is called Viper, and the published video shows part of a story mission in a swampy area, with the player opening the trainer interface on screen and testing its functions during the mission.</p>
<p>Viper's menu is split into five main categories: vehicle spawning, character stat management, vehicle customization, weapon assignment, and game world customization. GameGPU reports that the trainer's database already recognizes 642 vehicle models and 52 types of weapons, and the player section lists options for health, invulnerability, ammunition, stamina, and speed. The community noted that the cutscene in the demo was likely sped up to look smoother, and some environmental objects still loaded with delays.</p>
<p>Separately, footage shared by X user cccurrenccc shows an in-game mod menu running on an unofficial GTA 6 PC build. TweakTown and Notebookcheck both covered the clip, and both note that the interface resembles mod menus built for GTA 5 over the years. The current implementation was created mainly for debugging, not for playing the game.</p>

<h2>The Suco launcher</h2>
<p>The same day brought a second tool. Brazilian streamer Suco demonstrated a dedicated launcher for the unofficial PC version of GTA 6. Notebookcheck reports that the build in the demo averaged around 10 frames per second and occasionally dropped to just 2 fps, despite running on a system with an AMD Radeon RX 7900 XTX graphics card and 64 GB of system memory.</p>
<p>A launcher sounds like a small thing, but it matters for this project. Until now, running the unofficial builds has meant manual setup and command line work. A launcher that starts the game and manages its files is the kind of tool that appears when a project stops being an experiment and starts being something other people are expected to run. It is still early, and the performance in the demo shows how far there is to go, but the direction is clear.</p>

<h2>Why modders build tools before the game works</h2>
<p>It looks strange to build a mod menu for a game that barely runs, but there is a practical reason. GameGPU notes that the ability to load any vehicle, weapon, or effect model at a single point speeds up the search for graphical errors and lets developers benchmark the stability of the compatibility layers that render the Xbox files. Spawning a vehicle is faster than playing to the point where one appears. Testing every weapon is faster with a menu than by finding them in the world.</p>
<p>That is also why the first menu is a trainer, not a gameplay mod. Trainers exist to change game state on demand, which is exactly what developers need while the port is broken. The Viper menu is a debugging tool that happens to look like a cheat menu, because the two jobs use the same controls.</p>

<h2>CGBJ published a launcher, then its repository went dark</h2>
<p>The fastest project in the race had a confusing day of its own. MakeTechEasier reports that CGBJ published a Windows x64 launcher and runtime in a public GitHub repository early on November 26, 2026, at 06:35 UTC, with a release recording the build and a checksum. The repository and the release page returned a 404 error on a later check. The cause is unknown, and as of the community tracker's check at 00:21 UTC on November 27, GitHub had published no takedown notice naming the repository. PortWatch moved CGBJ back to its list of private builds the same day, and a pinned note described the code as taken down temporarily.</p>
<p>XDA Developers reported that it was unclear whether the team made the project private to avoid a potential takedown notice or whether Rockstar's legal department acted. Our <a href="../gta-6-pc-port-november-26-update/">November 26 update</a> covered CGBJ reaching 91 percent completion at 25 fps in its own tests, and a packaged build claiming to be CGBJ circulating on torrent sites. That torrent build is unverified, and the tracker warns that downloads offered as GTA 6 for PC have carried malware.</p>
<div class="warn"><strong>Do not download any build, launcher, or trainer claiming to be a GTA 6 PC port.</strong> No version of Viper has a confirmed public release, the CGBJ packages on torrent sites are unverified, and fake installers using the port race as bait are already circulating. The only safe position is to watch and wait.</div>

<h2>Where performance stands</h2>
<p>The tools arrived while the frame rate story kept moving. TweakTown reported on November 26 that community builds on VIctory, the open-source compatibility layer that runs GTA 6's Xbox code directly on Windows, have jumped to around 20 fps. PC Games Hardware reported that a public fork called VIctory-NVIDIA averages 20 to 22 fps indoors on an RTX 5070 and a Ryzen 7 9800X3D, though it uses the Xbox Series S graphics profile, rendering internally at 960 by 540 before upscaling, with ray tracing largely disabled. Footage posted to X by MrPoulpy shows a jet ski sequence at 19 to 23 fps on the coast and about 12 fps in town, with missing shoreline water and magenta streaks on a road. TweakTown's author wrote that he could not independently verify who made the build or what hardware it ran on, so treat the clip as a claim with video attached, not a benchmark.</p>
<p>The main VIctory project itself is still far behind its forks. Its README, updated November 25, still lists the first mission intro at 1 to 2 seconds per frame. Another fork, AvatarManz's VIctory-7900XTX, ran for 41 minutes without a crash, with indoor scenes at 13 to 20 fps and the first boat mission at 19 to 22 fps on a Radeon RX 7900 XTX. Our <a href="../gta-6-pc-port-tracker-portwatch/">PortWatch guide</a> explains how the community tracker scores each project, and our <a href="../gta-6-pc-release-date/">release date page</a> tracks the official position separately: Rockstar has announced no PC version.</p>

<h2>The legal pressure has not stopped the work</h2>
<p>All of this is happening under legal fire. Take-Two filed a DMCA notice on November 24 that took down the Leonida project's network of 3,007 GitHub repositories, and TweakTown notes that several other port repositories have since vanished without a public takedown notice. Leonida itself is still down, and its leads have left the project. Our <a href="../gta-6-pc-port-rockstar-crackdown/">crackdown explainer</a> has the full timeline.</p>
<p>The mod menu and launcher do not change the legal picture. They are built on the same leaked Xbox files, and Take-Two has shown it will act against public repositories. The work continues in private forks and smaller groups, which is also why so many of the claims now come with no public code to check. Treat every frame rate and every demo as a report from the project itself until a build is public and independently tested.</p>

<h2>The bottom line</h2>
<p>November 26 was the day the unofficial GTA 6 PC effort grew tools, not just frames. A trainer, a launcher, and a published runtime all appeared within hours of each other, which is what a maturing project looks like. But none of it is a game you can play. The fastest builds are private or unverified, the public code keeps disappearing, and the only official GTA 6 PC position is still silence from Rockstar. Watch the tools, download nothing.</p>

<h2>Quick answers</h2>
<h3>What is the GTA 6 PC mod menu?</h3>
<p>It is a trainer called Viper, the first unofficial mod menu for the fan-made GTA 6 PC port, demonstrated on November 26, 2026 in footage shared by X user cccurrenccc. Its interface resembles GTA 5 mod menus, and it was built mainly for debugging, with five categories covering vehicle spawning, character stats, vehicle customization, weapon assignment, and world customization.</p>
<h3>Can I download the Viper trainer?</h3>
<p>No. No public release of Viper has been confirmed. Only demo footage has been shown. Anything offered as a Viper download is unverified and should be treated as a likely scam or malware risk.</p>
<h3>What is the Suco launcher?</h3>
<p>It is a dedicated launcher for the unofficial GTA 6 PC build, demonstrated by Brazilian streamer Suco on November 26, 2026. In the demo the game averaged about 10 frames per second and occasionally dropped to 2 fps, on a PC with a Radeon RX 7900 XTX graphics card and 64 GB of RAM.</p>
<h3>Does the mod menu mean GTA 6 is playable on PC?</h3>
<p>No. The tools run on top of unfinished unofficial builds. The fastest community forks report about 20 fps with missing water, broken lighting, and other visual bugs, and the main VIctory project still lists its first mission intro at 1 to 2 seconds per frame. Rockstar has announced no official PC version.</p>
<h3>What happened to the CGBJ launcher?</h3>
<p>CGBJ published a Windows launcher and runtime in a public GitHub repository early on November 26, 2026, and the repository returned a 404 error on a later check. The cause is unknown, and GitHub had published no takedown notice naming the repository as of November 27. PortWatch moved CGBJ back to its list of private builds.</p>
""",
cover=dict(eyebrow="Port Race · Nov 27", title="Viper Trainer Live", sub="The first mod menu and launcher for the unofficial GTA 6 PC builds, and why they are debugging tools.", rows=[("Mod menu", "Viper", True), ("Launcher demo", "10 FPS", False), ("Playable yet", "No", False)]),
related=["gta-6-pc-port-november-26-update", "gta-6-pc-port-tracker-portwatch", "gta-6-pc-port-rockstar-crackdown"],
sources=[
("TweakTown: GTA 6 gets its first unofficial PC mod menu and launcher", "https://www.tweaktown.com/news/114902/gta-6-gets-its-first-unofficial-pc-mod-menu-and-launcher/index.html"),
("Notebookcheck: First unofficial GTA 6 PC mod menu and launcher surface", "https://www.notebookcheck.net/As-GTA-6-PC-port-projects-make-significant-progress-its-first-unofficial-mod-menu-and-launcher-have-surfaced.1461005.0.html"),
("GameGPU: Viper trainer released for the unofficial GTA 6 PC version", "https://en.gamegpu.com/news/igry/poyavilsya-trejner-viper-dlya-spavna-transporta-i-oruzhiya-v-piratskoj-pk-versii-grand-theft-auto-vi"),
("MakeTechEasier: CGBJ GTA 6 PC port launcher published, then GitHub 404", "https://maketecheasier.com/cgbj-gta-6-pc-port-github-404/"),
("TweakTown: GTA 6 PC port hits 20 FPS just days after drawing one frame every two seconds", "https://www.tweaktown.com/news/114905/gta-6-pc-port-hits-20-fps-just-days-after-drawing-one-frame-every-two-seconds/index.html"),
],
),
dict(
slug="gta-6-leak-hacker-arion-kurtaj-sentenced",
short="Hacker sentenced",
title="GTA 6 Hacker Arion Kurtaj Sentenced to Seven Years, Walks Free the Same Day",
h1="GTA 6 hacker Arion Kurtaj sentenced to seven years, walks free the same day",
desc="Arion Kurtaj, the Lapsus$ hacker behind the 2022 GTA 6 leak, was sentenced to seven years at Woolwich Crown Court on November 23, 2026, and released on licence the same day. Here is what happened and why.",
kicker="Leaks",
lede="Four days after GTA 6 launched on consoles, the teenager who leaked it in 2022 finally faced sentencing. Arion Kurtaj, now 21, received seven years at Woolwich Crown Court on November 23, 2026, then walked out of court a free man the same day, because the years he had already spent in a secure hospital and in custody counted toward the sentence.",
img_alt="GTA 6 hacker sentencing poster showing Arion Kurtaj, seven year sentence, released on licence",
tldr="Arion Kurtaj, the Lapsus$ hacker who leaked 90 clips of unfinished GTA 6 footage in 2022, was sentenced to <strong>seven years</strong> at Woolwich Crown Court on November 23, 2026, and released on licence <strong>the same day</strong>. Time already spent in a secure hospital and in custody counted toward the sentence. He is under a <strong>five-year Serious Crime Prevention Order</strong> restricting his online activity, including bans on Telegram and Discord.",
faq=[("Who is Arion Kurtaj?", "Arion Kurtaj is a 21-year-old former member of the hacking group Lapsus$. In September 2022, aged 17, he broke into Rockstar Games and leaked 90 clips containing nearly an hour of unfinished GTA 6 gameplay, posting them online as TeaPotUberHacker."), ("Why did he walk free after a seven-year sentence?", "The court first considered a nine-year term, then cut two years for time Kurtaj spent under a hospital order. Time in a secure hospital and on remand counted toward the sentence, and he had already served most of the term by the day he was sentenced, so he was released on licence, under supervision, the same day."), ("What restrictions is he under?", "The BBC reported from the hearing that Kurtaj must comply with a five-year Serious Crime Prevention Order restricting his online activity, including bans on using Telegram and Discord. Breaking the conditions of his release could send him back to prison."), ("What did the hack cost Rockstar?", "Rockstar said the breach cost the company about $5 million to recover from, plus thousands of hours of staff time. Kurtaj also threatened to release the game's source code unless Rockstar contacted him on Telegram."), ("Is Kurtaj connected to the 2026 Cyberleek leak?", "There is no evidence of a link. The 2026 Xbox build leak came from a separate, anonymous actor calling itself Cyberleek, which has been releasing GTA 6 material since August 2026. Kurtaj's case concerns the 2022 breach only.")],
body="""
<h2>The sentence</h2>
<p>Arion Kurtaj, 21, was sentenced at Woolwich Crown Court in London on Monday, November 23, 2026. The court gave him seven years in prison for a series of cyberattacks, including the 2022 breach of Rockstar Games that leaked unfinished GTA 6 footage. He walked out of court a free man the same day, released on licence, because the time he had already spent in a secure hospital and in custody counted toward the sentence.</p>
<p>The judge, Mr Justice Turner, had first considered a nine-year term, then cut two years to account for the time Kurtaj spent under a hospital order. The BBC reported from the hearing that Kurtaj must comply with a five-year Serious Crime Prevention Order restricting his online activity, including bans on using Telegram and Discord. The judge told him: "You are a very talented young man. Don't let this happen again." He could be sent back to prison if he breaks the conditions of his release.</p>
<p>The timing was striking. Sentencing came four days after GTA 6 launched worldwide on November 19, more than four years after the hack that first showed the game to the public.</p>

<h2>What he did in September 2022</h2>
<p>Kurtaj was 17 when he broke into Rockstar's systems. He was staying at a Travelodge hotel in Bicester, England, under police protection and on bail for other hacking offences, when he used an Amazon Fire TV Stick, a phone, and the hotel's Wi-Fi to get into Rockstar's internal systems. He stole 90 clips containing nearly an hour of unfinished GTA 6 gameplay, then posted them online under the username TeaPotUberHacker.</p>
<p>The footage revealed Vice City and the game's two protagonists long before Rockstar had announced them. Kurtaj also broke into Rockstar's Slack messaging system and threatened to release the game's source code unless the company contacted him on Telegram. Rockstar refused, and he published the stolen material. Rockstar later said the breach cost the company about $5 million to recover from, plus thousands of hours of staff time.</p>
<p>Kurtaj was a member of the international hacking group Lapsus$, which also targeted Uber, Revolut, and telecoms company BT/EE. The charges he eventually pleaded guilty to covered hacks on all of those companies, committed when he was 16 and 17.</p>

<h2>The long road to sentencing</h2>
<p>The case took more than four years to reach a sentence, because of Kurtaj's health. After a medical assessment found him unfit to stand trial, he was placed under an indefinite hospital order in December 2023. A jury that month found he had carried out the acts alleged. He stayed in a secure hospital for about two years, until a later assessment found him fit to plead and the hospital order was lifted in January 2026. He was then moved to a conventional prison.</p>
<p>On November 16, 2026, Kurtaj pleaded guilty to six offences at Woolwich Crown Court, including fraud and offences under the Computer Misuse Act, according to the City of London Police. Sentencing followed a week later, on November 23.</p>

<h2>Why a seven-year sentence meant walking free</h2>
<p>The result confuses people, but it follows normal UK sentencing rules. Time spent in custody and under a hospital order counts toward a sentence. Kurtaj had already spent more than four years in a secure hospital and in prison, so most of the seven-year term was already served by the day he was sentenced. The court also reduced the starting term from nine years to seven to reflect the hospital time.</p>
<p>Release on licence is not the same as being cleared. Kurtaj remains under supervision, must follow conditions set by the court, and can be recalled to prison if he breaks them. The five-year Serious Crime Prevention Order adds further restrictions on his online activity, and the ban on Telegram and Discord removes the two platforms he used during the Rockstar hack.</p>

<h2>What this means for the 2026 leaks</h2>
<p>Kurtaj has no known connection to the leaks of 2026. The Xbox build leak that put a near-complete GTA 6 build online in November 2026 came from a different, anonymous actor calling itself Cyberleek, which has been releasing GTA 6 material since August. Our <a href="../who-is-cyberleek/">Cyberleek explainer</a> covers that group separately, and our <a href="../gta-6-leaks-timeline/">leaks timeline</a> traces every major GTA 6 leak from the 2022 hack to the Xbox build.</p>
<p>The Kurtaj sentence still matters for the 2026 scene, because it shows the courts do reach leakers, even years later. Rockstar and Take-Two are actively pursuing the 2026 leakers too. Take-Two filed a DMCA notice on November 24 that removed the Leonida port project's network of 3,007 GitHub repositories, and the hunt for the source of the Xbox build leak continues. Our <a href="../gta-6-pc-port-rockstar-crackdown/">crackdown explainer</a> has the details.</p>
<p>The 2022 leak and the 2026 leak also bookend the same story. The first showed an unfinished game to the world and cost Rockstar millions. The second handed out a near-complete console build days after launch. Kurtaj's case is now closed. Cyberleek's is not.</p>

<h2>The bottom line</h2>
<p>Arion Kurtaj leaked GTA 6 as a teenager, spent more than four years in a secure hospital and in custody, pleaded guilty, and was sentenced to seven years on November 23, 2026. He walked free the same day because that time was already served, and he now lives under five years of online restrictions. The game he leaked is out, the leaker is free under supervision, and the next leak case is still open.</p>

<h2>Quick answers</h2>
<h3>Who is Arion Kurtaj?</h3>
<p>Arion Kurtaj is a 21-year-old former member of the hacking group Lapsus$. In September 2022, aged 17, he broke into Rockstar Games and leaked 90 clips containing nearly an hour of unfinished GTA 6 gameplay, posting them online as TeaPotUberHacker.</p>
<h3>Why did he walk free after a seven-year sentence?</h3>
<p>The court first considered a nine-year term, then cut two years for time Kurtaj spent under a hospital order. Time in a secure hospital and on remand counted toward the sentence, and he had already served most of the term by the day he was sentenced, so he was released on licence, under supervision, the same day.</p>
<h3>What restrictions is he under?</h3>
<p>The BBC reported from the hearing that Kurtaj must comply with a five-year Serious Crime Prevention Order restricting his online activity, including bans on using Telegram and Discord. Breaking the conditions of his release could send him back to prison.</p>
<h3>What did the hack cost Rockstar?</h3>
<p>Rockstar said the breach cost the company about $5 million to recover from, plus thousands of hours of staff time. Kurtaj also threatened to release the game's source code unless Rockstar contacted him on Telegram.</p>
<h3>Is Kurtaj connected to the 2026 Cyberleek leak?</h3>
<p>There is no evidence of a link. The 2026 Xbox build leak came from a separate, anonymous actor calling itself Cyberleek, which has been releasing GTA 6 material since August 2026. Kurtaj's case concerns the 2022 breach only.</p>
""",
cover=dict(eyebrow="Leaks · Nov 27", title="Seven Years, Free the Same Day", sub="The hacker behind the 2022 GTA 6 leak was sentenced at Woolwich Crown Court and released on licence.", rows=[("Sentence", "7 years", True), ("Pleaded guilty", "Nov 16", False), ("Online ban", "5 years", False)]),
related=["gta-6-leaks-timeline", "who-is-cyberleek", "gta-6-pc-leak"],
sources=[
("Dexerto: GTA 6 hacker released from prison after judge warns him not to do it again", "https://www.dexerto.com/gta/gta-6-hacker-released-from-prison-after-judge-warns-him-not-to-do-it-again-3430673/"),
("TweakTown: GTA 6 hacker sentenced to seven years, walks free the same day after Rockstar Games leak", "https://www.tweaktown.com/news/114888/gta-6-hacker-sentenced-to-seven-years-walks-free-the-same-day-after-rockstar-games-leak/index.html"),
("Polygon: GTA 6 hacker officially walks free after judge's final warning", "https://www.polygon.com/gta-6-hacker-released-prison-sentence/"),
("Neowin: GTA 6 hacker sentenced to seven years in prison, but released on the same day", "https://www.neowin.net/news/gta-6-hacker-sentenced-to-seven-years-in-prison-but-released-on-the-same-day/"),
("Help Net Security: GTA 6 hacker sentenced to seven years and released the same day", "https://www.helpnetsecurity.com/2026/11/24/gta-vi-hacker-sentenced-seven-years-released-on-licence/"),
],
),
]
