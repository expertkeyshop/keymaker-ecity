import http from "node:http";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { gzipSync } from "node:zlib";
const root = path.join(path.dirname(fileURLToPath(import.meta.url)), "dist");
const types = { ".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".webp": "image/webp", ".avif": "image/avif", ".png": "image/png", ".xml": "application/xml; charset=utf-8", ".txt": "text/plain; charset=utf-8", ".md": "text/markdown; charset=utf-8", ".json": "application/json; charset=utf-8" };
async function pageHeaders(pathname) {
  const headers = {};
  let matches = false;
  for (const line of (await readFile(path.join(root, "_headers"), "utf8")).split(/\r?\n/)) {
    if (!line.trim() || line.startsWith("#")) continue;
    if (!/^\s/.test(line)) matches = line === "/*" || line === pathname;
    else if (matches) {
      const colon = line.indexOf(":");
      if (colon > 0) headers[line.slice(0, colon).trim()] = line.slice(colon + 1).trim();
    }
  }
  return headers;
}
const server = http.createServer(async (req, res) => {
  try {
    const pathname = decodeURIComponent(new URL(req.url, "http://127.0.0.1").pathname);
    const requested = pathname === "/" ? "/index.html" : pathname === "/privacy" ? "/privacy.html" : pathname;
    const filename = path.resolve(root, "." + requested);
    if (!filename.startsWith(root + path.sep)) { res.writeHead(403); res.end("Forbidden"); return; }
    let body = await readFile(filename);
    const headers = { "Content-Type": types[path.extname(filename)] || "application/octet-stream", "Cache-Control": "no-store", ...await pageHeaders(pathname) };
    if (/gzip/.test(req.headers["accept-encoding"] || "") && /text|json|xml/.test(headers["Content-Type"])) {
      body = gzipSync(body);
      headers["Content-Encoding"] = "gzip";
      headers.Vary = "Accept-Encoding";
    }
    res.writeHead(200, headers);
    res.end(body);
  } catch { res.writeHead(404, { "Content-Type": "text/html; charset=utf-8", ...await pageHeaders("/404.html") }); res.end(await readFile(path.join(root, "404.html"))); }
});
const port = Number(process.argv[2] || 8126);
server.listen(port, "127.0.0.1", () => console.log(`Local: http://127.0.0.1:${port}/`));
for (const signal of ["SIGINT", "SIGTERM"]) process.on(signal, () => server.close(() => process.exit(0)));
