import assert from "node:assert/strict";
import { createHash } from "node:crypto";

const origin = new URL(process.argv[2] || "https://keymaker-ecity.pages.dev/");
assert.equal(origin.protocol, "https:");
assert.equal(origin.pathname, "/");
const backup = process.argv.includes("--backup");
const results = [];
const read = async (pathname, type) => {
  const response = await fetch(new URL(pathname, origin), { signal: AbortSignal.timeout(30000) });
  assert.equal(response.status, 200, `${pathname}: HTTP ${response.status}`);
  if (type) assert(response.headers.get("content-type")?.includes(type), `${pathname}: unexpected content type`);
  results.push({ path: pathname, status: response.status, type: response.headers.get("content-type") });
  return { response, body: await response.text() };
};

const { response, body: home } = await read("/", "text/html");
assert(home.includes('rel="canonical" href="https://keymaker-ecity.pages.dev/"'), "Primary canonical URL missing");
const robots = response.headers.get("x-robots-tag") || "";
assert(backup ? robots.includes("noindex") : robots.includes("index") && !robots.includes("noindex"), "Unexpected indexing header");
const policy = response.headers.get("content-security-policy") || "";
assert(policy.includes("'strict-dynamic'"), "Current CSP is not deployed");
const sha = value => "sha256-" + createHash("sha256").update(value).digest("base64");
const scriptTag = home.match(/<script\b[^>]*src="script\.js[^\"]*"[^>]*>/)?.[0];
assert(scriptTag, "Versioned application script missing");
const scriptSource = scriptTag.match(/src="([^"]+)"/)[1];
const expectedHash = scriptTag.match(/integrity="([^"]+)"/)[1];
assert.equal(sha((await read(scriptSource, "javascript")).body), expectedHash, "Live script integrity mismatch");
assert(policy.includes(expectedHash), "Live CSP script hash mismatch");
for (const style of home.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/g)) assert(policy.includes(sha(style[1])), "Live CSS hash mismatch");
for (const endpoint of ["/.well-known/ai-catalog.json", "/.well-known/ard.json", "/ai-catalog.json"]) {
  const catalog = JSON.parse((await read(endpoint, "application/ai-catalog+json")).body);
  assert.equal(catalog.specVersion, "1.0");
  assert(catalog.entries.every(entry => entry.url.startsWith("https://keymaker-ecity.pages.dev/")));
}
assert((await read("/agent-skills/locksmith-enquiry/SKILL.md", "text/markdown")).body.includes("name: locksmith-enquiry"));
assert((await read("/privacy", "text/html")).body.includes("https://keymaker-ecity.pages.dev/privacy"));
assert((await read("/robots.txt", "text/plain")).body.includes("https://keymaker-ecity.pages.dev/sitemap.xml"));
assert((await read("/llms.txt", "text/plain")).body.includes(".well-known/ai-catalog.json"));
assert((await read("/sitemap.xml", "application/xml")).body.includes("https://keymaker-ecity.pages.dev/privacy"));
assert((await read("/business.json", "application/ld+json")).body.includes("+919762306303"));
assert.equal((await read("/googlea8f5575206e3c038.html", "text/html")).body.trim(), "google-site-verification: googlea8f5575206e3c038.html");
const missing = await fetch(new URL("/missing-deployment-check.json", origin), { signal: AbortSignal.timeout(30000) });
assert.equal(missing.status, 404, "Missing JSON must not return the homepage");
console.log(JSON.stringify({ origin: origin.origin, role: backup ? "backup" : "primary", result: "PASS", checks: results, missingFileStatus: missing.status, robots }, null, 2));
