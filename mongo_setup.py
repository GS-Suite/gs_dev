from bson.objectid import ObjectId
from dotenv import load_dotenv
import pymongo
import os

load_dotenv()

Mongo_CONN = pymongo.MongoClient(os.getenv("MONGO_DB_URL"))
