from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from dotenv import load_dotenv
import os

load_dotenv()


def send_email(receiver_email, subject, html):

    message = Mail(
            from_email=os.getenv('SENDER_EMAIL'),
            to_emails = receiver_email,
            subject = subject,
            html_content=html
        )

    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        print(e.message)