from pathlib import Path
import json,re
root=Path(__file__).parent
proof='C:/Users/kbose/.codex/visualizations/2026/10/21/01a15ed4-019d-7e73-811d-563248a44e98/gbp-product-photo-required.png'
first='Key blank for compatible computerised locks. Match the key profile with your existing key or lock. Indicative price; confirm the suitable blank and whether cutting is included before purchase.'
note='Confirmed by submission validation: clicking Publish on the fully filled first product displayed the red error “Add a product photo”. The first product remains unsaved. Actual product photos are needed; no product was published.'
for name in ['PUBLISHING-QUEUE.json','service-product-drafts.json','business-content.json']:
    p=root/name;d=json.loads(p.read_text(encoding='utf-8'))
    products=d.get('products',d.get('product_drafts',[]))
    for i,item in enumerate(products):
        item['status']='attempted_unsaved_photo_required' if i==0 else 'prepared_not_submitted'
        item['editor_note']=note if i==0 else 'The same product editor requires a photo, confirmed on the first product. This item has not been submitted; an actual product photo is needed.'
        if i==0:
            item['description']=first
            item['validation_error']='Add a product photo'
            item['screenshot']=proof
            item['form_state']='Left open with name, category Keys and key blanks, INR price 250 and description filled; unsaved because a photo is required.'
    d['products_status']='blocked_missing_product_photos'
    d['products_published_count']=0
    d['product_photo_validation']={'checked_at_local':'2026-10-22','required':True,'error':'Add a product photo','first_product_status':'attempted_unsaved_photo_required','other_products_status':'prepared_not_submitted','screenshot':proof,'actual_product_images_in_workspace':False}
    if name=='PUBLISHING-QUEUE.json':
        d['blocker']='Six actual product photos are missing. First product Publish validation displayed “Add a product photo”; none of the six products is published.'
        d['publication_note']='Both service Updates and SPARE10 Offer are Published. Opening Update remains Pending review. Products are blocked by confirmed missing-photo validation, not browser access.'
    if name=='service-product-drafts.json':
        d['product_pricing_status']='Owner explicitly authorized the six generic reference prices and will update them. Prices retained: INR250,650,700,950,2300,1500. None are published because actual product photos are missing.'
    if name=='business-content.json':
        d['products_published']=False
        d['products_pending_reason']=d['blocker'] if 'blocker' in d else 'Confirmed Google validation requires a product photo. First product is attempted but unsaved; five are prepared and not submitted. Owner-authorized generic prices are preserved.'
        d['execution']['products']={'status':'blocked_missing_product_photos','complete':False,'details':'Publish was attempted for Computerised key blank at INR250. Google displayed “Add a product photo”. Six actual product photos are needed; first item is unsaved and other five are not submitted. Zero products published.'}
        d['publishing_queue']['products_status']='blocked_missing_product_photos'
        d['publishing_queue']['products_published_count']=0
        d['publishing_queue']['blocker']='Actual product photos missing; confirmed Google validation “Add a product photo”.'
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

p=root/'PUBLISHING-QUEUE.md';s=p.read_text(encoding='utf-8')
s=s.replace('- No products have been submitted. The screenshot supplied by the owner shows the empty Products introduction.','- **Products: blocked_missing_product_photos; 0 published.** The first item was fully filled and Publish clicked; Google displayed the red validation error “Add a product photo”. It remains unsaved, with the form open. The other five items are prepared but not submitted.')
s=s.replace('The earlier product form had a photo selector; mandatory-photo validation has not been tested. No competitor image, fake stock photo or invented branded SKU was used.','Photo requirement is now confirmed by actual Publish validation: **“Add a product photo”**. Screenshot: `'+proof+'`. No actual product images are present in the workspace. Supply one clear photo of each of the six listed physical products. No competitor image, fake stock photo or invented branded SKU was used.')
s=s.replace('Key blank for compatible computerised locks. Match the key profile with your existing key or lock. Confirm the suitable blank and whether cutting is included before purchase.',first)
s=s.replace('six products require individual verification.','six products are blocked by missing actual product photos.')
p.write_text(s,encoding='utf-8')

p=root/'SERVICES-AND-PRODUCTS.md';s=p.read_text(encoding='utf-8')
s=s.replace("These are prepared, not published. Prices are illustrative adaptations of the owner's pasted Expert Key Shop examples, not verified market prices or confirmed selling prices. Replace or confirm them before publication. Match each photo and description to the actual item sold. Brand/model names have been omitted because exact stock was not supplied.","**Product status: blocked_missing_product_photos; 0 published.** The owner explicitly authorized these generic reference prices and will update them. The first product’s fully filled form was submitted with Publish, and Google displayed the red error “Add a product photo”; the form remains unsaved. The other five items are prepared but not submitted. One actual product photo per item is needed. Brand/model names remain generic because exact stock was not supplied.\n\nScreenshot: `"+proof+"`.")
s=s.replace('Key blank for compatible computerised locks. Match the key profile with your existing key or lock. Confirm the suitable blank and whether cutting is included before purchase.',first)
s=s.replace('Photo/model needed: Actual uncut key blank and its profile; confirm exact blank type.','Status: attempted_unsaved_photo_required. Price ₹250, category Keys and key blanks, and description were filled.\n\nPhoto/model needed: Actual uncut key blank and its profile; confirm exact blank type.')
p.write_text(s,encoding='utf-8')

