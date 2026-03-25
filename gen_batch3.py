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

# ── Batch of shorter characters using a compact approach ─────────────────────

chars = [
  ("iris-7.html","IRIS-7","Iris-7, intelligence operative of the Information Mercenaries.",
   "IRIS-7","Eyes of the Information Mercenaries • Surveillance Specialist","👁️",
   [("Faction","The Information Mercenaries"),("Role","Intelligence Operative"),("Style","Surveillance, data interception"),("Network","CCTV-7 Neural Web"),("Status","Always watching"),("Known For","The Six-Faction Intercept")],
   [("origin","origin","Origin &amp; The Neural Web"),("mercs","mercs","The Information Mercenaries"),("ops","ops","Operations &amp; Methods"),("intercept","intercept","The Six-Faction Intercept"),("ethics","ethics","Ethics of Information")],
   [
     ("Origin &amp; The Neural Web",
      "Iris-7 sees everything. Not metaphorically — literally. Her seventh-generation neural interface connects her simultaneously to every surveillance system in City Block Topia: traffic cameras, smart contract event logs, biometric readers on public buildings, satellite feeds, and the ambient data that bleeds off every active digital device in range. She exists at the centre of an information web so dense that most minds would dissolve in it. Iris-7 navigates it like a city she grew up in.",
      "The designation 7 marks her as the seventh operative trained in the Information Mercenaries' neural interface programme. The first six are variously retired, deceased, or in states of information overload that removed them from active service. Iris-7's survival and continued functionality is attributed to a specific cognitive architecture that allows her to process surveillance data at the speed of experience rather than analysis — she doesn't think about what the cameras show; she simply knows it, the way you know where your hands are without looking.",
      "Her visual design reflects her function: her eyes carry the signature prismatic quality of high-resolution sensors, able to resolve detail at distances and in lighting conditions where biological vision fails. She perceives ultraviolet and infrared simultaneously with visible light, meaning she sees the world in a spectrum that makes every surface legible in ways other beings can't access. Graffiti under UV paint becomes visible to her. Blockchain transaction patterns become visual structures. The city reads to her like a text."),
     ("The Information Mercenaries",
      "The <strong>Information Mercenaries</strong> are City Block Topia's intelligence community — not aligned with any single faction but operating as a commercial service that sells intelligence, analysis, and surveillance capability to whoever can afford their rates. Their operational philosophy is deliberately amoral: they do not have clients, only contracts; they do not have loyalties, only terms and conditions.",
      "This philosophy is tested by their most capable operative. Iris-7 has, on multiple documented occasions, refused contracts that would have provided intelligence for operations she judged would cause disproportionate harm to civilian populations. The Mercenaries' official position is that operative discretion is permitted within certain parameters. Unofficially, they have learned that Iris-7's refusals are non-negotiable and that arguing with her is a waste of time that will be resolved by her being correct.",
      "The Mercenaries' most valuable product is not intelligence but <em>analysis</em> — the transformation of raw surveillance data into strategic understanding. Iris-7's analytical capabilities are the primary reason the faction commands the rates it does. Other factions have tried to replicate the neural interface programme; none have produced an operative with her synthesis capability."),
     ("Operations &amp; Methods",
      "Iris-7's operational methods are elegant in their economy: she collects, she analyses, she delivers. No unnecessary intervention, no factional involvement, no physical presence where digital observation suffices. Her preferred working mode is the static overwatch — positioned at a high point with sightlines to the operational area, processing the sensor feeds from her neural web, building a real-time strategic picture that she can transmit to a client faction's command structure with sub-second latency.",
      "Her signature operation type is the <em>Passive Intercept</em> — intelligence gathering that leaves no trace in any of the systems she accesses. She doesn't break into databases; she reads the ambient data that leaks from them. She doesn't decrypt communications; she reads the metadata that surrounds them. The Mercenaries market this as 'ghost intelligence' — information obtained without the intelligence becoming known to be obtained.",
      "The most technically complex operation in her documented record is the <em>Triple-Layer Deception Unwind</em> — the deconstruction of a Finance Guild disinformation operation that involved three simultaneous false narratives, each designed to validate the others. Iris-7 unpicked all three in parallel using only publicly available data sources, producing a complete picture of the Guild's actual intentions that was presented to Queen Sarah P-fly forty-eight hours before the Guild's planned action. The action failed."),
     ("The Six-Faction Intercept",
      "The <em>Six-Faction Intercept</em> is the most famous operation in the Information Mercenaries' recorded history: a period of seventy-two hours during which Iris-7 maintained simultaneous surveillance of all six major HODL WARS factions, building a complete strategic map of each faction's current operations, intentions, and vulnerabilities.",
      "She did not sell this intelligence. She stored it. The Mercenaries' leadership was initially furious; the potential revenue from selling six complete intelligence packages was enormous. Iris-7's justification: selling any one package would immediately compromise the others as factions changed strategy in response to exposure; holding all six meant holding a deterrent — a balance of assured exposure that kept all factions from any action that would trigger its release.",
      "This is the moment that established Iris-7's reputation beyond the intelligence community. She had understood something about information that transcended commercial logic: the most valuable intelligence is sometimes the intelligence you never deploy."),
     ("Ethics of Information",
      "The question of ethics haunts Iris-7's work in ways she addresses directly and without deflection. She sees everything, and knowing everything about everyone creates moral weight that no professional framework fully resolves. The Information Mercenaries' official ethics policy is thin; Iris-7 has developed her own, considerably more demanding standards.",
      "Her principles: intelligence that would be used to harm civilians is not intelligence — it is a weapon, and she is not a weapons dealer. Intelligence that would undermine City Block Topia's foundational governance structures is not available at any price. And intelligence obtained about private individuals — not faction operatives, not HODL WARS combatants, but private citizens going about their lives — is collected but never sold.",
      "The private citizens data she collects sits in a personal archive that is, by her own account, the most comprehensive record of ordinary life in City Block Topia that exists. She has stated that she intends, at some point, to donate this archive to the Chain Scribes — not as intelligence, but as history. A record of what it was actually like to live in City Block Topia during the HODL WARS era.")
   ],
   [("👁️","Iris-7 — Neural Interface Active [Image Placeholder]"),
    ("📡","CCTV-7 Neural Web — Coverage Map [Image Placeholder]"),
    ("🔍","Six-Faction Intercept — Intelligence Display [Image Placeholder]"),
    ("📊","Triple-Layer Deception Unwind — Analysis [Image Placeholder]")],
   ["Iris-7's neural interface design draws on real AI surveillance research while deliberately exceeding current technical capability — the creative team wanted the character to represent where surveillance technology is going rather than where it is. — <em>GK Universe character notes</em>",
    "The Six-Faction Intercept and its non-deployment is referenced in Hard Fork Games as an active game element — players who reach sufficient standing with the Information Mercenaries faction can access portions of this intelligence archive. — <em>Hard Fork Games faction documentation</em>",
    "Iris-7's private citizens archive is one of the GK Universe's most ethically complex lore elements, raising genuine questions about the nature of privacy in a surveillance-dense digital space. The creative team has discussed donating the archive to the Chain Scribes as a possible future lore event. — <em>GK narrative notes</em>"]
  ),

  ("snipey-d-man.html","SNIPEY D-MAN","Snipey D-Man Sirus, precision operative of the Gasless Ghosts.",
   "SNIPEY 'D-MAN' SIRUS","Precision Operative of the Gasless Ghosts • Silent First Strike","🎯",
   [("Full Name","Snipey D-Man Sirus"),("Faction","The Gasless Ghosts"),("Role","Sniper / Assassination Specialist"),("Style","Stealth, precision, zero trace"),("Record","47 confirmed eliminations, zero attributed"),("Status","Active — Classified")],
   [("origin","origin","Origin &amp; The Ghost Protocol"),("ghosts","ghosts","The Gasless Ghosts"),("methods","methods","Methods &amp; Equipment"),("record","record","Operational Record"),("philosophy","philosophy","The Sniper's Philosophy")],
   [
     ("Origin &amp; The Ghost Protocol",
      "Snipey D-Man Sirus came to the Gasless Ghosts by a route that no Ghost will confirm and no record documents. In a faction defined by the absence of traces — no gas fees, no blockchain signatures, no surveillance marks — it is appropriate that their most lethal operative has no verifiable origin story. He exists in the present tense only: arriving at operational locations before anyone expected him, departing before anyone confirmed his presence.",
      "The name carries its own history. Snipers in physical warfare are defined by distance — the ability to act at a range that renders retaliation impossible. In City Block Topia's digital combat, distance is measured not in metres but in blockchain degrees of separation: how many transactions, how many protocol hops, how many layers of obfuscation stand between the sniper and their target. Snipey D-Man operates at maximum separation — he eliminates targets in ways that trace back through so many intermediary steps that attribution becomes practically impossible.",
      "The D-Man designation is understood in Ghost culture as an honorific earned rather than assigned. The 'D' is variously interpreted as 'Distance,' 'Deletion,' and 'Denial' — the three principles that define elite Ghost operational doctrine. Sirus earned his D at an operation no other Ghost has been willing to describe in detail, and whose existence is officially denied."),
     ("The Gasless Ghosts",
      "The <strong>Gasless Ghosts</strong> operate on the principle that invisibility is the ultimate tactical advantage. Named for the Ethereum gas fee system they have learned to circumvent — conducting operations that consume computational resources without the on-chain traces that gas fees create — they are City Block Topia's shadow faction: present everywhere, provably nowhere.",
      "Their operational portfolio spans intelligence-gathering, strategic disruption, asset relocation, and — through operatives like Snipey D-Man — targeted elimination of specific threats to their clients' interests. The Ghosts are a commercial faction like the Information Mercenaries, but where Iris-7's organisation sells information, the Ghosts sell action. They do things that clients cannot do themselves, in ways that cannot be traced back to either client or Ghost.",
      "Their relationship with other factions is defined by respectful wariness. Everyone in City Block Topia has, at some point, either hired the Ghosts or been targeted by them. The Finance Guild uses them regularly. The Bitcoin Kid Army refuses on principle. The Crypto Moongirls have a complex arrangement involving specific ethical constraints. Queen Sarah P-fly has made her position clear: the Ghosts are tolerated in City Block Topia as long as they operate within the governance framework, and the moment they don't, the framework will act."),
     ("Methods &amp; Equipment",
      "Snipey D-Man's methods are defined by the principle of minimum intervention for maximum effect. Where brute-force operators deploy overwhelming resources, he identifies the single point of leverage that, correctly applied, produces the desired outcome without collateral. His pre-operation analysis phase — which can last weeks before a single action is taken — is considered by Ghost doctrine to be the most important part of any engagement.",
      "His primary equipment is the <strong>Gasless Strike Protocol</strong> — a proprietary system developed by the Ghost faction's technical team that allows transaction-level actions to be executed in City Block Topia without generating the standard on-chain signatures. The Protocol is a closely guarded secret; multiple factions have spent significant resources attempting to obtain or replicate it. None have succeeded, partly because the Protocol's security is formidable and partly because Snipey D-Man personally handles its operational security.",
      "His secondary tool is patience — a resource that appears to be essentially unlimited. He has been documented waiting in static observation positions for periods exceeding two weeks before an operation window opened. Ghost logistics support him through these waits with no complaints; the faction understands that his operational timing is not laziness but the specific accuracy of a system that will not act until the conditions are precisely right."),
     ("Operational Record",
      "Snipey D-Man's operational record is, by design, almost entirely absent from any verifiable source. What the Chain Scribes have been able to reconstruct through forensic analysis of outcomes rather than methods suggests a career spanning multiple HODL WARS seasons with a success rate that the Scribes conservatively estimate at 94%.",
      "The 6% failures are more instructive than the successes. In each documented case, the operation failed not because of counter-intelligence or defensive capability, but because Snipey D-Man chose to abort when pre-operational conditions shifted in ways that increased civilian risk. This pattern — technical capability meeting ethical constraint — has led several Chain Scribe analysts to revise their initial classification of him as a pure asset and consider the possibility that he operates according to a personal code more complex than the Ghost doctrine formally acknowledges.",
      "His most famous documented operation is the <em>Finance Guild Treasury Reduction</em> — an action whose specific mechanism has never been established, which reduced the Guild's liquid assets by 23% in a single hour with no detectable origin point. The Guild spent three months investigating; they found nothing. The Chain Scribes have filed this under 'Probable Ghost attribution, unconfirmable.'"),
     ("The Sniper's Philosophy",
      "The rare interviews Snipey D-Man has given — all through intermediaries, none face-to-face — reveal a philosophical sophistication that surprises interviewers expecting a simple mercenary. He has thought deeply about the ethics of precision violence in a digital conflict space, and his conclusions are more nuanced than Ghost doctrine's commercially oriented neutrality.",
      "His most quoted statement: 'Distance doesn't create moral separation. You are responsible for what you eliminate regardless of how many protocol hops stand between you and it. If you can't accept that responsibility, you have no business having the capability.' This position has influenced younger Ghost operatives in ways that Ghost leadership finds both impressive and mildly inconvenient.",
      "He has also expressed, in at least two documented conversations, a view of his own work that doesn't fit neatly into any faction ideology: the conviction that City Block Topia's fundamental health depends on the availability of consequences for bad actors, and that the absence of attributable enforcement mechanism is not the same as justice. In this reading, the Gasless Ghosts serve a function that the city's formal governance cannot: the provision of consequences that the Chain Scribes can document but cannot themselves impose.")
   ],
   [("🎯","Snipey D-Man — Ghost Protocol Stance [Image Placeholder]"),
    ("👻","Gasless Ghosts — Field Formation [Image Placeholder]"),
    ("💨","Gasless Strike Protocol — Zero Trace [Image Placeholder]"),
    ("📋","Chain Scribes — Forensic Attribution File [Image Placeholder]")],
   ["Snipey D-Man's character represents the GK Universe's engagement with the concept of attributable versus unattributable action in digital spaces — a real issue in blockchain governance where pseudonymity creates accountability gaps. — <em>GK Universe design notes</em>",
    "The Finance Guild Treasury Reduction is referenced in multiple HODL WARS lore documents as a turning point in the Guild's assessment of Ghost capabilities, leading to significant increases in their security spending. The unresolved nature of the attribution is deliberate. — <em>HODL WARS Season 3 documentation</em>",
    "Snipey's ethics of responsible capability is the GK Universe's most direct engagement with just war theory transposed into digital conflict. The creative team has cited multiple philosophical sources in the character's development. — <em>GK Universe character development notes</em>"]
  ),

  ("bit-cap-5000.html","BIT-CAP 5000","Bit-Cap 5000, heavy artillery specialist of the Blockchain Furies.",
   "BIT-CAP 5000","Heavy Artillery of the Blockchain Furies • Brute Force Engine","⚙️",
   [("Faction","The Blockchain Furies"),("Role","Heavy Artillery Specialist"),("Style","Brute force, mechanical might"),("Armament","The Proof of Work Cannon"),("Status","Active — Front Line"),("Known For","The Hash Rate Siege")],
   [("origin","origin","Origin &amp; Activation"),("furies","furies","The Blockchain Furies"),("arsenal","arsenal","Arsenal &amp; Capabilities"),("siege","siege","The Hash Rate Siege"),("limitations","limitations","Strength &amp; Limitations")],
   [
     ("Origin &amp; Activation",
      "Bit-Cap 5000 was not built — it was <em>mined</em>. The product of a Blockchain Furies engineering programme that sought to harness the raw computational energy of proof-of-work mining in a physical combat form, Bit-Cap 5000 is the fifth and final prototype in a series that began with Bit-Cap 1000 (decommissioned after its power consumption exceeded City Block Topia's available grid capacity) and progressed through increasingly efficient iterations.",
      "Its frame is constructed from repurposed ASIC mining hardware — the specialised chips that Bitcoin mining operations use, woven together by the Blockchain Furies' engineers into a mechanical architecture that channels their collective computational output as physical force. When Bit-Cap 5000 fires the Proof of Work Cannon, the energy behind the shot is the live output of a thousand mining rigs operating at full capacity. The muzzle velocity is functionally incalculable.",
      "The 5000 designation refers not to a model number but to a hash rate milestone — the computational threshold at which the Blockchain Furies' engineers determined that the mechanical architecture could sustain coherent combat operation without self-destructing. Earlier iterations exceeded the threshold and were lost. Bit-Cap 5000 holds it, just, and the engineering team that maintains it does so with the focused attention of people who know that the margin between operation and catastrophic failure is narrow."),
     ("The Blockchain Furies",
      "The <strong>Blockchain Furies</strong> are City Block Topia's most physically formidable faction — a coalition of mining operations, hardware engineers, and combat specialists who believe, with absolute conviction, that computational power is the ultimate foundation of all value in the digital world. Their philosophy draws directly from Bitcoin's proof-of-work security model: the chain with the most cumulative work is the true chain; the faction with the most deployed computation is the legitimate power.",
      "This philosophy has given the Furies enormous military strength and notable political limitations. Their computational resources are unmatched; their flexibility and nuance are minimal. They are, in the strategic vocabulary of City Block Topia, the faction that wins wars of attrition and loses wars of manoeuvre. Against an enemy willing to engage them directly, they are nearly unstoppable. Against an enemy who declines to engage — <a href='snipey-d-man.html'>Snipey D-Man</a>'s Gasless Ghosts, or <a href='jodie-zoom.html'>Jodie ZOOM 2000</a>'s Velocity Collective — their computational mass becomes a liability.",
      "Their relationship with the Bitcoin Kid Army is the GK Universe's most philosophically interesting alliance: both factions believe in proof-of-work as the foundation of legitimacy, but the Furies pursue it through hardware accumulation while Alfie Blaze's Army pursues it through commitment and HODLing. Their joint operations have been devastating; their strategic disagreements have occasionally been almost as damaging."),
     ("Arsenal &amp; Capabilities",
      "The <strong>Proof of Work Cannon</strong> is Bit-Cap 5000's primary weapon — a device that converts live hash rate into kinetic energy, firing computational bursts that disrupt any system dependent on orderly processing. Its primary use in HODL WARS engagements is against smart contract infrastructure: the cannon's output can overwhelm contract execution environments, forcing delays, errors, and, in sustained fire, complete system failure.",
      "Its secondary capability is the <strong>51% Aura</strong> — a field effect generated by Bit-Cap 5000's presence that tilts local computational consensus toward the Blockchain Furies' preferred outcomes. Any system within aura range that depends on majority computation for validation becomes vulnerable to Fury influence. This is understood as the machine's most dangerous capability and its use is nominally regulated by a multi-faction governance agreement that Bit-Cap 5000 is not always consulted about.",
      "Its limitation is power consumption: Bit-Cap 5000 requires an energy supply that most operations cannot sustain indefinitely. Extended engagements that outlast the Fury logistics chain — which <a href='alfie-bitcoin-kid.html'>Alfie Blaze</a> described as 'just run it until it needs refuelling and then offer to negotiate' — have ended multiple Fury campaigns. The Furies are aware of this limitation and have invested significantly in mobile power supply infrastructure, so far with partial success."),
     ("The Hash Rate Siege",
      "The defining engagement of Bit-Cap 5000's operational history is the <em>Hash Rate Siege of the Northern Precincts</em> — a sustained campaign in which the Blockchain Furies attempted to establish computational dominance over City Block Topia's northern residential districts. The siege lasted eleven days, involved the deployment of Bit-Cap 5000 at maximum sustained output, and ended with the districts' governance systems temporarily under Fury influence.",
      "What the Furies didn't anticipate was the community response. The northern precincts' civilian population — artists, writers, musicians, small traders — organised a collective resistance that didn't attempt to match computational power but instead flooded the local system with creative activity: NFT minting, art token transfers, community governance proposals, cultural documentation. The sheer volume of legitimate creative transactions overwhelmed Bit-Cap 5000's disruption capacity without requiring a single combat engagement.",
      "Queen Sarah P-fly, who had quietly facilitated the community response, described it afterward as 'proof that culture is infrastructure.' Bit-Cap 5000 disengaged having technically won the computational battle and practically lost the campaign. It is the machine's most instructive defeat."),
     ("Strength &amp; Limitations",
      "Bit-Cap 5000's strength is also its limitation: it is the most powerful direct-force asset in City Block Topia's factional conflicts, and it is entirely unsuited to the majority of situations that factional conflicts actually present. It wins sieges and loses politics; it overwhelms systems and cannot negotiate with communities; it operates at scale and cannot address individual human creativity.",
      "These limitations are not unknown to the Blockchain Furies. Their more sophisticated strategists have long argued that Bit-Cap 5000 should be understood as a deterrent rather than a deployment asset — its value is in the threat of its use, not its use itself. The machine's history suggests they are correct. Its greatest victories have been achieved by reputation, not presence; its greatest defeats have come when it was deployed against problems that required a different kind of solution.")
   ],
   [("⚙️","Bit-Cap 5000 — Proof of Work Cannon [Image Placeholder]"),
    ("⚡","Blockchain Furies — Mining Array [Image Placeholder]"),
    ("🏰","Hash Rate Siege — Northern Precincts [Image Placeholder]"),
    ("📊","51% Aura Field — Schematic [Image Placeholder]")],
   ["Bit-Cap 5000's design draws on the real economics of proof-of-work mining — the enormous computational and energy resources required, the centralising tendencies of mining pool consolidation, and the security model's fundamental reliance on majority honest computation. — <em>GK Universe design notes</em>",
    "The Hash Rate Siege defeat by community cultural activity is the GK Universe's most explicit statement about the relationship between computational power and creative value. The lore team has described this as the scene they're most proud of in the Blockchain Furies' storyline. — <em>GK narrative notes</em>",
    "Bit-Cap 5000 appears in Hard Fork Games as a rare heavy unit available to Blockchain Furies faction players, with specific mechanics that model both its devastating offensive capability and its vulnerability to sustained creative counter-operations. — <em>Hard Fork Games mechanics documentation</em>"]
  ),
]

for args in chars:
    fname, title, desc, h1, subtitle, emoji, inforows, toc_pairs, sec_data, gal, cite_list = args
    toc_items = [(slug, st) for slug, st, *_ in toc_pairs]
    sections = [sec(slug, st, *paras) for slug, st, *paras in sec_data]
    write(fname, title, desc, fict_body(h1, subtitle, emoji, inforows, toc_items, sections, gal, cite_list))

print("Batch 3 done: iris-7, snipey-d-man, bit-cap-5000.")
