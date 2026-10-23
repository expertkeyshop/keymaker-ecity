# Keymaker Ecity website

Prepared on 24 October 2026 for **Key Maker & Locksmith | Electronic City**.

## Current state

The owner reports deploying the redesign on Cloudflare at **https://keymaker-ecity.alishanaver72.workers.dev/**. This is the origin for the current bundle's canonical, social, structured-data and sitemap URLs. The owner's deployment report is not an independent verification of the latest live build.

All five WhatsApp links now contain the owner's exact **English WhatsApp booking URL**, directly in the HTML. The old three-language JavaScript override has been removed. This corrected bundle is rebuilt and checked, ready for the owner to redeploy; the latest correction is **not yet published or verified live**. No agent deployment to Cloudflare is claimed.

The former Sites project ID remains unchanged in `.openai/hosting.json` as historical metadata. The Sites connector returned `project_not_found` and an empty owned/editable inventory. That legacy access issue affects management of the old Sites project; it does **not** prevent the owner from redeploying the static bundle on Cloudflare. The Google Business Profile website field was last verified with the old URL and has not been changed by this documentation update.

## Local use

- Run `node build.mjs` to copy the HTML, CSS and JS to `dist` and regenerate robots/sitemap from the canonical URL.
- Run `node preview.mjs` to serve `dist` at `http://127.0.0.1:8126/`.
- Open `dist/index.html` directly for a portable local preview. All display assets are included and relative.
- Serve/package **dist**, not the source directory. The updated upload ZIP is `../keymaker-ecity-website-bundle.zip`; `../keymaker-ecity-website-preview.zip` contains the same files.

## Included

- Owner logo, storefront cover and two work photos, compressed to responsive WebP variants; originals untouched.
- Clear local service copy, six service groups, 20 confirmed service areas and eight FAQs.
- Accurate address, phone, 24/7 hours, payments, Maps directions and review link.
- Desktop and mobile layouts, accessible menu and FAQs, call links, and the owner's requested English WhatsApp booking message in the latest bundle update.
- Title, description, canonical URL, Open Graph/Twitter metadata, favicon, WebSite/Locksmith JSON-LD, robots.txt and sitemap.xml.
- Linked WebPage and Service entities matching the visible content; explicit search-crawler allowances; an image sitemap; generated `business.md`, `business.json` and supplemental `llms.txt` business summaries.
- Cloudflare static-asset `_headers` for indexable content and correct plain-text, Markdown, JSON-LD and XML content types. Dashboard-level bot rules still need separate verification.
- System fonts, deferred small JavaScript, image dimensions, prioritised hero image and lazy loading of lower-page photos.

The owner-supplied Google Analytics 4 tag **G-Q2CM2F0JB8** is included once immediately after the homepage's `<head>`. The Google verification file remains unchanged. No additional manual page-view or custom-event tracking was added. Analytics collection is not verified live until this bundle is redeployed and tested in the owner's Analytics account.

No unverified testimonials, coordinates, review-rating markup, card payments or blanket vehicle compatibility were invented. FAQs are visitor information; no FAQ rich-result outcome is promised. Arrival is confirmed by phone for the actual location.

## Verification

The redesign's earlier browser checks passed for desktop/mobile display, menu toggling and link dismissal, FAQ expansion, contact destinations and image loading. Overflow checks passed at 320, 390, 820 and 1280 CSS pixels. For the latest update, the static build and JavaScript syntax checks pass, every WhatsApp anchor matches the exact supplied URL, the old script override is absent, and canonical/social/schema/robots/sitemap URLs use the Workers origin. The packaged files are checked against the current build. These local checks do not verify that the updated bundle is deployed on Cloudflare. No published Lighthouse score or field Core Web Vitals measurement is claimed.

## Update the Cloudflare deployment

The owner-supplied Google HTML verification file `googlea8f5575206e3c038.html` is retained unchanged in `verification/` and copied to the root of `dist` on every build. Both ZIPs include it at their root. Keep it in later deployments so Search Console can recheck ownership. A public request before uploading this updated bundle returned 404 for the verification path; ownership is not yet verified.

Keep every absolute site URL on `https://keymaker-ecity.alishanaver72.workers.dev/`. Rebuild the current source with `node build.mjs`, check the exact English WhatsApp destination/message, and package the **contents of dist** with its assets. The owner then redeploys the latest bundle using their existing Cloudflare workflow. Do not upload an older ZIP or treat local rebuilding as publication. After redeployment, check the live pages, images and WhatsApp link at the Workers URL.

Search Console verification, sitemap submission, inspection/indexing and updating the Google Business Profile/owned directory website links remain follow-up work once the final URL and latest live build are verified. `../WEBSITE-RENAME-PLAN.md` describes the earlier Sites route and is historical for this Cloudflare workflow.

## AI and search discovery

The complete shop information and FAQ answers are in the initial HTML, with no login or JavaScript required to read them. `robots.txt` allows search crawlers, including OAI-SearchBot and PerplexityBot; model training and search discovery are separate concerns. The previous wildcard policy is preserved. Supplemental `llms.txt` is an optional content index, not a required search protocol or a promise of inclusion. The plain-text and JSON files are generated from the same HTML/business graph to avoid conflicting phone, hours, services or addresses.

On 24 October 2026, direct public HTTP checks of the deployed Workers homepage, robots.txt and sitemap returned 200 with no X-Robots-Tag restriction. However, that live build still used the old ChatGPT origin in its canonical and sitemap. The current ZIP corrects that. These checks do not prove access from actual verified crawler IPs, indexing or AI recommendations. Cloudflare AI Crawl Control/WAF and any managed robots policies were not changed. Browser verification was unavailable for this incremental update because local browser use was disabled.

After uploading the new ZIP, check the actual served files, canonical URLs and headers; then verify the Workers URL-prefix property in Google Search Console, submit its sitemap, and update owned profile/directory website links. Search engines and AI services choose their own indexing, citations and recommendations. Read `../AI-DISCOVERY.md` for the verification checklist and official references.
