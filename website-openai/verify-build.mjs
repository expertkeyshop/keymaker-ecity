import assert from "node:assert/strict";
import { readFile, readdir } from "node:fs/promises";
import { createHash } from "node:crypto";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.dirname(fileURLToPath(import.meta.url));
const dist = path.join(root, "dist");
const read = name => readFile(path.join(dist, name), "utf8");
const html = await read("index.html");
const origin = html.match(/<link rel="canonical" href="([^"]+)"/)?.[1];
assert.equal(origin, "https://keymaker-ecity.pages.dev/", "Primary origin must be Pages");
const headers = await read("_headers");
assert(!headers.includes("__SCRIPT_HASH__") && !headers.includes("__STYLE_HASHES__"));
const sha = text => "sha256-" + createHash("sha256").update(text).digest("base64");
const scriptHash = sha(await read("script.js"));
assert(headers.includes(scriptHash));
const analyticsHash = sha(await read("analytics.js"));
assert(headers.includes(analyticsHash));
const catalog = JSON.parse(await read(".well-known/ai-catalog.json"));
assert.equal(catalog.specVersion, "1.0");
for (const alias of ["ai-catalog.json", ".well-known/ard.json"]) {
  assert.deepEqual(JSON.parse(await read(alias)), catalog);
}
for (const entry of catalog.entries) {
  assert(entry.url.startsWith(origin));
  assert((await read(new URL(entry.url).pathname.slice(1))).includes("name: locksmith-enquiry"));
}
assert((await read("404.html")).includes('content="noindex, follow"'));
assert((await read("privacy.html")).includes(`href="${origin}privacy"`));
assert((await read("sitemap.xml")).includes(`${origin}privacy</loc>`));
assert((await read("robots.txt")).includes(`Sitemap: ${origin}sitemap.xml`));
const verification = "googlea8f5575206e3c038.html";
assert.deepEqual(await readFile(path.join(dist, verification)), await readFile(path.join(root, "verification", verification)));
const graph = JSON.parse(await read("business.json"));
assert(graph["@graph"].some(item => item["@type"] === "Locksmith" && item.telephone === "+919762306303"));
const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map(match => match[1]);
assert.equal(new Set(ids).size, ids.length, "Duplicate homepage IDs");
for (const name of ["index.html", "privacy.html", "404.html"]) {
  const page = await read(name);
  assert(!page.includes("alishanaver72.workers.dev"), `${name}: stale backup origin`);
  assert(!page.includes('rel="stylesheet"'), `${name}: render-blocking stylesheet`);
  if (page.includes('src="script.js')) assert(page.includes(`integrity="${scriptHash}"`));
  if (name !== "404.html") {
    assert(page.includes(`integrity="${analyticsHash}"`), `${name}: analytics integrity missing`);
    assert(page.includes('name="gtm-container-id" content="GTM-PKCWS4Z8"'));
    assert(!page.includes("googletagmanager.com/ns.html"), "Unconditional iframe would bypass consent");
  }
  for (const match of page.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/g)) assert(headers.includes(sha(match[1])), `${name}: CSS hash mismatch`);
  for (const match of page.matchAll(/(?:src|href)="(assets\/[^"?#]+)[^\"]*"/g)) await readFile(path.join(dist, match[1]));
  for (const match of page.matchAll(/srcset="([^"]+)"/g)) {
    for (const candidate of match[1].split(",")) await readFile(path.join(dist, candidate.trim().split(/\s/)[0]));
  }
  for (const match of page.matchAll(/href="#([^"]+)"/g)) {
    assert(page.includes(`id="${match[1]}"`), `${name}: missing fragment ${match[1]}`);
  }
}
async function walk(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    assert(![".git", ".openai", "node_modules"].includes(entry.name), "Private files in public output");
    if (entry.isDirectory()) await walk(path.join(directory, entry.name));
  }
}
await walk(dist);
console.log("PASS: catalog aliases and skill, primary URLs, assets and anchors, CSP/SRI hashes, 404, sitemap and byte-exact Google verification.");
