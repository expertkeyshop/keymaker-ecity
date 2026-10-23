from pathlib import Path
import json,re
r=Path(__file__).parent
shot='C:/Users/kbose/OneDrive/Desktop/keymaker/gbp-cover-logo-verified.png'
p=r/'business-content.json';b=json.loads(p.read_text(encoding='utf-8'))
b['execution']['photos']={'status':'Cover and logo verified','complete':True,'details':'Google Photos UI visually verified the actual storefront cover and proper gold/black Key Maker Locksmith logo on 22 October 2026.'}
b['cover_photo_status']={'status':'set_visually_verified','verified_at':'2026-10-22','source':'Google Photos UI visual verification','logo_verified':True,'logo_description':'Proper gold/black Key Maker Locksmith logo','screenshot':shot}
b['directory_listings']['status']='registration_in_progress'
platforms=b['directory_listings']['platforms']
platforms['Sulekha'].update(status='registration_in_progress',phone_verification='verified',selected_category='Key Maker & Locksmiths',business_name='Key Maker & Locksmith | Electronic City',selected_city='Bangalore',listing_created=False,submitted=False,captcha_authorized_by_owner=True,notes='Phone verified; category, full name and city selected. Registration/listing creation is still in progress; no public listing URL verified.')
platforms['Justdial'].update(status='otp_verification_pending',phone_verification='not_yet_verified',listing_created=False,submitted=False,terms_acceptance_authorized_by_owner=True,notes='OTP popup is still blank; actual verification has not been confirmed. Owner authorized Terms, Privacy and Infringement acceptance; no completed listing is claimed.')
b['execution']['consistency']={'status':'Free directory registration in progress','complete':False,'details':'Sulekha phone is verified and category/name/city are selected; registration continues. Justdial phone verification is still pending. Neither public directory listing is created or verified yet.'}
p.write_text(json.dumps(b,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
p=r/'DIRECTORY-LISTING-DRAFTS.json';d=json.loads(p.read_text(encoding='utf-8'));d['publication_status']='registration_in_progress';d['platforms']=platforms;d['listing_creation_status']='Neither public listing created or verified yet.';p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

p=r/'app.js';s=p.read_text(encoding='utf-8');m=re.search(r'  const execution = (\{[^\n]+\});',s);assert m;ex=json.loads(m.group(1))
ex['photos']={'status':'Cover and logo verified','summary':'Actual storefront cover and proper gold/black shop logo were visually verified in Google Photos.','steps':['Google Photos UI showed the actual storefront as the cover and a proper gold/black Key Maker Locksmith logo on 22 October 2026.','Evidence: gbp-cover-logo-verified.png in the keymaker workspace.','Six owner-authorized AI product illustrations are already uploaded separately. Continue adding useful real shop/work photos when available.'],'complete':True}
ex['consistency']['status']='Free directory registration in progress';ex['consistency']['summary']=b['execution']['consistency']['details']
ex['consistency']['steps']=['The owner authorized free Justdial and Sulekha listings and confirmed no existing directory listings.','Sulekha phone verification is complete; Key Maker & Locksmiths category, full business name and Bangalore city are selected. Registration remains in progress.','Justdial OTP popup is blank and actual phone verification is not confirmed. Owner authorized the current Terms, Privacy and Infringement acceptance.','Neither public listing is yet created or verified. Keep the directory task open until real status and listing URLs are available.']
s=s[:m.start(1)]+json.dumps(ex,ensure_ascii=False)+s[m.end(1):]
s=s.replace("const signboardConfirmationRevision = '2026-10-22-owner-full-signboard';","const signboardConfirmationRevision = '2026-10-22-owner-full-signboard';\n  const coverLogoRevision = '2026-10-22-cover-logo-verified';")
s=s.replace("savedSignboardConfirmationRevision = '';","savedSignboardConfirmationRevision = '', savedCoverLogoRevision = '';",1)
s=s.replace("savedSignboardConfirmationRevision = saved.signboardConfirmationRevision || '';","savedSignboardConfirmationRevision = saved.signboardConfirmationRevision || '';\n      savedCoverLogoRevision = saved.coverLogoRevision || '';",1)
s=s.replace('  function icon(name) {',"  if (savedCoverLogoRevision !== coverLogoRevision && execution.photos.complete) done.photos = true;\n  function icon(name) {",1)
s=s.replace('JSON.stringify({done, draft, executionRevision, productPublicationRevision, signboardConfirmationRevision})','JSON.stringify({done, draft, executionRevision, productPublicationRevision, signboardConfirmationRevision, coverLogoRevision})')
p.write_text(s,encoding='utf-8');assert sum(x['complete'] for x in ex.values())==16

p=r/'index.html';s=p.read_text(encoding='utf-8')
s=s.replace('id="navCount">3','id="navCount">2').replace('id="doneCount">15','id="doneCount">16').replace('15 items completed or reviewed. Three core profile follow-ups remain.','16 items completed or reviewed. Phone review and directory creation remain.').replace('aria-valuenow="15"','aria-valuenow="16"').replace('id="percent">83%','id="percent">89%').replace('15 checked. Three core profile follow-ups remain.','16 checked. Two core profile follow-ups remain.')
s=s.replace('<strong>Owner confirmed:</strong> the full signboard name matches Google, and the cover photo is set. <strong>Still open:</strong> phone visibility while Google review is pending (owner-reported); checking the logo; creating free Justdial and Sulekha listings. Directory drafts are ready locally, but no external directory listing has been created yet.','<strong>Verified:</strong> the full signboard name is owner-confirmed, and Google Photos visually shows the actual storefront cover and proper gold/black logo. <strong>Still open:</strong> phone visibility while Google review is pending (owner-reported), and free Justdial/Sulekha listing creation. Sulekha phone is verified and registration continues; Justdial phone verification is pending. Neither public listing is created or verified yet.')
p.write_text(s,encoding='utf-8')

p=r/'DIRECTORY-LISTING-DRAFTS.md';s=p.read_text(encoding='utf-8')
s=s.replace('**Created draft; neither Justdial nor Sulekha listing has been created or submitted.**','**Registration in progress; neither public listing is created or verified yet.**')
s=s.replace('| Justdial | Not started; draft only | Not created |','| Justdial | OTP verification pending; popup blank, verification not confirmed | Not created/verified |')
s=s.replace('| Sulekha | Not started; draft only | Not created |','| Sulekha | Phone verified; category/name/city selected, registration in progress | Not created/verified |')
s+='\nProgress checked 22 October: Sulekha phone verified, Key Maker & Locksmiths selected, full shop name and Bangalore city selected. Justdial OTP verification remains unconfirmed. Owner authorized the current Justdial Terms/Privacy/Infringement acceptance and Sulekha CAPTCHA; no completed listing or terms acceptance result is inferred from authorization alone.\n'
p.write_text(s,encoding='utf-8')

p=r/'GMB-EXECUTION.md';s=p.read_text(encoding='utf-8');a=s.index('## Current checklist:');z=s.index('## Links and assets',a);parts=['## Current checklist: 16 of 18 completed or reviewed','']
for k,v in ex.items():parts += [('✓' if v['complete'] else '−')+' **'+k.title()+': '+v['status']+'**',v['summary'],*['- '+x for x in v['steps']],'']
s=s[:a]+'\n'.join(parts)+s[z:]
s+='\n## Cover/logo verified and directory registration progress — 22 October 2026\n\nGoogle Photos UI visually verified the actual storefront cover and proper gold/black Key Maker Locksmith logo. Screenshot: `'+shot+'`. Photos task complete; checklist **16 of 18**.\n\nSulekha phone verification is complete; category Key Maker & Locksmiths, full shop name and Bangalore city are selected. Registration remains in progress. Justdial OTP popup remains blank and actual verification is not confirmed. No public Justdial or Sulekha listing is created or verified yet. The owner authorized the current Justdial Terms/Privacy/Infringement acceptance and Sulekha CAPTCHA. Existing products and Offer states remain unchanged.\n'
p.write_text(s,encoding='utf-8')
p=r/'README.md';s=p.read_text(encoding='utf-8');s=s.replace('with 15 checked','with 16 checked');s+='\nLatest 22 October update: actual cover and proper gold/black logo verified in Google Photos; checklist16/18. Sulekha phone verified with registration ongoing; Justdial verification pending. Neither public directory listing is created/verified yet.\n';p.write_text(s,encoding='utf-8')
for f in ['business-content.json','DIRECTORY-LISTING-DRAFTS.json','PUBLISHING-QUEUE.json']:json.loads((r/f).read_text(encoding='utf-8'))
print('16/18. Cover+logo verified; directory task open. Sulekha phone verified; Justdial verification pending; no listing created. Three JSONs valid.')
