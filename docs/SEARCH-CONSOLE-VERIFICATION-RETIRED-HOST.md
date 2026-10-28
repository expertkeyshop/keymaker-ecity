# Search Console verification

Property type: URL prefix.

Property URL: https://keymaker-ecity.alishanaver72.workers.dev/

The owner supplied `googlea8f5575206e3c038.html`. Its content is `google-site-verification: googlea8f5575206e3c038.html`. Original bytes are preserved in the source and bundle.

Expected public file URL:

https://keymaker-ecity.alishanaver72.workers.dev/googlea8f5575206e3c038.html

Status: prepared locally; the public path returned **404** when checked before this updated bundle was redeployed. Search Console ownership has not been verified by the agent.

1. Upload `keymaker-ecity-website-bundle.zip` to the existing Cloudflare deployment.
2. Open the expected file URL and confirm it shows the exact verification content above, not the homepage or a challenge.
3. Return to the same URL-prefix property's HTML file verification panel and press **Verify**.
4. Keep the verification file in future deployments. The build now preserves it automatically.
5. Once ownership is confirmed, submit `https://keymaker-ecity.alishanaver72.workers.dev/sitemap.xml` in Search Console and inspect the homepage for indexing.

No DNS TXT record is needed for this HTML file verification method. No Google or Cloudflare account settings were changed by preparing this file.
