// Read-only external link audit. HTTP blocks/timeouts are unverified, not dead.
import fs from 'node:fs';
import path from 'node:path';
const references = new Map();
function visit(dir = '.') {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name.startsWith('.') || entry.name === 'node_modules') continue;
    const file = path.posix.join(dir, entry.name);
    if (entry.isDirectory()) visit(file);
    else if (file.endsWith('.html') && !entry.name.startsWith('_')) {
      for (const match of fs.readFileSync(file, 'utf8').matchAll(/<a\b[^>]*\bhref=["'](https?:\/\/[^"']+)["']/g)) {
        const url = new URL(match[1].replace(/&amp;/g, '&'));
        if (url.hostname === 'graffitikings.com' || url.hostname === 'www.graffitikings.com') continue;
        url.hash = '';
        const key = url.toString();
        if (!references.has(key)) references.set(key, new Set());
        references.get(key).add(file);
      }
    }
  }
}
visit();
const targets = [...references];
const results = [];
let next = 0;
async function worker() {
  while (next < targets.length) {
    const [url, pages] = targets[next++];
    let record = { url, pages: [...pages] };
    try {
      let response = await fetch(url, { redirect: 'follow', signal: AbortSignal.timeout(12000) });
      // Confirm permanent failures once; do not turn access blocks into broken links.
      if ([404, 410].includes(response.status)) {
        await response.body?.cancel();
        response = await fetch(url, { redirect: 'follow', signal: AbortSignal.timeout(12000) });
      }
      record.status = response.status;
      record.finalURL = response.url;
      record.result = response.ok ? 'reachable' : [404, 410].includes(response.status) ? 'missing' : 'unverified';
      await response.body?.cancel();
    } catch (error) { record.result = 'unverified'; record.error = error.message; }
    results.push(record);
    if (record.result === 'missing') console.log('MISSING', record.status, url);
    if (results.length % 25 === 0) console.log('Checked', results.length, 'of', targets.length);
  }
}
await Promise.all(Array.from({length: 4}, worker));
const summary = Object.fromEntries(['reachable', 'missing', 'unverified'].map(key => [key, results.filter(item => item.result === key).length]));
const report = { checkedAt: new Date().toISOString(), summary, links: results.sort((a, b) => a.url.localeCompare(b.url)) };
const output = process.argv[2] || 'docs/external-link-audit.json';
fs.writeFileSync(output, JSON.stringify(report, null, 2) + '\n');
console.log('External link audit:', JSON.stringify(summary), '→', output);
