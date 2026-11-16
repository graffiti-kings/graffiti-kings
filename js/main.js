// Graffiti Kings Wiki — shared site script

const siteIndex = [
  { title: 'Home', type: 'Page', url: 'index.html' },
  { title: 'About', type: 'Page', url: 'about.html' },
  { title: 'History & Timeline', type: 'Page', url: 'history.html' },
  { title: 'Characters', type: 'Directory', url: 'characters/index.html' },
  { title: 'Factions and armies', type: 'Directory', url: 'factions/index.html' },
  { title: 'Mechanics', type: 'Page', url: 'pages/mechanics.html' },
  { title: 'Music', type: 'Page', url: 'pages/music.html' },
  { title: 'NFT Collections', type: 'Page', url: 'pages/nft-collections.html' },
  { title: 'WAXP Graffiti Kings Blockchain Native Coin NFT Guide', type: 'Guide', url: 'pages/waxp.html' },
  { title: 'Submit Lore', type: 'Page', url: 'pages/submit-lore.html' },
  { title: 'Charlie Buster: Grime Art and Saatchi original works', type: 'Archive', url: 'pages/charlie-buster-grime-art-history.html' },
  { title: 'Charlie Buster NO BALL GAMES NBG WAX XRP KIDs', type: 'Archive', url: 'pages/charlie-buster-no-ball-games-nbg.html' },
  { title: 'Charlie Buster TREEF Project and Regeneration', type: 'Archive', url: 'pages/charlie-buster-treef-project.html' },
  { title: 'Charlie Buster Artist Press Web Source Network', type: 'Archive', url: 'pages/charlie-buster-source-network.html' },
  { title: 'Darren Cullen SER Documented History', type: 'Archive', url: 'pages/darren-cullen-ser-history.html' },
  { title: 'Graffiti Kings Press Web and Social Sources', type: 'Archive', url: 'pages/graffiti-kings-web-network.html' },
  { title: 'Original Graffiti Kings 2019 Website Wayback Archive Services', type: 'Archive', url: 'pages/graffiti-kings-original-website-archive.html' },
  { title: 'Graffiti Kings Historic Marvel Jack Daniels Stefflon Don Campaigns', type: 'Archive', url: 'pages/graffiti-kings-legacy-campaigns.html' },
  { title: 'Graffiti Queens Decentraland 2021 Exhibition', type: 'Archive', url: 'pages/graffiti-queens-decentraland-2021.html' },
  { title: 'Graffiti Kings WAX NFT Collections', type: 'Archive', url: 'pages/graffiti-kings-wax-nft-collections.html' },
  { title: 'Graffiti Queens Second NFT Art Festival 2022', type: 'Archive', url: 'pages/graffiti-queens-nft-festival-2022.html' },
  { title: 'Graffiti Kings Web3 Partnerships SYNC Alien Worlds', type: 'Archive', url: 'pages/graffiti-kings-web3-partnerships.html' },
  { title: 'Crypto Moonboys GKniftyHEADS GraffPUNKS Connected Network', type: 'Archive', url: 'pages/crypto-moonboys-gkniftyheads-network.html' },
  { title: 'Bitcoin Kid Invasion Toys Vinyl NFT Archive', type: 'Archive', url: 'pages/bitcoin-kid-invasion-toys-archive.html' },
  { title: 'Darren Cullen SER', type: 'Person', url: 'characters/darren-cullen.html' },
  { title: 'Sarah PU51FLY', type: 'Person', url: 'characters/sarah-pu51fly.html' },
  { title: 'Charlie Buster', type: 'Person', url: 'characters/charlie-buster.html' },
  { title: 'Alfie The Bitcoin KiD Blaze', type: 'Character', url: 'characters/alfie-bitcoin-kid.html' },
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
  { title: 'Ava Chen investigative journalist', type: 'Character', url: 'characters/ava-chen.html' },
  { title: 'All City Bulls AllCity Bulls', type: 'Faction', url: 'factions/all-city-bulls.html' },
  { title: 'HODL X Warriors', type: 'City order', url: 'factions/hodl-x-warriors.html' },
  { title: 'GKniftyHEADS', type: 'Faction', url: 'factions/gkniftyheads.html' },
  { title: 'GraffPUNKS', type: 'Faction', url: 'factions/graffpunks.html' },
  { title: 'HODL Warriors', type: 'Army', url: 'factions/hodlwarriors.html' },
  { title: 'NoBallGames Legion', type: 'Culture', url: 'factions/no-ball-games-legion.html' },
  { title: 'Crypto Moongirls', type: 'Army', url: 'factions/crypto-moongirls-eternal.html' },
  { title: 'Bitcoin Kid Army', type: 'Army', url: 'factions/bitcoin-kid-army.html' },
  { title: 'Nomad Bears', type: 'Faction', url: 'factions/nomad-bears.html' },
  { title: 'House of Rackinsats', type: 'Household', url: 'factions/house-of-rackinsats-eternal.html' },
  { title: 'Burn Crews', type: 'Subformation', url: 'factions/burn-crews.html' },
  { title: 'Stencil Witches', type: 'Subformation', url: 'factions/stencil-witches.html' },
  { title: 'Tag Lords', type: 'Subformation', url: 'factions/tag-lords.html' },
  { title: 'Brush Daughters', type: 'Archive tradition', url: 'factions/brush-daughters.html' },
  { title: 'Echo Mothers', type: 'Archive tradition', url: 'factions/echo-mothers.html' },
  { title: 'Wildstyle Collective', type: 'Culture', url: 'factions/wildstyle-collective.html' },
  { title: 'Fractal Taggers', type: 'Culture', url: 'factions/fractal-taggers.html' },
  { title: 'Porch Poets', type: 'Culture', url: 'factions/porch-poets.html' },
  { title: 'Deep Holders', type: 'Archive tradition', url: 'factions/deep-holders.html' },
  { title: 'Whale Lords Eternal', type: 'Culture', url: 'factions/whale-lords-eternal.html' },
  { title: 'HODL Layer Sentinels', type: 'Archive tradition', url: 'factions/hodl-layer-sentinels.html' },
  { title: 'Compound Believers', type: 'Archive tradition', url: 'factions/compound-believers.html' },
  { title: 'Genesis Anchors', type: 'Archive tradition', url: 'factions/genesis-anchors.html' },
  { title: 'Porch Accord Diplomats', type: 'Archive tradition', url: 'factions/porch-accord-diplomats.html' },
  { title: 'Belief Miners', type: 'Archive tradition', url: 'factions/belief-miners.html' },
  { title: 'Eternal Porch Keepers', type: 'Archive tradition', url: 'factions/eternal-porch-keepers.html' },
  { title: 'BinLords', type: 'Archive tradition', url: 'factions/binlords.html' },
  { title: 'Tag Rush Crew', type: 'Archive tradition', url: 'factions/tag-rush-crew.html' },
  { title: 'League of Keepers', type: 'Archive tradition', url: 'factions/league-of-keepers.html' },
  { title: 'Arcade Scribes', type: 'Archive tradition', url: 'factions/arcade-scribes.html' },
  { title: 'Quest Givers', type: 'Archive tradition', url: 'factions/quest-givers.html' },
  { title: 'Pixel Pushers', type: 'Archive tradition', url: 'factions/pixel-pushers.html' },
  { title: 'Level Lords', type: 'Archive tradition', url: 'factions/level-lords.html' },
  { title: 'Nomad Drip House', type: 'Archive tradition', url: 'factions/nomad-drip-house.html' },
  { title: 'Rackinsats Fashion House', type: 'Archive tradition', url: 'factions/rackinsats-fashion-house.html' },
  { title: 'Crypto Badgers', type: 'Archive tradition', url: 'factions/crypto-badgers.html' },
  { title: 'Mutant Pasteups', type: 'Archive tradition', url: 'factions/mutant-pasteups.html' },
  { title: 'Cross-Chain Couriers', type: 'Archive tradition', url: 'factions/cross-chain-couriers.html' },
  { title: 'Croydon Oracles', type: 'Archive tradition', url: 'factions/croydon-oracles.html' },
  { title: 'Grid Ghosts', type: 'Archive tradition', url: 'factions/grid-ghosts.html' },
  { title: 'Null Priests', type: 'Archive tradition', url: 'factions/null-priests.html' },
  { title: 'SAM Watchers', type: 'Archive tradition', url: 'factions/sam-watchers.html' },
  { title: 'Whitewall Remnants', type: 'Archive tradition', url: 'factions/whitewall-remnants.html' },
  { title: 'Lost Moonboys', type: 'Archive tradition', url: 'factions/lost-moonboys.html' },
  { title: 'The Unnamed Fortieth', type: 'Archive tradition', url: 'factions/the-unnamed-fortieth.html' }
];

