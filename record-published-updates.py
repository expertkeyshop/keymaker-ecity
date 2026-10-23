from pathlib import Path
import json,re
root=Path(__file__).parent
car='Car remote shell or a new key? A cracked casing may need a replacement shell. We replace compatible car remote bodies and make or program keys and fobs for supported vehicles. Share the make, model, year and issue so we can confirm compatibility and a quote. Visit our shop on Gollahalli Main Road, Electronic City Phase 1.'
ids={'car-remote-care':'7837872470251824866','door-lock-help':'6937526443622698449'}
proof='C:/Users/kbose/.codex/visualizations/2026/10/21/01a15ed4-019d-7e73-811d-563248a44e98/gbp-new-updates-published.png'
def update(items):
    for item in items:
        if item.get('id') not in ids: continue
        if item['id']=='car-remote-care': item['text']=car
        item.update(status='published',post_id=ids[item['id']],verified_at_local='2026-10-21 approximately 22:44 IST',verification='Google Your posts explicitly displayed Published',cta_type='NONE',cta_url='',screenshot=proof)
    return items
for name in ['PUBLISHING-QUEUE.json','updates-and-offer.json','business-content.json']:
    path=root/name
    data=json.loads(path.read_text(encoding='utf-8'))
    update(data.get('updates',data.get('additional_update_drafts',[])))
    if name=='PUBLISHING-QUEUE.json':
        data['publication_status']='in_progress_two_updates_published'
        data['blocker']=None
        data['publication_note']='Browser access is working. Both additional Updates are published; offer, event and products require their own submission/readback verification.'
    if name=='updates-and-offer.json':
        data['publication_blocker']=None
        data['publication_note']='Browser access is working. Both Updates were verified Published on 21 October 2026 at approximately 22:44 IST. Offer status is tracked separately.'
    if name=='business-content.json':
        data['updates_offer_publication_blocker']=None
        if 'publishing_queue' in data:
            data['publishing_queue']['status']='in_progress_two_updates_published'
            data['publishing_queue']['blocker']=None
            data['publishing_queue']['published_new_updates']=2
        if 'execution' in data and 'posts' in data['execution']:
            data['execution']['posts']['details']='Shop announcement, FAQ update and two further service Updates are published. The latest two were verified in Google Your posts on 21 October 2026.'
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

path=root/'PUBLISHING-QUEUE.md'
s=path.read_text(encoding='utf-8')
s=s.replace('Checked 21 October 2026. **No additional products, updates, offers or events were published in this turn.**','Checked 21 October 2026, approximately 22:44 IST. **Both additional Updates are published.** Offer, event and product submissions are tracked separately and are not marked complete here.')
s=s.replace('The owner enabled browser use, but both the retry and a fresh browser-tool inventory still returned **Local browser use is disabled in Work settings**. The setting change has not reached this chat. The plugin directory also reports Windsor.ai is not installed in this session, and its tools are absent.','Browser access is now working. Google’s Your posts screen explicitly displayed Published for the two additional Updates. Earlier browser-disabled failures remain historical attempts, not the current blocker.')
s=s.replace('- Two further updates and the approved offer remain unpublished.','- Both further Updates are published: car remote post `7837872470251824866` and door lock post `6937526443622698449`. Neither has a CTA button.\n- The approved offer, opening event and six products require separate verification; no completion is inferred from the Update results.')
a=s.index('## Two updates');b=s.index('## Approved offer',a)
door=json.loads((root/'PUBLISHING-QUEUE.json').read_text(encoding='utf-8'))['updates'][1]['text']
s=s[:a]+'## Two published Updates\n\nVerified in Google Your posts on 21 October 2026 at approximately 22:44 IST.\n\n### Car remote shell or a new key?\n\n'+car+'\n\nStatus: Published. Post ID: `7837872470251824866`. CTA: none.\n\n### Sticking key or faulty door lock?\n\n'+door+'\n\nStatus: Published. Post ID: `6937526443622698449`. CTA: none.\n\nScreenshot: `'+proof+'`.\n\n'+s[b:]
s=s.replace('## Resume requirement\n\nThe current chat still cannot operate a local browser even after the owner reports enabling it. Reopen this chat after restarting the desktop app so the setting can be loaded again, then retry the browser inventory. Do not bypass the disabled browser setting using a different automation method.','## Remaining publication checks\n\nBrowser access is restored. Verify the offer, opening event and products individually after submission; distinguish published, pending and rejected states. Do not duplicate the two Updates already published.')
path.write_text(s,encoding='utf-8')

