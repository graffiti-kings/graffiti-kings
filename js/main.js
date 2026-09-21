// Matrix Rain Animation
const canvas = document.getElementById('matrixCanvas');
if (canvas) {
  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$₿⚡🎨';
  const fontSize = 14;
  const columns = Math.floor(canvas.width / fontSize);
  const drops = Array(columns).fill(1);

  function drawMatrix() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#FFD700';
    ctx.font = fontSize + 'px monospace';
    drops.forEach((y, i) => {
      const char = chars[Math.floor(Math.random() * chars.length)];
      ctx.fillText(char, i * fontSize, y * fontSize);
      if (y * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
      drops[i]++;
    });
  }
  setInterval(drawMatrix, 50);

  window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  });
}

// Sitewide layout fixes
(function applyWikiLayoutFixes() {
  const style = document.createElement('style');
  style.textContent = `
    .sidebar {
      max-height: calc(100vh - 110px);
      overflow-y: auto;
      overflow-x: hidden;
      scrollbar-width: thin;
      scrollbar-color: var(--neon-gold) #111;
    }

    .sidebar::-webkit-scrollbar {
      width: 8px;
    }

    .sidebar::-webkit-scrollbar-track {
      background: #111;
      border-radius: 8px;
    }

    .sidebar::-webkit-scrollbar-thumb {
      background: var(--neon-gold);
      border-radius: 8px;
    }

    .sidebar-section {
      margin-bottom: 1.25rem;
    }

    .sidebar-links a {
      display: block;
      line-height: 1.25;
      padding-top: 0.35rem;
      padding-bottom: 0.35rem;
      word-break: normal;
      overflow-wrap: anywhere;
    }

    @media (max-width: 900px) {
      .sidebar {
        position: relative;
        top: auto;
        max-height: none;
        overflow: visible;
      }
    }
  `;
  document.head.appendChild(style);

  const emojiPrefix = /^[\p{Emoji_Presentation}\p{Extended_Pictographic}\uFE0F\u200D\s]+/u;
  document.querySelectorAll('.sidebar-links a').forEach((link) => {
    link.textContent = link.textContent.replace(emojiPrefix, '').trim();
  });
})();

// Hamburger Menu
const hamburger = document.querySelector('.hamburger');
const siteHeader = document.querySelector('.site-header');
if (hamburger && siteHeader) {
  hamburger.addEventListener('click', () => {
    siteHeader.classList.toggle('nav-open');
    hamburger.classList.toggle('active');
  });
}

// Search functionality
const searchInput = document.querySelector('.search-input');
const searchResults = document.querySelector('.search-results');

