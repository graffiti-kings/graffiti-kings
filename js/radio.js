// A single audio element survives internal navigation. No autoplay or volume UI.
(() => {
  const audio = document.createElement('audio');
  audio.id = 'gk-radio';
  audio.preload = 'none';
  audio.hidden = true;
  document.body.append(audio);
  const notice = document.createElement('div');
  notice.className = 'radio-notice';
  notice.setAttribute('role', 'status');
  notice.hidden = true;
  document.body.append(notice);
  let wanted = false, managed = false, generation = 0, navigation;
  function sync(state) {
    document.querySelectorAll('.nav-radio').forEach(button => {
      button.setAttribute('aria-pressed', String(wanted));
      button.setAttribute('aria-label', wanted ? 'Turn GraffPUNKS Radio off' : 'Turn GraffPUNKS Radio on');
      button.querySelector('.radio-state').textContent = state || (wanted ? 'ON' : 'OFF');
    });
  }
  function off(message) {
    wanted = false; generation++;
    audio.pause(); audio.removeAttribute('src'); audio.load();
    sync(); notice.textContent = message || ''; notice.hidden = !message;
  }
  document.addEventListener('click', event => {
    const button = event.target.closest('.nav-radio');
    if (!button) return;
    if (wanted) { off(); return; }
    wanted = true;
    const attempt = ++generation;
    notice.hidden = true; sync('…');
    audio.src = 'https://api.cryptomoonboys.com/radio/stream';
    audio.play().then(() => {
      if (attempt !== generation) return;
      managed = true; sync();
    }).catch(() => { if (attempt === generation) off('Radio unavailable. Tap Radio to retry.'); });
  });
  audio.addEventListener('playing', () => { if (wanted) sync(); });
  audio.addEventListener('waiting', () => { if (wanted) sync('…'); });
  audio.addEventListener('error', () => { if (wanted) off('Radio connection lost. Tap Radio to retry.'); });

  async function navigate(url, push) {
    navigation?.abort();
    const controller = new AbortController(); navigation = controller;
    try {
      const response = await fetch(url, { signal: controller.signal });
      if (!response.ok || new URL(response.url).origin !== location.origin) throw new Error('Navigation unavailable');
      const doc = new DOMParser().parseFromString(await response.text(), 'text/html');
      const wrapper = doc.querySelector('.site-wrapper');
      if (!wrapper || !doc.querySelector('.site-header')) throw new Error('Not a wiki page');
      if (controller.signal.aborted) return;
      if (push) history.pushState(null, '', url);
      document.title = doc.title;
      document.head.querySelectorAll('style, meta, link[rel="canonical"], script[type="application/ld+json"]').forEach(node => node.remove());
      doc.head.querySelectorAll('style, meta, link[rel="canonical"], script[type="application/ld+json"]').forEach(node => document.head.append(document.importNode(node, true)));
      document.body.className = doc.body.className;
      if (!document.getElementById('matrixCanvas') && doc.getElementById('matrixCanvas')) document.body.prepend(document.importNode(doc.getElementById('matrixCanvas'), true));
      // Scripts are deliberately not inserted/executed. Shared modules stay alive.
      wrapper.querySelectorAll('script').forEach(node => node.remove());
      document.querySelector('.site-wrapper').replaceWith(document.importNode(wrapper, true));
      initGKWiki(); sync();
      const target = url.hash ? document.getElementById(decodeURIComponent(url.hash.slice(1))) : null;
      if (target) target.scrollIntoView(); else window.scrollTo(0, 0);
      document.getElementById('main-content')?.focus({ preventScroll: true });
    } catch (error) {
      if (error.name === 'AbortError') return;
      notice.textContent = 'Page could not load. Your radio is still available; try the link again.';
      notice.hidden = false;
    }
  }
  document.addEventListener('click', event => {
    if (!managed && !wanted) return;
    if (event.defaultPrevented || event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    const link = event.target.closest('a[href]');
    if (!link || link.hasAttribute('download') || (link.target && link.target !== '_self')) return;
    const url = new URL(link.href);
    if (!/^https?:$/.test(url.protocol)) return;
    if (url.origin !== location.origin) {
      if (wanted) { event.preventDefault(); window.open(url.href, '_blank', 'noopener'); }
      return;
    }
    if (!url.pathname.endsWith('.html') && !url.pathname.endsWith('/')) return;
    if (url.pathname === location.pathname && url.search === location.search && url.hash) return;
    event.preventDefault(); navigate(url, true);
  });
  document.addEventListener('submit', event => {
    if (!managed && !wanted) return;
    const form = event.target;
    if (!form.matches('.search-container, #wiki-search-form')) return;
    event.preventDefault();
    const url = new URL(form.action); url.search = new URLSearchParams(new FormData(form)).toString();
    navigate(url, true);
  });
  window.addEventListener('popstate', () => { if (managed || wanted) navigate(new URL(location.href), false); });
  sync();
})();
