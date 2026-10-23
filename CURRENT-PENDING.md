# Current pending work — 24 October 2026

Business: **Key Maker & Locksmith | Electronic City**

This audit combines local records with read-only live checks on 24 October. It does not change profile fields or checklist ticks. The saved checklist remains **16/18**, from the 22 October snapshot; the booking discrepancy below needs separate review.

## Pending actions

| Item | What is known | Next step |
| --- | --- | --- |
| Google phone | Today's public panel still lacks the phone and offers “Add place's phone number”. The owner reported pending Google review on 22 October; no approval decision was independently verified. | Recheck the review outcome and public phone button. Avoid repeated number edits while review is pending. |
| Directory public listings | Last verified **22 October**: Justdial and Sulekha registrations and owner-profile information are saved. Both public URLs/address checks remain unverified. Justdial had five categories Pending and an incomplete, unverified map location. Sulekha had one service mapped, but service details did not persist and attributes remained 0/11 with three required. | Verify public listing URLs, names, phone and full address. Resolve the remaining category/map/service/attribute fields. These directory editor states were not freshly rechecked today. |
| Sulekha support | Email sent 22 October. The thread checked today contains an acknowledgement for **ticket 3718518**, with no resolution. | Continue through the existing ticket when Sulekha responds; do not duplicate the request. |
| Booking link | Today's editor shows a saved English-only `https://wa.me/919762306303` booking link. The newer trilingual link was **not saved**. This differs from the local completed booking record. | Review the booking setup and correct its local status. Do not present the newer link as saved. |
| Product prices | All six products are publicly visible today. The owner authorized illustrative prices and intends to replace them: Computerised key **₹250**; car remote body/shell **₹650**; cylinder-lock handle **₹700**; door-lock cylinder **₹950**; main-door lock **₹2,300**; car remote key unit **₹1,500**. | Owner supplies final prices and confirms what each price includes. Current publication is complete. |
| SPARE10 expiry | Approved terms end **31 October 2026 at 23:59 India time**. The last editor readback showed “11:59” without AM/PM despite saving 23:59. Exact persisted expiry control remains unverified; it was not freshly checked today. | Confirm the actual end-time control. Publication and approved terms are recorded complete. |
| Website bundle update | The owner reports deploying the redesign at **https://keymaker-ecity.alishanaver72.workers.dev/**. The latest local bundle now uses this origin throughout. All five WhatsApp links use the owner's exact **English URL**, with the old three-language script override removed. The rebuilt and checked bundle is ready; the latest correction is not yet published or verified live. The legacy Sites access issue does not block the owner's Cloudflare redeployment. | Redeploy `keymaker-ecity-website-bundle.zip` to the existing Cloudflare site; then verify the live link/images and final URL before Search Console and profile/directory URL follow-up. No agent Cloudflare publication is claimed. Local preview: `website-openai/dist/index.html`; `keymaker-ecity-website-preview.zip` contains the same corrected build. |

## Completed checks and recurring work

- **Latest AI/search bundle:** rebuilt and checked with explicit search-crawler allowances, matching WebSite/WebPage/Locksmith/Service data, an image sitemap, generated business.md/business.json and supplemental llms.txt, plus the exact five English WhatsApp links. The new ZIP has not been deployed by the agent. Direct public HTTP checks on 24 October returned 200 for the live homepage/robots/sitemap, but their canonical/sitemap URLs still pointed to the old ChatGPT origin. Redeploy the corrected ZIP, verify served content and any Cloudflare crawler rules, then complete Search Console verification and sitemap submission. Details: `AI-DISCOVERY.md`.
- **Freshly checked today:** Google's Unreplied tab says “You've replied to new reviews”; all six products and FAQ/update content are publicly visible.
- **Previously verified:** all **29 service descriptions** were saved and checked; the website, cover/logo, categories, hours and service areas were verified during the 21–22 October work. These were not all independently rechecked today.
- **Recurring:** reply to new reviews, add useful real shop/work photos, publish factual updates as needed, confirm any holiday-hour changes, and compare profile performance over equivalent periods. The saved September–October baseline is historical, not today's totals.

## Local record discrepancies

`PUBLISHING-QUEUE.md` still has introductory bullets saying the first key edit is Pending, although later text and JSON correctly show all six live. The completed booking wording in the checklist/JSON is outdated. Some README and execution-log entries describe superseded intermediate states. Historical source files and checklist ticks were left unchanged in this audit.
