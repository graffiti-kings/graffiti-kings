import test from 'node:test';
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { auditLiveSite } from '../scripts/check-live-seo.mjs';

const root = process.cwd();
const expectedPages = [...fs.readFileSync('sitemap.xml', 'utf8').matchAll(/<loc>[^<]+<\/loc>/g)].length;

async function fixtureServer(change = () => null) {
  const server = createServer((req, res) => {
    const pathname = new URL(req.url, 'http://localhost').pathname;
    const file = pathname === '/' ? 'index.html' :
      pathname.endsWith('/') ? pathname.slice(1) + 'index.html' : pathname.slice(1);
    const exists = fs.existsSync(path.join(root, file)) && fs.statSync(path.join(root, file)).isFile();
    const originalStatus = exists ? 200 : 404;
    const originalBody = fs.readFileSync(path.join(root, exists ? file : '404.html'));
    const mime = file.endsWith('.xml') ? 'application/xml' :
      file.endsWith('.txt') ? 'text/plain' : file.endsWith('.png') ? 'image/png' : 'text/html';
    const replacement = change({ pathname, file, status: originalStatus, body: originalBody });
    res.writeHead(replacement?.status ?? originalStatus, {
      'Content-Type': replacement?.type || mime
    });
    res.end(replacement?.body ?? originalBody);
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  return {
    baseUrl: 'http://127.0.0.1:' + server.address().port,
    close: async () => {
      server.closeAllConnections();
      await new Promise(resolve => server.close(resolve));
    }
  };
}

test('all published URLs, images, metadata and custom 404 pass a local deployment fixture', async () => {
  const server = await fixtureServer();
  try {
    const result = await auditLiveSite({ baseUrl: server.baseUrl, checkHosts: false });
    assert.deepEqual(result.errors, []);
    assert.equal(result.sitemapCount, expectedPages);
    assert.equal(result.checkedPages, expectedPages);
    assert.equal(result.checkedImages, 2);
  } finally { await server.close(); }
});

test('a wrong canonical on a deep page fails the live crawl', async () => {
  const server = await fixtureServer(({ pathname, body }) => {
    if (pathname !== '/characters/charlie-buster.html') return null;
    const html = body.toString('utf8').replace(
      'rel="canonical" href="https://graffitikings.com/characters/charlie-buster.html"',
      'rel="canonical" href="https://graffitikings.com/wrong-page.html"'
    );
    return { body: html };
  });
  try {
    const result = await auditLiveSite({ baseUrl: server.baseUrl, checkHosts: false });
    assert.ok(result.errors.some(e => e.includes('charlie-buster.html') && e.includes('canonical')));
  } finally { await server.close(); }
});

test('a stale sitemap with a missing URL is reported', async () => {
  const server = await fixtureServer(({ pathname, body }) => {
    if (pathname !== '/sitemap.xml') return null;
    const xml = body.toString('utf8').replace(
      /\s*<url><loc>https:\/\/graffitikings\.com\/about\.html<\/loc><\/url>/, ''
    );
    return { body: xml };
  });
  try {
    const result = await auditLiveSite({ baseUrl: server.baseUrl, checkHosts: false });
    assert.ok(result.errors.some(e => e.includes('differs from the checked-out')));
  } finally { await server.close(); }
});

test('a missing favicon and soft 404 are both rejected', async () => {
  const server = await fixtureServer(({ pathname }) => {
    if (pathname === '/favicon.png') return { status: 404, type: 'text/html', body: 'missing' };
    if (pathname.startsWith('/page-not-found-seo-monitor-')) return { status: 200 };
    return null;
  });
  try {
    const result = await auditLiveSite({ baseUrl: server.baseUrl, checkHosts: false });
    assert.ok(result.errors.some(e => e.includes('favicon.png')));
    assert.ok(result.errors.some(e => e.includes('expected 404')));
  } finally { await server.close(); }
});

test('a generic HTTP 404 with the words Page not found is not accepted as our custom page', async () => {
  const server = await fixtureServer(({ pathname }) => {
    if (!pathname.startsWith('/page-not-found-seo-monitor-')) return null;
    return {
      status: 404,
      body: '<!doctype html><html><body><h1>Page not found</h1><p>Generic hosting error</p></body></html>'
    };
  });
  try {
    const result = await auditLiveSite({ baseUrl: server.baseUrl, checkHosts: false });
    assert.ok(result.errors.some(e => e.includes('Custom Graffiti Kings 404 page')),
      'A generic 404 page should fail the branded-404 check');
  } finally { await server.close(); }
});

test('a 404 response with archive branding but no wiki navigation is rejected', async () => {
  const server = await fixtureServer(({ pathname }) => {
    if (!pathname.startsWith('/page-not-found-seo-monitor-')) return null;
    return {
      status: 404,
      body: '<!doctype html><html><body><h1>Page not found</h1>' +
        '<p>That page is not in the Graffiti Kings archive.</p></body></html>'
    };
  });
  try {
    const result = await auditLiveSite({ baseUrl: server.baseUrl, checkHosts: false });
    assert.ok(result.errors.some(e => e.includes('Custom Graffiti Kings 404 page')),
      'Branding alone should not pass the custom 404 check without navigation');
  } finally { await server.close(); }
});

test('a one-off HTTP 503 on a published page is retried and then passes', async () => {
  let pixelRequests = 0;
  const server = await fixtureServer(({ pathname }) => {
    if (pathname !== '/factions/pixel-pushers.html') return null;
    pixelRequests++;
    if (pixelRequests === 1) return { status: 503, type: 'text/html', body: 'temporary service unavailable' };
    return null;
  });
  try {
    const result = await auditLiveSite({ baseUrl: server.baseUrl, checkHosts: false, retryDelayMs: 0 });
    assert.deepEqual(result.errors, []);
    assert.equal(result.checkedPages, expectedPages);
    assert.equal(pixelRequests, 2);
    assert.equal(result.retries, 1);
    assert.equal(result.recoveredRequests, 1);
  } finally { await server.close(); }
});

test('three consecutive HTTP 503 responses still fail the live crawl', async () => {
  let pixelRequests = 0;
  const server = await fixtureServer(({ pathname }) => {
    if (pathname !== '/factions/pixel-pushers.html') return null;
    pixelRequests++;
    return { status: 503, type: 'text/html', body: 'service unavailable' };
  });
  try {
    const result = await auditLiveSite({ baseUrl: server.baseUrl, checkHosts: false, retryDelayMs: 0 });
    assert.ok(result.errors.some(e => e.includes('pixel-pushers.html: HTTP 503')));
    assert.equal(result.checkedPages, expectedPages - 1);
    assert.equal(pixelRequests, 3);
    assert.equal(result.retries, 2);
    assert.equal(result.recoveredRequests, 0);
  } finally { await server.close(); }
});

test('permanent 404 on a published page fails without retries', async () => {
  let requests = 0;
  const server = await fixtureServer(({ pathname }) => {
    if (pathname !== '/factions/pixel-pushers.html') return null;
    requests++;
    return { status: 404, type: 'text/html', body: 'not found' };
  });
  try {
    const result = await auditLiveSite({ baseUrl: server.baseUrl, checkHosts: false, retryDelayMs: 0 });
    assert.ok(result.errors.some(e => e.includes('pixel-pushers.html: HTTP 404')));
    assert.equal(requests, 1);
    assert.equal(result.retries, 0);
  } finally { await server.close(); }
});
