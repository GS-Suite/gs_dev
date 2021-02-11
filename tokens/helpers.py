from tokens.models import get_token_by_value
import secrets


async def generate_token():
    gen = secrets.token_hex(32)
    while await get_token_by_value(gen):
        gen = secrets.token_hex(32)
    #print(gen)
    return str(gen)
