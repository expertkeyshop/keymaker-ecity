# Consent diagnostic recheck — 31 October 2026

**Superseded status:** The popup-based verification blocker described below was resolved using Google's read-only consent API. Live SDK readings confirmed Analytics + ads grants analytics_storage, ad_storage and ad_user_data; analytics-only denies both advertising flags; withdrawal denies all four flags. Personalisation stays denied. GTM version 5 is published and the exact export is saved. The 2 November check still shows Google's aggregate warning, with zero unpublished changes. See `CONSENT-VERIFICATION-2026-11-02.md` for the final evidence and remaining reporting limitation. The paragraphs below preserve the earlier check.

The user reported the same 0% consent warning again after the version-3 publication. The live GTM workspace is now draft 4 and has zero unpublished changes. Its diagnostic still lists one issue: 0% consent rate detected in some regions.

Only keymaker-ecity.pages.dev appears in auto-detected monitored domains. No custom or ignored domains are listed, and no retired Worker is contributing through this domain list. Monitoring was not disabled or changed.

Google's specific documentation says this diagnostic concerns always-denied **ad_user_data** in non-EEA regions. It is not, by itself, a requirement to enable personalised advertising. The published bridge grants ad_user_data and ad_storage for the explicit Analytics + ads choice, with personalization denied. Its analytics-only and decline paths retain denied advertising consent.

A fresh direct QA visit confirmed Analytics + ads sets the website's analytics and ad-measurement consent attributes to granted and loads both the container and Google tag. Source consent tests still pass using the actual exported version-3 template. These observations establish website wiring and template configuration, not independent receipt of the consent update by Google's servers.

One fresh Tag Assistant attempt after accepting measurement failed: the debugger reports Debug window closed / Could not connect. Repeating this connection failure does not independently prove an absent or broken published Google tag. The user was asked to click Reopen and keep the website debug window open so its Consent panel can be inspected. This is the remaining live-verification blocker; no further code, consent defaults or diagnostic-monitoring settings were changed in this pass.

The alert is still present and must not be described as cleared. It may include historical always-denied traffic and processing delay, but this is an inference until Google's updated diagnostic or the live Consent panel verifies the new incoming signal. The original fix was published at 4:46 PM IST on 31 October. No further change should be made solely to manufacture a nonzero consent rate.

References: https://support.google.com/analytics/answer/14681508?hl=en and https://support.google.com/tagmanager/answer/14218557 . The latter documents delayed Ads consent-status updates, not a guaranteed deadline for this GTM diagnostic.

Proof: proof/2026-10-31/consent-fix/diagnostic-recheck-still-pending.png. The debugger tab is retained for the user's connection step.
