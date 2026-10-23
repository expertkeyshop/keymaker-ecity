from pathlib import Path
import json

root=Path(__file__).resolve().parent
updates=json.loads((root/'updates-and-offer.json').read_text(encoding='utf-8'))
catalog=json.loads((root/'service-product-drafts.json').read_text(encoding='utf-8'))
faqs=json.loads((root/'faqs.json').read_text(encoding='utf-8'))
event={
 'title':'Shop opening — 1 October 2026',
 'start_date':'2026-10-01',
 'end_date':'2026-10-01',
 'all_day':True,
 'timezone':'Asia/Kolkata',
 'description':'Key Maker & Locksmith opened on 1 October 2026 on Gollahalli Main Road, Siraj Layout, Electronic City Phase 1, Bengaluru. We provide key duplication, keys for compatible cars and bikes, lock repair and replacement, and lockout assistance. The shop is open 24 hours, with on-site service across our listed areas. Visit us or contact us to confirm your key or lock requirements and a quote.',
 'cta_type':'LEARN_MORE',
 'cta_url':'https://keymaker-electronic-city.violetflame16.chatgpt.site/',
 'status':'prepared_not_published',
 'date_note':'The owner confirmed the shop opened on 1 October 2026. This is a past opening event, not a future ceremony or invented celebration. Check whether Google accepts a past event. If not, publish the factual opening announcement as an Update rather than inventing future event dates.'
}
products=[]
for item in catalog['products']:
    products.append({
       'name':item['name'],
       'category':item['category'],
       'requested_generic_price_inr':item['draft_price_inr'],
       'description':item['description'],
       'pricing_basis':'Owner explicitly requested generic reference pricing and intends to update it. These are not independently verified selling prices.',
       'status':'prepared_not_published',
       'image_note':item['photo_needed'],
       'editor_note':'The earlier form exposed a photo selector. Whether a photo is strictly required has not been validated by submission; do not falsely report it as a confirmed validation error.'
    })
