from uuid import uuid4
from user.models import get_user_by_uid
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