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
if (hamburger) {
  hamburger.addEventListener('click', () => {
    siteHeader.classList.toggle('nav-open');
    hamburger.classList.toggle('active');
  });
}

// Search functionality
const searchInput = document.querySelector('.search-input');
const searchResults = document.querySelector('.search-results');

// All pages index for search
const siteIndex = [
  { title: 'Darren Cullen (SER)', type: 'Person', url: 'characters/darren-cullen.html' },
  { title: 'Sarah PU51FLY', type: 'Person', url: 'characters/sarah-pu51fly.html' },
  { title: 'Charlie Buster', type: 'Person', url: 'characters/charlie-buster.html' },
  { title: 'Alfie "The Bitcoin Kid" Blaze', type: 'Character', url: 'characters/alfie-bitcoin-kid.html' },
  { title: 'Queen Sarah P-fly', type: 'Character', url: 'characters/queen-sarah-pfly.html' },
  { title: 'NULL THE PROPHET', type: 'Character', url: 'characters/null-the-prophet.html' },
  { title: 'Elder Codex-7', type: 'Character', url: 'characters/elder-codex-7.html' },
  { title: 'Thera-9', type: 'Character', url: 'characters/thera-9.html' },
  { title: 'The Bitcoin Kid Army', type: 'Faction', url: 'factions/bitcoin-kid-army.html' },
  { title: 'The GKniftyHEADS', type: 'Faction', url: 'factions/gkniftyheads.html' },
  { title: 'The Nomad Bears', type: 'Faction', url: 'factions/nomad-bears.html' },
  { title: 'The AllCity Bulls', type: 'Faction', url: 'factions/allcity-bulls.html' },
  { title: 'The GRAFFPUNKS', type: 'Faction', url: 'factions/graffpunks.html' },
  { title: 'The BALLY BOYS', type: 'Faction', url: 'factions/bally-boys.html' },
  { title: 'The CRYPTO MOONGIRLS', type: 'Faction', url: 'factions/crypto-moongirls.html' },
  { title: 'The DUCKY BOYS', type: 'Faction', url: 'factions/ducky-boys.html' },
  { title: 'The BLOCKCHAIN FURIES', type: 'Faction', url: 'factions/blockchain-furies.html' },
  { title: 'About', type: 'Page', url: 'about.html' },
  { title: 'History & Timeline', type: 'Page', url: 'history.html' },
  { title: 'Mechanics & Rewards', type: 'Page', url: 'pages/mechanics.html' },
  { title: 'Music & Radio', type: 'Page', url: 'pages/music.html' },
  { title: 'NFT Collections', type: 'Page', url: 'pages/nft-collections.html' },
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
    searchResults.innerHTML = matches.slice(0, 8).map(item =>
      `<a href="${item.url}" class="search-result-item">
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
