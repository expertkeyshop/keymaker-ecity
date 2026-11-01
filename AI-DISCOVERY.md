# Search and AI discovery — current guidance, 2 November 2026

The primary website is **https://keymaker-ecity.pages.dev/**. Use the shared website-openai/ source and cloudflare-pages/ build target. Historical Worker hostnames and older ZIPs below are superseded.

Release 93ff01b is deployed and live-verified. Business JSON-LD now includes the verified shop coordinates, customer languages and owner-confirmed Justdial identity reference. The same languages appear in the contact section, and business.md supplies matching facts. The agent-catalog aliases remain valid; they advertise a real enquiry reference, not a fictional booking API.

Build and live checks cover readable HTML, canonical, robots, XML sitemap, business JSON/Markdown, llms.txt, catalog aliases, the enquiry skill, privacy, script integrity, security headers and verification files. Both GitHub workflows passed. Analytics-only file changes now trigger CI validation too. Homepage and privacy sitemap dates follow their own actual revision dates.

Google's exact sitemap live fetch passed again on 2 November. One submission of the updated sitemap was accepted; the report still says Couldn't fetch / 0 pages. Google processing remains open. Submission acceptance must not be described as successful sitemap processing, and valid files should not be repeatedly changed simply to chase the badge.

All 13 Google posts and 11 products had their destinations audited and corrected to Pages in the 29 October finishing pass; the earlier five-retired-post-links item is resolved. Justdial has owner public sign-off. Sulekha's public website/address/About synchronization still requires its support team; the user chose to send the 2 November follow-up from the client account.

See CURRENT-PENDING.md and analytics/README.md for current status. These accessibility and factual-discovery improvements cannot guarantee Google rankings, indexing, or AI recommendations.

---

## Historical record — 24 October 2026

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

## Final access and pricing consistency check — 29 October 2026

The primary website is https://keymaker-ecity.pages.dev/ . A focused live check found quote-based product copy and no numeric product/service price fields in the homepage or business.json. No website pricing change was needed when the remaining Google product example prices were removed.

One normal-client request and one request for each official GPTBot/1.4 and OAI-SearchBot/1.4 identifier returned HTTP 200, the real HTML homepage, an index/follow robots header and no cf-mitigated challenge header. Live robots.txt returns 200, allows User-agent: * at / and names the correct Pages sitemap. No user-agent-level access fault was reproduced; no security configuration was changed. These probes did not originate from verified OpenAI crawler IPs and do not demonstrate actual AI indexing or recommendations.

Google's exact sitemap live test also fetched successfully with crawling allowed. The Sitemaps report still shows Couldn't fetch after one accepted controlled resubmission, so its processing result remains open. The indexed homepage's current Pages canonical is already confirmed. Do not change valid files or repeatedly submit unchanged sitemaps to manufacture a completed status.
