# Mobile content focus — interaction checks

Date: 25 October 2026.

Only `website-openai/script.js` was changed in this interaction task. Existing navigation, consent, cookie cleanup, sticky contact visibility, reveal behavior and CTA analytics logic remain in place.

Added behavior:

- Native `details[data-mobile-fold]` remains open in source HTML for visitors without JavaScript.
- At 700px and below, supplementary disclosures initially close and remember each visitor choice in a WeakMap for the current page session.
- Above 700px, disclosures open automatically. Returning to mobile restores each disclosure's previous mobile state.
- Programmatic changes distinguish pending/coalesced native toggle events from summary activation, avoiding state corruption during rapid breakpoint changes.
- Marked direct children of `main` move into numeric `data-mobile-order` order on mobile. The original node order is restored exactly on desktop. This keeps the visual, keyboard and reading orders aligned.
- Initial fragments, hash changes and ordinary same-document anchor clicks open all details ancestors of their target, then scroll to the target. Modifier-clicks and links targeting another tab retain native behavior. Malformed and missing fragments are ignored.
- Focus is preserved where possible when main sections are moved.

Validation:

- `node --check website-openai/script.js` passed.
- A temporary Node VM harness exercised the actual disclosure/ordering block with DOM, media-query and asynchronous toggle stubs. Assertions passed for: mobile initial collapse; desktop initial open; independent saved mobile states; rapid resize and coalesced toggle events; opening nested native details for a fragment; initial deep links; unknown/malformed fragments; the extra-products disclosure; exact desktop node-order restoration; and absence of toggle loops.
- These are logic checks. The parent task handles final browser layout and live interaction verification.

No build, deployment, browser interaction or HTML/CSS edits were performed by this subtask.
