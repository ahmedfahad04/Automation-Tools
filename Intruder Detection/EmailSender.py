import argparse
import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename


class EmailSender:
    
    def __init__(self, from_email, to_email, subject, body, attachment_file):
        self.from_email = from_email
        self.to_email = to_email
        self.subject = subject
        self.body = body
        self.attachment_file = attachment_file
        
        # Use get() to avoid KeyError
        self.password = os.environ.get('intruder')

    def create_message(self):
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = self.to_email
        msg['Subject'] = self.subject
        body = MIMEText(self.body, 'plain')
        msg.attach(body)

        # add attachment
        filename = self.attachment_file
        with open(filename, 'rb') as f:
            attachment = MIMEApplication(f.read(), Name=basename(filename))
            attachment['Content-Disposition'] = 'attachment; filename="{}"'.format(
                basename(filename))
            msg.attach(attachment)

        return msg

    def send_mail(self):
        msg = self.create_message()

        # 1. start the server
        server = smtplib.SMTP('smtp.gmail.com', 587)

        # 2. smtp server setup
        status_code, response = server.ehlo()
        print(f'[*] Echoing the server: {status_code} {response}')

        # 3. setting the secured TLS connection
        status_code, response = server.starttls()
        print(f'[*] Starting TLS server: {status_code} {response}')

        # 4. login to sender's mail
        status_code, response = server.login(self.from_email, self.password)
        print(f'[*] Logging in...: {status_code} {response}')

        # 5. sending mail
        server.send_message(msg, self.from_email, [self.to_email])
        server.quit()

        print("Mail Sent!!")


if __name__ == "__main__":

    # as argument
    parser = argparse.ArgumentParser(description="Send email with attachment.")
    parser.add_argument("--file", required=True, help="Attachment file name")

    # hard coded
    from_email = 'buzzsky786@gmail.com'
    to_email = 'ahmedfahad3596@gmail.com'
    subject = 'Does attachment send?'
    body = '''In this mail we are testing to send a message
        along with attachments

        Regards,
        Fahad
        '''

    args = parser.parse_args()

    email_sender = EmailSender(
        from_email=from_email,
        to_email=to_email,
        subject=subject,
        body=body,
        attachment_file=args.file
    )

    email_sender.send_mail()
