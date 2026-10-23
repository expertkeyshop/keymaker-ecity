from pathlib import Path
import json,re
root=Path(__file__).parent
paragraph='AI-generated representative illustration, not a photo of actual shop stock. Exact design, supplied parts and compatibility vary; confirm the item and price before purchase.'
slugs=['computerised-key-blank','car-remote-shell','cylinder-lock-handle','door-lock-cylinder','main-door-lock','car-remote-key-unit']
expiry='The approved terms explicitly end at 23:59 India time on 31 October 2026. The editor readback shows 11:59 without AM/PM despite attempts to save 23:59; the exact persisted expiry time is unresolved and needs a manual UI check. Do not claim the end-time control is verified.'
for name in ['PUBLISHING-QUEUE.json','service-product-drafts.json','business-content.json']:
    p=root/name;d=json.loads(p.read_text(encoding='utf-8'));products=d.get('products',d.get('product_drafts',[]))
    for i,item in enumerate(products):
        item['status']='submitted_processing' if i==0 else 'prepared_not_submitted'
        item['image_asset']='product-images/'+slugs[i]+'.png'
        item['image_note']=paragraph
        item['image_description_paragraph']=paragraph
        item['description_with_image_disclosure']=item['description']+'\n\n'+paragraph
        item['disclosure_publication_status']='prepared_for_browser_save_not_yet_verified'
        item['editor_note']='AI representative image uploaded; owner clicked Publish. Google confirmed “Your product is being added”, which may take up to 30 minutes. Not yet verified publicly visible.' if i==0 else 'AI representative image prepared; publication has not yet been verified for this item.'
        if i==0:
            item['photo_validation_history']='Earlier photo-required error was resolved by uploading the owner-authorized AI representative image.'
            item.pop('validation_error',None)
            item['form_state']='Submitted by owner; Google processing confirmation displayed.'
            item['pending_content_correction']='Current title remains Computerised key blank. Generated illustration depicts a generic cut/dimple key. Rename to Computerised key and add representative-image disclosure; correction not yet verified in Google.'
    d['products_status']='publication_in_progress'
    d['products_published_count']=0
    d['product_image_assets']={'manifest':'product-images/manifest.json','count':6,'type':'AI-generated generic representative illustrations, not actual stock photographs','owner_authorized':True,'description_disclosure':paragraph}
    d['product_photo_validation']['current_state']='resolved_with_owner_authorized_AI_representative_assets'
    d['product_photo_validation']['historical_error']=d['product_photo_validation']['error']
    d['product_photo_validation']['actual_product_images_in_workspace']=False
    d['product_photo_validation']['representative_AI_images_available']=True
    if name=='PUBLISHING-QUEUE.json':
        d['publication_status']='publication_in_progress'
        d['blocker']=None
        d['publication_note']='Six owner-authorized AI representative product illustrations are available. First product was submitted by the owner and is being processed; remaining five are not yet verified submitted. No products are claimed live. Existing posts remain published.'
        auth='Generate or download representative product images and use them for the generic product listings.'
        if auth not in d['owner_authorizations']:d['owner_authorizations'].append(auth)
        d['offer']['expiry_control_note']=expiry
    if name=='service-product-drafts.json':
        d['product_pricing_status']='Owner-authorized reference prices retained; first product submitted and processing, remaining five awaiting submission/readback. Owner will adjust prices. AI representative-image disclosures are prepared.'
    if name=='business-content.json':
        d['products_pending_reason']='Publication in progress with six owner-authorized AI representative illustrations. First item submitted and processing; five others not yet verified submitted. No live product verified yet.'
        d['execution']['products']={'status':'publication_in_progress','complete':False,'details':d['products_pending_reason']}
        d['publishing_queue']['products_status']='publication_in_progress'
        d['publishing_queue']['blocker']=None
        d['approved_offer']['expiry_control_note']=expiry
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

p=root/'updates-and-offer.json';d=json.loads(p.read_text(encoding='utf-8'));d['offer']['expiry_control_note']=expiry;p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

