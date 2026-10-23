# Website rename — 24 October 2026

**Cloudflare update:** The owner subsequently reported deploying at `https://keymaker-ecity.alishanaver72.workers.dev/`. The latest local bundle now uses this origin for canonical, social, structured-data, robots and sitemap URLs. All five WhatsApp links use the exact English URL requested by the owner. Upload `keymaker-ecity-website-bundle.zip` to the existing Cloudflare deployment. This latest correction has not been deployed by the agent. The Sites-specific plan below is historical and does not block Cloudflare redeployment.

Status: redesigned local source and static build are prepared and browser-tested. Hosting rename and live publication are blocked by Sites project access.

## Naming

- Owner-selected short URL label: **keymaker-ecity**.
- Candidate hosted address: `https://keymaker-ecity.violetflame16.chatgpt.site/`.
- Availability of that label has not been checked; the candidate is not a published address.
- Keep the owner-confirmed business branding: **Key Maker & Locksmith | Electronic City**.
- Prepared search title: **24/7 Key Maker & Locksmith | Electronic City, Bengaluru**.

## Access blocker

The project ID in `website-openai/.openai/hosting.json` was passed unchanged to the Sites connector. It returned `project_not_found` / `NOT_FOUND`. A recovery inventory of owned and editable Sites returned an empty list. The owning ChatGPT account or workspace must be selected before changing the existing Site. No duplicate Site was created and no alternate project ID was invented.

## Apply after access is restored

1. Confirm the existing Site and its public audience with `get_site`.
2. Request the `keymaker-ecity` slug using the native Sites slug-change operation; observe its asynchronous completion with `get_site`.
3. Open the existing source using its native source credential and the Sites workflow helper.
4. Replace the old origin in canonical, Open Graph/Twitter image URLs, WebSite and Locksmith JSON-LD URLs/IDs, `robots.txt` and `sitemap.xml` together. The redesigned title and content are already prepared. Preserve the exact confirmed business contact information.
5. Validate the changed source, package it from the pushed commit, and publish the same public Site. Check the new URL and any old-URL redirect behavior.
6. Update the GBP website field and owned directory links to the confirmed live URL; document any directory/support limitations.

## Search Console next

After the final address is live, add its exact HTTPS URL as a URL-prefix property, obtain the owner's verification tag or HTML file, publish that verification through the same source workflow, verify ownership, submit `sitemap.xml` and inspect the homepage for indexing. Inspect any existing Search Console property before attempting a move or creating redundant properties.

Google documentation:

- Property setup: https://support.google.com/webmasters/answer/34592
- Ownership verification: https://support.google.com/webmasters/answer/9008080
- URL migrations and redirects: https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes

Search Console verification and sitemap submission support indexing and monitoring. They do not guarantee a ranking position.

## Prepared website update

Source: `website-openai/index.html`, `styles.css`, `script.js`. Static output: `website-openai/dist/`.

The update uses the owner-chosen shop logo, cover/storefront photo, door-lock work photo and bike-key work photo. Responsive WebP variants, image dimensions, descriptive alt text, prioritised cover loading and lazy loading below the fold are included. It adds six service groups, 20 listed coverage areas, eight visible FAQs, mobile navigation and quick contact buttons, approved trilingual WhatsApp booking text, and consistent WebSite/Locksmith structured data.

Local HTTP readiness returned 200 after running the preview outside the restricted sandbox. Browser checks covered desktop and mobile layouts, navigation, FAQs, contact destinations, images and horizontal overflow. No field Core Web Vitals or ranking result is claimed.

The existing public website and business-profile website link have not changed. Canonical and sitemap still use the current confirmed live origin until the native rename succeeds.
