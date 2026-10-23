from pathlib import Path
import json,re
root=Path(__file__).parent
proof='C:/Users/kbose/.codex/visualizations/2026/10/21/01a15ed4-019d-7e73-811d-563248a44e98/gbp-all-new-posts-published.png'
for name in ['PUBLISHING-QUEUE.json','business-content.json']:
    p=root/name;d=json.loads(p.read_text(encoding='utf-8'));e=d['event'] if name=='PUBLISHING-QUEUE.json' else d['opening_event_draft']
    f=e['fallback_opening_update'];f.update(status='published',verified_at_local='2026-10-22',verification='Fresh Google Your posts view displayed Published 13 minutes ago',screenshot=proof)
    if name=='PUBLISHING-QUEUE.json':
        d['publication_note']='Both service Updates, SPARE10 Offer and factual opening Update fallback are verified Published. A past-date Event remains unavailable. Products are blocked by confirmed missing-photo validation; 0 products published.'
    else:
        d['publishing_queue']['opening_update_status']='published'
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

p=root/'PUBLISHING-QUEUE.md';s=p.read_text(encoding='utf-8')
s=s.replace('A factual opening Update fallback is Pending review;','The factual opening Update fallback is now Published;')
s=s.replace('Fallback Update ID: `6401196171407182369`. Status: **Pending**; Google displayed “Post submitted for review”. No CTA button. Do not mark this Published until readback verifies it.','Fallback Update ID: `6401196171407182369`. Status: **Published**, verified 22 October 2026 when Google Your posts displayed “Published 13 minutes ago”. It had initially been Pending review. No CTA button. Screenshot: `'+proof+'`.')
s=s.replace('Recheck the Pending opening Update and submit/verify products individually; distinguish published, pending and rejected states.','The opening Update is verified Published. Supply the six actual product photos, then submit/verify products individually; distinguish published, pending and rejected states.')
p.write_text(s,encoding='utf-8')

p=root/'GMB-EXECUTION.md';s=p.read_text(encoding='utf-8')
s=s.replace('## Opening announcement submitted for review — 22 October 2026','## Historical opening announcement submission — 22 October 2026')
if '## Opening Update verified Published' not in s:
    s+='\n## Opening Update verified Published — 22 October 2026\n\nA fresh Google Your posts view displayed **Published 13 minutes ago** for opening Update `6401196171407182369`, replacing the earlier Pending state. The content still states the actual opening date of 1 October 2026; no future ceremony or opening date was invented. It has no CTA button. The separate past-date Event remains unavailable in the editor. Screenshot: `'+proof+'`. Products remain blocked_missing_product_photos, with zero products published.\n'
p.write_text(s,encoding='utf-8')

p=root/'index.html';s=p.read_text(encoding='utf-8')
s=s.replace('The factual opening Update is Pending review because Google’s calendar would not accept the past Event date.','The factual opening Update is now verified Published. It states the real 1 October opening date; Google’s calendar would not accept a past Event.')
s=s.replace('The opening Update fallback is Pending review;','The opening Update fallback is verified Published;')
p.write_text(s,encoding='utf-8')

p=root/'app.js';s=p.read_text(encoding='utf-8');m=re.search(r'  const execution = (\{[^\n]+\});',s);assert m
d=json.loads(m.group(1));d['posts']['summary']='Shop announcement, FAQ update, two service Updates, SPARE10 Offer and opening Update are published.'
d['posts']['steps']=['The shop announcement and FAQ update were verified earlier.','The car remote and door lock Updates were verified Published on 21 October; the approved SPARE10 Offer is also Published.','A fresh 22 October view showed the opening announcement Update as Published. It correctly states the real opening date of 1 October 2026; the past-date Event form was unavailable.','The latest two service Updates and opening Update have no CTA. Products remain separately blocked by missing required photos; do not duplicate the published posts.']
s=s[:m.start(1)]+json.dumps(d,ensure_ascii=False)+s[m.end(1):];p.write_text(s,encoding='utf-8')
for name in ['PUBLISHING-QUEUE.json','business-content.json','service-product-drafts.json','updates-and-offer.json']:json.loads((root/name).read_text(encoding='utf-8'))
print('Four JSON files parsed. Opening fallback Published; Event unavailable; six product statuses and prices preserved.')