const siteIndex = [
  { title: 'Home', type: 'Page', url: 'index.html' },
  { title: 'About', type: 'Page', url: 'about.html' },
  { title: 'History & Timeline', type: 'Page', url: 'history.html' },
  { title: 'Characters', type: 'Directory', url: 'characters/index.html' },
  { title: 'Factions', type: 'Directory', url: 'factions/index.html' },
  { title: 'Mechanics & Rewards', type: 'Page', url: 'pages/mechanics.html' },
  { title: 'Music & Radio', type: 'Page', url: 'pages/music.html' },
  { title: 'NFT Collections', type: 'Page', url: 'pages/nft-collections.html' },
  { title: 'Submit Lore', type: 'Page', url: 'pages/submit-lore.html' },

  { title: 'Darren Cullen (SER)', type: 'Person', url: 'characters/darren-cullen.html' },
  { title: 'Sarah PU51FLY', type: 'Person', url: 'characters/sarah-pu51fly.html' },
  { title: 'Charlie Buster', type: 'Person', url: 'characters/charlie-buster.html' },
  { title: 'Alfie Bitcoin Kid', type: 'Character', url: 'characters/alfie-bitcoin-kid.html' },
  { title: 'Queen Sarah P-fly', type: 'Character', url: 'characters/queen-sarah-pfly.html' },
  { title: 'NULL THE PROPHET', type: 'Character', url: 'characters/null-the-prophet.html' },
  { title: 'Elder Codex-7', type: 'Character', url: 'characters/elder-codex-7.html' },
  { title: 'Thera-9', type: 'Character', url: 'characters/thera-9.html' },
  { title: 'Lady-INK', type: 'Character', url: 'characters/lady-ink.html' },
  { title: 'Jodie ZOOM 2000', type: 'Character', url: 'characters/jodie-zoom.html' },
  { title: 'Aleema', type: 'Character', url: 'characters/aleema.html' },
  { title: 'Iris-7', type: 'Character', url: 'characters/iris-7.html' },
  { title: 'Snipey D-Man', type: 'Character', url: 'characters/snipey-d-man.html' },
  { title: 'Bit-Cap 5000', type: 'Character', url: 'characters/bit-cap-5000.html' },
  { title: 'Forksplit', type: 'Character', url: 'characters/forksplit.html' },
  { title: 'M1NTR-K1LL', type: 'Character', url: 'characters/m1ntr-k1ll.html' },
  { title: 'SatoRebel', type: 'Character', url: 'characters/satorebel.html' },
  { title: 'Thorne Architect', type: 'Character', url: 'characters/thorne-architect.html' },
  { title: 'Billy Goat Kid', type: 'Character', url: 'characters/billy-goat-kid.html' },
  { title: 'HEX-TAGGER PRIME', type: 'Character', url: 'characters/hex-tagger-prime.html' },
  { title: 'The Whitewasher', type: 'Character', url: 'characters/whitewasher.html' },
  { title: 'GRIT', type: 'Character', url: 'characters/grit.html' },
  { title: 'PYRALITH', type: 'Character', url: 'characters/pyralith.html' },
  { title: 'Loopfiend', type: 'Character', url: 'characters/loopfiend.html' },
  { title: 'Samael.exe', type: 'Character', url: 'characters/samael-exe.html' },
  { title: 'Forklord You', type: 'Character', url: 'characters/forklord-you.html' },
  { title: 'Quell', type: 'Character', url: 'characters/quell.html' },
  { title: 'Sister Halcyon', type: 'Character', url: 'characters/sister-halcyon.html' },
  { title: 'Grit42', type: 'Character', url: 'characters/grit42.html' },
  { title: 'Rune Tag', type: 'Character', url: 'characters/rune-tag.html' },
  { title: 'Patchwork', type: 'Character', url: 'characters/patchwork.html' },
  { title: 'The Princess', type: 'Character', url: 'characters/the-princess.html' },
  { title: 'Dragan Volkov', type: 'Character', url: 'characters/dragan-volkov.html' },
  { title: 'Ava Chen', type: 'Character', url: 'characters/ava-chen.html' },

  { title: 'GKniftyHEADS', type: 'Faction', url: 'factions/gkniftyheads.html' },
  { title: 'GraffPUNKS', type: 'Faction', url: 'factions/graffpunks.html' },
  { title: 'HODLWARRIORS', type: 'Faction', url: 'factions/hodlwarriors.html' },
  { title: 'NoBallGames Legion', type: 'Faction', url: 'factions/no-ball-games-legion.html' },
  { title: 'Crypto Moongirls Eternal', type: 'Faction', url: 'factions/crypto-moongirls-eternal.html' },
  { title: 'Bitcoin Kid Army', type: 'Faction', url: 'factions/bitcoin-kid-army.html' },
  { title: 'Nomad Bears', type: 'Faction', url: 'factions/nomad-bears.html' },
  { title: 'House of Rackinsats Eternal', type: 'Faction', url: 'factions/house-of-rackinsats-eternal.html' },
  { title: 'Burn Crews', type: 'Faction', url: 'factions/burn-crews.html' },
  { title: 'Stencil Witches', type: 'Faction', url: 'factions/stencil-witches.html' },
  { title: 'Tag Lords', type: 'Faction', url: 'factions/tag-lords.html' },
  { title: 'Brush Daughters', type: 'Faction', url: 'factions/brush-daughters.html' },
  { title: 'Echo Mothers', type: 'Faction', url: 'factions/echo-mothers.html' },
  { title: 'Wildstyle Collective', type: 'Faction', url: 'factions/wildstyle-collective.html' },
  { title: 'Fractal Taggers', type: 'Faction', url: 'factions/fractal-taggers.html' },
  { title: 'Porch Poets', type: 'Faction', url: 'factions/porch-poets.html' },
  { title: 'Deep Holders', type: 'Faction', url: 'factions/deep-holders.html' },
  { title: 'Whale Lords Eternal', type: 'Faction', url: 'factions/whale-lords-eternal.html' },
  { title: 'HODL Layer Sentinels', type: 'Faction', url: 'factions/hodl-layer-sentinels.html' },
  { title: 'Compound Believers', type: 'Faction', url: 'factions/compound-believers.html' },
  { title: 'Genesis Anchors', type: 'Faction', url: 'factions/genesis-anchors.html' },
  { title: 'Porch Accord Diplomats', type: 'Faction', url: 'factions/porch-accord-diplomats.html' },
  { title: 'Belief Miners', type: 'Faction', url: 'factions/belief-miners.html' },
  { title: 'Eternal Porch Keepers', type: 'Faction', url: 'factions/eternal-porch-keepers.html' },
  { title: 'BinLords', type: 'Faction', url: 'factions/binlords.html' },
  { title: 'Tag Rush Crew', type: 'Faction', url: 'factions/tag-rush-crew.html' },
  { title: 'League of Keepers', type: 'Faction', url: 'factions/league-of-keepers.html' },
  { title: 'Arcade Scribes', type: 'Faction', url: 'factions/arcade-scribes.html' },
  { title: 'Quest Givers', type: 'Faction', url: 'factions/quest-givers.html' },
  { title: 'Pixel Pushers', type: 'Faction', url: 'factions/pixel-pushers.html' },
  { title: 'Level Lords', type: 'Faction', url: 'factions/level-lords.html' },
  { title: 'Nomad Drip House', type: 'Faction', url: 'factions/nomad-drip-house.html' },
  { title: 'Rackinsats Fashion House', type: 'Faction', url: 'factions/rackinsats-fashion-house.html' },
  { title: 'Crypto Badgers', type: 'Faction', url: 'factions/crypto-badgers.html' },
  { title: 'Mutant Pasteups', type: 'Faction', url: 'factions/mutant-pasteups.html' },
  { title: 'Cross-Chain Couriers', type: 'Faction', url: 'factions/cross-chain-couriers.html' },
  { title: 'Croydon Oracles', type: 'Faction', url: 'factions/croydon-oracles.html' },
  { title: 'Grid Ghosts', type: 'Faction', url: 'factions/grid-ghosts.html' },
  { title: 'Null Priests', type: 'Faction', url: 'factions/null-priests.html' },
  { title: 'SAM Watchers', type: 'Faction', url: 'factions/sam-watchers.html' },
  { title: 'Whitewall Remnants', type: 'Faction', url: 'factions/whitewall-remnants.html' },
  { title: 'Lost Moonboys', type: 'Faction', url: 'factions/lost-moonboys.html' },
  { title: 'The Unnamed Fortieth', type: 'Faction', url: 'factions/the-unnamed-fortieth.html' },
];

function resolveSearchUrl(url) {
  const path = window.location.pathname;
  if (path.includes('/characters/') || path.includes('/factions/') || path.includes('/pages/')) {
    return '../' + url;
  }
  return url;
}

if (searchInput) {
  searchInput.addEventListener('input', function() {
    const query = this.value.toLowerCase().trim();
    if (!searchResults) return;
    if (query.length < 2) {
      searchResults.style.display = 'none';
      return;
    }
    const matches = siteIndex.filter(item => item.title.toLowerCase().includes(query));
    if (matches.length === 0) {
      searchResults.style.display = 'none';
      return;
    }
    searchResults.innerHTML = matches.slice(0, 12).map(item =>
      `<a href="${resolveSearchUrl(item.url)}" class="search-result-item">
        <div class="search-result-title">${item.title}</div>
        <div class="search-result-type">${item.type}</div>
      </a>`
    ).join('');
    searchResults.style.display = 'block';
  });

  document.addEventListener('click', (e) => {
    if (!e.target.closest('.search-container')) {
      if (searchResults) searchResults.style.display = 'none';
    }
  });
}

// Smooth scroll for TOC links
document.querySelectorAll('.toc a[href^="#"]').forEach(link => {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});