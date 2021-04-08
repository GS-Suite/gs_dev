import random
import string


async def generate_message_code():
    N = 15
    gen_code = ''.join(random.choices(string.ascii_uppercase +
                                      string.digits +
                                      string.ascii_lowercase,
                                      k=N))
    return gen_code