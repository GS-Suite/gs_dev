from classrooms.models import get_classroom_by_uid
from uuid import uuid4


async def generate_uid():
    gen = str(uuid4())
    while await get_classroom_by_uid(gen):
        gen = str(uuid4())
    print(gen)
    return gen

async def get_user_role(user_id, classroom_id):
    return "teacher"
    return "student"
    return False