import { copyFile, mkdir, readFile, writeFile, readdir } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";
const root = path.dirname(fileURLToPath(import.meta.url));
const dist = path.join(root, "dist");
await mkdir(dist, { recursive: true });
for (const filename of ["index.html", "styles.css", "script.js", "_headers"]) await copyFile(path.join(root, filename), path.join(dist, filename));
const verificationDirectory = path.join(root, "verification");
await mkdir(verificationDirectory, { recursive: true });
for (const entry of await readdir(verificationDirectory, { withFileTypes: true })) {
  if (!entry.isFile() || !/^google[a-f0-9]+\.html$/.test(entry.name)) continue;
  const verificationFile = path.join(verificationDirectory, entry.name);
  const contents = await readFile(verificationFile, "utf8");
  if (contents.trim() !== `google-site-verification: ${entry.name}`) throw new Error(`Invalid Google verification file: ${entry.name}`);
  await copyFile(verificationFile, path.join(dist, entry.name));
}
const html = await readFile(path.join(root, "index.html"), "utf8");
const origin = html.match(/<link rel="canonical" href="([^"]+)"/)[1];
const schema = JSON.parse(html.match(/<script type="application\/ld\+json">\s*([\s\S]*?)\s*<\/script>/)[1]);
const business = schema["@graph"].find(item => item["@type"] === "Locksmith");
const webPage = schema["@graph"].find(item => item["@type"] === "WebPage");
const areas = business.areaServed;
const services = business.hasOfferCatalog.itemListElement.map(item => item.itemOffered);
const map = business.hasMap;
const decodeText = text => text.replace(/<[^>]*>/g, "").replace(/&amp;/g, "&").replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/\s+/g, " ").trim();
const faqs = [...html.matchAll(/<details><summary>([\s\S]*?)<\/summary><p>([\s\S]*?)<\/p><\/details>/g)].map(match => ({ question: decodeText(match[1]), answer: decodeText(match[2]) }));
const robots = ["# Public business information; search crawlers may access all published assets.", "User-agent: *", "Allow: /", "", ...["Googlebot", "bingbot", "OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "Perplexity-User"].flatMap(agent => [`User-agent: ${agent}`, "Allow: /", ""]), `Sitemap: ${origin}sitemap.xml`, ""].join("\n");
await writeFile(path.join(dist, "robots.txt"), robots);
const escapeXml = text => text.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll('"', "&quot;");
const imageEntries = business.image.map(image => `<image:image><image:loc>${escapeXml(image)}</image:loc></image:image>`).join("");
await writeFile(path.join(dist, "sitemap.xml"), `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"><url><loc>${escapeXml(origin)}</loc><lastmod>${webPage.dateModified}</lastmod>${imageEntries}</url></urlset>\n`);
await writeFile(path.join(dist, "business.json"), JSON.stringify(schema, null, 2) + "\n");
const markdown = [
  `# ${business.name}`, "", `> ${business.description}`, "", "## Contact and location", "",
  `- Website: ${origin}`, `- Telephone: ${business.telephone}`, "- WhatsApp: https://wa.me/919762306303",
  `- Address: ${business.address.streetAddress}, ${business.address.addressLocality}, ${business.address.addressRegion} ${business.address.postalCode}, India.`,
  `- Google Maps: ${map}`, "- Opening hours: open 24 hours, Monday to Sunday.",
  `- Payments: ${business.paymentAccepted}.`, `- Shop opened: ${business.foundingDate}.`, "",
  "## Services", "", ...services.flatMap(service => [`### ${service.name}`, "", service.description, ""]),
  "## On-site coverage", "", areas.join(", ") + ".", "", "Call-outs are available 10 km or more from the shop. Call with the exact location to confirm availability, arrival time and applicable travel charges.", "",
  "## Frequently asked questions", "", ...faqs.flatMap(faq => [`### ${faq.question}`, "", faq.answer, ""]),
  "## Quotes and compatibility", "", "Contact the shop before ordering or travelling for a specific key, vehicle model or part. Prices depend on the key or lock, parts, programming, installation and travel. Vehicle and lock compatibility must be checked. No blanket arrival time is guaranteed.", "",
  `Business information reviewed: ${webPage.dateModified}.`, ""
].join("\n");
await writeFile(path.join(dist, "business.md"), markdown);
await writeFile(path.join(dist, "llms.txt"), [
  `# ${business.name}`, "", `> ${business.description}`, "", "## Business summary", "",
  `- Shop: ${business.address.streetAddress}, Bengaluru, Karnataka 560100, India.`,
  `- Phone: ${business.telephone}. Open 24 hours every day.`, "- Shop visits and on-site service. Confirm compatibility, arrival time and charges directly.", "",
  "## Main sources", "", `[Website](${origin}): Services, location, hours, photographs, contact details and FAQs.`,
  `[Business details](${origin}business.md): Plain-text business facts and service information.`,
  `[Structured business data](${origin}business.json): JSON-LD matching the visible website.`,
  `[Google Maps](${map}): Shop directions and Google Business Profile.`, "", "## Discovery", "",
  `[Sitemap](${origin}sitemap.xml)`, `[Crawler preferences](${origin}robots.txt)`, "", `Information reviewed: ${webPage.dateModified}.`, ""
].join("\n"));
console.log("Static website built. Canonical origin: " + origin);
