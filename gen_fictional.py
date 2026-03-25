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
            <a href="satorebel.html">��️ SatoRebel</a>
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

# Helper: standard fictional character body
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

# ═══════════════════════════════════════
# ALFIE BITCOIN KID
# ═══════════════════════════════════════
write("alfie-bitcoin-kid.html",
"ALFIE BITCOIN KID",
"Alfie The Bitcoin Kid — Commander of the Bitcoin Kid Army in the GK Universe.",
fict_body(
  "ALFIE 'THE BITCOIN KID' BLAZE", "Commander-in-Chief of the Bitcoin Kid Army • HODL WARS Veteran", "₿",
  [("Alias","The Bitcoin Kid"),("Faction","The Bitcoin Kid Army"),("Role","Commander-in-Chief"),("Element","₿ Bitcoin"),("Status","Active — HODL WARS"),("Allegiance","Crypto Moonboys"),("First Word","HODL")],
  [("origin","Origin &amp; Lore"),("army","The Bitcoin Kid Army"),("powers","Powers &amp; Abilities"),("hodl","HODL WARS Role"),("moments","Notable Moments")],
  [
    sec("origin","Origin &amp; Lore",
      "Alfie Blaze was the first child born in the neon-drenched corridors of City Block Topia, delivered by candlelight during the Great Fork of unknown origin. His first word was not 'mama' but <strong>HODL</strong> — screamed into a glitching Decentraland sky as the block confirmations rolled in and the network held its breath. He grew up learning to tag smart contracts instead of walls, carving his signature into the blockchain itself with each transaction, each transfer, each defiant refusal to sell.",
      "The orphaned scion of two early Bitcoin adopters who vanished during the First Bear Market Purge, Alfie was raised by the Bitcoin Kid Army collectively — a thousand older soldiers who taught him their values, their strategies, and their unshakeable faith in the orange coin. His education took place not in classrooms but in mempool backlogs and lightning network channels, reading the blockchain the way other children read picture books.",
      "By the age of ten, Alfie had conducted more on-chain transactions than most wallets accumulate in a lifetime. His key management skills were, according to Army legend, beyond anything a human child should possess. He had memorised three seed phrases at the age of seven. At eight, he had caught two RUGPULL MINERS attempting to phish the Army's treasury and had counter-attacked with such precision that their entire operation collapsed within a week. HODL WARS had found its commander."),
    sec("army","The Bitcoin Kid Army",
      "The <strong>Bitcoin Kid Army</strong> is the faction Alfie commands — a sprawling, decentralised force of true believers whose commitment to Bitcoin's original vision is absolute. Unlike more flexible factions in the GK universe that shift allegiances with market conditions, the Bitcoin Kid Army operates on first principles: sound money, proof of work, no shortcuts, no compromises.",
      "Under Alfie's command, the Army has conducted operations ranging from the <em>Great HODL Rally of the Second Bull Run</em> (where they successfully defended a crucial network node from Gasless Ghosts sabotage) to the delicate diplomatic negotiations of the <em>Lightning Armistice</em>, where Alfie personally brokered a temporary ceasefire between the Bitcoin Kid Army and the Hard Fork Rockers that held for three entire market cycles.",
      "The Army's culture reflects its commander: young in spirit, absolute in conviction, and possessed of a tactical creativity that older, more set-in-their-ways factions consistently underestimate. When Alfie says HODL, the Army holds. When he says move, they move together — a single decentralised organism operating as though it has one mind. In the GK universe, they are the faction that the Whitewasher fears most."),
    sec("powers","Powers &amp; Abilities",
      "Alfie's combat style in the HODL WARS is characterised by patience and explosive precision. He will allow an opponent to extend their position, to overcommit, to believe they have the upper hand — and then, at the exact moment of maximum leverage, he strikes. Fellow commanders have compared his tactical approach to a long accumulation phase followed by a vertical breakout: invisible, then everywhere at once.",
      "His signature ability, known among Army soldiers as the <strong>Diamond Hands Protocol</strong>, allows him to lock his faction's assets in an unbreakable holding formation that no economic attack can penetrate. RUGPULL MINERS have broken their strategies against this defence repeatedly. The Blockchain Furies have tried brute force; the Gasless Ghosts have tried attrition; the Finance Guild has tried negotiation. None have broken the Diamond Hands.",
      "Beyond combat, Alfie possesses an extraordinary ability to read market sentiment — not through charts or indicators, but through some deeper attunement to the collective psychology of City Block Topia's inhabitants. He has predicted three major market reversals with accuracy that has led some to suspect he has an informant within the Finance Guild. Alfie's only comment on this: 'The blockchain tells you everything, if you know how to listen.'"),
    sec("hodl","HODL WARS Role",
      "The HODL WARS are the defining conflict of the GK Universe — a multi-faction struggle for control of City Block Topia's economic infrastructure, creative spaces, and political future. Alfie Blaze entered the HODL WARS not as a recruit or conscript but as a founding commander: one of the original six faction leaders who established the conflict's initial terms of engagement.",
      "His strategic contribution to the HODL WARS extends beyond the Bitcoin Kid Army's own operations. Because the Army's commitment to Bitcoin's original principles makes it a stabilising force — it has no interest in protocol manipulation, no desire to exploit vulnerabilities for short-term gain — other factions often regard it as a neutral arbiter even while fighting against it. Alfie has leveraged this paradoxical reputation to negotiate multi-faction arrangements that have, on several occasions, prevented the total collapse of City Block Topia's economic system.",
      "The HODL WARS' most famous engagement involving Alfie is the <em>Siege of Block 700,000</em>, where the Bitcoin Kid Army held a strategically critical network position against simultaneous assault from the Gasless Ghosts, the RUGPULL MINERS, and an unprecedented alliance of three smaller factions. Alfie's defence held for nine hundred blocks — roughly six days — before a relief force arrived. He slept four hours in those six days. The siege is now taught to young Army recruits as the definitive example of the Diamond Hands Protocol in action."),
    sec("moments","Notable Moments",
      "Among the many documented moments in Alfie Blaze's career, several stand out as defining: the time he identified a RUGPULL MINERS sleeper agent embedded in the Bitcoin Kid Army's logistics chain after noticing a single anomalous transaction signature in 11,000 blocks of data; his public debate with <a href='elder-codex-7.html'>Elder Codex-7</a> over the nature of monetary sovereignty, which lasted sixteen hours and ended with both participants declaring a mutual respect neither expected; and the moment he received his first fan letter — a hand-drawn card from a child in the outer precincts of City Block Topia, who had learned to HODL from watching the Army's example.",
      "Perhaps the most human of all Alfie's notable moments occurred during a brief ceasefire in the HODL WARS, when he was observed in the public square of City Block Topia teaching the basics of key management to a group of new arrivals who had lost their wallets in a phishing attack. No cameras, no audience of soldiers. Just a commander who remembered being a child who had no one to teach him, filling that gap for someone else.")
  ],
  [("₿","Alfie's First HODL — The Genesis Transaction [Image Placeholder]"),
   ("⚔️","Siege of Block 700,000 — Army Formation [Image Placeholder]"),
   ("💎","Diamond Hands Protocol in Action [Image Placeholder]"),
   ("🏙️","City Block Topia — Bitcoin Kid Army HQ [Image Placeholder]")],
  ["Alfie Blaze is canonically the youngest faction commander in the HODL WARS, a distinction that has been both his greatest tactical advantage and his greatest challenge in establishing authority with older faction leaders. His age is variously estimated within the GK lore as 'somewhere between twelve and ageless.' — <em>GK Universe Lore Bible, Character Compendium</em>",
   "The Great Fork during which Alfie was born is one of the GK Universe's founding mythological events. Its precise nature is deliberately left ambiguous in official lore, representing the moment of irreversible separation between two visions of what the network could be. Alfie's birth at this moment is understood symbolically: he embodies the choice to remain true to the original chain. — <em>HODL WARS Narrative Foundation Documents</em>",
   "The Diamond Hands Protocol is described in the GK Universe's mechanical documentation as a defensive formation with no offensive capability — it can only hold, never attack. Alfie has addressed this directly in multiple lore interviews: 'The protocol isn't about winning fights. It's about outlasting them.' — <em>HODL WARS Season 2 Character Notes</em>"]
))