path=root/'updates-and-offer.md'
s=path.read_text(encoding='utf-8')
s=s.replace('# Google updates and proposed offer','# Google published updates and approved offer')
s=s.replace('Prepared 21 October 2026. The two updates use confirmed shop services. The owner explicitly approved the exact offer discount, dates and terms and confirmed it will be honoured. Nothing in this document has been published yet.','Checked 21 October 2026 at approximately 22:44 IST. Both Updates use confirmed shop services and were verified Published in Google’s Your posts screen. The owner explicitly approved the exact offer discount, dates and terms and confirmed it will be honoured; offer verification is separate.')
s=s.replace('Publication is blocked because local browser use is disabled in Work settings, and Windsor.ai tools are not available in the current session. Enable local browser use, then resume. If publication is delayed, verify the offer dates are still appropriate before posting.','Browser access is working. Neither of these two published Updates has a CTA button. Screenshot: `'+proof+'`.')
a=s.index('## Update:');b=s.index('## Owner-approved offer',a)
s=s[:a]+'## Published Update: Car remote shell or a new key?\n\n'+car+'\n\nPost ID: `7837872470251824866`. Status: Published. CTA: none.\n\n## Published Update: Sticking key or faulty door lock?\n\n'+door+'\n\nPost ID: `6937526443622698449`. Status: Published. CTA: none.\n\n'+s[b:]
path.write_text(s,encoding='utf-8')

path=root/'GMB-EXECUTION.md'
s=path.read_text(encoding='utf-8')
if '## Two additional Updates verified Published' not in s:
    s+='\n## Two additional Updates verified Published — 21 October 2026\n\nBrowser access is restored. Google’s Your posts screen explicitly showed Published for both additional Updates at approximately 22:44 IST:\n\n- Car remote shell or a new key? Post ID `7837872470251824866`. The actual published text is the shortened version recorded in `PUBLISHING-QUEUE.json`.\n- Sticking key or faulty door lock? Post ID `6937526443622698449`. Text matches the prepared queue.\n\nNeither Update has a CTA button. Screenshot: `'+proof+'`. Earlier paragraphs describing browser-disabled attempts are historical; they no longer describe current access. Offer submission was in progress when this record was written; event and product status must be verified separately. No offer, event or product is marked complete based on these two Updates.\n'
path.write_text(s,encoding='utf-8')

path=root/'app.js'
s=path.read_text(encoding='utf-8')
pattern=r'(  const execution = )(\{[^\n]+\})(;)'
m=re.search(pattern,s)
if m:
    data=json.loads(m.group(2))
    data['posts']['summary']='Shop announcement, FAQ update and two additional service Updates are published.'
    data['posts']['steps']=['The original shop announcement and FAQ update were verified earlier.','On 21 October 2026 at approximately 22:44 IST, Google Your posts showed both the car remote and door lock Updates as Published.','The two latest Updates have no CTA button. Their post IDs and exact text are recorded in PUBLISHING-QUEUE.json.','Offer, event and product publication status is tracked separately; do not duplicate these Updates.']
    s=s[:m.start(2)]+json.dumps(data,ensure_ascii=False)+s[m.end(2):]
path.write_text(s,encoding='utf-8')

path=root/'index.html'
s=path.read_text(encoding='utf-8')
s=s.replace('The shop announcement and an eight-topic FAQ update are published.','The shop announcement, an eight-topic FAQ update and two further service Updates are published.')
s=s.replace('<h2>Publishing is still blocked</h2><p>The owner enabled browser use, but a refreshed connection still reports that local browser use is disabled. No new products, updates, offers or events have been published.</p><p>Ready: six products with generic price references, two updates, the approved SPARE10 offer, and the 1 October opening event. The eight FAQ topics were already published in one earlier Update.</p>','<h2>Two more Updates are published</h2><p>Browser access is working. The car remote and door lock Updates were verified Published in Google on 21 October 2026 at approximately 22:44 IST. Neither has a CTA button.</p><p>Offer, opening event and product publication checks remain separate. The eight FAQ topics were already published in one earlier Update.</p>')
s=s.replace('<p>Ready to publish. No new update or offer from this batch is live yet.</p></div><span class="pill neutral">Browser access needed</span>','<p>Both service Updates are published. The approved offer is tracked separately.</p></div><span class="pill">Updates published</span>')
s=s.replace('<p>Local browser use is disabled in Work settings. Re-enable it and resume publishing.</p>','<p>Browser access is restored. Google showed both Updates as Published; offer publication is being verified separately.</p>')
path.write_text(s,encoding='utf-8')
print('Updated the two published Update records in seven status/content files; offer, event and product objects preserved.')
