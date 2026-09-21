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

function getSearchBasePath() {
  const path = window.location.pathname;
  if (path.includes('/characters/') || path.includes('/factions/') || path.includes('/pages/')) {
    return '../';
  }
  return '';
}

// All pages index for search
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
  { title: 'Aleema', type: 'Character', url: 'characters/aleema.html' },
  { title: 'Ava Chen', type: 'Character', url: 'characters/ava-chen.html' },
  { title: 'Billy Goat Kid', type: 'Character', url: 'characters/billy-goat-kid.html' },
  { title: 'Bit-Cap 5000', type: 'Character', url: 'characters/bit-cap-5000.html' },
  { title: 'Dragan Volkov', type: 'Character', url: 'characters/dragan-volkov.html' },
  { title: 'Elder Codex-7', type: 'Character', url: 'characters/elder-codex-7.html' },
  { title: 'Forklord You', type: 'Character', url: 'characters/forklord-you.html' },
  { title: 'Forksplit', type: 'Character', url: 'characters/forksplit.html' },
  { title: 'GRIT', type: 'Character', url: 'characters/grit.html' },
  { title: 'Grit42', type: 'Character', url: 'characters/grit42.html' },
  { title: 'HEX-TAGGER PRIME', type: 'Character', url: 'characters/hex-tagger-prime.html' },
  { title: 'Iris-7', type: 'Character', url: 'characters/iris-7.html' },
  { title: 'Jodie ZOOM 2000', type: 'Character', url: 'characters/jodie-zoom.html' },
  { title: 'Lady-INK', type: 'Character', url: 'characters/lady-ink.html' },
  { title: 'Loopfiend', type: 'Character', url: 'characters/loopfiend.html' },
  { title: 'M1NTR-K1LL', type: 'Character', url: 'characters/m1ntr-k1ll.html' },
  { title: 'NULL THE PROPHET', type: 'Character', url: 'characters/null-the-prophet.html' },
  { title: 'Patchwork', type: 'Character', url: 'characters/patchwork.html' },
  { title: 'PYRALITH', type: 'Character', url: 'characters/pyralith.html' },
  { title: 'Queen Sarah P-fly', type: 'Character', url: 'characters/queen-sarah-pfly.html' },
  { title: 'Quell', type: 'Character', url: 'characters/quell.html' },
  { title: 'Rune Tag', type: 'Character', url: 'characters/rune-tag.html' },
  { title: 'Samael.exe', type: 'Character', url: 'characters/samael-exe.html' },
  { title: 'SatoRebel', type: 'Character', url: 'characters/satorebel.html' },
  { title: 'Sister Halcyon', type: 'Character', url: 'characters/sister-halcyon.html' },
  { title: 'Snipey D-Man', type: 'Character', url: 'characters/snipey-d-man.html' },
  { title: 'The Princess', type: 'Character', url: 'characters/the-princess.html' },
  { title: 'The Whitewasher', type: 'Character', url: 'characters/whitewasher.html' },
  { title: 'Thera-9', type: 'Character', url: 'characters/thera-9.html' },
  { title: 'Thorne Architect', type: 'Character', url: 'characters/thorne-architect.html' },

  { title: 'Bitcoin Kid Army', type: 'Faction', url: 'factions/bitcoin-kid-army.html' },
  { title: 'GKniftyHEADS', type: 'Faction', url: 'factions/gkniftyheads.html' },
  { title: 'GRAFFPUNKS', type: 'Faction', url: 'factions/graffpunks.html' },
  { title: 'HODLWARRIORS', type: 'Faction', url: 'factions/hodlwarriors.html' },
  { title: 'NoBallGames Legion', type: 'Faction', url: 'factions/no-ball-games-legion.html' },
  { title: 'Crypto Moongirls Eternal', type: 'Faction', url: 'factions/crypto-moongirls-eternal.html' },
  { title: 'Nomad Bears', type: 'Faction', url: 'factions/nomad-bears.html' },
  { title: 'House of Rackinsats Eternal', type: 'Faction', url: 'factions/house-of-rackinsats-eternal.html' },
];

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

    const basePath = getSearchBasePath();
    searchResults.innerHTML = matches.slice(0, 12).map(item =>
      `<a href="${basePath}${item.url}" class="search-result-item">
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
