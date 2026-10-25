# Reference redesign — browser verification

Verified on 25 October 2026 with the built `website-openai/dist/` website served locally. This does not assert a production deployment or a Lighthouse score.

- The local HTTP homepage returned 200. The preview server needed execution outside the network sandbox; the browser's direct local-file navigation was unavailable.
- Desktop (1280 px), tablet (820 px), and mobile (390 px and 320 px) had no document horizontal overflow. The decorative hero outline extends within a clipped hero container by design.
- All 22 images loaded successfully. The page showed the real logo, storefront and work photographs alongside clearly labelled illustrative images.
- Inspected the desktop hero and services grid, tablet hero/navigation, and mobile hero/product catalogue. Contact actions remain visible in the hero and the fixed mobile contact bar.
- Mobile navigation opened and closed; selecting Products moved to its anchor and closed the menu. Closed navigation had `inert`. Escape closed the menu and restored focus to its button.
- The native payment FAQ opened and closed by click, and toggled with Enter while its summary held focus. Its cash/UPI/IMPS/NEFT answer matched the confirmed payment methods.
- Product contact buttons measured 44 px high on mobile. Call and WhatsApp destinations were checked structurally; no test calls or messages were sent.
- JavaScript behavior tests separately covered reduced motion, missing IntersectionObserver, duplicate initialization and GA4 contact event routing. No production analytics event delivery or Ads conversion was asserted.

Browser-led refinements: mobile anchor navigation uses immediate scrolling; product text/contact targets were enlarged; illustration alt text describes the actual generated scenes; FAQ heading whitespace reads naturally.

Preview captures: `website-previews/redesign-desktop.jpg` and `website-previews/redesign-mobile.jpg`.

Static build and archive checks are recorded in `QA-results-v2-build.md`; interaction logic checks are in `QA-results-v2-js.md`.
