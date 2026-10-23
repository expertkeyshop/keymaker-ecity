from pathlib import Path
import json,re
root=Path(__file__).parent
exact='Computerised/dimple key for compatible locks. Match the key profile with your original key or lock. Indicative price; confirm the exact key type and cutting requirements before ordering. Representative AI-generated illustration; actual key design may differ.'
shot='C:/Users/kbose/.codex/visualizations/2026/10/21/01a15ed4-019d-7e73-811d-563248a44e98/gbp-six-products-manager.png'
publicshot='C:/Users/kbose/.codex/visualizations/2026/10/21/01a15ed4-019d-7e73-811d-563248a44e98/gbp-products-live.png'
summary='All six product names/prices were verified in the public Google catalogue. Five remain live; the previously public key listing now has a corrected title/description edit Pending Google review. No duplicate product was created.'
for file in ['PUBLISHING-QUEUE.json','service-product-drafts.json','business-content.json']:
    p=root/file;d=json.loads(p.read_text(encoding='utf-8'));items=d.get('products',d.get('product_drafts',[]))
    for i,x in enumerate(items):
        x['status']='previously_public_edit_pending' if i==0 else 'publicly_visible'
        x['visibility_verified']='All six names/prices verified publicly on 22 October 2026; first item now has a subsequent Pending content edit.' if i==0 else 'Name and INR price verified in the public Google Products catalogue and owner product manager on 22 October 2026.'
        x['catalogue_screenshot']=publicshot;x['manager_screenshot']=shot
        if i==0:
            x['previous_public_name']='Computerised key blank'
            x['name']='Computerised key';x['description']=exact;x['description_with_image_disclosure']=exact
            x['product_uuid']='8b6e11a4-2174-4d9e-95e7-81612fa0f5fb';x['public_product_id']='8210459654379117113'
            x['pending_content_correction']='Corrected title and exact description were saved in the same product. Google product manager shows Pending; the former public title may remain until approval.'
            x['disclosure_publication_status']='exact_corrected_description_saved_pending_review'
            x['editor_note']='Same product edited and saved, not duplicated. Corrected title Computerised key and representative-image disclosure are Pending Google review.'
            x['form_state']='Edit saved; Pending Google review.'
        else:
            x['description_record_note']='This file retains the queued reference body. Submitted copy was concise and included: Representative AI-generated illustration; actual design may differ. Exact full body was not independently transcribed from the catalogue.'
            x['editor_note']='Public name/price and owner-manager presence verified; no Pending label observed on this item.'
    d['products_status']='five_public_one_previously_public_edit_pending'
    d['products_published_count']=6;d['products_submitted_count']=6
    d['products_publicly_visible_verified_count']=5;d['products_previously_public_pending_edit_count']=1;d['initial_public_catalogue_verified_count']=6
    d['products_pending_reason']=summary
    if file=='PUBLISHING-QUEUE.json':
        d['publication_status']='published_with_key_edit_pending'
        d['publication_note']=summary+' All new Updates and SPARE10 Offer are Published; expiry-control readback needs a manual check.'
    if file=='service-product-drafts.json':d['product_pricing_status']='Six owner-authorized generic prices were published and verified: INR250,650,700,950,2300,1500. Owner will update prices. Corrected key title/description is Pending review.'
    if file=='business-content.json':
        d['products_published']=True
        d['execution']['products']={'status':'Published; corrected key edit Pending','complete':True,'details':summary}
        d['publishing_queue'].update(products_status=d['products_status'],products_published_count=6,products_submitted_count=6,products_publicly_visible_verified_count=5,products_previously_public_pending_edit_count=1)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

p=root/'product-images/manifest.json';d=json.loads(p.read_text(encoding='utf-8'))
for i,a in enumerate(d['assets']):a['publication_status']='previously_public_edit_pending' if i==0 else 'publicly_visible';a['manager_screenshot']=shot
d['assets'][0]['current_product_name']='Computerised key';d['assets'][0]['observed_correction_note']='The generic illustration depicts a cut/dimple key, so the product was corrected from Computerised key blank to Computerised key. The same product edit is saved and Pending Google review.';d['assets'][0]['corrected_description_pending_review']=exact
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