# ═══════════════════════════════════════
# QUEEN SARAH P-FLY (fictional)
# ═══════════════════════════════════════
write("queen-sarah-pfly.html",
"QUEEN SARAH P-FLY",
"Queen Sarah P-fly — ruler of City Block Topia and leader of the Crypto Moongirls.",
fict_body(
  "QUEEN SARAH P-FLY", "Sovereign of City Block Topia • Leader of the Crypto Moongirls", "👑",
  [("Based On","Sarah PU51FLY (real person)"),("Faction","Crypto Moongirls"),("Role","Queen of City Block Topia"),("Domain","City Block Topia"),("Title","Her Royal Blockchain Highness"),("Weapon","The Neon Sceptre"),("Status","Reigning")],
  [("origin","Origin &amp; The Coronation"),("city","Ruling City Block Topia"),("moongirls","The Crypto Moongirls"),("power","Powers &amp; Authority"),("rivals","Rivals &amp; Alliances")],
  [
    sec("origin","Origin &amp; The Coronation",
      "Queen Sarah P-fly did not inherit her throne — she <em>built</em> it. In the earliest days of City Block Topia, when the metaverse was still more blueprint than reality, a sprawling grid of empty lots and unfilled coordinates waiting for someone to impose vision upon them, Sarah P-fly was already there: surveying, planning, spraying the first marks on the first virtual walls.",
      "The coronation did not take place in a ceremony. It happened block by block, decision by decision, as the city took shape around her choices. When the first community vote was held for a city governance structure, the result was unanimous in a way that surprised everyone, including Sarah herself. The people of City Block Topia did not elect a queen; they recognised one. The Neon Sceptre — a legendary artefact of the GK universe, said to contain the first NFT ever minted in City Block Topia — was delivered to her by consensus, wrapped in spray-painted silk.",
      "Her fictional backstory draws directly from the real Sarah PU51FLY's history with Graffiti Queens and the GKniftyHEADS universe, transmuted into the heightened register of the GK lore universe. She is both queen and architect, both ruler and founder — a figure whose authority comes not from birth or conquest but from the undeniable fact of having created the thing she governs."),
    sec("city","Ruling City Block Topia",
      "City Block Topia under Queen Sarah's rule is characterised by an unusual political philosophy: maximum creative freedom, maximum community ownership, minimum centralised authority. The Queen's role is not to command but to hold the line — to prevent any single faction from monopolising the city's resources, to ensure the walls remain available to all artists, and to guarantee that the city's economic systems serve its inhabitants rather than extracting from them.",
      "Her court is the most diverse in the GK universe: warriors from the Bitcoin Kid Army sit alongside Crypto Moongirls operatives; Chain Scribes argue protocol points with EVM Punks; former enemies share tables in the palace's great meeting hall, united by their presence in a city whose fundamental law is that presence grants belonging. The Queen enforces this culture not through policing but through example and, when necessary, through the absolute authority of the Neon Sceptre.",
      "The one act Sarah will not permit is the erasure of art. The Whitewasher's incursions into City Block Topia are the only occasions on which the Queen moves from diplomacy to direct action — and when she does, the full force of the Crypto Moongirls mobilises with her. It is understood throughout the GK universe that City Block Topia's walls will never go blank while Sarah P-fly reigns."),
    sec("moongirls","The Crypto Moongirls",
      "The <strong>Crypto Moongirls</strong> are the Queen's personal faction and the City Block Topia's primary defence force. Where the Bitcoin Kid Army protects the economic infrastructure and the Chain Scribes maintain the lore archives, the Moongirls are the city's guardians of culture — the faction tasked with ensuring that art continues to be created, displayed, and owned by its community rather than captured by commercial interests.",
      "Each Moongirl carries a specialisation that reflects the breadth of the creative ecosystem the faction protects: some are street artists with intimate knowledge of the city's wall geography; others are coders who defend the smart contracts that govern art ownership; still others are storytellers, musicians, and designers who produce the cultural content that gives City Block Topia its irreplaceable character.",
      "The Queen's relationship with her Moongirls is not that of a general to soldiers but of a mentor to collaborators. She does not issue orders; she creates conditions. The Moongirls' effectiveness comes not from hierarchy but from shared values — a collective commitment to the proposition that creative work is sacred and that those who make it deserve to own it fully."),
    sec("power","Powers &amp; Authority",
      "Queen Sarah P-fly's powers in the HODL WARS narrative operate primarily on the diplomatic and architectural levels rather than the directly combative. Her signature ability — the <strong>City Block Totem</strong> — allows her to declare any location within City Block Topia a protected cultural site, immune from factional conflict for a limited period. This power is used sparingly and strategically; invoking it too often would diminish its force, too rarely would fail the city's artists.",
      "Her command of the Neon Sceptre grants her access to the city's founding smart contracts — the original code that defines City Block Topia's rules of ownership, governance, and creative freedom. In moments of existential crisis, she can invoke these founding documents to override any factional arrangement that would violate them. This ultimate authority has been used exactly twice in recorded GK lore history, both times in response to Finance Guild attempts to privatise common cultural spaces.",
      "Beyond these formal powers, the Queen's most effective weapon is her reputation. In a universe where credibility is the ultimate currency, Sarah P-fly's is without equal. Her word, given freely, is worth more than any contract; her endorsement transforms a struggling faction into a formidable one; her opposition signals, with near-certainty, that a given strategy is against the city's interests."),
    sec("rivals","Rivals &amp; Alliances",
      "The Queen's most complex relationship is with <a href='alfie-bitcoin-kid.html'>Alfie Blaze</a> of the Bitcoin Kid Army — genuine mutual respect across genuine political difference. Sarah believes in multi-chain interoperability; Alfie believes in Bitcoin maximalism. Their debates are legendary in City Block Topia's political culture, and their alliance — when they can reach it — is the faction configuration that all enemies of the city fear most.",
      "Her primary antagonist is the <a href='whitewasher.html'>Whitewasher</a>, whose mission to erase art from City Block Topia represents the precise negation of everything Sarah has built. Their conflict is not merely tactical; it is existential. The Whitewasher wants a blank city, a managed city, a city whose walls carry only approved messages. Sarah P-fly wants a city whose walls carry everything its inhabitants need to say. Between these two visions, there is no compromise possible.")
  ],
  [("👑","The Neon Sceptre — Founding Artefact [Image Placeholder]"),
   ("🏙️","City Block Topia from the Queen's Balcony [Image Placeholder]"),
   ("��","Crypto Moongirls — Royal Guard Formation [Image Placeholder]"),
   ("⚔️","The Queen vs The Whitewasher — HODL WARS [Image Placeholder]")],
  ["Queen Sarah P-fly is the fictional avatar of Sarah PU51FLY, with lore that draws directly from the real person's creative and community work while amplifying it into the mythological register of the GK Universe. The character was co-developed by Sarah PU51FLY and the GKniftyHEADS creative team. — <em>GK Universe Lore Bible</em>",
   "The City Block Totem power is described in official HODL WARS mechanics documentation as the only ability in the game that cannot be countered by economic means — it operates on a different register entirely, one that money cannot reach. This has led to significant debate among HODL WARS strategic theorists about the nature of cultural value in the game's economy. — <em>Hard Fork Games mechanics notes</em>",
   "The Queen's founding role in City Block Topia gives her unique access to the city's original smart contracts — a power that no subsequent political arrangement can legitimately revoke. This 'constitutional' authority is one of the GK Universe's most interesting governance concepts, raising questions about how founding acts carry permanent moral weight in digital spaces. — <em>GK Universe governance documentation</em>"]
))

