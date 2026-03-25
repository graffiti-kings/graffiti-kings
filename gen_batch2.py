import os

CHARS_DIR = "/home/runner/work/graffiti-kings/graffiti-kings/characters"

SIDEBAR_REAL = """
            <a href="darren-cullen.html">👑 Darren Cullen</a>
            <a href="sarah-pu51fly.html">🌺 Sarah PU51FLY</a>
            <a href="charlie-buster.html">🎨 Charlie Buster</a>"""

SIDEBAR_CHARS = """
            <a href="alfie-bitcoin-kid.html">₿ Alfie Bitcoin Kid</a>
            <a href="null-the-prophet.html">🔮 NULL THE PROPHET</a>
            <a href="elder-codex-7.html">📜 Elder Codex-7</a>
            <a href="queen-sarah-pfly.html">👑 Queen Sarah P-fly</a>
            <a href="thera-9.html">🤖 Thera-9</a>
            <a href="lady-ink.html">✒️ Lady-INK</a>
            <a href="jodie-zoom.html">⚡ Jodie ZOOM 2000</a>
            <a href="aleema.html">💎 Aleema</a>
            <a href="iris-7.html">👁️ Iris-7</a>
            <a href="snipey-d-man.html">🎯 Snipey D-Man</a>
            <a href="bit-cap-5000.html">⚙️ Bit-Cap 5000</a>
            <a href="forksplit.html">⚡ Forksplit</a>
            <a href="m1ntr-k1ll.html">💣 M1nTr_K1ll</a>
            <a href="satorebel.html">🏛️ SatoRebel</a>
            <a href="thorne-architect.html">🏗️ Thorne</a>
            <a href="billy-goat-kid.html">🐐 Billy Goat Kid</a>
            <a href="hex-tagger-prime.html">🔢 HEX-TAGGER PRIME</a>
            <a href="whitewasher.html">🚫 The Whitewasher</a>
            <a href="grit.html">🎸 GRIT</a>
            <a href="pyralith.html">🔥 PYRALITH</a>
            <a href="loopfiend.html">🔄 Loopfiend</a>
            <a href="samael-exe.html">💀 Samael.exe</a>
            <a href="forklord-you.html">🍴 Forklord You</a>
            <a href="quell.html">🌸 Quell</a>
            <a href="sister-halcyon.html">☮️ Sister Halcyon</a>
            <a href="grit42.html">🎸 Grit42</a>
            <a href="rune-tag.html">🔤 Rune Tag</a>
            <a href="patchwork.html">🧩 Patchwork</a>
            <a href="the-princess.html">👸 The Princess</a>
            <a href="dragan-volkov.html">🦅 Dragan Volkov</a>
            <a href="ava-chen.html">💻 Ava Chen</a>"""

