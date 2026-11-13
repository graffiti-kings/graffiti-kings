// Technical SEO assertions for the static Graffiti Kings website.
// Run with: node scripts/check-seo.mjs
import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const HOME = 'https://graffitikings.com/';
const SITE_NAME = 'Graffiti Kings Wiki';
const SOCIAL_IMAGE = HOME + 'images/GK_NIFTYHEADS_niftys.png';
const errors = [];
const warnings = [];
const pages = [];
const text = (p) => fs.readFileSync(path.join(ROOT, p), 'utf8');

function gather(dir = '.') {
  for (const entry of fs.readdirSync(path.join(ROOT, dir), { withFileTypes: true })) {
    if (entry.name === '.git' || entry.name === 'node_modules') continue;
    const p = path.posix.join(dir, entry.name);
    if (entry.isDirectory()) gather(p);
    else if (entry.isFile() && p.endsWith('.html') && p !== '_article-template.html' && p !== '404.html') pages.push(p);
  }
}
gather();
pages.sort();

const decode = (s) => s.replace(/&amp;/gi, '&').replace(/&quot;/gi, '"').replace(/&#39;|&apos;/gi, "'").replace(/&lt;/gi, '<').replace(/&gt;/gi, '>');
const urlFor = (p) => HOME + (p === 'index.html' ? '' : p.endsWith('/index.html') ? p.slice(0, -10) : p);
const seenTitles = new Map();
const seenDescriptions = new Map();
let imageCount = 0;
let breadcrumbCount = 0;

function attrs(markup) {
  const result = {};
  for (const m of markup.matchAll(/([a-zA-Z_:][\w:.-]*)\s*=\s*(["'])(.*?)\2/g)) result[m[1].toLowerCase()] = m[3];
  return result;
}

function getMeta(metas, type, key, file) {
  const found = metas.filter((m) => m[type] === key);
  if (found.length !== 1) errors.push(file + ': expected one ' + type + '=' + key + ' (got ' + found.length + ')');
  return decode(found[0]?.content || '');
}

function validatePNG(file, minSize, square = false) {
  if (!fs.existsSync(path.join(ROOT, file))) { errors.push('missing image: ' + file); return; }
  const data = fs.readFileSync(path.join(ROOT, file));
  if (data.length < 24 || data.subarray(0, 8).toString('hex') !== '89504e470d0a1a0a') {
    errors.push(file + ': invalid PNG');
    return;
  }
  const width = data.readUInt32BE(16), height = data.readUInt32BE(20);
  if (width < minSize || height < minSize) errors.push(file + ': image below ' + minSize + 'px (got ' + width + 'x' + height + ')');
  if (square && width !== height) errors.push(file + ': favicon must be square');
  console.log('Image check: ' + file + ' ' + width + 'x' + height + ' (' + Math.round(data.length / 1024) + ' KiB)');
}

for (const file of pages) {
  const html = text(file);
  const head = html.split(/<\/head>/i)[0];
  const url = urlFor(file);
  const metas = [...head.matchAll(/<meta\b[^>]*>/gi)].map((m) => attrs(m[0]));
  const titleTags = [...head.matchAll(/<title\b[^>]*>([\s\S]*?)<\/title>/gi)];
  if (titleTags.length !== 1) errors.push(file + ': expected exactly one page title');
  const title = decode(titleTags[0]?.[1]?.trim() || '');
  const description = getMeta(metas, 'name', 'description', file);
  if (!/<html\b[^>]*\blang=["']en(?:-GB)?["']/i.test(html)) errors.push(file + ': missing English document language');
  if (!title || title.length < 10) errors.push(file + ': missing or unusable title');
  if (!description || description.length < 35) errors.push(file + ': missing or unusable description');
  if (title.length > 75) warnings.push(file + ': title is long (' + title.length + ')');
  if (description.length < 80 || description.length > 185) warnings.push(file + ': description length ' + description.length);
  for (const [value, seen, type] of [[title, seenTitles, 'title'], [description, seenDescriptions, 'description']]) {
    const key = value.toLowerCase().replace(/\s+/g, ' ').trim();
    if (key && seen.has(key)) errors.push(file + ': duplicate ' + type + ' of ' + seen.get(key));
    else seen.set(key, file);
  }
  const canonical = [...head.matchAll(/<link\b[^>]*\brel=["']canonical["'][^>]*>/gi)];
  if (canonical.length !== 1 || attrs(canonical[0][0]).href !== url) errors.push(file + ': invalid canonical');
  const h1s = [...html.matchAll(/<h1\b/gi)].length;
  if (h1s !== 1) errors.push(file + ': expected one H1 (got ' + h1s + ')');
  const robots = metas.filter((m) => m.name === 'robots').map((m) => m.content.toLowerCase());
  if (robots.length !== 1 || robots[0].includes('noindex')) errors.push(file + ': indexable pages must have one non-noindex robots tag');
  if (!robots[0]?.includes('max-image-preview:large')) errors.push(file + ': large image preview permission missing');
  const expected = [
    ['og:type', 'website'], ['og:site_name', SITE_NAME], ['og:locale', 'en_GB'],
    ['og:url', url], ['og:title', title], ['og:description', description],
    ['og:image', SOCIAL_IMAGE], ['og:image:alt', 'GKniftyHEADS and Graffiti Kings wiki artwork'],
  ];
  for (const [key, value] of expected) {
    if (getMeta(metas, 'property', key, file) !== value) errors.push(file + ': incorrect ' + key);
  }
  for (const [key, value] of [
    ['twitter:card', 'summary_large_image'], ['twitter:title', title],
    ['twitter:description', description], ['twitter:image', SOCIAL_IMAGE]
  ]) {
    if (getMeta(metas, 'name', key, file) !== value) errors.push(file + ': incorrect ' + key);
  }

  const scripts = [...head.matchAll(/<script\b[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)];
  if (scripts.length !== 1) errors.push(file + ': expected exactly one JSON-LD block');
  let json = {};
  try { json = JSON.parse(scripts[0]?.[1] || '{}'); }
  catch (error) { errors.push(file + ': invalid JSON-LD: ' + error.message); }
  if (json['@context'] !== 'https://schema.org' || !Array.isArray(json['@graph'])) errors.push(file + ': malformed schema.org graph');
  const graph = Array.isArray(json['@graph']) ? json['@graph'] : [];
  const site = graph.filter((g) => g['@type'] === 'WebSite');
  const web = graph.find((g) => ['WebPage', 'AboutPage', 'CollectionPage'].includes(g['@type']));
  const crumbs = graph.filter((g) => g['@type'] === 'BreadcrumbList');
  const pageType = file === 'about.html' ? 'AboutPage' : file === 'characters/index.html' || file === 'factions/index.html' ? 'CollectionPage' : 'WebPage';
  if (!web || web.url !== url || web['@id'] !== url + '#webpage' || web['@type'] !== pageType || web.isPartOf?.['@id'] !== HOME + '#website' || web.description !== description || web.inLanguage !== 'en-GB') errors.push(file + ': invalid WebPage structured data');
  if (file === 'index.html') {
    if (site.length !== 1 || site[0].name !== SITE_NAME || site[0].url !== HOME || site[0]['@id'] !== HOME + '#website') errors.push('homepage: invalid WebSite site-name data');
    if (crumbs.length !== 0) errors.push('homepage: unexpected breadcrumb');
    const icon = [...head.matchAll(/<link\b[^>]*\brel=["']icon["'][^>]*>/gi)];
    if (icon.length !== 1 || attrs(icon[0][0]).href !== '/favicon.png') errors.push('homepage: favicon must link to /favicon.png');
  } else {
    if (site.length) errors.push(file + ': WebSite schema only belongs on homepage');
    if (crumbs.length !== 1 || web?.breadcrumb?.['@id'] !== url + '#breadcrumb') errors.push(file + ': missing breadcrumb graph');
    const items = crumbs[0]?.itemListElement || [];
    const expectedDepth = file.startsWith('characters/') && file !== 'characters/index.html' || file.startsWith('factions/') && file !== 'factions/index.html' ? 3 : 2;
    if (items.length !== expectedDepth || items[0]?.item !== HOME || items.at(-1)?.item !== url || !items.every((item, i) => item['@type'] === 'ListItem' && item.position === i + 1 && item.name)) errors.push(file + ': invalid breadcrumb trail');
    if (expectedDepth === 3 && items[1]?.item !== HOME + file.split('/')[0] + '/') errors.push(file + ': wrong breadcrumb parent');
    breadcrumbCount++;
  }

  for (const m of html.matchAll(/<img\b[^>]*>/gi)) {
    imageCount++;
    const image = attrs(m[0]);
    if (image.alt === undefined) errors.push(file + ': image missing alt attribute');
  }
}
validatePNG('favicon.png', 48, true);
validatePNG('images/GK_NIFTYHEADS_niftys.png', 200);

const fallback = text('404.html');
if (!/<meta\b[^>]*name=["']robots["'][^>]*content=["']noindex/i.test(fallback)) errors.push('404 page must be noindex');
if (/<link\b[^>]*rel=["']canonical/i.test(fallback)) errors.push('404 page should not specify a canonical');
if (text('sitemap.xml').includes('404.html') || text('sitemap.xml').includes('_article-template.html')) errors.push('sitemap contains a nonindexable page');

console.log('SEO audit: ' + pages.length + ' public pages, ' + breadcrumbCount + ' breadcrumbs, ' + imageCount + ' HTML images checked.');
if (warnings.length) {
  console.log('Editorial warnings (' + warnings.length + ', not build blockers):');
  for (const note of warnings.slice(0, 35)) console.log('WARN:', note);
  if (warnings.length > 35) console.log('... and ' + (warnings.length - 35) + ' more warnings');
}
if (errors.length) {
  for (const issue of errors) console.error('ERROR:', issue);
  console.error(errors.length + ' SEO error(s)');
  process.exitCode = 1;
} else {
  console.log('SEO validation passed: canonical URLs, titles, descriptions, Open Graph, Twitter Cards, JSON-LD, favicons and 404 controls.');
}
