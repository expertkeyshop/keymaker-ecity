"use strict";
(() => {
  if (window.__keymakerUI) return;
  window.__keymakerUI = true;

  const init = () => {
    const root = document.documentElement;
    root.classList.add("js");
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
