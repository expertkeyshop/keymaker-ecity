# Search and AI discovery — 24 October 2026

Business: Key Maker & Locksmith | Electronic City.

Production origin selected by the owner: **https://keymaker-ecity.alishanaver72.workers.dev/**.

## Latest bundle

`keymaker-ecity-website-bundle.zip` and `keymaker-ecity-website-preview.zip` contain the same updated static files. No Cloudflare deployment was performed by the agent for this update.

- Shop identity, address, phone, hours, payments, six service groups, 20 listed coverage areas and eight FAQs are available in the initial HTML. They do not rely on JavaScript or image text.
- Canonical, social, entity and sitemap URLs use the Workers origin.
- WebSite, WebPage, Locksmith and Service structured information describe the same real shop and services. No self-serving rating, unconfirmed coordinates or guaranteed response time was added.
- `robots.txt` retains wildcard access and explicitly allows Googlebot, bingbot, OAI-SearchBot, ChatGPT-User, PerplexityBot and Perplexity-User.
- The XML sitemap includes the homepage and genuine shop/work image URLs.
- `business.md` and `business.json` provide plain-text and structured business information generated from the page. `llms.txt` is a supplemental content index; it is not a guarantee that any AI system will read, index or recommend the shop.
- `_headers` configures correct response content types and permissive indexing/snippet headers for Cloudflare static assets. It does not override Cloudflare account or firewall policies.
- All five WhatsApp anchors retain the exact English link supplied by the owner, directly in HTML.

## Live check before this bundle is uploaded

Direct public HTTP requests to the deployed homepage, `/robots.txt` and `/sitemap.xml` returned **200** on 24 October 2026. No X-Robots-Tag restriction was returned in those requests. The homepage's robots meta allows indexing.

Important outstanding live defect: its canonical URL and sitemap still point at `keymaker-electronic-city.violetflame16.chatgpt.site`. The current bundle corrects those. Do not describe this correction as live until the new archive has been deployed and checked.

Browser inspection was unavailable because local browser use was disabled. No Cloudflare settings were inspected or altered. A successful ordinary public HTTP request does not prove access from a search crawler's verified IP addresses.

## After redeploying

1. Confirm `/`, `/robots.txt`, `/sitemap.xml`, `/business.md`, `/business.json` and `/llms.txt` return 200 with their correct content types, not a challenge/login page or a homepage fallback.
2. Confirm canonical, structured data, social images and sitemap URLs all use the Workers origin. Check for unexpected `noindex`, `nosnippet` or disallow rules in served headers and robots.txt.
3. In Cloudflare, review any AI Crawl Control, managed robots and WAF rules that could block verified search crawlers. Permissive robots.txt alone cannot override an upstream firewall. Keep normal security protections; identify actual crawler restrictions before changing rules.
4. Verify the exact HTTPS URL-prefix property in Google Search Console. The owner has now supplied `googlea8f5575206e3c038.html`; it is preserved byte-for-byte in the source verification directory, static root and updated ZIPs. Upload the latest bundle, confirm the verification URL returns that exact file, then press Verify in Search Console. The public verification URL returned 404 before redeployment. No successful ownership verification is claimed. Once verified, submit `sitemap.xml` and inspect the homepage.
5. Verify the same site in Bing Webmaster Tools if the owner chooses, and submit the sitemap there. No Bing property was created by this task.
6. Update the Google Business Profile and owned directory website fields to the confirmed final URL, avoiding duplicate listings. These external fields were not changed by this bundle update.
7. Monitor genuine impressions, clicks, calls, directions and referral sources. Keep hours, services and prices current and add genuine work photos. No automation or paid service was created.

## Official references

- Google AI features: https://developers.google.com/search/docs/appearance/ai-features
- Google local business data: https://developers.google.com/search/docs/appearance/structured-data/local-business
- OpenAI search and user-agent access: https://developers.openai.com/api/docs/bots
- Perplexity crawlers: https://docs.perplexity.ai/docs/resources/perplexity-crawlers
- Cloudflare crawler blocks: https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-waf/
- Cloudflare static headers: https://developers.cloudflare.com/workers/static-assets/headers/

Ordinary SEO requirements, useful factual content and crawler accessibility remain the foundation. Google does not require a special AI text file or AI-specific schema. Indexing, answer inclusion and recommendations are decisions made by each service, not settings this bundle can force.
