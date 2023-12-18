import smtplib
from email import message

# constants
FROM = 'buzzsky786@gmail.com'
TO = 'ahmedfahad3596@gmail.com'
PASS = 'ubpz ucgx irad trej'
SUBJECT = 'Does attachment send?'
BODY = """
In this mail we are testing to send message
along with attachments

Regards,
Fahad
"""

# create the message object
msg = message.Message()
msg.add_header('from', FROM)
msg.add_header('to', TO)
msg.add_header('subject', SUBJECT)
msg.set_payload(BODY)

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
# server.sendmail(FROM, TO, BODY)
server.send_message(msg, FROM, [TO])
server.quit()

print("Mail Sent!!")