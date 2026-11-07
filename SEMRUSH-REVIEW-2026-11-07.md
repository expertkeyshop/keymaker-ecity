# Semrush interpretation and setup — 7 November 2026

Update: the user has now provided the exact issue destinations and all eight crawled URLs. See `SEMRUSH-FIXES-2026-11-07.md` for the diagnosis, published code changes and live verification. The earlier missing-details statements below describe the initial report only; they are no longer outstanding requests to the user. The GitHub push and deployment blocker is resolved; the Semrush account re-audit remains open.

Source: user-supplied dashboard text and two keyword-setup screenshots. No signed-in Semrush account was read or changed: browser runtime still fails with “failed to write kernel assets: path not found”. No Semrush connector is currently available.

## What the supplied report establishes

- Site Audit reports 93% health, 1 error, 17 warnings and 8 crawled pages. It provides no issue titles or affected URLs, so the error cannot yet be diagnosed or marked resolved. The counts may include repeated occurrences; they do not prove 18 different defects.
- The keyword setup images show Added: 0 and a 0/10 limit. The separately pasted dashboard says data collection is in progress. These could be different moments. Verify the current tracked-keyword list before starting another campaign or duplicating keywords.
- Organic/AI metrics marked n/a are unavailable measurements. They are not verified zero visits, zero mentions or zero Google rankings. Semrush's main keyword database can miss local-only queries; Search Console's actual impressions/clicks remain relevant first-party evidence. Authority Score is a Semrush metric, not Google's score for the shop.
- The Odoo-labelled comparison and software-query explanation strongly suggest platform-level scope or a generated-summary mismatch. The reported 383.1K must not be attributed to the individual locksmith without inspecting the subdomain-scoped report. The same scope check applies to Localo's 138.4K. This is a diagnosis to verify, not proof of an account setting we have inspected.
- Site health is a weighted technical audit score. It does not measure a probability of ranking first, customer demand or enquiries.

## Proposed configuration within the displayed 10-keyword allowance

1. Reuse the existing project. Target the exact shop host keymaker-ecity.pages.dev, using the scope that restricts results to this subdomain. Verify that Semrush does not broaden the target to all of pages.dev.
2. Search engine Google; device Mobile; location postal code 560100, Karnataka, India; language English. Mobile is a sensible starting assumption for urgent local enquiries, not a conclusion from analytics. Confirm device/location before launch, since Semrush restricts changing them on an existing target.
3. For Local Pack identification, use the exact confirmed GBP name: Key Maker & Locksmith | Electronic City.
4. For Only Keywords, paste SEMRUSH-KEYWORDS-560100.txt. For Tagged Keywords, paste SEMRUSH-TAGGED-KEYWORDS-560100.txt. Use one format, not both. Click Add keywords to campaign, verify 10 unique terms, then Start Tracking. If a target is already running, edit its tracked keywords instead.
5. Do not start a trial, buy extra tracking capacity, change email subscriptions or expand targeting as part of this preparation. The current screenshot's email tick is a user preference to review before submitting.
6. Let the initial collection finish; Semrush documents that fresh ranking collection can take up to an hour, despite the dashboard's shorter estimate. No result after collection can mean the shop is outside the tool's measured results for the selected keywords/location/device; inspect the SERP snapshots instead of treating it as a broken website.

The ten proposed phrases reflect confirmed services and local enquiry intent. They are seed terms, not a claim of measured search volume or guaranteed leads. After data arrives, replace weak terms using genuine Search Console queries and business outcomes. The list deliberately has no unsupported arrival-time promise.

## Competitor comparison

Use exactly armanlockandkeys1.odoo.com and professional-key-makers.localo.site with matching subdomain scope, country, date range and device where available. Do not compare the shop with the whole Odoo, Localo or Pages platform. Check each competitor actually serves the shop's local market.

For M.D Key Makers & Lock Repair, confirm its actual business website before adding it as a domain competitor. Do not invent a URL or assign a hosting platform's traffic to it. Compare Local Pack presence separately from organic website positions and sponsored placements. A single 560100 tracking location is not a measurement of every point across the 10 km service radius.

## Initial Site Audit assessment — superseded by the fixes report

Open Issues, then the error and warning groups. Obtain each issue title, affected URL and crawler explanation. Review the eight crawled URLs and audit date relative to today's deployment. Do not guess that the one error is the sitemap, canonical, schema or tracking installation.

Today's live deployment checks passed the public sitemap, robots, canonical metadata, catalog, Google verification file, favicon, sharing image, script integrity and true 404 behaviour. Those checks do not replace Semrush's specific findings. If the audit predates the published fixes, rerun it once after confirming the build is live; do not alter working code simply to force a score of 100.

Once the concrete issue is known: reproduce it, fix the source, run the relevant validation, deploy, rerun the audit and record whether the issue cleared. Review each warning for customer/indexing impact rather than applying every suggestion indiscriminately.

## Outcome measures

Keep separate records for: technical issue resolution; tracked organic positions; Local Pack presence; actual Search Console clicks/impressions; Ads spending and calls; unique owner-confirmed enquiries and paid jobs. An increase in Semrush score or estimated traffic alone is not proof of more business.

## Official references

- No data: https://www.semrush.com/kb/65-no-data
- Position Tracking configuration: https://www.semrush.com/kb/548-configuring-position-tracking
- Initial collection: https://www.semrush.com/kb/1113-why-is-position-tracking-not-showing-any-rankings
- Site health: https://www.semrush.com/kb/540-site-audit-overview
- Specific issues: https://www.semrush.com/kb/541-site-audit-issues-report
- Domain/subdomain scope: https://www.semrush.com/kb/254-domain-overview

## Signed-in completion update — 7 November, after the initial report

The initial browser blocker is resolved. The existing Position Tracking target incorrectly tracked `pages.dev` as a root domain. It has now been saved as **keymaker-ecity.pages.dev, Subdomain**, with local-pack business name **Key Maker & Locksmith | Electronic City**. The existing Google / 560100, Karnataka, India / English / Desktop target and weekly email preference were retained; the earlier proposed Mobile setup was not applied to this running target.

Saved keywords (10/10): key maker; key maker near me; key makers near me; locksmith near me; key maker electronic city; duplicate key maker electronic city; car key maker near me; bike key maker near me; lock repair near me; emergency locksmith electronic city. Results need fresh collection; zero/empty initial figures do not establish actual universal rankings.

Site Audit scope was already the correct host with subdomains excluded. The www 404 has zero internal source links. Crawl pacing was changed from Minimum to one URL per two seconds. Rerun was attempted once and blocked by “You've reached your monthly limit for crawled pages”; the popup also displayed 8/100 pages. No trial or upgrade was activated. Therefore the old 93% score was not re-certified after the live code fixes. No audit checks or individual findings were hidden.

The earlier statements about no signed-in access and unchanged settings are historical and superseded by this section. The original proposed keyword files are preparation artifacts; this saved list is authoritative. Google first-party Web and generative-AI performance data is recorded separately in the local client report.
