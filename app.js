(() => {
  'use strict';
  const sources = {
    guidelines: ['Represent your business accurately', 'https://support.google.com/business/answer/3038177?hl=en'],
    categories: ['Choose the right categories', 'https://support.google.com/business/answer/7249669?hl=en'],
    links: ['Booking and business link policies', 'https://support.google.com/business/answer/13769188?hl=en'],
    areas: ['Set accurate service areas', 'https://support.google.com/business/answer/9157481?hl=en'],
    ranking: ['Understand local ranking', 'https://support.google.com/business/answer/7091?hl=en'],
    edit: ['Edit your Business Profile', 'https://support.google.com/business/answer/3039617?hl=en']
  };
  const groups = [
    { id: 'first', title: 'Start with the essentials', subtitle: 'A few important fixes to get the foundations right.', badge: '', tasks: [
      { id: 'name', title: 'Match your name to your signboard', summary: 'Your real business name, without extra keywords.', time: '2 min', where: 'Edit profile → About → Business name', steps: ['Compare the name in Google with your permanent shop sign and branding.', 'Use “Key Maker & Locksmith” only if that is the name customers see.', 'Confirm the profile is verified in the Google account you use to manage it.'], next: 'Make sure it matches the sign above your door.', source: 'guidelines' },
      { id: 'category', title: 'Choose the right primary category', summary: 'Help Google understand what you do best.', time: '5 min', where: 'Edit profile → About → Business category', steps: ['Choose “Locksmith” as primary if lock repair, replacement and lockouts are your main work.', 'If most of your work is duplicate keys, keep “Key duplication service” as primary and add “Locksmith” as a secondary.', 'Select only accurate categories offered in Google’s dropdown. Use a few relevant categories, rather than one for every service.'], note: 'Your main line of work is unconfirmed. Category changes can require verification.', next: 'Pick the category that best describes your main business.', source: 'categories' },
      { id: 'description', title: 'Give your description a fresh start', summary: 'Fix the typo and make your location and services clear.', time: '5 min', where: 'Edit profile → About → Description', steps: ['Open the description draft under Ready-to-copy.', 'Remove any services you do not provide. Keep it factual and within 750 characters.', 'Copy the text into Google, save it and check the edit status.'], draft: true, next: 'A ready-to-copy description is waiting for your review.', source: 'guidelines' },
      { id: 'hours', title: 'Double-check your 24-hour availability', summary: 'Set hours that match when customers can get service.', time: '5 min', where: 'Edit profile → Hours', steps: ['Confirm whether customers can visit the staffed shop at every advertised hour.', 'If the shop closes, use its actual staffed hours. Describe after-hours emergency call-outs accurately if offered.', 'Test that your business number is answered during advertised service hours.'], next: 'Check your shop hours and emergency call-out availability.', source: 'guidelines' },
      { id: 'attributes', title: 'Make every attribute accurate', summary: 'Review accessibility, parking and facilities.', time: '10 min', where: 'Edit profile → More', steps: ['Check assisted listening devices and changing tables; remove these claims if those facilities are absent.', 'Verify wheelchair-accessible entrance, seating and parking against the actual facilities.', 'Review other listed attributes, including on-site service, so they reflect what customers can expect.'], next: 'Review the unusual facilities listed in your profile.', source: 'guidelines' },
      { id: 'booking', title: 'Make the appointment option work', summary: 'Use a real booking page, or remove the claim.', time: '5 min', where: 'Booking options, if available; Edit profile → More', steps: ['If you have a working booking page and Google offers a booking field, add its dedicated link.', 'If customers cannot book online, remove “Offers online appointments”. Walk-in service can still be available.', 'Keep https://wa.me/919762306303 in the WhatsApp contact field. Google’s action-link policy excludes messaging links from booking links.'], next: 'Check that online appointments really have a booking flow.', source: 'links' }
    ] },
    { id: 'week', title: 'Build it out this week', subtitle: 'Show customers what you offer and how to reach you.', badge: 'week', tasks: [
      { id: 'services', title: 'Give each service its own listing', summary: 'Key duplication, vehicle keys, lock repairs and lockouts.', time: '15 min', where: 'Edit services', steps: ['Review the service descriptions under Ready-to-copy.', 'Add separate entries for house keys, car keys, bike keys, lock repair, lock replacement and emergency lockouts, only where offered.', 'Add your real prices where useful. If a job is variable, explain what affects the quote.', 'Do not add chip programming, smart locks or safe opening unless you provide those services.'], draft: true, next: 'List your actual services using the prepared descriptions.', source: 'edit' },
      { id: 'website', title: 'Add a simple business website', summary: 'One useful page is a great place to start.', time: '30+ min', where: 'Edit profile → Contact → Website', steps: ['Prepare a public page showing your services, address, actual hours, phone, WhatsApp and directions.', 'Use the same business identity as your signboard and Google profile.', 'Test the page on a phone, then add its URL in Google. Add social pages in supported social-link fields.'], next: 'Add a public page that helps customers call and find the shop.', source: 'edit' },
      { id: 'areas', title: 'Review your service area coverage', summary: 'Keep the places you actually visit. No need to fill all 20.', time: '10 min', where: 'Edit profile → Location → Service area', steps: ['Review the 20 locations shown in Business details.', 'Keep areas you genuinely serve. Check travel time and availability for farther locations such as Sarjapura and Jigani.', 'Keep your storefront address visible if customers visit the shop and it has permanent signage.', 'Verify that your map pin marks the real entrance. Correct the address only if it is inaccurate.'], next: 'Make sure your service coverage matches the jobs you accept.', source: 'areas' },
      { id: 'photos', title: 'Let customers see your shop', summary: 'Real photos of your storefront, machines and work.', time: '20 min', where: 'Photos → Add photos', steps: ['Upload clear daytime photos of the signboard, street-facing storefront and entrance.', 'Add interior, key-cutting machine and genuine work photos, with permission for identifiable people.', 'Add a logo and suitable cover photo if available. Avoid showing sensitive key patterns, customer addresses or security codes.', 'Optionally record a short key-cutting video. A 20–30 second clip is enough; photo geotagging is not a required checklist step.'], next: 'Start with a clear storefront photo to help customers find you.', source: 'ranking' },
      { id: 'payments', title: 'Confirm your payment options', summary: 'Let customers know how they can pay.', time: '3 min', where: 'Edit profile → More, if payment fields are offered', steps: ['Select only the payment methods you accept, such as cash, UPI or cards.', 'If your category or region does not expose payment attributes, confirm them on your website instead.', 'Do not claim card acceptance unless your card payment setup works.'], next: 'Check which payment options are true and available to list.', source: 'edit' },
      { id: 'consistency', title: 'Create free Justdial and Sulekha listings', summary: 'The same shop name, phone and address across listings.', time: '20 min', where: 'Justdial and Sulekha free-listing forms', steps: ['Check your existing Justdial, Sulekha, Facebook, Bing Places and other business listings.', 'Correct name, address, phone and hours where you already have a listing.', 'Avoid creating duplicate profiles on Google or signing up to directories just to fill space.'], next: 'Check your existing listings against your real shop details.', source: 'guidelines' }
    ] },
    { id: 'ongoing', title: 'Keep the good things going', subtitle: 'Repeat these habits as your business grows.', badge: 'ongoing', tasks: [
      { id: 'reviews', title: 'Reply to reviews and invite honest feedback', summary: 'Build trust, one real customer at a time.', time: 'Weekly', where: 'Read reviews; Ask for reviews', steps: ['Reply to existing reviews in your own voice, without exposing customer details.', 'Copy your real review link from “Ask for reviews” and use it in the prepared request.', 'Invite customers consistently. Do not offer incentives, ask only happy customers or require a five-star rating.'], draft: true, next: 'Reply to a review and get your genuine review request ready.', source: 'ranking' },
      { id: 'posts', title: 'Share a useful shop update', summary: 'Show a real service or introduce your new shop.', time: 'Weekly', where: 'Add update', steps: ['Review the prepared shop announcement in Ready-to-copy.', 'Pair it with a genuine shop or work photo.', 'Publish when you have useful news. Weekly is an optional planning rhythm, not a Google ranking requirement.'], draft: true, next: 'Introduce your shop with a useful update and a real photo.', source: 'edit' },
      { id: 'special', title: 'Review upcoming holiday hours', summary: 'Keep customers informed when your schedule changes.', time: 'As needed', where: 'Edit profile → Hours → Special hours', steps: ['Check your actual schedule for upcoming holidays and closures.', 'Set special hours when they differ from the usual schedule; confirm normal holiday hours if Google prompts you.', 'Recheck that public hours match the staffing and service you can provide.'], next: 'Check upcoming closures and set accurate special hours.', source: 'ranking' },
      { id: 'performance', title: 'Check what brings customers to you', summary: 'Review available profile performance each month.', time: 'Monthly', where: 'Performance', steps: ['Record the available metrics, such as call-button clicks, direction requests and website clicks.', 'Review relevant search terms if shown. Clicks are interest signals, not confirmed completed jobs.', 'Compare similar periods and note which enquiries actually turn into work. Plan the next improvement from that evidence.'], next: 'Record a monthly baseline so you can see what changes.', source: 'ranking' }
    ] }
  ];
  // Execution snapshot, verified 21 October 2026. This is not a live Google feed.
  groups[0].tasks.splice(5, 0, {id:'contact', title:'Resolve public phone visibility', time:'Google follow-up', where:'Edit profile → Contact; public Search/Maps', source:'edit'});
  groups[1].tasks.splice(1, 0, {id:'products', title:'Publish accurate physical products', time:'Added', where:'Edit products', source:'edit', draft:true});
  const execution = {"name": {"status": "Owner-confirmed signboard match", "summary": "On 22 October 2026 the owner confirmed the full permanent shop name is Key Maker & Locksmith | Electronic City, matching the public Google name.", "steps": ["Owner confirmed on 22 October that the full permanent signboard name is Key Maker & Locksmith | Electronic City.", "The same name appears publicly on the Google profile.", "Keep the same real-world name on the new directory listings."], "complete": true}, "category": {"status": "Saved in Google", "summary": "Locksmith is primary; Key Duplication Service is additional.", "steps": ["Both categories were saved using Google’s category dropdown and verified in the editor.", "The public listing now identifies the shop as a locksmith.", "Revisit only if your actual main business changes."], "complete": true}, "description": {"status": "Saved and public", "summary": "The corrected 490-character description is saved and visible publicly.", "steps": ["The description covers your location, confirmed services, 24-hour availability, on-site coverage and accepted payments.", "The original “locksmit” typo was corrected.", "No unconfirmed prices or competitor details were copied."], "complete": true}, "hours": {"status": "Owner-confirmed and checked", "summary": "Google shows 24 hours every day, matching your confirmation.", "steps": ["Monday–Sunday are set to Open 24 hours.", "You confirmed that the shop and service are always available.", "Keep the phone answered and update hours if availability changes."], "complete": true}, "attributes": {"status": "Owner-confirmed and checked", "summary": "Your confirmed accessibility, parking and facilities were retained.", "steps": ["You confirmed the listed accessible entrance, seating, parking, assisted listening devices and changing table.", "Existing on-site services were checked in the editor.", "Revisit attributes if the actual facilities change."], "complete": true}, "booking": {"status": "Checked", "summary": "The current editor lists on-site services; the old online-appointments claim is absent.", "steps": ["No unsupported booking claim remains in the current service-options list.", "WhatsApp stays in the chat field. It was not inserted as an appointment link.", "Add a booking link only if a genuine booking page becomes available."], "complete": true}, "contact": {"status": "Awaiting Google review — owner reported", "summary": "The phone is saved, but public display remains pending. On 22 October the owner reported that Google review is pending. Wait for Google’s decision and recheck visibility; do not repeatedly resubmit the number.", "steps": ["Phone +91 97623 06303 is saved; the “Don’t show” switch was already checked off.", "The owner reports pending Google review on 22 October. This is owner-reported status, not a fresh independent approval decision.", "Wait for the review result and check the public phone button. Avoid repeated edits while review is pending."], "complete": false}, "services": {"status": "All descriptions saved and verified", "summary": "All 29 services have complete descriptions; none exceed 300 characters.", "steps": ["Filled the 12 empty standard descriptions through the connected Windsor action after exact approval.", "A fresh readback verified every description matches the approved payload; all 17 existing custom descriptions were retained.", "Standard services shown under both Google categories share the same underlying item; no duplicate was added.", "No service prices changed. Service names were checked for spelling, misleading compatibility claims and keyword stuffing."], "complete": true}, "website": {"status": "Public and linked", "summary": "Customer website is public; Google now shows its Website button.", "steps": ["The live site includes services, 24-hour hours, phone, WhatsApp, directions and confirmed payment methods.", "Canonical metadata, sitemap, robots.txt and Locksmith structured data were added.", "The actual Google review link is in the site footer.", "Production version 2 was deployed successfully and checked in the browser."], "complete": true}, "areas": {"status": "Owner-confirmed and checked", "summary": "You confirmed that you serve all 20 existing areas.", "steps": ["All 20 areas were checked against the saved editor list.", "You explicitly confirmed Sarjapura, Jigani, Huskur, Kudlu Gate and the remaining listed areas.", "No service areas were removed or invented. Continue quoting travel charges for the exact customer address."], "complete": true}, "photos": {"status": "Cover and logo verified", "summary": "Actual storefront cover and proper gold/black shop logo were visually verified in Google Photos.", "steps": ["Google Photos UI showed the actual storefront as the cover and a proper gold/black Key Maker Locksmith logo on 22 October 2026.", "Evidence: gbp-cover-logo-verified.png in the keymaker workspace.", "Six owner-authorized AI product illustrations are already uploaded separately. Continue adding useful real shop/work photos when available."], "complete": true}, "payments": {"status": "Confirmed and published", "summary": "Cash, UPI, IMPS and NEFT are stated on the website; no cards claimed.", "steps": ["Your payment methods were included in the saved description and the public website.", "This profile editor did not expose a Payments attribute, so none was invented.", "Update the website if your accepted payment methods change."], "complete": true}, "consistency": {"status": "Owner profiles saved; public verification pending", "summary": "Both directory owner profiles have saved information and three gallery photos each. Justdial categories/map and both public URL/address checks remain pending. Sulekha has no exposed street/map editor. Google phone remains under owner-reported review.", "steps": ["Sulekha About, website, payments, all seven 24-hour days, 2026, service mapping, cover/logo and three gallery photos were saved. The owner confirmed current company type Freelance - GST Unregistered and employee range 11–25 on 22 October; this supersedes the earlier Sole Proprietorship answer.", "Justdial owner details and three gallery images are saved/readback-verified: bike-key work, storefront and logo. Accepted originals were 2304×4096,1600×900 and 1254×1254 respectively.", "Justdial categories still show 5 Pending; map info and public/share destination remain unverified. Public address consistency must be checked before completing this task.", "Directory UI completeness scores are platform measures, not SEO ranking. The owner-authorized email to care@sulekha.com was sent on 22 October and separately verified with Gmail SENT metadata. No WhatsApp message, paid plan or invented private field was used. Public directory verification remains open."], "complete": false}, "reviews": {"status": "Current audit complete", "summary": "All 33 existing reviews have replies. Your real review link and printable QR are ready.", "steps": ["Google’s Unreplied filter showed “You’ve replied to new reviews”. Existing replies were retained.", "The review URL was obtained from your own Ask for reviews screen.", "Use review-counter-sign.html at the counter. Invite honest feedback consistently without incentives.", "No review-request messages were sent to customers. Repeat the reply check regularly."], "complete": true}, "posts": {"status": "Published", "summary": "Shop announcement, FAQ update, two service Updates, SPARE10 Offer and opening Update are published.", "steps": ["The shop announcement and FAQ update were verified earlier.", "The car remote and door lock Updates were verified Published on 21 October; the approved SPARE10 Offer is also Published.", "A fresh 22 October view showed the opening announcement Update as Published. It correctly states the real opening date of 1 October 2026; the past-date Event form was unavailable.", "The latest two service Updates and opening Update have no CTA. All six products are live with owner-authorized representative AI imagery; no duplicate posts or products are needed."], "complete": true}, "special": {"status": "Current schedule reviewed", "summary": "No holiday exceptions were supplied to your confirmed always-24/7 schedule.", "steps": ["No holiday closures or reduced hours were invented.", "Keep normal hours when they remain accurate.", "Add or confirm special hours if your actual holiday schedule changes or Google asks you to confirm them."], "complete": true}, "performance": {"status": "Baseline recorded", "summary": "September–October 2026: 224 views and 26 interactions.", "steps": ["Google’s selected period was September 2026–October 2026; October is still in progress.", "Interactions: 20 direction requests, 6 chat clicks, 0 call clicks and 0 website clicks. September interactions were 0; October interactions were 26.", "Views: 109 Maps mobile, 100 Search mobile, 8 Maps desktop, 7 Search desktop.", "Searches were fewer than 50, so search terms were unavailable. Compare equivalent periods later; clicks are not confirmed jobs."], "complete": true}, "products": {"status": "All six products live", "summary": "All six products and prices are publicly visible, including the corrected Computerised key title.", "steps": ["All six generic prices were verified in the public catalogue: key ₹250; remote shell ₹650; handle ₹700; cylinder ₹950; main door lock ₹2,300; remote unit ₹1,500.", "The same first product was corrected to Computerised key with representative-image wording. Fresh public Search showed the corrected title, the owner catalogue showed no Pending label, and public product detail confirmed the exact description with its representative AI-image disclosure.", "The six images are owner-authorized AI representative illustrations, not photographs of actual stock. You can update prices later. No more product images are needed for this completed workflow.", "All new Updates and the approved SPARE10 Offer are Published. The offer end-time control still needs a manual check: terms say 23:59 but readback shows 11:59 without AM/PM."], "complete": true}};
  groups.forEach(group => group.tasks.forEach(task => {
    const snapshot = execution[task.id];
    task.summary = snapshot.status + ' · ' + snapshot.summary;
    task.steps = snapshot.steps;
    task.next = snapshot.summary;
    task.note = 'Checked 21 October 2026. ' + (snapshot.complete ? 'Completed or reviewed for the current snapshot; recurring care continues.' : 'Still open; do not treat this as completed.');
  }));
  const executionRevision = '2026-10-21-final-v2';
  const productPublicationRevision = '2026-10-22-six-products';
  const signboardConfirmationRevision = '2026-10-22-owner-full-signboard';
  const coverLogoRevision = '2026-10-22-cover-logo-verified';
  const services = [
  [
    "Building lockouts",
    "24-hour lockout assistance for homes, offices and shops. On-site help is available for authorised owners and occupants. Share your location and lock details to confirm availability, call-out charges and the quote."
  ],
  [
    "Building key copying",
    "Duplicate keys for supported home, office, shop and cupboard locks. Bring the original key so we can check the correct blank and cutting requirements. Contact us to confirm compatibility and pricing."
  ],
  [
    "Car digital and remote key reprogramming",
    "Programming and reprogramming for compatible car transponder keys and remotes. Share the make, model, year and existing key details to confirm support and the quote. Service availability depends on the vehicle and key system."
  ],
  [
    "Car key copying",
    "Spare car keys for supported makes and models. We check the key type, cutting requirements and any chip or remote programming needed. Bring your original key and vehicle details to confirm compatibility and pricing."
  ],
  [
    "Car lockouts",
    "24-hour assistance when keys are locked inside a supported vehicle. Available to authorised owners and users. Call with your location, vehicle make and model so we can confirm access options, availability and charges."
  ],
  [
    "Door lock and bolt hardware installation",
    "Installation of compatible door locks, cylinders, handles and bolts for homes, offices and shops. Share door and existing hardware details to confirm suitable parts, fitting requirements and installation charges."
  ],
  [
    "Lock rekeying",
    "Rekeying for compatible locks so they work with a different key. Useful when keys are lost or access needs to change. Share the lock type to confirm whether rekeying is suitable and to receive a quote."
  ],
  [
    "New key fob creation",
    "New electronic key fobs for compatible vehicles. Supply the vehicle make, model, year and key details so we can check the correct fob, cutting and programming requirements. Parts and programming are quoted for the specific vehicle."
  ],
  [
    "Repair hardware",
    "Repair assistance for compatible door lock hardware, including cylinders, handles and related fittings. Share photos or details of the fault so we can check repair options, parts availability and the quote."
  ],
  [
    "Safe lock install, open and repair",
    "Safe opening, lock installation and repair for authorised owners. Share the safe type and the problem to confirm service availability, access requirements and pricing. Work depends on the safe and locking system."
  ],
  [
    "Security door locks",
    "Supply, installation, repair and replacement of compatible security door locks. We check the existing lock, door type and required fittings before recommending suitable parts and quoting for the work."
  ],
  [
    "Window locks",
    "Repair and replacement of compatible window locks and locking hardware. Share the window and lock type, the fault and your location so we can confirm suitable parts, service availability and pricing."
  ],
  [
    "House key duplication",
    "Duplicate keys for supported house and door locks. Bring your original key or share the key type so we can confirm compatibility and quote."
  ],
  [
    "Lock repair and replacement",
    "Repair and replacement of compatible door locks, cylinders and handles for homes, offices and shops. Contact us with the lock details and location for parts, installation and call-out pricing."
  ],
  [
    "Office and shop key duplication",
    "Key duplication for supported office, shop and cupboard locks. Contact us with the original key or lock details to confirm the suitable blank and price."
  ],
  [
    "Computerised key duplication",
    "Duplication of compatible computerised, dimple and high-security keys. Bring the original key or share its type to confirm support and the correct key blank."
  ],
  [
    "Car remote key body and cover replacement",
    "Replacement of compatible car remote key bodies, shells and covers. Share your vehicle model and remote type so we can confirm fit, availability and pricing."
  ],
  [
    "24-hour key making",
    "Key making assistance available 24 hours every day. Call with your key type and location to confirm the service, timing and any call-out charges."
  ],
  [
    "Home lockout assistance",
    "24-hour lockout help for authorised home owners and occupants. Contact us with your address and lock details to confirm availability and the applicable quote."
  ],
  [
    "Main door lock replacement",
    "Replacement of compatible main door locks, cylinders and handles. Contact us with the existing lock details to discuss suitable parts and installation charges."
  ],
  [
    "Spare key cutting",
    "Spare keys cut for supported home, office, shop and vehicle key types. Bring the original key or share its details to confirm the suitable blank and price."
  ],
  [
    "Padlock key duplication",
    "Duplicate keys for compatible padlocks. Bring your original key or share the padlock and key details so we can confirm the suitable blank and quote."
  ],
  [
    "Grille lock repair",
    "Repair assistance for compatible grille and gate locks. Share the lock details and location to confirm the available repair, parts and call-out charges."
  ],
  [
    "Bike key making",
    "Bike key making and duplication for supported models. Contact us with your bike model and key details to confirm availability and pricing."
  ],
  [
    "Bike key replacement",
    "Replacement keys for compatible bikes. Share your bike make, model and key or lock details so we can confirm the required service and quote."
  ],
  [
    "Door lock repair",
    "Repair of sticking, faulty or damaged door locks for homes, offices and shops. Contact us with the lock type and location to confirm parts, service and pricing."
  ],
  [
    "Car key repair",
    "Repair assistance for compatible car keys and remote key bodies. Share the vehicle model, key type and problem so we can confirm the available repair and quote."
  ],
  [
    "Car key making",
    "Car key making and duplication for supported makes and models. Share the vehicle make, model, year and key type to confirm compatibility and the applicable quote."
  ],
  [
    "Emergency locksmith services",
    "24-hour locksmith and lockout assistance for authorised owners and occupants. Call with your location and lock details to confirm availability, travel charges and the quote."
  ]
];
  const areas = ['Jigani', 'Bommasandra', 'Hulimangala', 'Huskur', 'Begur', 'Basapura', 'Rayasandra', 'Chandapura', 'Bettadasanapura', 'Sarjapura', 'Kudlu Gate', 'Hebbagodi', 'Electronic City Phase II', 'Shikaripalya', 'Hosa Road', 'Konappana Agrahara', 'Doddathoguru', 'Neeladri Nagar', 'Ananth Nagar Phase 2', 'Veerasandra 2nd Stage'];
  const description = "Key Maker & Locksmith provides 24-hour key making and locksmith services on Gollahalli Main Road, Electronic City Phase 1, Bengaluru. We duplicate keys for homes, offices and shops, make car and bike keys, repair and replace door locks, and help with lockouts. We also replace compatible car remote key bodies and covers. Visit our shop or contact us for on-site service in Electronic City and nearby areas, including call-outs 10 km or more away. Cash, UPI and bank transfers are accepted.";
  const post = "Need a spare key or help with a lock? Key Maker & Locksmith on Gollahalli Main Road, Electronic City Phase 1, Bengaluru is available 24 hours for key making, door lock repair and replacement, and lockout assistance. We also make keys for supported cars and bikes and replace compatible car remote key bodies and covers. Visit the shop or contact us for on-site service. Cash, UPI and bank transfers are accepted.";
  const reviewRequest = "Thank you for choosing Key Maker & Locksmith. Please share an honest review of your experience here: https://g.page/r/CdLplcdusA5eEBM/review. Your feedback helps us improve and helps other customers find our shop.";
  const allTasks = groups.flatMap(group => group.tasks);
  const $ = id => document.getElementById(id);
  const storageKey = 'keymaker-gbp-v1';
  let done = {}, draft = description, filter = 'all', canSave = true, toastTimer, savedRevision = '', savedProductPublicationRevision = '', savedSignboardConfirmationRevision = '', savedCoverLogoRevision = '';
  try {
    const saved = JSON.parse(localStorage.getItem(storageKey) || '{}');
    if (saved && typeof saved === 'object') {
      savedRevision = saved.executionRevision || '';
      savedProductPublicationRevision = saved.productPublicationRevision || '';
      savedSignboardConfirmationRevision = saved.signboardConfirmationRevision || '';
      savedCoverLogoRevision = saved.coverLogoRevision || '';
      if (saved.done && typeof saved.done === 'object') allTasks.forEach(task => { if (saved.done[task.id] === true) done[task.id] = true; });
      if (typeof saved.draft === 'string' && saved.draft.length <= 750) draft = saved.draft;
    }
    localStorage.setItem('keymaker-storage-test', '1');
    localStorage.removeItem('keymaker-storage-test');
  } catch { canSave = false; }
  if (savedRevision !== executionRevision) {
    // Seed the factual audit once; subsequent manual ticks and resets stay under owner control.
    allTasks.forEach(task => { if (execution[task.id].complete) done[task.id] = true; else delete done[task.id]; });
  }
  // Add the newly verified product tick once without changing other saved owner progress.
  if (savedProductPublicationRevision !== productPublicationRevision && execution.products.complete) done.products = true;
  if (savedSignboardConfirmationRevision !== signboardConfirmationRevision && execution.name.complete) done.name = true;
  if (savedCoverLogoRevision !== coverLogoRevision && execution.photos.complete) done.photos = true;
  function icon(name) {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('aria-hidden', 'true');
    const use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
    use.setAttribute('href', '#i-' + name); svg.append(use); return svg;
  }
  function element(tag, cls, text) {
    const el = document.createElement(tag);
    if (cls) el.className = cls;
    if (text !== undefined) el.textContent = text;
    return el;
  }
  function notify(message) {
    $('toast').textContent = message; $('toast').classList.add('visible');
    clearTimeout(toastTimer); toastTimer = setTimeout(() => $('toast').classList.remove('visible'), 3500);
  }
  function save() {
    try { localStorage.setItem(storageKey, JSON.stringify({done, draft, executionRevision, productPublicationRevision, signboardConfirmationRevision, coverLogoRevision})); canSave = true; }
    catch { canSave = false; }
    $('saveStatus').replaceChildren(icon(canSave ? 'check' : 'clock'), document.createTextNode(canSave ? 'Progress saved on this browser' : 'Progress kept for this session only'));
  }
  function renderTasks() {
    const container = $('taskGroups'); container.replaceChildren();
    let shown = 0;
    groups.forEach(group => {
      const visible = group.tasks.filter(task => filter === 'all' || (filter === 'done' ? !!done[task.id] : !done[task.id]));
      if (!visible.length) return;
      shown += visible.length;
      const section = element('section', 'task-group');
      const heading = element('div', 'group-heading');
      heading.append(element('span', 'stage-dot ' + group.badge), element('h3', '', group.title), element('span', 'group-counter', `${group.tasks.filter(t => done[t.id]).length} / ${group.tasks.length}`));
      section.append(heading, element('p', 'group-description', group.subtitle));
      const list = element('div', 'task-list');
      visible.forEach(task => {
        const row = element('article', 'task-row' + (done[task.id] ? ' done' : '')); row.id = 'task-' + task.id;
        const top = element('div', 'task-top');
        const checkWrap = element('span', 'check-wrap');
        const checkbox = element('input', 'task-checkbox'); checkbox.type = 'checkbox'; checkbox.checked = !!done[task.id];
        checkbox.setAttribute('aria-label', `Mark “${task.title}” complete`);
        checkbox.addEventListener('change', () => {
          if (checkbox.checked) done[task.id] = true; else delete done[task.id];
          row.classList.toggle('done', checkbox.checked); save(); updateProgress();
          const sectionCounter = section.querySelector('.group-counter');
          sectionCounter.textContent = `${group.tasks.filter(t => done[t.id]).length} / ${group.tasks.length}`;
          if (filter !== 'all') {
            const nextFocus = row.nextElementSibling?.querySelector('.task-checkbox') || row.previousElementSibling?.querySelector('.task-checkbox');
            const nextLabel = nextFocus?.getAttribute('aria-label');
            renderTasks();
            const target = nextLabel && [...document.querySelectorAll('.task-checkbox')].find(el => el.getAttribute('aria-label') === nextLabel);
            (target || document.querySelector(`[data-filter="${filter}"]`)).focus();
          }
        });
        checkWrap.append(checkbox, icon('check'));
        const expand = element('button', 'task-expand'); expand.type = 'button';
        expand.setAttribute('aria-expanded', 'false'); expand.setAttribute('aria-controls', 'detail-' + task.id);
        const text = element('span', 'task-text'); text.append(element('span', 'task-title', task.title), element('span', 'task-summary', task.summary));
        const chevron = icon('chevron'); chevron.classList.add('chevron');
        expand.append(text, element('span', 'task-time', task.time), chevron);
        const detail = element('div', 'task-detail'); detail.id = 'detail-' + task.id; detail.hidden = true;
        const where = element('div', 'where'); where.append(icon('pin'), document.createTextNode(task.where));
        const steps = element('ol'); task.steps.forEach(step => steps.append(element('li', '', step)));
        detail.append(where, steps);
        if (task.note) detail.append(element('p', 'task-note', task.note));
        const actions = element('div', 'task-detail-actions');
        const action = element('a', 'text-link', task.draft ? 'See ready-to-copy text' : 'Open Google profile');
        action.href = task.draft ? '#drafts' : 'https://business.google.com/';
        if (!task.draft) { action.target = '_blank'; action.rel = 'noopener noreferrer'; }
        action.append(icon(task.draft ? 'arrow' : 'external'));
        const policy = element('a', 'policy-link', 'Google guidance'); policy.href = sources[task.source][1]; policy.target = '_blank'; policy.rel = 'noopener noreferrer';
        actions.append(action, policy); detail.append(actions);
        expand.addEventListener('click', () => { const opening = expand.getAttribute('aria-expanded') !== 'true'; expand.setAttribute('aria-expanded', String(opening)); detail.hidden = !opening; });
        top.append(checkWrap, expand); row.append(top, detail); list.append(row);
      });
      section.append(list); container.append(section);
    });
    if (!shown) container.append(element('div', 'empty-state', filter === 'done' ? 'Your completed tasks will appear here. Every small step counts.' : 'All caught up! Keep your recurring tasks on your regular schedule.'));
  }
  function updateProgress() {
    const count = allTasks.filter(task => done[task.id]).length;
    $('doneCount').textContent = count;
    const percent = Math.round(count / allTasks.length * 100);
    $('percent').textContent = percent + '%'; $('progressFill').style.width = percent + '%';
    document.querySelector('[role="progressbar"]').setAttribute('aria-valuenow', count);
    $('navCount').textContent = allTasks.length - count;
    $('progressMessage').textContent = count === 0 ? 'A fresh start. Let’s make your first improvement.' : count === allTasks.length ? 'Your action plan is complete. Keep the regular habits going.' : `${count} improvement${count === 1 ? '' : 's'} made. Your next step is ready when you are.`;
    const next = allTasks.find(task => !done[task.id]);
    $('nextTitle').textContent = next ? next.title : 'You’ve worked through your plan';
    $('nextText').textContent = next ? next.next : 'Revisit reviews, updates and performance as your shop grows.';
    $('nextTask').hidden = !next;
    document.querySelector('[data-filter="todo"]').setAttribute('aria-label', `To do (${allTasks.length - count})`);
    document.querySelector('[data-filter="done"]').setAttribute('aria-label', `Done (${count})`);
  }
  function route() {
    const requested = location.hash.slice(1) || 'checklist';
    const view = ['checklist', 'profile', 'drafts', 'resources'].includes(requested) ? requested : 'checklist';
    document.querySelectorAll('.view').forEach(section => { section.hidden = section.id !== 'view-' + view; });
    document.querySelectorAll('[data-view]').forEach(link => { const active = link.dataset.view === view; link.classList.toggle('active', active); if (active) link.setAttribute('aria-current', 'page'); else link.removeAttribute('aria-current'); });
    window.scrollTo({top:0, behavior:'instant'});
  }
  async function copy(text, button) {
    try {
      if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(text); notify('Copied. Ready to paste into your profile.');
    } catch {
      const field = document.createElement('textarea'); field.value = text; field.style.cssText = 'position:fixed;left:0;top:0;width:1px;height:1px;opacity:0'; document.body.append(field); field.select();
      const copied = document.execCommand('copy'); field.remove();
      if (copied) { notify('Copied. Ready to paste into your profile.'); button?.focus(); }
      else {
        const selection = window.getSelection();
        const target = button?.closest('.panel, .service-draft')?.querySelector('textarea, .copy-block, p');
        if (target instanceof HTMLTextAreaElement) { target.focus(); target.select(); }
        else if (target && selection) { const range = document.createRange(); range.selectNodeContents(target); selection.removeAllRanges(); selection.addRange(range); }
        notify('Clipboard unavailable. Select the text and copy it manually.');
      }
    }
  }
  $('description').value = draft;
  const updateCharCount = () => { $('charCount').textContent = `${$('description').value.length} / 750 characters`; };
  $('description').addEventListener('input', () => { draft = $('description').value; updateCharCount(); save(); }); updateCharCount();
  $('copyDescription').addEventListener('click', event => { if (!draft.trim()) return notify('Add a description before copying.'); copy(draft, event.currentTarget); });
  services.forEach(([title, text]) => {
    const row = element('div', 'service-draft'), body = element('div'); body.append(element('h3', '', title), element('p', '', text));
    const button = element('button'); button.type = 'button'; button.setAttribute('aria-label', 'Copy ' + title); button.append(icon('copy')); button.addEventListener('click', () => copy(`${title}\n${text}`, button));
    row.append(body, button); $('serviceDrafts').append(row);
  });
  $('copyServices').addEventListener('click', event => copy(services.map(s => s.join('\n')).join('\n\n'), event.currentTarget));
  $('postDraft').textContent = post; $('reviewDraft').textContent = reviewRequest;
  $('copyPost').addEventListener('click', event => copy(post, event.currentTarget));
  $('copyReview').addEventListener('click', event => copy(reviewRequest, event.currentTarget));
  areas.forEach(area => $('serviceAreas').append(element('span', '', area)));
  Object.values(sources).forEach(([title, url]) => { const link = element('a', '', title); link.href = url; link.target = '_blank'; link.rel = 'noopener noreferrer'; link.append(icon('external')); $('sourceLinks').append(link); });
  document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => { filter = button.dataset.filter; document.querySelectorAll('[data-filter]').forEach(b => b.setAttribute('aria-pressed', String(b === button))); renderTasks(); }));
  $('nextTask').addEventListener('click', () => {
    const next = allTasks.find(task => !done[task.id]); if (!next) return;
    if (filter === 'done') { filter = 'all'; document.querySelectorAll('[data-filter]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.filter === 'all'))); renderTasks(); }
    const row = $('task-' + next.id), button = row.querySelector('.task-expand');
    if (button.getAttribute('aria-expanded') !== 'true') button.click();
    row.scrollIntoView({behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth', block:'center'}); button.focus({preventScroll:true});
  });
  $('reset').addEventListener('click', () => $('resetDialog').showModal());
  $('resetDialog').addEventListener('close', () => { if ($('resetDialog').returnValue === 'reset') { done = {}; save(); renderTasks(); updateProgress(); notify('Checklist reset. Your description draft is still saved.'); } });
  $('export').addEventListener('click', () => {
    const text = ['KEY MAKER & LOCKSMITH — GOOGLE BUSINESS PROFILE ACTION PLAN', 'Electronic City Phase 1, Bengaluru | +91 97623 06303', 'Verified editor/public snapshot: 21 October 2026; not a live feed.', '', ...groups.flatMap(group => [group.title.toUpperCase(), ...group.tasks.flatMap(task => [`${done[task.id] ? '[x]' : '[ ]'} ${task.title}`, `  Where: ${task.where}`, ...task.steps.map((step, i) => `  ${i + 1}. ${step}`), ...(task.note ? ['  Note: ' + task.note] : []), `  Guidance: ${sources[task.source][1]}`, ''])]), 'DESCRIPTION DRAFT', draft, '', 'SERVICE DRAFTS', services.map(s => s.join('\n')).join('\n\n'), '', 'SHOP UPDATE', post, '', 'REVIEW REQUEST', reviewRequest, '', 'ASSUMPTIONS', 'Shop visits and on-site locksmith work are based on supplied details. Specialist services, facilities, payment methods and all 20 areas were owner-confirmed. Prices remain unconfirmed. No ranking guarantee.'].join('\n');
    const url = URL.createObjectURL(new Blob([text], {type:'text/plain;charset=utf-8'}));
    const a = element('a'); a.href = url; a.download = 'keymaker-google-profile-checklist.txt'; document.body.append(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000); notify('Your checklist export is ready.');
  });
  window.addEventListener('hashchange', route);
  save(); renderTasks(); updateProgress(); route();
  if (!canSave) $('saveStatus').replaceChildren(icon('clock'), document.createTextNode('Progress kept for this session only'));
})();