function isNestedPage() {
  return /\/(characters|factions|pages)\//.test(window.location.pathname);
}
function prefixPath(url) { return isNestedPage() ? '../' + url : url; }

let indexPromise;
function loadSearchIndex() {
  if (window.GK_SEARCH_INDEX) return Promise.resolve(window.GK_SEARCH_INDEX);
  if (indexPromise) return indexPromise;
  indexPromise = new Promise((resolve, reject) => {
    const script = document.createElement('script');
    script.src = prefixPath('js/search-index.js');
    script.onload = () => {
      script.remove();
      if (Array.isArray(window.GK_SEARCH_INDEX)) resolve(window.GK_SEARCH_INDEX);
      else { indexPromise = null; reject(new Error('Search data unavailable')); }
    };
    script.onerror = () => { script.remove(); indexPromise = null; reject(new Error('Search data unavailable')); };
    document.head.appendChild(script);
  });
  return indexPromise;
}

function makeResult(item, fullPage = false) {
  const link = document.createElement('a');
  link.href = prefixPath(item.url);
  link.className = fullPage ? 'search-page-link' : 'search-result-item';
  const title = document.createElement(fullPage ? 'h2' : 'span');
  title.className = 'search-result-title';
  title.textContent = item.title;
  const type = document.createElement('span');
  type.className = 'search-result-type';
  type.textContent = item.type;
  link.append(title, type);
  if (fullPage) {
    const summary = document.createElement('p');
    summary.textContent = item.summary;
    link.append(summary);
  }
  return link;
}

