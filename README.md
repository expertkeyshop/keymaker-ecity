# Deployment targets (28 October 2026)

Repository: https://github.com/expertkeyshop/keymaker-ecity

- **Primary website:** https://keymaker-ecity.pages.dev/ — root `cloudflare-pages/`, build `npm run build`, public output `dist/`, Pages project `keymaker-ecity`.
- **Backup website:** https://keymaker.electronicity.workers.dev/ — root `cloudflare-workers/`, build `npm run build`, deploy `npm run deploy`, existing Worker `keymaker`.
- **Shared source:** `website-openai/`. Both targets build the same current website, including the 28 October PageSpeed, image and agent-catalog fixes. Edit this source once to update both deployments.
- **CI/CD:** Pages deploys through its native Git integration; the backup deploys through GitHub Actions using an encrypted, limited Worker token. Separate workflows validate pull requests. Changes to shared source trigger both targets from `main`.
- **SEO:** the Pages address is canonical everywhere. The backup serves the same site with an additional `noindex, follow` response header. An outage does not automatically switch customer traffic to the backup.

See [CLOUDFLARE-DEPLOYMENT.md](CLOUDFLARE-DEPLOYMENT.md) for exact dashboard settings, validation commands and deployment status. The root `index.html` is the owner's checklist and must never be configured as the customer homepage.

---

The sections below retain the earlier workspace documentation. The target configuration above supersedes old hostnames, build locations and archive references.
# Keymaker Ecity

Website and business-profile workspace for **Key Maker & Locksmith | Electronic City**, Bengaluru.

Customer website: [keymaker-ecity.pages.dev](https://keymaker-ecity.pages.dev/).

The former `keymaker-ecity.alishanaver72.workers.dev` hostname is retired. Do not use it in links, Analytics, Search Console integrations, canonical URLs or deployment targets.

## Website source and deployment

The customer website lives in `website-openai/`. The root `index.html` is the owner's Google Business Profile checklist, so it should not be used as the customer homepage.

Build the customer site from the repository root with Node.js:

```sh
node website-openai/build.mjs
node website-openai/preview.mjs
```

The preview serves `http://127.0.0.1:8126/`. Deploy the contents of **`website-openai/dist/`** using the existing Cloudflare static-site workflow. Its image assets are included in this repository. The builder copies HTML, CSS, JavaScript and verification files and generates discovery files; it does not regenerate image assets or ZIP archives.

ZIP archives dated 25 October 2026 are historical snapshots. For the current website, build from `cloudflare-pages/` and deploy its `dist/` output, or push the shared source to `main` for the configured Git deployment.

Other ZIPs and the `keymaker-ecity-website-bundle/` directory are earlier snapshots retained for history.

The configured production origin is `https://keymaker-ecity.pages.dev/`. Keep this origin for both deployment targets so the primary site's canonical and discovery URLs remain consistent. Building and pushing the repository do not themselves confirm a live deployment, Analytics collection or Google indexing.

See [`website-openai/README.md`](website-openai/README.md), [`AI-DISCOVERY.md`](AI-DISCOVERY.md) and [`SEARCH-CONSOLE-VERIFICATION.md`](SEARCH-CONSOLE-VERIFICATION.md) for the deployment and discovery checks. The old `.openai/hosting.json` is retained as historical Sites metadata.

## Owner checklist and business materials

- `index.html`, `styles.css`, `app.js` — owner checklist; progress is saved in the current browser, not read live from Google.
- `CURRENT-PENDING.md`, `GMB-EXECUTION.md` — recorded follow-up tasks and execution history.
- `business-content.json` and the service, product, FAQ, update and directory drafts — business information and publishing records.
- `business-images/` — original business photos and their manifest.
- `product-images/` — representative product illustrations and their manifest.
- Review assets, support correspondence, screenshots, design references, `website-backups/`, QA reports and earlier deployment archives — retained project materials.
- [`docs/WORKSPACE-HISTORY.md`](docs/WORKSPACE-HISTORY.md) — the original workspace README, preserving its chronological notes. Later records supersede earlier statements.

To preview the owner checklist, run `node server.cjs` and open `http://127.0.0.1:4173/`.

The `prepare-*.py`, `record-*.py` and `finalize-*.py` scripts are historical record-editing helpers. Do not run them as a build or test suite: they can overwrite business records. `verify.cjs` is a historical checklist test, not a current deployment check.

## Public repository copy

This repository contains the project files synchronized from the local `keymaker` workspace on 25 October 2026, including source, static builds, photos, archives and business records. Nested Git metadata, the temporary sync checkout, caches and `debug.log` are excluded. Private Gmail message/thread identifiers in support records are replaced with `redacted-private-message-id`; the original local records are preserved.
