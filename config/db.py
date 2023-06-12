from pymongo import MongoClient

conn = MongoClient("mongodb+srv://test:<password>@atlascluster.yfvzxy0.mongodb.net/?retryWrites=true&w=majority")

if 'webApp' in conn.list_database_names():
    print("MongoDB is connected!")
else:
    print("MongoDB connection failed!")