// Shared, dependency-free search logic for the header and full results page.
(function (root) {
  function normalize(value) {
    return String(value || '').normalize('NFKD').replace(/[\u0300-\u036f]/g, '')
      .toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  }

  function search(index, query) {
    const phrase = normalize(query);
    if (phrase.length < 2) return [];
    const words = phrase.split(/\s+/);
    return index.map((item) => {
      const title = normalize(item.title);
      const aliases = normalize((item.aliases || []).join(' '));
      const summary = normalize(item.summary);
      const body = normalize(item.text);
      const combined = [title, aliases, summary, body, normalize(item.type)].join(' ');
      if (!words.every((word) => combined.includes(word))) return null;
      let score = title === phrase ? 200 : title.includes(phrase) ? 100 : 0;
      if (aliases.includes(phrase)) score += 65;
      if (summary.includes(phrase)) score += 30;
      for (const word of words) {
        if (title.includes(word)) score += 12;
        if (aliases.includes(word)) score += 8;
        if (summary.includes(word)) score += 3;
      }
      return { item, score };
    }).filter(Boolean).sort((a, b) => b.score - a.score || a.item.title.localeCompare(b.item.title))
      .map((match) => match.item);
  }

  const api = { normalize, search };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.GKSearch = api;
})(typeof window === 'undefined' ? globalThis : window);