p=root/'PUBLISHING-QUEUE.md';s=p.read_text(encoding='utf-8')
s=re.sub(r'- \*\*Products: publication_in_progress;.*?(?=\n- Both further Updates)', '- **Products: six added and initially verified publicly.** Five remain live; the first key listing has a saved corrected title/description Pending Google review. Its former public name may remain until approved. Same product, no duplicate.\n',s,flags=re.S)
s=s.replace('six products are being prepared/submitted with AI representative illustrations.','all six products were added with AI representative illustrations; the corrected key edit is Pending review.')
s=s.replace('### Computerised key blank — reference ₹250','### Computerised key — reference ₹250 (corrected edit Pending)')
s=s.replace('Key blank for compatible computerised locks. Match the key profile with your existing key or lock. Indicative price; confirm the suitable blank and whether cutting is included before purchase.',exact)
s=s.replace('The first item currently says Computerised key blank, while its generated illustration depicts a generic cut/dimple key. A title correction to Computerised key and disclosure save remain to be verified; do not claim those edits are live yet.','The first key was corrected in the same product to Computerised key, with the exact description above and representative-image disclosure. The product manager shows Pending. UUID `8b6e11a4-2174-4d9e-95e7-81612fa0f5fb`; public product ID `8210459654379117113`. The former public title may remain until review completes.\n\nAll six names/prices were initially verified in the public catalogue. The other five are live without a Pending label. Screenshots: `'+publicshot+'` and `'+shot+'`.')
s=s.replace('Use the prepared AI representative assets with the image disclosure, then submit/verify products individually; distinguish published, pending and rejected states.','All six were added and initially verified publicly. Recheck the first corrected product edit after Google review; do not create duplicates.')
p.write_text(s,encoding='utf-8')

p=root/'SERVICES-AND-PRODUCTS.md';s=p.read_text(encoding='utf-8');a=s.index('## Six physical-product drafts');b=s.index('## Corrections and safeguards',a)
queue=json.loads((root/'PUBLISHING-QUEUE.json').read_text(encoding='utf-8'))
part=['## Six physical products added', '', summary, '', 'The owner authorized these generic prices and will update them. Product images are AI-generated representatives, not photos of actual shop stock. Prompts and assets are recorded in `product-images/manifest.json`.', '', 'Public catalogue screenshot: `'+publicshot+'`. Owner manager screenshot: `'+shot+'`.', '']
for i,x in enumerate(queue['products']):
    part += ['### '+x['name']+' — ₹'+str(x['requested_generic_price_inr']), '', 'Category: '+x['category'], '', 'Status: '+x['status']+'.', '', ('Exact saved description; Pending Google review:' if i==0 else 'Queued reference description; submitted copy was concise and included the representative-image disclosure:'), '', x['description'], '']
    if i>0:part += ['Submitted disclosure: Representative AI-generated illustration; actual design may differ. The exact full submitted body is not independently transcribed here.', '']
s=s[:a]+'\n'.join(part)+s[b:]
p.write_text(s,encoding='utf-8')

p=root/'GMB-EXECUTION.md';s=p.read_text(encoding='utf-8')
s=re.sub(r'## Current checklist: 13 of (?:17|18) completed or reviewed','## Current checklist: 14 of 18 completed or reviewed',s)
if '## All six products added and catalogue verified' not in s:
    s+='\n## All six products added and catalogue verified — 22 October 2026\n\n'+summary+'\n\n- Computerised key: ₹250. Same item originally published as Computerised key blank; saved correction is Pending review.\n- Car remote key body and shell: ₹650, live.\n- Cylinder lock handle: ₹700, live.\n- Door lock cylinder: ₹950, live.\n- Main door lock: ₹2,300, live.\n- Car remote key unit: ₹1,500, live.\n\nThe initial six names/prices were verified publicly; the owner manager subsequently showed all six entries, with only the corrected key marked Pending. Key UUID `8b6e11a4-2174-4d9e-95e7-81612fa0f5fb`, public product ID `8210459654379117113`. Its exact saved revised description is: '+exact+'\n\nFor products 2–6, the submitted concise descriptions included “Representative AI-generated illustration; actual design may differ.” Local queued reference bodies are retained and labelled as such, rather than claiming a full exact readback. Owner-authorized generic prices can be changed later. No real-product-photo upload is required from the owner for this completed generic-image workflow.\n\nScreenshots: `'+publicshot+'` and `'+shot+'`. Checklist: 14 of 18 checked; four core profile follow-ups remain (phone visibility, real-world branding match, shop cover/logo, existing directories). The first key edit and offer expiry-control readback also need follow-up. A historical opening announcement is Published as an Update; a future Event would need real future event dates.\n'
p.write_text(s,encoding='utf-8')

