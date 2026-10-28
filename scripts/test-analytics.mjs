import assert from "node:assert/strict";
import vm from "node:vm";
import { readFile } from "node:fs/promises";
const source = await readFile(new URL("../website-openai/analytics.js",import.meta.url),"utf8");
function setup(host="keymaker-ecity.pages.dev",query="") {
  const scripts = [], deleted = [];
  const window = {location:{hostname:host,href:`https://${host}/${query}`,search:query}};
  const document = {referrer:"https://www.google.com/search?q=customer@example.com",querySelector:selector=>({content:selector.includes("ga-measurement")?"G-Q2CM2F0JB8":"GTM-PKCWS4Z8"}),createElement:()=>({}),head:{appendChild:script=>scripts.push(script)}};
  Object.defineProperty(document,"cookie",{get:()=>"_ga=123; _ga_Q2CM2F0JB8=456; essential=kept",set:value=>deleted.push(value)});
  vm.runInNewContext(source,{window,document,URL,URLSearchParams,Date,Set,Object});
  return {window,analytics:window.keymakerAnalytics,scripts,deleted};
}
const page = setup("keymaker-ecity.pages.dev","?utm_source=google&utm_medium=organic&utm_campaign=gbp&email=customer@example.com&phone=919999999999");
assert.equal(page.scripts.length,0,"No tag before consent");
assert.equal(page.analytics.track("click_call"),false);
page.analytics.setConsent("denied");
assert.equal(page.scripts.length,0,"No tag after decline");
page.analytics.setConsent("granted");
assert.equal(page.scripts.length,1);
assert.equal(page.scripts[0].src,"https://www.googletagmanager.com/gtm.js?id=GTM-PKCWS4Z8");
page.analytics.setConsent("granted");
assert.equal(page.scripts.length,1,"Never insert duplicate containers");
assert.equal(page.window.dataLayer.filter(e=>e.event==="km_analytics_ready").length,1,"One page initialization only");
assert(page.analytics.track("click_whatsapp",{section:"service",item_name:"Car key",contact_method:"whatsapp",customer_phone:"9999999999",url:"https://wa.me/private"}));
const action = page.window.dataLayer.at(-1);
assert.equal(action.contact_method,"whatsapp");
assert(!JSON.stringify(action).includes("customer@"));
assert(!JSON.stringify(action).includes("999999"));
assert(!JSON.stringify(action).includes("wa.me"));
assert.equal(action.page_referrer,"https://www.google.com/");
assert.equal(action.page_location,"https://keymaker-ecity.pages.dev/?utm_source=google&utm_medium=organic&utm_campaign=gbp");
assert.equal(page.analytics.track("purchase"),false,"Do not invent transaction tracking");
page.analytics.setConsent("denied");
assert(page.window["ga-disable-G-Q2CM2F0JB8"]);
assert.equal(page.analytics.track("click_call"),false,"No events after withdrawal");
assert(page.deleted.some(value=>value.startsWith("_ga=")));
assert(page.deleted.every(value=>!value.startsWith("essential=")));
page.analytics.setConsent("granted");
assert.equal(page.scripts.length,1,"Regrant uses existing container");
assert.equal(page.window.dataLayer.filter(e=>e.event==="km_analytics_ready").length,1);
for (const host of ["localhost","127.0.0.1","keymaker.electronicity.workers.dev","preview.keymaker-ecity.pages.dev"]) {
  const excluded=setup(host); excluded.analytics.setConsent("granted");
  assert.equal(excluded.scripts.length,0,`Do not measure ${host}`);
  assert.equal(excluded.analytics.track("click_call"),false);
}
const debug=setup("keymaker-ecity.pages.dev","?km_debug=1"); debug.analytics.setConsent("granted");
assert.equal(debug.window.dataLayer.at(-1).debug_mode,true);
assert.equal(debug.window.dataLayer.at(-1).traffic_type,"developer");
console.log("PASS: consent before load, decline, withdrawal/cookie cleanup, regrant, no duplicates, primary-host gate, safe URLs/parameters and developer mode.");
const container = JSON.parse(await readFile(new URL("../analytics/gtm-container-ready.json", import.meta.url), "utf8")).containerVersion;
const variables = new Set([...container.variable, ...container.builtInVariable].map(variable => variable.name));
for (const match of JSON.stringify(container).matchAll(/\{\{([^}]+)\}\}/g)) {
  assert(match[1] === "_event" || variables.has(match[1]), `Unknown GTM variable: ${match[1]}`);
}
assert.equal(container.tag.length, 4);
assert.equal(container.trigger.length, 3);
for (const trigger of container.trigger) {
  assert(trigger.filter.some(filter => filter.parameter.some(value => value.value === "{{Page Hostname}}")), `Missing primary-host gate: ${trigger.name}`);
}
const template = await readFile(new URL("../analytics/keymaker-consent.tpl", import.meta.url), "utf8");
const consentSource = template.split("___SANDBOXED_JS_FOR_WEB_TEMPLATE___")[1].split("___WEB_PERMISSIONS___")[0];
for (const command of ["default", "update"]) {
  for (const analyticsConsent of ["granted", "denied"]) {
    const calls = [];
    vm.runInNewContext(consentSource, {
      data: { command, analyticsConsent, gtmOnSuccess: () => calls.push("success") },
      require: name => state => calls.push({ name, state })
    });
    assert.equal(calls.at(-1), "success");
    const updates = calls.filter(call => call.name === "updateConsentState");
    assert.equal(updates.length, 1);
    assert.equal(updates[0].state.analytics_storage, analyticsConsent);
    for (const key of ["ad_storage", "ad_user_data", "ad_personalization"]) assert.equal(updates[0].state[key], "denied");
    assert.equal(calls.some(call => call.name === "setDefaultConsentState"), command === "default");
  }
}
console.log("PASS: GTM variable references, primary-host gates and sandboxed consent state transitions.");
