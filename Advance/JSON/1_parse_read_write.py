"""
Read, Write and Parse JSON:
"""

import json

# Parse JSON :
# JSON To Python Dictionary.
json_string = '{"id":"09", "name": "Noah", "department":"Finance"}'
emp_dict = json.loads(json_string)
print(emp_dict)
print(emp_dict['name'])


# Reading JSON File:
# json.load(file_object): read file which contains a json object.
with open('Employee.json', ) as f:
    data = json.load(f)  # dictionary
    for i in data['emp_details']:
        print(i)


# Python Object To JSON:

# json.dumps(dict, indent)
# indent: number of units for indentation.
dictionary = {"id": "04", "name": "Ira", "department": "HR"}
json_object = json.dumps(dictionary, indent=4)  # serializing json
print(json_object)


# Write JSON To File:
# json.dump(dict, file_pointer)
dictionary = {"name": "Abram", "id": 100, "cgpa": 8.6}
with open("New.json", "w") as f:
    json.dump(dictionary, f)
