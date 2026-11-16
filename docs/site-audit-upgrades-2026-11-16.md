# Website audit upgrades — 16 November 2026

The 103-page baseline passed its existing tests but lacked usable keyboard search,
visible breadcrumbs, a submission destination and consistent icon links. This
change adds the search page, bringing the public sitemap to 104 pages.

## Implemented

- Full article and summary search with alias matching, ranked results, result
  counts, empty/error feedback, arrow/Escape handling and native Enter submission.
  Header suggestions link to the complete results page. Search data is loaded on
  demand and a CI check rejects stale generated content.
- Static navigation with labelled search, 44px menu controls, active-page links,
  Escape/outside-click closing, responsive menus, visible breadcrumbs and a
  focusable skip-to-content destination. Navigation remains available without JS.
- Consistent favicon links on every page, including future article template.
- Reduced-motion support, pausing Matrix drawing in hidden tabs and removal of
  repeated delayed header replacement and duplicate Google Fonts loading.
- AVIF/WebP artwork variants, explicit dimensions, priority loading and the PNG
  fallback. The original 852 KiB artwork is preserved; AVIF variants are about
  36–104 KiB at 480–1200px.
- Unique 1200×630 JPEG share cards for all 104 public pages, based on each page's
  actual title and existing project artwork. Open Graph and X metadata match.
- A public GitHub issue form for sourced history, corrections and proposed lore.
  The site explains account requirements, visibility and editorial review.
- Expanded source checks and a pull-request browser job for six viewport widths,
  two full-site layout sweeps, keyboard flows, reduced motion, no-JS navigation,
  screenshots and explicitly labelled local LCP/CLS observations.

## Verification and limits

The dependency-free source audits and 23 tests pass locally and in GitHub CI.
The browser job also passed in run 43908371580: all 104 pages were checked at
320px and 1440px, with representative pages at 390px, 768px, 1024px and 1280px.
Search, keyboard navigation, native Enter submission, breadcrumbs, the contribution
route, reduced motion and JavaScript-disabled navigation passed. No page overflow
or runtime errors were reported. The saved mobile homepage, desktop homepage and
mobile search screenshots were visually reviewed.

The unthrottled local fixture measured zero CLS at 390px and 1440px and selected
480px / 960px AVIF artwork respectively. Lab LCP observations were 48ms / 120ms.
These measurements describe a fast local CI server; they are not production or
field Core Web Vitals. The browser artifact contains the full report and images.
Local headless execution in the editing workspace was restricted, so CI supplied
the browser evidence.

The workflow action runtimes were also updated from deprecated Node 20 actions
to the officially published Node 24 releases: checkout v7.0.1, setup-node v7.1.0
and upload-artifact v7.0.2 (verified against their official action.yml files).

External link audit: 236 unique article destinations, 195 reachable, no confirmed
404/410 destinations, and 41 unverified because of network/access responses.
See `external-link-audit.json` for URLs, referring pages and exact outcomes. A
blocked or timed-out publisher is not evidence that its cited article has vanished.
