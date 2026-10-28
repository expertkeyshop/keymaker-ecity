# Website measurement

Primary website: https://keymaker-ecity.pages.dev/

- GA4 account: `412825980`
- GA4 property: `560000241`
- Web stream: `16191970685`
- Measurement ID: `G-Q2CM2F0JB8`
- Google Tag Manager: `GTM-PKCWS4Z8` (account `6400619169`, container `284013809`)

`gtm-container-ready.json` is the container configuration for this existing GTM container. Import using **Merge → Overwrite conflicting tags, triggers and variables**, review the changes, then publish. `keymaker-consent.tpl` is the original private sandboxed consent template. Neither file contains credentials. Future GTM edits must also be exported back into this folder.

## Consent and data

The site loads GTM only after analytics consent and only on the primary hostname. The local preview, Pages preview hostnames and Worker backup do not send Analytics events. No unconditional GTM noscript iframe is used, since it would bypass the site's consent choice. Declining or withdrawing consent disables measurement and removes Analytics cookies. Advertising consent stays denied; Google signals and user-provided data collection are off.

Page locations keep the pathname and validated campaign parameters only. Referrers keep the origin only. Customer messages, phone numbers, full WhatsApp links and form values are not event parameters. Enhanced measurement is limited to page loads and scrolls; browser-history pageviews and automatic outbound clicks are disabled.

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

Event-scoped custom dimensions: **CTA location** (`section`), **Service or product** (`item_name`), **Contact method** (`contact_method`), **FAQ question** (`question_id`). New definitions and events can take 24–48 hours to appear in standard reports. Use Engagement → Events, Acquisition → Traffic acquisition and the key-event reports to compare enquiries by source and device. India timezone and INR are configured; event and user retention are 14 months with activity reset enabled.

For a Business Profile campaign link, use:

`https://keymaker-ecity.pages.dev/?utm_source=google&utm_medium=organic&utm_campaign=gbp`

Use short campaign labels, never customer identifiers. No Business Profile links were changed as part of this Analytics implementation.

## Verification and maintenance

- `node scripts/test-analytics.mjs`: consent, cookie cleanup, duplicate prevention, hostname gates and safe parameters.
- `npm run build` in either Cloudflare folder: shared build and integrity/CSP checks.
- `node scripts/verify-live.mjs https://keymaker-ecity.pages.dev/`: live deployment checks.
- Add `?km_debug=1` to the primary site URL for QA. These visits set `debug_mode=true` and `traffic_type=developer`. Google Tag Manager Preview and GA4 DebugView can inspect them. Normal visits do not enable debug mode.
- No owner IP filter is guessed. Internal traffic filtering remains in Testing until a stable owner IP is supplied. Ads integrations, remarketing, paid services, purchase/revenue events and customer-data uploads require a separate business need and were not enabled.
- Publish GTM changes as a named version so they can be rolled back independently of a website deployment.
