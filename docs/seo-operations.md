# Graffiti Kings — SEO operations and launch checklist

Primary site: **https://graffitikings.com/**  
Host: GitHub Pages (repository `graffiti-kings/graffiti-kings`)  
DNS: GoDaddy; keep existing A/CNAME/NS records intact while verifying search accounts.

## What is enforced in GitHub Actions

- 86 published HTML pages currently have one canonical URL each on `graffitikings.com`, unique page titles and descriptions.
- HTML source contains Open Graph and Twitter Card previews, with existing GKniftyHEADS artwork as the shared social image.
- Home page contains a `WebSite` node for the preferred site name. Other pages have a `WebPage`, `AboutPage` or `CollectionPage` node, with `BreadcrumbList` for navigation context. No unsupported awards, ratings, reviews or authors are invented.
- A square 96×96 PNG favicon is linked from the homepage.
- The sitemap lists the published canonical URLs. `404.html` and `_article-template.html` are excluded; the custom 404 page is `noindex`.
- `node scripts/check-site.mjs` checks internal links, anchor targets, sitemap consistency and the search index.
- `node scripts/check-seo.mjs` checks metadata, structured data, image alt attributes, social URL alignment, favicon, duplicate titles/descriptions, and indexability controls.

All modifications require a successful **Graffiti Kings site audit** workflow before merge.

## Actions required outside the repository

### Google Search Console (domain property)

1. Open https://search.google.com/search-console and select **Add property → Domain** for `graffitikings.com`.
2. Copy Google's **actual** DNS TXT verification value. In **GoDaddy → DNS**, add that TXT record exactly as provided by Google. Do **not** change or remove the A/CNAME records used by GitHub Pages.
3. Complete verification in Search Console. A domain property covers www and non-www plus HTTP/HTTPS.
4. In **Sitemaps**, submit `https://graffitikings.com/sitemap.xml`. Confirm processing; this is a discovery hint, not guaranteed indexing.
5. In **URL Inspection**, test the homepage, `/characters/`, `/factions/`, a real-person biography and a fictional faction page. Check that the **Google-selected canonical** is correct, pages can be crawled and rendered, and no unexpected `noindex` applies.
6. Monitor Pages/Indexing, Performance, Manual actions, Security issues and Core Web Vitals. Compare periods rather than judging a brand-new domain immediately.

### Bing Webmaster Tools

1. Open https://www.bing.com/webmasters/ and import the verified Search Console property or verify site ownership independently.
2. Submit the same sitemap and monitor crawl/indexing reports.

### Redirects and availability — after each deployment

Verify with a real browser or HTTP redirect tracer:
- `https://graffitikings.com/` is reachable with a valid certificate.
- `https://www.graffitikings.com/` resolves or permanently redirects to the preferred non-www host.
- `http://graffitikings.com/` upgrades to HTTPS.
- The old `https://graffiti-kings.github.io/graffiti-kings/` does not become a competing indexed canonical URL.
- `/robots.txt`, `/sitemap.xml`, `/favicon.png` and `/images/GK_NIFTYHEADS_niftys.png` all return success.
- A nonexistent URL uses the branded 404 page and an HTTP **404** status, not a soft 404.
- Source canonical links and sitemap entries remain consistent.

These runtime claims cannot be established from the repository alone and must be checked on the deployed domain.

### Social previews, mobile performance and content review

- Test a homepage, a character page and a faction page in Facebook Sharing Debugger and LinkedIn Post Inspector. Confirm the shared artwork crops cleanly. If not, replace the social image with a properly composed, licensed preview; do not rely on guessed image dimensions.
- Run PageSpeed Insights (mobile first) on the homepage and representative deep pages: evaluate LCP, INP, CLS, fonts, the Matrix animation and hero image weight. Use field data when enough traffic exists; otherwise use Lighthouse lab diagnostics.
- Keep real-world artist biographies independently sourced and distinguish them from fictional year-3008 lore. Prioritize original art, citations, useful biographies, clear entity names and human-readable internal links over keyword repetition.
- Review generic descriptions reported as *warnings* by `check-seo.mjs`; technical passing does not mean each page has competitive editorial content.
- Do not add fake `Review`, `AggregateRating`, `FAQPage`, `Organization` identity, product offers, author metadata, `SearchAction`, unsupported hreflang, or fabricated sitemap `lastmod` dates.
- Keep search titles, summaries and image alt text descriptive and accurate. Meta keywords and artificial keyword density are not part of this plan.

## Verification references

- https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- https://developers.google.com/search/docs/appearance/site-names
- https://developers.google.com/search/docs/appearance/structured-data/breadcrumb
- https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- https://developers.google.com/search/docs/appearance/favicon-in-search
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap

## Change policy

Create a pull request, run the complete audit, review any editorial changes, and **merge manually** only when checks pass. After GitHub Pages deploys, repeat the HTTP, Search Console and social-preview checks. Never assume that passing source tests proves search-engine indexing or rankings.
