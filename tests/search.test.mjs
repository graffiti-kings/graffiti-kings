import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { createRequire } from 'node:module';
const { search } = createRequire(import.meta.url)('../js/search.js');
const index = JSON.parse(fs.readFileSync('js/search-index.js', 'utf8').match(/window.GK_SEARCH_INDEX = ([\s\S]*);\s*$/)[1]);

test('aliases find the real Sarah profile while retaining her fictional role separately', () => {
  for (const name of ['PFLY', 'P-fly', 'PU51FLY', 'Sarah Wadmore']) {
    assert.ok(search(index, name).some(item => item.url === 'characters/sarah-pu51fly.html'), name);
  }
  assert.equal(search(index, 'Queen Sarah P-fly')[0].url, 'characters/queen-sarah-pfly.html');
});
test('body text and summaries are searched even without the phrase in the title', () => {
  assert.ok(search(index, 'Wallington').some(item => item.url === 'about.html'));
  assert.ok(search(index, 'pirate radio').some(item => item.url === 'about.html'));
});
test('all matching pages are returned, with no silent twelve-result ceiling', () => {
  assert.ok(search(index, 'the').length > 12);
});
test('empty, very short, unmatched and HTML-like queries are harmless', () => {
  for (const q of ['', ' ', 'a', 'zzznomatch123456789', '<script>alert(1)</script>']) assert.deepEqual(search(index, q), []);
});
test('exact titles beat incidental mentions and punctuation is normalized', () => {
  assert.equal(search(index, 'Darren Cullen / SER')[0].url, 'characters/darren-cullen.html');
  assert.ok(search(index, 'HODL X Warriors').some(item => item.url === 'factions/hodl-x-warriors.html'));
});
