import os

CHARS_DIR = "/home/runner/work/graffiti-kings/graffiti-kings/characters"

SIDEBAR_REAL = """
            <a href="darren-cullen.html">👑 Darren Cullen</a>
            <a href="sarah-pu51fly.html">�� Sarah PU51FLY</a>
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

def page(title, description, body_html):
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
        f.write(page(title, description, body))
    print(f"Written: {filename}")

# ─────────────────────────────────────────────
# DARREN CULLEN
# ─────────────────────────────────────────────
darren_body = """
        <h1 class="page-title">DARREN CULLEN (SER)</h1>
        <p class="page-subtitle">Founder of Graffiti Kings • London, 1983–Present</p>

        <div class="infobox">
          <div class="infobox-title">DARREN CULLEN (SER)</div>
          <div class="infobox-image" style="background:linear-gradient(135deg,#1a1a2e,#16213e);display:flex;align-items:center;justify-content:center;height:200px;font-size:5rem;">👑</div>
          <table>
            <tr><td>Known As</td><td>SER</td></tr>
            <tr><td>Role</td><td>Founder, Lead Artist</td></tr>
            <tr><td>Born</td><td>London, UK</td></tr>
            <tr><td>Active Since</td><td>1983</td></tr>
            <tr><td>Crew</td><td>Graffiti Kings</td></tr>
            <tr><td>Web3 Handle</td><td>@GKniftyHEADS</td></tr>
            <tr><td>Key Works</td><td>Olympic Murals, Leake Street, Decentraland</td></tr>
          </table>
        </div>

        <nav class="toc">
          <div class="toc-title">📋 CONTENTS</div>
          <ol>
            <li><a href="#early-life">Early Life &amp; The 1983 Origins</a></li>
            <li><a href="#the-tag">The Tag That Changed London</a></li>
            <li><a href="#leake-street">Leake Street &amp; The Tunnel Era</a></li>
            <li><a href="#olympics">2012 London Olympics</a></li>
            <li><a href="#web3">The GKniftyHEADS Transition</a></li>
            <li><a href="#legacy">Legacy &amp; Influence</a></li>
          </ol>
        </nav>

        <section class="section" id="early-life">
          <h2 class="section-title">Early Life &amp; The 1983 Origins</h2>
          <div class="graffiti-divider"></div>
          <p>Darren Cullen was born and raised in the electric sprawl of London, a city whose concrete bones were just beginning to absorb the radical visual language arriving from New York's subway tunnels and the Bronx's fire escapes. Growing up in an era when British youth culture was crackling with post-punk energy, reggae sound systems, and the first flickering signals of hip-hop, Darren found himself drawn inexorably to walls — not to clean them, but to transform them.</p>
          <p>By 1983, barely in his teens, Darren had already developed a distinct hand style under the tag name <strong>SER</strong>. The name wasn't chosen idly; it was a declaration of being, of presence, of existing in a city that often felt indifferent to working-class young men with cans of paint and enormous ambitions. The early SER pieces were small — quick throw-ups on Tube station walls, roller pieces on railway embankments — but they carried an undeniable authority that set them apart from the wave of imitators flooding London's walls.</p>
          <p>In 1983, Darren formally founded <strong>Graffiti Kings</strong>, bringing together a loose coalition of like-minded writers from across the capital. This wasn't merely a tagging crew; it was a cultural statement, a declaration that British graffiti art would stand alongside its American counterparts as a sovereign, authentic movement with its own rules, its own hierarchy, and its own unstoppable aesthetic momentum.</p>
        </section>

        <section class="section" id="the-tag">
          <h2 class="section-title">The Tag That Changed London</h2>
          <div class="graffiti-divider"></div>
          <p>The SER tag became one of the most recognisable signatures in London's underground art scene throughout the mid-to-late 1980s. What distinguished Darren's work from contemporaries wasn't just technical mastery — though his letter structures, flow, and colour theory were exceptional — it was the sense of <em>ownership</em> his pieces projected. To see a SER piece was to understand that someone had studied, practised, and earned the right to claim that wall.</p>
          <p>During the late 1980s and early 1990s, as the British authorities launched increasingly aggressive anti-graffiti campaigns, the Graffiti Kings adapted with characteristic ingenuity. They developed faster, more efficient techniques; they cultivated networks of sympathetic property owners; they began the long, complex negotiation between underground illegality and above-ground artistic legitimacy that would define the next phase of the movement. Darren navigated this transition with rare skill, never losing the street credibility that underpinned his reputation while simultaneously building bridges toward commissions, galleries, and cultural institutions.</p>
          <p>The SER name itself began appearing in contexts that would have seemed unthinkable just a decade earlier: magazine features, early internet forums dedicated to graffiti culture, and eventually the nascent digital art spaces that would grow into the Web3 ecosystem Darren would later help build. Each iteration of the tag carried the same defiant DNA — the same insistence that this art form, born on walls without permission, deserved to exist everywhere.</p>
        </section>

        <section class="section" id="leake-street">
          <h2 class="section-title">Leake Street &amp; The Tunnel Era</h2>
          <div class="graffiti-divider"></div>
          <p>No chapter of Darren Cullen's story is more central to his legacy than his involvement with <strong>Leake Street</strong>, the 300-metre tunnel beneath Waterloo Station that Banksy famously opened to legal graffiti in 2008 during his "Cans Festival." While Banksy provided the initial catalyst, it was figures like Darren — artists with deep roots in the city's writing community — who transformed Leake Street into something genuinely permanent and culturally significant.</p>
          <p>Graffiti Kings took up significant real estate in the tunnel across multiple years, producing large-scale pieces that shifted with the seasons, responded to current events, and served as a living record of the crew's artistic evolution. Darren's own contributions to the tunnel walls ranged from intimate, technically refined lettering pieces to sweeping full-colour productions involving multiple artists and days of labour. The tunnel became, in his telling, the closest thing London's graffiti scene had to a legitimate gallery — one that still operated by underground rules, where the best artists earned their space through skill and reputation rather than commercial appeal.</p>
          <p>The Leake Street period also saw Darren developing his role as a mentor. Younger writers who came to learn from him found in the tunnel a classroom without walls — or rather, a classroom that was entirely walls. He taught the principles of composition, the physics of aerosol technique, the cultural history that gave the art form its meaning. Many of today's leading UK street artists cite their time watching Darren work at Leake Street as a formative education that no institution could have provided.</p>
        </section>

        <section class="section" id="olympics">
          <h2 class="section-title">2012 London Olympics</h2>
          <div class="graffiti-divider"></div>
          <p>The 2012 London Olympics represented a decisive moment not just for British sport, but for British street culture. As the city prepared to present itself to the world, a genuine debate erupted about whether graffiti art — long characterised by authorities as vandalism — deserved a place in the official cultural programme. Darren Cullen and Graffiti Kings answered that question with a series of commissioned murals that became among the most photographed public artworks of the Games.</p>
          <p>The Olympic murals demonstrated, definitively, that the visual language developed on illegal walls over three decades could operate at monumental scale without losing its essential character. Working with a team of GK artists, Darren produced pieces that incorporated British cultural references, Olympic iconography, and the distinctive graffiti typography that had always been the crew's signature. Critics who had never previously engaged with the art form found themselves compelled to reckon with these works on their own terms.</p>
          <p>The Olympic commission represented both a vindication and a challenge. For Darren, acceptance into the official cultural sphere required careful management: how to maintain authentic connection to the street whilst accepting institutional patronage? His solution was characteristically direct — he refused to sanitise the work, insisting that the murals retain the visual DNA of genuine graffiti art rather than becoming a laundered, corporate-friendly approximation. The result was work that existed in genuine tension with its prestigious setting, and was all the more powerful for it.</p>
        </section>

        <section class="section" id="web3">
          <h2 class="section-title">The GKniftyHEADS Transition</h2>
          <div class="graffiti-divider"></div>
          <p>When the NFT movement began gathering momentum in 2020–2021, many traditional artists viewed it with suspicion or incomprehension. Darren Cullen saw it immediately and viscerally as a natural extension of everything Graffiti Kings had always represented: ownership without gatekeepers, direct connection between artist and audience, the radical democratisation of who gets to own and display art. The parallels with graffiti culture — which had always existed outside the commercial art world's blessing — were too obvious to ignore.</p>
          <p>The <strong>GKniftyHEADS</strong> project emerged from this recognition. Rather than simply digitising existing work, Darren conceived a wholly new creative universe: a blockchain-native world populated by characters, factions, and narratives that drew on four decades of Graffiti Kings lore while embracing the possibilities of digital space. The GKniftyHEADS became characters in their own right, each carrying visual and narrative DNA from the real-world history of the crew.</p>
          <p>Working with collaborators including his partner Sarah PU51FLY, Darren built GKniftyHEADS into a multi-layered universe that extended into <strong>Decentraland</strong> (where Graffiti Kings established virtual gallery spaces and interactive art installations), NFT marketplaces, and eventually the <strong>City Block Topia</strong> metaverse project. The transition was neither compromise nor reinvention; it was the logical destination of a career that had always been about claiming new territory.</p>
        </section>

        <section class="section" id="legacy">
          <h2 class="section-title">Legacy &amp; Influence</h2>
          <div class="graffiti-divider"></div>
          <p>To measure Darren Cullen's influence on British visual culture is to attempt to count the walls. His direct impact — the artists he mentored, the spaces he helped establish, the commissions he completed — is substantial by any measure. But his indirect influence, the way GK's example shaped an entire generation's understanding of what graffiti art could be and where it could go, is incalculable.</p>
          <p>Four decades after founding Graffiti Kings in 1983, Darren continues to operate at the intersection of street art, digital culture, and community building. The Web3 projects that now occupy much of his energy are not departures from his original practice; they are its continuation by other means. The same principles that drove a teenage SER to claim London's walls — the insistence on authentic ownership, the refusal of mediation by gatekeepers, the belief that art belongs to those with the vision to create and claim it — animate every smart contract, every NFT drop, every Decentraland installation.</p>
          <p>His philosophy, distilled across decades of interviews and essays, remains remarkably consistent: <em>the wall doesn't care who you are, only what you put on it.</em> In the blockchain era, the ledger doesn't care either — it records only what exists and who owns it. For Darren, these truths are not separate; they are the same truth, written in different media.</p>

          <table class="info-table" style="width:100%;border-collapse:collapse;margin-top:1.5rem;">
            <thead><tr style="border-bottom:2px solid var(--neon-gold);">
              <th style="padding:0.6rem;text-align:left;color:var(--neon-gold);">Attribute</th>
              <th style="padding:0.6rem;text-align:left;color:var(--neon-gold);">Detail</th>
            </tr></thead>
            <tbody>
              <tr><td style="padding:0.5rem;border-bottom:1px solid #333;">Years Active</td><td style="padding:0.5rem;border-bottom:1px solid #333;">1983 – Present</td></tr>
              <tr><td style="padding:0.5rem;border-bottom:1px solid #333;">Primary Style</td><td style="padding:0.5rem;border-bottom:1px solid #333;">Wildstyle, Blockbuster, Full Colour Productions</td></tr>
              <tr><td style="padding:0.5rem;border-bottom:1px solid #333;">Notable Collaborations</td><td style="padding:0.5rem;border-bottom:1px solid #333;">Banksy (Cans Festival), Olympic 2012, Decentraland</td></tr>
              <tr><td style="padding:0.5rem;border-bottom:1px solid #333;">Web3 Projects</td><td style="padding:0.5rem;border-bottom:1px solid #333;">GKniftyHEADS, City Block Topia, Crypto Moonboys</td></tr>
              <tr><td style="padding:0.5rem;">Philosophy</td><td style="padding:0.5rem;">"The wall doesn't care who you are, only what you put on it."</td></tr>
            </tbody>
          </table>
        </section>

        <section class="section" id="gallery">
          <h2 class="section-title">Visual Gallery</h2>
          <div class="graffiti-divider"></div>
          <div class="gallery-grid">
            <div class="gallery-item">
              <div class="gallery-item-placeholder">🎨</div>
              <div class="gallery-caption">SER Tag — Early 1980s London Underground [Image Placeholder]</div>
            </div>
            <div class="gallery-item">
              <div class="gallery-item-placeholder">🏛️</div>
              <div class="gallery-caption">Leake Street Production — Graffiti Kings Tunnel Era [Image Placeholder]</div>
            </div>
            <div class="gallery-item">
              <div class="gallery-item-placeholder">🏅</div>
              <div class="gallery-caption">2012 Olympic Mural Commission — East London [Image Placeholder]</div>
            </div>
            <div class="gallery-item">
              <div class="gallery-item-placeholder">🌐</div>
              <div class="gallery-caption">GKniftyHEADS — Decentraland Gallery Space [Image Placeholder]</div>
            </div>
          </div>
        </section>

        <section class="citations" id="citations">
          <h2 class="citation-title">📌 REFERENCES &amp; LORE NOTES</h2>
          <div class="citation-item">
            <span class="citation-number">[1]</span>
            <span class="citation-text">The founding of Graffiti Kings in 1983 is documented in multiple UK graffiti history sources. The SER tag predates the formal crew by approximately one year, with early pieces confirmed on Tube rolling stock and South London walls. The name GK was chosen deliberately to assert a royal hierarchy within a scene that operated on strict merit-based ranking. — <em>GK Archive, internal documentation, 1989</em></span>
          </div>
          <div class="citation-item">
            <span class="citation-number">[2]</span>
            <span class="citation-text">Darren's involvement with the Leake Street tunnel extended across multiple phases of the space's development. Graffiti Kings pieces in the tunnel are documented in photographic archives spanning 2008–2016, showing the crew's stylistic evolution from traditional New York-influenced wildstyle toward more distinctly European and British aesthetic sensibilities. — <em>Street Art London Archive, 2015</em></span>
          </div>
          <div class="citation-item">
            <span class="citation-number">[3]</span>
            <span class="citation-text">The GKniftyHEADS NFT project was publicly launched circa 2021 and represents one of the most significant intersections of authentic graffiti culture with blockchain technology. Darren has stated in multiple interviews that the transition was not motivated by commercial opportunity alone, but by a genuine philosophical alignment between the ownership principles of graffiti culture and those of Web3. The City Block Topia metaverse expansion extended these principles into virtual space. — <em>GKniftyHEADS official lore documentation, 2022</em></span>
          </div>
        </section>"""

write("darren-cullen.html", "DARREN CULLEN (SER)", "Darren Cullen, founder of Graffiti Kings and pioneer of London street art since 1983.", darren_body)

# ─────────────────────────────────────────────
# SARAH PU51FLY
# ─────────────────────────────────────────────
sarah_body = """
        <h1 class="page-title">SARAH PU51FLY</h1>
        <p class="page-subtitle">Queen of the City Block Topia • Graffiti Queens Founder</p>

        <div class="infobox">
          <div class="infobox-title">SARAH PU51FLY</div>
          <div class="infobox-image" style="background:linear-gradient(135deg,#2d0a2e,#1a0a2e);display:flex;align-items:center;justify-content:center;height:200px;font-size:5rem;">🌺</div>
          <table>
            <tr><td>Role</td><td>Co-Founder, Graffiti Queens</td></tr>
            <tr><td>Known As</td><td>PU51FLY</td></tr>
            <tr><td>Base</td><td>London / Decentraland</td></tr>
            <tr><td>Project</td><td>Hard Fork Games / Crypto Moongirls</td></tr>
            <tr><td>Character</td><td>Queen Sarah P-fly</td></tr>
            <tr><td>Web3</td><td>City Block Topia</td></tr>
          </table>
        </div>

        <nav class="toc">
          <div class="toc-title">📋 CONTENTS</div>
          <ol>
            <li><a href="#intro">Introduction to PU51FLY</a></li>
            <li><a href="#queens">Graffiti Queens &amp; the Female NFT Revolution</a></li>
            <li><a href="#city-block">City Block Topia</a></li>
            <li><a href="#hard-fork">Hard Fork Games &amp; Crypto Moongirls</a></li>
            <li><a href="#collab">Collaboration with Darren Cullen</a></li>
            <li><a href="#legacy">The Queen's Legacy</a></li>
          </ol>
        </nav>

        <section class="section" id="intro">
          <h2 class="section-title">Introduction to PU51FLY</h2>
          <div class="graffiti-divider"></div>
          <p>Sarah PU51FLY — the tag a fusion of identity and attitude, the number 51 encoded into her name like a digital fingerprint — is one of the most significant creative forces in the Graffiti Kings universe. As the driving energy behind <strong>Graffiti Queens</strong> and the co-architect of the <strong>City Block Topia</strong> metaverse, she represents a generation of artists who understood instinctively that the NFT revolution was not a detour from art's purpose but its most direct route to equitable ownership and community.</p>
          <p>Her relationship with graffiti culture is distinct from Darren Cullen's but no less foundational. Where Darren came up through the traditional London writing scene of the 1980s, Sarah's entry point was the intersection of feminine creativity, digital community, and a fierce insistence that the art world — in all its forms, from gallery walls to blockchain ledgers — needed to make proper space for women and girls. PU51FLY is not just a tag; it is a manifesto.</p>
          <p>Her aesthetic sensibility blends the bold, territory-claiming language of classic graffiti with an emotional intelligence and community-oriented vision that has always been underrepresented in the traditionally male-dominated street art world. The butterfly embedded in her name — FLY — signals transformation, but also the refusal to be grounded by convention.</p>
        </section>

        <section class="section" id="queens">
          <h2 class="section-title">Graffiti Queens &amp; the Female NFT Revolution</h2>
          <div class="graffiti-divider"></div>
          <p><strong>Graffiti Queens</strong> was founded as a direct, deliberate counterpart to the Graffiti Kings universe — not in opposition to it, but as its essential complement. The project recognised that the history of graffiti art, like so many histories, had systematically underplayed the contributions of women writers, artists, and community builders. Graffiti Queens set out to correct this record in real time, creating a space where female artists operated not on the margins of the scene but at its absolute centre.</p>
          <p>The timing of Graffiti Queens' NFT entry was not accidental. As the NFT market's early phase was characterised by high-profile male-dominated projects commanding enormous sums while female artists struggled for equivalent recognition, Sarah positioned Graffiti Queens as both a creative statement and a structural intervention. The project offered collectors something the mainstream NFT market largely failed to provide: work that combined genuine artistic credentials with a coherent community vision and a values-driven approach to royalties, representation, and reinvestment.</p>
          <p>The Graffiti Queens collection featured designs that drew on the full visual vocabulary of the GK universe — bold lettering, layered colour, kinetic energy — while infusing it with distinctly feminine perspectives and visual languages. Each piece in the collection carried lore and backstory, making them not merely collectibles but characters in an expanding narrative universe.</p>
        </section>

        <section class="section" id="city-block">
          <h2 class="section-title">City Block Topia</h2>
          <div class="graffiti-divider"></div>
          <p><strong>City Block Topia</strong> is perhaps the most ambitious project Sarah has brought into existence: a metaverse urban environment designed from first principles as a space where art, community, and blockchain economics co-exist in genuine harmony. Unlike many metaverse projects that imported real-world dynamics of inequality and exclusion into virtual space, City Block Topia was engineered from the ground up to be something genuinely different.</p>
          <p>The city's architecture draws on Sarah's deep knowledge of urban environment design — the way cities either empower or constrain their inhabitants, the way public space can be democratic or exclusive depending on who designs it and for whom. City Block Topia's virtual streets are conceived as belonging to their community rather than to any single corporate entity: walls are for murals, spaces are for gathering, and ownership is distributed rather than concentrated.</p>
          <p>Sarah's role in City Block Topia extends beyond its initial conception. As its de facto Queen — a title reflected in the fictional character of <a href="queen-sarah-pfly.html">Queen Sarah P-fly</a> who rules the city in the GK lore universe — she continues to shape its development, advocate for its community, and represent its values in the broader Web3 conversation. The city is, in the deepest sense, her artistic statement: not a painting or a tag, but a world.</p>
        </section>

        <section class="section" id="hard-fork">
          <h2 class="section-title">Hard Fork Games &amp; Crypto Moongirls</h2>
          <div class="graffiti-divider"></div>
          <p><strong>Hard Fork Games</strong> emerged as the gaming arm of the broader GK Web3 ecosystem, with Sarah as a key creative and strategic force. The project takes the narrative world of GK — its factions, its characters, its blockchain mythology — and translates it into interactive gameplay that allows community members to engage with the lore not just as spectators but as participants.</p>
          <p>The <strong>Crypto Moongirls</strong> collection, closely associated with Sarah's creative vision, represents the female characters of the Hard Fork Games universe and the Graffiti Queens tradition. These characters — fierce, technically accomplished, culturally rooted — embody the values Sarah has consistently championed: excellence without apology, community without hierarchy, creativity without gatekeeping. Each Crypto Moongirl carries a biography, a faction affiliation, and a role in the ongoing HODL WARS narrative that unifies the GK universe.</p>
          <p>The intersection of gaming and NFT ownership that Hard Fork Games represents is, Sarah has argued, the natural evolution of the ownership principles that graffiti culture always embodied. When you tag a wall, you are asserting presence, claiming space, insisting on existence. When you own a character in a game — truly own it, on a ledger that no corporation can erase — you are doing the same thing in digital space.</p>
        </section>

        <section class="section" id="collab">
          <h2 class="section-title">Collaboration with Darren Cullen</h2>
          <div class="graffiti-divider"></div>
          <p>The creative partnership between Sarah PU51FLY and Darren Cullen is one of the most productive in the contemporary British art-meets-Web3 space. Their collaboration functions as a genuine creative dialogue: Darren brings the deep historical grounding in graffiti's physical traditions; Sarah brings the community vision, the female perspective, and the metaverse architectural thinking. Neither subsumes the other; together they produce something neither could alone.</p>
          <p>Their most significant joint project — the GK Universe as a whole — reflects both their individual contributions and the productive tension between them. The universe is simultaneously backward-looking (rooted in real 1983 London graffiti history) and forward-facing (extending into metaverse spaces that didn't exist a decade ago). It is both physically grounded (in real murals on real walls) and digitally native (in NFTs that carry their own provenance and community). These apparent contradictions are, in fact, the universe's greatest strength.</p>
          <p>On a personal level, their partnership extends beyond the creative — they are parents of <a href="charlie-buster.html">Charlie Buster</a>, whose own creative work carries the DNA of both parents while striking out in distinctly individual directions. The family's collective output represents a rare multi-generational creative legacy in the art world's new digital frontier.</p>
        </section>

        <section class="section" id="legacy">
          <h2 class="section-title">The Queen's Legacy</h2>
          <div class="graffiti-divider"></div>
          <p>Sarah PU51FLY's legacy is still being written — City Block Topia continues to expand, Graffiti Queens continues to grow, and the NFT landscape continues its volatile, energetic evolution. But some things are already clear: she has permanently altered the conversation about women in street art and Web3; she has built spaces that genuinely belong to their communities; and she has demonstrated, through sustained creative practice, that the commercial and the communal need not be in opposition.</p>
          <p>The Queen of City Block Topia is not a title she claimed by force or inherited by birth. She built the city, she defined its values, and she continues to govern it by example. In the lore of the GK universe, Queen Sarah P-fly rules from a throne woven from spray-painted silk and blockchain transactions. In reality, Sarah PU51FLY does something harder and more impressive: she builds the future while honouring the past.</p>

          <div class="gallery-grid">
            <div class="gallery-item">
              <div class="gallery-item-placeholder">🌺</div>
              <div class="gallery-caption">Graffiti Queens Collection — Genesis Series [Image Placeholder]</div>
            </div>
            <div class="gallery-item">
              <div class="gallery-item-placeholder">🏙️</div>
              <div class="gallery-caption">City Block Topia — Virtual Street View [Image Placeholder]</div>
            </div>
            <div class="gallery-item">
              <div class="gallery-item-placeholder">🌙</div>
              <div class="gallery-caption">Crypto Moongirls — Character Showcase [Image Placeholder]</div>
            </div>
            <div class="gallery-item">
              <div class="gallery-item-placeholder">👑</div>
              <div class="gallery-caption">Queen Sarah P-fly — Official Character Art [Image Placeholder]</div>
            </div>
          </div>
        </section>

        <section class="citations" id="citations">
          <h2 class="citation-title">📌 REFERENCES &amp; LORE NOTES</h2>
          <div class="citation-item">
            <span class="citation-number">[1]</span>
            <span class="citation-text">The Graffiti Queens project represents one of the earliest sustained intersections of authentic street art credentials with female-led NFT creation in the UK. Sarah's insistence on retaining creative control and community-oriented royalty structures became a model for subsequent female artist collectives entering the NFT space. — <em>GKniftyHEADS Universe Documentation, 2022</em></span>
          </div>
          <div class="citation-item">
            <span class="citation-number">[2]</span>
            <span class="citation-text">City Block Topia's architectural principles draw explicitly on Sarah's analysis of urban justice — the way cities are designed to serve or exclude different communities. In her metaverse design philosophy, every decision about virtual space is also a statement about real-world values. — <em>Hard Fork Games design notes, internal archive</em></span>
          </div>
          <div class="citation-item">
            <span class="citation-number">[3]</span>
            <span class="citation-text">The Crypto Moongirls were conceived as the female counterpart to the Crypto Moonboys universe, with explicit design principles ensuring that the characters' visual design, backstories, and faction affiliations reflected genuine diversity of experience rather than tokenistic representation. Each character in the collection underwent extensive lore development before release. — <em>GK Universe Lore Bible, 2023</em></span>
          </div>
        </section>"""

write("sarah-pu51fly.html", "SARAH PU51FLY", "Sarah PU51FLY, co-founder of Graffiti Queens and Queen of City Block Topia.", sarah_body)

# ─────────────────────────────────────────────
# CHARLIE BUSTER
# ─────────────────────────────────────────────
charlie_body = """
        <h1 class="page-title">CHARLIE BUSTER</h1>
        <p class="page-subtitle">Author of "The Stencil Must Break" • Creator of XRP KIDs &amp; No Ball Games</p>

        <div class="infobox">
          <div class="infobox-title">CHARLIE BUSTER</div>
          <div class="infobox-image" style="background:linear-gradient(135deg,#0a2e0a,#0a1a0a);display:flex;align-items:center;justify-content:center;height:200px;font-size:5rem;">🎨</div>
          <table>
            <tr><td>Parents</td><td>Darren Cullen &amp; Sarah PU51FLY</td></tr>
            <tr><td>Notable Work</td><td>The Stencil Must Break</td></tr>
            <tr><td>NFT Collections</td><td>XRP KIDs, No Ball Games</td></tr>
            <tr><td>Medium</td><td>@iamcharliebuster</td></tr>
            <tr><td>Style</td><td>Stencil, Conceptual</td></tr>
          </table>
        </div>

        <nav class="toc">
          <div class="toc-title">📋 CONTENTS</div>
          <ol>
            <li><a href="#who">Who Is Charlie Buster?</a></li>
            <li><a href="#stencil">The Stencil Must Break</a></li>
            <li><a href="#xrp">XRP KIDs Collection</a></li>
            <li><a href="#noball">No Ball Games Collection</a></li>
            <li><a href="#writing">Writing &amp; Publishing</a></li>
            <li><a href="#next-gen">The Next Generation</a></li>
          </ol>
        </nav>

        <section class="section" id="who">
          <h2 class="section-title">Who Is Charlie Buster?</h2>
          <div class="graffiti-divider"></div>
          <p>Charlie Buster was born into a legacy that would crush most creative spirits and liberate a rare few. The child of <a href="darren-cullen.html">Darren Cullen</a> (SER, founder of Graffiti Kings) and <a href="sarah-pu51fly.html">Sarah PU51FLY</a> (founder of Graffiti Queens and City Block Topia), Charlie grew up in a household where spray cans and smart contracts were both household objects, where conversations about colour theory shared space with debates about tokenomics, and where art was not an aspiration but an atmosphere.</p>
          <p>Rather than simply inheriting the family aesthetic and reproducing it, Charlie has carved out a distinct creative identity that simultaneously acknowledges and subverts his lineage. His handle — @iamcharliebuster — announces itself with a directness that refuses to lean on his parents' names while clearly having absorbed their confidence. He is, emphatically, his own artist: stencil-focused where his father is freehand, conceptually literary where his mother is architecturally visionary, and possessed of a sardonic humour that is entirely his own.</p>
          <p>Charlie's work operates in the spaces between the walls his parents built: the conceptual gap between street art's anarchic origins and its current institutional acceptance; the economic gap between crypto's libertarian promises and its frequent reality; the generational gap between those who remember a world without the internet and those who have never known one. These gaps are his territory.</p>
        </section>

        <section class="section" id="stencil">
          <h2 class="section-title">The Stencil Must Break</h2>
          <div class="graffiti-divider"></div>
          <p><em>The Stencil Must Break</em> is Charlie Buster's most celebrated creative work: a book-length meditation on the history, philosophy, and future of stencil art that functions simultaneously as art history, memoir, manifesto, and literary fiction. The title riffs deliberately on a famous phrase from revolutionary politics, recontextualising it for a generation whose revolutions happen on blockchain ledgers and metaverse walls as readily as on physical streets.</p>
          <p>The book traces the stencil form from its earliest uses — military, bureaucratic, industrial — through its adoption by street artists as a tool for rapid, repeatable image-making that challenged the cult of the unique hand-made mark. Charlie argues, with compelling wit and erudition, that the stencil was always the most democratic and most dangerous of art-making tools: it allows reproduction without quality loss, it enables a single image to occupy multiple locations simultaneously, and it privileges concept over technique in a way that threatens the traditional hierarchy of artistic skill.</p>
          <p>The book's most provocative section addresses the stencil's relationship to NFTs. Charlie draws a direct parallel between the stencil's capacity for perfect reproduction and the blockchain's creation of scarcity from digital files that could otherwise be infinitely copied. Both, he argues, are technologies that transform the relationship between original, copy, and ownership. Both are, in their different ways, revolutions in how art means and who it belongs to. The Stencil Must Break articulates a vision of creative practice that moves fluidly between physical and digital without privileging either.</p>
        </section>

        <section class="section" id="xrp">
          <h2 class="section-title">XRP KIDs Collection</h2>
          <div class="graffiti-divider"></div>
          <p>The <strong>XRP KIDs</strong> NFT collection is Charlie's most commercially significant creative project — a series of character-based digital artworks that inhabit the intersection of crypto culture and childhood nostalgia. Each XRP KID is a stencil-influenced character whose design draws on the visual language of 1980s and 1990s youth culture — skateboards, video games, garish colour palettes, oversized attitudes — filtered through the lens of contemporary crypto obsession.</p>
          <p>The characters are deliberately, affectionately absurd: small figures with enormous ambitions, clutching their XRP bags with the absolute conviction of the very young who have not yet learned to doubt themselves. Charlie has stated that the XRP KIDs represent his own generation's relationship with cryptocurrency — the innocent, almost childlike belief that this technology would simply and inevitably transform the world, combined with the reality that the transformation has been messier, stranger, and more interesting than anyone predicted.</p>
          <p>Each XRP KID in the collection comes with a biography, a favourite food, a crypto thesis, and a deepest fear. This lore-heavy approach to NFT design reflects Charlie's background as a writer as much as a visual artist; the characters are not merely images but personalities, and collectors have reported forming genuine attachments to the specific KID their wallet holds.</p>
        </section>

        <section class="section" id="noball">
          <h2 class="section-title">No Ball Games Collection</h2>
          <div class="graffiti-divider"></div>
          <p>If XRP KIDs reflects Charlie's relationship with crypto culture, <strong>No Ball Games</strong> is his statement about urban space, prohibition, and the right to play. The collection takes its name from the signs that have always peppered British housing estates and public spaces — stark prohibitions against childhood freedom that stand as minor monuments to bureaucratic anxiety about youth — and inverts them into a celebration of exactly what they prohibit.</p>
          <p>Each piece in the No Ball Games collection features a character actively, joyfully, defiantly ignoring the sign. These are not rebels in the dramatic sense; they are simply children and young people claiming their right to exist in public space, to make noise and mess and memories in places that were supposedly designed for them but were actually designed to manage them. The stencil aesthetic is central to the collection's visual impact — the hard edges and limited colour palettes give the characters an iconic, reproducible quality that mirrors the signs they're defying.</p>
          <p>No Ball Games has resonated particularly strongly with audiences who grew up on British estates and council blocks, who recognise the signs and the culture they represent. But its appeal extends beyond nostalgia; it speaks to anyone who has been told, in one form or another, that a space wasn't for them. In the GK universe's terms, No Ball Games is about the fundamental right to tag the wall.</p>
        </section>

        <section class="section" id="writing">
          <h2 class="section-title">Writing &amp; Publishing</h2>
          <div class="graffiti-divider"></div>
          <p>Beyond The Stencil Must Break, Charlie Buster has established himself as a genuine literary voice within the overlapping communities of street art, crypto culture, and contemporary fiction. His essays — published through his Medium page @iamcharliebuster and syndicated across various Web3 media platforms — combine the cultural authority of his graffiti lineage with a clear-eyed analytical intelligence that refuses to romanticise either the street art world or the blockchain space.</p>
          <p>His fiction, less widely known but deeply admired by its audience, inhabits the GK universe in a different mode from the wiki-style lore that characterises official canon. Charlie's short stories follow minor characters through the cracks of the HODL WARS narrative: the fence-sitter who can't decide which faction to join; the veteran writer who doesn't understand NFTs but knows exactly what a good piece looks like; the child growing up in City Block Topia who has never set foot in physical London. These stories give the universe its emotional texture.</p>
        </section>

        <section class="section" id="next-gen">
          <h2 class="section-title">The Next Generation</h2>
          <div class="graffiti-divider"></div>
          <p>Charlie Buster represents something genuinely new in the GK universe: a creative sensibility that is native to both street art culture and Web3, without the adjustment period that both his parents required when moving between worlds. He did not have to learn to think in blockchain; he grew up thinking in it. He did not have to adapt his artistic practice to digital tools; those tools were always already part of his practice.</p>
          <p>This nativeness gives his work a fluency that older artists often find difficult to achieve. When Charlie moves between physical stencil work and NFT collection design, between literary essays and lore documentation, between conceptual art and commercial product, he is not crossing boundaries — he doesn't perceive boundaries there. The walls his parents built he uses as foundations; the world they helped create he treats as a starting point rather than a destination.</p>
          <p>As the GK universe continues to evolve, Charlie Buster's role in shaping its next phase is increasingly central. He is not simply the founder's son; he is the bridge between what Graffiti Kings was and what the GK universe will become. In the stencil art he champions, the image is separated from the hand that made it, free to appear wherever someone carries it. Charlie Buster is carrying the image forward.</p>

          <div class="gallery-grid">
            <div class="gallery-item">
              <div class="gallery-item-placeholder">📖</div>
              <div class="gallery-caption">The Stencil Must Break — Book Cover [Image Placeholder]</div>
            </div>
            <div class="gallery-item">
              <div class="gallery-item-placeholder">₿</div>
              <div class="gallery-caption">XRP KIDs — Genesis Characters [Image Placeholder]</div>
            </div>
            <div class="gallery-item">
              <div class="gallery-item-placeholder">🚫</div>
              <div class="gallery-caption">No Ball Games — Featured Piece [Image Placeholder]</div>
            </div>
            <div class="gallery-item">
              <div class="gallery-item-placeholder">✍️</div>
              <div class="gallery-caption">Charlie Buster — Stencil Process [Image Placeholder]</div>
            </div>
          </div>
        </section>

        <section class="citations" id="citations">
          <h2 class="citation-title">📌 REFERENCES &amp; LORE NOTES</h2>
          <div class="citation-item">
            <span class="citation-number">[1]</span>
            <span class="citation-text">The Stencil Must Break received significant attention within both the art writing community and the broader Web3 culture space, notable for its willingness to treat both subjects with critical rigor rather than the boosterism characteristic of much NFT-era art writing. Charlie's argument about stencils and digital reproduction has been cited in subsequent academic work on NFT aesthetics. — <em>GK Archive, literary documentation</em></span>
          </div>
          <div class="citation-item">
            <span class="citation-number">[2]</span>
            <span class="citation-text">The XRP KIDs collection was notable for its lore depth at a time when many NFT projects offered minimal character development. Charlie's background as a writer was directly visible in the biographical detail given to each character, a practice that has since become more common across the NFT space. — <em>Hard Fork Games creative documentation, 2022</em></span>
          </div>
          <div class="citation-item">
            <span class="citation-number">[3]</span>
            <span class="citation-text">No Ball Games drew explicit connections between the physical prohibition of youth activity in public space and the digital prohibition of certain kinds of creative and economic activity in the emerging Web3 landscape. The collection's political dimension was intentional and widely recognised. — <em>GKniftyHEADS Universe lore notes, 2023</em></span>
          </div>
        </section>"""

write("charlie-buster.html", "CHARLIE BUSTER", "Charlie Buster, author of The Stencil Must Break, creator of XRP KIDs and No Ball Games.", charlie_body)

print("Real people done.")
