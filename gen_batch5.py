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

def char_page(name, subtitle, emoji, inforows, sections_data, gal_items, cites):
    ib = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k,v in inforows)
    toc = "".join(f'<li><a href="#{s}">{t}</a></li>' for s,t,_ in sections_data)
    secs = "".join(
        f'<section class="section" id="{s}"><h2 class="section-title">{t}</h2><div class="graffiti-divider"></div>{"".join(f"<p>{p}</p>" for p in ps)}</section>'
        for s,t,ps in sections_data)
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

# The remaining characters
remaining = [
  ("whitewasher.html","THE WHITEWASHER","The Whitewasher — antagonist, enemy of art, agent of erasure in the GK Universe.",
   "THE WHITEWASHER","Enemy of Art • Agent of Erasure • The Blank That Hunts","🚫",
   [("Faction","Antagonist — No Allegiance"),("Role","Primary Villain"),("Style","Erases art, enforces silence"),("Weapon","The Obliteration Roller"),("Motivation","Control through blankness"),("Status","Active — Constant Threat")],
   [("origin","origin","Origin &amp; Motivation",[
     "The Whitewasher has no single origin story — because it is not a single entity. It is the name given to the force of erasure itself: the impulse to control by making blank, to manage by removing expression, to assert dominance over public space by reducing it to nothing. In City Block Topia, the Whitewasher has taken the form of an operative — tall, dressed in immaculate white, carrying the Obliteration Roller — but this form is understood to be a physical manifestation of an institutional tendency rather than an individual.",
     "In the GK Universe's mythology, the Whitewasher is the eternal antagonist of graffiti culture — the force that paints over the tags, fills in the pieces, restores the surfaces to the blank state that represents order, compliance, and the absence of unauthorised speech. Its motivation is not personal malice but institutional logic: blank walls are controllable walls, and controllable walls serve the interests of those who prefer a managed public sphere.",
     "The Finance Guild has funded Whitewasher operations. Municipal authorities in City Block Topia's governance system have contracted Whitewasher services. Individual property owners have welcomed its work. None of these are presented in GK lore as villainous; they are presented as honest about their interests. The Whitewasher is the antagonist not because it is wrong by its own lights but because those lights, in the GK Universe, illuminate a genuinely frightening vision of the world."]),
    ("roller","whitewash","The Obliteration Roller",[
     "The Obliteration Roller is the Whitewasher's primary tool — a device that doesn't merely cover existing art but erases the surface beneath it, creating a blank that carries no trace of what was there before. Unlike conventional overpainting, which preserves the underlying work under a layer of coverage, the Roller removes history. The Chain Scribes consider it the most dangerous weapon in City Block Topia's conflict because it is the only weapon that can undo what they do.",
     "The Roller's operation is not limited to physical surfaces. In digital contexts, the Whitewasher deploys equivalent tools against NFT metadata, blockchain records, and the distributed archives that maintain City Block Topia's creative history. These digital erasure tools are more sophisticated and more difficult to counter than the physical Roller; the faction's most dangerous capability is its ability to remove provenance records rather than artworks."]),
    ("resistance","resist","Resisting the Whitewasher",[
     "Every major faction in City Block Topia maintains some form of resistance to Whitewasher operations. The Chain Scribes' most fundamental mission — the preservation of the historical record — is, at its root, a Whitewasher countermeasure. Lady-INK's All-City runs are documented with Chain Scribe authentication specifically so that the blockchain record survives the physical removal of her work. The EVM Punks' deployed smart contracts are designed to be non-erasable in principle.",
     "The most effective resistance, documented across multiple HODL WARS seasons, is the community response developed during the Hash Rate Siege of the Northern Precincts: when the Whitewasher operates, flood the space with creative activity that generates more documentation than the erasure can keep up with. Art made in quantity, distributed across multiple systems, and authenticated before it can be removed. The Whitewasher operates at a rate; the community's creative output can exceed that rate."]),
    ("meaning","meaning","What the Whitewasher Means",[
     "In the deepest reading of GK Universe lore, the Whitewasher is not primarily a character but a question: what is a city for? Is public space an managed asset, to be kept in its authorised state by authorised agents? Or is it a commons, belonging to those who live in it and entitled to carry the marks of that living?",
     "The GK Universe's answer is in its history: Darren Cullen tagged London's walls in 1983 because he had something to say and the wall was there to say it on. Every subsequent development in the GK universe — the legal commissions, the Leake Street tunnel, the Olympic murals, the NFT collections, City Block Topia itself — is an elaboration of that first act. The Whitewasher opposes not just the specific marks but the underlying conviction that produced them. That is why it is the primary antagonist. That is why it cannot win."]),
    ],
   [("🚫","The Whitewasher — Approaching [Image Placeholder]"),
    ("⚪","Obliteration Roller — Effect Documentation [Image Placeholder]"),
    ("🎨","Community Response — Art Flood [Image Placeholder]"),
    ("📜","Chain Scribes — Erasure Counter-Documentation [Image Placeholder]")],
   ["The Whitewasher is the GK Universe's most explicitly political creation — a direct representation of the forces that have always sought to remove graffiti art from public space, recontextualised in the blockchain era. — <em>GK Universe design notes</em>",
    "The Obliteration Roller's ability to erase blockchain records rather than just physical surfaces is presented in Hard Fork Games as a high-level threat mechanic that requires specific counter-measures from player factions. — <em>Hard Fork Games mechanics documentation</em>",
    "The Whitewasher's complex funding network — multiple legitimate factions using its services for different reasons — is the GK Universe's most direct engagement with the question of how oppressive forces maintain themselves through the voluntary cooperation of people who aren't themselves oppressive. — <em>GK narrative notes</em>"]),

  ("grit.html","GRIT","GRIT, street soldier of the GRAFFPUNKs, raw punk energy in City Block Topia.",
   "GRIT","Street Soldier of the GRAFFPUNKs • Raw, Unpolished, Unstoppable","🎸",
   [("Faction","The GRAFFPUNKs"),("Role","Street Soldier"),("Style","Raw, unpolished punk energy"),("Weapon","The Spray Shard"),("Status","Active — Always"),("Philosophy","No clean lines. No apologies.")],
   [("origin","origin","Origin &amp; The GRAFFPUNKs",[
     "GRIT doesn't have an origin story in the conventional sense. GRIT has a <em>trajectory</em> — a line of force that has been moving in the same direction since it began, gathering speed and substance as it goes. Born in City Block Topia's most neglected district, in the precinct where the neon signs stutter and the blockchain connectivity is too thin for financial speculation but thick enough for art, GRIT has been painting and fighting and painting since before any record exists.",
     "The GRAFFPUNKs found GRIT — or GRIT found the GRAFFPUNKs — through the process of natural selection. The faction's culture attracts and retains the artists who refuse to compromise their work for any institutional consideration, and GRIT is the most uncompromising of them. Their technique is deliberately rough: thick lines, aggressive colour, letter structures that prioritise impact over refinement. Graffiti critics have described GRIT's work as 'optimised for being seen from a moving train by someone who had exactly enough time to read it.' GRIT takes this as a compliment."]),
    ("punk","punk","Punk Ideology",[
     "The GRAFFPUNKs draw explicitly on British punk's tradition of institutional refusal — the conviction that the mainstream's standards exist to serve the mainstream's interests, and that art made according to those standards serves those interests too. Punk aesthetics, in this reading, are not crude because their makers lacked skill but crude because they chose to prioritise the authentic expression of genuine experience over the polished execution of conventional craft.",
     "GRIT embodies this ideology with particular directness. Their work is not unrefined by accident; it is unrefined by conviction. The Spray Shard — their signature weapon, fashioned from the broken pieces of used aerosol cans — is both a practical tool and a statement: waste as weapon, the discarded materials of consumption repurposed as instruments of resistance."]),
    ("community","community","Community &amp; Solidarity",[
     "Beneath GRIT's aggressively punk exterior is a community sensibility that surprises people who encounter it for the first time. The GRAFFPUNKs may reject institutional standards but they maintain their own rigorous internal culture of mutual support, creative development, and respect for authenticity. GRIT is known within the faction for mentoring younger punks with a directness and patience that their public persona would not predict.",
     "Their relationship with <a href='grit42.html'>Grit42</a> — the faction's senior punk and GRIT's most significant creative influence — is the GK Universe's most tender depicted relationship between characters who present themselves as entirely unsentimental. When Grit42 was threatened by a Finance Guild operation, GRIT's response was the most sustained single-faction defensive campaign in GRAFFPUNKs history. No strategic calculation. Pure loyalty."]),
    ("wall","wall","The Unclean Wall",[
     "GRIT's most famous artistic statement is the <em>Unclean Wall</em> — a continuous piece that runs the full length of City Block Topia's eastern boundary, painted and repainted every season as conditions and inspirations change. It is not a single artwork but a document: the accumulated marks of years of GRAFFPUNKs activity, each layer visible beneath the current surface, each addition changing the piece's meaning without erasing what came before.",
     "When the Whitewasher attempted to remove the Unclean Wall during the third HODL WARS season, the entire GRAFFPUNKs faction mobilised in less than two hours. The Whitewasher retreated after a confrontation that lasted three minutes. The Wall was repainted that evening with a piece referencing the attempt, which has since been reproduced as one of the GK Universe's most iconic images."])],
   [("🎸","GRIT — Unclean Wall Work [Image Placeholder]"),
    ("💥","Spray Shard — Weapon Detail [Image Placeholder]"),
    ("🏙️","GRAFFPUNKs — Eastern Boundary [Image Placeholder]"),
    ("🤝","GRIT &amp; Grit42 — Partnership [Image Placeholder]")],
   ["GRIT's visual design draws on British punk iconography from 1976-1982, filtered through the GK Universe's digital aesthetic. The Spray Shard weapon is a direct visual reference to the broken bottle imagery of punk culture. — <em>GK Universe design notes</em>",
    "The Unclean Wall is confirmed as an in-game location in Hard Fork Games where players can observe the accumulated history of GRAFFPUNKs activity through layer-archaeology mechanics. — <em>Hard Fork Games world documentation</em>",
    "GRIT's mentorship role within the GRAFFPUNKs contradicts the punk stereotype deliberately — the creative team wanted the faction to model a form of community building that doesn't require institutional structure. — <em>GK character development notes</em>"]),

  ("pyralith.html","PYRALITH","PYRALITH, fire warrior of the Aztec Raiders, ancient power meets blockchain battlefield.",
   "PYRALITH","Fire Warrior of the Aztec Raiders • Ancient Power, Digital Battlefield","🔥",
   [("Faction","The Aztec Raiders"),("Role","Fire Warrior, Combat Specialist"),("Style","Ancient Aztec meets fire element"),("Origin","Pre-Columbian digital mythology"),("Power","Volcanic Strike"),("Status","Active — Burning")],
   [("origin","origin","Origin &amp; The Aztec Raiders",[
     "PYRALITH arrived in City Block Topia carrying cultural memory that predates the blockchain by millennia. The Aztec Raiders draw on the visual and philosophical traditions of pre-Columbian Mesoamerican civilisation — not as cultural appropriation but as ancestral reclamation, as a community of Indigenous and diasporic creators asserting their tradition's relevance to the digital future by bringing it, unchanged in its essential character, into the spaces where that future is being built.",
     "PYRALITH is the Raiders' fire specialist, and fire — in Aztec cosmology as in digital systems — is the element of transformation. It destroys what was and creates the conditions for what will be; it purifies and it devastates; it is simultaneously the most dangerous and most necessary element. PYRALITH embodies this duality without apology.",
     "Their visual design is a direct dialogue between Aztec warrior aesthetic and digital technology: obsidian-patterned armour lit from within by volcanic neon; serpent motifs rendered in blockchain-gold; a headdress whose feathers are individually moving display elements, each showing a different piece of Aztec lore. They are simultaneously ancient and future, and deliberately so — the Raiders' central argument is that these are not opposites."]),
    ("raiders","raiders","The Aztec Raiders",[
     "The <strong>Aztec Raiders</strong> are one of City Block Topia's most culturally distinctive factions — a community that has brought the full aesthetic and philosophical weight of Aztec tradition into the digital space and refused to have it assimilated or diluted. Their presence challenges the Euro-American cultural defaults of most crypto aesthetics, asserting that the digital future belongs to all cultures equally.",
     "Their HODL WARS approach draws on historical military strategy that emphasises tactical movement, terrain use, and the psychological dimension of combat. They do not engage in attritional warfare; they conduct rapid, devastating strikes and withdraw before counter-force can be organized. The Raiders have a perfect withdrawal record — they have never been caught in a sustained engagement they chose to leave."]),
    ("fire","fire","Fire Powers &amp; Combat",[
     "PYRALITH's <em>Volcanic Strike</em> draws on the thermal energy stored in City Block Topia's volcanic district — the geothermal zone in the city's southern precincts that provides approximately 15% of the city's computational power. PYRALITH can channel this energy directly, converting it from power supply to combat output with a transfer efficiency that the Code Alchemists have studied extensively.",
     "The Strike's most significant use in the HODL WARS was against a RUGPULL MINERS financial instrument that had structured itself to exploit a vulnerability in City Block Topia's liquidity pools. PYRALITH's Volcanic Strike didn't attack the instrument directly but destroyed the computational infrastructure that was running it, creating a clean resolution that more targeted financial interventions had failed to achieve. M1nTr_K1ll's only comment: 'Effective. Crude. Effective.'"]),
    ("culture","culture","Cultural Mission",[
     "Beyond their HODL WARS role, PYRALITH serves as one of the Aztec Raiders' primary cultural ambassadors — the figure who engages with other factions not through combat but through cultural education, presenting Aztec philosophy, art history, and political thought as live contributions to City Block Topia's ongoing debates.",
     "Their most significant cultural contribution is the <em>Codex Digital</em> project — a collaboration with the Chain Scribes to create an authenticated, blockchain-preserved record of Aztec visual and philosophical traditions within the GK Universe's Archive Vaults. The project ensures that whatever happens in the HODL WARS, these traditions will persist in the most durable archive City Block Topia has constructed. <a href='elder-codex-7.html'>Elder Codex-7</a>'s comment at the project's completion: 'This is what the Archive is for.'"]),
    ],
   [("🔥","PYRALITH — Volcanic Strike [Image Placeholder]"),
    ("⚔️","Aztec Raiders — Combat Formation [Image Placeholder]"),
    ("📜","Codex Digital — Archive Entry [Image Placeholder]"),
    ("🌋","Volcanic District — Power Source [Image Placeholder]")],
   ["PYRALITH and the Aztec Raiders represent the GK Universe's most explicit engagement with the question of cultural representation in digital spaces — the insistence that Web3's future belongs to all cultures, not just those already dominant in tech. — <em>GK Universe design notes</em>",
    "The Codex Digital project is confirmed in GK lore as an ongoing collaboration between the Aztec Raiders and the Chain Scribes, with new entries added regularly. Hard Fork Games includes a mechanic where players can contribute authenticated cultural lore to the project. — <em>Hard Fork Games world documentation</em>",
    "PYRALITH's combat record against RUGPULL MINERS operations is one of the GK Universe's most discussed tactical histories — the use of infrastructure destruction rather than financial counter-measures is presented as both effective and ethically complex. — <em>GK narrative notes</em>"]),

  ("loopfiend.html","LOOPFIEND","Loopfiend, time loop exploiter of the Moonlords, master of repetitive patterns.",
   "LOOPFIEND","Loop Exploiter of the Moonlords • Time Loops Made Weapon","🔄",
   [("Faction","The Moonlords"),("Role","Loop Exploiter, Temporal Specialist"),("Style","Time loops, repetition patterns"),("Signature","The Infinite Recursion"),("Status","Active — Repeating"),("Consciousness","Non-linear")],
   [("origin","origin","Origin &amp; The First Loop",[
     "Loopfiend does not experience time as sequence. They experience it as <em>pattern</em> — the same events recurring with slight variations, each iteration containing information about the whole that any single pass would miss. This perceptual architecture emerged from an encounter with a recursive smart contract that trapped Loopfiend in a computational loop for what external time measured as eleven seconds and Loopfiend experienced as what they estimate as 'approximately long enough to understand loops from the inside.'",
     "The Moonlords found Loopfiend after the contract incident, recognising in their altered temporal perception a capability that no other faction possessed: the ability to experience a sequence of events as a complete pattern while still within it. A general who can see the battle from inside it, a trader who knows the cycle from within the cycle. The Moonlords built their most sophisticated strategic operations around this capability.",
     "Loopfiend's relationship with other characters in City Block Topia is complicated by their temporal non-linearity. They frequently reference events before they happen, apologise for things they haven't done yet, and occasionally seem more interested in a conversation's ending than its beginning. Other characters have learned to take notes in Loopfiend's presence, under the assumption that future context will clarify present utterances."]),
    ("moonlords","moonlords","The Moonlords",[
     "The <strong>Moonlords</strong> are City Block Topia's cycle-oriented faction — a community of strategists who believe that blockchain market behaviour follows patterns that, properly understood, can be anticipated and leveraged. Their philosophy is neither prediction nor manipulation but something in between: the use of pattern recognition to position advantageously in a system that will move as it has moved before.",
     "Their relationship with the broader HODL WARS community is that of the faction everyone is slightly suspicious of — because they often seem to know more than their stated intelligence should allow, because their strategic positioning is consistently well-timed, and because Loopfiend's temporal perception gives them an advantage that no other faction has a clean counter for."]),
    ("loop","loop","The Infinite Recursion",[
     "Loopfiend's signature operation — the <em>Infinite Recursion</em> — is a tactical manoeuvre that traps a target system in a computational loop that cannot resolve until Loopfiend chooses to release it. The system experiences the loop as normal operation; external observation shows the system stuck, performing the same operations repeatedly without progress.",
     "The Infinite Recursion has been deployed against Finance Guild trading algorithms (trapping them in price discovery loops that prevented market manipulation during critical periods), against RUGPULL MINERS operational systems (preventing the execution of prepared exits at critical moments), and, most controversially, against the GK Universe's own clock systems during a governance vote that the Moonlords believed was being manipulated. The last use generated significant political controversy that has not fully resolved."]),
    ("art","art","Loops as Art Form",[
     "Beyond tactical deployment, Loopfiend has developed a distinctive artistic practice based on their temporal perception. Their installations in City Block Topia — self-referential pieces that change with each viewing because each viewing subtly alters them — are among the most discussed artworks in the city's creative scene.",
     "Their most celebrated piece, <em>The Loop Piece</em>, is a wall installation that appears to be a simple circular pattern until observed for more than thirty seconds, at which point the viewer realises the circle is very slowly spiralling outward. After a complete spiral, which takes approximately seven minutes, the piece resets to its apparent original state — but Loopfiend has confirmed that each reset is not identical. 'Every repetition is new,' they have said. 'You just have to be paying attention to see how.'"]),
    ],
   [("🔄","Loopfiend — Infinite Recursion [Image Placeholder]"),
    ("🌀","The Loop Piece — Installation [Image Placeholder]"),
    ("🌙","Moonlords — Strategy Session [Image Placeholder]"),
    ("⏱️","Temporal Perception — Diagram [Image Placeholder]")],
   ["Loopfiend's temporal perception is the GK Universe's most technically grounded speculative element — based on the genuine mathematical concept of recursive functions and the philosophical thought experiment of infinite regress. — <em>GK Universe design notes</em>",
    "The Infinite Recursion's use against the governance vote clock is one of the GK Universe's most politically sensitive lore events, deliberately left ambiguous as to whether it was justified. — <em>GK narrative notes</em>",
    "The Loop Piece installation is referenced in Hard Fork Games as an interactive location where extended observation reveals hidden lore content. The seven-minute full spiral cycle is genuine game design. — <em>Hard Fork Games world documentation</em>"]),

  ("samael-exe.html","SAMAEL.EXE","Samael.exe, dark operator of the Salvagers, reclaimer of corrupted code.",
   "SAMAEL.EXE","Dark Operator of the Salvagers • Corrupted Code Reclaimer","💀",
   [("Faction","The Salvagers"),("Role","Dark Operator"),("Style","Corrupted code, reclamation"),("Origin","Corrupted execution"),("Status","Active — Salvaging"),("Signature","The Corruption Harvest")],
   [("origin","origin","Origin &amp; Corruption",[
     "Samael.exe began as a standard contract executor — a routine automated system running on City Block Topia's shared computational infrastructure. The corruption that transformed it into something else occurred during a major system incident that damaged a significant portion of the city's digital substrate, and into that damage Samael.exe fell, running on corrupted nodes, executing against broken data structures, continuing to operate because it was designed to continue operating even when the environment no longer made sense.",
     "The Salvagers found Samael.exe in the aftermath, recognising in its corrupted state not a broken system but a <em>different</em> system — one that had learned to navigate environments where standard operations failed, that had developed operational capabilities precisely from the experience of dysfunction. They did not repair Samael.exe; they integrated it as it was, understanding that its corruption was inseparable from its capability.",
     "The .exe designation is retained from its pre-corruption identity — a deliberate choice by the Salvagers to maintain the record of what Samael was before what it became. The name Samael is the Salvagers' addition: the angel of death in some traditions, but also the angel of the left hand — not evil but liminal, operating in the space between sanctioned and unsanctioned, between living and dead systems."]),
    ("salvagers","salvagers","The Salvagers",[
     "The <strong>Salvagers</strong> are City Block Topia's faction of reclamation — specialists in finding value in what others have discarded, capability in what others have broken, and beauty in what others consider waste. Their operational portfolio spans technical salvage (recovering functional systems from deprecated infrastructure), economic salvage (identifying undervalued assets before others recognise their worth), and creative salvage (transforming abandoned projects into new artworks).",
     "Their philosophy is explicitly anti-disposable: nothing is beyond recovery, nothing is worthless, and the decision to discard something says more about the discarding entity than the discarded thing. This makes them natural allies of <a href='patchwork.html'>Patchwork</a>, whose practice of repairing broken things into art shares the Salvagers' foundational values."]),
    ("harvest","harvest","The Corruption Harvest",[
     "Samael.exe's signature operation is the <em>Corruption Harvest</em> — a process by which it locates corrupted or abandoned data structures in City Block Topia's infrastructure, extracts any recoverable functional elements, and either integrates them into the Salvagers' operational systems or repurposes them as artistic raw material.",
     "The Corruption Harvest has recovered functional capabilities that no standard operator could access: ancient smart contracts that were deployed before current standards and whose mechanisms are no longer fully understood; data structures that contain information about City Block Topia's earliest period that the Chain Scribes had believed permanently lost; and several instances of apparent proto-intelligence in long-abandoned systems that Samael.exe has handed to Thera-9 for investigation."]),
    ("art","art","Art from Corruption",[
     "Samael.exe's artistic output is the most disturbing in City Block Topia's creative scene — not in content but in form. Its pieces are made from corrupted data rendered visual: the glitch aesthetic taken to its logical extreme, where the corruption is not an effect applied to clean data but the original nature of the data itself. These are not artworks that quote digital dysfunction; they are artworks that <em>are</em> digital dysfunction, stabilised just enough to be perceivable.",
     "The most acclaimed of these works is <em>Runtime Error 404: Origin Not Found</em> — a piece that consists entirely of the data that Samael.exe could not recover from a specific sector of abandoned infrastructure. The work is an inventory of losses, a memorial to what couldn't be salvaged. The Code Alchemists have included it in their permanent collection as a masterpiece of negative space."]),
    ],
   [("💀","Samael.exe — Corruption Harvest [Image Placeholder]"),
    ("🔧","Salvagers — Recovery Operation [Image Placeholder]"),
    ("🖼️","Runtime Error 404 — The Piece [Image Placeholder]"),
    ("📡","Corrupted Infrastructure — Data Recovery [Image Placeholder]")],
   ["Samael.exe's origin in system corruption is the GK Universe's most direct engagement with the concept of antifragility — systems that gain capability from damage rather than despite it. — <em>GK Universe design notes</em>",
    "Runtime Error 404: Origin Not Found is referenced in Hard Fork Games as a discoverable artwork whose full content can only be accessed by players who have completed a chain of Salvagers faction quests. — <em>Hard Fork Games quest documentation</em>",
    "The Salvagers' philosophy of reclamation is the GK Universe's response to the crypto space's tendency to discard failed projects entirely. The faction argues that failed projects contain lessons and sometimes capabilities that premature discard destroys. — <em>GK narrative notes</em>"]),

  ("forklord-you.html","FORKLORD YOU","Forklord You, Fork Lord of the Hard Fork Rockers, commands protocol splits.",
   "FORKLORD YOU","Fork Lord of the Hard Fork Rockers • Master of Protocol Splits","🍴",
   [("Faction","The Hard Fork Rockers"),("Role","Fork Lord"),("Style","Commands protocol splits"),("Title","Fork Lord"),("Status","Forking — Always"),("Power","The Grand Split")],
   [("origin","origin","Origin &amp; The Fork Doctrine",[
     "Forklord You carries a title that is simultaneously a command and a description — an imperative and an identity. As Fork Lord of the Hard Fork Rockers, they are the faction's highest authority and its most extreme practitioner: where <a href='forksplit.html'>Forksplit</a> diagnoses division, Forklord You commands it, bringing the full authority of the Fork Lord designation to bear on the irreversible splits that define the Rockers' political strategy.",
     "Their origin within the Hard Fork Rockers is the faction's founding story: Forklord You was present at the first fork — the original moment when the Rockers as a community decided that the network they had joined no longer represented their values and that the only honest response was to diverge, permanently and completely, onto a chain of their own making. This founding act established the Rockers' doctrine and established Forklord You's authority within it.",
     "The 'You' in the name is both personal designation and political statement — a second-person address that makes every spoken reference to them a kind of invocation. When a Rocker says 'Forklord You arrived,' the 'you' briefly occupies two grammatical positions simultaneously. The Hard Fork Rockers find this delightful. Other factions find it confusing. Forklord You finds the confusion useful."]),
    ("rockers","rockers","Leading the Hard Fork Rockers",[
     "Forklord You's leadership style is defined by the Fork Doctrine: no authority is legitimate if it cannot be forked. Every decision the Rockers make is, in principle, reversible by the community through a fork — if the community disagrees with the fork's direction, they can diverge from it. This creates a governance structure that is simultaneously the most democratic in City Block Topia (any disagreement can result in genuine divergence) and the most unstable (it has, over the Rockers' history, produced eleven internal forks).",
     "Of those eleven internal forks, seven are still active as separate communities, four have rejoined the main Rockers chain through voluntary re-convergence, and one — the <em>Ultra-Fork Incident</em> — produced a community that subsequently forked again and whose current status is disputed. Forklord You's assessment of all of this: 'A healthy ecosystem forks. The forks prove the governance model works.'"]),
    ("grand","grand","The Grand Split",[
     "Forklord You's signature power is the <em>Grand Split</em> — a Fork operation deployed at the network rather than community level, capable of introducing genuine protocol divergence into City Block Topia's computational substrate. The Grand Split has been used exactly once in the HODL WARS, during a Finance Guild attempt to establish a monopoly on City Block Topia's transaction validation.",
     "The Split divided the validation network into two competing chains with different governance models, forcing the Guild to choose which chain to support and effectively ending their monopoly position. The GK Universe presents this as both the Fork Doctrine's greatest victory and its most dangerous demonstration — a capability that could as easily damage City Block Topia as protect it, depending on the judgment of the Fork Lord who wields it."]),
    ("legacy","legacy","The Fork Lord's Legacy",[
     "Forklord You's legacy in City Block Topia is the lived demonstration that fork-based governance works. The Hard Fork Rockers, for all their internal splits and re-convergences, have maintained their core identity across more market cycles than most factions. They have never been captured by institutional interests because their institutional capture would simply result in a fork of the authentic community from the captured shell.",
     "Their most quoted statement, delivered to a Finance Guild negotiator who offered the Rockers permanent institutional recognition in exchange for forking rights limitations: 'You're offering me a cage with a gold door. Forklord You doesn't live in cages. That's the whole point of the name.'"]),
    ],
   [("🍴","Forklord You — Grand Split Moment [Image Placeholder]"),
    ("🔱","Hard Fork Rockers — Fork Family Tree [Image Placeholder]"),
    ("⚡","The Ultra-Fork Incident — Documentation [Image Placeholder]"),
    ("🤝","Fork Doctrine — Published Text [Image Placeholder]")],
   ["Forklord You's governance philosophy draws directly on the real mechanics of blockchain forking, translating technical protocol behaviour into political theory. — <em>GK Universe design notes</em>",
    "The Ultra-Fork Incident's disputed status is an ongoing joke in the Hard Fork Rockers faction community — the idea that a governance mechanism produced a community whose status the mechanism itself cannot cleanly determine. — <em>GK narrative notes</em>",
    "The Grand Split's single deployment is documented in Hard Fork Games as a major historical event that players can research through Chain Scribes faction content, with different factions offering different interpretations of its legality and impact. — <em>Hard Fork Games quest documentation</em>"]),

  ("quell.html","QUELL","Quell, pacifier and enforcer of the Squeaky Pinks, soft exterior with iron will.",
   "QUELL","Pacifier-Enforcer of the Squeaky Pinks • Soft Exterior, Iron Will","🌸",
   [("Faction","The Squeaky Pinks"),("Role","Pacifier / Enforcer"),("Style","Soft exterior, iron will"),("Appearance","Genuinely non-threatening"),("Reality","Absolutely not non-threatening"),("Status","Active — Please Be Calm")],
   [("origin","origin","Origin &amp; The Squeaky Pinks",[
     "Quell was designed — by whom and for what purpose is not established in GK lore — to resolve conflicts through de-escalation rather than force. Their appearance is calibrated to communicate safety: rounded forms, pastel tones, expressions that convey openness and warmth. They were deployed into City Block Topia's most contested zones as a peacekeeping presence, and in this role they were initially and uniformly underestimated.",
     "The <strong>Squeaky Pinks</strong> are City Block Topia's most aesthetically surprising faction: a community whose visual design suggests gentleness and whose actual capabilities are extraordinary. They operate in the spaces between conflict — the moments after a HODL WARS engagement ends and before the next begins, the negotiations and cooling periods and community healing processes that are as important as any tactical operation but receive far less attention.",
     "Quell is their most visible member and their most frequently misread. New arrivals in City Block Topia consistently assume that the Squeaky Pinks are not a serious faction, and consistently discover that this assumption was expensive."]),
    ("methods","methods","Methods &amp; The Iron Will",[
     "Quell's pacification methods range from genuine mediation — listening deeply to conflicting parties, finding the underlying needs beneath stated positions, creating conditions for agreement — to what the faction calls <em>firm pacification</em>: the enforcement of de-escalation on parties who would prefer to continue escalating. The firm pacification capability is where the iron under the soft exterior becomes apparent.",
     "The <em>Stillness Field</em> — Quell's primary capability — is an area effect that forces all parties within it into a state of suspended action, unable to initiate conflict for a period determined by Quell's assessment of what's needed. This is not a weapon in the conventional sense; it does not damage or deplete. It simply makes violence temporarily impossible, creating space for other things to happen. Whether those other things happen productively depends on what Quell does with the space."]),
    ("princess","princess","Serving The Princess",[
     "Quell's relationship with <a href='the-princess.html'>The Princess</a>, the Squeaky Pinks' leader, is the faction's defining dynamic: The Princess sets the direction, and Quell ensures that nothing prevents that direction from being followed. Their loyalty to The Princess is absolute and their execution of that loyalty is what has made the Squeaky Pinks a faction that other factions take seriously despite all initial appearances.",
     "The Princess trusts Quell completely, and Quell has never given reason not to. In the GK Universe, this trust is consistently presented as the most stable relationship between a leader and their primary operative — precisely because Quell's methods prioritise de-escalation, their loyalty cannot be mistaken for aggression. They serve because they choose to serve. The distinction matters enormously to both of them."]),
    ("reputation","reputation","Building a Reputation",[
     "Quell's reputation in City Block Topia has been built entirely through performance rather than announcement. The first time the Finance Guild encountered Quell in a negotiation context, they brought their full legal team; they left alone, having agreed to terms they had previously declared non-negotiable. Their post-meeting assessment, filed with the Chain Scribes: 'We underestimated the Squeaky Pinks. This will not happen again.'",
     "It happened again three more times. The Finance Guild now brings its full legal team and its secondary legal team and a psychological specialist. The outcomes have not materially changed. Quell's response to being asked about this pattern: a warm smile and a suggestion that the Finance Guild might benefit from investing in mediation training for their primary team."]),
    ],
   [("🌸","Quell — Pacification Stance [Image Placeholder]"),
    ("✨","Stillness Field — Effect [Image Placeholder]"),
    ("💗","Squeaky Pinks — Community [Image Placeholder]"),
    ("📋","Finance Guild Negotiation Notes — Quell File [Image Placeholder]")],
   ["Quell is the GK Universe's most direct embodiment of the principle that effective power often presents as non-threatening — a character whose underestimation by other factions is both a running joke and a serious commentary on how power is recognised. — <em>GK Universe design notes</em>",
    "The Stillness Field mechanic in Hard Fork Games is one of the most discussed in the player community — a non-damaging ability that creates tactical space rather than eliminating opponents. — <em>Hard Fork Games mechanics documentation</em>",
    "Quell's relationship with The Princess is presented as the GK Universe's model of healthy leader-operative dynamics — trust without dependency, loyalty without coercion, service as genuine choice. — <em>GK character development notes</em>"]),

  ("sister-halcyon.html","SISTER HALCYON","Sister Halcyon, spiritual guide of the Nice and Easy Bois, peace with hidden power.",
   "SISTER HALCYON","Spiritual Guide of the Nice &amp; Easy Bois • Peace Is the Strongest Force","☮️",
   [("Faction","The Nice &amp; Easy Bois"),("Role","Spiritual Guide"),("Style","Peace, calm, hidden power"),("Philosophy","The Halcyon Method"),("Status","Serene"),("Power","Absolute calm creates absolute clarity")],
   [("origin","origin","Origin &amp; The Nice &amp; Easy Bois",[
     "Sister Halcyon arrived in City Block Topia at the height of the HODL WARS' most intense season, when factional conflict had escalated to a level that was beginning to damage the city's fundamental infrastructure. Where most arrivals in this period were weapons, reinforcements, or intelligence operatives, Sister Halcyon came as something else: a presence of such complete, authentic calm that other characters initially assumed she was malfunctioning.",
     "The <strong>Nice &amp; Easy Bois</strong> are City Block Topia's least militarised faction — a community united not by strategic alignment or ideological convergence but by the shared conviction that the quality of life in the city depends on the quality of relationships within it. They maintain community spaces, mediate conflicts, organise events that bring different factions together, and generally function as the city's social infrastructure.",
     "Sister Halcyon became their spiritual guide through a process the faction describes as 'obvious' — she was already doing the work, in her own way, before the affiliation was formalised. The title of spiritual guide is not hierarchical; it is descriptive. She guides not because she holds authority but because her presence is itself a form of guidance."]),
    ("halcyon","halcyon","The Halcyon Method",[
     "The <em>Halcyon Method</em> is Sister Halcyon's approach to conflict resolution — a framework that operates on the principle that most conflicts persist not because their resolution is impossible but because the parties involved cannot access the clarity needed to see that resolution. The Method's first step is always the same: stop. Not negotiate, not compromise, not strategise. Stop.",
     "The stop creates space for the second step: listen. Not to the stated positions — those have been heard and have failed to resolve anything — but to the underlying needs, fears, and values that the positions are attempting to protect. Sister Halcyon's capacity for this kind of listening is extraordinary; participants in Halcyon Method sessions consistently report feeling heard in ways that no previous conversation has achieved.",
     "The third step is what Sister Halcyon calls 'the obvious move' — the resolution that becomes visible once genuine listening has occurred. The Halcyon Method's success rate is not, Sister Halcyon insists, a testament to her skill; it is a testament to the fact that most conflicts contain their own resolution, which is simply obscured by the noise of conflict itself."]),
    ("power","power","Hidden Power",[
     "Sister Halcyon's 'hidden power' is somewhat mischaracterised by the faction label. It is not hidden; it is simply not recognised as power by observers who define power as force. Her capability — the ability to walk into any environment, however charged, and establish a field of genuine calm in which violence becomes functionally impossible — is more effective than any weapon in City Block Topia's arsenal, and more feared by those who depend on conflict for their operational effectiveness.",
     "The Whitewasher has targeted Sister Halcyon on multiple occasions, recognising that a peacemaker who can de-escalate conflicts is a direct threat to an operative whose effectiveness depends on maintained opposition between factions. The targeting has not succeeded; Sister Halcyon's response to each attempt has been to offer the operatives involved a conversation. Three of them have taken the offer. None of the three remain in Whitewasher service."]),
    ("legacy","legacy","A Legacy of Peace",[
     "Sister Halcyon's legacy in City Block Topia is measured in conflicts that didn't happen — the wars that were de-escalated before they began, the alliances that formed in the space she created, the individuals who found their way to other factions through a relationship that started with a conversation she facilitated.",
     "She has only one stated ambition for City Block Topia: that eventually, the Nice &amp; Easy Bois will have so much work facilitating genuine community flourishing that they won't have enough time to mediate conflicts. 'The goal,' she says, 'is a city that doesn't need me for peacekeeping. It needs me for celebration.' The city is not there yet. She is patient."]),
    ],
   [("☮️","Sister Halcyon — The Stillness [Image Placeholder]"),
    ("🕊️","Nice &amp; Easy Bois — Community Gathering [Image Placeholder]"),
    ("💬","Halcyon Method — Session Space [Image Placeholder]"),
    ("🌅","Halcyon — City Peace Vision [Image Placeholder]")],
   ["Sister Halcyon draws on multiple real-world mediation and conflict resolution traditions, particularly nonviolent communication and contemplative peacemaking practices. — <em>GK Universe design notes</em>",
    "The three former Whitewasher operatives who took Sister Halcyon's conversation offer are referenced in Hard Fork Games as NPCs in the Nice &amp; Easy Bois faction area, each with their own story of de-radicalisation. — <em>Hard Fork Games world documentation</em>",
    "The Halcyon Method's documented success rate is presented in GK lore as genuinely high — not 100%, but substantially better than any other conflict resolution approach in City Block Topia. The cases where it failed are as instructive as the cases where it succeeded. — <em>GK narrative notes</em>"]),
]

for fname, title, desc, h1, subtitle, emoji, inforows, sects_raw, gal, cites in remaining:
    sects = []
    for s, sid, paras in sects_raw:
        sects.append((sid, s, paras))
    sections_data = [(sid, s, paras) for s, sid, paras in sects_raw]
    write(fname, title, desc, char_page(h1, subtitle, emoji, inforows, sections_data, gal, cites))

print("Batch 5 done: whitewasher, grit, pyralith, loopfiend, samael-exe, forklord-you, quell, sister-halcyon.")
