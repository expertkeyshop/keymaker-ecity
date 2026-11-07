# Semrush audit resolution — 7 November 2026

Primary website: https://keymaker-ecity.pages.dev/

## Release status

The code changes are committed as `bae07b5` in `.repo-sync`. Both Cloudflare target builds and their validations passed. The user-requested push retry successfully published this commit and documentation commit `0de0eff` to main. **The fixes are now deployed and verified live.** All seven compared primary HTML/JS/CSS files exactly match the release bytes. Both primary and backup pass the 17-endpoint live verifier and expected 404 check.

An earlier push attempt was not executed because automatic approval review hit its usage limit. That historical blocker is resolved by the later successful retry. No alternate publishing route was used to bypass the check.

Upload-ready archive: `keymaker-ecity-pages-2026-11-07-semrush-fixes.zip`.

- 99 public files, 2,571,721 bytes.
- SHA-256: `9f845e3933593e7ee162c0abea024026c38bf07ce71663e4139643c42fb2a2db`.
- Files are at the archive root, including `index.html`, `_headers` and `.well-known`.
- Archive integrity and compact JavaScript/CSS were checked. Twenty source/generated files were also synchronized back to the main local folder after verifying the mirror had no independent edits to those files.

## What the audit findings mean and what was done

| Finding supplied by the user | Evidence and action | Status |
| --- | --- | --- |
| One 404 at `https://www.keymaker-ecity.pages.dev/` | This exact hostname returned 404. The actual primary host returned 200. No authored navigation, canonical or discovery file points to the `www` hostname. It is not a configured production alias. Restrict the audit to the actual host and inspect the audit's discovery source for the extra hostname. | Audit-scope correction pending account access; no production-page 404 was found. |
| Twelve broken WhatsApp links, all HTTP 429 | The supplied destinations are contact links on WhatsApp. Fresh read-only GET checks of all 13 distinct WhatsApp destinations in the site returned 200 after redirects. No messages were sent. HTTP 429 records rate limiting at the time of Semrush's requests. | Keep working contact links. Retry at a lower crawl rate; document an external rate-limit exception only if it persists after manual checking. |
| Four unminified JS/CSS warnings | The build now compacts all five published JavaScript/CSS assets and embedded CSS using pinned esbuild. Hashes, CSP and SRI are regenerated from the resulting bytes. | Fixed and verified live; Semrush re-audit pending. |
| One low text-to-HTML ratio warning | The homepage contains useful service content, structured data and inline CSS. Compaction reduces HTML size while preserving content. No filler text or extra mobile clutter was added just to change the ratio. | Reassess in the next audit. A score warning alone is not grounds to remove useful markup or redesign the approved layout. |
| Two pages with one incoming internal link | The latest supplied table includes the homepage, privacy page and machine-readable `business.md`. The privacy footer now also links to Business details, providing another genuine source page linking to `business.md`. A small site's homepage having few incoming internal source pages is not itself a broken navigation path. | Relevant link published; no invented pages or repetitive links. Re-audit pending. |
| One hostname lacks HSTS | The primary host and its privacy page return `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`. The extra `www` hostname does not. Build/live validation now explicitly checks HSTS. | Production HSTS verified. Exclude the unconfigured host from production audit scope. |
| `/privacy.html` permanently redirects | It correctly returns 308 to `/privacy`. The privacy footer's internal cookie link was updated to `/privacy#cookies`, removing an unnecessary redirect for that navigation path. | Direct link fixed live; preserve the legitimate redirect for old URLs. |

The WhatsApp checks establish that the destinations were accessible during these requests. They do not guarantee that every external crawler or WhatsApp client will always receive the same response. The buttons and their prefilled messages remain intact.

The `www` finding should not be addressed by creating a duplicate website or a preview branch solely to silence an audit. Configuration of a conventional `www` redirect requires control of the relevant hostname. We do not own the parent `pages.dev` zone.

## Latest supplied crawl inventory

This table is transcribed from the user's Semrush report, not from a newly accessed Semrush session.

| URL on the primary host unless specified | Status | Reported issues |
| --- | --- | --- |
| `/privacy` | 200 | 3 |
| `/` | 200 | 16 |
| `/business.md` | 200 | 1 |
| `/llms.txt` | 200 | Healthy |
| `/robots.txt` | 200 | Healthy |
| `/sitemap.xml` | 200 | Healthy |
| `https://www.keymaker-ecity.pages.dev/` | 404 | Broken |
| `/privacy.html` | 308 | Redirected |

