import { copyFile, mkdir, readFile, writeFile, readdir } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";

const root = path.dirname(fileURLToPath(import.meta.url));
const dist = path.join(root, "dist");
const args = process.argv.slice(2);
let requestedOrigin;
for (let i = 0; i < args.length; i++) {
  if (args[i] === "--origin") requestedOrigin = args[++i];
  else if (args[i].startsWith("--origin=")) requestedOrigin = args[i].slice(9);
  else throw new Error(`Unknown build argument: ${args[i]}. Use --origin https://your-final-domain/ when changing the production URL.`);
  if (!requestedOrigin) throw new Error("The --origin option requires an HTTPS website origin.");
}

function normalizeOrigin(value) {
  const url = new URL(value);
  if (url.protocol !== "https:" || url.username || url.password || url.pathname !== "/" || url.search || url.hash) {
    throw new Error("Production origin must be an HTTPS origin without a path, credentials, query or fragment.");
  }
  return url.origin + "/";
}

const sourceHtml = await readFile(path.join(root, "index.html"), "utf8");
const canonicalTag = sourceHtml.match(/<link\b[^>]*\brel=["']canonical["'][^>]*>/i)?.[0];
const canonicalHref = canonicalTag?.match(/\bhref=["']([^"']+)["']/i)?.[1];
if (!canonicalHref) throw new Error("The source homepage must declare its canonical website URL.");
const sourceOrigin = normalizeOrigin(canonicalHref);
const origin = requestedOrigin ? normalizeOrigin(requestedOrigin) : sourceOrigin;
// Only generated output changes when a new production origin is supplied.
const html = origin === sourceOrigin ? sourceHtml : sourceHtml.replaceAll(sourceOrigin.slice(0, -1), origin.slice(0, -1));
const schemaText = html.match(/<script\b[^>]*\btype=["']application\/ld\+json["'][^>]*>\s*([\s\S]*?)\s*<\/script>/i)?.[1];
if (!schemaText) throw new Error("The source homepage must contain business JSON-LD.");
const schema = JSON.parse(schemaText);
const graph = schema["@graph"];
if (!Array.isArray(graph)) throw new Error("Expected a linked business graph in the homepage JSON-LD.");
const hasType = (item, type) => [item["@type"]].flat().includes(type);
const business = graph.find(item => hasType(item, "Locksmith"));
const webPage = graph.find(item => hasType(item, "WebPage"));
if (!business || !webPage?.dateModified) throw new Error("Locksmith and dated WebPage entities are required.");
const areas = (business.areaServed ?? []).map(area => typeof area === "string" ? area : area.name).filter(Boolean);
const services = (business.hasOfferCatalog?.itemListElement ?? []).map(item => item.itemOffered).filter(Boolean);
if (!services.length || !areas.length) throw new Error("The business graph must include services and service areas.");
const map = business.hasMap;

await mkdir(dist, { recursive: true });
await writeFile(path.join(dist, "index.html"), html);
await copyFile(path.join(root, "privacy.html"), path.join(dist, "privacy.html"));
for (const filename of ["styles.css", "script.js", "_headers"]) {
  await copyFile(path.join(root, filename), path.join(dist, filename));
}

// Keep source art and provenance locally; upload only finished website assets.
let assetCount = 0;
async function copyAssets(sourceDirectory, outputDirectory) {
  await mkdir(outputDirectory, { recursive: true });
  for (const entry of await readdir(sourceDirectory, { withFileTypes: true })) {
    if (entry.name.startsWith(".") || /^thumbs\.db$/i.test(entry.name)) continue;
    if (/-original\.(png|jpe?g|webp|avif)$/i.test(entry.name) || /^image-manifest.*\.json$/i.test(entry.name)) continue;
    const source = path.join(sourceDirectory, entry.name);
    const target = path.join(outputDirectory, entry.name);
    if (entry.isSymbolicLink()) throw new Error(`Asset symlinks are not supported: ${entry.name}`);
    if (entry.isDirectory()) await copyAssets(source, target);
    else if (entry.isFile()) {
      await copyFile(source, target);
      assetCount++;
    }
  }
}
await copyAssets(path.join(root, "assets"), path.join(dist, "assets"));

// copyFile preserves the exact owner-supplied Search Console verification bytes.
const verificationDirectory = path.join(root, "verification");
await mkdir(verificationDirectory, { recursive: true });
for (const entry of await readdir(verificationDirectory, { withFileTypes: true })) {
  if (!entry.isFile() || !/^google[a-f0-9]+\.html$/.test(entry.name)) continue;
  const verificationFile = path.join(verificationDirectory, entry.name);
  const contents = await readFile(verificationFile, "utf8");
  if (contents.trim() !== `google-site-verification: ${entry.name}`) throw new Error(`Invalid Google verification file: ${entry.name}`);
  await copyFile(verificationFile, path.join(dist, entry.name));
}

const decodeText = text => text.replace(/<[^>]*>/g, " ")
  .replace(/&#x([a-f0-9]+);/gi, (_, code) => String.fromCodePoint(parseInt(code, 16)))
  .replace(/&#([0-9]+);/g, (_, code) => String.fromCodePoint(Number(code)))
  .replace(/&amp;/g, "&").replace(/&quot;/g, '"').replace(/&apos;/g, "'")
  .replace(/&nbsp;/g, " ").replace(/&lt;/g, "<").replace(/&gt;/g, ">")
  .replace(/\s+/g, " ").trim();
const faqs = [...html.matchAll(/<details\b[^>]*>\s*<summary\b[^>]*>([\s\S]*?)<\/summary>\s*<p\b[^>]*>([\s\S]*?)<\/p>\s*<\/details>/gi)]
  .map(match => ({ question: decodeText(match[1]), answer: decodeText(match[2]) }));
if (!faqs.length) throw new Error("No readable FAQ entries were found in the source HTML.");
const robots = ["# Public business information; search crawlers may access all published assets.", "User-agent: *", "Allow: /", "", ...["Googlebot", "bingbot", "OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "Perplexity-User"].flatMap(agent => [`User-agent: ${agent}`, "Allow: /", ""]), `Sitemap: ${origin}sitemap.xml`, ""].join("\n");
await writeFile(path.join(dist, "robots.txt"), robots);
const escapeXml = text => String(text).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll('"', "&quot;");
const businessImages = [business.image ?? []].flat().map(image => typeof image === "string" ? image : image.url ?? image.contentUrl).filter(Boolean);
const imageEntries = businessImages.map(image => `<image:image><image:loc>${escapeXml(image)}</image:loc></image:image>`).join("");
await writeFile(path.join(dist, "sitemap.xml"), `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"><url><loc>${escapeXml(origin)}</loc><lastmod>${escapeXml(webPage.dateModified)}</lastmod>${imageEntries}</url><url><loc>${escapeXml(origin)}privacy.html</loc><lastmod>${escapeXml(webPage.dateModified)}</lastmod></url></urlset>\n`);
await writeFile(path.join(dist, "business.json"), JSON.stringify(schema, null, 2) + "\n");
const markdown = [
  `# ${business.name}`, "", `> ${business.description}`, "", "## Contact and location", "",
  `- Website: ${origin}`, `- Telephone: ${business.telephone}`, "- WhatsApp: https://wa.me/919762306303",
  `- Address: ${business.address.streetAddress}, ${business.address.addressLocality}, ${business.address.addressRegion} ${business.address.postalCode}, India.`,
  `- Google Maps: ${map}`, "- Opening hours: open 24 hours, Monday to Sunday.",
  `- Payments: ${business.paymentAccepted}.`, `- Shop opened: ${business.foundingDate}.`, "",
  "## Services", "", ...services.flatMap(service => [`### ${service.name}`, "", service.description, ""]),
  "## On-site coverage", "", areas.join(", ") + ".", "", "Call with the exact location to confirm availability, arrival time and applicable travel charges.", "",
  "## Frequently asked questions", "", ...faqs.flatMap(faq => [`### ${faq.question}`, "", faq.answer, ""]),
  "## Quotes and compatibility", "", "Contact the shop before ordering or travelling for a specific key, vehicle model or part. Prices depend on the key or lock, parts, programming, installation and travel. Vehicle and lock compatibility must be checked. Confirm arrival time by phone for your location.", "",
  `Business information reviewed: ${webPage.dateModified}.`, ""
].join("\n");
await writeFile(path.join(dist, "business.md"), markdown);
await writeFile(path.join(dist, "llms.txt"), [
  `# ${business.name}`, "", `> ${business.description}`, "", "## Business summary", "",
  `- Shop: ${business.address.streetAddress}, Bengaluru, Karnataka 560100, India.`,
  `- Phone: ${business.telephone}. Open 24 hours every day.`, "- Shop visits and on-site service. Confirm compatibility, arrival time and charges directly.", "",
  "## Main sources", "", `[Website](${origin}): Services, products, location, hours, photographs, contact details and FAQs.`,
  `[Business details](${origin}business.md): Plain-text business facts and service information.`,
  `[Structured business data](${origin}business.json): JSON-LD matching the visible website.`,
  `[Privacy and cookies](${origin}privacy.html): Analytics consent and data choices.`,
  `[Google Maps](${map}): Shop directions and Google Business Profile.`, "", "## Discovery", "",
  `[Sitemap](${origin}sitemap.xml)`, `[Crawler preferences](${origin}robots.txt)`, "", `Information reviewed: ${webPage.dateModified}.`, ""
].join("\n"));
console.log(`Static website built: ${assetCount} assets, ${services.length} service groups, ${faqs.length} FAQs.`);
console.log("Canonical origin: " + origin);
