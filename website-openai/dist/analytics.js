"use strict";
(() => {
  if (window.keymakerAnalytics) return;
  const measurementId = document.querySelector('meta[name="ga-measurement-id"]')?.content || "";
  const containerId = document.querySelector('meta[name="gtm-container-id"]')?.content || "";
  const productionHost = "keymaker-ecity.pages.dev";
  const enabledHost = window.location.hostname === productionHost;
  const validIds = /^G-[A-Z0-9]+$/.test(measurementId) && /^GTM-[A-Z0-9]+$/.test(containerId);
  const disableKey = `ga-disable-${measurementId}`;
  const debug = new URLSearchParams(window.location.search).get("km_debug") === "1";
  const eventNames = new Set(["click_call", "click_whatsapp", "click_directions", "click_review", "faq_open", "view_section"]);
  let granted = false;
  let adsGranted = false;
  let loaded = false;
  let pageSent = false;
  window[disableKey] = true;
  window.dataLayer = window.dataLayer || [];

  const safeLocation = () => {
    const url = new URL(window.location.href);
    const safe = new URL(url.origin + url.pathname);
    for (const name of ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"]) {
      const value = url.searchParams.get(name) || "";
      if (/^[a-zA-Z][a-zA-Z0-9_.-]{0,79}$/.test(value) && !/\d{7,}/.test(value)) safe.searchParams.set(name, value);
    }
    // Click identifiers are optional advertising measurement data, not campaign
    // labels. Include them only after the visitor explicitly chooses measurement.
    if (adsGranted) {
      for (const name of ["gclid", "gbraid", "wbraid"]) {
        const value = url.searchParams.get(name) || "";
        if (/^[a-zA-Z0-9_-]{10,512}$/.test(value)) safe.searchParams.set(name, value);
      }
    }
    return safe.href;
  };
  const safeReferrer = () => {
    try { return document.referrer ? new URL(document.referrer).origin + "/" : ""; }
    catch (_) { return ""; }
  };
  const context = () => ({
    page_location: safeLocation(), page_referrer: safeReferrer(),
    site_environment: "production", debug_mode: debug,
    traffic_type: debug ? "developer" : "external"
  });
  const clearCookies = (adsOnly = false) => {
    const host = window.location.hostname;
    const domains = ["", host, `.${host}`];
    document.cookie.split(";").forEach(part => {
      const name = part.split("=")[0].trim();
      if (!/^_(ga|gid|gat|gcl)(_|$)/.test(name)) return;
      if (adsOnly && !/^_gcl(_|$)/.test(name)) return;
      domains.forEach(domain => {
        document.cookie = `${name}=; Max-Age=0; path=/; SameSite=Lax${domain ? `; domain=${domain}` : ""}`;
      });
    });
  };
  const setConsent = choice => {
    // "granted" is the existing analytics-only choice; never upgrade old consent.
    granted = enabledHost && validIds && (choice === "granted" || choice === "measurement");
    adsGranted = granted && choice === "measurement";
    window[disableKey] = !granted;
    if (!granted) clearCookies();
    else if (!adsGranted) clearCookies(true);
    if (!enabledHost || !validIds) return;
    // No Google resources load until consent. The sandboxed GTM consent tag
    // processes this state with Google's consent APIs before measurement tags.
    const consent = {
      analytics_consent: granted ? "granted" : "denied",
      ads_measurement_consent: adsGranted ? "granted" : "denied"
    };
    window.dataLayer.push({ event: "km_consent_update", ...consent, ...context() });
    if (!granted) return;
    if (!loaded) {
      loaded = true;
      window.dataLayer.push({ "gtm.start": Date.now(), event: "gtm.js" });
      const script = document.createElement("script");
      script.async = true;
      script.src = `https://www.googletagmanager.com/gtm.js?id=${encodeURIComponent(containerId)}`;
      document.head.appendChild(script);
    }
    if (!pageSent) {
      pageSent = true;
      window.dataLayer.push({ event: "km_analytics_ready", ...consent, ...context() });
    }
  };
  const track = (name, input = {}) => {
    if (!granted || !eventNames.has(name)) return false;
    const parameters = { ...context(), analytics_consent: "granted" };
    for (const key of ["section", "contact_method", "question_id"]) {
      if (/^[a-z][a-z0-9_-]{0,39}$/.test(input[key] || "")) parameters[key] = input[key];
    }
    // item_name is authored catalogue metadata; never take it from customer input.
    if (typeof input.item_name === "string") parameters.item_name = input.item_name.replace(/[\u0000-\u001f\u007f]/g, "").trim().slice(0, 80);
    window.dataLayer.push({ event: name, section: "", item_name: "", contact_method: "", question_id: "", ...parameters });
    return true;
  };
  window.keymakerAnalytics = Object.freeze({ setConsent, track, isEnabled: () => granted });
})();
