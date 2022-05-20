"""
Append to JSON file using Python:
"""

import json

x = '{ "organization":"IT",' \
    '"city":"Noida",' \
    '"country":"India"' \
    '}'

y = {"pin": 110096}
z = json.loads(x)
z.update(y)
x = json.dumps(z)
print(x)


def write_json(new_data, filename='Employee.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)


if __name__ == '__main__':
    # python object to be appended
    y = {"emp_name": "Henry", "emp_id": 18, "department": "Technical"}
    write_json(y)