queue={
 'checked_at':'2026-10-21',
 'business_name':'Key Maker & Locksmith | Electronic City',
 'google_profile_id':'15540039722934592193',
 'publication_status':'blocked_no_new_items_published',
 'blocker':'After the owner said browser use was enabled, retrying and refreshing the browser tool still returned: Local browser use is disabled in Work settings. Inventory has no accessible browsers. Windsor.ai has no available tools; the plugin directory reports installed=false in this session.',
 'owner_authorizations':['Publish multiple product listings with generic prices based on the supplied Expert Key Shop examples; owner will adjust prices.','Publish multiple factual updates.','Publish exact SPARE10 offer terms already approved on 21 October 2026.','Add an event reflecting the confirmed opening date of 1 October 2026.'],
 'products':products,
 'updates':updates['updates'],
 'offer':updates['offer'],
 'event':event,
 'existing_faq_post':{'status':faqs['status'],'post_url':faqs['post_url'],'topic_count':len(faqs['faqs']),'format':faqs['published_as']},
 'verification_before_completion':['Check current products and posts to avoid duplicates.','Submit each product and distinguish saved, pending, rejected and publicly visible states.','Publish the two updates, approved Offer and opening Event using the correct Google post type.','Verify each submission in the editor and public view; retain screenshots.','Keep all publication status fields accurate. No draft should be labelled live.']
}
(root/'PUBLISHING-QUEUE.json').write_text(json.dumps(queue,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
md='# Google publishing queue\n\nChecked 21 October 2026. **No additional products, updates, offers or events were published in this turn.**\n\n'
md+='The owner enabled browser use, but both the retry and a fresh browser-tool inventory still returned **Local browser use is disabled in Work settings**. The setting change has not reached this chat. The plugin directory also reports Windsor.ai is not installed in this session, and its tools are absent.\n\n'
md+='## Current verified publication record\n\n- All 29 service descriptions were saved and verified earlier.\n- The shop announcement and one eight-topic FAQ post were verified live earlier. Eight FAQs in one update are not eight separate posts or dedicated Q&A entries.\n- No products have been submitted. The screenshot supplied by the owner shows the empty Products introduction.\n- Two further updates and the approved offer remain unpublished.\n\n'
md+='## Six products\n\nThese are the requested generic price references, not independently verified selling prices. Exact product details and images must match the item represented.\n\n'
for p in products:
    md+='### '+p['name']+' — reference ₹'+str(p['requested_generic_price_inr'])+'\n\nCategory: '+p['category']+'\n\n'+p['description']+'\n\nImage needed: '+p['image_note']+'\n\n'
md+='The earlier product form had a photo selector; mandatory-photo validation has not been tested. No competitor image, fake stock photo or invented branded SKU was used.\n\n'
md+='## Two updates\n\n'
for u in updates['updates']:
    md+='### '+u['title']+'\n\n'+u['text']+'\n\nButton: Learn more → '+u['cta_url']+'\n\n'
o=updates['offer']
md+='## Approved offer\n\nTitle: '+o['title']+'\n\nValid: 22–31 October 2026 (India time). Coupon: SPARE10.\n\n'+o['description']+'\n\nTerms: '+o['terms']+'\n\nExact terms are already approved; no repeat approval is needed if unchanged. Recheck dates if the task resumes later.\n\n'
md+='## Opening event\n\nTitle: '+event['title']+'\n\nDate: 1 October 2026, all day, India time.\n\n'+event['description']+'\n\n'+event['date_note']+'\n\n'
md+='## Existing FAQ post\n\n[Eight-topic FAQ update]('+faqs['post_url']+') was verified LIVE earlier. It covers location, 24/7 hours, call-outs, key types, programming, lockouts, quotes and payments.\n\n'
md+='## Resume requirement\n\nThe current chat still cannot operate a local browser even after the owner reports enabling it. Reopen this chat after restarting the desktop app so the setting can be loaded again, then retry the browser inventory. Do not bypass the disabled browser setting using a different automation method.\n'
(root/'PUBLISHING-QUEUE.md').write_text(md,encoding='utf-8')
biz=json.loads((root/'business-content.json').read_text(encoding='utf-8'))
biz['opening_event_draft']=event
biz['publishing_queue']={'file':'PUBLISHING-QUEUE.json','status':queue['publication_status'],'blocker':queue['blocker'],'products':6,'new_updates':2,'approved_offers':1,'opening_events':1}
(root/'business-content.json').write_text(json.dumps(biz,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report=(root/'GMB-EXECUTION.md').read_text(encoding='utf-8')
report+='\n\n## Publication retry after user enabled browser — 21 October 2026\n\nThe owner supplied an empty Products screenshot and asked to complete multiple products, updates, FAQs and an opening event. The owner then reported local browser use was enabled. A direct retry and a fresh browser inventory still reported “Local browser use is disabled in Work settings”, with no accessible browsers. No publications occurred. The plugin directory reports Windsor.ai installed=false and no Windsor tools are exposed. All authorizations, six product references, the two updates, approved SPARE10 offer and opening-event copy are preserved in `PUBLISHING-QUEUE.md` and `PUBLISHING-QUEUE.json`.\n'
(root/'GMB-EXECUTION.md').write_text(report,encoding='utf-8')
index=(root/'index.html').read_text(encoding='utf-8')
addition='<section class="panel"><h2>Publishing is still blocked</h2><p>The owner enabled browser use, but a refreshed connection still reports that local browser use is disabled. No new products, updates, offers or events have been published.</p><p>Ready: six products with generic price references, two updates, the approved SPARE10 offer, and the 1 October opening event. The eight FAQ topics were already published in one earlier Update.</p><a class="text-link" href="PUBLISHING-QUEUE.md">Open the complete publishing queue</a></section>'
index=index.replace('<div class="content-columns">',addition+'<div class="content-columns">',1)
(root/'index.html').write_text(index,encoding='utf-8')
print(json.dumps({'queued_products':len(products),'queued_updates':len(updates['updates']),'queued_offers':1,'queued_events':1,'new_publications':0}))
