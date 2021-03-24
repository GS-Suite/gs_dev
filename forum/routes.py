from responses.standard_response_body import StandardResponseBody
from starlette.status import HTTP_200_OK

from tokens import controllers as token_controllers
from fastapi import status


async def create_forum(classroom_uid, token):
    '''
        1. Validate token
        2. Check if user_id is classroom owner
        3. Check if classroom already exits, if true, return forum id, name, 'Already created for your classroom'
            message
        4. Create forum if does not exist, return forum id, name, 'Forum created' message
    '''