# Separate Cloudflare deployment targets

Repository: https://github.com/expertkeyshop/keymaker-ecity

| Setting | Primary Pages site | Backup Worker |
| --- | --- | --- |
| Existing application | Pages `keymaker-ecity` | Worker `keymaker` |
| Branch | `main` | `main` |
| Root directory | `cloudflare-pages` | `cloudflare-workers` |
| Build command | `npm run build` | `npm run build` |
| Output directory | `dist` | `dist`, configured in Wrangler |
| Deployment runner | Native Pages Git integration | GitHub Actions |
| Deploy command | Managed by Pages | `npm run deploy` |
| Node version | 22 | 22 |
| Website | https://keymaker-ecity.pages.dev/ | https://keymaker.electronicity.workers.dev/ |

Both folders build the shared `website-openai/` source. Their `dist/` folders are generated and Git-ignored. Each target validates public-file boundaries, canonical URL, catalog JSON, security hashes, Search Console verification, image references and links before publication. The two `package-lock.json` files pin Wrangler and dependencies. Separate GitHub Actions workflows use read-only GitHub permissions and validate pull requests without Cloudflare credentials.

Pages uses its native Git integration and deploys production on pushes to `main`. The backup Worker uses its GitHub Actions workflow and the encrypted repository secret `CLOUDFLARE_WORKERS_API_TOKEN` (the approved Workers Scripts / Edit token for the configured account). The native Worker build-token picker does not list this limited token; using Actions avoids generating Cloudflare's broader default token. Do not also enable native Workers Builds. Pull requests validate only; they do not deploy. Pages preview branches are disabled. Pages build watch paths are `cloudflare-pages/*`, `website-openai/*`, and `scripts/*`; Cloudflare's `*` also includes nested paths. The Worker workflow watches its own folder plus the shared source and scripts.

## Local checks

```sh
node cloudflare-pages/build.mjs
node cloudflare-workers/build.mjs
node scripts/verify-live.mjs https://keymaker-ecity.pages.dev/
node scripts/verify-live.mjs https://keymaker.electronicity.workers.dev/ --backup
```

Run builds sequentially because both regenerate the shared intermediate `website-openai/dist/`. Cloudflare and GitHub run the targets in separate checkouts, so their jobs do not share this intermediate output.

The backup keeps Pages canonical URLs and sends `X-Robots-Tag: noindex, follow`. It uses true 404 responses rather than a single-page fallback, so missing agent-catalog files cannot silently return homepage HTML. This is an independently deployed backup, not automatic traffic failover.

## Status

Completed and live-verified on 28 October 2026:

- Commit `0cee43606f7a9f5311f8cb23c57ad30ae7b69cba` added both targets, validation workflows and the latest website fixes. Both GitHub checks passed.
- The existing Pages project connected successfully to `expertkeyshop/keymaker-ecity`, branch `main`, root `cloudflare-pages`, build `npm run build`, output `dist`. First Git deployment `72236e52-03db-4f3d-b646-65be0f4bd37d` succeeded in 19 seconds: https://72236e52.keymaker-ecity.pages.dev/
- Commit `706fdbcd6bd346ed5d90916c81c92ceb09330730` enabled the approved Worker deployment. Build, deploy and post-deploy verification all passed: https://github.com/expertkeyshop/keymaker-ecity/actions/runs/40630097263
- Both public hostnames passed live checks for canonical URL, application-script integrity, inline CSS security hashes, all three catalog aliases and their JSON MIME types, the enquiry skill, privacy page, robots, llms, sitemap, business data, Google verification and a real HTTP 404 for a missing JSON file.
- Pages returns `index, follow`; the backup returns `noindex, follow`. The backup remains independently accessible and does not automatically take over traffic during a Pages outage.
- The approved limited Worker credential is stored only as an encrypted GitHub Actions secret. No credential value was committed or written to the project files.

For later commits, inspect the Cloudflare Pages deployment status and the GitHub backup deployment workflow separately. A Git push alone is not proof that either deployment succeeded.
