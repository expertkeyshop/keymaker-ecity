from pathlib import Path
import json,re
r=Path(__file__).parent
texts=[
'Computerised/dimple key for compatible locks. Match the key profile with your original key or lock. Indicative price; confirm the exact key type and cutting requirements before ordering. Representative AI-generated illustration; actual key design may differ.',
'Replacement outer body or shell for compatible car remote keys. Casing only, not a complete programmed key. Confirm the vehicle model, button layout, included parts and final price before ordering. Indicative price. Representative AI-generated illustration; actual design may differ.',
'Replacement handle for compatible cylinder-lock fittings. Check door thickness, fixing positions and existing hardware before purchase. Indicative price; confirm the model, supplied parts and installation charges. Representative AI-generated illustration; actual design may differ.',
'Replacement cylinder for compatible door locks. Match the cylinder size and fitting type to your existing hardware. Indicative price; confirm the exact model, supplied keys, finish and installation charges before purchase. Representative AI-generated illustration; actual design may differ.',
'Main door lock for compatible door sizes and fitting types. Share your existing lock and door details to check suitability. Indicative price; confirm the exact model, supplied components and fitting charges before purchase. Representative AI-generated illustration; actual design may differ.',
'Remote key unit for supported vehicle models. Electronics and compatibility depend on the vehicle. Indicative price; confirm the exact unit, included blade, cutting and programming charges before ordering. Representative AI-generated illustration; actual design may differ.'
]
for f in ['PUBLISHING-QUEUE.json','service-product-drafts.json','business-content.json']:
 p=r/f;d=json.loads(p.read_text(encoding='utf-8'));a=d.get('products',d.get('product_drafts',[]))
 for i,x in enumerate(a):
  x['description']=texts[i];x['description_with_image_disclosure']=texts[i];x['description_record_note']='Exact text entered and submitted through the Google product form. First corrected item is Pending review; other five product names/prices are publicly verified.'
  x['disclosure_publication_status']='exact_corrected_description_saved_pending_review' if i==0 else 'exact_submitted_description_recorded'
  if 'photo_needed' in x:x['original_model_reference']=x.pop('photo_needed')
  x['image_available']=x['image_asset']
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

p=r/'product-images/manifest.json';d=json.loads(p.read_text(encoding='utf-8'))
for i,a in enumerate(d['assets']):a['exact_submitted_product_description']=texts[i]
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

p=r/'SERVICES-AND-PRODUCTS.md';s=p.read_text(encoding='utf-8');a=s.index('## Six physical products added');b=s.index('## Corrections and safeguards',a)
q=json.loads((r/'PUBLISHING-QUEUE.json').read_text(encoding='utf-8'));part=['## Six physical products added','','All six names/prices were verified in the public Google catalogue. The same first key listing was then corrected to Computerised key and its edit is Pending Google review; the other five are live. The former public key title may remain until approval.','','The owner authorized the generic prices and AI representative illustrations and will update prices. These are not photographs of actual stock. Assets, prompts and exact submitted descriptions are in `product-images/manifest.json`.','']
for i,x in enumerate(q['products']):
 part += ['### '+x['name']+' — ₹'+str(x['requested_generic_price_inr']),'','Category: '+x['category'],'','Status: '+x['status']+'.','','Exact submitted description'+(' — correction Pending review:' if i==0 else ':'),'',texts[i],'','Image asset: `'+x['image_asset']+'`.','']
s=s[:a]+'\n'.join(part)+s[b:];p.write_text(s,encoding='utf-8')

p=r/'PUBLISHING-QUEUE.md';s=p.read_text(encoding='utf-8');a=s.index('## Six products');b=s.index('## Two published Updates',a)
part=['## Six products added','','All six initial names/prices were verified publicly. The key correction is saved in the same item and Pending Google review; the other five remain live. Generic prices and representative AI imagery were explicitly owner-authorized.','']
for i,x in enumerate(q['products']):
 part += ['### '+x['name']+' — ₹'+str(x['requested_generic_price_inr']),'','Category: '+x['category']+'. Status: '+x['status']+'.','',texts[i],'','Representative image: `'+x['image_asset']+'`.','']
part += ['The initial missing-photo error was resolved using the authorized AI illustrations. No further product-photo input is needed. The illustrations are not actual-stock photographs.','','Key edit identifiers: UUID `8b6e11a4-2174-4d9e-95e7-81612fa0f5fb`; public product ID `8210459654379117113`. No duplicate was created. The former public name Computerised key blank may remain until review completes.','','Screenshots: `gbp-products-live.png` and `gbp-six-products-manager.png` in the task visualization folder.','']
s=s[:a]+'\n'.join(part)+s[b:];p.write_text(s,encoding='utf-8')

p=r/'GMB-EXECUTION.md';s=p.read_text(encoding='utf-8')
s=s.replace('- Add useful interior, machine and work images as needed. No new images were uploaded during this work.','- Add useful shop interior, machine and work images as needed. No new storefront or logo photo was uploaded; six representative AI product illustrations were uploaded separately.')
s=s.replace('For products 2–6, the submitted concise descriptions included “Representative AI-generated illustration; actual design may differ.” Local queued reference bodies are retained and labelled as such, rather than claiming a full exact readback.','Exact submitted descriptions for all six products are now recorded in PUBLISHING-QUEUE.json, service-product-drafts.json, business-content.json, SERVICES-AND-PRODUCTS.md and product-images/manifest.json. They include clear representative AI-image disclosures. The first corrected text remains Pending review; the other five are live.')
p.write_text(s,encoding='utf-8')
for f in ['PUBLISHING-QUEUE.json','service-product-drafts.json','business-content.json','updates-and-offer.json','product-images/manifest.json']:json.loads((r/f).read_text(encoding='utf-8'))
print('Exact submitted descriptions recorded for six products. Five JSON files parsed. No product-image upload demand remains in current queue.')
