from pathlib import Path
import json,re
r=Path(__file__).parent
company='Freelance - GST Unregistered'
range_value='11-25'
fact={'value':company,'owner_confirmed':True,'confirmed_at':'2026-10-22','source':'Owner confirmed current Sulekha UI values','supersedes':'Earlier Sole Proprietorship confirmation','agent_changed_current_value':False}
employees={'value':range_value,'owner_confirmed':True,'confirmed_at':'2026-10-22','source':'Owner confirmed current Sulekha UI values','agent_invented_or_changed':False}
p=r/'business-content.json';b=json.loads(p.read_text(encoding='utf-8'));b['company_type']=fact;b['employee_range']=employees
su=b['directory_listings']['platforms']['Sulekha'];su['company_type']=fact;su['employee_range']=employees
su['current_verification_summary']={'verified_items':1,'total_items':3,'bank_verification':'pending','business_verification':'pending','source':'Current Sulekha UI / owner observation','observed_at':'2026-10-22','agent_submitted_verification_documents_or_bank_details':False,'note':'Only the minimal status is recorded; no document or bank information is copied.'}
su['support_issue_draft']={'file':'SULEKHA-SUPPORT-DRAFT.md','status':'draft_not_sent'}
p.write_text(json.dumps(b,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
p=r/'DIRECTORY-LISTING-DRAFTS.json';d=json.loads(p.read_text(encoding='utf-8'));d['company_type']=fact;d['employee_range']=employees;d['platforms']['Sulekha']=su;d['support_issue_draft']={'file':'SULEKHA-SUPPORT-DRAFT.md','status':'draft_not_sent'};p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

support='''# Sulekha service/attribute issue — internal draft, not sent

Prepared 22 October 2026. Do not send without the owner's instruction. No support message or enquiry has been submitted.

Subject: Help checking Key Maker & Locksmiths service mapping and profile attributes

Hello Sulekha Support,

Please help check the service mapping and available business attributes for our registered business:

- Business: Key Maker & Locksmith | Electronic City
- Registered business phone: +91 97623 06303
- Area/city: Electronic City Phase I, Bangalore
- Signed-in owner profile: https://www.sulekha.com/business/profile

The Services page shows one saved service, Key Maker & Locksmiths. Its category details previously showed “No needs available for this service”. The existing mapped service's Edit screen now exposes “Additional info”; this was selected and Submit clicked, but a fresh saved readback is not yet confirmed.

The business attribute editor still displays “Add services first”. Please check which service details and attributes apply to the Key Maker & Locksmiths category and whether an additional configuration step is needed. We are not assuming a cause for the conflicting prompts.

Please also help us locate and verify the public profile URL. The owner profile has saved business information, website, hours, payments, service mapping and business images, but Share has not exposed a public page URL in the observed workflow.

Please preserve the accurate locksmith category and existing profile. We do not want unrelated categories, duplicate registrations or a paid package added to address this issue.

Thank you.

## Reference and current scope

Official help: https://www.sulekha.com/local-services/business-owners/business/faq

This is a local draft only. It includes no KYC document, bank details, private email, GST number or invented legal/contact name. Current service-edit and attribute results must be updated before sending if the next readback resolves or changes them.
'''
(r/'SULEKHA-SUPPORT-DRAFT.md').write_text(support,encoding='utf-8')

p=r/'app.js';s=p.read_text(encoding='utf-8');m=re.search(r'  const execution = (\{[^\n]+\});',s);assert m;ex=json.loads(m.group(1))
steps=ex['consistency']['steps']
steps[0]='Sulekha About, website, payments, all seven 24-hour days, 2026, service mapping, cover/logo and three gallery photos were saved. The owner confirmed current company type Freelance - GST Unregistered and employee range 11–25 on 22 October; this supersedes the earlier Sole Proprietorship answer.'
ex['consistency']['steps']=steps
s=s[:m.start(1)]+json.dumps(ex,ensure_ascii=False)+s[m.end(1):];p.write_text(s,encoding='utf-8');assert sum(v['complete'] for v in ex.values())==16

p=r/'DIRECTORY-LISTING-DRAFTS.md';s=p.read_text(encoding='utf-8')
s=s.replace('## Shared business details\n','## Shared business details\n\nCurrent owner-confirmed company type: **Freelance - GST Unregistered**. Employee range: **11–25**. Confirmed 22 October 2026; these current values supersede the earlier Sole Proprietorship answer.\n',1)
s+='\n## Current company and headcount confirmation — 22 October 2026\n\nThe owner confirmed that the current Sulekha values are correct: Freelance - GST Unregistered and 11–25 employees. The earlier Sole Proprietorship confirmation is superseded; the agent did not restore or invent these current values. Minimal current verification status is1/3 verified, with bank and business verification pending; no verification documents or bank details were submitted by the agent.\n\n`SULEKHA-SUPPORT-DRAFT.md` is an internal draft only and has not been sent. Service/attribute editing results are held until fresh saved readback.\n';p.write_text(s,encoding='utf-8')
p=r/'GMB-EXECUTION.md';s=p.read_text(encoding='utf-8');a=s.index('## Current checklist:');z=s.index('## Links and assets',a);parts=['## Current checklist: 16 of 18 completed or reviewed','']
for k,v in ex.items():parts += [('✓' if v['complete'] else '−')+' **'+k.title()+': '+v['status']+'**',v['summary'],*['- '+t for t in v['steps']],'']
s=s[:a]+'\n'.join(parts)+s[z:]
s+='\n## Current company/headcount owner confirmation — 22 October 2026\n\nThe owner confirmed the current Sulekha company type **Freelance - GST Unregistered** and employee range **11–25**. These supersede the earlier Sole Proprietorship answer. No restoration or new external field change is claimed by this local record update. Current minimal verification summary is1/3 verified, bank and business pending; the agent did not submit documents or bank details.\n\nAn unsent issue draft was prepared at `SULEKHA-SUPPORT-DRAFT.md` for the service/attribute prompts. It does not assert a cause. The latest Additional info Submit result is not yet marked saved/readback-verified; service and attribute state remains unchanged pending browser results. Checklist remains16/18.\n';p.write_text(s,encoding='utf-8')
p=r/'README.md';s=p.read_text(encoding='utf-8');s+='\nCurrent owner-confirmed company type is Freelance - GST Unregistered, employee range11–25 (22 October2026), superseding the earlier Sole Proprietorship answer. SULEKHA-SUPPORT-DRAFT.md is local and unsent. Latest service/attribute changes await readback; checklist16/18.\n';p.write_text(s,encoding='utf-8')
for f in ['business-content.json','DIRECTORY-LISTING-DRAFTS.json','PUBLISHING-QUEUE.json']:json.loads((r/f).read_text(encoding='utf-8'))
print('Owner-confirmed current company/headcount recorded; support draft unsent; service/attribute status unchanged.16/18;3JSONvalid.')
