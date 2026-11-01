import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const source = await readFile(new URL("../dist/server/index.js", import.meta.url), "utf8");
const { default: worker } = await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);
const cases = [
  ["/", "/"],
  ["/index.html?utm_source=sulekha", "/?utm_source=sulekha"],
  ["/privacy.html", "/privacy.html"],
  ["/robots.txt", "/robots.txt"],
  ["/sitemap.xml", "/sitemap.xml"],
  ["//example.com/other?next=https://example.com", "//example.com/other?next=https://example.com"],
  ["/missing-page", "/missing-page"],
];
for (const [path, expected] of cases) {
  const response = worker.fetch(new Request("https://keymaker-ecity.alishanaver72.chatgpt.site" + path));
  assert.equal(response.status, 301);
  assert.equal(response.headers.get("Location"), "https://keymaker-ecity.pages.dev" + expected);
  assert.equal(new URL(response.headers.get("Location")).origin, "https://keymaker-ecity.pages.dev");
  assert.equal(await response.text(), "");
}
assert.equal(worker.fetch(new Request("https://keymaker-ecity.alishanaver72.chatgpt.site/", {method:"HEAD"})).status, 301);
console.log("8 redirect checks passed: permanent status, fixed destination, paths and query preservation");