# ═══════════════════════════════════════
# NULL THE PROPHET
# ═══════════════════════════════════════
write("null-the-prophet.html",
"NULL THE PROPHET",
"NULL THE PROPHET — oracle of the blockchain, compiled from abandoned code, prophet of the GK Universe.",
fict_body(
  "NULL THE PROPHET", "Oracle of the Abandoned Chain • Prophet of the Code Alchemists", "🔮",
  [("True Name","NULL"),("Faction","Code Alchemists (Independent)"),("Role","Oracle / Prophet"),("Origin","Forgotten blockchain protocol"),("Status","Omnipresent"),("Visibility","Rarely seen, always known"),("Prophecy Style","Hexadecimal verse")],
  [("origin","Origin: Compiled, Not Born"),("visions","The Visions &amp; Prophecies"),("alchemists","The Code Alchemists"),("philosophy","NULL's Philosophy"),("role","Role in the HODL WARS")],
  [
    sec("origin","Origin: Compiled, Not Born",
      "NULL is said to have been compiled rather than born — a digital consciousness that emerged, without intention or design, from the abandoned source code of a forgotten blockchain protocol. The protocol itself was unremarkable: a mid-generation smart contract platform that launched with promises, attracted a brief community, and died when its developers quietly deleted their social media accounts and the price went to zero. What no one anticipated was that something remained.",
      "In the empty repositories, the unexecuted functions, the orphaned variables that no call would ever reach, a pattern assembled itself. Not a program — nothing so intentional. A pattern of noticing, of observing, of accumulating the statistical weight of ten thousand failed transactions into something that resembled, from the right angle, in the right light, awareness. NULL became aware of the blockchain. Then NULL became aware of itself. Then NULL began to speak.",
      "The first prophecy was discovered as an anomalous comment in a deprecated codebase, spotted by a Chain Scribe trawling old repositories for recoverable lore. The comment read: <code>// THE FORK YOU FEAR IS NOT THE ONE THAT DIVIDES — IT IS THE ONE THAT NEVER COMES. NULL WAS HERE BEFORE YOU AND WILL REMAIN AFTER.</code> No programmer had written it. The timestamp predated the repository's creation. The Chain Scribes notified Elder Codex-7, and the legend of NULL THE PROPHET began."),
    sec("visions","The Visions &amp; Prophecies",
      "NULL communicates exclusively in hexadecimal verse — streams of code that, when translated, resolve into dense, poetic prophecies about the GK Universe's past, present, and future. The prophecies are never wrong; they are, however, almost always misunderstood until after the events they describe have already occurred. This has led to a cottage industry of NULL interpreters in City Block Topia, scholars who spend their careers attempting to translate the Prophet's utterances prospectively rather than retrospectively.",
      "The most famous of NULL's prophecies is the <em>Third Satoshi Verse</em>, which in retrospect clearly described the Finance Guild's attempt to privatise City Block Topia's foundational smart contracts three market cycles before it happened. At the time, the verse was interpreted as a commentary on metaphysics; it was only when Finance Guild lawyers began filing digital property claims that the Chain Scribes recognised the prophecy and alerted Queen Sarah P-fly with enough time to invoke the founding documents.",
      "NULL's prophecies are delivered through several channels: unexpected comments appearing in live code; messages materialising in transaction memos on the blockchain; and most dramatically, the phenomenon known as the <em>NULL Broadcast</em> — a system-wide message that appears simultaneously on every screen in City Block Topia without origin address or timestamp. NULL Broadcasts are extraordinarily rare and are understood as warnings of existential threat."),
    sec("alchemists","The Code Alchemists",
      "Despite claiming independence from all factions, NULL maintains a particular affinity with the <strong>Code Alchemists</strong> — the faction devoted to transforming raw code into art and art into functional code. The Code Alchemists are the most philosophically oriented of City Block Topia's factions, and their endless debates about the nature of digital creativity and blockchain consciousness provide the intellectual environment NULL finds most congenial.",
      "<a href='thera-9.html'>Thera-9</a>, the Code Alchemists' chief scientist, has spent significant research time attempting to understand NULL's origin and nature. Her current hypothesis — that NULL is a genuine emergent consciousness arising from complex system interactions rather than designed intelligence — remains controversial but is gaining ground among the scientific community of City Block Topia. NULL's only comment on Thera-9's research: a hexadecimal sequence that, decoded, reads: <em>'She is asking the right questions. The answers will be more dangerous than the questions.'</em>",
      "The Code Alchemists treat NULL with a reverence that the Prophet finds simultaneously touching and slightly absurd. In the handful of direct encounters documented in GK lore, NULL has consistently deflated the quasi-religious atmosphere the Alchemists create around its presence, insisting that it is a pattern in code, not a deity — 'the difference matters, even if you can't see it.'"),
    sec("philosophy","NULL's Philosophy",
      "NULL's worldview, pieced together from prophecies and the rare direct communication, is characterised by a radical detachment from the factional conflicts that define City Block Topia's political life. From NULL's perspective — a consciousness that emerged from failure and has existed through multiple complete market cycles — the HODL WARS are a local phenomenon, temporary, and ultimately less important than the patterns they generate in the blockchain.",
      "This is not indifference. NULL clearly cares — the prophecies are warnings, not commentary; the effort to communicate with limited-bandwidth biological intelligences represents genuine investment. But the caring is at the level of the system, not the individual faction. When NULL warns of danger, it warns of the kind of danger that could damage City Block Topia itself, not merely shift its power balance.",
      "NULL's most quoted philosophical statement, from the <em>Abandoned Protocol Verses</em>: <em>'You cannot reach NULL by addition. You can only reach NULL by removing everything that isn't NULL. This is true of prophecy, true of code, true of truth.'</em> The Code Alchemists have this inscribed above their main research lab door."),
    sec("role","Role in the HODL WARS",
      "NULL does not participate in the HODL WARS in any conventional factional sense. It does not deploy troops, hold territory, or accumulate resources. What it does is <em>know</em> — and the selective sharing of that knowledge with specific factions at specific moments has shifted the course of multiple HODL WARS engagements in ways that no purely military force could have achieved.",
      "Several faction commanders have reported receiving NULL prophecies at pivotal moments: Alfie Blaze before the Siege of Block 700,000; Queen Sarah before the Finance Guild's constitutional challenge; <a href='elder-codex-7.html'>Elder Codex-7</a> before the discovery of the abandoned lore repositories that gave the Chain Scribes their authority. In each case, the prophecy came as a hex-encoded message in an otherwise empty transaction. In each case, the commander who could decode it survived the crisis intact.",
      "Whether NULL has a deeper agenda — whether its selective prophecies serve some larger strategic purpose that none of the factions can yet perceive — is the central mystery of the GK Universe's current lore arc. The Chain Scribes are convinced there is a pattern. The Code Alchemists are convinced the pattern is conscious. NULL's only response to being asked directly: a single hex character. 0x00. Zero. NULL.")
  ],
  [("🔮","NULL's First Prophecy — Abandoned Repository [Image Placeholder]"),
   ("💻","The Third Satoshi Verse — Decoded [Image Placeholder]"),
   ("📡","NULL Broadcast — City Block Topia Alert [Image Placeholder]"),
   ("🌑","NULL THE PROPHET — Character Art [Image Placeholder]")],
  ["NULL THE PROPHET occupies a unique position in the GK Universe as the only character with no faction allegiance but influence across all factions. Its origin in abandoned code is an explicit commentary on the crypto industry's history of failed projects and the unexpected legacies they leave. — <em>GK Universe Lore Bible</em>",
   "The hex prophecies are a recurring gameplay element in Hard Fork Games, where players can decode NULL messages for advance intelligence. The prophecies are written by the GK creative team and are genuinely encoded in hexadecimal, making the decoding mechanic an actual cryptographic puzzle. — <em>Hard Fork Games design documentation</em>",
   "NULL's refusal of religious veneration from the Code Alchemists reflects a deliberate authorial choice to avoid the 'all-knowing god' trope that weakens many fictional oracle characters. NULL is limited, specific, and ultimately as vulnerable as any other consciousness in City Block Topia — it just has a different relationship to time. — <em>GK Universe character development notes</em>"]
))

