# Mobile content focus — local review build

Updated 25 October 2026. No commit or deployment was made.

## Changes

- At widths up to 700px, the customer journey is hero/contact, six services, three products, shop details, then expandable supporting content.
- Cards use brief descriptions, 1.4 line height, tighter margins and 54–64px thumbnails. Call and WhatsApp actions retain a 44px minimum height.
- The other three products, specialist details, FAQs, coverage, about text and shop photos remain available in native disclosures.
- Decorative hero imagery and repeated promotional sections are hidden on mobile. Desktop retains full copy and its original section order and grid breakpoints.
- Disclosures remember choices across viewport changes. Deep links expand their ancestors. Source HTML keeps disclosures open without JavaScript.
- The deployable dist includes the additional mobile-focus.css stylesheet.

## Checks completed

- Node syntax checks and static build passed: 30 image assets, six service groups and eight FAQs.
- HTML nesting, unique IDs and internal fragment targets checked; no issues found.
- All six service cards and six product cards remain in HTML. No existing contact links were removed.
- No missing local assets or page links were found in homepage/privacy HTML.
- Original base stylesheet, privacy page and security headers are unchanged from the pre-change backup.
- Source and built mobile stylesheet match; structured business JSON and Google verification file remain valid.
- Disclosure/order logic passed a Node VM check, including rapid breakpoint changes, independent disclosure choices, nested fragments and desktop order restoration. See QA-results-mobile-focus-js.md.
- HTTP check returned 200 from http://127.0.0.1:8126/ and confirmed the new mobile stylesheet link is being served.

## Visual checks pending

The browser tool returned “Local browser use is disabled in Work settings” before and after the user's access confirmation. No rendered screenshot, viewport measurement, Axe or Lighthouse result is claimed for this revision. Review the served page at 320px, 390px, 700/701px and desktop once browser access is restored, including expandable products and sticky contact behavior.

Backup: website-backups/before-mobile-focus-2026-10-25/.
