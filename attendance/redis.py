from db_setup.redis_setup import REDIS_CONN as RED


def set_token(token, classroom_uid, timeout):
    x = RED.set(token, classroom_uid, ex = timeout)
    return x


def get_token(token):
    x = RED.get(token)
    return x


def delete_token(token):
    x = RED.delete(token)
    print(x)
    return x