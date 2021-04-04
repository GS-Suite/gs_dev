from mail import helpers as mail_helpers
import random
import string

async def announcement_email(user, creator_info, classroom_info, email_struc):
    return f'''
            <html>
                <body>
                    <h3>GS-Suite | Announcements<u></h3>
                    <p>Hi {user['first_name']} {user['last_name']}!</p>
                    <p>{creator_info.username}, posted an announcement on {classroom_info.name}</p>
                    <p>The following is the announcement<p>
                    <br>

                    <hr>
                        <p>{email_struc['announcement']}</p>
                        <br>
                        <p>Date & Time: {email_struc['datetime']}</p>
                    </hr>

                    <br>
                    <p>For more info, visit our app!</p>
                    <br>
                    <p>Regards, GS-Suite Devs, 2021.</p>
                <body>
            <html>
        '''


async def send_bulk(enrolled_mailing_list, subject, creator_info, classroom_info, email_struc):
    for user in enrolled_mailing_list:
        await mail_helpers.send_email(
            receiver_email= user['email'],
            subject = subject,
            html = await announcement_email(
                user = user,
                creator_info = creator_info, 
                classroom_info = classroom_info,
                email_struc =  email_struc
            )
        )


async def send_announcement_email(enrolled_mailing_list, creator_info, classroom_info, email_struc, bg):
    bg.add_task(
        send_bulk,
        enrolled_mailing_list = enrolled_mailing_list,
        subject = 'Announcement from ' + classroom_info.name,
        creator_info = creator_info,
        classroom_info = classroom_info,
        email_struc = email_struc
    )
    return True


def generate_message_code():
    N = 15
    gen_code = ''.join(random.choices(string.ascii_uppercase +
                                      string.digits +
                                      string.ascii_lowercase,
                                      k=N))
    return gen_code
