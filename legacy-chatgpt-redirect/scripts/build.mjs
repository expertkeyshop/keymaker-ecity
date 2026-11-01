import { mkdir, readFile, rm, copyFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("../", import.meta.url));
const dist = resolve(root, "dist");
if (dist !== resolve(root, "./dist") || !dist.startsWith(resolve(root) + "/") && !dist.startsWith(resolve(root) + "\\")) {
  throw new Error("Refusing to remove a directory outside this Site's dist");
}
const manifest = JSON.parse(await readFile(resolve(root, ".openai/hosting.json"), "utf8"));
if (manifest.project_id !== "appgprj_6ad8d539e2a88191ad3d4657fd33d7d3" || manifest.static) {
  throw new Error("Preserve the selected Site identity and Worker deployment configuration");
}
await rm(dist, { recursive: true, force: true });
await mkdir(resolve(dist, "server"), { recursive: true });
await mkdir(resolve(dist, ".openai"), { recursive: true });
await copyFile(resolve(root, "worker/index.js"), resolve(dist, "server/index.js"));
await copyFile(resolve(root, ".openai/hosting.json"), resolve(dist, ".openai/hosting.json"));
console.log("Built the legacy Site's permanent redirect Worker");
