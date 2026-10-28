import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";

// Publish real information and an agent-readable workflow. This static shop
// website does not advertise a fictitious MCP server or an automated booking API.
export async function writeDiscovery({ dist, origin, business, services, faqs, modified }) {
  const skillPath = "agent-skills/locksmith-enquiry/SKILL.md";
  const catalog = {
    specVersion: "1.0",
    host: {
      displayName: business.name,
      identifier: origin,
      documentationUrl: `${origin}business.md`,
      logoUrl: business.logo
    },
    entries: [{
      identifier: `urn:air:${new URL(origin).hostname}:skills:locksmith-enquiry`,
      displayName: "Keymaker Ecity service enquiry",
      type: 'text/markdown; profile="urn:air:agent-skills"',
      url: `${origin}${skillPath}`,
      description: "Read the shop's services, location and hours, then help a customer prepare an enquiry by phone or WhatsApp. Availability, compatibility and quotes require confirmation from the shop.",
      tags: ["locksmith", "key duplication", "Electronic City", "Bengaluru"],
      representativeQueries: [
        "Where can I get a spare house key in Electronic City Phase 1?",
        "How do I contact Key Maker & Locksmith for a lock repair quote?",
        "Does Keymaker Ecity provide 24-hour locksmith assistance?"
      ],
      version: "1.0.0",
      updatedAt: `${modified.slice(0, 10)}T00:00:00+05:30`
    }]
  };
  await mkdir(path.join(dist, ".well-known"), { recursive: true });
  for (const filename of [".well-known/ai-catalog.json", ".well-known/ard.json", "ai-catalog.json"]) {
    await writeFile(path.join(dist, filename), JSON.stringify(catalog, null, 2) + "\n");
  }
  const skill = [
    "---", "name: locksmith-enquiry",
    "description: Find Keymaker Ecity shop information and help a customer prepare a locksmith or key duplication enquiry in Electronic City, Bengaluru.",
    "---", "", "# Keymaker Ecity service enquiry", "",
    "Use this reference when a customer asks about this shop or its services. Follow the customer's instructions and obtain their approval before contacting the business or sharing their details.", "",
    `Source website: ${origin}`, `Business details: ${origin}business.md`,
    `Structured facts: ${origin}business.json`, `Last reviewed: ${modified.slice(0, 10)}.`, "",
    "## Shop", "", `${business.name}.`,
    `${business.address.streetAddress}, ${business.address.addressLocality}, ${business.address.addressRegion} ${business.address.postalCode}, India.`,
    `Telephone: ${business.telephone}. WhatsApp: https://wa.me/919762306303.`,
    "Open 24 hours every day. Shop visits and on-site service are available. Call the shop to confirm the current availability, arrival time, compatibility, price and any travel charges.", "",
    "## Services", "", ...services.map(service => `- [${service.name}](${service.url}): ${service.description}`), "",
    "## Prepare an enquiry", "",
    "1. Identify the requested service and whether the customer plans a shop visit or needs on-site assistance.",
    "2. For duplicate keys, ask whether an original is available. For vehicle keys, ask for the vehicle make, model and year. For lock repair, ask for the lock type and problem. Share photos only if the customer chooses to do so.",
    "3. For an on-site enquiry, use the area the customer chooses to share. Do not request identity documents, security codes, precise location or payment details in this website workflow.",
    "4. Offer the phone link or a WhatsApp draft. The user sends the message or authorises contact. Opening a link does not book a visit.",
    "5. Let the shop confirm parts, service support, arrival time and quote. Do not claim that a job is booked, guarantee a ten-minute arrival, or invent prices, stock levels or discounts.", "",
    "Lockout and safe-opening work is for authorised owners or occupants. Ownership checks are handled directly by the shop. This document does not provide lock bypass instructions.", "",
    "## Customer questions", "", ...faqs.flatMap(faq => [`### ${faq.question}`, "", faq.answer, ""])
  ].join("\n");
  await mkdir(path.join(dist, path.dirname(skillPath)), { recursive: true });
  await writeFile(path.join(dist, skillPath), skill);
}
