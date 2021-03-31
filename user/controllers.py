from mail.reset_password_mail import send_reset_password_email_mail
from classrooms import controllers as classroom_controllers
from mail.verify_email_mail import send_verify_email_mail
from tokens import controllers as token_controllers
from user import dropbox as user_dropbox
from user import helpers as user_helpers
from user import models as user_models
from user import redis as user_redis


async def sign_up(user, url, bg):
    check = await user_models.get_user_by_username(user.username)
    if check == None:
        user.password = user_helpers.hash_password(user.password)
        uid = await user_helpers.generate_uid()
        #print(user, uid)
        res = await user_models.create_user(user, uid)
        if res:

            ### generate token
            token = await user_helpers.generate_verify_email_token()
            ### store in redis
            await user_redis.set_token(token, user.email)
            ''' EMAIL VALIDATION MAIL, USE SPARINGLY '''
            #await send_verify_email_mail(user, url, token, bg)
            return True
        else:
            return False
    return "exists"


async def sign_in(user):
    ''' get user '''
    res = await user_models.get_user_by_username(user.username)
    if res:
        ''' check password '''
        if user_helpers.check_password(user.password, res.password):
            token_value = await token_controllers.refresh_token(res.uid)
            return token_value
    return False


async def sign_out(token_value):
    await token_controllers.delete_token(token_value)


async def update_profile(uid, details):
    user = await user_models.get_user_by_uid(uid)
    if user:
        res = await user_models.update_profile(user, details)
        if res:
            return await user_helpers.user_object_response(user)
    return False


async def update_password(uid, password):
    user = await user_models.get_user_by_uid(uid)
    if user:
        if user_helpers.check_password(password.current_password, user.password):
            return await user_models.update_password(
                user,
                user_helpers.hash_password(password.new_password)
            )
        return "invalid_password"
    return False


async def delete_account(password, token):
    try:
        '''get user'''
        user = await user_models.get_user_by_uid(token.user_id)
        if user == None:
            return False

        '''check password'''
        print(password, user.password)
        if not user_helpers.check_password(password, user.password):
            return False
        else:
            ''' delete other data'''
            if await classroom_controllers.delete_user_classrooms(user.uid):
                '''delete tokens'''
                if await token_controllers.delete_user_tokens(user.uid):
                    '''delete user'''
                    if await user_models.delete_user(user):
                        return True

    except Exception as e:
        print(e)
        return False


async def get_user_dashboard(uid):
    #print(uid)
    ### get user from uid
    user = await user_models.get_user_for_dashboard(uid)
    if user:
        return {
            "uid": user.uid,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "email": user.email
        }
    return False

async def get_user_username(uid):
    user = await user_models.get_user_by_uid(uid)
    if user:
        return user.username
    return False


async def change_profile_picture(user_uid, picture):
    ### delete previous pictures
    await user_dropbox.delete_profile_pictures(user_uid)

    if picture != None:
        pic = picture.file.read()
        x = await user_dropbox.change_profile_picture(user_uid, pic, picture.filename)
        return x
    return "deleted"


async def verify_email(token):
    email = await user_redis.get_token(token)
    if email:
        res = await user_models.set_verified(email)
        if res:
            await user_redis.delete_token(token)
        return res 
    return False


async def send_reset_password(user, url, bg):
    ### generate token
    token = await user_helpers.generate_reset_password_token()

    ### store in redis
    if await user_redis.set_token(token, user.username, ex = 60 * 60):
        ### send email
        res = await send_reset_password_email_mail(user, url, token, bg)
        return res
    return False


async def get_user_from_email(username, email):
    return await user_models.get_user_by_email(username, email)


async def reset_password(reset):
    ### get email from token
    username = await user_redis.get_token(reset.token)
    #print(email, reset.email)
    if username:
        if reset.username == username:
            ### get user
            user = await user_models.get_user_by_username(username)
            if user:
                ### reset password
                res = await user_models.update_password(
                    user, 
                    user_helpers.hash_password(reset.password)
                )
                if res:
                    ### delete token
                    await user_redis.delete_token(reset.token)
                    
                    return True
        ### delete token
        await user_redis.delete_token(reset.token)
    return False