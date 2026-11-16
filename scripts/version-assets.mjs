// Content hashes prevent old CSS/JS being reused with newly deployed HTML.
import fs from 'node:fs';
import path from 'node:path';
import { createHash } from 'node:crypto';
let stale = false;
function visit(dir = '.') {
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    if (item.name.startsWith('.') || item.name === 'node_modules') continue;
    const file = path.join(dir, item.name);
    if (item.isDirectory()) { visit(file); continue; }
    if (!file.endsWith('.html')) continue;
    const old = fs.readFileSync(file, 'utf8');
    const updated = old.replace(/\b(href|src)="((?:\.\.\/|\/)?(?:css\/style\.css|js\/(?:main|search|radio)\.js))(?:\?[^\"]*)?"/g, (match, attr, url) => {
      const target = url.startsWith('/') ? path.join(process.cwd(), url.slice(1)) : path.resolve(path.dirname(file), url);
      // The root template is designed to be copied into a nested directory.
      const asset = fs.existsSync(target) ? target : path.join(process.cwd(), url.replace(/^\.\.\//, ''));
      const version = createHash('sha256').update(fs.readFileSync(asset)).digest('hex').slice(0, 12);
      return `${attr}="${url}?v=${version}"`;
    });
    if (updated !== old) {
      stale = true;
      if (!process.argv.includes('--check')) fs.writeFileSync(file, updated);
    }
  }
}
visit();
if (stale && process.argv.includes('--check')) { console.error('Asset versions are stale. Run node scripts/version-assets.mjs'); process.exitCode = 1; }
else console.log('CSS and JavaScript asset versions are current.');
