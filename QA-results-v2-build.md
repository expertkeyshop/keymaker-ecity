# Redesign v2 static build and archive QA

Checked **25 October 2026**, after the final illustrative-image wording, mobile anchor-scroll, FAQ heading and mobile product-text/tap-target refinements.

- Final archives: `keymaker-ecity-redesign-2026-10-25.zip`, `keymaker-ecity-website-bundle.zip`, `keymaker-ecity-website-preview.zip`.
- All three archives are byte-identical: **1,277,066 bytes**, **34 files**, including **24 finished assets**.
- SHA-256: `697e714416ebd4d0db2dfd1979ee1041dbcce73ef606d705bf9cd1bfd7baf3a1`.
- Source HTML/CSS/JavaScript/headers exactly match the latest generated output.
- All local link and responsive-image targets resolve; one H1, six service cards, six product cards and eight FAQs.
- All 22 HTML image dimensions match their source images; all packaged image files decode successfully.
- All call and WhatsApp links use the confirmed business number; item-specific WhatsApp messages identify the selected service/product.
- JSON-LD matches `business.json`; robots, Markdown, llms.txt and valid sitemap XML use the Workers production origin and 25 October review date.
- Sitemap/business-image metadata include only the three genuine shop/work photos; illustrative hero/work scenes are excluded from those business images.
- GA4 loader/configuration appears once; Google Search Console verification remains the exact 53 supplied bytes in source, output, extracted bundle and every ZIP.
- ZIP CRC and every archived byte match the checked `dist/` output. No working originals, provenance manifests, Git metadata or dependencies are packaged. Files/count meet Cloudflare Direct Upload limits.
- Previous normal archives were copied unchanged into `website-backups/before-reference-redesign-2026-10-25/` before replacement.
- The extracted `keymaker-ecity-website-bundle/` was refreshed by copy-only overwrite and its expected files match `dist/` byte-for-byte.
- Stale files in extracted bundle: none. No files were deleted.

These are local static/archive checks. Browser QA is recorded separately by the primary agent; this report does not claim Cloudflare publication or live Analytics/Search Console verification.
