# Website measurement

**Latest verification — 7 November 2026:** Both the GTM container and the separate Google tag report **Excellent / No issues detected**; the historical aggregate consent warning is closed. GTM has zero unpublished changes. The separate tag's domain configuration is exactly `keymaker-ecity.pages.dev`. Live GA4 DebugView received page_view, session_start, first_visit, scroll, faq_open and click_whatsapp during consent-approved developer QA. Test events are not customer leads. The Smart campaign installation reminder remains visible despite receipt evidence and is tracked in ../CURRENT-PENDING.md. Do not install a duplicate tag or force consent to clear it. The current budget is the latest user-approved ₹300 average/day; dated sections below preserve historical settings rather than current instructions.

Google’s actual consent API confirmed Analytics + ads grants analytics_storage, ad_storage and ad_user_data; analytics-only and withdrawal revoke advertising consent. Personalization remains denied. See ../CONSENT-VERIFICATION-2026-11-02.md. The current call-lead action uses One conversion and no invented value; its 60-second threshold is retained. Business outcomes still require owner confirmation.

Primary website: https://keymaker-ecity.pages.dev/

- GA4 account: `412825980`
- GA4 property: `560000241`
- Web stream: `16191970685`
- Measurement ID: `G-Q2CM2F0JB8`
- Google Tag Manager: `GTM-PKCWS4Z8` (account `6400619169`, container `284013809`)

The former `keymaker-ecity.alishanaver72.workers.dev` address is retired and must not be used for integrations or measurement. The primary Pages property is the Search Console property linked to this web stream.

`gtm-container-ready.json` is the container configuration for this existing GTM container. Import using **Merge → Overwrite conflicting tags, triggers and variables**, review the changes, then publish. `keymaker-consent.tpl` is the original private sandboxed consent template. Neither file contains credentials. Future GTM edits must also be exported back into this folder.

## Consent and data

The site loads GTM only after analytics consent and only on the primary hostname. Local previews, Pages preview hostnames and the Worker backup do not send Analytics events. No unconditional GTM noscript iframe is used. Declining or withdrawing consent disables measurement and removes Analytics cookies. Advertising measurement is granted only by the explicit Analytics + ads choice; analytics-only choices keep it denied. Personalisation, Google signals and customer-data uploads remain off.

Page locations keep the pathname and validated campaign parameters; explicit advertising measurement consent also permits validated Google click IDs. Referrers keep the origin only. Customer messages, phone numbers, full WhatsApp links and form values are not event parameters. Enhanced measurement is limited to page loads and scrolls; browser-history pageviews and automatic outbound clicks are disabled.

## Events and reporting

| Event | Purpose | GA4 key event |
| --- | --- | --- |
| `click_call` | Click on a telephone contact button | Yes, once per session |
| `click_whatsapp` | Click on a WhatsApp enquiry button | Yes, once per session |
| `click_directions` | Click on directions | Yes, once per session |
| `click_review` | Click on the Google review link | No |
| `faq_open` | Open a customer FAQ | No |
| `view_section` | See a services, products or visit heading | No |

Contact clicks measure intent, not completed calls, confirmed bookings or revenue. Do not assign invented revenue to them. Existing GA4 key events are preserved.

All three contact key events use **Don't set a default key event value**. Google's initial USD 1 default was removed during setup; the early QA WhatsApp event was sent before that correction and is test data, not earned revenue.

Event-scoped custom dimensions: **CTA location** (`section`), **Service or product** (`item_name`), **Contact method** (`contact_method`), **FAQ question** (`question_id`). New definitions and events can take 24–48 hours to appear in standard reports. Use Engagement → Events, Acquisition → Traffic acquisition and the key-event reports to compare enquiries by source and device. India timezone and INR are configured; event and user retention are 14 months with activity reset enabled.

For a Business Profile campaign link, use:

`https://keymaker-ecity.pages.dev/?utm_source=google&utm_medium=organic&utm_campaign=gbp`

Use short campaign labels, never customer identifiers. No Business Profile links were changed as part of this Analytics implementation.

## Verification and maintenance

- `node scripts/test-analytics.mjs`: consent, cookie cleanup, duplicate prevention, hostname gates and safe parameters.
- `npm run build` in either Cloudflare folder: shared build and integrity/CSP checks.
- `node scripts/verify-live.mjs https://keymaker-ecity.pages.dev/`: live deployment checks.
- Add `?km_debug=1` to the primary site URL for QA. These visits set `debug_mode=true` and `traffic_type=developer`. Google Tag Manager Preview and GA4 DebugView can inspect them. Normal visits do not enable debug mode.
- No owner IP filter is guessed. Internal traffic filtering remains in Testing until a stable owner IP is supplied. The owner-approved Google Ads links and Secondary contact-click imports were completed on 29 October as recorded below. Remarketing, purchase/revenue events and customer-data uploads remain off; the Ads account was left unfunded at the owner's request.
- Publish GTM changes as a named version so they can be rolled back independently of a website deployment.

## Verified setup on 28 October 2026

