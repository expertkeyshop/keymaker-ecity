# Cloudflare Workers: backup website

Existing Worker: `keymaker` in the configured Cloudflare account. Dashboard address observed on 28 October 2026: https://keymaker.electronicity.workers.dev/

This folder is its deployment root. `npm run build` builds and verifies the shared source in `../website-openai/`, then copies the public files into this folder's `dist/`. Wrangler deploys static assets directly with real 404 responses and extension-free HTML routes. No server script or database is needed for this site.

```sh
cd cloudflare-workers
npm ci
npm run build
npm run deploy
```

The primary canonical URL remains https://keymaker-ecity.pages.dev/. The backup sends `X-Robots-Tag: noindex, follow` to keep search indexing focused on the primary website while remaining usable as a backup.

The GitHub Actions workflow `.github/workflows/cloudflare-workers.yml` validates relevant pull requests and pushes and can also be run manually. Production deployment is handled by Cloudflare's native Workers Builds connection to `expertkeyshop/keymaker-ecity`, branch `main`. Do not enable a second production deployment in GitHub Actions.

Native configuration: repository `expertkeyshop/keymaker-ecity`, branch `main`, root `cloudflare-workers`, build `npm run build`, deploy `npm run deploy`. The Worker name must match `wrangler.jsonc`. Reuse an existing authorized deployment token where available; no token value belongs in source control. The historical `keymaker-ecity.alishanaver72.workers.dev` hostname was not present in the currently signed-in account's application list.
