import random
import string


def generate_attendance_code():
    N = 9
    gen_code = ''.join(random.choices(string.ascii_uppercase +
                                      string.digits +
                                      string.ascii_lowercase,
                                      k=N))
    return gen_code
