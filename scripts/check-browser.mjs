// Run against a local fixture so a branch can be verified before publishing.
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
const root = process.cwd();
const output = path.join(root, '.audit-results');
fs.mkdirSync(output, { recursive: true });
const mime = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.png': 'image/png', '.jpg': 'image/jpeg', '.avif': 'image/avif', '.webp': 'image/webp', '.json': 'application/json', '.xml': 'application/xml' };
const server = createServer((req, res) => {
  const url = new URL(req.url, 'http://localhost');
  let file = path.resolve(root, '.' + decodeURIComponent(url.pathname));
  if (!file.startsWith(root + path.sep) && file !== root) { res.writeHead(403); res.end(); return; }
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
  const exists = fs.existsSync(file) && fs.statSync(file).isFile();
  res.writeHead(exists ? 200 : 404, { 'Content-Type': exists ? mime[path.extname(file)] || 'application/octet-stream' : 'text/html' });
  res.end(fs.readFileSync(exists ? file : path.join(root, '404.html')));
});
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
const origin = 'http://127.0.0.1:' + server.address().port;
const paths = [...fs.readFileSync('sitemap.xml', 'utf8').matchAll(/<loc>(.*?)<\/loc>/g)].map(match => new URL(match[1]).pathname);
const failures = [];
const measurements = [];
let browser;
try {
  browser = await chromium.launch({ ...(process.env.GK_BROWSER_EXECUTABLE ? { executablePath: process.env.GK_BROWSER_EXECUTABLE } : {}) });
  const context = await browser.newContext();
  await context.addInitScript(() => {
    window.gkLab = { lcpMs: null, cls: 0 };
    new PerformanceObserver(list => { for (const item of list.getEntries()) window.gkLab.lcpMs = item.startTime; }).observe({ type: 'largest-contentful-paint', buffered: true });
    new PerformanceObserver(list => { for (const item of list.getEntries()) if (!item.hadRecentInput) window.gkLab.cls += item.value; }).observe({ type: 'layout-shift', buffered: true });
  });
  const page = await context.newPage();
  page.on('pageerror', error => failures.push(error.message));
  page.on('response', response => {
    if (response.url().startsWith(origin) && response.status() >= 400 && !response.url().includes('/audit-not-found')) failures.push(response.status() + ' ' + response.url());
  });
  for (const width of [320, 390, 768, 1024, 1280, 1440]) {
    await page.setViewportSize({ width, height: 900 });
    // All pages on the narrowest mobile and a full desktop viewport.
    const sweep = [320, 1440].includes(width) ? paths : ['/', '/about.html', '/characters/', '/factions/', '/pages/waxp.html', '/search.html'];
    for (const pathname of sweep) {
      await page.goto(origin + pathname, { waitUntil: 'load' });
      await page.evaluate(() => document.fonts.ready);
      const dimensions = await page.evaluate(() => ({ width: innerWidth, scroll: document.documentElement.scrollWidth }));
      if (dimensions.scroll > width + 1) failures.push(`${pathname} overflows at ${width}px: ${dimensions.scroll}px`);
    }
    await page.goto(origin + '/', { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    if ([390, 1440].includes(width)) {
      await page.screenshot({ path: path.join(output, `home-${width}.png`) });
      measurements.push({ viewport: width, ...await page.evaluate(() => ({ ...window.gkLab, art: document.querySelector('main img').currentSrc.replace(location.origin, '') })) });
    }
    if (width <= 1200) {
      await page.getByRole('button', { name: 'Toggle navigation' }).click();
      assert.equal(await page.getByRole('navigation', { name: 'Main navigation' }).isVisible(), true);
      await page.keyboard.press('Escape');
      assert.equal(await page.getByRole('navigation', { name: 'Main navigation' }).isVisible(), false);
    }
  }
  await page.setViewportSize({ width: 390, height: 844 });
  const search = page.getByRole('searchbox', { name: 'Search the wiki', exact: true });
  await search.fill('PFLY');
  await page.getByText('View all', { exact: false }).waitFor();
  assert.ok((await page.locator('#header-results').innerText()).includes('Sarah'));
  await search.press('ArrowDown');
  assert.equal(await page.evaluate(() => document.activeElement.className), 'search-result-item');
  await page.keyboard.press('Escape');
  assert.equal(await page.locator('#header-results').isVisible(), false);
  await search.fill('zzznomatch12345');
  await page.getByText('No matching pages. Try a name, topic or different spelling.').waitFor();
  await search.fill('pirate radio');
  await search.press('Enter');
  await page.waitForURL('**/search.html?q=pirate+radio');
  await page.locator('#wiki-search-results li').first().waitFor();
  assert.ok((await page.locator('#wiki-search-results').innerText()).includes('Graffiti Kings'));
  await page.screenshot({ path: path.join(output, 'search-mobile.png') });
  await page.goto(origin + '/search.html?q=the');
  await page.locator('#wiki-search-results li').nth(12).waitFor();
  await page.goto(origin + '/characters/sarah-pu51fly.html');
  assert.equal(await page.getByRole('navigation', { name: 'Breadcrumb', exact: true }).isVisible(), true);
  await page.getByRole('link', { name: 'Skip to content' }).focus();
  await page.keyboard.press('Enter');
  assert.equal(await page.evaluate(() => document.activeElement.id), 'main-content');
  await page.goto(origin + '/pages/submit-lore.html');
  assert.match(await page.getByRole('link', { name: 'Open the contribution form on GitHub' }).getAttribute('href'), /template=lore-contribution.yml/);
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto(origin + '/');
  assert.equal(await page.locator('#matrixCanvas').isVisible(), false);
  const noJS = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 844 } });
  const staticPage = await noJS.newPage();
  await staticPage.goto(origin + '/about.html');
  assert.equal(await staticPage.getByRole('navigation', { name: 'Main navigation' }).isVisible(), true);
  await noJS.close();
  assert.deepEqual(failures, []);
  fs.writeFileSync(path.join(output, 'browser-report.json'), JSON.stringify({ pages: paths.length, widths: [320, 390, 768, 1024, 1280, 1440], measurements, note: 'Local unthrottled lab LCP and CLS; these are not field Core Web Vitals.', failures }, null, 2));
  console.log(`Browser audit passed: ${paths.length} pages, six viewport widths, search, keyboard, breadcrumbs, contribution route, reduced motion and JS-disabled navigation.`);
} finally {
  await browser?.close();
  server.closeAllConnections();
  await new Promise(resolve => server.close(resolve));
}
