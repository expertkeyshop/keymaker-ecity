# Search Console verification — 28 October 2026

Property type: **URL prefix**.

Primary property: **https://keymaker-ecity.pages.dev/**.

Status: **ownership verified and linked to GA4**. With the owner's explicit approval, the additional HTML verification meta tag was deployed in commit `dd58131`, Google confirmed ownership, and the Pages property was linked to GA4 property `560000241`, stream `16191970685`.

## Preserve verification

- Keep the `google-site-verification` meta tag in `website-openai/index.html` and future builds.
- The pre-existing owner-supplied `googlea8f5575206e3c038.html` is also retained. Its public path is https://keymaker-ecity.pages.dev/googlea8f5575206e3c038.html and the live check confirms its original content: `google-site-verification: googlea8f5575206e3c038.html`.
- No DNS TXT record is needed for this URL-prefix HTML verification method. Do not replace it with a Domain-property verification attempt for the shared `pages.dev` hostname.
- Do not remove existing owners or verification resources as part of routine deployment.

## Sitemap and indexing follow-up

The live sitemap is **https://keymaker-ecity.pages.dev/sitemap.xml**. Its availability and primary URLs were verified. Submission status and homepage indexing have not been freshly confirmed in this setup record.

1. Open the verified Pages property in Search Console and inspect **Sitemaps**.
2. If the primary sitemap is absent, submit the URL above. If present, inspect its current status instead of repeatedly submitting it.
3. Inspect the primary homepage URL and review its indexing result. Verification and a successful sitemap fetch do not guarantee indexing or search ranking.
4. Use the linked Search Console reports in GA4 after Google has processed the data.

The former `keymaker-ecity.alishanaver72.workers.dev` hostname is retired; do not use it for new properties, links or integrations. The old instructions are preserved only as [historical records](docs/SEARCH-CONSOLE-VERIFICATION-RETIRED-HOST.md). See [Analytics setup](analytics/README.md) for the verified integration and [current pending work](CURRENT-PENDING.md) for remaining checks.
