import { cp, mkdir, readFile, rm, writeFile } from "node:fs/promises";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import path from "node:path";

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const targets = new Set(["cloudflare-pages", "cloudflare-workers"]);

export async function buildTarget(target) {
  if (!targets.has(target)) throw new Error("Unknown Cloudflare deployment target");
  const targetRoot = path.join(repo, target);
  const output = path.resolve(targetRoot, "dist");
  // Only remove this deployment target's generated output, never the source.
  if (path.dirname(output) !== targetRoot || path.basename(output) !== "dist") {
    throw new Error("Generated output must stay inside its deployment folder");
  }
  for (const script of ["build.mjs", "verify-build.mjs"]) {
    const result = spawnSync(process.execPath, [path.join(repo, "website-openai", script)], { stdio: "inherit" });
    if (result.status !== 0) throw new Error(`${script} failed`);
  }
  await rm(output, { recursive: true, force: true });
  await mkdir(output, { recursive: true });
  await cp(path.join(repo, "website-openai", "dist"), output, { recursive: true });
  if (target === "cloudflare-workers") {
    // The backup serves the complete site while the Pages origin stays canonical.
    const headersPath = path.join(output, "_headers");
    const headers = await readFile(headersPath, "utf8");
    if (!headers.includes("X-Robots-Tag: index, follow, max-image-preview:large, max-snippet:-1")) {
      throw new Error("Expected primary indexing header is missing");
    }
    await writeFile(headersPath, headers.replace(
      "X-Robots-Tag: index, follow, max-image-preview:large, max-snippet:-1",
      "X-Robots-Tag: noindex, follow"
    ));
  }
  const { verifyTarget } = await import("./verify-cloudflare-target.mjs");
  await verifyTarget(target);
  console.log(`Ready to deploy: ${target}/dist/`);
}
