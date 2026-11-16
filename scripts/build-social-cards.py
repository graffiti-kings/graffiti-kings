"""Build deterministic page-specific share cards and responsive artwork.

Development dependency: Pillow with AVIF and WebP support. The committed outputs
are served directly; visitors and GitHub Pages need no Python or image runtime.
Uses only the existing GK artwork, real page titles and local DejaVu fonts.
"""
from pathlib import Path
from html import unescape
import json
import re
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT = Path('/usr/share/fonts/truetype/dejavu')
art = Image.open(ROOT / 'images/GK_NIFTYHEADS_niftys.png').convert('RGBA')
for width in (480, 960, 1200):
    resized = art.resize((width, width), Image.Resampling.LANCZOS)
    resized.save(ROOT / f'images/GK_NIFTYHEADS-{width}.webp', quality=85, method=6)
    resized.save(ROOT / f'images/GK_NIFTYHEADS-{width}.avif', quality=65)

out = ROOT / 'images/social'
out.mkdir(exist_ok=True)
manifest = {}
for page in sorted(ROOT.rglob('*.html')):
    if '.git' in page.parts or page.name in ('404.html', '_article-template.html'):
        continue
    source = page.read_text()
    path = page.relative_to(ROOT).as_posix()
    title = unescape(re.sub(r'<[^>]+>', '', re.search(r'<h1\b[^>]*>(.*?)</h1>', source, re.S).group(1)))
    title = re.sub(r'\s+', ' ', title).strip()
    category = 'PEOPLE & CHARACTERS' if path.startswith('characters/') else 'FACTIONS & ARMIES' if path.startswith('factions/') else 'STREET ART · HISTORY · WORLDS'
    card = Image.new('RGB', (1200, 630), '#0a0a0a')
    draw = ImageDraw.Draw(card)
    draw.rectangle((0, 0, 1199, 8), fill='#ffd700')
    draw.rounded_rectangle((820, 70, 1160, 560), radius=24, fill='#141919')
    illustration = art.copy()
    illustration.thumbnail((400, 490), Image.Resampling.LANCZOS)
    card.paste(illustration, (790 + (400-illustration.width)//2, 75 + (490-illustration.height)//2), illustration)
    small = ImageFont.truetype(str(FONT / 'DejaVuSans.ttf'), 19)
    brand = ImageFont.truetype(str(FONT / 'DejaVuSans-Bold.ttf'), 25)
    draw.text((55, 56), 'GRAFFITI KINGS WIKI', font=brand, fill='#ffd700')
    draw.text((55, 106), category, font=small, fill='#69dddd')
    size = 57
    while True:
        font = ImageFont.truetype(str(FONT / 'DejaVuSans-Bold.ttf'), size)
        lines, current = [], ''
        for word in title.split():
            candidate = (current+' '+word).strip()
            if draw.textlength(candidate, font=font) > 700 and current:
                lines.append(current)
                current = word
            else:
                current = candidate
        if current:
            lines.append(current)
        if (len(lines) <= 5 and all(draw.textlength(line, font=font) <= 700 for line in lines)) or size <= 28:
            break
        size -= 2
    y = 172
    for line in lines:
        draw.text((55, y), line, font=font, fill='#f5f5f5')
        y += size + 13
    draw.line((55, 520, 750, 520), fill='#555555', width=1)
    draw.text((55, 551), 'graffitikings.com', font=brand, fill='#ffd700')
    filename = path.removesuffix('.html').replace('/', '-') + '.jpg'
    card.save(out / filename, quality=88, optimize=True, progressive=True)
    relative = 'images/social/' + filename
    manifest[path] = {'image': relative, 'alt': title + ' — Graffiti Kings Wiki', 'width': 1200, 'height': 630}
    # Match the same page-specific card on Open Graph and X.
    absolute = 'https://graffitikings.com/' + relative
    source = re.sub(r'(<meta (?:property="og:image"|name="twitter:image") content=")[^"]*(">)', lambda m: m[1]+absolute+m[2], source)
    escaped_alt = manifest[path]['alt'].replace('&', '&amp;').replace('"', '&quot;')
    source = re.sub(r'(<meta property="og:image:alt" content=")[^"]*(">)', lambda m: m[1]+escaped_alt+m[2], source)
    for prop, value in [('og:image:width', '1200'), ('og:image:height', '630'), ('og:image:type', 'image/jpeg')]:
        if f'property="{prop}"' not in source:
            source = source.replace('</head>', f'  <meta property="{prop}" content="{value}">\n</head>')
    page.write_text(source)
(ROOT / 'images/social/manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+'\n')
print(f'Generated {len(manifest)} page-specific 1200×630 share cards and six responsive artwork variants.')
