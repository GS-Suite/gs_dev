from mail import helpers as mail_helpers
import os


async def verify_email_message_body(user, url, token_value):
    return f'''
        <html>
            <body>
                <h3>GS-Suite | Verify your email<u></h3>
                <p>Hi {user.first_name} {user.last_name}!</p>
                <p>Your account with username <b>{user.username}</b> has been created successfully!</p>
                <p>Verify your email by clicking on the button below.<p>
                <a href="{url}?token={token_value}">
                    <button>Verify Email</button>
                </a>
                <p>or, just click on the link below to verify your account</p>
                <a href="{url}?token={token_value}">
                    {url}?token={token_value}
                </a>
            <body>
        <html>
    '''


async def send_verify_email_mail(user, url, token_value, bg):
    bg.add_task(
        mail_helpers.send_email,
        user.email,
        "Verify your email",
        await verify_email_message_body(user, url, token_value)
    )
    return True