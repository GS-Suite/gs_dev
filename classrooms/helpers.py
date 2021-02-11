from classrooms.models import get_classroom_by_uid
from uuid import uuid4


async def generate_uid():
    gen = str(uuid4())
    while await get_classroom_by_uid(gen):
        gen = str(uuid4())
    print(gen)
    return gen