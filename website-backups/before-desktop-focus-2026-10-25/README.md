# Keymaker Ecity website

Single-page website for **Key Maker &amp; Locksmith | Electronic City**, redesigned on **25 October 2026** around the owner's locksmith and home-service references. A separate privacy and cookie page is included.

## Source and build

The stack stays HTML, CSS and vanilla JavaScript. The build uses Node's built-in modules; there are no npm dependencies, framework runtime, database, checkout or contact-form backend.

From the parent `keymaker` folder:

```powershell
node website-openai/build.mjs
node website-openai/preview.mjs
```

The preview is served at `http://127.0.0.1:8126/`. Upload or package the **contents of `website-openai/dist/`**, with `index.html` at the archive root. The parent folder's `index.html` is the owner's profile checklist, not this customer website.

The build copies HTML, CSS, JavaScript, the privacy page, static security headers, final image assets and the byte-exact Google verification file. It regenerates `robots.txt`, `sitemap.xml`, `business.json`, `business.md` and `llms.txt` from the homepage's canonical URL, visible FAQs and linked business data. Source `assets/` is the asset source of truth. Working originals named `*-original.png` (or JPG, WebP, AVIF) and `image-manifest*.json` are kept locally and excluded from copying into the public output. Do not place credentials or internal documents in `dist/`.

## Production URL

The default canonical origin is the existing owner-supplied website:

**https://keymaker-ecity.alishanaver72.workers.dev/**

Building locally does not deploy to that URL. This folder also remains suitable for a Cloudflare Pages Direct Upload project. A new Pages project receives its own `pages.dev` URL; it does not rename the existing Workers website.

Once a different final production origin is known, rebuild before uploading:

```powershell
node website-openai/build.mjs --origin https://your-final-domain/
```

Use the actual assigned Pages URL or connected custom domain. The option requires an HTTPS origin without a path, query or fragment. It updates absolute URLs in the generated HTML, linked business data and discovery files without altering the source homepage. Supply the option again on later builds for that domain, or deliberately update the source canonical and all source absolute URLs. Keep one consistent final canonical URL.

## Design and contact behavior

The redesigned page uses a large locksmith visual, the owner's real shop/work photos and logo, service and product catalogues, prominent Call/WhatsApp actions, local contact information and FAQs. Generated imagery is representative visual material; it must not be described as an actual employee or completed customer job. Original business photography remains the source for business-image metadata.

The static page contains the business content and contact links before JavaScript loads. Navigation, section reveals, analytics consent and CTA measurement progressively enhance it. Reduced-motion preferences and keyboard access are supported. Service/product WhatsApp messages identify the selected enquiry; visitors still confirm availability, compatibility, arrival time and the quote directly with the shop.

At 700px and below, `mobile-focus.css` provides a compact customer journey: services, products, then shop details. Cards use short summaries and small thumbnails. Three more products, specialist details, FAQs, service areas, the shop introduction and photos remain available in native disclosures. Decorative hero imagery and repeated promotional sections are hidden on phones. Desktop retains the full copy and original section order. The disclosure script opens deep-linked sections and preserves mobile choices across resizing; the source disclosures stay open without JavaScript. Keep `mobile-focus.css` in the deployable bundle.

Catalogue prices are quote-based unless the owner has confirmed an actual starting price for that product. Do not turn suggested ₹399/₹999 tiers, reference-site statistics, stock faces, example testimonials or sample licences into business claims.

## Analytics and verification

### Analytics and consent

The GA4 property **G-Q2CM2F0JB8** is configured but **does not load until a visitor accepts analytics**. The choice is stored in local storage under `km-analytics-consent`; declining keeps Google Analytics unloaded and clears existing `_ga*` cookies where the browser permits. Visitors can reopen the choice from the footer or the privacy page. The privacy page explains analytics, cookies, retention and contact details.

Once consent is granted, CTA events are `click_call`, `click_whatsapp` and `click_directions`. They measure link interactions, not completed calls, confirmed bookings or paying customers. The tracking code does not configure a Google Ads account, launch an advertising budget or establish Ads call-conversion measurement. Check events in GA4 Realtime/DebugView after deployment and configure reporting/key events in the account when appropriate.

### Search Console verification

`verification/googlea8f5575206e3c038.html` is copied unchanged to the public root on every build. Keep it available for Search Console ownership rechecks. A separate URL-prefix property is needed if the production hostname changes.

## Search and AI discovery

Canonical/social metadata, Locksmith/WebSite/WebPage/Service structured data, descriptive images, sitemap and robots directives describe the same public business information as the visible page. The complete content is crawlable without JavaScript. Supplemental Markdown, JSON-LD and `llms.txt` files provide matching business facts; their presence cannot guarantee indexing, rankings or AI recommendations. Cloudflare account-level bot restrictions require separate live checking.

## Deployment and final checks

The build output in `website-openai/dist/` is the deployable bundle. Verify the canonical origin, privacy page, consent behavior, responsive layout and security headers on the preview before uploading. A prepared bundle is not evidence of a completed Cloudflare deployment or a live performance score. The legacy `.openai/hosting.json` identifies the earlier Sites project and is not needed for the Cloudflare static upload.
