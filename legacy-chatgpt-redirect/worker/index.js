const PRIMARY_ORIGIN = "https://keymaker-ecity.pages.dev";

export default {
  fetch(request) {
    const incoming = new URL(request.url);
    const destination = new URL(PRIMARY_ORIGIN);
    // Assign pathname rather than resolving an untrusted URL against the origin.
    destination.pathname = incoming.pathname === "/index.html" ? "/" : incoming.pathname;
    destination.search = incoming.search;

    return new Response(null, {
      status: 301,
      headers: {
        Location: destination.href,
        "Cache-Control": "public, max-age=3600",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "X-Content-Type-Options": "nosniff",
      },
    });
  },
};
