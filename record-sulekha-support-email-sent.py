from pathlib import Path
from email.parser import BytesParser
from email.policy import SMTP
import json,re
r=Path(__file__).parent
recipient='care@sulekha.com';subject='Sulekha profile help: locksmith services, attributes and public page';gid='redacted-private-message-id'
msg=BytesParser(policy=SMTP).parsebytes((r/'SULEKHA-SUPPORT-EMAIL.eml').read_bytes())
body=msg.get_content().replace('\r\n','\n');assert len(body.split())==201
assert msg['From'] is None
msg['X-Local-Support-Status']='Sent; separately verified Gmail SENT label'
msg['X-Local-Sent-Date']='2026-10-22'
msg['X-Gmail-Internal-Message-Id']=gid
(r/'SULEKHA-SUPPORT-EMAIL.eml').write_bytes(msg.as_bytes())
check=BytesParser(policy=SMTP).parsebytes((r/'SULEKHA-SUPPORT-EMAIL.eml').read_bytes());assert check['From'] is None;assert check.get_content().replace('\r\n','\n')==body
(r/'SULEKHA-SUPPORT-EMAIL.txt').write_text('Status: SENT — verified via a separate Gmail metadata read with the SENT label\nSent date: 22 October 2026 (user date, Asia/Calcutta)\nGmail message/thread ID: '+gid+'\nRecord of an email already sent. Do not send again.\nTo: '+recipient+'\nSubject: '+subject+'\n\n'+body,encoding='utf-8')
record={'file':'SULEKHA-SUPPORT-DRAFT.md','text_file':'SULEKHA-SUPPORT-EMAIL.txt','email_file':'SULEKHA-SUPPORT-EMAIL.eml','status':'sent','recipient':recipient,'subject':subject,'body_word_count':201,'owner_authorized_purpose':'Owner requested Sulekha profile support by email instead of WhatsApp','email_sent':True,'whatsapp_sent':False,'sent_at_date':'2026-10-22','date_timezone':'Asia/Calcutta','gmail_message_id':gid,'gmail_thread_id':gid,'gmail_internal_date_ms':1792685113000,'verification':{'method':'Separate read_email metadata readback','gmail_label':'SENT','recipient_verified':True,'subject_verified':True},'sender_private_details_persisted':False,'note':'Do not send again or create an automation. Sender name/address are deliberately not copied into business records.'}
for f in ['business-content.json','DIRECTORY-LISTING-DRAFTS.json']:
 p=r/f;d=json.loads(p.read_text(encoding='utf-8'));d['support_issue_draft']=record
 su=d['directory_listings']['platforms']['Sulekha'] if f=='business-content.json' else d['platforms']['Sulekha']
 su['support_issue_draft']=record;su['support_email_sent']=True;su['whatsapp_sent']=False;su['customer_contact_messages_sent']=False;su['outbound_messages_sent']=True;su['outbound_message_note']='Only the explicitly owner-authorized support email to care@sulekha.com was sent. No WhatsApp or customer-contact message was sent.'
 p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
md=['# Sulekha support email — sent and verified','','Status: **sent**. Sent on **22 October 2026**, using the user date in Asia/Calcutta. A separate Gmail metadata read confirmed the SENT label, recipient and exact subject. This is a sent-message record; do not send it again. No WhatsApp message was sent.','','To: '+recipient,'','Subject: '+subject,'','Gmail message/thread ID: `'+gid+'`. Gmail internal date: `1792685113000` milliseconds. Sender private name/address were not copied into these business records.','','## Email body — unchanged','',body,'','## Local files','','- `SULEKHA-SUPPORT-EMAIL.txt`: sent status plus unchanged body.','- `SULEKHA-SUPPORT-EMAIL.eml`: original body retained, with local sent-record metadata; no invented From header.','','The directory task remains open: public profile and structured address/service/attribute issues are not resolved by sending the email. Checklist stays16/18. No automation was created.']
(r/'SULEKHA-SUPPORT-DRAFT.md').write_text('\n'.join(md)+'\n',encoding='utf-8')

p=r/'app.js';s=p.read_text(encoding='utf-8');m=re.search(r'  const execution = (\{[^\n]+\});',s);assert m;ex=json.loads(m.group(1))
ex['consistency']['steps'][-1]='Directory UI completeness scores are platform measures, not SEO ranking. The owner-authorized email to care@sulekha.com was sent on 22 October and separately verified with Gmail SENT metadata. No WhatsApp message, paid plan or invented private field was used. Public directory verification remains open.'
s=s[:m.start(1)]+json.dumps(ex,ensure_ascii=False)+s[m.end(1):];p.write_text(s,encoding='utf-8');assert sum(v['complete'] for v in ex.values())==16

p=r/'GMB-EXECUTION.md';s=p.read_text(encoding='utf-8');a=s.index('## Current checklist:');z=s.index('## Links and assets',a);parts=['## Current checklist: 16 of 18 completed or reviewed','']
for k,v in ex.items():parts += [('✓' if v['complete'] else '−')+' **'+k.title()+': '+v['status']+'**',v['summary'],*['- '+t for t in v['steps']],'']
s=s[:a]+'\n'.join(parts)+s[z:]
s+='\n## Sulekha support email sent and verified — 22 October 2026\n\nThe owner-authorized email was sent to care@sulekha.com with subject “'+subject+'”. A separate read_email metadata read confirmed the Gmail SENT label, recipient and exact subject. Message/thread ID `'+gid+'`; internal date1792685113000 milliseconds. Sender private name/address were not copied into business records. The201-word local body is unchanged. No WhatsApp message was sent and no automation was created. Status: sent. Do not send again. Directory public/service/attribute issues remain open; checklist stays16/18.\n';p.write_text(s,encoding='utf-8')
p=r/'DIRECTORY-LISTING-DRAFTS.md';s=p.read_text(encoding='utf-8');s+='\n## Support email sent — 22 October 2026\n\nEmail to care@sulekha.com was sent and separately verified with the Gmail SENT label. Subject: '+subject+'. Message/thread ID: `'+gid+'`. The body in SULEKHA-SUPPORT-EMAIL.txt/.eml remains unchanged. Sender private details were not stored. No WhatsApp message was sent. Do not send again; no automation was created. Public listing and service/attribute issues are still open, so checklist remains16/18.\n';p.write_text(s,encoding='utf-8')
p=r/'index.html';s=p.read_text(encoding='utf-8');s=s.replace('Directory completion remains open.','Directory completion remains open. The owner-authorized Sulekha support email was sent and verified on 22 October; no WhatsApp message was sent.',1);p.write_text(s,encoding='utf-8')
for f in ['business-content.json','DIRECTORY-LISTING-DRAFTS.json','PUBLISHING-QUEUE.json']:json.loads((r/f).read_text(encoding='utf-8'))
print('Support status sent, Gmail SENT metadata recorded. Body unchanged201words; no sender details/WhatsApp/automation.16/18;3JSONvalid.')
