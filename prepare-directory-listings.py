from pathlib import Path
import json,re,ast
r=Path(__file__).parent
p=r/'business-content.json';business=json.loads(p.read_text(encoding='utf-8'))
app=(r/'app.js').read_text(encoding='utf-8')
areas=ast.literal_eval(re.search(r'  const areas = (\[[^\n]+\]);',app).group(1))
name='Key Maker & Locksmith | Electronic City'
directory_description='Key Maker & Locksmith | Electronic City is a 24-hour key making and locksmith shop on Gollahalli Main Road, Siraj Layout, Electronic City Phase 1, Bengaluru. We duplicate keys for homes, offices and shops, make keys for compatible cars and bikes, and provide lock repair, lock replacement and lockout assistance. We also offer compatible car chip and remote programming, key fobs, remote shell replacement, rekeying, safe opening and window-lock work. Visit the shop or ask about on-site service across our listed areas. Contact us with your key, lock or vehicle details and exact location to confirm compatibility, availability and a quote. Cash, UPI, IMPS and NEFT are accepted.'
draft={
 'prepared_at':'2026-10-22','publication_status':'not_started','draft_status':'created_draft_not_submitted',
 'owner_authorization':'Create free Justdial and Sulekha business listings. No existing directory listings, as confirmed by owner on 22 October 2026.',
 'business_name':name,'phone_country_code':'+91','phone_number':'9762306303','phone_display':'+91 97623 06303','whatsapp':'https://wa.me/919762306303',
 'website':business['website'],'address':business['address'],'street':'Gollahalli Main Road','layout':'Siraj Layout','locality':'Electronic City Phase 1','city':'Bengaluru','state':'Karnataka','postcode':'560100','country':'India',
 'google_maps':'https://www.google.com/maps?cid=6777548479080557010','opening_date':'2026-10-01','hours':'Open 24 hours, Monday to Sunday',
 'hours_by_day':{day:'Open 24 hours' for day in ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']},
 'suggested_primary_category':'Locksmith','suggested_additional_category':'Key duplication service','category_note':'Select only accurate categories actually offered by each directory; category labels here are draft suggestions.',
 'business_description':directory_description,'short_description':'24-hour key duplication and locksmith services in Electronic City Phase 1, Bengaluru. Shop visits and on-site help for supported keys, locks and vehicles.',
 'services':[x['name'] for x in business['services']],'service_areas':areas,'coverage_note':'Owner confirmed all 20 listed areas and call-outs 10 km or more away. Confirm availability and travel charges for the exact address.',
 'payments':['Cash','UPI','IMPS bank transfer','NEFT bank transfer'],'cards_accepted':False,
 'business_email':None,'owner_legal_name':None,'gstin':None,'tax_registration':None,'year_established':'2026',
 'missing_data_note':'Do not invent an email, owner/legal name, GSTIN, tax registration, certifications or landmarks. Collect any mandatory missing field from the owner or allow owner completion.',
 'platforms':{
  'Justdial':{'status':'not_started','draft_status':'created_draft_not_submitted','listing_url':None,'account_created':False,'submitted':False,'paid_plan_authorized':False,'notes':'Free listing only. Inspect live categories/fields and check for a matching listing before creating a duplicate.'},
  'Sulekha':{'status':'not_started','draft_status':'created_draft_not_submitted','listing_url':None,'account_created':False,'submitted':False,'paid_plan_authorized':False,'notes':'Free listing only. Inspect live categories/fields and check for a matching listing before creating a duplicate.'}
 }
}
(r/'DIRECTORY-LISTING-DRAFTS.json').write_text(json.dumps(draft,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
md=['# Free directory listing drafts','','Prepared 22 October 2026. **Created draft; neither Justdial nor Sulekha listing has been created or submitted.** The owner confirmed no existing directory listings and authorized free listings on these two services.','','## Shared business details','',f'- Exact name: {name}.',f'- Phone: {draft["phone_display"]}.',f'- WhatsApp: {draft["whatsapp"]}.',f'- Website: {draft["website"]}.',f'- Address: {draft["address"]}.','- Open 24 hours every day, Monday–Sunday.','- Opening date: 1 October 2026. Established year: 2026.','- Category suggestions: Locksmith; Key duplication service. Choose the closest accurate labels offered in each live directory.','- Service options: shop visits and on-site work.','- Payments: cash, UPI, IMPS and NEFT. No cards.','','## Description ready to paste','',directory_description,'','## Short description','',draft['short_description'],'','## Confirmed services','',*['- '+s for s in draft['services']],'','## Confirmed service areas','',*['- '+a for a in areas],'',draft['coverage_note'],'','## Platform status','','| Platform | Status | Public listing URL |','|---|---|---|','| Justdial | Not started; draft only | Not created |','| Sulekha | Not started; draft only | Not created |','','Free listings only. No paid plan, subscription or advertising purchase is authorized by this draft. Inspect each platform’s current listing flow and mandatory fields. Never claim a listing exists until it has actually been created and its status verified.','','## Missing fields to obtain only if mandatory','','Business email, owner/legal name, GSTIN and tax-registration information were not supplied. Leave them blank where optional; do not invent them. Avoid invented certifications, warranties, response times or landmarks. Do not copy the reference shop’s address or branding.','','Use the business phone for the listing; any verification prompt can be completed by the owner as required. The business has no supplied directory login credentials.','','Detailed structured copy: `DIRECTORY-LISTING-DRAFTS.json`.']
(r/'DIRECTORY-LISTING-DRAFTS.md').write_text('\n'.join(md)+'\n',encoding='utf-8')

updates={
 'name':{'status':'Owner-confirmed signboard match','complete':True,'details':'On 22 October 2026 the owner confirmed the full permanent shop name is Key Maker & Locksmith | Electronic City, matching the public Google name.'},
 'contact':{'status':'Awaiting Google review — owner reported','complete':False,'details':'The phone is saved, but public display remains pending. On 22 October the owner reported that Google review is pending. Wait for Google’s decision and recheck visibility; do not repeatedly resubmit the number.'},
 'photos':{'status':'Cover owner-confirmed; logo unverified','complete':False,'details':'The owner said the cover photo is set on 22 October. Logo selection remains unverified; do not mark the full photo/logo task complete until checked. Product AI illustrations are already uploaded separately.'},
 'consistency':{'status':'Free Justdial and Sulekha drafts ready','complete':False,'details':'The owner confirmed no existing directory listings and requested free Justdial and Sulekha listings. Drafts are created locally; neither external listing is created or submitted yet.'}
}
for k,v in updates.items():business['execution'][k]=v
business['owner_signboard_confirmation']={'confirmed_at':'2026-10-22','full_name':name,'matches_full_google_name':True}
business['phone_review_status']={'status':'awaiting_google_review','source':'owner report','reported_at':'2026-10-22','public_visibility_still_pending':True}
business['cover_photo_status']={'status':'set_owner_confirmed','reported_at':'2026-10-22','source':'owner report','logo_verified':False}
business['directory_listings']={'status':'not_started','draft_status':'created_draft_not_submitted','owner_reports_no_existing_listings':True,'authorized_platforms':['Justdial','Sulekha'],'free_only':True,'draft_file':'DIRECTORY-LISTING-DRAFTS.json','platforms':draft['platforms']}
p.write_text(json.dumps(business,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

m=re.search(r'  const execution = (\{[^\n]+\});',app);assert m;ex=json.loads(m.group(1))
for k,v in updates.items():
 ex[k]['status']=v['status'];ex[k]['complete']=v['complete'];ex[k]['summary']=v['details']
ex['name']['steps']=['Owner confirmed on 22 October that the full permanent signboard name is Key Maker & Locksmith | Electronic City.','The same name appears publicly on the Google profile.','Keep the same real-world name on the new directory listings.']
ex['contact']['steps']=['Phone +91 97623 06303 is saved; the “Don’t show” switch was already checked off.','The owner reports pending Google review on 22 October. This is owner-reported status, not a fresh independent approval decision.','Wait for the review result and check the public phone button. Avoid repeated edits while review is pending.']
ex['photos']['steps']=['The owner confirmed that the cover photo is set. Do not ask for it again without a concrete issue.','Inspect the logo slot before marking the whole photo/logo task complete; the logo has not been confirmed yet.','Six AI product illustrations are already uploaded and all products are live; storefront and logo imagery are separate.']
ex['consistency']['steps']=['The owner confirmed no existing directory listings and authorized free Justdial and Sulekha listings.','Shared business details, descriptions, all services and all 20 areas are in DIRECTORY-LISTING-DRAFTS.md and .json.','Neither listing has been created or submitted yet. Use only free options, avoid duplicates, and record the actual listing URL/status.','No business email, owner/legal name, GSTIN or tax details were supplied. Leave optional fields blank; do not invent missing facts.']
app=app[:m.start(1)]+json.dumps(ex,ensure_ascii=False)+app[m.end(1):]
app=app.replace("title: 'Keep your details consistent elsewhere'","title: 'Create free Justdial and Sulekha listings'")
app=app.replace("where: 'Your existing directory and social profiles'","where: 'Justdial and Sulekha free-listing forms'")
app=app.replace("const productPublicationRevision = '2026-10-22-six-products';","const productPublicationRevision = '2026-10-22-six-products';\n  const signboardConfirmationRevision = '2026-10-22-owner-full-signboard';")
app=app.replace("savedProductPublicationRevision = '';","savedProductPublicationRevision = '', savedSignboardConfirmationRevision = '';",1)
app=app.replace("savedProductPublicationRevision = saved.productPublicationRevision || '';","savedProductPublicationRevision = saved.productPublicationRevision || '';\n      savedSignboardConfirmationRevision = saved.signboardConfirmationRevision || '';",1)
app=app.replace('  function icon(name) {',"  if (savedSignboardConfirmationRevision !== signboardConfirmationRevision && execution.name.complete) done.name = true;\n  function icon(name) {",1)
app=app.replace('JSON.stringify({done, draft, executionRevision, productPublicationRevision})','JSON.stringify({done, draft, executionRevision, productPublicationRevision, signboardConfirmationRevision})')
(r/'app.js').write_text(app,encoding='utf-8')
assert sum(x['complete'] for x in ex.values())==15

p=r/'index.html';s=p.read_text(encoding='utf-8')
s=s.replace('id="navCount">4','id="navCount">3').replace('id="doneCount">14','id="doneCount">15').replace('14 items completed or reviewed. Four core profile follow-ups remain.','15 items completed or reviewed. Three core profile follow-ups remain.').replace('aria-valuenow="14"','aria-valuenow="15"').replace('id="percent">78%','id="percent">83%').replace('14 checked. Four core profile follow-ups remain.','15 checked. Three core profile follow-ups remain.')
s=s.replace('<strong>Still open:</strong> public phone visibility; matching the chosen full name to your physical branding; a cover photo and correct logo; existing directory listings. Separately, all six products are live, and the offer expiry time still needs a manual check.','<strong>Owner confirmed:</strong> the full signboard name matches Google, and the cover photo is set. <strong>Still open:</strong> phone visibility while Google review is pending (owner-reported); checking the logo; creating free Justdial and Sulekha listings. Directory drafts are ready locally, but no external directory listing has been created yet. All six products are live; the offer expiry control still needs a manual check.')
s=s.replace('Detailed execution record</a></p></section>','Detailed execution record</a> · <a href="DIRECTORY-LISTING-DRAFTS.md">Free directory drafts</a></p></section>',1)
p.write_text(s,encoding='utf-8')

p=r/'GMB-EXECUTION.md';s=p.read_text(encoding='utf-8');s=s.replace('## Current checklist: 14 of 18 completed or reviewed','## Current checklist: 15 of 18 completed or reviewed')
if '## Latest owner confirmations and directory drafts' not in s:
 s+='\n## Latest owner confirmations and directory drafts — 22 October 2026\n\nChecklist: **15 of 18** completed or reviewed.\n\n- Name: complete. The owner confirmed the full permanent signboard name is Key Maker & Locksmith | Electronic City, matching the public profile.\n- Phone: Awaiting Google review, as reported by the owner. The phone is saved but public visibility remains pending. Do not repeatedly edit it during review.\n- Cover: set, confirmed by owner. Logo selection is not yet verified, so the broader photo/logo task remains open. Product illustrations are already uploaded separately.\n- Directories: the owner confirmed no existing directory listings and requested free Justdial and Sulekha listings. DIRECTORY-LISTING-DRAFTS.md and .json contain exact known business details, descriptions, services, payments and all 20 areas. Status: not_started / created_draft_not_submitted. Neither external listing has been created or submitted.\n\nNo email, owner/legal name, GSTIN or tax-registration details were invented. No paid directory package or account was created. Existing six live products and Offer states are unchanged. Earlier requests for existing directory links or signboard confirmation are superseded by these owner answers.\n'
p.write_text(s,encoding='utf-8')
p=r/'README.md';s=p.read_text(encoding='utf-8');s=s.replace('with 14 checked','with 15 checked');s+='\nOn 22 October the owner confirmed the full signboard name and set cover photo; phone review is pending according to the owner. Logo remains unverified. Free Justdial/Sulekha listing drafts are in DIRECTORY-LISTING-DRAFTS.md and .json; no external listing has been created yet.\n';p.write_text(s,encoding='utf-8')
for f in ['business-content.json','DIRECTORY-LISTING-DRAFTS.json','PUBLISHING-QUEUE.json']:json.loads((r/f).read_text(encoding='utf-8'))
print('15/18 checked. Directory drafts only; Justdial/Sulekha both not_started. Three JSON files parsed. Product and Offer states preserved.')
