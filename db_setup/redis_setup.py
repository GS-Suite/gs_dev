from dotenv import load_dotenv
import redis
import os

load_dotenv()

REDIS_CONN = redis.Redis(host=os.getenv("REDIS_URL"), password=os.getenv("REDIS_PORT"), port=os.getenv("REDIS_PORT"))