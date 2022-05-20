from pymongo import MongoClient

c = MongoClient("mongodb://localhost:27017")
print(c)
db0 = c['pythondb']  # db = c.pydb
print(db0)

# Important :
# In MongoDB, a database is not created until it gets content(collection and documents)!
# In MongoDB, a collection is not created until it gets content!

new_co0 = db0['customer']
print(new_co0)
print(c.list_database_names())

db = c['pydb']
new_co = db['person']

# d = {'name': 'Edwina', 'gender': 'F', 'profession': 'manager'}
# new_co.insert_one(d, comment='Inserting same data again!')

d = {'name': 'Noah', 'gender': 'm'}
x = new_co.insert_one(d, comment='Inserting new data!')

print("_id:", x.inserted_id)
print(c.list_database_names())

# delete:
query = {"name": "Noah"}
new_co.delete_one(query)

q = {"name": {"$regex": "^E"}}
new_co.delete_many(q)

# drop collection:
# new_co.drop()

c.close()