p=root/'GMB-EXECUTION.md';s=p.read_text(encoding='utf-8')
s=s.replace('The editor’s INR price is optional, and its product-photo input was inspected. Actual photos, exact product identification and selling prices are still needed.','The owner authorized the six generic reference prices and intends to update them. A subsequent Publish attempt confirmed that an actual product photo is required; see the latest validation record below.')
if '## Product Publish validation confirmed photo requirement' not in s:
    s+='\n## Product Publish validation confirmed photo requirement — 22 October 2026\n\nStatus: **blocked_missing_product_photos; 0 products published.** The Computerised key blank form was fully filled: category Keys and key blanks; price ₹250; description “'+first+'”. Clicking Publish displayed the red error **“Add a product photo”**. It remains unsaved with the first form open. The other five products are prepared but not submitted. No actual product photos are present in the workspace.\n\nOwner-authorized generic prices retained:\n\n- Computerised key blank: ₹250.\n- Car remote key body and shell: ₹650.\n- Cylinder lock handle: ₹700.\n- Door lock cylinder: ₹950.\n- Main door lock: ₹2,300.\n- Car remote key unit: ₹1,500.\n\nThe owner needs to supply one actual photo of each physical product. Screenshot: `'+proof+'`. Browser access is working; product-photo validation is the current product blocker. Opening Update status remains Pending; it has not been changed by this product attempt.\n'
p.write_text(s,encoding='utf-8')

p=root/'app.js';s=p.read_text(encoding='utf-8');m=re.search(r'  const execution = (\{[^\n]+\});',s)
assert m
d=json.loads(m.group(1));d['products']={'status':'Needs product photos — validation confirmed','summary':'0 products published. Google requires a product photo; the first item remains unsaved.','steps':['Publish was clicked for Computerised key blank with category Keys and key blanks, price ₹250 and the description filled. Google displayed the red error “Add a product photo”.','Send actual photos of the six physical products. No suitable product images are present in the workspace.','Authorized reference prices: key blank ₹250; remote shell ₹650; cylinder handle ₹700; door cylinder ₹950; main door lock ₹2,300; electronic remote unit ₹1,500. The owner will update prices.','The first form is open but unsaved; the other five items are prepared and not submitted. Products are blocked by missing photos, not browser access.'],'complete':False}
s=s[:m.start(1)]+json.dumps(d,ensure_ascii=False)+s[m.end(1):]
p.write_text(s,encoding='utf-8')

p=root/'index.html';s=p.read_text(encoding='utf-8')
s=s.replace('product photos and selling prices.','actual product photos required by Google.')
s=s.replace('Products require their own publication checks.','Products are blocked by confirmed “Add a product photo” validation; none is published.')
s=s.replace('Illustrative prices from your Expert Key Shop reference. Not published.','Owner-authorized generic prices from your reference. 0 published: Google requires product photos.')
s=s.replace('Photos and price confirmation needed','Actual product photos required')
s=s.replace('Provide genuine product photos and exact model details. Confirm actual selling prices before publishing. Shells, electronic remote units and complete programmed keys have different inclusions.','The first item was fully filled, but clicking Publish showed “Add a product photo”. Its form remains open and unsaved. The other five items have not been submitted. Send one actual photo per product; you have authorized the generic prices and will update them. Shells, electronic units and programmed keys have different inclusions.')
s=s.replace('products remain separately tracked.','products are blocked by missing required product photos; 0 are published.')
p.write_text(s,encoding='utf-8')

p=root/'README.md';s=p.read_text(encoding='utf-8')
s=s.replace('Product publication awaits actual photos/model details and confirmed selling prices.','Product publication is blocked_missing_product_photos: the first fully filled product failed Publish validation with “Add a product photo” and remains unsaved; five more are prepared but not submitted, with zero published. The owner authorized generic prices and will update them. Actual product photos are needed.')
p.write_text(s,encoding='utf-8')

for name in ['PUBLISHING-QUEUE.json','service-product-drafts.json','business-content.json','updates-and-offer.json']:
    json.loads((root/name).read_text(encoding='utf-8'))
print('JSON parsed: 4 files. Product states: first attempted_unsaved_photo_required; five prepared_not_submitted; zero published. Opening state preserved.')
