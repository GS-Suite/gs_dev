from dotenv import load_dotenv
import redis
import os

load_dotenv()


'''
        LISTEN UP

        # default = 86400



    # t = 3
    r = redis.Redis(blah blah blah)

    ex -> seconds
    px -> milliseconds

    # r.set('uid', 'b2hj430', ex=t)

    # print(r.get("uid"))

    # time.sleep(2)
    r.flushall()
    # r.delete("uid")
    print(r.get("uid"))

    ttl -> time to live
    # print(r.ttl("uid"))


'''

REDIS_CONN = redis.Redis(host=os.getenv("REDIS_URL"), password=os.getenv("REDIS_PORT"), port=os.getenv("REDIS_PORT"))