Semrush ILR is an internal-link metric. The displayed crawl-depth clicks describe navigation steps from the start URL, not customer visits. Neither is a Google ranking. A healthy fetched sitemap here does not establish that Search Console has finished processing its separate submission report.

## Size changes

Raw file sizes; these are not compressed transfer sizes or new Lighthouse scores.

| Asset | Before bytes | After bytes | Reduction |
| --- | ---: | ---: | ---: |
| `script.js` | 13,483 | 9,468 | 29.8% |
| `analytics.js` | 4,731 | 3,507 | 25.9% |
| `styles.css` | 46,631 | 42,839 | 8.1% |
| `mobile-focus.css` | 8,012 | 7,629 | 4.8% |
| `desktop-focus.css` | 5,643 | 5,014 | 11.1% |
| `index.html` | 123,502 | 118,698 | 3.9% |
| `privacy.html` | 60,368 | 56,615 | 6.2% |

Only whitespace minification is enabled; syntax and identifier transformations are disabled. No layout change is intended. Browser visual QA was unavailable because the local browser runtime fails before opening tabs; no fresh visual or Lighthouse pass is claimed.

## Validation completed

- Both Pages and Workers builds passed with their pinned dependencies.
- Analytics tests passed for readable source and generated JavaScript: no choice, decline, analytics only, analytics plus ads, withdrawal, cookie cleanup, hostname gating and click-ID handling.
- Generated pages, internal anchors, catalog, sitemap, verification file, canonical metadata, CSP and SRI checks passed.
- Target output validation passed for 99 files.
- Read-only public checks covered 33 internal URL/asset entries, external destinations, and both the exact primary and extra `www` hostname.
- No consent defaults were changed and no extra Google tag was introduced.

Local evidence is in `proof/2026-11-07/semrush/`: `internal-live-before.json`, `external-live-before.json`, `hostname-check.json`, `minification-sizes.json`, `package.json` and `live-release-comparison.json`. The `before` filenames denote checks made before this release was deployed; the comparison file records the successful new release check.

## Remaining steps

1. Completed: pushed the approved local commits through the existing Git integration. The ZIP remains an alternate artifact; no additional upload is needed for this release.
2. Completed: Pages live verification and byte-for-byte comparison of the seven main HTML/JS/CSS files. Evidence is `proof/2026-11-07/semrush/live-release-comparison.json`. The business-only backup also passed with noindex intact.
3. In the existing Semrush project, set the crawl start to `https://keymaker-ecity.pages.dev/`. Clear **Crawl all subdomains** and remove the unconfigured `www` URL from any custom URL list. Review how the crawler discovered that URL before changing settings. Keep the production site's real URLs in scope.
4. Reduce crawl speed for the retry if WhatsApp continues returning 429. Keep the contact links usable and visible; do not replace them with concealed JavaScript links or redirects to game the audit.
5. Re-run the audit once the corrected build is live, inspect remaining affected URLs, and record the resulting issue counts. Do not predeclare a new health score or guaranteed clearance of every warning.
6. Reuse the prepared 10-keyword list for postal code 560100 only after checking the existing target to avoid duplication. Keyword tracking setup is not confirmed complete.

No Semrush settings have been changed or new crawl launched in this session. Other account-dependent items remain in `CURRENT-PENDING.md`; this release does not certify Ads recommendations, Search Console processing, Sulekha support corrections or ChatGPT username availability.

The user can publish the already-reviewed commits from their own terminal with:

```powershell
git -C "C:\Users\kbose\OneDrive\Desktop\keymaker\.repo-sync" push origin main
```

The agent successfully executed this push on the user's requested retry. It is retained here as a reference, not an outstanding user action.

## Official references

- Audit scope and crawl configuration: https://www.semrush.com/kb/539-configuring-site-audit
- Crawled-page metrics: https://www.semrush.com/kb/543-site-audit-crawled-pages
- Working pages reported broken: https://www.semrush.com/kb/1088-why-do-working-pages-appear-broken
- Cloudflare static response headers: https://developers.cloudflare.com/pages/configuration/headers/
- Cloudflare preview hostname behavior: https://developers.cloudflare.com/pages/configuration/preview-deployments/
- Independent esbuild minification options: https://esbuild.github.io/api/#minify
