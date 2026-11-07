# Website branding release — 7 November 2026

Implementation commit: 6f6eddf, pushed to expertkeyshop/keymaker-ecity/main. Primary: https://keymaker-ecity.pages.dev/ . Live primary and backup checks passed; backup remains noindex.

- Added branded multi-size favicon.ico, 48/192-pixel PNG links and 180-pixel Apple touch icon.
- Added 1200 x 675 JPEG sharing preview using the existing genuine storefront image. Open Graph/Twitter tags cover homepage, privacy and 404 pages; page titles/descriptions remain specific to each page.
- Preserved WebSite/Locksmith schema and added a second truthful alternate business name.
- Added a compact, keyboard-accessible Preferred Sources deep link to each page. No extra third-party JavaScript is loaded. Visitor choice remains on Google.
- Extended build/live validation for all three pages, image files and correct MIME types. Both target builds pass, with 99 public files and 79 assets. Each live origin passes 17 endpoints plus a real 404 response.
- Local archive: keymaker-ecity-pages-2026-11-07-branding.zip (2,576,280 bytes), SHA-256 c659fc5a05d1f96e1ad288a6d86a2b35f66ee204b330cb972a9bbc2b77448a25. The ZIP has root index.html and includes .well-known.

Google chooses search-result site names and icons. This deployment supplies consistent brand signals; it does not immediately replace Google's cached Cloudflare/ChatGPT labels. The legacy Site redirects to Pages rather than serving duplicate business content. The retired Worker was not reactivated.

The Preferred Sources chooser returned No results on the last browser check (2 November); current eligibility has not been rechecked because the browser runtime fails. Its link is functional as a link to Google's settings, but listing availability is Google's decision. Search Console's generative-AI control was Include on that date. The button is not a universal recommendation, an indexing request, or a promise of Discover/AI placement.

Official implementation references:
- https://developers.google.com/search/docs/appearance/preferred-sources
- https://developers.google.com/search/docs/appearance/site-names
- https://developers.google.com/search/docs/appearance/favicon-in-search
- https://developers.google.com/search/docs/appearance/ai-features
