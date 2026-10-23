from pathlib import Path
import json
root=Path(__file__).parent
proof='C:/Users/kbose/.codex/visualizations/2026/10/21/01a15ed4-019d-7e73-811d-563248a44e98/gbp-offer-published.png'
for name in ['PUBLISHING-QUEUE.json','updates-and-offer.json','business-content.json']:
    p=root/name; data=json.loads(p.read_text(encoding='utf-8'))
    obj=data['approved_offer'] if name=='business-content.json' else data['offer']
    obj.update(status='published',post_id='8812472286834001751',verified_at_local='2026-10-21',verification='Google Your posts explicitly displayed Published 27 seconds ago',screenshot=proof)
    if name=='PUBLISHING-QUEUE.json':
        data['publication_status']='in_progress_two_updates_and_offer_published'
        data['publication_note']='Browser access is working. Both additional Updates and SPARE10 Offer are verified Published; event and products require their own submission/readback verification.'
    if name=='updates-and-offer.json':
        data['publication_note']='Both Updates and the approved SPARE10 Offer were verified Published in Google Your posts on 21 October 2026.'
    if name=='business-content.json':
        data['publishing_queue']['status']='in_progress_two_updates_and_offer_published'
        data['publishing_queue']['published_approved_offers']=1
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

p=root/'PUBLISHING-QUEUE.md';s=p.read_text(encoding='utf-8')
s=s.replace('**Both additional Updates are published.** Offer, event and product submissions are tracked separately and are not marked complete here.','**Both additional Updates and the approved SPARE10 Offer are published.** Event and product submissions remain separately tracked.')
s=s.replace('- The approved offer, opening event and six products require separate verification; no completion is inferred from the Update results.','- The approved SPARE10 Offer is Published, post ID `8812472286834001751`; dates and terms match owner approval.\n- The opening event and six products require separate verification; no completion is inferred from post results.')
s=s.replace('## Approved offer\n','## Approved offer — Published\n\nGoogle Your posts displayed Published 27 seconds ago on 21 October 2026. Post ID: `8812472286834001751`. Screenshot: `'+proof+'`.\n',1)
s=s.replace('Verify the offer, opening event and products individually after submission; distinguish published, pending and rejected states. Do not duplicate the two Updates already published.','Verify the opening event and products individually after submission; distinguish published, pending and rejected states. Do not duplicate the two Updates or SPARE10 Offer already published.')
p.write_text(s,encoding='utf-8')

p=root/'updates-and-offer.md';s=p.read_text(encoding='utf-8')
s=s.replace('offer verification is separate.','the exact SPARE10 Offer was subsequently verified Published.')
s=s.replace('## Owner-approved offer — not published','## Owner-approved offer — Published\n\nGoogle Your posts displayed Published 27 seconds ago on 21 October 2026. Post ID: `8812472286834001751`. Screenshot: `'+proof+'`.')
s=s.replace('It has not yet been promised publicly because no post was submitted.','The exact approved offer is now published.')
p.write_text(s,encoding='utf-8')

p=root/'GMB-EXECUTION.md';s=p.read_text(encoding='utf-8')
s=s.replace('## Two further updates and approved offer — 21 October 2026','## Historical preparation of two further updates and offer — 21 October 2026')
s=s.replace('## Publication retry after user enabled browser — 21 October 2026','## Historical publication retry after user enabled browser — 21 October 2026')
if '## SPARE10 Offer verified Published' not in s:
    s+='\n## SPARE10 Offer verified Published — 21 October 2026\n\nGoogle Your posts explicitly displayed Published 27 seconds ago for the exact approved offer. Post ID: `8812472286834001751`. Coupon SPARE10; 22–31 October 2026, 00:00–23:59 India time; 10% off eligible in-shop ordinary mechanical edge-cut house-key duplication, capped at ₹100 per order. The approved exclusions and full terms are preserved unchanged in `PUBLISHING-QUEUE.json` and `updates-and-offer.json`. Screenshot: `'+proof+'`. The opening event and products still require individual verification.\n'
p.write_text(s,encoding='utf-8')

p=root/'index.html';s=p.read_text(encoding='utf-8')
s=s.replace('<h2>Two more Updates are published</h2>','<h2>Two more Updates and your offer are published</h2>')
s=s.replace('<p>Offer, opening event and product publication checks remain separate.','<p>The approved SPARE10 Offer is also verified Published. Opening event and product publication checks remain separate.')
s=s.replace('Both service Updates are published. The approved offer is tracked separately.','Both service Updates and the approved SPARE10 Offer are published.')
s=s.replace('<span class="pill">Updates published</span>','<span class="pill">Updates and offer published</span>')
s=s.replace('Google showed both Updates as Published; offer publication is being verified separately.','Google showed both Updates and the SPARE10 Offer as Published. Event and product submissions are tracked separately.')
p.write_text(s,encoding='utf-8')
print('Recorded two published Updates and exact published SPARE10 Offer; event/product state remains pending.')
