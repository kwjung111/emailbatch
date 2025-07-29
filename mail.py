import email
import smtplib
import re
from email.mime.text import MIMEText
from imapclient import IMAPClient
from config import *
from logger import get_logger
from email.header import decode_header
from batch_info import BatchInfo,BatchStatus

logger = get_logger(__name__)

def poll_mail():
    with IMAPClient(HOST, ssl=True) as client:
        client.login(USER,PASS)
        client.select_folder('INBOX')
        
        uids = client.search(['UNSEEN'])
        if uids:
            #lates_uid = max(uids)
            response = client.fetch(uids,['RFC822'])
            for uid, data in response.items():
                msg = email.message_from_bytes(data[b'RFC822'])
                sub, enc = decode_header(msg['Subject'])[0]
                subject=  sub.decode(enc or 'utf-8') if isinstance(sub,bytes) else sub
             
                logger.info(f"New mail : {subject}")
                #메세지 파싱
                batch_info = parse_subject(subject)
                if batch_info.check():
                    logger.info(f"===Starting new job===")
                    #client.add_flags(uid,[r'\Seen'])
                    #client.add_flags(uid,[r'\Deleted'])
                    #merge_excels_preserve(INPUT_DIR,OUTPUT_DIR)
                    #client.expunge()
                    send("batch",batch_info.status.value)

def parse_subject(subject : str) -> BatchInfo:
    matches = re.findall(r'\[(.*?)\]', subject)
    if matches and len(matches) == 3:
        job_name, status, timestamp = matches
        batch_status = BatchStatus.from_str(status)
        batch = BatchInfo(job_name,batch_status,timestamp)
        logger.info(f"Batch status : {batch.__str__()}")
        return batch
    else:
        logger.info(f"{subject} : Not a Batch trigger")
        return None
    
def send(content,status):
    gmail_smtp="smtp.gmail.com"
    gmail_port=465
    
    smtp = smtplib.SMTP_SSL(gmail_smtp,gmail_port)
    smtp.login(USER,PASS)
    
    msg = MIMEText(content,'html')
    msg['Subject'] = f"[{status}] : loc sms"
    
    for rcv in RECV:
        smtp.sendmail(USER,rcv,msg.as_string())
    smtp.quit()
    
if __name__=="__main__":
    content= "aa"
    send(content,"success")
    