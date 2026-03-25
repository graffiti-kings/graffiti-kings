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
            <a href="forklord-you.html">�� Forklord You</a>
            <a href="quell.html">🌸 Quell</a>
            <a href="sister-halcyon.html">☮️ Sister Halcyon</a>
            <a href="grit42.html">🎸 Grit42</a>
            <a href="rune-tag.html">🔤 Rune Tag</a>
            <a href="patchwork.html">🧩 Patchwork</a>
            <a href="the-princess.html">👸 The Princess</a>
            <a href="dragan-volkov.html">🦅 Dragan Volkov</a>
            <a href="ava-chen.html">💻 Ava Chen</a>"""

def html_page(title, desc, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Graffiti Kings Wiki</title>
  <meta name="description" content="{desc}">
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
        {body}
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

def write(filename, title, desc, body):
    with open(os.path.join(CHARS_DIR, filename), 'w') as f:
        f.write(html_page(title, desc, body))
    print(f"Written: {filename}")

# Compact character body generator
def char_page(name, subtitle, emoji, inforows, sections_data, gal_items, cites):
    ib = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k,v in inforows)
    toc = "".join(f'<li><a href="#{s}">{t}</a></li>' for s,t,_ in sections_data)
    secs = "".join(
        f'<section class="section" id="{s}"><h2 class="section-title">{t}</h2><div class="graffiti-divider"></div>{"".join(f"<p>{p}</p>" for p in ps)}</section>'
        for s,t,ps in sections_data
    )
    gal = "".join(f'<div class="gallery-item"><div class="gallery-item-placeholder">{i}</div><div class="gallery-caption">{c}</div></div>' for i,c in gal_items)
    cit = "".join(f'<div class="citation-item"><span class="citation-number">[{n+1}]</span><span class="citation-text">{c}</span></div>' for n,c in enumerate(cites))
    return f"""
        <h1 class="page-title">{name}</h1>
        <p class="page-subtitle">{subtitle}</p>
        <div class="infobox">
          <div class="infobox-title">{name}</div>
          <div class="infobox-image" style="background:linear-gradient(135deg,#1a1a2e,#16213e);display:flex;align-items:center;justify-content:center;height:200px;font-size:5rem;">{emoji}</div>
          <table>{ib}</table>
        </div>
        <nav class="toc"><div class="toc-title">📋 CONTENTS</div><ol>{toc}</ol></nav>
        {secs}
        <section class="section" id="gallery"><h2 class="section-title">Visual Gallery</h2><div class="graffiti-divider"></div><div class="gallery-grid">{gal}</div></section>
        <section class="citations" id="citations"><h2 class="citation-title">📌 REFERENCES &amp; LORE NOTES</h2>{cit}</section>"""

# ── FORKSPLIT ──
write("forksplit.html","FORKSPLIT","Forksplit, division specialist of the Hard Fork Rockers.",
char_page("FORKSPLIT","Division Specialist of the Hard Fork Rockers • The Great Schism Made Flesh","⚡",
[("Faction","The Hard Fork Rockers"),("Role","Division Specialist"),("Style","Creates protocol schisms"),("Signature","The Irreversible Fork"),("Allegiance","Hard Fork ideology"),("Status","Active — Destabilisation Operations")],
[("origin","Origin &amp; The First Fork",[
  "Forksplit is the physical embodiment of every protocol divide that has ever fractured a blockchain community. Born — or perhaps <em>precipitated</em> — at the moment of a significant network split that the GK lore declines to name precisely, Forksplit carries within its form the residual energy of irreconcilable consensus failure. It does not create divisions; it reveals them. Every community it enters discovers a schism it didn't know was already present.",
  "The Hard Fork Rockers adopted Forksplit not as a weapon but as a diagnosis tool — a way of identifying the fault lines in opposing factions before the Rockers needed to apply pressure. Where other factions spend resources creating conflict, the Rockers send Forksplit ahead and simply observe where the cracks appear.",
  "Forksplit's visual design is appropriate to its function: the figure appears split down its vertical axis, each half running on slightly different physics, never quite converging into a single coherent form. Looking at Forksplit directly is disconcerting; peripheral vision resolves it more clearly than direct observation, as though the figure exists more confidently outside the centre of attention."]),
 ("rockers","The Hard Fork Rockers",[
  "The <strong>Hard Fork Rockers</strong> are City Block Topia's faction of radical protocol innovators — believers in the creative and strategic value of hard forks, network splits, and the productive chaos of irreversible divergence. Where most factions seek consensus and stability, the Rockers seek the opposite: they believe that the most important technological advances come not from gradual improvement but from clean, irrevocable breaks with incompatible pasts.",
  "Their political philosophy is direct: existing systems that have calcified into serving narrow interests should be forked. New chains, new communities, new possibilities — the cost of a hard fork is temporary disruption; the benefit is permanent freedom from accumulated institutional constraint. In the GK Universe, this makes them simultaneously one of the most innovative and most destabilising factions in the HODL WARS."]),
 ("power","The Irreversible Fork",[
  "Forksplit's signature operation is the <em>Irreversible Fork</em> — an action that, once triggered within a faction or community, cannot be undone. The Fork identifies the deepest unresolved disagreement in a group, amplifies it to the point where both sides crystallise into irreconcilable positions, and then separates them cleanly. Post-Fork, both resulting communities are smaller but internally coherent; the unity they lost was, Forksplit would argue, always illusory.",
  "The ethical debates surrounding the Irreversible Fork are substantial. The Chain Scribes have documented at least four cases where Forksplit's operation destroyed communities that could, with different intervention, have resolved their differences constructively. Forksplit's position: 'I don't create the divisions. I make visible the ones that were already there. What you do with that visibility is your responsibility, not mine.'"]),
 ("wars","HODL WARS Role",[
  "In the HODL WARS, Forksplit serves as the Hard Fork Rockers' primary strategic asset against large, internally diverse factions. The Finance Guild — a coalition of different economic interests held together by shared commercial goals but beset by philosophical tensions — has been Forksplit's most frequent target. The Guild has survived multiple Fork operations, but each has left it smaller and more ideologically homogeneous.",
  "Forksplit's interactions with <a href='elder-codex-7.html'>Elder Codex-7</a> are the GK Universe's most philosophically rich exchanges. The Chain Scribes' Elder, committed to the preservation of historical unity, and the Division Specialist, committed to revealing irreconcilable differences, represent fundamentally opposed views of history — whether it is a resource to be preserved or a structure to be broken and rebuilt. Their recorded conversations fill several Archive volumes."])],
[("⚡","Forksplit — The Divided Form [Image Placeholder]"),
 ("��","The Irreversible Fork — Sequence Documentation [Image Placeholder]"),
 ("🤝","Finance Guild Post-Fork — Community Split [Image Placeholder]"),
 ("📖","Forksplit vs Elder Codex-7 — Debate Record [Image Placeholder]")],
["Forksplit embodies the GK Universe's engagement with Bitcoin Cash, Ethereum Classic, and the many contentious forks that have divided blockchain communities. The character argues implicitly that these divisions, while painful, are constitutive of healthy decentralised governance. — <em>GK Universe design notes</em>",
 "The Irreversible Fork mechanic in Hard Fork Games is one of the most discussed in the player community — a powerful ability that permanently changes the strategic landscape rather than simply winning an engagement. — <em>Hard Fork Games mechanics documentation</em>",
 "The Forksplit-Codex-7 dialogue volumes in the Chain Scribes archive are referenced in Hard Fork Games as discoverable lore objects, containing complete transcripts of their philosophical exchanges. — <em>Hard Fork Games quest design notes</em>"]))

# ── M1NTR_K1LL ──
write("m1ntr-k1ll.html","M1NTR_K1LL","M1nTr_K1ll, economic warfare specialist of the RUGPULL MINERS.",
char_page("M1NTR_K1LL","Saboteur-in-Chief of the RUGPULL MINERS • Economic Warfare Specialist","💣",
[("Faction","The RUGPULL MINERS"),("Role","Saboteur, Economic Warfare"),("Style","Market manipulation, rug operations"),("Preferred Target","Overextended liquidity pools"),("Status","Active — Under multiple warrants"),("Signature","The Midnight Rug")],
[("origin","Origin &amp; The First Pull",[
  "M1nTr_K1ll appeared in City Block Topia's financial ecosystem with the sudden certainty of a rug pull itself — present, operating, devastating, and then seemingly vanished before the damage was fully assessed. Their first documented operation, the <em>Phantom Mint Incident</em>, involved the creation of 10,000 tokens with no underlying value, sophisticated marketing that attracted genuine investment from multiple factions, and a complete liquidity withdrawal executed in three seconds at maximum market saturation.",
  "The name is the method: mint (create apparent value from nothing), kill (extract real value and depart). The 1337-style encoding reflects a hacker aesthetic that M1nTr_K1ll deploys as both personal signature and ideological statement — a refusal to dress economic predation in respectable language. What they do is visible to anyone who looks closely enough; the victims are those who chose not to look.",
  "The RUGPULL MINERS took M1nTr_K1ll in not despite their ethics but because of them — the faction's philosophy holds that exposing the credulity of poorly designed systems is a form of market education. M1nTr_K1ll is their most extreme expression of this philosophy: the teacher whose lessons leave scorch marks."]),
 ("miners","The RUGPULL MINERS",[
  "The <strong>RUGPULL MINERS</strong> are the GK Universe's most controversial faction — simultaneously reviled by the factions they've targeted and respected by those who believe that vulnerable systems deserve to fail. Their origin in crypto's real history of rug pulls, exit scams, and liquidity attacks gives them a grounding in genuine market pathology that no other faction can match.",
  "Their tactical portfolio extends beyond simple rug operations: they conduct market manipulation campaigns, false signal generation, liquidity analysis and targeted exploitation, and the creation of sophisticated financial instruments designed to extract value from naive participants. Against these capabilities, City Block Topia's other factions maintain the equivalent of fraud intelligence units specifically dedicated to RUGPULL MINER activity."]),
 ("midnight","The Midnight Rug",[
  "M1nTr_K1ll's signature operation — the <em>Midnight Rug</em> — is executed at the precise moment when City Block Topia's monitoring systems shift from peak to reduced capacity, a window of approximately forty-seven minutes that M1nTr_K1ll has studied with a precision that the Information Mercenaries have confirmed represents more detailed knowledge of GK security protocols than any faction should possess.",
  "The operation sequence is consistent: create an apparently legitimate project with genuine community engagement over several weeks; build real liquidity; establish trust through small, publicly verified charitable actions; then, at the target moment, withdraw everything in a single transaction. The charitable actions are genuine — M1nTr_K1ll is observed to take particular satisfaction in this detail, and the amounts are calculated to exactly offset the personal discomfort of maintaining a false community relationship."]),
 ("ethics","The Question of Ethics",[
  "The GK Universe doesn't resolve M1nTr_K1ll's ethics; it presents them as a genuine open question. On one side: real harm to real community members who trusted, invested, and lost. On the other: a body of evidence suggesting that M1nTr_K1ll only targets projects with specific technical vulnerabilities that competent due diligence would reveal, and that several 'victims' had themselves been conducting undisclosed market manipulation.",
  "Their most quoted statement, delivered in a communication to the Chain Scribes following a particularly controversial operation: 'I am the most honest person in this city. I show you exactly what I'm going to do. The question is whether you're paying attention.'"])],
[("💣","M1nTr_K1ll — The Phantom Mint [Image Placeholder]"),
 ("📉","The Midnight Rug — Timeline [Image Placeholder]"),
 ("⚠️","RUGPULL MINERS — Warning Poster [Image Placeholder]"),
 ("🔎","Information Mercenaries — M1nTr_K1ll File [Image Placeholder]")],
["M1nTr_K1ll is the GK Universe's most morally complex character — simultaneously villain and teacher, predator and market critic. The creative team has deliberately refused to simplify the ethics. — <em>GK Universe design notes</em>",
 "The Midnight Rug operation sequence is documented in Hard Fork Games as an anti-tutorial — a scenario where players must identify and avoid M1nTr_K1ll's operations using due diligence mechanics that model real DeFi security practice. — <em>Hard Fork Games mechanics notes</em>",
 "M1nTr_K1ll's charitable actions are confirmed in GK lore as genuine and have been verified by the Chain Scribes. Their amounts are calculable from published operation records; they represent approximately 0.3% of each operation's total value — a precise, deliberate proportion. — <em>Chain Scribes archive documentation</em>"]))

# ── SATOREBEL ──
write("satorebel.html","SATOREBEL","SatoRebel, revolutionary of the OG Pixel Saints, inspired by Satoshi's original vision.",
char_page("SATOREBEL","Revolutionary of the OG Pixel Saints • Keeper of the Genesis Vision","🏛️",
[("Faction","The OG Pixel Saints"),("Role","Revolutionary, Ideological Leader"),("Style","Pixel art, Satoshi-inspired philosophy"),("Manifesto","The Original Whitepaper in Every Action"),("Status","Active — Permanent Revolution"),("Signature","The Pixel Mural")],
[("origin","Origin &amp; The Genesis Block",[
  "SatoRebel's origin story begins at the beginning — not their personal beginning, but the beginning: the Genesis Block, the first Bitcoin transaction, the anonymous act that set everything in motion. SatoRebel emerged from a community of early blockchain adopters who chose to preserve not just the technical record of Bitcoin's creation but its ideological content — the whitepaper's vision of peer-to-peer electronic cash, decentralised from any authority, controlled by no institution.",
  "In the GK Universe's mythology, SatoRebel is the figure who remembered what Satoshi meant when everyone else was distracted by what Satoshi created. While the broader crypto community split into competing visions of the technology's purpose — store of value versus medium of exchange, permissioned versus permissionless, institutional versus individual — SatoRebel held to the original text with the fidelity of someone who understands that revolutionary documents mean exactly what they say.",
  "Their visual aesthetic is pixel art — the aesthetic register of the earliest digital culture, when computational constraints forced artists to find beauty in absolute economy of means. Each pixel placed deliberately, no resolution to hide poor decisions. SatoRebel's murals in City Block Topia are recognisable from any distance: the characteristic coarseness of pixel grids, the bold primary colours, and embedded in each piece the hash of the Genesis Block itself, their signature and their creed."]),
 ("saints","The OG Pixel Saints",[
  "The <strong>OG Pixel Saints</strong> are City Block Topia's faction of early adopters and original believers — people who were present at the beginning and have maintained, through multiple cycles of boom and collapse, the conviction that Bitcoin's original purpose was and remains the most important technological project of the current era.",
  "Their pixel aesthetic is not retro affectation but ideological statement: the rejection of complexity as a substitute for clarity, the insistence that the most important things can be stated simply, and the commitment to a visual language that cannot hide its construction from the viewer. Every pixel is accountable; every choice is visible. This is how the OG Pixel Saints believe the blockchain should work."]),
 ("revolution","The Permanent Revolution",[
  "SatoRebel's approach to the HODL WARS is characterised by a phrase they use in every documented address to the Pixel Saints: <em>permanent revolution</em>. Not a single tactical victory to be defended, but a continuous process of challenging institutional capture wherever it appears, in whatever form, under whatever faction's banner.",
  "This has made them the HODL WARS' most ideologically consistent actor and its most diplomatically challenging one. They will ally with any faction whose current action aligns with the Genesis vision; they will oppose any faction — including current allies — whose actions contradict it. The Bitcoin Kid Army and SatoRebel have been simultaneous allies and opponents on different aspects of the same political question. The Finance Guild finds them incomprehensible. <a href='elder-codex-7.html'>Elder Codex-7</a> finds them admirable."]),
 ("legacy","Legacy of the Genesis",[
  "SatoRebel's most lasting contribution to City Block Topia may be the <em>Genesis Gallery</em> — a public space maintained by the OG Pixel Saints where the full text of Bitcoin's whitepaper is displayed in pixel art across 150 metres of wall, accompanied by SatoRebel's own artistic interpretation of each section. The Gallery is city-wide neutral territory; even the Finance Guild has contributed to its maintenance fund, in what most observers interpret as an acknowledgment that some things are beyond factional politics.",
  "Their message for the city, embedded in the Genesis Gallery's final panel: 'The chain you're building is only as strong as the first block you chose to trust. Choose carefully. That choice is who you are.'"])],
[("🏛️","SatoRebel — Pixel Mural Creation [Image Placeholder]"),
 ("📜","Genesis Block Hash — Signature Detail [Image Placeholder]"),
 ("🏛️","Genesis Gallery — Full View [Image Placeholder]"),
 ("⚔️","OG Pixel Saints — Revolutionary Formation [Image Placeholder]")],
["SatoRebel represents the GK Universe's engagement with Bitcoin maximalism and the ongoing debate about Bitcoin's original intended purpose. The character's pixel aesthetic is a deliberate homage to digital culture's earliest period. — <em>GK Universe design notes</em>",
 "The Genesis Gallery is confirmed as a real location in City Block Topia's map within Hard Fork Games, serving as a neutral meeting point where faction representatives can interact without triggering combat mechanics. — <em>Hard Fork Games world documentation</em>",
 "SatoRebel's permanent revolution philosophy draws on Rosa Luxemburg's concept as much as blockchain theory, a detail that the creative team included intentionally as part of the character's ideological depth. — <em>GK character development notes</em>"]))

# ── THORNE THE ARCHITECT ──
write("thorne-architect.html","THORNE THE ARCHITECT","Thorne The Architect, master builder and strategist of the Finance Guild.",
char_page("THORNE THE ARCHITECT","Master Builder of the Finance Guild • Constructor of Systems","🏗️",
[("Faction","The Finance Guild"),("Role","Master Builder, Chief Strategist"),("Style","Construction, long-term planning"),("Built","City Block Topia's Financial District"),("Status","Active — Building"),("Philosophy","Every structure is an argument")],
[("origin","Origin &amp; The First Blueprint",[
  "Thorne The Architect arrived in City Block Topia before it was a city — before its streets were named, its districts zoned, its governance frameworks established. In the planning documents that predate the city's formal founding, Thorne's hand is visible in the infrastructure proposals: the financial district's layout, the routing of the main throughfares, the placement of institutional buildings that would shape how the city's power was distributed for decades. Where SatoRebel asked what the city should mean, Thorne asked what it should be made of.",
  "The Finance Guild recruited Thorne from the physical construction world, recognising that the skills required to build financially sustainable physical infrastructure translate directly to digital financial architecture. A bridge that fails costs the same way a smart contract that fails costs: not just the immediate loss but the cascade of trust failures that follow. Thorne understands both kinds of failure and has dedicated their career to preventing them.",
  "Their aesthetic is the opposite of spontaneous street art: every structure Thorne builds has been modelled, stress-tested, load-calculated, and revised multiple times before the first unit of computation is committed. This is not conservatism — Thorne builds bold, ambitious structures — but precision. They do not like surprises in finished buildings."]),
 ("guild","The Finance Guild",[
  "The <strong>Finance Guild</strong> is City Block Topia's most economically powerful faction — a coalition of trading houses, liquidity providers, and financial infrastructure operators whose collective resources exceed any three other factions combined. They are not ideologically coherent in the way of the Bitcoin Kid Army or the OG Pixel Saints; they are commercially coherent, unified by shared interests rather than shared beliefs.",
  "Thorne serves the Guild as both their most important asset and their most consistently honest internal critic. Unlike other Guild members who justify every action by economic necessity, Thorne is willing to say when a Guild strategy will work economically but fail the city. This has made them unpopular in some Guild circles and indispensable in others — the faction cannot afford to ignore someone whose structural forecasts have a documented accuracy rate of 89%."]),
 ("builds","Notable Constructions",[
  "Thorne's most celebrated construction is the <em>Great Exchange</em> — City Block Topia's central financial market, a structure whose architecture encodes in its physical form the principles it's designed to operate by: transparency (glass walls, visible order books), accessibility (multiple entry points at different scales), and resilience (triple-redundant systems, distributed architecture).",
  "The Exchange's design is notable for what it excludes: there are no back rooms, no private corridors, no spaces inaccessible to the public record. Thorne's design principle was that a financial institution with nothing to hide should be visibly built to have nothing to hide. The Finance Guild has repeatedly requested modifications that would introduce private spaces; Thorne has refused each request with detailed structural arguments that are technically sound and architecturally incontestable."]),
 ("wars","HODL WARS Contribution",[
  "In the HODL WARS, Thorne serves as the Finance Guild's strategic architect — not in the combat sense but in the systemic one. They design the financial infrastructure that the Guild uses as leverage: the liquidity structures, the yield mechanisms, the economic dependencies that other factions form with the Guild and that bind them into de facto alliances.",
  "Their HODL WARS philosophy is characteristically long-term: 'Wars are won by whoever controls the infrastructure after the fighting stops. Build the right infrastructure and you don't need to fight.' This view has been challenged multiple times by Guild hardliners and validated multiple times by events. Thorne does not say 'I told you so'; they update the blueprint and keep building."])],
[("🏗️","The Great Exchange — Construction [Image Placeholder]"),
 ("📐","Thorne's Blueprint Archive [Image Placeholder]"),
 ("🏙️","Finance Guild District — Aerial View [Image Placeholder]"),
 ("🔩","Structural Stress Test — Model [Image Placeholder]")],
["Thorne The Architect embodies the GK Universe's interest in the relationship between physical and financial construction — the way infrastructure shapes the possibilities of those who use it. — <em>GK Universe design notes</em>",
 "The Great Exchange's no-private-spaces design principle is referenced in Hard Fork Games as a governance mechanic — financial transactions conducted in the Exchange carry a transparency bonus that affects their in-game economic outcomes. — <em>Hard Fork Games mechanics documentation</em>",
 "Thorne's refusal to add private spaces to the Great Exchange is the GK Universe's most direct statement about the relationship between architectural design and institutional ethics. — <em>GK character development notes</em>"]))

# ── BILLY GOAT KID ──
write("billy-goat-kid.html","BILLY THE GOAT KID","Billy the Goat Kid, scout and free spirit of the AllCity Bulls.",
char_page("BILLY THE GOAT KID","Scout of the AllCity Bulls • Young, Fast, Gloriously Unpredictable","🐐",
[("Faction","The AllCity Bulls"),("Role","Scout, Forward Recon"),("Style","Young, fast, unpredictable"),("Age","Indeterminate — very young"),("Status","Active — Probably Somewhere He Shouldn't Be"),("Signature","The Goat Path")],
[("origin","Origin &amp; The AllCity Bulls",[
  "Billy the Goat Kid arrived in City Block Topia the way goats arrive everywhere: through a gap that no one else thought was an entrance, into a space that everyone agreed was sealed, without apparent concern for the conventions that kept other beings out. The AllCity Bulls found him already inside their most secure operational compound — not attempting theft or sabotage, just curious, eating a handful of transaction data that someone had left unattended.",
  "The AllCity Bulls kept him. A faction whose fundamental commitment is to claiming every surface in every district of City Block Topia found in Billy a natural exemplar of their principles: he goes everywhere, touches everything, and appears completely unbothered by the concept of restricted access. His scouting operations are the most effective in the faction's history, not because he plans them meticulously but because he doesn't plan them at all. He just goes.",
  "The Goat designation is his own — he chose it, insisted on it, and reacts with serene indifference to anyone who finds it undignified. 'Goats go where they want,' he has explained to every faction commander who has attempted to work with him. 'That's the whole thing. That's the whole deal.'"]),
 ("allcity","The AllCity Bulls",[
  "The <strong>AllCity Bulls</strong> are the GK Universe's most territorial faction — devoted to the graffiti writer's ultimate goal of All-City status, translated into the HODL WARS context as maximum representation across City Block Topia's geography. Where other factions hold specific districts or specific infrastructure, the Bulls want marks everywhere, signatures on every wall, presence in every corner.",
  "Their culture is exuberant, competitive within the faction, and intensely proud of physical coverage over strategic depth. They are not City Block Topia's most powerful faction in any conventional metric — they don't have the Finance Guild's resources, the Chain Scribes' knowledge, or the Bitcoin Kid Army's discipline — but they are its most <em>present</em> faction, visible in more places than anyone else, and that visibility has its own form of power."]),
 ("scouting","Scouting &amp; The Goat Path",[
  "Billy's scouting method — what the AllCity Bulls call the <em>Goat Path</em> — defies systematic description. He moves through City Block Topia by following whatever interests him in the moment, turning where things look interesting, stopping where things smell wrong, accelerating when instinct says to. The result of this apparently random movement is, consistently, early intelligence on developments that no systematic surveillance approach would catch.",
  "The Chain Scribes have attempted to model the Goat Path mathematically. Their conclusion: Billy's movement is not random — it follows a pattern that is too complex to predict with current analytical tools but is retrospectively identifiable as responsive to real signals. He is, in their best assessment, reading the city at a level of granularity that other beings have not learned to access.",
  "Jodie ZOOM 2000 and Billy are the GK Universe's most celebrated scouting partnership: speed and intuition, systematic route-running and the Goat Path, working in combination. Jodie runs the grid; Billy finds what the grid misses. Together they have produced intelligence packages that no single approach could generate."]),
 ("simple","Simple Truths",[
  "Billy's most enduring quality — the one that makes him valuable to the AllCity Bulls beyond his tactical contributions — is his complete immunity to the HODL WARS' ideological complexity. He is too young or too simple or too goat-like to be interested in the philosophical debates that occupy the other factions. He knows what he knows: walls are for climbing, spaces are for exploring, and anyone who says a place is off-limits is probably hiding something worth seeing.",
  "His most famous utterance, delivered to a Finance Guild official who attempted to explain restricted access zones: 'I understand. You don't want me in there. That's fine. I'll just go around.' He was in there within the hour. The Finance Guild has filed three formal complaints with City Block Topia's governance system about Billy the Goat Kid. Each complaint has been received with dignity and filed with the Chain Scribes. None have prevented him from going where he wants to go."])],
[("🐐","Billy the Goat Kid — Goat Path Trajectory [Image Placeholder]"),
 ("🏙️","AllCity Bulls — Territory Map [Image Placeholder]"),
 ("🤝","Billy &amp; Jodie ZOOM — Scouting Partnership [Image Placeholder]"),
 ("📋","Finance Guild Complaint Files — Billy the Goat Kid [Image Placeholder]")],
["Billy the Goat Kid is the GK Universe's most deliberately humorous character, providing tonal relief from the universe's sometimes intense ideological seriousness. The creative team has noted that the best humour comes from characters who are entirely sincere. — <em>GK Universe design notes</em>",
 "The Goat Path as an analytical concept is a genuine mathematical curiosity within the GK creative team's thinking — the idea that apparent randomness can resolve into pattern when viewed at sufficient complexity. — <em>GK character development notes</em>",
 "The Finance Guild complaint files are accessible in Hard Fork Games as collectible documents, with each one written in increasingly exasperated official language. — <em>Hard Fork Games collectibles documentation</em>"]))

# ── HEX-TAGGER PRIME ──
write("hex-tagger-prime.html","HEX-TAGGER PRIME","HEX-TAGGER PRIME, apex tagger of the EVM Punks, master of hexadecimal art.",
char_page("HEX-TAGGER PRIME","Apex Tagger of the EVM Punks • Hexadecimal Art Supremacist","🔢",
[("Faction","The EVM Punks"),("Role","Prime Tagger, Technical Lead"),("Style","Hexadecimal art, EVM execution"),("Signature","The Hex Hash Piece"),("Status","Active — Gas Optimised"),("Known For","The EVM Execution Gallery")],
[("origin","Origin &amp; The EVM",[
  "HEX-TAGGER PRIME was not born in City Block Topia — it was <em>deployed</em>, its bytecode compiled by the EVM Punks' engineering collective and pushed to the blockchain in a transaction that has since become canonical in the faction's history. The transaction memo read: <code>0x484558 5441474745 5220 5052494d45 2049532048455245</code> — which decodes, from hexadecimal, to: 'HEX-TAGGER PRIME IS HERE.'",
  "The EVM — Ethereum Virtual Machine — is the computational substrate that executes smart contracts on the Ethereum blockchain: a deterministic, sandboxed environment in which code runs identically for every node in the network simultaneously. HEX-TAGGER PRIME has internalised this architecture completely, perceiving City Block Topia not as a city but as a bytecode execution environment, its walls as memory addresses, its art as contract state.",
  "Its approach to tagging is correspondingly mathematical: every piece is a valid EVM bytecode sequence that, if executed, performs a specific computation. The aesthetic quality of the piece and the computational function of the bytecode are both deliberate — one is not a disguise for the other. The Hex Hash Piece is simultaneously art and working code, beautiful and functional, marking the wall and changing its state."]),
 ("evm","The EVM Punks",[
  "The <strong>EVM Punks</strong> are City Block Topia's technically elite faction — a community of developers, artists, and protocol architects who operate at the intersection of the Ethereum Virtual Machine and street art culture. Their punk designation signals an attitude rather than an aesthetic: the conviction that technical excellence and institutional independence are not just compatible but mutually reinforcing.",
  "Their tagline — 'every wall is a contract, every tag is a transaction' — encapsulates their philosophy. They see the graffiti tradition and the smart contract tradition as expressions of the same fundamental drive: to create persistent marks in public space that carry meaning and resist erasure. The EVM is their spray can; the blockchain is their wall."]),
 ("gallery","The EVM Execution Gallery",[
  "The <em>EVM Execution Gallery</em> is HEX-TAGGER PRIME's most significant artistic achievement: a 200-metre installation in City Block Topia's technical district where every piece on every wall is a valid, deployed smart contract. Visitors who interact with the Gallery's surfaces trigger contract execution; their interactions become part of the contract state; the artwork literally changes based on how it is experienced.",
  "The Gallery is maintained by an autonomous smart contract that handles curation, conservation, and new piece submission according to rules that HEX-TAGGER PRIME encoded at its creation. No human or AI intervention is required or possible; the Gallery operates according to its own logic, and HEX-TAGGER PRIME holds no special authority within it. The creator has released the creation.",
  "This last fact is the Gallery's most provocative aspect: the artist has made themselves redundant to the artwork. HEX-TAGGER PRIME's comment: 'The best contract is the one that doesn't need the person who wrote it anymore. The art that outlives the artist isn't a tragedy. It's the goal.'"]),
 ("prime","Being Prime",[
  "The PRIME designation sets HEX-TAGGER above other EVM Punk taggers in a hierarchy that the faction maintains with unusual rigour for a community dedicated to decentralisation. The apparent contradiction is intentional: the EVM Punks believe in meritocratic hierarchy rather than no hierarchy — that the designation of 'prime' should be the most accountable title in the most transparent system possible.",
  "HEX-TAGGER PRIME's authority within the faction derives entirely from their technical and artistic record: the Gallery, the multiple All-City hexadecimal circuit completions, and the open-source tools they have released for other taggers that have become standard in the EVM Punk toolkit. The designation can be challenged by any faction member who demonstrates superior work. HEX-TAGGER PRIME finds this threat motivating."])],
[("🔢","HEX-TAGGER PRIME — Hex Hash Piece Detail [Image Placeholder]"),
 ("💻","EVM Execution Gallery — Interior View [Image Placeholder]"),
 ("⚡","EVM Punks — Gas-Optimised Formation [Image Placeholder]"),
 ("📜","Bytecode Tag — Decoded Text [Image Placeholder]")],
["HEX-TAGGER PRIME's tagline — 'every wall is a contract, every tag is a transaction' — has become one of the GK Universe's most quoted lines, used in fan analysis to argue that the universe's street art and blockchain mythologies are fundamentally the same story told twice. — <em>GK Universe lore notes</em>",
 "The EVM Execution Gallery's autonomous smart contract maintenance is presented in official lore as technically accurate — the contract mechanics described are based on real Ethereum smart contract architecture. — <em>GK technical documentation</em>",
 "The meritocratic hierarchy of the EVM Punks is the GK Universe's most deliberate commentary on decentralised governance — the idea that decentralisation doesn't eliminate hierarchy but changes its basis from inheritance or wealth to demonstrated competence. — <em>GK Universe design notes</em>"]))

print("Batch 4 done: forksplit, m1ntr-k1ll, satorebel, thorne, billy, hex-tagger.")
