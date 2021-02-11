from bson.objectid import ObjectId
from dotenv import load_dotenv
import pymongo
import os

load_dotenv()

connection = pymongo.MongoClient(os.getenv("MONGO_DB_URL"))
mongodb = connection["Enrolled"]