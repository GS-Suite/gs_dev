from sendgrid.helpers.mail import Mail, Email, To, Content
from sendgrid import SendGridAPIClient

from dotenv import load_dotenv
import os

load_dotenv()

SENDER_EMAIL = Email(os.getenv('SENDER_EMAIL'))

async def send_email(receiver_email, subject, html):

    message = Mail(
            from_email = SENDER_EMAIL,
            to_emails = To(receiver_email),
            subject = subject,
            html_content = Content("text/html", html)
        )

    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        #print(response.status_code)
        #print(response.body)
        #print(response.headers)
        return True

    except Exception as e:
        print(e.message)
        return False