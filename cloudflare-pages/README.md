# Cloudflare Pages: primary website

Production: https://keymaker-ecity.pages.dev/

This folder is the deployment root for the existing `keymaker-ecity` Pages project. `npm run build` builds and verifies the shared source in `../website-openai/`, then copies the public files into this folder's `dist/`. Keep business documents and the owner checklist outside the deployed folder.

```sh
cd cloudflare-pages
npm ci
npm run build
npm run deploy
```

The GitHub Actions workflow `.github/workflows/cloudflare-pages.yml` validates relevant pull requests and pushes and can also be run manually. Production deployment is handled by Cloudflare's native Git connection to `expertkeyshop/keymaker-ecity`, branch `main`. This avoids a second deployment trigger and requires no Cloudflare secret in GitHub Actions.

The current dashboard exposes a Connect control on the existing Pages project. Configure root `cloudflare-pages`, build `npm run build`, output `dist`, Node 22, and watch both this folder and `website-openai/` plus `scripts/`. If the platform refuses the connection, preserve the current project and URL; use a separately authorized Wrangler CI token rather than deleting/recreating production.
