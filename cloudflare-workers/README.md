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

The GitHub Actions workflow `.github/workflows/cloudflare-workers.yml` validates relevant pull requests, builds and deploys pushes to `main`, and can also be run manually. It reads the encrypted repository secret `CLOUDFLARE_WORKERS_API_TOKEN`. The approved token has only Account / Workers Scripts / Edit on the configured Cloudflare account. It grants no database, storage, queue or zone-route permissions. Pull requests never use the token or deploy production. Keep native Workers Builds disconnected to avoid duplicate deployment triggers.

If native Workers Builds is deliberately enabled later, disable deployment in the GitHub workflow first. Native settings would be: repository `expertkeyshop/keymaker-ecity`, branch `main`, root `cloudflare-workers`, build `npm run build`, deploy `npm run deploy`. The Worker name must match `wrangler.jsonc`. The current native build-token picker does not list the limited custom token; its default token requests broader permissions. No token value belongs in source control. The historical `keymaker-ecity.alishanaver72.workers.dev` hostname was not present in the currently signed-in account's application list.
