import os
import smtplib
# for sending attachments
from email import message
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename


def get_data():
        
    # constants
    FROM = 'buzzsky786@gmail.com'
    TO = 'ahmedfahad3596@gmail.com'
    PASS = os.environ['intruder']           # ojch couz gidg lhpo
    SUBJECT = 'Does attachment send?'
    BODY = """
    In this mail we are testing to send message
    along with attachments

    Regards,
    Fahad
    """
    
    return FROM, TO, PASS, SUBJECT, BODY

def get_message_obj(attachment_file):
    
    FROM, TO, _, SUBJECT, BODY = get_data()

    # create the message object
    msg = MIMEMultipart()
    msg['From'] = FROM
    msg['To'] = TO
    msg['Subject'] = SUBJECT
    body = MIMEText(BODY, 'plain')
    msg.attach(body)
    
    # add attachment
    filename = attachment_file
    with open(filename, 'rb') as f:
        attachment = MIMEApplication(f.read(), Name=basename(filename))
        attachment['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
        msg.attach(attachment)
        
    return msg

def send_mail(attachment_file_name):
    
    FROM, TO, PASS, _, _ = get_data()
    msg = get_message_obj(attachment_file_name)

    # 1. start the server
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # 2. smtp server setup
    status_code, response = server.ehlo()
    print(f'[*] Echoing the server: {status_code} {response}')

    # 3. setting the secured TLS connection
    status_code, response = server.starttls()
    print(f'[*] Starting TLS server: {status_code} {response}')

    # 4. login to senders' mail
    status_code, response = server.login(FROM, PASS)
    print(f'[*] Logingin in...: {status_code} {response}')

    # 5. sending mail
    server.send_message(msg, FROM, [TO])
    server.quit()

    print("Mail Sent!!")
    
    
send_mail('BERT.png')