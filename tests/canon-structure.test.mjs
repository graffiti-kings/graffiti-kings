import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';

const read = p => readFileSync(new URL('../' + p, import.meta.url), 'utf8');
const article = p => read(p).match(/<article class="main-content">([\s\S]*?)<\/article>/)[1];
const text = p => article(p).replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ');
const search = [...read('js/main.js').matchAll(/\{ title: '([^']*)', type: '([^']*)', url: '([^']*)' \}/g)]
  .map(([, title, type, url]) => ({title, type, url}));

test('search distinguishes military service from political faction membership', () => {
  for (const [slug, type] of [
    ['bitcoin-kid-army', 'Army'], ['hodlwarriors', 'Army'],
    ['hodl-x-warriors', 'City order'], ['crypto-moongirls-eternal', 'Army'],
    ['all-city-bulls', 'Faction'], ['nomad-bears', 'Faction'], ['gkniftyheads', 'Faction']
  ]) {
    const matches = search.filter(e => e.url === 'factions/' + slug + '.html');
    assert.equal(matches.length, 1, slug + ' must have one search result');
    assert.equal(matches[0].type, type, slug + ' has the wrong entity type');
  }
});

test('market protection and all-faction mobilisation keep their different command roles', () => {
  const army = text('factions/bitcoin-kid-army.html');
  assert.match(army, /24\/7/);
  assert.match(army, /orders\s+only from GKniftyHEADS/i);
  assert.match(army, /not an additional GK street faction/i);
  const united = text('factions/hodlwarriors.html');
  assert.match(united, /members of\s+all GK factions/i);
  assert.match(united, /keep their original faction identities/i);
  assert.match(united, /not a faction/i);
  assert.match(united, /aspires to become a\s+HODL X Warrior/i);
});

test('both market factions and both HODL forces are reachable from the directory', () => {
  const directory = article('factions/index.html');
  for (const slug of ['all-city-bulls', 'nomad-bears', 'bitcoin-kid-army', 'hodlwarriors', 'hodl-x-warriors']) {
    assert.ok(directory.includes('href="' + slug + '.html"'), slug + ' is missing');
  }
  assert.doesNotMatch(directory, /THE COMPLETE 40 FACTIONS/);
  assert.match(text('factions/hodl-x-warriors.html'), /Queen Sarah P-fly/);
  assert.match(text('factions/hodl-x-warriors.html'), /not prove that both have always belonged to the same order/);
});

test('real-root profiles are separate from the fictional Queen and the two Grit characters', () => {
  assert.equal(search.find(e => e.url === 'characters/sarah-pu51fly.html').type, 'Person');
  assert.equal(search.find(e => e.url === 'characters/queen-sarah-pfly.html').type, 'Character');
  assert.match(article('characters/sarah-pu51fly.html'), /href="queen-sarah-pfly.html"/);
  assert.match(text('characters/grit.html'), /female/);
  assert.match(text('characters/grit42.html'), /distinct from GRIT/i);
});

test('the central entrances link the current source hierarchy and leave the ending unresolved', () => {
  for (const page of ['index.html', 'about.html', 'history.html', 'pages/submit-lore.html']) {
    const body = article(page);
    assert.ok(body.includes('https://cryptomoonboys.com/wiki/crypto-moonboys.html'), page);
    assert.match(text(page), /Final Fork[\s\S]{0,100}unresolved|unresolved[\s\S]{0,100}Final Fork/i, page);
  }
});
