from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import smtplib
import os


load_dotenv()

VERIFY_URL = os.getenv("VERIFY_EMAIL_URL")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

async def send_verify_mail(receiver, token):
    try:
        mail_content = f'''
        <html>
            <h1>Welcome to GS Suite!</h1>
            <h3>
                <p>
                    Your account has been created successfully.
                    <br>
                    Click the link below to verify your email.
                </p>
            </h3>
            
            <hr>

            <a href="{VERIFY_URL}?token={token}">{VERIFY_URL}?token={token}</a>

            <hr>
            
            <p>
                The Devs,
                <br>
                GS Suite.
            </p>
        </html>
        '''

        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = SENDER_EMAIL
        message['To'] = receiver
        message['Subject'] = 'GS-Suite | Verify your Account'   #The subject line

        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'html'))

        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(SENDER_EMAIL, SENDER_PASSWORD) #login with mail_id and password
        
        session.sendmail(SENDER_EMAIL, receiver, message.as_string())
        
        session.quit()
        return True

    except Exception as e:
        print(e)
        return False