p=root/'app.js';s=p.read_text(encoding='utf-8');m=re.search(r'  const execution = (\{[^\n]+\});',s);assert m
d=json.loads(m.group(1));d['products']={'status':'Six products added; key edit Pending','summary':'Six listings were verified publicly. Five remain live; the corrected key title/description awaits Google review.','steps':['All six generic prices were verified in the public catalogue: key ₹250; remote shell ₹650; handle ₹700; cylinder ₹950; main door lock ₹2,300; remote unit ₹1,500.','The first key was corrected in the same listing to Computerised key with a representative-image description. The edit is saved and Pending; its former public title may remain until approved.','The six images are owner-authorized AI representative illustrations, not photographs of actual stock. You can update prices later. No more product images are needed for this completed workflow.','All new Updates and the approved SPARE10 Offer are Published. The offer end-time control still needs a manual check: terms say 23:59 but readback shows 11:59 without AM/PM.'],'complete':True}
d['photos']['steps'][2]='Add useful shop interior, machine and work images as needed. No new storefront or logo photo was uploaded; the product illustrations are separate.'
d['posts']['steps'][3]='The latest two service Updates and opening Update have no CTA. All six products were added; one corrected key edit awaits Google review. Do not duplicate the published posts.'
s=s[:m.start(1)]+json.dumps(d,ensure_ascii=False)+s[m.end(1):]
s=s.replace("const executionRevision = '2026-10-21-final-v2';","const executionRevision = '2026-10-21-final-v2';\n  const productPublicationRevision = '2026-10-22-six-products';")
s=s.replace("toastTimer, savedRevision = '';","toastTimer, savedRevision = '', savedProductPublicationRevision = '';",1)
s=s.replace("savedRevision = saved.executionRevision || '';","savedRevision = saved.executionRevision || '';\n      savedProductPublicationRevision = saved.productPublicationRevision || '';",1)
s=s.replace('  function icon(name) {',"  // Add the newly verified product tick once without changing other saved owner progress.\n  if (savedProductPublicationRevision !== productPublicationRevision && execution.products.complete) done.products = true;\n  function icon(name) {",1)
s=s.replace('JSON.stringify({done, draft, executionRevision})','JSON.stringify({done, draft, executionRevision, productPublicationRevision})')
s=s.replace("id:'products', title:'Publish accurate physical products', time:'In progress'","id:'products', title:'Publish accurate physical products', time:'Added'")
p.write_text(s,encoding='utf-8')

p=root/'index.html';s=p.read_text(encoding='utf-8')
s=s.replace('id="navCount">5','id="navCount">4').replace('id="doneCount">13','id="doneCount">14').replace('13 items completed or reviewed. Five follow-ups remain.','14 items completed or reviewed. Four core profile follow-ups remain.').replace('aria-valuenow="13"','aria-valuenow="14"').replace('id="percent">72%','id="percent">78%').replace('13 checked. Five follow-ups remain.','14 checked. Four core profile follow-ups remain.').replace('VERIFIED SNAPSHOT · 21 OCTOBER 2026','VERIFIED SNAPSHOT · 22 OCTOBER 2026')
s=s.replace('; product publication and representative-image descriptions.','. Separately, Google is reviewing one corrected key product edit, and the offer expiry time needs a manual check.')
s=s.replace('The first five products are submitted and processing; public catalogue readback remains to be verified.','All six products were verified publicly. Five remain live; the corrected key title/description edit is Pending Google review.')
s=s.replace('<h2>Physical product drafts</h2><p>Owner-authorized generic prices and representative AI illustrations. Five items submitted; public visibility not yet verified.</p></div><span class="pill neutral">Publication in progress</span>','<h2>Six products added</h2><p>Owner-authorized generic prices and representative AI illustrations. Initial six-item catalogue verified publicly.</p></div><span class="pill">Added · one edit Pending</span>')
s=s.replace('<td>Computerised key blank</td>','<td>Computerised key (edit Pending)</td>')
s=s.replace('Five products were submitted after AI image uploads. Google confirms processing for each, which may take up to 30 minutes. The sixth is being prepared; public catalogue readback remains to be verified. The images are AI-generated representatives, not photographs of actual stock. Product disclosure and the first key-title correction remain to be verified. You will update the generic prices.','All six names and prices were verified in Google’s public Products catalogue. The first key listing was then corrected in the same product to Computerised key with an image disclosure; that edit is saved and Pending review, so its former public title may remain temporarily. The other five are live. Images are AI-generated representatives, not photographs of actual shop stock. You will update the generic prices.')
s=s.replace('Open all descriptions and product drafts','Open descriptions and publication details')
s=s.replace('product publication is in progress with AI representative assets; public product visibility is not yet verified.','all six products were added, with one corrected key edit Pending review. Offer expiry control readback still needs a manual check.')
p.write_text(s,encoding='utf-8')

p=root/'README.md';s=p.read_text(encoding='utf-8')
s=s.replace('with 13 seeded from the verified 21 October 2026 execution snapshot','with 14 checked from the verified 21–22 October 2026 execution snapshot')
s=re.sub(r'Product publication is in progress\..*?AI image disclosures and the first key-title correction are prepared for browser saving\.', 'All six product names/prices were verified in the public catalogue. Five remain live; the same first key listing was corrected to Computerised key with a representative-image description, and that edit is Pending Google review. Six owner-authorized AI representative illustrations are in product-images/manifest.json. The owner will update generic prices. No further product-image input is needed for this workflow.',s)
s+='\nThe new product completion tick is added once without clearing other saved checklist progress. Later resets remain respected. The offer expiry-control readback shows 11:59 without AM/PM while approved terms state 23:59; exact control verification remains unresolved.\n'
p.write_text(s,encoding='utf-8')

for f in ['PUBLISHING-QUEUE.json','service-product-drafts.json','business-content.json','updates-and-offer.json','product-images/manifest.json']:json.loads((root/f).read_text(encoding='utf-8'))
assert sum(x['complete'] for x in d.values())==14
print('Five JSON files parsed. Checklist14/18. Five public products + one previously public Pending edit; exact key correction recorded. No more product-photo request.')
