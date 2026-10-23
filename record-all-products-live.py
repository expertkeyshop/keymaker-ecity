from pathlib import Path
import json,re
r=Path(__file__).parent
summary='All six products are live. A fresh owner-catalogue reload showed no Pending label on Computerised key, and fresh public Google Search Products displayed the corrected title and all six prices.'
for f in ['PUBLISHING-QUEUE.json','service-product-drafts.json','business-content.json']:
 p=r/f;d=json.loads(p.read_text(encoding='utf-8'));items=d.get('products',d.get('product_drafts',[]))
 for i,x in enumerate(items):
  x['status']='publicly_visible';x['visibility_verified']='Fresh Google owner catalogue and public Search Products confirmed the current name and price on 22 October 2026; no Pending label remains.'
  x['editor_note']='Current product is publicly visible. All six catalogue entries were verified after reload.'
  if i==0:
   x['correction_status']='approved_publicly_visible'
   x['correction_note']='The same product was renamed from Computerised key blank to Computerised key. Fresh public Search verified the corrected title; no Pending label remains in the reloaded owner catalogue.'
   x.pop('pending_content_correction',None);x['form_state']='Edit approved; corrected title publicly visible.'
   x['disclosure_publication_status']='exact_corrected_description_submitted_product_now_public'
  x['description_record_note']='Exact text entered and submitted through the Google product form. Current name and price are publicly verified. Full public detail body is being checked separately.'
 d['products_status']='publicly_visible';d['products_published_count']=6;d['products_publicly_visible_verified_count']=6;d['products_previously_public_pending_edit_count']=0;d['products_pending_reason']=None
 if f=='PUBLISHING-QUEUE.json':
  d['publication_status']='published';d['publication_note']=summary+' Offer expiry-control readback remains a separate manual check.'
 if f=='service-product-drafts.json':d['product_pricing_status']='All six owner-authorized generic prices published and verified: INR250,650,700,950,2300,1500. Corrected key title is publicly visible. Owner will update prices.'
 if f=='business-content.json':
  d['execution']['products']={'status':'All six products live','complete':True,'details':summary}
  d['publishing_queue'].update(products_status='publicly_visible',products_published_count=6,products_publicly_visible_verified_count=6,products_previously_public_pending_edit_count=0)
 p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

p=r/'product-images/manifest.json';d=json.loads(p.read_text(encoding='utf-8'))
for a in d['assets']:a['publication_status']='publicly_visible'
d['assets'][0]['observed_correction_note']='The image depicts a generic cut/dimple key. The same product was corrected to Computerised key; a fresh public Search readback verified the title and a reloaded owner catalogue showed no Pending label.'
d['assets'][0]['corrected_description_submitted']=d['assets'][0].pop('corrected_description_pending_review',None)
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

q=json.loads((r/'PUBLISHING-QUEUE.json').read_text(encoding='utf-8'))
for file,start,end in [('PUBLISHING-QUEUE.md','## Six products added','## Two published Updates'),('SERVICES-AND-PRODUCTS.md','## Six physical products added','## Corrections and safeguards')]:
 p=r/file;s=p.read_text(encoding='utf-8');a=s.index(start);b=s.index(end,a)
 section=[start,'',summary,'','The owner authorized the generic prices and AI representative illustrations and will update prices. The illustrations are not photographs of actual shop stock. Assets and prompts are in `product-images/manifest.json`.','']
 for x in q['products']:
  section += ['### '+x['name']+' — ₹'+str(x['requested_generic_price_inr']),'','Category: '+x['category']+'. Status: publicly_visible.','','Exact submitted description:', '',x['description'],'','Image: `'+x['image_asset']+'`.','']
 section += ['The same first product was corrected from Computerised key blank to Computerised key; no duplicate was created. Corrected title is now public. UUID `8b6e11a4-2174-4d9e-95e7-81612fa0f5fb`; public product ID `8210459654379117113`.','','Screenshots: `gbp-products-live.png` and refreshed `gbp-six-products-manager.png` in the task visualization folder.','']
 s=s[:a]+'\n'.join(section)+s[b:];s=s.replace('Recheck the first corrected product edit after Google review; do not create duplicates.','The corrected key edit is approved and publicly visible; no duplicate products are needed.')
 p.write_text(s,encoding='utf-8')

