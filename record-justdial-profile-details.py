from pathlib import Path
import json,re
r=Path(__file__).parent
proof='C:/Users/kbose/OneDrive/Desktop/keymaker/justdial-profile-details-saved.png'
site='https://keymaker-electronic-city.violetflame16.chatgpt.site/'
p=r/'business-content.json';b=json.loads(p.read_text(encoding='utf-8'));platforms=b['directory_listings']['platforms']
for platform in platforms.values():
 platform['registration_created']=True;platform['registration_completed']=True;platform['draft_status']='submitted_registered';platform['account_created']=None;platform['public_listing_verified']=False;platform['public_url']=None;platform['listing_url']=None
 platform.pop('listing_created',None)
 platform['account_note']='Business registration confirmed. Separate new account-creation event is not independently verified; account_created is unknown, not false.'
jd=platforms['Justdial']
jd.update(website=site,website_saved_verified=True,website_verification={'source':'Rendered Justdial Business Profile DOM','value':site,'verified_at':'2026-10-22','screenshot':proof},established_month=10,established_year=2026,establishment_saved_verified=True,establishment_readback='Oct - 2026',establishment_verification={'source':'Rendered Justdial Business Profile readback','verified_at':'2026-10-22','screenshot':proof},on_site_services={'selected':True,'save_clicked':True,'readback_verified':False,'status':'saved_awaiting_readback'},profile_details_screenshot=proof)
jd['notes']='Registration confirmed. Saved website and establishment readbacks verified. On Site Services was selected and Save clicked, but rendered readback is not yet verified. Owner dashboard URL is not a verified public URL; public address/link checks remain open.'
b['directory_listings']['platforms']=platforms
details='Both registrations confirmed. Justdial website and Oct-2026 establishment are saved and readback-verified; On Site Services save awaits readback. Public directory URLs and final address checks remain pending. Sulekha profile/SMS link is still preparing.'
b['execution']['consistency']={'status':'Registered; public checks pending','complete':False,'details':details}
p.write_text(json.dumps(b,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
p=r/'DIRECTORY-LISTING-DRAFTS.json';d=json.loads(p.read_text(encoding='utf-8'));d['platforms']=platforms;d['listing_creation_status']=details;d['draft_status']='submitted_registered';p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

p=r/'app.js';s=p.read_text(encoding='utf-8');m=re.search(r'  const execution = (\{[^\n]+\});',s);assert m;ex=json.loads(m.group(1));ex['consistency']['status']='Registered; public checks pending';ex['consistency']['summary']=details
ex['consistency']['steps']=['Justdial registration is confirmed. Its rendered Business Profile showed the exact shop website and establishment readback Oct - 2026 after saving.','Justdial On Site Services was checked and Save clicked, but its saved readback is not yet verified. Do not treat the setting as confirmed until checked.','Sulekha registration is confirmed; its profile page/SMS link remains in preparation.','Keep the directory task open until actual public URLs, public profile availability and address consistency are verified. Both registrations exist; owner-dashboard and thank-you URLs are not public listing URLs.']
s=s[:m.start(1)]+json.dumps(ex,ensure_ascii=False)+s[m.end(1):];p.write_text(s,encoding='utf-8');assert sum(x['complete'] for x in ex.values())==16

p=r/'DIRECTORY-LISTING-DRAFTS.md';s=p.read_text(encoding='utf-8');s+='\n## Saved Justdial profile details verified — 22 October 2026\n\n- Rendered Business Profile DOM showed the saved website: '+site+'\n- Establishment readback explicitly showed **Oct - 2026**. Only month/year is verified in Justdial; the owner-confirmed actual opening date remains 1 October 2026.\n- Proof: `'+proof+'`.\n- On Site Services was checked and Save clicked. Status: saved_awaiting_readback; do not mark the setting readback-verified yet.\n- Both business registrations are created/completed. A separate new account-creation event is not independently verified, so account_created is unknown.\n- Both public_listing_verified flags remain false and public_url/listing_url remain null until actual public URLs and public checks are available.\n\nChecklist remains16/18; free-directory task is still open.\n';p.write_text(s,encoding='utf-8')
p=r/'GMB-EXECUTION.md';s=p.read_text(encoding='utf-8');a=s.index('## Current checklist:');z=s.index('## Links and assets',a);parts=['## Current checklist: 16 of 18 completed or reviewed','']
for k,v in ex.items():parts += [('✓' if v['complete'] else '−')+' **'+k.title()+': '+v['status']+'**',v['summary'],*['- '+t for t in v['steps']],'']
s=s[:a]+'\n'.join(parts)+s[z:]
s+='\n## Justdial website and establishment saved/read back — 22 October 2026\n\nThe rendered Business Profile showed '+site+' and establishment **Oct - 2026**. Proof: `'+proof+'`. On Site Services was checked and Save clicked, but readback remains pending. Both registrations are confirmed; separate account-creation events are unknown, and public listing URLs/verification remain absent. These conservative record flags replace stale draft-only booleans. No public directory completion is claimed; checklist stays16/18.\n';p.write_text(s,encoding='utf-8')
p=r/'index.html';s=p.read_text(encoding='utf-8');s=s.replace('Justdial’s free owner profile is available; its public URL and final address consistency remain to be checked.','Justdial’s free owner profile is available, with website and Oct-2026 establishment saved/readback-verified. Its public URL and final address consistency remain to be checked.');p.write_text(s,encoding='utf-8')
p=r/'README.md';s=p.read_text(encoding='utf-8');s+='\nJustdial saved website and Oct - 2026 establishment were readback-verified. On Site Services save awaits readback. Both registrations are created, separate account-created state is unknown, and public URLs/verification remain pending. Checklist16/18.\n';p.write_text(s,encoding='utf-8')
for f in ['business-content.json','DIRECTORY-LISTING-DRAFTS.json','PUBLISHING-QUEUE.json']:json.loads((r/f).read_text(encoding='utf-8'))
print('JD website+Oct2026 verified; onsite save unverified; registrations true/public URLs null.16/18;3JSONvalid.')
