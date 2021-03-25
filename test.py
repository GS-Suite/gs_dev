from time import sleep
from db_setup.redis_setup import REDIS_CONN
import json

print(REDIS_CONN)

x = {"code": "gjhfhgfhg"}
k = json.dumps(x)

#REDIS_CONN.set("test2", k, ex = 300)

p = REDIS_CONN.get("test2")
print(json.loads(p))

sleep(3)

print(REDIS_CONN.ttl("test2"))