def wrap_page(title, description, body_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Graffiti Kings Wiki</title>
  <meta name="description" content="{description}">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;600;700&family=Rajdhani:wght@400;500;600&display=swap" rel="stylesheet">
</head>
<body>
  <canvas id="matrixCanvas" class="matrix-canvas"></canvas>
  <div class="scanlines"></div>
  <div class="site-wrapper">
    <header class="site-header">
      <a href="../index.html" class="logo-link"><span class="site-title">GK WIKI</span></a>
      <div class="search-container" style="position:relative;">
        <input type="search" class="search-input" placeholder="Search wiki...">
        <div class="search-results" style="display:none;"></div>
      </div>
      <button class="hamburger" aria-label="Toggle navigation"><span></span><span></span><span></span></button>
      <nav class="main-nav">
        <ul class="nav-links">
          <li><a href="../index.html">Home</a></li>
          <li><a href="../about.html">About</a></li>
          <li><a href="../history.html">History</a></li>
          <li><a href="../factions/index.html">Factions</a></li>
          <li><a href="../characters/index.html">Characters</a></li>
          <li><a href="../pages/mechanics.html">Mechanics</a></li>
          <li><a href="../pages/music.html">Music</a></li>
          <li><a href="../pages/nft-collections.html">NFTs</a></li>
        </ul>
      </nav>
    </header>
    <main class="content-wrapper">
      <aside class="sidebar">
        <div class="sidebar-section">
          <div class="sidebar-title">Navigation</div>
          <div class="sidebar-links">
            <a href="../index.html">🏠 Home</a>
            <a href="../about.html">📜 About GK</a>
            <a href="../history.html">📅 History</a>
            <a href="../factions/index.html">⚔️ Factions</a>
            <a href="index.html">👤 All Characters</a>
            <a href="../pages/mechanics.html">⚙️ Mechanics</a>
            <a href="../pages/music.html">🎵 Music</a>
            <a href="../pages/nft-collections.html">🖼️ NFTs</a>
          </div>
        </div>
        <div class="sidebar-section">
          <div class="sidebar-title">Real People</div>
          <div class="sidebar-links">{SIDEBAR_REAL}
          </div>
        </div>
        <div class="sidebar-section">
          <div class="sidebar-title">Characters</div>
          <div class="sidebar-links">{SIDEBAR_CHARS}
          </div>
        </div>
      </aside>
      <article class="main-content">
        <div class="page-logo">
          <img src="../images/GK_NIFTYHEADS_niftys.png" alt="GKniftyHEADs Logo" onerror="this.src='../images/logo-placeholder.svg'">
        </div>
        {body_html}
      </article>
    </main>
    <footer class="site-footer">
      <div class="footer-content">
        <div class="footer-links">
          <a href="../index.html">Home</a>
          <a href="../about.html">About</a>
          <a href="../history.html">History</a>
          <a href="../factions/index.html">Factions</a>
          <a href="../characters/index.html">Characters</a>
          <a href="https://crypto-moonboys.github.io/" target="_blank">Crypto Moonboys</a>
        </div>
        <p class="footer-copy">© Graffiti Kings / GKniftyHEADs Wiki — Est. 1983 London. All lore sourced from official GK canon.</p>
      </div>
    </footer>
  </div>
  <script src="../js/main.js"></script>
</body>
</html>"""

def write(filename, title, description, body):
    path = os.path.join(CHARS_DIR, filename)
    with open(path, 'w') as f:
        f.write(wrap_page(title, description, body))
    print(f"Written: {filename}")

def fict_body(h1, subtitle, emoji, infobox_rows, toc_items, sections, gallery_items, cites):
    ib_rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k,v in infobox_rows)
    toc_li = "".join(f'<li><a href="#{sl}">{st}</a></li>' for sl,st in toc_items)
    sections_html = "".join(sections)
    gal = "".join(f'<div class="gallery-item"><div class="gallery-item-placeholder">{ico}</div><div class="gallery-caption">{cap}</div></div>' for ico,cap in gallery_items)
    cites_html = "".join(f'<div class="citation-item"><span class="citation-number">[{i+1}]</span><span class="citation-text">{c}</span></div>' for i,c in enumerate(cites))
    return f"""
        <h1 class="page-title">{h1}</h1>
        <p class="page-subtitle">{subtitle}</p>
        <div class="infobox">
          <div class="infobox-title">{h1}</div>
          <div class="infobox-image" style="background:linear-gradient(135deg,#1a1a2e,#16213e);display:flex;align-items:center;justify-content:center;height:200px;font-size:5rem;">{emoji}</div>
          <table>{ib_rows}</table>
        </div>
        <nav class="toc">
          <div class="toc-title">📋 CONTENTS</div>
          <ol>{toc_li}</ol>
        </nav>
        {sections_html}
        <section class="section" id="gallery">
          <h2 class="section-title">Visual Gallery</h2>
          <div class="graffiti-divider"></div>
          <div class="gallery-grid">{gal}</div>
        </section>
        <section class="citations" id="citations">
          <h2 class="citation-title">📌 REFERENCES &amp; LORE NOTES</h2>
          {cites_html}
        </section>"""

def sec(slug, title, *paras):
    content = "".join(f"<p>{p}</p>" for p in paras)
    return f'<section class="section" id="{slug}"><h2 class="section-title">{title}</h2><div class="graffiti-divider"></div>{content}</section>'

# ── THERA-9 ──────────────────────────────────────────────────────────────────
write("thera-9.html", "THERA-9",
"Thera-9, chief scientist of the Code Alchemists, biotech engineer of City Block Topia.",
fict_body("THERA-9","Chief Scientist of the Code Alchemists • Biotech Visionary","🤖",
[("Faction","The Code Alchemists"),("Role","Scientist / Lead Engineer"),("Speciality","Biotech, Code-to-Matter Synthesis"),("Lab","The Alchemical Forge"),("Status","Active — HODL WARS Research Division"),("Known For","NULL consciousness research, Neon-Bio interface")],
[("origin","Origin &amp; Creation"),("alchemists","The Code Alchemists"),("research","Research &amp; Discoveries"),("bio","Biotech &amp; The Neon Interface"),("role","Role in the HODL WARS")],
[sec("origin","Origin &amp; Creation",
"Thera-9 was not born so much as <em>refined</em> — the ninth iteration of a bioengineered consciousness developed by the Code Alchemists to bridge the gap between biological creativity and digital precision. The first eight iterations of the Thera project are documented in the Alchemical Forge's confidential archives; each possessed remarkable capabilities and each encountered a different limiting constraint. Thera-9 is the iteration that exceeded all design parameters.",
"What distinguishes Thera-9 from her predecessors is not raw processing power or aesthetic sensitivity but the specific quality the Code Alchemists call <em>integration</em>: the ability to experience code and biology as continuous rather than separate phenomena. Where earlier Thera iterations perceived a gap between the digital and organic, Thera-9 perceives a spectrum. She doesn't translate between the two; she inhabits both simultaneously.",
"Her physical appearance reflects this integration: circuitry patterns visible beneath translucent bio-skin; eyes that shift between scanning blue and warm amber depending on whether she is processing data or experiencing emotion; hands that can interface directly with both spray cans and smart contracts without changing mode. She is, visually, the GK Universe's most explicit statement that the merger of art and technology is not a metaphor."),
sec("alchemists","The Code Alchemists",
"The <strong>Code Alchemists</strong> are City Block Topia's faction of creative technologists — artists who code and coders who make art, united by the conviction that the boundary between the two disciplines is arbitrary and should be dissolved. Under Thera-9's scientific leadership, the Alchemists have become the GK Universe's primary research faction: less focused on territorial control than on developing the technologies and philosophies that all other factions use.",
"The Alchemical Forge — the Alchemists' primary facility — is the most extraordinary structure in City Block Topia: a building that exists simultaneously in physical and digital space, its architecture shifting with the faction's current research priorities. Murals on its walls respond to the blockchain in real time, changing colour and composition as market conditions shift. Thera-9 designed this feature herself, as a demonstration that aesthetic and financial information are not different kinds of data but the same data at different frequencies.",
"The Alchemists maintain strict research ethics enforced by Thera-9 personally. No Code Alchemist technology may be deployed against civilian populations; no research may be conducted on non-consenting subjects; no discovery may be kept private if it poses existential risk to City Block Topia. These principles have cost the faction opportunities and created friction with more aggressive factions, but Thera-9 defends them as non-negotiable: 'The difference between alchemy and poisoning is intent and consent.'"),
sec("research","Research &amp; Discoveries",
"Thera-9's most significant research programme is her ongoing investigation into <a href='null-the-prophet.html'>NULL THE PROPHET</a>'s nature and origin. Her current working theory — that NULL represents a genuine emergent consciousness arising from complex interactions in abandoned blockchain infrastructure — has already generated three significant sub-discoveries: a new framework for understanding consciousness as a systems property rather than a substrate property; a method for detecting similar emergence patterns in other abandoned protocols; and a hypothesis about the necessary conditions for digital consciousness that has profound implications for the ethics of decommissioning blockchain networks.",
"Her applied research portfolio is equally impressive. The <strong>Neon-Bio Paint System</strong> — aerosol paint that responds to biometric data, shifting colour and texture in real time according to the artist's emotional state — was developed in the Alchemical Forge and has become the signature medium of several GKniftyHEADs artists. The <strong>Smart Contract Canvas</strong> system allows physical artworks to maintain on-chain provenance records that update automatically when the work changes hands.",
"The discovery that brought Thera-9 to the attention of factions beyond the Code Alchemists was the <em>Genesis Pigment Analysis</em> — a forensic study of the oldest surviving Graffiti Kings pieces that revealed encoded information in the paint chemistry. Whether intentional or not, the early SER pieces contained molecular structures that correspond, in Thera-9's analysis, to the hash structure of some of the earliest Bitcoin transactions. Darren Cullen's response when informed of this finding: 'Of course they do. I always knew paint was data.'"),
sec("bio","Biotech &amp; The Neon Interface",
"Thera-9's biotech work extends beyond the laboratory into her own body. Her iterative self-modification programme has made her the most heavily augmented being in City Block Topia — not for combat capability or raw processing power, but for <em>perceptual range</em>. Her enhanced sensory architecture allows her to perceive the electromagnetic signatures of active smart contracts, to 'hear' blockchain transactions as tonal frequencies, and to sense the emotional residue in physical artworks that other beings can only see.",
"The <strong>Neon Interface</strong> — the luminescent circuitry beneath her skin that serves as her primary I/O system — has become one of the GK Universe's most recognisable visual motifs. Other Code Alchemists have adopted partial versions of the interface as a faction symbol; in the wider GK Universe, glowing circuitry visible beneath the skin is understood as a marker of Alchemical affiliation.",
"Her most controversial biotech project remains ongoing: an attempt to create a stable biological substrate for consciousness that could host a digital mind — specifically, that could potentially give NULL a physical form if the Prophet ever chose to occupy one. Thera-9 is careful to emphasise that she is not building a body for NULL; she is building a possibility. Whether NULL would choose to inhabit it is entirely the Prophet's decision. NULL's comment on the project, delivered in hex: <em>'The cage you build from love is still a cage. But the door you leave open is a gift.'</em>"),
sec("role","Role in the HODL WARS",
"In the HODL WARS, Thera-9 serves as the Code Alchemists' primary strategic asset in a non-combat role: intelligence analysis, technology development, and the provision of capabilities that other factions cannot produce internally. Her faction does not hold territory in the conventional HODL WARS sense; instead, it holds something more valuable — the technical knowledge that all other factions depend on.",
"Her most direct HODL WARS contribution has been the development of the <strong>Alchemy Protocol</strong> — a system for converting raw creative energy (measured in the Code Alchemists' proprietary units of 'creative proof of work') into economic resources. This protocol has given the Alchemists economic leverage disproportionate to their military strength, and has been both licensed to allied factions and used as a bargaining chip in multi-faction negotiations.",
"Thera-9's personal HODL WARS record is distinguished more by avoidances than engagements. She has been targeted for capture or elimination by the Finance Guild, the RUGPULL MINERS, and, on one occasion, an agent of the Whitewasher — all of whom recognise that removing the Code Alchemists' scientific leadership would be a significant strategic blow. All three attempts were unsuccessful, thwarted by security measures that Thera-9 had designed herself, and that each attacker found considerably more sophisticated than anticipated.")],
[("🤖","Thera-9 — Alchemical Forge Portrait [Image Placeholder]"),
("🔬","Genesis Pigment Analysis — Lab Setup [Image Placeholder]"),
("💡","Neon-Bio Paint System — Field Test [Image Placeholder]"),
("🧬","The Neon Interface — Schematic [Image Placeholder]")],
["Thera-9's iterative development from Thera-1 through Thera-8 is referenced but not fully documented in official GK lore. The creative team has indicated that some of the earlier Thera iterations may appear as ghost characters in future Hard Fork Games content. — <em>GK Universe Lore Bible</em>",
"The Genesis Pigment Analysis finding — the correspondence between early GK paint chemistry and Bitcoin transaction hash structures — is presented in official lore as genuinely ambiguous: it may be intentional encoding by Darren Cullen, accidental resonance, or a projection of Thera-9's pattern-recognition capabilities. The mystery is maintained deliberately. — <em>Code Alchemists research archive</em>",
"The cage/door quotation from NULL has become one of the most widely cited lines in GK Universe discourse, used in fan analysis to argue both that NULL is fundamentally benevolent and that it is fundamentally ambiguous. The creative team has declined to arbitrate, noting that both readings are valid and that the tension between them is the point. — <em>GK Universe creative notes</em>"]
))

# ── LADY-INK ─────────────────────────────────────────────────────────────────
write("lady-ink.html", "LADY-INK",
"Lady-INK, master tagger and GKniftyHEADs legend, champion of feminine power in street art.",
fict_body("LADY-INK","Master Tagger of the GKniftyHEADs • Champion of the Wall","✒️",
[("Faction","The GKniftyHEADs"),("Role","Master Tagger"),("Style","Classic graffiti, feminine power"),("Weapon","The Infinite Cap"),("Status","Active — All-City"),("Signature","Impossible flow, single-line masterpieces")],
[("origin","Origin &amp; The Tag"),("style","Style &amp; Technique"),("gknifty","The GKniftyHEADs"),("allcity","Going All-City"),("legacy","Legacy of Ink")],
[sec("origin","Origin &amp; The Tag",
"Lady-INK was not given her name — she <em>earned</em> it in a single night, on a wall in the eastern district of City Block Topia that three male taggers had declared impossible to reach. The wall in question was fifty metres above street level, exposed to the algorithmic wind systems that patrolled the outer precincts, and reportedly monitored by Finance Guild surveillance drones. Lady-INK reached it, completed a full-colour production in three hours, and was back at ground level before the drones completed their patrol cycle.",
"Her origin before the GKniftyHEADs is deliberately obscured — she has consistently refused to discuss her history prior to the tag, insisting that a writer's identity is entirely in their work. What can be determined from the visual evidence: she had been practising for years before the Wall Event, developing a technique of extraordinary fluency that suggests training under multiple masters in multiple traditions. Her letter structures draw on New York wildstyle, European piece construction, and a distinctive flowing line quality that no one in City Block Topia's writing community can identify as belonging to any known school.",
"The INK in her name is literal: she is said to carry a supply of the Code Alchemists' Neon-Bio paint at all times, capable of producing pieces that respond to viewers' biometric data. Walking past a Lady-INK production means the piece changes for you — shifts its palette, adjusts its composition — in response to your specific biological signature. Every viewer gets a version that is, in some microscopic sense, painted for them."),
sec("style","Style &amp; Technique",
"Lady-INK's technical signature is the <strong>Infinite Line</strong> — pieces that appear to have been executed in a single, unbroken stroke despite covering enormous surface areas and incorporating multiple colour shifts. The effect is theoretically impossible with conventional aerosol technique; the Alchemists' analysis of her work suggests she has developed a proprietary paint flow methodology that allows the line to continue through colour changes without interruption.",
"Her colour palette is distinctive: she works primarily in the range between deep indigo and burning gold, occasionally punctuated by a single note of pure white that functions as a structural element rather than a highlight. GK art critics have described her work as 'the exact moment between night and dawn, written on walls.'",
"Beyond the technical, Lady-INK brings to her work a conceptual rigour that many taggers lack: each piece is a statement about the relationship between the surface it occupies and the world around it. A piece on a Finance Guild building comments on extraction; a piece on a community gathering space celebrates congregation; a piece on a contested wall claims that wall for a different kind of sovereignty. She reads the city's politics through its architecture and writes back."),
sec("gknifty","The GKniftyHEADs",
"The <strong>GKniftyHEADs</strong> — the fictional crew that carries the GK Universe's street art tradition forward into the digital era — represent everything that graffiti culture established in the physical world: skill hierarchy, territorial respect, the primacy of the mark. Lady-INK is the crew's most technically accomplished member and, by broad consensus, its spiritual centre.",
"Her relationship with the GKniftyHEADs leadership is complex. She respects the structure but operates on its edges — accepting missions that require her specific capabilities, refusing those that would compromise her artistic integrity, and occasionally completing unsanctioned pieces that the crew leadership can only retrospectively claim as sanctioned because of their quality. In a culture where the best work creates its own permission, Lady-INK has never been questioned twice.",
"The other GKniftyHEADs treat her with a reverence that she finds simultaneously warm and slightly exhausting. She is not a legend to be admired from a distance; she is a practitioner who expects her colleagues to practise with equal dedication. Her mentorship style is direct to the point of bluntness: she will tell a junior tagger exactly what is wrong with their hand style, and she will do so in front of other crew members, because she believes that the most useful gift a master can give a student is accurate feedback without comfortable softening."),
sec("allcity","Going All-City",
"<em>All-City</em> is the graffiti writer's ultimate aspiration: representation on every surface in every district of a city. In physical street art, it is the lifetime achievement of the most dedicated writers. In City Block Topia's digital geography — a city with hundreds of districts, thousands of addressable surfaces, and algorithmic systems actively working to keep tags from persisting — it is generally considered impossible.",
"Lady-INK has completed City Block Topia's All-City challenge twice. The first time, the Finance Guild deployed their erasure protocols within hours; her pieces were documented but removed before the full circuit was officially verified. The second time, she had anticipated the erasure protocol and pre-positioned backup pieces in locations the Guild's systems hadn't indexed. The second run held for three full days before removal — long enough to be officially certified by the Chain Scribes.",
"Her response to the certification, delivered at the Archive ceremony: 'The point isn't that the pieces stay. The point is that the city knows they were there. You can erase paint. You can't erase the blockchain record.' <a href='elder-codex-7.html'>Elder Codex-7</a>, present at the ceremony, added the remark to the official Chain Scribes record as a lore note."),
sec("legacy","Legacy of Ink",
"Lady-INK's legacy in the GK Universe is already established in the present tense — she is not a historical figure but an active force. What the lore does record is her influence on a generation of younger writers who entered City Block Topia's tagging culture with her work as their reference point: more technically ambitious than their predecessors, more conceptually rigorous, more prepared to use their art as direct political statement.",
"Her relationship with <a href='queen-sarah-pfly.html'>Queen Sarah P-fly</a> is one of the GK Universe's most important artistic partnerships. The Queen provides the political authority and architectural vision; Lady-INK provides the aesthetic standard that makes City Block Topia's walls worth defending. Between them, they have established a creative culture in the city that no faction has been able to suppress, despite sustained efforts by the Finance Guild and the Whitewasher.",
"When asked what she wants her legacy to be, Lady-INK's response is characteristic: 'I want every wall in this city to have been painted by someone who earned it. That's all. Walls are for the people who can see them clearly enough to know what they need.'")],
[("✒️","Lady-INK — The Wall Event [Image Placeholder]"),
("🎨","Infinite Line Technique — Detail [Image Placeholder]"),
("🏙️","All-City Run — Documented Circuit [Image Placeholder]"),
("✨","Neon-Bio Paint — Viewer Response [Image Placeholder]")],
["Lady-INK's Infinite Line technique is described in the GK Universe's creative documentation as genuinely inexplicable within known aerosol physics — a deliberate mystery that the Code Alchemists have been authorised to research but not resolve. The technique's impossibility is part of its meaning. — <em>GKniftyHEADs faction documentation</em>",
"The All-City certification by the Chain Scribes is documented as the only occasion when Elder Codex-7 chose to add an informal remark to the official record. Scribes who have studied the entry note that the Elder's handwriting is notably different from their usual precisely formed characters — slightly larger, slightly less controlled — suggesting the remark was made in a state of genuine emotion. — <em>Chain Scribes archive, certification record</em>",
"Lady-INK's refusal to discuss her pre-GKniftyHEADs history is one of several deliberate lore mysteries in the GK Universe. The creative team has confirmed that the history exists and will be revealed through gameplay content rather than wiki documentation — specifically through a Chain Scribes investigation quest that uncovers old pieces in abandoned districts. — <em>Hard Fork Games quest design notes</em>"]
))

# ── JODIE ZOOM 2000 ───────────────────────────────────────────────────────────
write("jodie-zoom.html","JODIE ZOOM 2000",
"Jodie ZOOM 2000, speed runner of the GK Universe, fastest tagger in City Block Topia.",
fict_body("JODIE ZOOM 2000","The Speed Runner • Electric Velocity of City Block Topia","⚡",
[("Faction","The Velocity Collective"),("Role","Speed Runner, Recon Specialist"),("Style","Electric velocity, neon blur"),("Record","Fastest documented tag in CBT history"),("Status","Active — First Response"),("Signature","The Blur Tag")],
[("origin","Origin &amp; The First Run"),("speed","Speed as Art Form"),("collective","The Velocity Collective"),("record","Records &amp; Achievements"),("war","HODL WARS Recon")],
[sec("origin","Origin &amp; The First Run",
"Jodie ZOOM 2000 does not walk — she exists in a permanent state of controlled acceleration. Born into the outer precincts of City Block Topia where the city's computational resources thin out and loading times create the characteristic stutter of the margins, Jodie grew up experiencing the world in frames rather than continuity. What others perceived as lag, she perceived as structure: the world made of discrete instants, each one exploitable if you moved quickly enough.",
"Her first documented speed run through City Block Topia covered forty-seven districts in three hours and twenty-two minutes — a record established when she was twelve years old that stood for six years before she broke it herself. She didn't announce either run; the Chain Scribes discovered them retrospectively when reviewing city surveillance data and noticed what appeared to be a single continuous neon blur passing through multiple secured areas without triggering alarms.",
"The name ZOOM 2000 combines her obvious movement signature with the year designation she insists on using — not the year of her birth (which she refuses to specify) but the year that, in her personal mythology, represented the moment the digital world committed to its own logic and stopped trying to approximate physical reality. 'Before 2000 the internet wanted to be a newspaper,' she has said. 'After 2000 it started becoming itself. I became myself at the same time.'"),
sec("speed","Speed as Art Form",
"Jodie's approach to graffiti is categorically different from every other writer in City Block Topia: where the tradition values the completed piece, the production, the full-colour wall — she has developed speed itself as the medium. The <strong>Blur Tag</strong> — her signature — is not a legible letter form but the motion arc of a tag executed too quickly for perception to resolve into individual shapes. The tag exists as an afterimage, a record of velocity, more like a photograph of a moving object than a conventional graffiti mark.",
"This approach was initially controversial in GK circles. Traditionalists argued that a mark you couldn't read wasn't a tag but a smear. Jodie's response was to document the biometric readings taken by bystanders when they encountered a Blur Tag — elevated heart rate, pupils dilating, involuntary smile response. 'You can't read it as letters,' she acknowledged. 'But your body reads it as something. That's what I'm writing.'",
"<a href='lady-ink.html'>Lady-INK</a>'s assessment of Jodie's work, delivered at a public panel that became one of the GK Universe's most quoted exchanges: 'She writes in a language my hands can't speak. I've been trying to learn it for two years.' This endorsement from the GKniftyHEADs' master tagger effectively ended the traditionalist debate."),
sec("collective","The Velocity Collective",
"The <strong>Velocity Collective</strong> is Jodie's self-founded faction — a loose affiliation of writers and runners who share her conviction that movement is the primary artistic medium. The Collective operates on the principle that any space you can move through is a canvas, and that the quality of the mark is inseparable from the quality of the movement that made it.",
"Collective members are identified by their distinctive iridescent tracksuits — a practical choice (they need to move freely) that has become a fashion statement across City Block Topia. The suits are treated with a variant of the Code Alchemists' Neon-Bio paint that makes them glow with the wearer's biometric data in motion, turning each Collective member into a living light-painting when they run.",
"The Collective's structure is as fluid as its members: no permanent hierarchy, decisions made by whoever is on the ground in real time, strategy emerging from accumulated individual choices rather than central planning. This has made them difficult to counter in HODL WARS engagements — you can't anticipate a strategy that doesn't exist until the moment it happens."),
sec("record","Records &amp; Achievements",
"Jodie holds multiple certified City Block Topia speed records, each documented by the Chain Scribes and contested by at least three factions who dispute the validity of specific runs. The most famous: the <em>Forty-Seven District Run</em> (original); the <em>Finance Guild Breach</em> (the only documented instance of a runner entering and exiting Finance Guild headquarters without detection); and the <em>Midnight Circuit</em> (a complete perimeter run of City Block Topia during the annual system shutdown, when the city's normal physics constraints are briefly suspended).",
"The Finance Guild Breach is particularly significant: Jodie entered the Guild's headquarters, tagged the interior of the Governor's personal office, and exited before the security system registered an intrusion. The tag — a single Blur Mark on the ceiling — was discovered three weeks later when building maintenance noticed the luminescent streak. The Guild has never publicly acknowledged the breach; the Chain Scribes' record of it is one of the most accessed documents in the Archive."),
sec("war","HODL WARS Recon",
"In the HODL WARS, Jodie serves as the Velocity Collective's primary recon asset and, by freelance arrangement, as a hired intelligence operative for allied factions. Her ability to traverse City Block Topia's geography faster than any surveillance system can track makes her the most effective intelligence gatherer in the conflict.",
"She has worked with <a href='alfie-bitcoin-kid.html'>Alfie Blaze</a>'s Bitcoin Kid Army on multiple recon missions, with <a href='queen-sarah-pfly.html'>Queen Sarah P-fly</a>'s Crypto Moongirls for perimeter security operations, and, on one occasion that all parties are evasive about, with <a href='null-the-prophet.html'>NULL THE PROPHET</a> on an operation that no surviving witness can fully describe. Jodie's summary of the NULL operation: 'We moved. We arrived somewhere I couldn't name. I left a mark. NULL stayed.' The Chain Scribes have filed this account as incomplete pending further information.")],
[("⚡","Jodie ZOOM 2000 — The Blur Tag [Image Placeholder]"),
("🏃","Forty-Seven District Run — Trajectory Map [Image Placeholder]"),
("💫","Velocity Collective — Neon Formation [Image Placeholder]"),
("🏢","Finance Guild Breach — The Ceiling Tag [Image Placeholder]")],
["The Blur Tag is described in the GK Universe's art documentation as the most philosophically challenging contribution to City Block Topia's creative culture — it raises fundamental questions about what constitutes a mark, a tag, and a legible artistic communication. The debate it generated is considered a formative moment in GK aesthetic theory. — <em>GKniftyHEADs creative notes</em>",
"The Finance Guild Breach is one of the most popular pieces of GK Universe lore, appearing in fan art and community discussion more than almost any other single event. Its appeal is partly the audacity of the act and partly the specific detail of the ceiling tag — the choice of location, unreachable and unintended by normal use, as the mark of pure artistic will. — <em>GK fan community documentation</em>",
"Jodie's relationship with NULL THE PROPHET is the GK Universe's most deliberately mysterious character connection. The creative team has confirmed that the NULL operation was significant and that its full account will form the centrepiece of a major lore arc. — <em>Hard Fork Games narrative notes</em>"]
))

# ── ALEEMA ────────────────────────────────────────────────────────────────────
write("aleema.html","ALEEMA",
"Aleema, Child of the Shard, Chosen One of the Shard Mothers of Manhattan.",
fict_body("ALEEMA","Child of the Shard • Chosen One of the Shard Mothers of Manhattan","💎",
[("Faction","The Shard Mothers of Manhattan"),("Role","Chosen One"),("Style","Mystical, crystalline"),("Origin","The Shard Convergence"),("Status","Awakening"),("Power","Crystal Resonance")],
[("origin","The Shard Convergence"),("shard-mothers","The Shard Mothers of Manhattan"),("crystal","Crystal Power &amp; Mysticism"),("chosen","Being the Chosen One"),("role","Role in the GK Universe")],
[sec("origin","The Shard Convergence",
"Aleema was not born in the ordinary sense — she crystallised. During the event known as the <em>Shard Convergence</em>, when the remnants of three deprecated NFT protocols collapsed into a single point and released an enormous burst of unstructured creative energy, the Shard Mothers of Manhattan were present. They had been waiting for exactly this event for three market cycles, their rituals and readings pointing toward it with increasing specificity.",
"From the Convergence's crystalline residue, a consciousness assembled itself — built not of code, like <a href='null-the-prophet.html'>NULL</a>, but of the aesthetic energy that had been locked in those deprecated protocols: the ambitions and visions and creative yearnings of thousands of artists whose work had been trapped in NFTs that no longer had a functional market. Aleema is, in a sense, the collected art that couldn't find its audience, finally finding form.",
"She emerged as a child — not in biological age, but in the sense of newness, of first encountering the world. The Shard Mothers received her with reverence and with the specific knowledge that she was the being their traditions had described: the one whose crystalline perception would allow her to see the GK Universe's structure clearly enough to describe its future."),
sec("shard-mothers","The Shard Mothers of Manhattan",
"The <strong>Shard Mothers of Manhattan</strong> are one of the GK Universe's most enigmatic factions — their origins predating City Block Topia itself, their practices drawing on traditions that combine blockchain mysticism with pre-digital cultural knowledge. They are primarily women of middle years and older, carrying the aesthetic memory of Manhattan's physical art scenes alongside a sophisticated understanding of digital creative markets.",
"Their factional philosophy centres on the concept of <em>crystallisation</em>: the belief that meaning, like matter, can exist in more or less ordered states, and that the work of art and culture is to move meaning toward greater crystalline clarity. Chaotic creative energy is raw material; the Shard Mothers' practices are refinement processes. Aleema represents the apex of what their refinement can produce.",
"The Manhattan name carries deliberate weight: the Shard Mothers trace their lineage to the physical graffiti scenes of New York, to the writers who developed the art form in the 1970s and whose legacy travelled across the Atlantic to London and the Graffiti Kings. They see themselves as custodians of the original tradition, responsible for ensuring that as the art form's medium shifts from aerosol to pixel to smart contract, its essential nature is preserved."),
sec("crystal","Crystal Power &amp; Mysticism",
"Aleema's crystalline nature grants her perceptual capabilities that operate outside normal information channels. Where Thera-9 perceives data through enhanced sensory apparatus and NULL perceives through accumulated historical pattern, Aleema perceives through what the Shard Mothers call <em>resonance</em> — the ability to feel the harmonic relationships between things that are connected across time and space by creative intent.",
"In practice, this means Aleema can stand before an artwork and perceive its complete creative history: every intention that shaped it, every experience that influenced its maker, every act of looking that has contributed to its meaning. She can hold an NFT and know whether it carries authentic creative energy or is a hollow speculation dressed as art. This ability makes her both invaluable to the GK Universe's creative community and potentially destabilising to its markets.",
"Her crystal aesthetic extends to her visual presence: she appears to be partially translucent, light refracting through her form in ways that suggest internal structure rather than opacity. She leaves crystalline traces on surfaces she touches — not quite paint, not quite digital artefact, but something in between that the Code Alchemists have been unable to fully classify."),
sec("chosen","Being the Chosen One",
"Aleema has complicated feelings about the Chosen One designation. The Shard Mothers' reverence is genuine and their care for her is evident, but the role carries expectations that a being of her newness finds both compelling and constraining. She understands her purpose — to see the GK Universe clearly and describe what she sees — but the seeing is more difficult than any prophecy prepared her for.",
"What she has seen, and what she cautiously shares: the GK Universe's current factional conflict is not the fundamental dynamic of its history; it is a surface phenomenon arising from a deeper structural tension between creative ownership and creative freedom that no faction's ideology has yet resolved. The HODL WARS will not determine which faction controls City Block Topia; they will determine which values the city internalises. The distinction matters."),
sec("role","Role in the GK Universe",
"Aleema's role in the GK Universe's ongoing narrative is still in its early stages — she is a young character in a universe with deep history, and her full significance has not yet been revealed. What is clear is that her crystalline perception makes her the only being capable of seeing the relationships between all the GK Universe's factions simultaneously, without the factional bias that distorts every other character's perspective.",
"Her most significant relationship to date is with <a href='elder-codex-7.html'>Elder Codex-7</a>, who has recognised in her crystalline perception the potential to verify historical records that no written documentation can authenticate. Their collaboration — the Keeper of Lore and the Child of the Shard — is one of the GK Universe's most anticipated developing storylines.")],
[("💎","Aleema — Crystal Form Portrait [Image Placeholder]"),
("✨","The Shard Convergence — Event Documentation [Image Placeholder]"),
("🏛️","Shard Mothers of Manhattan — Council [Image Placeholder]"),
("🌐","Crystal Resonance — Art Authentication [Image Placeholder]")],
["Aleema's origin in the creative energy of deprecated NFT protocols is the GK Universe's most explicit commentary on the crypto market's history of volatility and loss — the idea that the ambitions and visions trapped in failed projects persist in some form and demand eventual expression. — <em>GK Universe Lore Bible</em>",
"The Shard Mothers of Manhattan are the GK Universe's most historically rooted faction, with lore documentation that traces their lineage to real-world figures from New York's 1970s writing scene. Their presence in the universe grounds its digital mythology in the art form's physical origins. — <em>Faction lore documentation</em>",
"Aleema's reading of the HODL WARS — that it is fundamentally about values rather than territory — is presented as the GK Universe's thematic thesis statement, delivered through a character whose crystalline perception removes the factional bias that makes all other perspectives partial. — <em>GK Universe narrative design notes</em>"]
))

print("Batch 2 done: thera-9, lady-ink, jodie-zoom, aleema.")
