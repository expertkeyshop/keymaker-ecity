# Search Console and Analytics check — 28 October 2026

Primary website and URL-prefix property: **https://keymaker-ecity.pages.dev/**.

## Actions and observed results

| Check | Result |
| --- | --- |
| Submitted sitemaps before this action | Empty list. |
| Sitemap submission | Submitted `sitemap.xml` once. Google displayed "Sitemap submitted successfully". |
| Sitemap processing | Subsequent Sitemaps report: "Couldn't fetch", type Unknown, zero discovered pages. The detailed report says "Sitemap could not be read". A later readback still showed the warning. |
| Public sitemap response | HTTP 200, `application/xml; charset=utf-8`, URLs for the primary homepage and `/privacy`, with primary-host image references. |
| Sitemap live test | At 9:36 PM IST: URL available to Google, crawl allowed Yes, page fetch Successful, indexing allowed Yes. Sitemap indexing itself was not requested as a remedy. |
| Homepage index status | URL is on Google; page is indexed. Last stored crawl: 26 October 2026, Googlebot smartphone. |
| Stored homepage canonical | Old crawl still lists the retired host as user-declared canonical. Google-selected canonical is the inspected Pages URL. This is an older crawl, not the current deployed HTML. |
| Homepage live test | At 9:34 PM IST: URL available to Google, crawl allowed Yes, page fetch Successful, indexing allowed Yes, declared canonical `https://keymaker-ecity.pages.dev/`. |
| Homepage recrawl request | Rejected with "Quota Exceeded" and instruction to try again the following day. The request is not recorded as accepted. |
| Manual actions | No issues detected. |
| Security issues | No issues detected. |
| GA4 stream | Primary Pages URL and measurement ID `G-Q2CM2F0JB8`; data collection active in the past 48 hours. |
| GA4 enhanced measurement | Page views and Scrolls only. |
| GA4 redaction | Email enabled; query redaction enabled for email, phone, mobile, name, address, text, message and token. |
| Standard reporting | Reports snapshot is populated. Historical data may include prior configuration and QA traffic, so it is not a count of verified customers or new leads. |

## Follow-up

1. Recheck the existing sitemap entry after Google has had another opportunity to process it. Do not repeatedly submit the unchanged file or change a valid sitemap merely to remove a dashboard warning.
2. If the warning persists, use Google's sitemap live test again and examine any new fetch error before changing server settings. Current tests did not establish a robots block, server failure or manual action.
3. Retry the primary homepage's recrawl request after the daily quota resets. Google suggested the following day (29 October); the exact reset time is not established.
4. Keep both verification methods and the Pages canonical in future deployments. The former host remains retired.

Google's [Sitemaps report guidance](https://support.google.com/webmasters/answer/7451001?hl=en) recommends inspecting sitemap fetch failures with a live URL test. A successful test does not change the separate processing status observed in the report.

Screenshots are retained privately in the local `analytics-proof/` folder, outside this public repository: `search-console-live-homepage.png`, `search-console-live-sitemap.png`, `search-console-sitemap-submitted.png`, `search-console-indexing-quota.png`, `ga4-reports-snapshot.png`, and `ga4-redaction-verified.png`.