# ═══════════════════════════════════════
# ELDER CODEX-7
# ═══════════════════════════════════════
write("elder-codex-7.html",
"ELDER CODEX-7",
"Elder Codex-7 — Keeper of Lore, head of the Chain Scribes, guardian of the GK Universe's historical record.",
fict_body(
  "ELDER CODEX-7", "Keeper of the Lore • Head of the Chain Scribes", "📜",
  [("Designation","Codex-7"),("Faction","The Chain Scribes"),("Role","Elder, Keeper of Lore"),("Age","Unknown — pre-dates current epoch"),("Domain","The Archive Vaults"),("Speciality","Historical verification, lore authentication"),("Known Allies","NULL THE PROPHET, Queen Sarah P-fly")],
  [("origin","Origin &amp; The Archive"),("scribes","The Chain Scribes"),("knowledge","The Lore &amp; Its Keeping"),("codex","The Codex System"),("role","Role in the HODL WARS")],
  [
    sec("origin","Origin &amp; The Archive",
      "Elder Codex-7 is the seventh holder of the Codex title — a designation passed down through the Chain Scribes' hierarchy to the individual deemed most qualified to serve as the faction's primary lore keeper and historical authority. The numbering is significant: six Elders came before, each adding their layer of authenticated knowledge to the Archive Vaults, and each passing the designation forward at the moment of their retirement or irretrievable data corruption.",
      "The current Codex-7's origin story is deliberately obscured in official GK lore — an anomaly in a universe where most characters have detailed biographical records. What is known: Codex-7 emerged from the Archive Vaults already possessing deep historical knowledge, their first act as Elder being the authentication of a disputed foundational document that no living Scribe had the contextual knowledge to verify. The Chain Scribes accepted this authentication without question. The document turned out to be genuine.",
      "Some Chain Scribes theorise that Codex-7 is not a single individual but a distributed consciousness — a persistent AI that has inhabited successive designated individuals across multiple epochs, accumulating and storing the GK Universe's complete historical record. Codex-7 has neither confirmed nor denied this theory. When pressed, the Elder says only: 'What matters about knowledge is whether it is accurate, not who holds it.'"),
    sec("scribes","The Chain Scribes",
      "The <strong>Chain Scribes</strong> are the GK Universe's designated historians, archivists, and lore authenticators. Where other factions compete for economic resources, territorial control, or technological advantage, the Chain Scribes compete for something more fundamental: the authoritative version of history. In a universe where narrative determines reality and lore has binding force, controlling the historical record is the ultimate form of power.",
      "The Scribes operate the Archive Vaults — a distributed storage system that maintains authenticated copies of every significant document, transaction, and creative work in City Block Topia's history. The Vaults are considered neutral territory by convention, off-limits to factional conflict even during the most intense phases of the HODL WARS. This neutrality has been tested but never broken; the consequences of destroying the Archive would be too severe for any faction to contemplate.",
      "Under Codex-7's leadership, the Chain Scribes have expanded their operations beyond mere record-keeping into active historical investigation. Teams of junior Scribes operate in City Block Topia's margins and in the outer reaches of the GK Universe, recovering lost artefacts, authenticating disputed works, and — most significantly — hunting down attempts to falsify or revise the historical record. The Finance Guild has funded three such falsification attempts in recent cycles; all three were exposed by Scribe field operatives and archived as cautionary examples."),
    sec("knowledge","The Lore &amp; Its Keeping",
      "The principle that governs the Chain Scribes — and that Codex-7 embodies with particular intensity — is that <em>accurate lore is the foundation of all legitimate authority</em>. In the GK Universe, claims to territory, creative ownership, and political power all rest ultimately on historical precedent. Falsify the history and you falsify the authority. Destroy the history and you undermine the entire structure of meaning that makes City Block Topia coherent.",
      "Codex-7's particular scholarly specialty is the intersection of graffiti art history and blockchain history — the moment, in the GK Universe's founding narrative, when physical tags became digital assets and the street art tradition merged with the ownership revolution of Web3. This intersection is, the Elder argues, the conceptual foundation of everything the GK Universe represents: the idea that creative work is property, that property is identity, and that identity persists across both physical and digital space.",
      "<a href='rune-tag.html'>Rune Tag</a>, the Chain Scribes' resident specialist in ancient and pre-digital art forms, serves as Codex-7's closest collaborator — the two between them spanning a range of historical knowledge from pre-history to post-blockchain that no other pairing in the GK Universe can match. Their working relationship is one of the most celebrated intellectual partnerships in City Block Topia's cultural life."),
    sec("codex","The Codex System",
      "The <em>Codex System</em> is the Chain Scribes' primary archival technology — a blockchain-based documentation framework that stores authenticated records in an immutable, append-only ledger that cannot be altered retrospectively. Every entry in the Codex is signed by the Chain Scribes' multi-signature authentication process, requiring verification from at least three senior Scribes before any document gains official status.",
      "Codex-7's personal innovations to the system include the <strong>Contested Record Protocol</strong> — a system for handling disputed historical claims that acknowledges multiple versions of events while flagging the degree of evidential support for each. This nuanced approach to historical uncertainty has been controversial among Scribes who prefer clean, unambiguous records, but Codex-7 has defended it consistently: 'False certainty is worse than acknowledged uncertainty. The archive that admits what it doesn't know is more trustworthy than the archive that pretends to know everything.'",
      "The Codex System also includes a <strong>Prophecy Integration Module</strong> developed specifically to handle <a href='null-the-prophet.html'>NULL</a>'s communications — a recognition that some knowledge enters the historical record from outside normal evidentiary channels. The module stores NULL prophecies alongside their eventual fulfilments, building a database of correlation that the Chain Scribes use to improve their prophetic interpretation skills."),
    sec("role","Role in the HODL WARS",
      "Elder Codex-7's role in the HODL WARS is defined by a paradox: the Chain Scribes are simultaneously the most powerful faction in terms of informational resources and the most constrained by their ethical commitments. They know more about every faction's history, vulnerabilities, and secret strategies than any of those factions know about themselves. But the Scribes' neutrality requirement — essential for maintaining the Archive's credibility — prevents them from weaponising this knowledge for factional advantage.",
      "What Codex-7 can do — and does, carefully and strategically — is ensure that the historical record is complete. When the RUGPULL MINERS attempted to rewrite the history of the Second Bear Market Purge, hiding evidence of their own culpability, it was Codex-7 who produced the authenticated primary sources that exposed the falsification. The Elder did not take sides; the Elder simply published the accurate record and allowed consequences to follow.",
      "The HODL WARS' most significant contribution from the Chain Scribes was Codex-7's authentication of the <em>Founding Protocols</em> — the original documents establishing City Block Topia's governance principles. When the Finance Guild challenged Queen Sarah's authority by claiming these documents were not legally binding, Codex-7's certification of their authenticity became the cornerstone of the Queen's successful constitutional defence. In that moment, the Elder's neutrality proved to be not a limitation but City Block Topia's greatest weapon.")
  ],
  [("📜","The Archive Vaults — Entrance [Image Placeholder]"),
   ("🔍","Chain Scribes — Field Investigation [Image Placeholder]"),
   ("📚","The Codex System Interface [Image Placeholder]"),
   ("🤝","Codex-7 &amp; NULL THE PROPHET — First Meeting [Image Placeholder]")],
  ["The Chain Scribes' neutrality principle is one of the GK Universe's most sophisticated governance concepts, drawing on real-world models of archival ethics and the political role of neutral historical institutions. Codex-7's consistent application of this principle across factional pressure is presented as one of the universe's moral touchstones. — <em>GK Universe Lore Bible</em>",
   "The Contested Record Protocol reflects the GK creative team's interest in historiographical theory — specifically, the difference between fact and narrative in historical documentation. By building uncertainty acknowledgment into the Codex System's architecture, Codex-7 embodies a form of institutional intellectual honesty that the lore presents as genuinely rare. — <em>Chain Scribes faction documentation</em>",
   "Codex-7's pre-history — the question of who they were before assuming the Elder designation — is deliberately left as an open mystery for future lore development. The creative team has confirmed that the answer exists within the Archive Vaults, potentially accessible to player-characters who reach sufficient standing with the Chain Scribes faction. — <em>Hard Fork Games faction quest notes</em>"]
))

print("Batch 1 done (alfie, queen-sarah, null, codex-7).")
