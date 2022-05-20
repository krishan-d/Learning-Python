"""
JSON: JavaScript Object Notation
"""
import json
import demjson3 as dem

# A script(executable) file which is made of text in a programming language, is used to store and transfer data.

json_var = """
{
    "Country": {
        "name": "INDIA",
        "Languages_spoken": [
            {
                "names": ["Hindi", "English", "Bengali", "Telugu"]
            }
        ]
    }
}
"""
var = json.loads(json_var)
print(var)

# demjson3.encode(obj, nest_level=0):
# Convert python into a JSON string representation.
var = [{"Math": 50, "physics": 60, "Chemistry": 70}]
print(dem.encode(var))

# demjson3.decode(obj):
# convert the JSON object into python-format type.
var = '{"a":0, "b":1, "c":2, "d":3, "e":4}'
text = dem.decode(var)
print(text)
