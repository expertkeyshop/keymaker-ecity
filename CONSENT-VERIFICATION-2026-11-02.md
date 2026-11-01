# Google consent verification — 2 November 2026

The consent implementation is published and its effective Google SDK state has been verified. Google's aggregate **0% consent rate** diagnostic is still present in the fresh check on 2 November; it has not been dismissed or described as cleared.

## Published configuration

- Website: https://keymaker-ecity.pages.dev/
- Container: GTM-PKCWS4Z8. Version 3 introduced the visitor-choice advertising-measurement fix on 31 October at 4:46 PM IST.
- Version **5**, published on 31 October at **5:54 PM IST**, is the current saved export. It includes a read-only QA consent verifier; the four existing production tags and three existing triggers were preserved.
- Workspace 6 has **zero unpublished changes** in the 2 November check.
- No budget, billing, targeting, customer-data uploads, remarketing settings or website security headers were changed during verification.

## Live SDK results

The live check used Google's documented `isConsentGranted` API inside a sandboxed GTM template, deferred with `callLater` until queued consent updates settled. These are Google's effective client-side flags, rather than the website's own consent attributes.

| Visitor choice | analytics_storage | ad_storage | ad_user_data | ad_personalization |
| --- | --- | --- | --- | --- |
| Analytics + ads | Granted | Granted | Granted | Denied |
| Switch to Analytics only | Granted | Denied | Denied | Denied |
| Decline / withdraw | Denied | Denied | Denied | Denied |

The readings were captured on 31 October at approximately 5:54–5:55 PM IST. A reload after Decline produced **zero Google measurement script elements**. No paid ad, phone link or WhatsApp enquiry was clicked to conduct these tests. Contact clicks were not fabricated.

Machine-readable console evidence is preserved in `analytics/qa-consent-results-2026-10-31.json`. It contains only four consent booleans, timestamps and the public GTM script URL. This proves client-side application of the consent update; it does not establish Google's server-side aggregate consent rate or completed customer enquiries.

The subsequent signed-in **GA4 Admin → Consent settings** check on 2 November reports **Excellent**, **No issues detected in this property**, with both behavioral analytics and advertising consent signals **Active** for the keymaker-ecity stream. The page specifically lists active analytics_storage, ad_storage, ad_user_data and ad_personalization signals. Active means the signal is being communicated, not that a user granted it or that remarketing was enabled. This is Google's received-signal status; the separate GTM aggregate warning remains open. Proof: proof/2026-11-02/completion/analytics-consent-excellent.png.

## QA verifier and maintenance

The verifier fires only for `km_consent_update` or `km_analytics_ready`, on the primary hostname and with `DLV - debug_mode` equal to true. It independently checks `getQueryParameters('km_debug') === '1'`. Ordinary visits do not produce this diagnostic output.

It reads the four consent states and logs the fixed `KEYMAKER_CONSENT_SDK` marker locally. It has no consent write, cookie, network or global-variable permissions. URL access is restricted to the `km_debug` query key. Tag consent settings remain `NOT_SET`, with no override that could force `isConsentGranted` to return true. Denied-state tests also confirmed the result is not always true.

Use `https://keymaker-ecity.pages.dev/?km_debug=1`, open Cookie settings, select a choice and inspect the console marker. These direct visits are labelled developer traffic. The console check avoids dependence on Tag Assistant's popup, which repeatedly disconnected in this browser. Cross-Origin-Opener-Policy was not weakened to work around that connection problem.

`analytics/gtm-container-ready.json` is the exact version-5 export retrieved from Google's JSON Preview. `analytics/keymaker-consent-debug.tpl` matches its saved template. `node scripts/test-analytics.mjs` passes the website consent tests, GTM bindings and hostname gates, all bridge consent combinations, and the QA template's deferred reads, documented query API signature, restricted read-only permissions and exact export consistency.

## Remaining diagnostic status

The fresh GTM UI still shows **Container quality: Urgent → 0% consent rate detected in some regions**. The implementation no longer forces advertising measurement to denied after explicit opt-in, as demonstrated above. The report may reflect historical traffic, actual visitor choices or processing delay; those explanations remain inferences. The console results do not reveal which explanation currently drives Google's aggregate alert.

The subsequent Monitored domains inspection lists only `keymaker-ecity.pages.dev` as auto-detected, no manually added domains and zero ignored domains. No retired ChatGPT or Worker hostname appears in that list, so a stale monitored-domain selection is not supported as the explanation. Monitoring was preserved rather than excluding the primary domain to suppress its alert. Screenshot: `proof/2026-11-02/migration/gtm-monitored-primary-only.png`.

The diagnostic must be re-evaluated by Google against subsequent genuine traffic. There is no verified completion date for clearing it. Keep declined and analytics-only choices truthful; do not switch all visitors to granted, manufacture opt-ins or hide the issue merely to remove a warning. If it persists despite genuine opted-in traffic, provide the published version, three-state results and diagnostic screenshot to Google support.

Primary references: [Google's consent API](https://developers.google.com/tag-platform/tag-manager/templates/api#isConsentGranted), [template permission controls](https://developers.google.com/tag-platform/tag-manager/templates/permissions), [tag diagnostics](https://support.google.com/tagmanager/answer/14681508), and [verify consent implementation](https://support.google.com/tagmanager/answer/14218557).
