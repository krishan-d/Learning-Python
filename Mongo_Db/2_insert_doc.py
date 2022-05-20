from pymongo import MongoClient

c = MongoClient("mongodb://localhost:27017")

db = c['pydb']
co = db['customer']

# insert_one():
d = {'isRetailCustomer': 0, 'incorporationName': 'IT', 'incorporationCity': 'noida'}
x = co.insert_one(d)
print("_id:", x.inserted_id)

# insert_many():
nList = [{'isRetailCustomer': 1, 'name': 'Noah', 'dob': 10/10/2000, 'address': 'noida'},
         {'isRetailCustomer': 1, 'name': 'Edwina', 'dob': 25/10/2002, 'address': 'mumbai'},
         {'isRetailCustomer': 1, 'name': 'Eve', 'dob': 2/12/1998, 'address': 'jaipur'}]

z = co.insert_many(nList)
print("_ids:", z.inserted_ids)

# important: _id can be provided while inserting.

c.close()
