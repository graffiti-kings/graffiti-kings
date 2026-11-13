// Dependency-free source checks for this GitHub Pages website.
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const home = 'https://graffitikings.com/';
const origin = new URL(home).origin;
const files = new Set();
const errors = [];

function visit(dir) {
  for (const entry of readdirSync(path.join(root, dir), { withFileTypes: true })) {
    if (entry.name === '.git' || entry.name === 'node_modules') continue;
    const file = path.posix.join(dir, entry.name);
    if (entry.isDirectory()) visit(file);
    else if (entry.isFile()) files.add(file);
  }
}
visit('.');

const read = (file) => readFileSync(path.join(root, file), 'utf8');
const publicPages = [...files].filter((file) => file.endsWith('.html') && file !== '_article-template.html' && file !== '404.html').sort();
const canonicalUrl = (file) => home + (file === 'index.html' ? '' : file.endsWith('/index.html') ? file.slice(0, -10) : file);
const ids = new Map();

function idsOf(file) {
  if (!ids.has(file)) {
    const matches = [...read(file).matchAll(/\bid\s*=\s*(["'])(.*?)\1/gi)].map((match) => match[2]);
    ids.set(file, new Set(matches));
  }
  return ids.get(file);
}

for (const file of publicPages) {
  const source = read(file);
  const expected = canonicalUrl(file);
  const canonicalTags = [...source.matchAll(/<link\b[^>]*\brel=["']canonical["'][^>]*>/gi)];
  if (canonicalTags.length !== 1 || !canonicalTags[0][0].includes('href="' + expected + '"')) {
    errors.push(file + ': expected exactly one canonical URL ' + expected);
  }
  if (!/<title\b[^>]*>[^<]+<\/title>/i.test(source)) errors.push(file + ': missing page title');
  if (!/<meta\b[^>]*name=["']description["']/i.test(source)) errors.push(file + ': missing description');

  for (const match of source.matchAll(/\b(?:href|src|poster)\s*=\s*(["'])(.*?)\1/gi)) {
    const value = match[2].trim();
    if (!value || value === '#' || /^(mailto:|tel:|javascript:|data:)/i.test(value)) continue;
    let url;
    try { url = new URL(value, home + file); }
    catch { errors.push(file + ': malformed URL ' + value); continue; }
    if (url.origin !== origin) continue;
    let target;
    try { target = decodeURIComponent(url.pathname.slice(1)); }
    catch { errors.push(file + ': malformed URL encoding ' + value); continue; }
    if (!target || target.endsWith('/')) target += 'index.html';
    if (!files.has(target)) {
      errors.push(file + ': missing local target ' + value + ' (' + target + ')');
      continue;
    }
    if (url.hash && target.endsWith('.html')) {
      let fragment;
      try { fragment = decodeURIComponent(url.hash.slice(1)); }
      catch { errors.push(file + ': invalid fragment ' + value); continue; }
      if (fragment && !idsOf(target).has(fragment)) errors.push(file + ': missing anchor ' + value);
    }
  }
}

if (!existsSync(path.join(root, 'CNAME')) || read('CNAME').trim() !== 'graffitikings.com') {
  errors.push('CNAME must equal graffitikings.com');
}
if (!files.has('sitemap.xml')) errors.push('missing sitemap.xml');
else {
  const urls = [...read('sitemap.xml').matchAll(/<loc>(.*?)<\/loc>/g)].map((match) => match[1]);
  if (urls.length !== publicPages.length || new Set(urls).size !== urls.length) errors.push('sitemap has missing/duplicate entries');
  for (const page of publicPages) {
    if (!urls.includes(canonicalUrl(page))) errors.push('missing sitemap entry: ' + page);
  }
}
if (!files.has('robots.txt') || !read('robots.txt').includes(home + 'sitemap.xml')) {
  errors.push('robots.txt must advertise the canonical sitemap');
}

const searchIndex = [...read('js/main.js').matchAll(/\burl:\s*'([^']+)'/g)].map((match) => match[1]);
for (const file of searchIndex) {
  if (!files.has(file)) errors.push('search index missing target: ' + file);
}

if (errors.length) {
  for (const error of errors) console.error('ERROR:', error);
  console.error(errors.length + ' site audit error(s)');
  process.exitCode = 1;
} else {
  console.log('Site audit passed: ' + publicPages.length + ' pages, ' + searchIndex.length + ' search entries, canonical URLs, local links, anchors and sitemap checked.');
}
