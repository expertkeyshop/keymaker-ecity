"use strict";
(() => {
  if (window.__keymakerUI) return;
  window.__keymakerUI = true;

  const CONSENT_KEY = "km-analytics-consent";

  const readConsent = () => {
    try {
      return window.localStorage.getItem(CONSENT_KEY);
    } catch (_) {
      return null;
    }
  };
  const writeConsent = value => {
    try {
      window.localStorage.setItem(CONSENT_KEY, value);
    } catch (_) { /* Storage can be unavailable in private modes. */ }
  };

  const init = () => {
    const root = document.documentElement;
    const menuButton = document.querySelector(".menu-toggle");
    const navigation = document.querySelector("#main-nav");
    const desktop = window.matchMedia("(min-width: 801px)");
    const motion = window.matchMedia("(prefers-reduced-motion: reduce)");
    const onChange = (query, handler) => {
      if (query.addEventListener) query.addEventListener("change", handler);
      else if (query.addListener) query.addListener(handler);
    };

    const setMenu = open => {
      if (!menuButton || !navigation) return;
      open = Boolean(open && !desktop.matches);
      menuButton.setAttribute("aria-expanded", String(open));
      const label = menuButton.querySelector(".visually-hidden");
      if (label) label.textContent = open ? "Close navigation" : "Open navigation";
      navigation.classList.toggle("is-open", open);
      document.body.classList.toggle("nav-open", open);
      navigation.inert = !desktop.matches && !open;
      if (desktop.matches) navigation.removeAttribute("aria-hidden");
      else navigation.setAttribute("aria-hidden", String(!open));
    };
    if (menuButton && navigation) {
      menuButton.hidden = false;
      setMenu(false);
      menuButton.addEventListener("click", () => {
        setMenu(menuButton.getAttribute("aria-expanded") !== "true");
      });
      onChange(desktop, () => setMenu(false));
      document.addEventListener("keydown", event => {
        if (event.key === "Escape" && menuButton.getAttribute("aria-expanded") === "true") {
          setMenu(false);
          menuButton.focus();
        }
      });
    }

    const header = document.querySelector(".site-header");
    if (header) {
      const updateHeader = () => header.classList.toggle("is-scrolled", window.scrollY > 16);
      updateHeader();
      window.addEventListener("scroll", updateHeader, { passive: true });
    }

    // The quick-contact bar appears only after the hero, so it never covers
    // the hero call-to-action buttons on small screens.
    const contact = document.querySelector(".mobile-contact");
    const hero = document.querySelector(".hero");
    if (contact && hero) {
      if ("IntersectionObserver" in window) {
        const contactObserver = new IntersectionObserver(entries => {
          entries.forEach(entry => contact.classList.toggle("is-visible", !entry.isIntersecting));
        }, { threshold: 0 });
        contactObserver.observe(hero);
      } else {
        const updateContact = () => {
          contact.classList.toggle("is-visible", window.scrollY > hero.offsetHeight);
        };
        updateContact();
        window.addEventListener("scroll", updateContact, { passive: true });
      }
    }

    // Google Analytics loads only after explicit consent. No cookies or
    // analytics requests are made when a visitor declines or has not chosen.
    const measurementId = document.querySelector('meta[name="ga-measurement-id"]')?.content;
    const disableKey = measurementId ? `ga-disable-${measurementId}` : null;
    let analyticsLoaded = false;
    const clearAnalyticsCookies = () => {
      const host = window.location.hostname;
      const parent = host.split(".").slice(-2).join(".");
      const domains = ["", host, `.${host}`];
      if (parent && parent !== host) domains.push(`.${parent}`);
      document.cookie.split(";").forEach(part => {
        const name = part.split("=")[0].trim();
        if (!/^_(ga|gid|gat|gcl)/.test(name)) return;
        domains.forEach(domain => {
          const suffix = domain ? `; domain=${domain}` : "";
          document.cookie = `${name}=; Max-Age=0; path=/${suffix}; SameSite=Lax`;
        });
      });
    };
    const setAnalyticsEnabled = enabled => {
      if (!disableKey) return;
      window[disableKey] = !enabled;
      if (typeof window.gtag === "function") {
        window.gtag("consent", "update", { analytics_storage: enabled ? "granted" : "denied" });
      }
    };
    const loadAnalytics = () => {
      if (!measurementId || analyticsLoaded) return;
      analyticsLoaded = true;
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { window.dataLayer.push(arguments); };
      window.gtag("js", new Date());
      window.gtag("config", measurementId, { anonymize_ip: true });
      const script = document.createElement("script");
      script.async = true;
      script.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(measurementId)}`;
      document.head.appendChild(script);
    };

    const banner = document.querySelector(".cookie-banner");
    const consent = readConsent();
    let settingsTrigger = null;
    const openBanner = trigger => {
      if (!banner) return;
      settingsTrigger = trigger || null;
      banner.hidden = false;
      const first = banner.querySelector("button");
      if (first) first.focus({ preventScroll: true });
    };
    if (consent === "granted") {
      setAnalyticsEnabled(true);
      loadAnalytics();
      root.dataset.analyticsConsent = "granted";
    } else if (consent === "denied") {
      setAnalyticsEnabled(false);
      clearAnalyticsCookies();
      root.dataset.analyticsConsent = "denied";
    }
    if (banner) {
      banner.querySelectorAll("[data-consent]").forEach(button => {
        button.addEventListener("click", () => {
          const choice = button.dataset.consent === "granted" ? "granted" : "denied";
          writeConsent(choice);
          banner.hidden = true;
          root.dataset.analyticsConsent = choice;
          if (choice === "granted") {
            setAnalyticsEnabled(true);
            loadAnalytics();
          } else {
            setAnalyticsEnabled(false);
            clearAnalyticsCookies();
          }
          if (settingsTrigger) {
            settingsTrigger.focus({ preventScroll: true });
            settingsTrigger = null;
          }
        });
      });
      if (consent !== "granted" && consent !== "denied") banner.hidden = false;
    }
    document.querySelectorAll("[data-cookie-settings]").forEach(settings => {
      settings.addEventListener("click", event => {
        event.preventDefault();
        openBanner(settings);
      });
    });

    const reveals = Array.from(document.querySelectorAll("[data-reveal]"));
    let observer;
    const showAll = () => {
      if (observer) observer.disconnect();
      root.classList.remove("reveal-ready");
      reveals.forEach(element => element.classList.add("is-visible"));
    };
    const reveal = () => {
      if (motion.matches || !("IntersectionObserver" in window)) return showAll();
      try {
        observer = new IntersectionObserver(entries => {
          entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          });
        }, { threshold: 0.1, rootMargin: "0px 0px -36px 0px" });
        reveals.forEach(element => {
          if (element.closest(".hero, .site-header, [data-no-reveal]") || element.matches("a, button")) {
            element.classList.add("is-visible");
            return;
          }
          const delay = Math.min(240, Math.max(0, Number(element.dataset.delay) || 0));
          element.style.setProperty("--reveal-delay", `${delay}ms`);
          if (!element.classList.contains("is-visible")) observer.observe(element);
        });
        root.classList.add("reveal-ready");
      } catch (_) { showAll(); }
    };
    reveal();
    onChange(motion, () => {
      if (observer) observer.disconnect();
      reveal();
    });

    // GA4 contact events only. Add Ads conversions after a real destination ID is supplied.
    const eventNames = { call: "click_call", whatsapp: "click_whatsapp", directions: "click_directions" };
    document.addEventListener("click", event => {
      if (event.defaultPrevented) return;
      const link = event.target.closest ? event.target.closest("a") : null;
      if (!link) return;
      if (navigation && navigation.contains(link)) setMenu(false);
      const eventName = eventNames[link.dataset.track];
      if (!eventName || typeof window.gtag !== "function") return;
      const section = /^[a-z][a-z0-9_-]{0,31}$/.test(link.dataset.section || "") ? link.dataset.section : "unknown";
      const parameters = { section, transport_type: "beacon" };
      // Only use static markup labels; never send form fields, phone numbers or URLs.
      if (link.dataset.item) parameters.item_name = link.dataset.item.replace(/[\u0000-\u001f\u007f]/g, "").trim().slice(0, 80);
      try { window.gtag("event", eventName, parameters); } catch (_) { /* Navigation stays native. */ }
    });
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init, { once: true });
  else init();
})();
