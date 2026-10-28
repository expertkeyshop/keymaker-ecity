import assert from "node:assert/strict";
import { readFile, readdir } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
export async function verifyTarget(target) {
  assert(["cloudflare-pages", "cloudflare-workers"].includes(target));
  const directory = path.join(repo, target, "dist");
  const forbidden = new Set([".git", ".openai", "node_modules", ".env", "wrangler.jsonc", "package.json"]);
  const files = [];
  async function walk(dir, prefix = "") {
    for (const entry of await readdir(dir, { withFileTypes: true })) {
      assert(!forbidden.has(entry.name), `Private/build-only file in public output: ${entry.name}`);
      assert(!entry.isSymbolicLink(), "Public output must not contain symlinks");
      const relative = path.posix.join(prefix, entry.name);
      if (entry.isDirectory()) await walk(path.join(dir, entry.name), relative);
      else files.push(relative);
    }
  }
  await walk(directory);
  for (const file of files) {
    if (file === "_headers" && target === "cloudflare-workers") continue;
    assert.deepEqual(await readFile(path.join(directory, file)), await readFile(path.join(repo, "website-openai", "dist", file)), `Outdated target file: ${file}`);
  }
  const read = file => readFile(path.join(directory, file), "utf8");
  assert((await read("index.html")).includes('rel="canonical" href="https://keymaker-ecity.pages.dev/"'));
  const headers = await read("_headers");
  assert(headers.includes(target === "cloudflare-pages" ? "X-Robots-Tag: index, follow" : "X-Robots-Tag: noindex, follow"));
  assert(headers.split(/\r?\n/).every(line => line.length <= 2000), "Cloudflare header line exceeds 2000 characters");
  assert(!headers.includes("__SCRIPT_HASH__") && !headers.includes("__STYLE_HASHES__"));
  assert.equal(JSON.parse(await read(".well-known/ai-catalog.json")).specVersion, "1.0");
  assert((await read("404.html")).includes('content="noindex, follow"'));
  assert((await read("googlea8f5575206e3c038.html")).trim() === "google-site-verification: googlea8f5575206e3c038.html");
  console.log(`PASS: ${target}: ${files.length} public files, current build, canonical URL, indexing, headers, discovery and verification.`);
}
