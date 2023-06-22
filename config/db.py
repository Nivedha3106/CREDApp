from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv('/Users/nivedha/Documents/CREDApp/.env')

MongoConn = os.getenv('connection')
client = MongoClient(MongoConn)
conn = client['webApp']

if 'webApp' in client.list_database_names():
    print("MongoDB is connected!")
else:
    print("MongoDB connection failed!")