import assert from "node:assert/strict";
import vm from "node:vm";
import { readFile } from "node:fs/promises";
const source = await readFile(new URL("../website-openai/analytics.js",import.meta.url),"utf8");
function setup(host="keymaker-ecity.pages.dev",query="") {
  const scripts = [], deleted = [];
  const window = {location:{hostname:host,href:`https://${host}/${query}`,search:query}};
  const document = {referrer:"https://www.google.com/search?q=customer@example.com",querySelector:selector=>({content:selector.includes("ga-measurement")?"G-Q2CM2F0JB8":"GTM-PKCWS4Z8"}),createElement:()=>({}),head:{appendChild:script=>scripts.push(script)}};
  Object.defineProperty(document,"cookie",{get:()=>"_ga=123; _ga_Q2CM2F0JB8=456; _gcl_au=abc; essential=kept",set:value=>deleted.push(value)});
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
const clickId = "TestClickId_abcdefghij-0123456789";
const ads=setup("keymaker-ecity.pages.dev",`?gclid=${clickId}&gbraid=${clickId}&wbraid=${clickId}&email=private@example.com&text=private`);
ads.analytics.setConsent("granted");
assert.equal(ads.window.dataLayer.at(-1).ads_measurement_consent,"denied","Legacy acceptance is analytics only");
assert(!ads.window.dataLayer.at(-1).page_location.includes("gclid"));
ads.analytics.setConsent("measurement");
assert.equal(ads.scripts.length,1);
assert.equal(ads.window.dataLayer.at(-1).ads_measurement_consent,"granted");
assert.equal(ads.window.dataLayer.at(-1).analytics_consent,"granted");
assert(ads.analytics.track("click_call",{contact_method:"phone"}));
const adsUrl = new URL(ads.window.dataLayer.at(-1).page_location);
for(const key of ["gclid","gbraid","wbraid"]) assert.equal(adsUrl.searchParams.get(key),clickId);
assert(!adsUrl.searchParams.has("email"));
assert(!adsUrl.searchParams.has("text"));
ads.deleted.length=0;
ads.analytics.setConsent("granted");
assert.equal(ads.window.dataLayer.at(-1).ads_measurement_consent,"denied");
assert.equal(ads.window.dataLayer.at(-1).page_location,"https://keymaker-ecity.pages.dev/");
assert(ads.deleted.some(value=>value.startsWith("_gcl_au=")),"Delete ad cookies on measurement withdrawal");
assert(!ads.deleted.some(value=>value.startsWith("_ga=")),"Keep analytics cookies if analytics remains accepted");
ads.analytics.setConsent("denied");
assert(!ads.analytics.track("click_call"));
assert(ads.deleted.some(value=>value.startsWith("_ga=")));
const malformed=setup("keymaker-ecity.pages.dev","?gclid=customer@example.com&wbraid=short&gbraid="+"x".repeat(513));
malformed.analytics.setConsent("measurement");
assert.equal(malformed.window.dataLayer.at(-1).page_location,"https://keymaker-ecity.pages.dev/");
for(const choice of [undefined,"invalid",{analytics:"granted"}]) {
  const invalid=setup(); invalid.analytics.setConsent(choice);
  assert.equal(invalid.scripts.length,0,"Unknown choices fail closed");
}
console.log("PASS: consent before load, legacy analytics only, explicit ad opt-in, ad-only/full withdrawal, primary-host gate, click-ID validation/redaction and developer mode.");
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
   for (const adsMeasurementConsent of ["granted", "denied", undefined]) {
    const calls = [];
    vm.runInNewContext(consentSource, {
      data: { command, analyticsConsent, adsMeasurementConsent, gtmOnSuccess: () => calls.push("success") },
      require: name => state => calls.push({ name, state })
    });
    assert.equal(calls.at(-1), "success");
    const updates = calls.filter(call => call.name === "updateConsentState");
    assert.equal(updates.length, 1);
    assert.equal(updates[0].state.analytics_storage, analyticsConsent);
    for (const key of ["ad_storage", "ad_user_data"]) assert.equal(updates[0].state[key], analyticsConsent === "granted" && adsMeasurementConsent === "granted" ? "granted" : "denied");
    assert.equal(updates[0].state.ad_personalization,"denied");
    assert.equal(calls.some(call => call.name === "setDefaultConsentState"), command === "default");
    if(command==="default") for(const value of Object.values(calls[0].state)) assert.equal(value,"denied","Defaults precede user updates");
   }
  }
}
assert.equal(container.customTemplate.find(template=>template.name==="Keymaker consent bridge").templateData.trimEnd(),template.trimEnd());
const adsVariable=container.variable.find(variable=>variable.name==="DLV - Ads measurement consent");
assert(adsVariable.parameter.some(parameter=>parameter.key==="name" && parameter.value==="ads_measurement_consent"));
for(const tag of container.tag.filter(tag=>tag.name.startsWith("Consent -"))) {
  assert(tag.parameter.some(parameter=>parameter.key==="adsMeasurementConsent" && parameter.value==="{{DLV - Ads measurement consent}}"));
}
for(const file of ["index.html","privacy.html"]) {
  const html=await readFile(new URL(`../website-openai/${file}`,import.meta.url),"utf8");
  for(const choice of ["denied","granted","measurement"]) assert.equal((html.match(new RegExp(`data-consent="${choice}"`,"g"))||[]).length,1,`${file} exposes each visitor choice once`);
}
console.log("PASS: GTM variable references, primary-host gates, all consent combinations, template/export consistency and banner choices.");