let pageEvents;
let headerObserver;
let matrixStarted = false;

function bindSearch() {
  const form = document.querySelector('.search-container');
  const input = form?.querySelector('.search-input');
  const results = form?.querySelector('.search-results');
  const status = form?.querySelector('.search-status');
  if (!input || !results) return;
  let version = 0;
  function close() {
    version++;
    results.hidden = true;
  }
  async function update() {
    const request = ++version;
    const query = input.value.trim();
    if (window.GKSearch.normalize(query).length < 2) { close(); status.textContent = ''; return; }
    status.textContent = 'Searching the wiki…';
    try {
      const index = await loadSearchIndex();
      if (request !== version) return;
      const matches = window.GKSearch.search(index, query);
      results.replaceChildren();
      const count = document.createElement('p');
      count.className = 'search-result-count';
      count.textContent = matches.length ? `${matches.length} matching ${matches.length === 1 ? 'page' : 'pages'}` : 'No matching pages. Try a name, topic or different spelling.';
      results.append(count);
      matches.slice(0, 6).forEach(item => results.append(makeResult(item)));
      if (matches.length) {
        const all = document.createElement('a');
        all.className = 'search-all';
        all.href = prefixPath('search.html') + '?q=' + encodeURIComponent(query);
        all.textContent = `View all ${matches.length} results →`;
        results.append(all);
      }
      status.textContent = count.textContent;
      results.hidden = false;
    } catch {
      if (request !== version) return;
      results.replaceChildren();
      const message = document.createElement('p');
      message.className = 'search-result-count';
      message.textContent = 'Search could not load. Check your connection and try again.';
      results.append(message);
      status.textContent = message.textContent;
      results.hidden = false;
    }
  }
  input.addEventListener('input', update);
  input.addEventListener('focus', () => {
    // Lazy-load 103+ article texts only when the visitor uses search.
    loadSearchIndex().catch(() => {});
    if (input.value.trim().length >= 2) update();
  });
  input.addEventListener('keydown', event => {
    if (event.key === 'ArrowDown' && !results.hidden) {
      const first = results.querySelector('a');
      if (first) { event.preventDefault(); first.focus(); }
    }
    if (event.key === 'Escape') close();
  });
  results.addEventListener('keydown', event => {
    const links = [...results.querySelectorAll('a')];
    const position = links.indexOf(document.activeElement);
    if (event.key === 'Escape') { event.preventDefault(); input.focus(); close(); }
    if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
      event.preventDefault();
      const next = position + (event.key === 'ArrowDown' ? 1 : -1);
      if (next < 0) input.focus();
      else links[Math.min(next, links.length - 1)]?.focus();
    }
  });
  document.addEventListener('click', event => { if (!form.contains(event.target)) close(); }, { signal: pageEvents.signal });
  form.addEventListener('focusout', event => { if (!form.contains(event.relatedTarget)) close(); });
}

