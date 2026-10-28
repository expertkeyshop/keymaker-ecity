# Separate Cloudflare deployment targets

Repository: https://github.com/expertkeyshop/keymaker-ecity

| Setting | Primary Pages site | Backup Worker |
| --- | --- | --- |
| Existing application | Pages `keymaker-ecity` | Worker `keymaker` |
| Branch | `main` | `main` |
| Root directory | `cloudflare-pages` | `cloudflare-workers` |
| Build command | `npm run build` | `npm run build` |
| Output directory | `dist` | `dist`, configured in Wrangler |
| Deploy command | Managed by Pages | `npm run deploy` |
| Node version | 22 | 22 |
| Website | https://keymaker-ecity.pages.dev/ | https://keymaker.electronicity.workers.dev/ |

Both folders build the shared `website-openai/` source. Their `dist/` folders are generated and Git-ignored. Each target validates public-file boundaries, canonical URL, catalog JSON, security hashes, Search Console verification, image references and links before publication. The two `package-lock.json` files pin Wrangler and dependencies. Separate GitHub Actions workflows use read-only GitHub permissions and validate pull requests without Cloudflare credentials.

Pages uses its native Git integration and deploys production on pushes to `main`. The backup Worker uses its GitHub Actions workflow and the encrypted repository secret `CLOUDFLARE_WORKERS_API_TOKEN` (the approved Workers Scripts / Edit token for the configured account). The native Worker build-token picker does not list this limited token; using Actions avoids generating Cloudflare's broader default token. Do not also enable native Workers Builds. Pull requests validate only; they do not deploy. Pages preview branches are disabled. Build watch paths must include the target folder, `website-openai/**` and `scripts/**`; the default watch-all setting is safe if selective watches are not available.

## Local checks

```sh
node cloudflare-pages/build.mjs
node cloudflare-workers/build.mjs
```

Run builds sequentially because both regenerate the shared intermediate `website-openai/dist/`. Cloudflare and GitHub run the targets in separate checkouts, so their jobs do not share this intermediate output.

The backup keeps Pages canonical URLs and sends `X-Robots-Tag: noindex, follow`. It uses true 404 responses rather than a single-page fallback, so missing agent-catalog files cannot silently return homepage HTML. This is an independently deployed backup, not automatic traffic failover.

## Status

Prepared and locally verified on 28 October 2026. Repository push, Cloudflare connection and live deployment must each be verified separately; file preparation alone does not establish that production has changed.