p=r/'GMB-EXECUTION.md';s=p.read_text(encoding='utf-8')
s+='\n## Final reload: all six products live — 22 October 2026\n\n'+summary+' The corrected key edit is approved in the same product. Exact submitted descriptions and representative-image disclosures are preserved in the product records. This supersedes the earlier Pending-edit status.\n\nChecklist remains **14 of 18**. Six live products/prices: Computerised key ₹250; car remote shell ₹650; cylinder handle ₹700; door cylinder ₹950; main door lock ₹2,300; car remote key unit ₹1,500. Owner may update generic prices. No more product images or duplicate listings are needed. The offer expiry-control readback and public phone visibility remain separate unresolved checks.\n'
p.write_text(s,encoding='utf-8')

p=r/'app.js';s=p.read_text(encoding='utf-8');m=re.search(r'  const execution = (\{[^\n]+\});',s);assert m;d=json.loads(m.group(1))
d['products']['status']='All six products live';d['products']['summary']='All six products and prices are publicly visible, including the corrected Computerised key title.'
d['products']['steps'][1]='The same first product was corrected to Computerised key with representative-image wording. Fresh public Search showed the corrected title and the reloaded owner catalogue showed no Pending label.'
d['posts']['steps'][3]='The latest two service Updates and opening Update have no CTA. All six products are live with owner-authorized representative AI imagery; no duplicate posts or products are needed.'
s=s[:m.start(1)]+json.dumps(d,ensure_ascii=False)+s[m.end(1):];p.write_text(s,encoding='utf-8')

p=r/'index.html';s=p.read_text(encoding='utf-8')
s=s.replace('Google is reviewing one corrected key product edit, and the offer expiry time needs a manual check.','all six products are live, and the offer expiry time still needs a manual check.')
s=s.replace('All six products were verified publicly. Five remain live; the corrected key title/description edit is Pending Google review.','All six products are live, including the corrected Computerised key title. A refreshed catalogue showed no Pending label.')
s=s.replace('Added · one edit Pending','All six live').replace('Computerised key (edit Pending)','Computerised key')
s=s.replace('All six names and prices were verified in Google’s public Products catalogue. The first key listing was then corrected in the same product to Computerised key with an image disclosure; that edit is saved and Pending review, so its former public title may remain temporarily. The other five are live. Images are AI-generated representatives, not photographs of actual shop stock. You will update the generic prices.','All six names and prices are verified in Google’s public Products catalogue. The corrected Computerised key title is now public, and the reloaded owner catalogue shows no Pending label. Images are AI-generated representatives, not photographs of actual shop stock. You will update the generic prices.')
s=s.replace('all six products were added, with one corrected key edit Pending review.','all six products are live, including the approved key correction.')
p.write_text(s,encoding='utf-8')

p=r/'README.md';s=p.read_text(encoding='utf-8')
s=s.replace('All six product names/prices were verified in the public catalogue. Five remain live; the same first key listing was corrected to Computerised key with a representative-image description, and that edit is Pending Google review.','All six product names/prices are verified in the public catalogue. The same first key listing was corrected to Computerised key, and a fresh public Search plus owner-catalogue reload confirmed the correction is live with no Pending label.')
p.write_text(s,encoding='utf-8')
for f in ['PUBLISHING-QUEUE.json','service-product-drafts.json','business-content.json','updates-and-offer.json','product-images/manifest.json']:json.loads((r/f).read_text(encoding='utf-8'))
print('All6 publicly_visible; correctedkeyapproved;14/18. Five JSONs parsed.')
