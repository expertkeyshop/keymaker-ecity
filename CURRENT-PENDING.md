# Current pending work — 28 October 2026

Primary customer website: **https://keymaker-ecity.pages.dev/**. The former `keymaker-ecity.alishanaver72.workers.dev` address is retired and must not be used. This record distinguishes verified setup from older business-profile observations; it is not a live Google feed.

## Website measurement completed

- GA4 `G-Q2CM2F0JB8` and published GTM container `GTM-PKCWS4Z8` measure the primary Pages website only, after analytics consent.
- Call, WhatsApp and directions clicks are key events, counted once per session without invented monetary values. FAQ opens, section views and review-link clicks are also configured.
- GA4 DebugView received live page, section, FAQ and WhatsApp test events. Consent decline, acceptance and withdrawal were checked. See [measurement setup](analytics/README.md).
- Search Console ownership of the primary Pages URL-prefix property was verified and linked to GA4. The Marketing performance Reports snapshot is configured.
- Integration code and documentation were pushed to `expertkeyshop/keymaker-ecity`. Commit `d6d9d04` passed the Pages deployment and both build checks; the live primary and current backup passed deployment verification.
- Browser access resumed. Fresh GA4 readback confirms the primary stream is receiving traffic, page views/scrolls are the only enhanced measurements, and email plus all eight query-redaction keys are enabled. The separate Tag Assistant preview remains optional; actual collection was verified in DebugView.
- Search Console confirms the homepage is indexed. Its live test fetches successfully and declares the Pages homepage as canonical. Manual actions and Security issues both report no issues. See the [28 October check](SEARCH-CONSOLE-CHECK-2026-10-28.md).

## Remaining website checks

| Item | Verified state | Next step |
| --- | --- | --- |
| Sitemap processing | Submitted `https://keymaker-ecity.pages.dev/sitemap.xml` on 28 October. The Sitemaps report says "Couldn't fetch", although Google's live test says crawl allowed and fetch successful. The public URL returns valid XML with HTTP 200. | Recheck Google's processing result later. Do not treat submission or the live test as successful sitemap processing, and do not repeatedly submit the same unchanged file. |
| Homepage recrawl | Homepage is indexed, but Google's 26 October stored crawl contains the former declared canonical. The 28 October live test confirms the corrected Pages canonical. A manual recrawl request was rejected with "Quota Exceeded". | Retry after Google's daily request quota resets; Google suggested the following day. Do not claim a new indexing request was accepted. |
| Ongoing Analytics review | Reports snapshot now shows recorded traffic; the primary stream confirms data collection is active. Earlier report dates include pre-update traffic and may include QA visits. | Compare contact clicks by source/device after the new event setup has accumulated data. Clicks do not establish completed calls, jobs or revenue. |
| Internal traffic exclusion, optional | No stable owner IP was supplied; the internal filter remains in Testing. | Configure an exclusion only when the owner supplies a suitable stable IP. |

## Earlier business-profile follow-ups

The 25 October audit verified **11 products**, **32 services** and **three published updates**. Preserve those results as historical observations; they have not been re-audited during this Analytics task. The saved owner-checklist snapshot remains 16/18 until its outstanding items are verified.

| Item | Last recorded status | Next step |
| --- | --- | --- |
| Final product prices | Six generic prices and five blank quote-based prices were recorded on 25 October. | Owner supplies model-specific prices and what cutting, programming, fitting or travel includes. |
| Google phone | Public visibility was unresolved on 25 October; the owner reported Google review pending. | Read Google's decision and check the public Call button without repeated number edits. |
| Directory listings | Justdial/Sulekha registrations and owner fields were saved; public URL/address/map/category/service/attribute verification remained unresolved. | Continue checks in the existing accounts, without creating duplicates. |
| Sulekha support | Ticket **3718518** had an acknowledgement when last checked on 24 October. | Read the existing support thread for a reply before taking further action. |
| SPARE10 expiry control | Approved terms end **31 October 2026, 23:59 India time**; the earlier control lacked an AM/PM indicator. | Verify the saved end time. No offer changes were made in this Analytics task. |

Keep replying to reviews, adding genuine work photos and maintaining holiday hours. These are ongoing owner activities, not completed one-time setup tasks. Previous audits are preserved in [25 October record](CURRENT-PENDING-2026-10-25.md) and [24 October record](CURRENT-PENDING-2026-10-24.md).
