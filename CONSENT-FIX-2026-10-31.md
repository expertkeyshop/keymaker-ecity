# Consent diagnostics and Ads setup — 31 October 2026

Primary website: https://keymaker-ecity.pages.dev/. GTM-PKCWS4Z8, Google Analytics G-Q2CM2F0JB8, Ads account 548-847-0694.

## Implemented and published

The former consent bridge always sent ad_storage, ad_user_data and ad_personalization as denied. The original banner offered analytics acceptance only. This explains why accepting it never produced advertising consent; it was not evidence that all customers deliberately rejected advertising measurement.

GTM **version 3 — Visitor-choice ad measurement consent** was published on **31 October at 4:46 PM IST**. The merge changed the two consent tags and their sandboxed template and added one data-layer variable. The existing Google tag, GA4 events and three triggers were retained. There are four tags, three triggers, ten user variables and two built-in variables. The actual version-3 export was copied through Google's JSON Preview after the download control failed, and saved in analytics/gtm-container-ready.json; the template file matches that export.

Website commit **b9999d0 — Honor optional advertising measurement consent** was pushed to main and its new behaviour was verified on the live Pages site. The website and privacy page offer three equally styled choices:

| Visitor choice | analytics_storage | ad_storage | ad_user_data | ad_personalization |
| --- | --- | --- | --- | --- |
| No choice / Decline | denied | denied | denied | denied |
| Analytics only | granted | denied | denied | denied |
| Analytics + ads | granted | granted | granted | denied |

Advertising measurement is optional. Existing stored “granted” remains analytics-only, so earlier consent is never silently expanded. Personalised advertising and Google signals remain disabled. Decline blocks Google measurement resources from loading; changing back to Analytics only removes advertising measurement cookies; full withdrawal removes Analytics cookies too. The site continues to work for every choice.

Only advertising-measurement opt-in permits validated gclid, gbraid and wbraid values in reported page URLs. Arbitrary query strings, messages and customer contact details remain excluded. This corrects a click-attribution limitation without adding a duplicate GA4 tag, inventing conversions or enabling customer-data uploads.

## Google Ads notifications

The **Your website needs a Google tag** setup flow identified the existing **G-Q2CM2F0JB8** tag. Test connection succeeded: **“A Google tag was found on your website.”** The two existing click_call and click_whatsapp event goals were shown as **Active**, and Finish was saved.

The second **Set up conversion measurement to get more insights** flow recognised the existing contact goal. Its event summary showed click_call and one other event; the existing contact action was saved, without creating another tag or duplicate conversion action.

After refreshing Ads, neither setup notification appeared. The remaining notice is **Balance is running low**. No payment was made and the ₹100 average/day and 10 km settings were retained. Active event setup is not proof of a completed customer call, WhatsApp conversation or paid job.

## Verification

- Expanded consent tests pass for no consent, legacy acceptance, advertising opt-in, ad-only withdrawal, full withdrawal, invalid choices, cookie deletion, primary-host gates, malformed/oversized click IDs and customer-data redaction.
- The GTM sandboxed consent API is tested for every analytics/advertising consent combination, including a missing advertising choice. Defaults are denied before updates. The exported template and its bindings are checked against the source.
- Both Pages and Worker builds pass canonical/discovery/asset/link/security-integrity checks. The retired alishanaver72 Worker was not used.
- Live Pages verification passes 13 endpoints and the missing-file 404 check. The new website scripts and three-choice banner were confirmed in the browser.
- Live UI: Decline + reload yielded zero Google measurement script elements and denied consent attributes. Analytics + ads yielded granted analytics/ad-measurement attributes and loaded GTM/GA4. Switching back to Analytics only yielded analytics granted / ad measurement denied. These browser observations validate the site's consent wiring; they do not replace Google's processing of real attributed traffic.
- At 320 × 700 px: all three buttons fit, each is approximately 80 × 49 px, banner height is about 137 px and starts at y=555. Page scroll width is 305 px with a 320 px viewport; no horizontal overflow was observed. The viewport override was reset afterwards.
- No own ad was clicked, no call placed and no WhatsApp message sent during QA. Direct QA visits used km_debug=1.

## Processing and limitations

The implementation cause is corrected and published. Google's aggregate consent diagnostics may still reflect historical denied signals and low visitor volume. The urgent warning must not be described as cleared until Google's updated diagnostic actually shows that. Personalisation consent intentionally remains denied, because personalised advertising is not enabled. Visitors who decline or choose analytics-only must continue to be reported truthfully.

Google documents that Ads consent status may take 48 hours and in some instances up to two weeks to update. That is a reporting window, not a promise that every GTM alert will disappear within 48 hours. The 0% alert is not manually dismissed and defaults were not changed to unconditional granted. No conversion-modeling eligibility or recovered historical leads is claimed.

Sources: [Google consent troubleshooting](https://support.google.com/tagmanager/answer/14522438), [verify consent and processing timing](https://support.google.com/tagmanager/answer/14218557), [tag diagnostics](https://support.google.com/tagmanager/answer/14681508).

Evidence is in proof/2026-10-31/consent-fix/: published GTM version, successful Google tag detection, cleared Ads setup notices and the live mobile banner.
