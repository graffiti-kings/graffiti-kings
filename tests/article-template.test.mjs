import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';

const template = fs.readFileSync('_article-template.html', 'utf8');
const header = template.match(/<header class="site-header">([\s\S]*?)<\/header>/)[1];

test('copied article templates resolve navigation and search from every supported directory', () => {
  for (const directory of ['pages', 'characters', 'factions']) {
    const base = new URL(`https://graffitikings.com/${directory}/new-article.html`);
    for (const [, attribute, value] of header.matchAll(/\b(href|action)="([^"]+)"/g)) {
      const url = new URL(value, base);
      assert.equal(url.origin, base.origin);
      assert.ok(fs.existsSync(path.join(process.cwd(), url.pathname.slice(1))), `${directory}: broken ${attribute} ${value}`);
    }
    assert.equal(new URL(header.match(/class="search-container" action="([^"]+)"/)[1], base).pathname, '/search.html');
    assert.equal(new URL(header.match(/<a href="([^"]+)" class="logo-link"/)[1], base).pathname, '/index.html');
  }
});

test('article templates load the search API before its consumers', () => {
  const scripts = [...template.matchAll(/<script\b[^>]*src="([^"]+)"/g)].map(match => match[1]);
  assert.ok(scripts.includes('../js/search.js'));
  assert.ok(scripts.indexOf('../js/search.js') < scripts.indexOf('../js/main.js'));
});
