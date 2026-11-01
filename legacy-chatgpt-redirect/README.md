# Legacy ChatGPT Site migration

The primary business website is https://keymaker-ecity.pages.dev/.

This repository belongs only to Sites project appgprj_6ad8d539e2a88191ad3d4657fd33d7d3. On 2 November 2026 its slug was shortened to keymaker-ecity. Sites returned https://keymaker-ecity.alishanaver72.chatgpt.site as the hosted address.

The Worker issues a permanent HTTP 301 redirect to the primary Pages website. It preserves paths and query parameters, maps /index.html to /, and cannot redirect to an incoming external host. Missing paths stay missing on the primary site rather than all becoming homepage redirects. This service collects no analytics, stores no data, and adds no competing business content.

The original static page is retained in Git history. All currently supported legacy hostname aliases must be checked after publication; the slug API does not itself promise a redirect from an older account suffix. Google replaces indexed addresses after recrawling; deployment does not directly edit a Google result.

Build and validate with `node scripts/build.mjs` and `node scripts/verify.mjs`. Publish through the existing Sites source helper and saved-version deployment workflow. Do not deploy this redirect Worker into the primary Cloudflare Pages project.
