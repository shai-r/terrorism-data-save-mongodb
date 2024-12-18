import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(verbose=True)

client = MongoClient(os.environ['MONGO_URL'])
db = client[os.environ['TERRORISM_DATA']]
terrorism_collection = db['terrorism_events']

def restart_mongo():
    db.drop_collection('terrorism_events')
    db.create_collection('terrorism_events')