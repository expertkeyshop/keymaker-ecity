from pathlib import Path
import json
root=Path(__file__).parent
for name in ['PUBLISHING-QUEUE.json','business-content.json']:
    p=root/name;d=json.loads(p.read_text(encoding='utf-8'))
    e=d['event'] if name=='PUBLISHING-QUEUE.json' else d['opening_event_draft']
    e['status']='event_unavailable_past_date'
    e['date_note']='The shop opening date remains 1 October 2026. Google’s end-date calendar disabled dates before 22 October 2026, so the one-day past Event could not be created. No future opening date was invented.'
    e['fallback_opening_update']={'post_id':'6401196171407182369','status':'pending','verified_at_local':'2026-10-22','verification':'Google Your posts displayed Pending and Post submitted for review','text':e['description'],'cta_type':'NONE','cta_url':''}
    if name=='PUBLISHING-QUEUE.json':
        d['publication_note']='Both additional Updates and SPARE10 Offer are verified Published. The past-date opening Event is unavailable; the factual opening Update fallback is Pending review. Products require individual submission/readback verification.'
    if name=='business-content.json':
        d['publishing_queue']['opening_event_status']='event_unavailable_past_date'
        d['publishing_queue']['opening_update_status']='pending'
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=root/'PUBLISHING-QUEUE.md';s=p.read_text(encoding='utf-8')
s=s.replace('The opening event and six products require separate verification; no completion is inferred from post results.','The one-day past opening Event is unavailable in Google’s date picker. A factual opening Update fallback is Pending review; six products require individual verification.')
s=s.replace('The owner confirmed the shop opened on 1 October 2026. This is a past opening event, not a future ceremony or invented celebration. Check whether Google accepts a past event. If not, publish the factual opening announcement as an Update rather than inventing future event dates.','The owner-confirmed opening date remains 1 October 2026. On 22 October, Google’s end-date calendar disabled dates before 22 October 2026; the one-day past Event could not be created. The same factual description was submitted as an Update instead, without inventing future event dates.\n\nFallback Update ID: `6401196171407182369`. Status: **Pending**; Google displayed “Post submitted for review”. No CTA button. Do not mark this Published until readback verifies it.')
s=s.replace('Verify the opening event and products individually after submission; distinguish published, pending and rejected states.','Recheck the Pending opening Update and submit/verify products individually; distinguish published, pending and rejected states.')
p.write_text(s,encoding='utf-8')
p=root/'GMB-EXECUTION.md';s=p.read_text(encoding='utf-8')
if '## Opening announcement submitted for review' not in s:
    s+='\n## Opening announcement submitted for review — 22 October 2026\n\nThe actual opening date remains 1 October 2026. Google’s Event end-date picker disabled dates before 22 October 2026, preventing creation of the one-day past opening Event. The same factual description was submitted as an Update instead. Post ID `6401196171407182369`; Google Your posts explicitly showed Pending and “Post submitted for review”. It has no CTA button. This is not yet marked Published. No future ceremony or opening date was invented.\n'
p.write_text(s,encoding='utf-8')
p=root/'index.html';s=p.read_text(encoding='utf-8')
s=s.replace('Opening event and product publication checks remain separate.','The factual opening Update is Pending review because Google’s calendar would not accept the past Event date. Products require their own publication checks.')
s=s.replace('Event and product submissions are tracked separately.','The opening Update fallback is Pending review; products remain separately tracked.')
p.write_text(s,encoding='utf-8')
print('Recorded past-date Event limitation and Pending fallback Update; publication is not assumed.')
