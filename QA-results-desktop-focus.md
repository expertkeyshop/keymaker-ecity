# Desktop content refinement — 25 October 2026

Local review build at http://127.0.0.1:8126/. No commit or deployment.

## What changed

- Practical desktop order: hero/trust strip, services, products, visit details, genuine work photos, about, coverage and FAQs.
- Service images use 155px height and product images 150px. Card descriptions use 14px text with 1.5 line height; contact targets remain at least 44px high.
- All six services and six products remain visible on desktop. Two columns are used at 701–1100px and three above 1100px.
- Section padding is 48–64px; redundant promotional sections and repeated image badges are hidden. Real business photography, brand, links, compatibility explanations and quote details remain available.
- Changes are contained in desktop-focus.css, loaded only above 700px. The source section order changed while preserving data-mobile-order values and each section's original markup.

## Verification

- Build passed with 30 image assets, six service groups and eight FAQ entries.
- HTML nesting, one H1, unique IDs, fragment targets and local asset/page references checked successfully.
- All original section markup and contact links retained. Mobile section order is identical to the pre-desktop backup.
- styles.css, mobile-focus.css, script.js, privacy.html and _headers are byte-identical to the pre-desktop backup.
- Browser access was restored during the final pass. Layout measurements completed at 320, 390, 700, 701, 768, 800, 801, 900, 901, 1024, 1100, 1280, 1440 and 1920px: no horizontal page overflow, card/action overflow or visible text below 12px found.
- At 1440px: service cards measure 341px high; product cards approximately 314px. The product grid is three columns by two rows, and all responsive disclosures are open.
- Visually inspected desktop service/product grids and the 768px hero. Saved desktop screenshots in website-previews/desktop-focus-services.jpg and desktop-focus-products.jpg.
- At 390px, opening and closing More products works; product action targets remain at least 44px, and mobile section order is hero/services/products/visit followed by optional content. Resizing back to desktop opens all disclosures.
- No new Lighthouse or Axe scores are claimed for this revision.

Backup: website-backups/before-desktop-focus-2026-10-25/.
