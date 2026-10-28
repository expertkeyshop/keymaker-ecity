# Search Console verification — 28 October 2026

Property type: **URL prefix**.

Primary property: **https://keymaker-ecity.pages.dev/**.

Status: **ownership verified and linked to GA4**. With the owner's explicit approval, the additional HTML verification meta tag was deployed in commit `dd58131`, Google confirmed ownership, and the Pages property was linked to GA4 property `560000241`, stream `16191970685`.

## Preserve verification

- Keep the `google-site-verification` meta tag in `website-openai/index.html` and future builds.
- The pre-existing owner-supplied `googlea8f5575206e3c038.html` is also retained. Its public path is https://keymaker-ecity.pages.dev/googlea8f5575206e3c038.html and the live check confirms its original content: `google-site-verification: googlea8f5575206e3c038.html`.
- No DNS TXT record is needed for this URL-prefix HTML verification method. Do not replace it with a Domain-property verification attempt for the shared `pages.dev` hostname.
- Do not remove existing owners or verification resources as part of routine deployment.

## Sitemap and indexing — checked 28 October 2026

The live sitemap is **https://keymaker-ecity.pages.dev/sitemap.xml**. It was absent from the submitted-sitemap list and was submitted once. Google confirmed successful submission, but the subsequent processing report says **Couldn't fetch** with zero discovered pages. This warning remains unresolved; submission is not the same as successful processing.

- Google's sitemap live test at 9:36 PM IST reports **URL is available to Google**, crawl allowed **Yes**, and page fetch **Successful**. The public endpoint also returns HTTP 200 and XML. No site-side fetch block was established in these checks.
- The homepage inspection reports **URL is on Google / Page is indexed**. Its stored crawl is dated 26 October and contains the retired declared canonical, while Google selected the inspected Pages URL.
- The homepage live test at 9:34 PM IST reports successful fetching, indexing allowed and the current declared canonical **https://keymaker-ecity.pages.dev/**.
- A request to recrawl the corrected homepage was rejected with **Quota Exceeded**. Google asked to try the following day; no accepted request is claimed.
- Manual actions and Security issues both report **No issues detected**.

Next: recheck sitemap processing later and retry the homepage recrawl after the daily quota resets. Avoid repeat submissions of the unchanged sitemap. Detailed evidence and the diagnostic reference are recorded in [28 October check](SEARCH-CONSOLE-CHECK-2026-10-28.md). Verification and indexing do not guarantee ranking.

The former `keymaker-ecity.alishanaver72.workers.dev` hostname is retired; do not use it for new properties, links or integrations. The old instructions are preserved only as [historical records](docs/SEARCH-CONSOLE-VERIFICATION-RETIRED-HOST.md). See [Analytics setup](analytics/README.md) for the verified integration and [current pending work](CURRENT-PENDING.md) for remaining checks.
