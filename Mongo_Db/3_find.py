import datetime

from pymongo import MongoClient

c = MongoClient("mongodb://localhost:27017")

db = c['pydb']
co = db['customer']

# Find one:
print(co.find_one())
print(co.find_one({'name': 'Edwina'}))


# Find all:
print('\n')
for x in co.find(): print(x)

print('\n')
query = {'isRetailCustomer': 1, 'name': 'Noah'}
z = co.find(query)
print(z.next())

z = co.find({'isRetailCustomer': 0})
print(z.next())

print('\n')
query = {'dob': {'$gt': datetime.datetime(2000, 1, 1)}}
dc = co.find(query)
for x in dc: print(x)

# Regular Expression Filter:
for x in co.find({'address': {'$regex': '^n'}}): print(x)


# Sorting:
print('\nSorting:')
for x in co.find().sort('name'): print(x)
print('\nSort Ascending:')
for x in co.find().sort('name', 1): print(x)
print('\nSort Descending:')
for x in co.find().sort('name', -1): print(x)


# Limit:
print('\n')
for x in co.find().limit(2): print(x)

c.close()