- GTM version **2 — Consent-based GA4 contact measurement** published with 4 tags, 3 triggers, 9 data-layer variables and 2 built-in variables.
- Commit `2eee7c826e107c4b46cd59dff0e46036e4471081` deployed the Analytics integration. The Pages deployment, Pages build check and Worker backup workflow all succeeded.
- Live browser verification: declining consent followed by reload produced no Google scripts; accepting loaded GTM and its Google tag once.
- GA4 DebugView received `page_view`, `view_section`, `faq_open` and `click_whatsapp`; the WhatsApp event was marked as a key event. Its `page_location` was the clean primary homepage URL, without the debug query or WhatsApp message.
- Query redaction is enabled for `email`, `phone`, `mobile`, `name`, `address`, `text`, `message` and `token`, in addition to email redaction.
- Commit `dd58131` deployed the approved additional Search Console verification meta tag. Ownership verification succeeded and the primary Pages Search Console property was linked to stream `16191970685`. The pre-existing HTML verification file is retained.
- The Reports snapshot uses the Marketing performance template for traffic sources, sessions, engagement and key events. Search Console's Queries and Google organic search traffic reports are visible in the report navigation.
- The browser's separate Tag Assistant popup did not connect in this session. Collection was verified directly in GA4 DebugView and with live asset/CSP checks; a disconnected Preview window does not mean the published container is inactive.
- Later fresh UI readback confirmed the primary stream reports data collection active in the past 48 hours, email redaction is enabled and all eight query-redaction keys are saved. The Reports snapshot contains traffic data; historical report dates must not be attributed solely to the new configuration or to genuine customers.
- The remaining Search Console checks were performed: homepage indexed, current homepage/sitemap live fetches successful, sitemap submitted but processing warning unresolved, and homepage recrawl blocked by Google's daily quota. See `../SEARCH-CONSOLE-CHECK-2026-10-28.md`.

## Google Ads integration verified on 29 October 2026

- Correct Google Ads account: **548-847-0694** (`ocid=8554859915`), Smart campaign **24402045516 — Need a new key fast?**. The saved budget is ₹100 average/day, monthly max ₹3,040, within 10 km of the verified shop plus code RMJ6+V3 Bengaluru.
- Smart's radius includes people in the area and people searching for the area. No presence-only setting was observed. Full-account Data manager/Conversions links were used without switching to Expert Mode, migrating or creating another campaign.
- Ads–GA4 link completed for this account and GA4 property `560000241`. Personalized advertising is OFF, Analytics editing by Ads users is OFF, and enable auto-tagging was selected in the completed link flow.
- Search Console–Ads shows Linked for the primary Pages website. The existing Search Console–GA4 link from 28 October was confirmed for stream `16191970685`. The existing Business Profile–GA4 link from 21 October was also confirmed.
- The Ads Business Profile association is the correct shop, using phone `097623 06303`; location and call-button options are enabled.
- `click_call` (Ads conversion action `7880280131`) and `click_whatsapp` (`7880280134`) were imported as **Contact / Secondary**, counting **Only one**, with **no default monetary value**. These remain click proxies, not completed communications or jobs. Directions were not added as a primary Ads lead goal.
- Saved Ads landing URL: `https://keymaker-ecity.pages.dev/?utm_source=google&utm_medium=cpc&utm_campaign=need_a_new_key_fast&utm_content=local_calls`. These fixed labels pass the existing sanitizer; no Ads click ID or conversion label has been invented.
- No GTM changes or new publication were needed. Four existing tags remain. Advertising consent stays denied; the 0% advertising-consent warning is expected under that configuration. No extra administrator was added in response to the single-administrator warning.
- Final Goals readback: the active Smart account goal is **Smart campaign ad clicks to call**, Primary / Every / 30-day. Existing Clicks to call, Smart map clicks to call and Directions actions show Primary but are outside account goals. Both GA4 imports are Secondary / Only one / 90-day and outside account goals. No Smart tracked-calls entry was visible; connected-call measurement remains unverified. No custom 60-second duration threshold, served Google forwarding number or completed test call is claimed.
- The ad is pending policy review. The balance is exhausted/nearly exhausted, and the owner explicitly instructed that it stay unfunded. No funds were added. The current last-30-days view, 29 September–28 October, shows ₹0 spend and 0 impressions, clicks or calls; this zero-activity baseline provides no acquisition-cost estimate.
- Search Console on 29 October confirms the homepage is on Google. Request indexing succeeded and the URL was added to the priority crawl queue, resolving the earlier daily-quota blocker. This is not proof of a completed refreshed crawl. Sitemaps still shows Couldn't fetch / 0 discovered pages; the unchanged sitemap was not resubmitted.
- Ongoing checks are sitemap processing, the refreshed stored crawl, Smart connected-call reporting availability and real paid attribution once the campaign is eligible and the owner chooses to fund it. See [the 29 October implementation record](../GOOGLE-INTEGRATIONS-STATUS-2026-10-29.md); it supersedes the prior browser-access blocker without changing the historical record.
