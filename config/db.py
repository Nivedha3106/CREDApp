from pymongo import MongoClient
# from dotenv import load_dotenv
# import os

# load_dotenv('/Users/nivedha/Documents/CREDApp/.env')

# MongoConn = os.getenv('connection')
# conn = MongoClient(MongoConn)
# client = conn['webApp']

conn = MongoClient("mongodb+srv://test:test@atlascluster.yfvzxy0.mongodb.net/")

if 'webApp' in conn.list_database_names():
    print("MongoDB is connected!")
else:
    print("MongoDB connection failed!")