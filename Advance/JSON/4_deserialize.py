"""
Deserialize/Decode:
    JSON to Python Object
    Decoding JSON data into native data type.
"""

import json


data = '{"Name" : "Romy", "Gender" : "F"}'
print("DataType:", type(data))
data = json.loads(data)  # deserializing the data
print("DataType:", type(data))


with open('Employee.json', ) as f:
    print("DataType:", type(f))
    data = json.load(f)  # deserializing the data
    print("DataType:", type(data))