async function initSearchPage() {
  const form = document.getElementById('wiki-search-form');
  if (!form) return;
  const input = form.querySelector('input');
  const status = document.getElementById('wiki-search-status');
  const list = document.getElementById('wiki-search-results');
  const query = new URLSearchParams(window.location.search).get('q') || '';
  input.value = query;
  try {
    const index = await loadSearchIndex();
    const matches = query.trim() ? window.GKSearch.search(index, query) : index;
    status.textContent = query.trim() ? `${matches.length} ${matches.length === 1 ? 'result' : 'results'} for “${query}”` : `Browse all ${index.length} pages, or search by name or topic.`;
    if (query.trim() && window.GKSearch.normalize(query).length < 2) status.textContent = 'Enter at least two letters or numbers to search.';
    else if (!matches.length) status.textContent += '. Try a different spelling or a broader topic.';
    list.replaceChildren();
    matches.forEach(item => {
      const row = document.createElement('li');
      row.append(makeResult(item, true));
      list.append(row);
    });
  } catch {
    status.textContent = 'Search could not load. Check your connection, then reload this page. You can also browse Characters or Factions from the navigation.';
  }
}

function initNavigation() {
  document.documentElement.classList.add('js-enabled');
  const header = document.querySelector('.site-header');
  const button = header?.querySelector('.hamburger');
  if (!header || !button) return;
  const close = () => {
    header.classList.remove('nav-open');
    button.setAttribute('aria-expanded', 'false');
  };
  button.addEventListener('click', () => {
    const open = header.classList.toggle('nav-open');
    button.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && header.classList.contains('nav-open')) {
      close(); button.focus();
    }
  }, { signal: pageEvents.signal });
  document.addEventListener('click', event => { if (!header.contains(event.target)) close(); }, { signal: pageEvents.signal });
  const updateHeight = () => document.documentElement.style.setProperty('--header-height', header.offsetHeight + 'px');
  if (window.ResizeObserver) { headerObserver = new ResizeObserver(updateHeight); headerObserver.observe(header); }
  updateHeight();
  window.matchMedia('(min-width: 1201px)').addEventListener('change', close, { signal: pageEvents.signal });
}

function initMatrix() {
  const canvas = document.getElementById('matrixCanvas');
  const ctx = canvas?.getContext('2d');
  if (!ctx || matrixStarted) return;
  matrixStarted = true;
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const chars = Array.from('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$₿⚡🎨');
  const fontSize = 14;
  let drops = [];
  let frame = 0;
  let previous = 0;
  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    drops = Array(Math.ceil(canvas.width / fontSize)).fill(1);
  }
  function draw(time) {
    if (document.hidden || motion.matches) { frame = 0; return; }
    if (time - previous >= 50) {
      previous = time;
      ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = '#FFD700';
      ctx.font = fontSize + 'px monospace';
      drops.forEach((y, i) => {
        ctx.fillText(chars[Math.floor(Math.random() * chars.length)], i * fontSize, y * fontSize);
        if (y * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
        drops[i]++;
      });
    }
    frame = window.requestAnimationFrame(draw);
  }
  function sync() {
    window.cancelAnimationFrame(frame);
    frame = 0;
    if (motion.matches) ctx.clearRect(0, 0, canvas.width, canvas.height);
    if (!document.hidden && !motion.matches) frame = window.requestAnimationFrame(draw);
  }
  resize(); sync();
  window.addEventListener('resize', resize);
  document.addEventListener('visibilitychange', sync);
  motion.addEventListener('change', sync);
}

function initGKWiki() {
  pageEvents?.abort();
  headerObserver?.disconnect();
  pageEvents = new AbortController();
  initNavigation();
  bindSearch();
  initSearchPage();
  initMatrix();
}
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initGKWiki, { once: true });
else initGKWiki();
