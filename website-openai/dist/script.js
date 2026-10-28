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

    // Supplementary content is open in the HTML, so no-JS visitors can read it.
    // On phones, each disclosure remembers the visitor's choice across resizes.
    const compact = window.matchMedia("(max-width: 700px)");
    const mobileFolds = Array.from(document.querySelectorAll("details[data-mobile-fold]"));
    const mobileFoldState = new WeakMap();
    const programmaticFoldState = new WeakMap();
    const main = document.querySelector("main");
    const originalMainChildren = main ? Array.from(main.children) : [];
    const hasMobileOrder = originalMainChildren.some(child => child.hasAttribute("data-mobile-order"));
    const orderedMobileChildren = originalMainChildren.slice().sort((a, b) => {
      const order = child => {
        const value = Number(child.dataset.mobileOrder ?? 90);
        return Number.isFinite(value) ? value : 90;
      };
      return order(a) - order(b);
    });
    const setFoldOpen = (fold, open) => {
      // Native toggle events are asynchronous and can coalesce. Retain the
      // latest requested state even when a rapid resize needs no DOM change.
      programmaticFoldState.set(fold, open);
      if (fold.open !== open) fold.open = open;
    };
    const applyFoldLayout = () => {
      const focused = main?.contains(document.activeElement) ? document.activeElement : null;
      if (main && hasMobileOrder) {
        const children = compact.matches ? orderedMobileChildren : originalMainChildren;
        if (children.some((child, index) => main.children[index] !== child)) main.append(...children);
      }
      mobileFolds.forEach(fold => setFoldOpen(fold,
        compact.matches ? mobileFoldState.get(fold) === true : true));
      if (focused && document.activeElement !== focused && focused.getClientRects().length) {
        focused.focus({ preventScroll: true });
      }
    };
    mobileFolds.forEach(fold => {
      mobileFoldState.set(fold, false);
      const summary = fold.querySelector("summary");
      if (summary) summary.addEventListener("click", event => {
        if (event.defaultPrevented || !compact.matches) return;
        // Keyboard activation also dispatches click. This distinguishes user
        // toggles from a pending programmatic toggle after a breakpoint change.
        programmaticFoldState.delete(fold);
        mobileFoldState.set(fold, !fold.open);
      });
      fold.addEventListener("toggle", () => {
        if (!compact.matches) {
          if (!fold.open) setFoldOpen(fold, true);
          return;
        }
        if (programmaticFoldState.has(fold) &&
            programmaticFoldState.get(fold) === fold.open) {
          programmaticFoldState.delete(fold);
          return;
        }
        programmaticFoldState.delete(fold);
        mobileFoldState.set(fold, fold.open);
      });
    });
    applyFoldLayout();
    onChange(compact, applyFoldLayout);

    const revealFragment = hash => {
      if (!hash || hash === "#") return;
      let id;
      try { id = decodeURIComponent(hash.slice(1)); } catch (_) { return; }
      const target = document.getElementById(id);
      if (!target) return;
      let ancestor = target.closest("details");
      while (ancestor) {
        if (mobileFoldState.has(ancestor)) {
          if (compact.matches) mobileFoldState.set(ancestor, true);
          setFoldOpen(ancestor, true);
        } else if (!ancestor.open) ancestor.open = true;
        ancestor = ancestor.parentElement?.closest("details");
      }
      // Reposition after expanding ancestors and any native fragment scroll.
      // Immediate movement also respects reduced-motion preferences.
      window.requestAnimationFrame(() => target.scrollIntoView({ behavior: "auto", block: "start" }));
    };
    window.addEventListener("hashchange", () => revealFragment(window.location.hash));
    if (window.location.hash) revealFragment(window.location.hash);

    const header = document.querySelector(".site-header");
    if (header) {
      const topBand = document.querySelector(".availability-bar");
      // Observing the top band avoids a synchronous layout read immediately
      // after mobile content has been reordered and folded.
      if (topBand && "IntersectionObserver" in window) {
        const headerObserver = new IntersectionObserver(entries => {
          header.classList.toggle("is-scrolled", !entries[0].isIntersecting);
        });
        headerObserver.observe(topBand);
      }
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

    // The consent-gated GTM module owns Analytics. The UI never loads gtag.js.
    const setAnalyticsEnabled = enabled => window.keymakerAnalytics?.setConsent(enabled ? "granted" : "denied");
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
      root.dataset.analyticsConsent = "granted";
    } else if (consent === "denied") {
      setAnalyticsEnabled(false);
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
          } else {
            setAnalyticsEnabled(false);
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
      if (compact.matches || motion.matches || !("IntersectionObserver" in window)) return showAll();
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
    onChange(compact, () => {
      if (observer) observer.disconnect();
      reveal();
    });

    // Authored content labels only; never track customer message text or link URLs.
    document.querySelectorAll("#faq .faq-list > details").forEach((detail, index) => {
      detail.addEventListener("toggle", () => {
        if (detail.open) window.keymakerAnalytics?.track("faq_open", { section: "faq", question_id: `faq_${index + 1}` });
      });
    });
    if ("IntersectionObserver" in window) {
      const measuredSections = new Set();
      const sectionObserver = new IntersectionObserver(entries => {
        if (!window.keymakerAnalytics?.isEnabled()) return;
        entries.forEach(entry => {
          if (!entry.isIntersecting) return;
          const section = entry.target.closest("section")?.id;
          if (!section || measuredSections.has(section)) return;
          if (window.keymakerAnalytics.track("view_section", { section })) {
            measuredSections.add(section);
            sectionObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.5 });
      document.querySelectorAll("#services h2, #products h2, #visit h2").forEach(heading => sectionObserver.observe(heading));
    }

    const eventNames = { call: "click_call", whatsapp: "click_whatsapp", directions: "click_directions", review: "click_review" };
    document.addEventListener("click", event => {
      if (event.defaultPrevented) return;
      const link = event.target.closest ? event.target.closest("a") : null;
      if (!link) return;
      if (navigation && navigation.contains(link)) setMenu(false);
      if (!event.ctrlKey && !event.metaKey && !event.shiftKey && !event.altKey &&
          (event.button === undefined || event.button === 0) &&
          (!link.target || link.target === "_self")) {
        try {
          const destination = new URL(link.href, window.location.href);
          const current = new URL(window.location.href);
          if (destination.origin === current.origin && destination.pathname === current.pathname &&
              destination.search === current.search && destination.hash) revealFragment(destination.hash);
        } catch (_) { /* Non-URL actions retain their native behavior. */ }
      }
      const eventName = eventNames[link.dataset.track];
      if (!eventName) return;
      const section = /^[a-z][a-z0-9_-]{0,31}$/.test(link.dataset.section || "") ? link.dataset.section : "unknown";
      const parameters = { section, contact_method: link.dataset.track };
      // Only use static markup labels; never send form fields, phone numbers or URLs.
      if (link.dataset.item) parameters.item_name = link.dataset.item.replace(/[\u0000-\u001f\u007f]/g, "").trim().slice(0, 80);
      try { window.keymakerAnalytics?.track(eventName, parameters); } catch (_) { /* Navigation stays native. */ }
    });
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init, { once: true });
  else init();
})();
