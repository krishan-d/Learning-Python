from pymongo import MongoClient

# run mongodb service using cmd. >mongod

# client = MongoClient(host="127.0.0.1", port=27017)
client = MongoClient("mongodb://localhost:27017")
print(client)

print(client.list_database_names())

# db = client['content']
db = client.content
print(db)

client.close()
