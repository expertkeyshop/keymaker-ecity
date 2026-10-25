# Website redesign deployment

Prepared **25 October 2026** for **Key Maker & Locksmith | Electronic City**.

## Prepared redesign ZIP

`keymaker-ecity-redesign-2026-10-25.zip` contains **34 files** at the correct archive paths, including 24 finished assets. The checked version is **1,277,066 bytes** (approximately 1.28 MB). Its SHA-256 is `697e714416ebd4d0db2dfd1979ee1041dbcce73ef606d705bf9cd1bfd7baf3a1`.

Local checks passed for source/output parity, all 22 image dimensions and readable image files, local links, six services, six products, eight FAQs, matching JSON-LD/discovery output, sitemap XML, robots directives, one GA4 configuration, byte-exact Google verification, archive integrity and Cloudflare's upload limits. This is a static build/archive check; browser review and actual deployment are separate steps. Rebuilding or editing the page after this check requires repackaging the ZIP.

## Build and preview

Run these commands from `C:\Users\kbose\OneDrive\Desktop\keymaker`:

```powershell
node website-openai/build.mjs
node website-openai/preview.mjs
```

Open `http://127.0.0.1:8126/` to review the customer website. The production files are in `website-openai/dist/`. Package the files **inside** that folder so `index.html`, `styles.css`, `script.js`, `_headers`, verification/discovery files and `assets/` are at the ZIP root. Keep the private project records, original source art, nested Git metadata and owner checklist out of the deployment ZIP.

The build preserves `googlea8f5575206e3c038.html` exactly and the existing GA4 property `G-Q2CM2F0JB8`. Optimized final images are copied from source `assets/`; provenance manifests and working originals are not public website assets.

## Existing Workers URL or a new Pages project

The current production origin in the source is **https://keymaker-ecity.alishanaver72.workers.dev/**. Redeploying through the owner's existing Workers workflow can keep that hostname.

For the requested Pages workflow, Cloudflare supports a ZIP or a folder of prebuilt assets through dashboard Direct Upload. In **Workers & Pages**, choose **Create application → Get started → Drag and drop your files**, enter the project name, upload the built ZIP and deploy. Later versions use **Create a new deployment**. A new Pages project gets a separate `pages.dev` hostname; use the actual assigned hostname or a connected custom domain. [Cloudflare Direct Upload documentation](https://developers.cloudflare.com/pages/get-started/direct-upload/).

Before final publication at a different hostname, regenerate canonical, social, sitemap and structured-data URLs using the actual production origin:

```powershell
node website-openai/build.mjs --origin https://your-final-domain/
```

Then create a fresh ZIP from `dist/` and upload it. The example above is a placeholder; no Pages hostname has been invented or reserved by this document. The origin option changes generated output only, so use the same argument for future builds on that domain. Preview deployments can retain the production canonical; the canonical should identify the intended primary website.

Dashboard Direct Upload supports up to 1,000 files and 25 MiB per asset. A Direct Upload project cannot switch in place to Git integration; choose a new Git-integrated project if automatic deployment is needed later. [Cloudflare upload limits and project behavior](https://developers.cloudflare.com/pages/get-started/direct-upload/).

## Check the published website

After an actual deployment, verify the public site from a signed-out browser:

- Homepage and images load on desktop and mobile; navigation, FAQs and sticky contact buttons remain usable.
- Phone links dial the correct business number. WhatsApp opens the intended number and selected service/product message. Directions open the actual shop location.
- The canonical URL, social image URLs, JSON-LD, `robots.txt`, `sitemap.xml`, `business.json` and `llms.txt` all use the final production hostname.
- `https://YOUR-FINAL-HOST/googlea8f5575206e3c038.html` returns the exact Google verification line rather than the homepage or a 404.
- Public content has no login requirement, `noindex` restriction or accidental Cloudflare challenge blocking the intended search crawlers.
- Optimized images load without layout jumps; reduced-motion preferences disable decorative motion; contact actions remain available if JavaScript is disabled.

Add or verify the **URL-prefix** property for the final HTTPS origin in Google Search Console. Submit `sitemap.xml`, inspect the homepage and request indexing if eligible. If the hostname changes, update the Google Business Profile and other owned listings only after the new destination has been checked. Search Console submission does not guarantee indexing or ranking.

## Analytics and advertising

The existing Google tag remains once on the page. The site emits `click_call`, `click_whatsapp` and `click_directions` for contact interactions, with context identifying where the visitor clicked. Verify each event once per intended click in GA4 Realtime or DebugView after upload. Confirm that no duplicate custom handlers or a second Google tag are added in Cloudflare, Tag Manager or another tool. [Google's event setup and validation guide](https://developers.google.com/analytics/devguides/collection/ga4/events).

A link click is an enquiry signal, not proof of a completed call or booked job. Google Ads account linking, conversion imports, actual call conversion setup and any ₹200/day campaign remain account work; this static build does not create or charge an advertising campaign. Mark the appropriate measured interactions as key events only after testing, then evaluate qualified calls and paying jobs separately.

## Status boundary

These instructions describe a local build and a manual deployment workflow. They do not assert that the redesigned ZIP has been uploaded, that a new Pages project exists, that Search Console ownership has been verified, or that live Analytics events/Core Web Vitals have passed. Record actual deployment URLs and verified results after publication.