p=root/'product-images'/'manifest.json';d=json.loads(p.read_text(encoding='utf-8'))
d['description_reference_file']='../service-product-drafts.json'
d['description_disclosure']=paragraph
for i,a in enumerate(d['assets']):
    a['description_disclosure']=paragraph
    a['product_index']=i+1
    a['generic_price_inr']=[250,650,700,950,2300,1500][i]
    a['publication_status']='submitted_processing' if i==0 else 'prepared_not_submitted'
    if i==0:a['observed_correction_note']='Parent visually identified this as a generic cut/dimple key illustration rather than an uncut blank. Current product title needs correction to Computerised key.'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

p=root/'PUBLISHING-QUEUE.md';s=p.read_text(encoding='utf-8')
s=s.replace('- **Products: blocked_missing_product_photos; 0 published.** The first item was fully filled and Publish clicked; Google displayed the red validation error “Add a product photo”. It remains unsaved, with the form open. The other five items are prepared but not submitted.','- **Products: publication_in_progress; 0 verified live.** Six owner-authorized AI representative illustrations are available. The owner clicked Publish on the first item after its image upload; Google displayed “Your product is being added” and up to 30 minutes processing. The remaining five items are prepared and not yet verified submitted.')
s=s.replace('six products are blocked by missing actual product photos.','six products are being prepared/submitted with AI representative illustrations.')
s=s.replace('Photo requirement is now confirmed by actual Publish validation: **“Add a product photo”**. Screenshot: `C:/Users/kbose/.codex/visualizations/2026/10/21/01a15ed4-019d-7e73-811d-563248a44e98/gbp-product-photo-required.png`. No actual product images are present in the workspace. Supply one clear photo of each of the six listed physical products. No competitor image, fake stock photo or invented branded SKU was used.','The earlier required-photo validation was resolved for the first item using an owner-authorized AI representative illustration. Six generated assets and their prompts are in `product-images/manifest.json`; they are illustrations, not photographs of actual stock. No competitor images or brand claims were copied.\n\nPrepared disclosure for each product: '+paragraph+'\n\nThe first item currently says Computerised key blank, while its generated illustration depicts a generic cut/dimple key. A title correction to Computerised key and disclosure save remain to be verified; do not claim those edits are live yet.')
s=s.replace('Supply the six actual product photos, then submit/verify products individually;','Use the prepared AI representative assets with the image disclosure, then submit/verify products individually;')
if '## Offer expiry control check' not in s:s+='\n## Offer expiry control check\n\n'+expiry+'\n'
p.write_text(s,encoding='utf-8')

p=root/'SERVICES-AND-PRODUCTS.md';s=p.read_text(encoding='utf-8')
start=s.index('**Product status: blocked_missing_product_photos; 0 published.**');end=s.index('### Computerised key blank',start)
s=s[:start]+'**Product status: publication_in_progress; 0 verified live.** The owner authorized generic prices and AI representative illustrations. All six generated assets are in `product-images/`, with prompts and disclosure in `product-images/manifest.json`. The first product was submitted by the owner after image upload; Google confirmed it is being added and may take up to 30 minutes. The other five products are not yet verified submitted.\n\nPrepared image disclosure for each product: '+paragraph+'\n\nThe image is representative; confirm the actual item, inclusions and price. The first illustration is a cut/dimple key, so the current “Computerised key blank” title needs correction to “Computerised key”. That Google edit is not yet verified.\n\n'+s[end:]
s=s.replace('Status: attempted_unsaved_photo_required. Price ₹250, category Keys and key blanks, and description were filled.','Status: submitted_processing. Price ₹250, category Keys and key blanks; Google confirmed the product is being added. Image disclosure and title correction are prepared, not yet verified saved.')
s=re.sub(r'Photo/model needed: ([^\n]+)',r'Actual model reference for future owner refinement: \1',s)
p.write_text(s,encoding='utf-8')

p=root/'GMB-EXECUTION.md';s=p.read_text(encoding='utf-8')
s=s.replace('## Product Publish validation confirmed photo requirement — 22 October 2026','## Historical product photo validation — 22 October 2026')
if '## Representative product assets and submission in progress' not in s:
    s+='\n## Representative product assets and submission in progress — 22 October 2026\n\nThe owner explicitly authorized generated or downloaded product images. Six generic AI illustrations were generated and saved in `product-images/`; `product-images/manifest.json` records prompts, source files, intended products, prices and the representative-image disclosure. They are not photos of actual stock.\n\nAfter the first image upload, the owner clicked Publish. Google confirmed “Your product is being added” and up to 30 minutes processing. First item: submitted_processing; other five: prepared_not_submitted. **No products are yet verified live.** The first image depicts a cut/dimple key rather than an uncut blank, so its current title requires correction to Computerised key and an image-disclosure save; neither edit is yet claimed verified. The older photo-blocked status is superseded.\n\nDisclosure prepared for each product: '+paragraph+'\n\n### Offer expiry readback uncertainty\n\n'+expiry+'\n'
