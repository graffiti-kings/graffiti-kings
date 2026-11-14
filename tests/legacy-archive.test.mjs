import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const read = (file) => readFileSync(new URL('../' + file, import.meta.url), 'utf8');
const hubPath = 'pages/graffiti-kings-original-website-archive.html';
const workPath = 'pages/graffiti-kings-legacy-campaigns.html';
const hub = read(hubPath);
const work = read(workPath);

const captures = [
  'https://web.archive.org/web/20191208235829/https://graffitikings.co.uk/',
  'https://web.archive.org/web/20191122122032/https://graffitikings.co.uk/work/',
  'https://web.archive.org/web/20200926042053/https://graffitikings.co.uk/work/',
  'https://web.archive.org/web/20191209000718/https://graffitikings.co.uk/work/stefflon-don/',
  'https://web.archive.org/web/20191122122008/https://graffitikings.co.uk/work/jack-daniels/',
  'https://web.archive.org/web/20191122133602/https://graffitikings.co.uk/work/marvel-studios/',
  'https://web.archive.org/web/20191122125121/https://graffitikings.co.uk/work/game-of-thrones/'
];

test('historic page links retain the original timestamped Wayback addresses', () => {
  for (const url of captures.slice(0, 3)) assert.ok(hub.includes(url), 'missing archive hub link: ' + url);
  for (const url of captures.slice(3)) assert.ok(work.includes(url), 'missing project source: ' + url);
  assert.match(hub, /Wayback captures|Wayback snapshots/);
  assert.match(work, /Stefflon Don/);
  assert.match(work, /Jack Daniel/);
  assert.match(work, /Marvel Studios/);
  assert.match(work, /Game of Thrones/);
});

test('legacy pages use distinct self canonicals and accessible page structure', () => {
  for (const [file, html] of [[hubPath, hub], [workPath, work]]) {
    const canonical = 'https://graffitikings.com/' + file;
    assert.ok(html.includes('<link rel="canonical" href="' + canonical + '">'));
    assert.equal([...html.matchAll(/<h1\b/gi)].length, 1);
    assert.ok(html.includes('<main class="content-wrapper">'));
    assert.ok(html.includes('rel="noopener noreferrer"'));
    assert.ok(html.includes('<script type="application/ld+json">'));
    assert.ok(html.includes('../js/main.js'));
  }
});

test('original archives are findable from the main wiki and both existing source directories', () => {
  for (const file of ['index.html','about.html','history.html','pages/graffiti-kings-web-network.html']) {
    const text = read(file);
    assert.ok(text.includes('graffiti-kings-original-website-archive.html'), file + ' missing legacy link');
    assert.ok(text.includes('graffiti-kings-legacy-campaigns.html'), file + ' missing project link');
  }
  const js = read('js/main.js');
  assert.ok(js.includes("pages/graffiti-kings-original-website-archive.html"));
  assert.ok(js.includes("pages/graffiti-kings-legacy-campaigns.html"));
  const sitemap = read('sitemap.xml');
  for (const file of [hubPath, workPath]) assert.ok(sitemap.includes('https://graffitikings.com/' + file));
});

test('provenance and present-day business status are qualified', () => {
  assert.match(hub, /not a booking website/i);
  assert.match(work, /not.*present-day endorsements/i);
  assert.match(read('docs/legacy-archive-source-register.md'), /not freshly verified/);
});
