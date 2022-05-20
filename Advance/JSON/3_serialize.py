"""
Serialize/Encode:
    Python Object to JSON.
    Encoding naive data type to JSON format.

    Transaction:
    dict -> object
    list, tuple -> array
    str -> string
    int, float -> number
    True -> true| False -> false| None -> null
"""

import json

data = {
    "user": {
        "name": "Emma Queens",
        "age": 21,
        "Nation": "USA"
    }
}

# Serializing json
res = json.dumps(data)
print("Type:", type(res), '||', res)

# Serializing json and writing json file
with open("Temp.json", "w") as write:
    json.dump(data, write)
