from user.models import get_user_by_uid
from uuid import uuid4
import bcrypt


def hash_password(password):
    return bcrypt.hashpw(
        password.encode("utf-8"), 
        bcrypt.gensalt()
    ).decode("utf-8")


def check_password(password, hashed):
    #print(password.encode("utf-8"))
    #print(hashed.encode("utf-8"))
    return bcrypt.checkpw(
        password.encode("utf-8"), 
        hashed.encode("utf-8")
    )


async def generate_uid():
    gen = str(uuid4())
    while await get_user_by_uid(gen):
        gen = str(uuid4())
    #print(gen)
    return gen


async def user_object_response(user):
    return {
        "uid": user.uid,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email
    }