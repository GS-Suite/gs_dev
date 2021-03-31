from mail import helpers as mail_helpers
import os


async def reset_password_mail_body(user, url, token_value):
    return f'''
        <html>
            <body>
                <h3>GS-Suite | Reset your password<u></h3>
                <p>Hi {user.first_name} {user.last_name}!</p>
                <p>To reset your password for your account with username <b>{user.username}</b>, click the button below</p>
                <p>Note: This link is valid for one hour, after which you won't be able to reset your password using this link.<p>
                <a href="{url}?token={token_value}">
                    <button>Reset Password</button>
                </a>
                <p>or, just click on the link below to verify your account</p>
                <a href="{url}?token={token_value}">
                    {url}?token={token_value}
                </a>
            <body>
        <html>
    '''


async def send_reset_password_email_mail(user, url, token_value, bg):
    bg.add_task(
        mail_helpers.send_email,
        user.email,
        "Reset Password",
        await reset_password_mail_body(user, url, token_value)
    )
    return True