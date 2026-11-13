// Runtime crawl of the deployed GitHub Pages site.
// No dependencies or credentials. Use "node scripts/check-live-seo.mjs" after deployment.
// Tests can supply a local HTTP origin while keeping the production canonical expectation.
import fs from 'node:fs';
import { pathToFileURL } from 'node:url';

const SITE = 'https://graffitikings.com';
const PRODUCTION = new URL(SITE);
const imagePaths = ['/favicon.png', '/images/GK_NIFTYHEADS_niftys.png'];
const timeoutMs = 15000;
const maxAttempts = 3;
const retryableStatuses = new Set([408, 429, 500, 502, 503, 504]);

function unique(values) { return [...new Set(values)]; }
function attrs(tag) {
  const values = {};
  for (const m of tag.matchAll(/([a-zA-Z_:][\w:.-]*)\s*=\s*(["'])(.*?)\2/g)) values[m[1].toLowerCase()] = m[3];
  return values;
}
function metadata(head, kind, name) {
  const metas = [...head.matchAll(/<meta\b[^>]*>/gi)].map(m => attrs(m[0]));
  return metas.filter(m => m[kind] === name).map(m => m.content);
}
function htmlTags(head, name) {
  return [...head.matchAll(new RegExp('<' + name + '\\b[^>]*>', 'gi'))].map(m => attrs(m[0]));
}

export async function auditLiveSite({ baseUrl = SITE, checkHosts = baseUrl === SITE, fetchFn = fetch, retryDelayMs = 400 } = {}) {
  const errors = [];
  const warnings = [];
  const results = { checkedPages: 0, sitemapCount: 0, checkedImages: 0, checkedRedirects: 0, retries: 0, recoveredRequests: 0 };
  const requestBase = new URL(baseUrl);
  const target = (path) => new URL(path, requestBase).toString();

  async function request(url, options = {}) {
    // A single 503 from the CDN must not fail the whole sitemap crawl.
    // Retry only temporary failures, and still report the last response if
    // the problem persists; permanent HTTP errors are never hidden.
    for (let attempt = 1; attempt <= maxAttempts; attempt++) {
      try {
        const response = await fetchFn(url, {
          redirect: options.redirect || 'follow',
          signal: AbortSignal.timeout(timeoutMs),
          headers: { 'User-Agent': 'GraffitiKingsLiveSEOCrawl/1.0' }
        });
        if (retryableStatuses.has(response.status) && attempt < maxAttempts) {
          results.retries++;
          await new Promise(resolve => setTimeout(resolve, retryDelayMs * (2 ** (attempt - 1))));
          continue;
        }
        if (attempt > 1 && !retryableStatuses.has(response.status)) {
          results.recoveredRequests++;
          warnings.push('Recovered transient failure on attempt ' + attempt + ': ' + url);
        }
        return response;
      } catch (error) {
        if (attempt === maxAttempts) {
          errors.push('Network failure after ' + attempt + ' attempts for ' + url + ': ' + error.message);
          return null;
        }
        results.retries++;
        await new Promise(resolve => setTimeout(resolve, retryDelayMs * (2 ** (attempt - 1))));
      }
    }
    return null;
  }
  async function read(url, expectedStatus, expectedType) {
    const response = await request(url);
    if (!response) return null;
    if (response.status !== expectedStatus) errors.push(url + ': HTTP ' + response.status + ' (expected ' + expectedStatus + ')');
    if (expectedType && !response.headers.get('content-type')?.toLowerCase().includes(expectedType)) {
      errors.push(url + ': unexpected Content-Type ' + response.headers.get('content-type'));
    }
    return response;
  }

  const sitemapUrl = target('/sitemap.xml');
  const sitemapResponse = await read(sitemapUrl, 200, 'xml');
  let liveURLs = [];
  if (sitemapResponse) {
    const xml = await sitemapResponse.text();
    liveURLs = [...xml.matchAll(/<loc>\s*([^<]+)\s*<\/loc>/gi)].map(m => m[1].trim());
    if (!xml.includes('<urlset') || !liveURLs.length) errors.push('Deployed sitemap has no valid <urlset>/<loc> entries');
    if (unique(liveURLs).length !== liveURLs.length) errors.push('Deployed sitemap contains duplicate URLs');
    if (liveURLs.some(u => {
      try { return new URL(u).origin !== SITE || new URL(u).hash !== ''; } catch { return true; }
    })) errors.push('Deployed sitemap contains invalid, off-domain or fragment URLs');
    if (liveURLs.some(u => u.endsWith('/404.html') || u.endsWith('/_article-template.html'))) {
      errors.push('Deployed sitemap includes a nonindexable template or 404 page');
    }
    const sourceXML = fs.readFileSync('sitemap.xml', 'utf8');
    const expectedURLs = [...sourceXML.matchAll(/<loc>\s*([^<]+)\s*<\/loc>/gi)].map(m => m[1].trim());
    if (liveURLs.length !== expectedURLs.length || expectedURLs.some(u => !liveURLs.includes(u))) {
      errors.push('Deployed sitemap differs from the checked-out main-branch sitemap (' +
        liveURLs.length + ' deployed versus ' + expectedURLs.length + ' expected)');
    }
    results.sitemapCount = liveURLs.length;
  }

  const robotsResponse = await read(target('/robots.txt'), 200, 'text/plain');
  if (robotsResponse) {
    const body = await robotsResponse.text();
    if (!/^\s*Sitemap:\s*https:\/\/graffitikings\.com\/sitemap\.xml\s*$/im.test(body)) {
      errors.push('Deployed robots.txt is missing the canonical Sitemap directive');
    }
    if (/^\s*Disallow:\s*\/\s*$/im.test(body)) errors.push('Deployed robots.txt disallows the entire site');
  }

  // Only trust same-domain sitemap URLs, even if deployment was compromised.
  const paths = liveURLs.filter(u => {
    try { return new URL(u).origin === SITE; } catch { return false; }
  }).map(u => [u, new URL(u).pathname]);

  // Avoid burst-loading GitHub Pages. Three simultaneous requests maximum.
  let nextIndex = 0;
  async function worker() {
    while (nextIndex < paths.length) {
      const [canonical, path] = paths[nextIndex++];
      const pageURL = target(path);
      const response = await read(pageURL, 200, 'text/html');
      if (!response || response.status !== 200) continue;
      results.checkedPages++;
      const responseURL = new URL(response.url);
      if (responseURL.origin !== requestBase.origin || responseURL.pathname !== path) {
        errors.push(pageURL + ': unexpected final page URL ' + response.url);
      }
      const content = await response.text();
      const head = content.split(/<\/head>/i)[0];
      const tags = htmlTags(head, 'link');
      const canonicals = tags.filter(t => t.rel === 'canonical');
      if (canonicals.length !== 1 || canonicals[0].href !== canonical) errors.push(pageURL + ': canonical does not equal sitemap URL');
      const og = metadata(head, 'property', 'og:url');
      if (og.length !== 1 || og[0] !== canonical) errors.push(pageURL + ': og:url does not equal sitemap URL');
      if (metadata(head, 'property', 'og:title').length !== 1) errors.push(pageURL + ': missing/duplicate og:title');
      if (metadata(head, 'name', 'description').length !== 1) errors.push(pageURL + ': missing/duplicate description');
      if (metadata(head, 'name', 'twitter:card')[0] !== 'summary_large_image') errors.push(pageURL + ': missing social preview card');
      if (metadata(head, 'name', 'robots').some(x => /\bnoindex\b/i.test(x))) errors.push(pageURL + ': unexpected robots noindex');
      if (response.headers.get('x-robots-tag')?.toLowerCase().includes('noindex')) errors.push(pageURL + ': X-Robots-Tag noindex');
      const jsonScripts = [...head.matchAll(/<script\b[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)];
      if (jsonScripts.length !== 1) errors.push(pageURL + ': expected one JSON-LD script');
      else {
        try {
          const graph = JSON.parse(jsonScripts[0][1])['@graph'];
          if (!Array.isArray(graph) || !graph.some(x => ['WebPage', 'AboutPage', 'CollectionPage'].includes(x['@type']) && x.url === canonical)) {
            errors.push(pageURL + ': structured data does not match canonical');
          }
        } catch (e) { errors.push(pageURL + ': invalid deployed JSON-LD: ' + e.message); }
      }
    }
  }
  await Promise.all(Array.from({length: 3}, () => worker()));

  for (const path of imagePaths) {
    const url = target(path);
    const response = await read(url, 200, 'image/png');
    if (!response || response.status !== 200) continue;
    const binary = new Uint8Array(await response.arrayBuffer());
    if (binary.length < 24 || Buffer.from(binary.subarray(0, 8)).toString('hex') !== '89504e470d0a1a0a') {
      errors.push(url + ': invalid PNG signature');
    }
    results.checkedImages++;
  }
  const missingPath = '/page-not-found-seo-monitor-2026-11-13';
  const notFound = await read(target(missingPath), 404, 'text/html');
  if (notFound) {
    const html = await notFound.text();
    // A generic host 404 can say "Page not found" and still return HTTP 404.
    // Require markers from our actual branded 404.html, including a way back
    // into the wiki, so a missing custom error document fails this check.
    const hasBrand = html.includes('That page is not in the Graffiti Kings archive.');
    const hasWikiHome = /<a\s+href=["']\/["'][^>]*>\s*Wiki home\s*<\/a>/i.test(html);
    const hasCharacterLink = /<a\s+href=["']\/characters\/["'][^>]*>\s*Characters\s*<\/a>/i.test(html);
    if (!hasBrand || !hasWikiHome || !hasCharacterLink) {
      errors.push('Custom Graffiti Kings 404 page is not being served (missing archive branding or navigation)');
    }
  }

  if (checkHosts) {
    for (const [url, label] of [
      ['https://www.graffitikings.com/', 'www to apex'],
      ['http://graffitikings.com/', 'HTTP to HTTPS']
    ]) {
      const response = await request(url);
      if (!response) continue;
      results.checkedRedirects++;
      if (response.url !== SITE + '/' || response.status !== 200) {
        errors.push(label + ': expected final https://graffitikings.com/ (got ' + response.url + ', HTTP ' + response.status + ')');
      }
    }
    // Legacy GitHub Pages project address is useful for migration, but outside
    // the site's current DNS authority; report problems without blocking deploy.
    try {
      const response = await fetchFn('https://graffiti-kings.github.io/graffiti-kings/', {
        redirect: 'follow', signal: AbortSignal.timeout(timeoutMs)
      });
      if (response.url !== SITE + '/') warnings.push('Old GitHub Pages URL did not resolve to the canonical homepage: ' + response.url);
    } catch (error) {
      warnings.push('Legacy GitHub Pages redirect could not be checked: ' + error.message);
    }
  }

  return { ...results, errors, warnings };
}

async function main() {
  const report = await auditLiveSite();
  for (const warning of report.warnings) console.log('WARNING:', warning);
  for (const error of report.errors) console.error('ERROR:', error);
  console.log('Live SEO:', JSON.stringify({
    sitemapURLs: report.sitemapCount, verifiedPages: report.checkedPages,
    images: report.checkedImages, hostRedirects: report.checkedRedirects,
    retries: report.retries, recovered: report.recoveredRequests,
    errors: report.errors.length, warnings: report.warnings.length
  }));
  if (report.errors.length) process.exitCode = 1;
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) await main();
