# Keymaker Ecity

Website and business-profile workspace for **Key Maker & Locksmith | Electronic City**, Bengaluru.

Customer website: [keymaker-ecity.alishanaver72.workers.dev](https://keymaker-ecity.alishanaver72.workers.dev/).

## Website source and deployment

The customer website lives in `website-openai/`. The root `index.html` is the owner's Google Business Profile checklist, so it should not be used as the customer homepage.

Build the customer site from the repository root with Node.js:

```sh
node website-openai/build.mjs
node website-openai/preview.mjs
```

The preview serves `http://127.0.0.1:8126/`. Deploy the contents of **`website-openai/dist/`** using the existing Cloudflare static-site workflow. Its image assets are included in this repository. The builder copies HTML, CSS, JavaScript and verification files and generates discovery files; it does not regenerate image assets or ZIP archives.

The current ready-to-upload copies are:

- `keymaker-ecity-website-bundle/` — the complete static website.
- `keymaker-ecity-website-bundle.zip` — its files at the archive root.
- `keymaker-ecity-website-preview.zip` — the same static files.

The 24 October 2026 bundle includes the owner's English WhatsApp booking link, GA4 tag `G-Q2CM2F0JB8`, the supplied Google Search Console verification file, canonical URLs, structured business data, sitemap, crawler preferences and plain-text business summaries. Local bundle checks do not confirm Cloudflare deployment, Analytics collection or Google indexing. This repository sync does not configure automatic deployment.

See [`website-openai/README.md`](website-openai/README.md), [`AI-DISCOVERY.md`](AI-DISCOVERY.md) and [`SEARCH-CONSOLE-VERIFICATION.md`](SEARCH-CONSOLE-VERIFICATION.md) for the deployment and discovery checks. The old `.openai/hosting.json` is retained as historical Sites metadata.

## Owner checklist and business materials

- `index.html`, `styles.css`, `app.js` — owner checklist; progress is saved in the current browser, not read live from Google.
- `CURRENT-PENDING.md`, `GMB-EXECUTION.md` — recorded follow-up tasks and execution history.
- `business-content.json` and the service, product, FAQ, update and directory drafts — business information and publishing records.
- `business-images/` — original business photos and their manifest.
- `product-images/` — representative product illustrations and their manifest.
- Review assets, support correspondence, screenshots and earlier deployment archives — retained project materials.
- [`docs/WORKSPACE-HISTORY.md`](docs/WORKSPACE-HISTORY.md) — the original workspace README, preserving its chronological notes. Later records supersede earlier statements.

To preview the owner checklist, run `node server.cjs` and open `http://127.0.0.1:4173/`.

The `prepare-*.py`, `record-*.py` and `finalize-*.py` scripts are historical record-editing helpers. Do not run them as a build or test suite: they can overwrite business records. `verify.cjs` is a historical checklist test, not a current deployment check.

## Public repository copy

This repository contains the project files copied from the local `keymaker` workspace on 24 October 2026, including source, static builds, photos, archives and business records. Nested Git metadata, the temporary sync checkout, caches and `debug.log` are excluded. Private Gmail message/thread identifiers in support records are replaced with `redacted-private-message-id`; the original local records are preserved.
