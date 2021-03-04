from tokens import controllers as token_controllers
from user import helpers as user_helpers
from user import models as user_models
from fastapi import status

from user import mongo


async def sign_up(user):
    check = await user_models.get_user_by_username(user.username)
    if check == None:
        user.password = user_helpers.hash_password(user.password)
        uid = await user_helpers.generate_uid()
        #print(user, uid)
        res = await user_models.create_user(user, uid)
        if res:
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
            '''delete tokens'''
            await token_controllers.delete_user_tokens(user.uid)
            
            ''' delete other data'''

            '''delete user'''
            await user_models.delete_user(user)
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
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "email": user.email
        }
    return False