p.write_text(s,encoding='utf-8')

p=root/'updates-and-offer.md';s=p.read_text(encoding='utf-8')
if '## Expiry control readback check' not in s:s+='\n## Expiry control readback check\n\n'+expiry+'\n'
p.write_text(s,encoding='utf-8')

p=root/'app.js';s=p.read_text(encoding='utf-8');m=re.search(r'  const execution = (\{[^\n]+\});',s);assert m
d=json.loads(m.group(1));d['products']={'status':'Publication in progress','summary':'Six representative AI product illustrations are ready. First item submitted and processing; 0 verified live.','steps':['The owner authorized generic prices and generated product illustrations. Files and prompts are in product-images/manifest.json. These are not photographs of actual shop stock.','The owner clicked Publish after the first image upload; Google confirmed the product is being added and may take up to 30 minutes. The other five are not yet verified submitted.','Prepared descriptions disclose that the images are AI-generated and representative. Confirm exact design, supplied parts, compatibility and price before purchase.','The first illustration depicts a cut/dimple key, so the existing Computerised key blank title needs correction to Computerised key. Neither this correction nor the new disclosure is yet claimed verified.'],'complete':False}
s=s[:m.start(1)]+json.dumps(d,ensure_ascii=False)+s[m.end(1):]
s=s.replace("id:'products', title:'Publish accurate physical products', time:'Photos needed'","id:'products', title:'Publish accurate physical products', time:'In progress'")
p.write_text(s,encoding='utf-8')

p=root/'index.html';s=p.read_text(encoding='utf-8')
s=s.replace('actual product photos required by Google.','product publication and representative-image descriptions.')
s=s.replace('Products are blocked by confirmed “Add a product photo” validation; none is published.','Six owner-authorized representative AI product illustrations are ready. The first product is being processed; no product is yet verified live.')
s=s.replace('Owner-authorized generic prices from your reference. 0 published: Google requires product photos.','Owner-authorized generic prices and representative AI illustrations. First item submitted; 0 verified live.')
s=s.replace('Actual product photos required','Publication in progress')
s=s.replace('The first item was fully filled, but clicking Publish showed “Add a product photo”. Its form remains open and unsaved. The other five items have not been submitted. Send one actual photo per product; you have authorized the generic prices and will update them. Shells, electronic units and programmed keys have different inclusions.','The first product was submitted by the owner after an AI image upload. Google says it is being added and may take up to 30 minutes. Five more are prepared and not yet verified submitted. The images are AI-generated representatives, not photographs of actual stock. Product disclosure and the first key-title correction remain to be verified. You will update the generic prices.')
s=s.replace('products are blocked by missing required product photos; 0 are published.','product publication is in progress with AI representative assets; 0 products are yet verified live.')
p.write_text(s,encoding='utf-8')

p=root/'README.md';s=p.read_text(encoding='utf-8')
s=s.replace('Product publication is blocked_missing_product_photos: the first fully filled product failed Publish validation with “Add a product photo” and remains unsaved; five more are prepared but not submitted, with zero published. The owner authorized generic prices and will update them. Actual product photos are needed.','Product publication is in progress. Six owner-authorized AI representative illustrations and their prompts are in product-images/manifest.json. The owner submitted the first item after image upload; Google says it is being added. Five more are prepared and not yet verified submitted; zero products are yet verified live. The owner will update the generic prices. AI image disclosures and the first key-title correction are prepared for browser saving.')
p.write_text(s,encoding='utf-8')

for name in ['PUBLISHING-QUEUE.json','service-product-drafts.json','business-content.json','updates-and-offer.json','product-images/manifest.json']:json.loads((root/name).read_text(encoding='utf-8'))
print('Five JSON files parsed. Six asset/disclosure references saved. First submitted_processing; five prepared_not_submitted; zero verified live. Offer expiry control remains unresolved.')
