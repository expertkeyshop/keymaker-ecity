# Website interaction verification — 25 October 2026

Changed file: `website-openai/script.js` (4,675 bytes; no dependencies).

Validation: `node --check website-openai/script.js` passed. A Node VM with DOM, media-query and IntersectionObserver stubs exercised the behavior below. This is logic verification; visual browser verification is handled separately.

- Mobile navigation opens and closes, updates its accessible label and `aria-expanded`, and disables focus inside the closed navigation with `inert`.
- Escape closes the open menu and restores focus to its button. Selecting a navigation link closes it without blocking navigation.
- At the 801 px desktop breakpoint, navigation becomes available and its mobile `aria-hidden` state is removed. Returning to mobile restores the closed state.
- Loading the script twice, including before DOM ready, does not duplicate listeners or analytics events.
- Call, WhatsApp and directions links each generate one corresponding GA4 event. Approved link destinations remain unchanged. Cancelled clicks and unavailable or throwing analytics do not block navigation.
- Tracking sends only bounded static `data-section` and `data-item` labels, with no form fields, destination URLs, phone numbers or additional page-view events.
- The header scroll listener is passive and changes its state after 16 px.
- Reveal elements are unobserved after first appearance; delays are capped at 240 ms. Hero content and direct call-to-action elements remain visible.
- Reduced-motion preferences, including changes while the page is open, leave content visible. Missing IntersectionObserver also leaves everything visible.

CSS integration uses `.reveal-ready [data-reveal]:not(.is-visible)` and the `--reveal-delay` custom property. All page content remains visible if JavaScript does not initialize.

Google Ads conversion tracking needs a real Ads destination/conversion identifier; none was invented. Existing GA4 receives contact events when available.
