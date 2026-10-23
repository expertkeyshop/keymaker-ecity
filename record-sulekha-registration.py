from pathlib import Path
import json,re
r=Path(__file__).parent
shot='C:/Users/kbose/OneDrive/Desktop/keymaker/sulekha-registered-confirmation.png'
p=r/'business-content.json';b=json.loads(p.read_text(encoding='utf-8'));platforms=b['directory_listings']['platforms']
platforms['Sulekha'].update(status='registered_profile_preparing',registration_completed=True,phone_verification='verified',submitted=True,public_listing_verified=False,listing_url=None,profile_status='preparing_link_to_be_sent_by_SMS',selected_category='Key Maker & Locksmiths',selected_city='Bangalore',selected_area='Electronic City Phase I',screenshot=shot,confirmation_page='https://www.sulekha.com/list-your-business#thankyou',confirmation_text='Your business is registered. Your profile page is being prepared; the link will be sent by text shortly.',notes='Registration confirmed by thank-you UI. Public profile is still being prepared; no public listing URL is known or verified yet.')
platforms['Justdial'].update(status='business_address_form_in_progress',phone_verification='verified',registration_completed=False,submitted=False,public_listing_verified=False,listing_url=None,notes='Phone verification is complete. Business address form is being filled; no completed registration or public listing is claimed yet.')
b['directory_listings'].update(status='partially_registered',draft_status='partially_submitted',platforms=platforms)
details='Sulekha registration confirmed; profile page is being prepared and its public URL is not yet known. Justdial phone verified, business-address form in progress. Directory task remains open.'
b['execution']['consistency']={'status':'Sulekha registered; Justdial in progress','complete':False,'details':details}
p.write_text(json.dumps(b,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
p=r/'DIRECTORY-LISTING-DRAFTS.json';d=json.loads(p.read_text(encoding='utf-8'));d.update(publication_status='partially_registered',draft_status='partially_submitted',platforms=platforms,listing_creation_status=details);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

p=r/'app.js';s=p.read_text(encoding='utf-8');m=re.search(r'  const execution = (\{[^\n]+\});',s);assert m;ex=json.loads(m.group(1));ex['consistency']['status']='Sulekha registered; Justdial in progress';ex['consistency']['summary']=details
ex['consistency']['steps']=['Sulekha thank-you page confirms the business is registered. Its public profile page is being prepared and the link will be sent by SMS; no public URL is yet known.','Sulekha details: Key Maker & Locksmiths; Bangalore; Electronic City Phase I; full shop name; business phone verified.','Justdial phone verification is now complete. The business address form is in progress; submission and public listing have not yet been confirmed.','Keep this task open until Justdial submission and both directory public-link/status checks are clear. Do not create duplicate Sulekha registrations.']
s=s[:m.start(1)]+json.dumps(ex,ensure_ascii=False)+s[m.end(1):];p.write_text(s,encoding='utf-8')

p=r/'index.html';s=p.read_text(encoding='utf-8');s=s.replace('Sulekha phone is verified and registration continues; Justdial phone verification is pending. Neither public listing is created or verified yet.','Sulekha registration is confirmed and its profile page is being prepared; no public URL is known yet. Justdial phone is verified and its business-address form is in progress. Directory completion remains open.');p.write_text(s,encoding='utf-8')

p=r/'DIRECTORY-LISTING-DRAFTS.md';s=p.read_text(encoding='utf-8')
s=s.replace('**Registration in progress; neither public listing is created or verified yet.**','**Sulekha registered, profile preparing; Justdial phone verified and business-address form in progress. Public links/status checks remain open.**')
s=s.replace('| Justdial | OTP verification pending; popup blank, verification not confirmed | Not created/verified |','| Justdial | Phone verified; business-address form in progress, not submitted | Not known/verified |')
s=s.replace('| Sulekha | Phone verified; category/name/city selected, registration in progress | Not created/verified |','| Sulekha | Registered; public profile page preparing, SMS link pending | Not yet known |')
s+='\n## Confirmed registration progress — 22 October 2026\n\nSulekha showed the thank-you confirmation at https://www.sulekha.com/list-your-business#thankyou: the business is registered, its profile page is being prepared, and a link will be sent by text. Confirmed category Key Maker & Locksmiths, city Bangalore, area Electronic City Phase I, full business name and verified phone 9762306303. Status: registered_profile_preparing. No public listing URL is known yet. Screenshot: `'+shot+'`.\n\nJustdial phone verification is complete; its business address form remains in progress. Directory task is not complete and no Justdial submission/public listing is claimed yet.\n'
p.write_text(s,encoding='utf-8')

p=r/'GMB-EXECUTION.md';s=p.read_text(encoding='utf-8');a=s.index('## Current checklist:');z=s.index('## Links and assets',a);parts=['## Current checklist: 16 of 18 completed or reviewed','']
for k,v in ex.items():parts += [('✓' if v['complete'] else '−')+' **'+k.title()+': '+v['status']+'**',v['summary'],*['- '+t for t in v['steps']],'']
s=s[:a]+'\n'.join(parts)+s[z:]
s+='\n## Sulekha registration confirmed; Justdial address step — 22 October 2026\n\n'+details+' Sulekha UI said the business is registered and its profile page is being prepared, with a link to follow by text. Category Key Maker & Locksmiths; Bangalore; Electronic City Phase I; full business name and phone verified. Screenshot: `'+shot+'`. Sulekha status registered_profile_preparing; no public URL known yet. Justdial phone verified, business-address form in progress. Checklist remains16/18; directory task is not marked complete.\n';p.write_text(s,encoding='utf-8')
p=r/'README.md';s=p.read_text(encoding='utf-8');s+='\nLatest directory state: Sulekha registered_profile_preparing (thank-you UI confirmed), public link pending by SMS. Justdial phone verified, address form in progress. Directory task stays open; checklist16/18.\n';p.write_text(s,encoding='utf-8')
for f in ['business-content.json','DIRECTORY-LISTING-DRAFTS.json','PUBLISHING-QUEUE.json']:json.loads((r/f).read_text(encoding='utf-8'))
assert sum(v['complete'] for v in ex.values())==16
print('Sulekha registered_profile_preparing; Justdial address form in progress. No public URLs invented.16/18; threeJSONvalid.')
