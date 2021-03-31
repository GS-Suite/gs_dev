from db_setup.redis_setup import REDIS_CONN as RED


async def set_token(token, email, ex = 60 * 60 * 24):
    x = RED.set(token, email, ex = ex)
    return x


async def get_token(token):
    x = RED.get(token)
    if x:
        return x.decode("utf-8")
    return x


async def delete_token(token):
    x = RED.delete(token)
    return x