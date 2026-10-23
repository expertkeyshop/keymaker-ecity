from pathlib import Path
from email.message import EmailMessage
from email.policy import SMTP
from email.parser import BytesParser
import json
r=Path(__file__).parent
recipient='care@sulekha.com'
subject='Sulekha profile help: locksmith services, attributes and public page'
body='''Hello Sulekha Support,

Please help resolve the service and attribute setup for our existing registered profile and confirm whether its free public listing is live.

Business: Key Maker & Locksmith | Electronic City
Registered phone: +91 97623 06303
Shop address: Gollahalli Main Road, Siraj Layout, Electronic City Phase 1, Bengaluru, Karnataka 560100.

The Services page lists Key Maker & Locksmiths. Its details show “No needs available for this service”. We selected “Additional info” in the existing service’s Edit screen and submitted it, but after reloading it still says “No information added yet”.

The attributes editor says “Add services first” despite the saved locksmith mapping. It shows 0 of 11 attributes, with 3 required attributes missing. Please check the mapping and make the applicable service details and attributes available.

The structured location currently shows Electronic City Phase I; the full street address is in About. Please identify or enable the street-address and map editor so we can verify the actual shop location.

Please also confirm publication status and provide the working public profile URL; the dashboard’s Share option has not exposed one. Please preserve our existing profile and accurate category without adding unrelated categories, duplicate registrations or a paid package.

Thank you.
'''
count=len(body.split());assert 180<=count<=230,count
(r/'SULEKHA-SUPPORT-EMAIL.txt').write_text('To: '+recipient+'\nSubject: '+subject+'\n\n'+body,encoding='utf-8')
msg=EmailMessage(policy=SMTP);msg['To']=recipient;msg['Subject']=subject;msg.set_content(body,charset='utf-8')
(r/'SULEKHA-SUPPORT-EMAIL.eml').write_bytes(msg.as_bytes())
check=BytesParser(policy=SMTP).parsebytes((r/'SULEKHA-SUPPORT-EMAIL.eml').read_bytes())
assert check['From'] is None
assert str(check['To'])==recipient
assert check.get_content().replace('\r\n','\n')==body
status={'file':'SULEKHA-SUPPORT-DRAFT.md','text_file':'SULEKHA-SUPPORT-EMAIL.txt','email_file':'SULEKHA-SUPPORT-EMAIL.eml','status':'approved_email_unsent','recipient':recipient,'subject':subject,'body_word_count':count,'owner_authorized_purpose':'Owner requested support by email instead of WhatsApp','sender_address':None,'email_sent':False,'whatsapp_sent':False,'sent_at':None}
for f in ['business-content.json','DIRECTORY-LISTING-DRAFTS.json']:
 p=r/f;d=json.loads(p.read_text(encoding='utf-8'))
 if f=='business-content.json':d['directory_listings']['platforms']['Sulekha']['support_issue_draft']=status
 else:d['platforms']['Sulekha']['support_issue_draft']=status
 d['support_issue_draft']=status
 p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
md=['# Owner-approved Sulekha support email — not sent','','Status: **approved_email_unsent**. Prepared22 October2026. The owner requested email instead of WhatsApp. No email or WhatsApp message has been sent. Sender address is not supplied or invented.','','To: '+recipient,'','Subject: '+subject,'',body,'','## Prepared files','','- `SULEKHA-SUPPORT-EMAIL.txt`: readable recipient, subject and body.','- `SULEKHA-SUPPORT-EMAIL.eml`: email draft with To and Subject; no invented From header.','','Body length: '+str(count)+' words. Includes only public business identification and the observed profile issues; no KYC documents, bank information, private email, GST number or invented legal/contact name.','','Official support recipient was observed in Sulekha’s signed-in Help and support screen. This remains an unsent local draft; account/tool sending is handled separately.']
(r/'SULEKHA-SUPPORT-DRAFT.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
for f in ['DIRECTORY-LISTING-DRAFTS.md','GMB-EXECUTION.md']:
 p=r/f;s=p.read_text(encoding='utf-8');s+='\n## Support email prepared, not sent — 22 October2026\n\nThe owner requested email support instead of WhatsApp. An email to care@sulekha.com was prepared as SULEKHA-SUPPORT-EMAIL.txt and .eml, with no invented From address. Status: approved_email_unsent. It covers the verified post-reload service-detail failure,0/11 attributes with3 required missing, structured street/map access and public profile URL. Body length:'+str(count)+' words. No email or WhatsApp message has been sent. Directory task and checklist16/18 remain unchanged.\n';p.write_text(s,encoding='utf-8')
for f in ['business-content.json','DIRECTORY-LISTING-DRAFTS.json']:json.loads((r/f).read_text(encoding='utf-8'))
print(json.dumps({'recipient':recipient,'body_words':count,'from_header_present':False,'status':'approved_email_unsent','email_sent':False,'whatsapp_sent':False,'files':['SULEKHA-SUPPORT-EMAIL.txt','SULEKHA-SUPPORT-EMAIL.eml']}))
