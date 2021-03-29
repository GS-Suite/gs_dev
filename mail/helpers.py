from email.mime.multipart import MIMEMultipart
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from email.mime.text import MIMEText
from dotenv import load_dotenv
import smtplib
import os


load_dotenv()


conf = ConnectionConfig(
    MAIL_USERNAME = os.getenv("SENDER_EMAIL"),
    MAIL_PASSWORD = os.getenv("SENDER_PASSWORD"),
    MAIL_FROM = os.getenv("SENDER_EMAIL"),
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_TLS = True,
    MAIL_SSL = False
)

VERIFY_URL = os.getenv("VERIFY_EMAIL_URL")

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

        message = MessageSchema(
            subject = "Verify your email",
            recipients = [receiver],  # List of recipients, as many as you can pass 
            body = mail_content,
            subtype = "html"
        )

        fm = FastMail(conf)
        await fm.send_message(message)

        return True

    except Exception as e:
        print(e)
        return False
